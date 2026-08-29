#!/usr/bin/env python3
"""
Sends a Discord webhook message per newly-public post.

Usage:
    python3 scripts/notify_discord.py --posts new-posts.json --webhook-url "$DISCORD_WEBHOOK_URL"

Reads DISCORD_WEBHOOK_URL from the --webhook-url argument. If --posts is an
empty JSON array, does nothing (no request is sent).
"""
import argparse
import json
import sys
import urllib.request
from datetime import datetime


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
    if post.get("tags"):
        embed["footer"] = {"text": ", ".join(post["tags"])}
    return embed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--posts", required=True)
    ap.add_argument("--webhook-url", required=True)
    args = ap.parse_args()

    with open(args.posts, encoding="utf-8") as f:
        posts = json.load(f)

    if not posts:
        print("No new posts to announce.", file=sys.stderr)
        return

    for post in posts:
        payload = {
            "content": f"📝 New post published: **{post['title']}**",
            "embeds": [build_embed(post)],
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            args.webhook_url,
            data=data,
            headers={"Content-Type": "application/json"},
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
