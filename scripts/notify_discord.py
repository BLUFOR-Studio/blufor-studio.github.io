#!/usr/bin/env python3
"""
Sends a Discord webhook message per newly-public post.

Usage:
    python3 scripts/notify_discord.py --posts new-posts.json \
        --webhook-url "$DISCORD_WEBHOOK_URL" \
        --news-role-id "$DISCORD_NEWS_ROLE_ID" \
        --research-role-id "$DISCORD_RESEARCH_ROLE_ID"

Reads DISCORD_WEBHOOK_URL from the --webhook-url argument. If --posts is an
empty JSON array, does nothing (no request is sent).

Which ping a post gets is decided by its `tags` front matter:
    - "announcement"/"announcements"   -> @everyone
    - "update"/"updates"               -> the News role (--news-role-id)
    - "research"                       -> the Research role (--research-role-id)
    - anything else / no tags          -> no ping, just the plain message

A post can match more than one of these (e.g. tagged both "updates" and
"research") - in that case every matching ping is included. Role IDs are
Discord's numeric snowflake IDs, not the role's display name - see the
README note in the workflow file for how to find them. If a role ID isn't
supplied (left blank), that category's ping is just skipped, not an error.
"""
import argparse
import json
import sys
import urllib.request

ANNOUNCEMENT_TAGS = {"announcement", "announcements"}
UPDATE_TAGS = {"update", "updates"}
RESEARCH_TAGS = {"research"}


def build_content(post, news_role_id, research_role_id):
    tags = {t.lower() for t in (post.get("tags") or [])}
    pings = []

    if tags & ANNOUNCEMENT_TAGS:
        pings.append("@everyone")
    if tags & UPDATE_TAGS and news_role_id:
        pings.append(f"<@&{news_role_id}>")
    if tags & RESEARCH_TAGS and research_role_id:
        pings.append(f"<@&{research_role_id}>")

    prefix = " ".join(pings) + " " if pings else ""
    return f"{prefix}📝 New post published: **{post['title']}**"


def build_embed(post):
    embed = {
        "title": post["title"],
        "url": post["permalink"],
        "color": 0x5865F2,
        "timestamp": post["date"],
    }
    authors = post.get("authors") or []
    if authors:
        embed["author"] = {"name": ", ".join(authors)}
    if post.get("feature_url"):
        embed["image"] = {"url": post["feature_url"]}
    if post.get("tags"):
        embed["footer"] = {"text": ", ".join(post["tags"])}
    return embed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--posts", required=True)
    ap.add_argument("--webhook-url", required=True)
    ap.add_argument("--news-role-id", default="")
    ap.add_argument("--research-role-id", default="")
    args = ap.parse_args()

    with open(args.posts, encoding="utf-8") as f:
        posts = json.load(f)

    if not posts:
        print("No new posts to announce.", file=sys.stderr)
        return

    for post in posts:
        payload = {
            "content": build_content(post, args.news_role_id, args.research_role_id),
            "embeds": [build_embed(post)],
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            args.webhook_url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "blufor-studio-blog-notifier/1.0 (+https://blufor-studio.github.io/)",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req) as resp:
                print(f"Notified Discord for '{post['title']}': HTTP {resp.status}", file=sys.stderr)
        except Exception as e:
            # Don't fail the whole deploy just because the notification failed.
            print(f"Failed to notify Discord for '{post['title']}': {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
