#!/usr/bin/env python3
"""
Finds posts under content/posts/ that are now publicly live (draft = false
and their `date` is in the past) but haven't been notified about yet.

"Notified yet" is tracked in a small JSON state file (a list of permalinks),
persisted between CI runs via actions/cache. This makes the check idempotent
and independent of *how* the workflow was triggered: a post pushed live
right now, and a future-dated post whose scheduled date the daily cron just
caught up to, are both detected the same way - date has passed and it isn't
in the state file yet.

Usage:
    python3 scripts/find_new_posts.py \
        --content-dir content/posts \
        --authors-file data/en/authors.toml \
        --base-url https://blufor-studio.github.io/ \
        --state-file .cache/notified-posts.json \
        --out new-posts.json

Writes newly-detected posts as a JSON array to --out (empty array if none),
and updates --state-file in place so they aren't reported again next run.
"""
import argparse
import json
import sys
import tomllib
from datetime import datetime, timezone
from pathlib import Path


def parse_date(raw):
    if raw is None:
        return None
    s = str(raw).strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def load_front_matter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++"):
        return None
    end = text.find("\n+++", 3)
    if end == -1:
        return None
    raw_toml = text[3:end]
    return tomllib.loads(raw_toml)


def slug_for(path: Path, content_dir: Path):
    rel = path.relative_to(content_dir)
    if rel.name == "index.md":
        # Leaf bundle: content/posts/<slug>/index.md
        return rel.parent.as_posix()
    # Flat file: content/posts/<slug>.md
    return rel.with_suffix("").as_posix()


def load_authors(authors_file: Path):
    if not authors_file.exists():
        return {}
    return tomllib.loads(authors_file.read_text(encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--content-dir", required=True, type=Path)
    ap.add_argument("--authors-file", required=True, type=Path)
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--state-file", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    base_url = args.base_url.rstrip("/")
    now = datetime.now(timezone.utc)

    authors = load_authors(args.authors_file)

    if args.state_file.exists():
        notified = set(json.loads(args.state_file.read_text(encoding="utf-8")))
    else:
        notified = set()

    live_permalinks = set()
    new_posts = []

    for md_path in sorted(args.content_dir.rglob("*.md")):
        fm = load_front_matter(md_path)
        if not fm:
            continue
        if fm.get("draft", False):
            continue
        date = parse_date(fm.get("date"))
        if date is None or date > now:
            continue

        slug = slug_for(md_path, args.content_dir)
        permalink = f"{base_url}/posts/{slug}/"
        live_permalinks.add(permalink)

        if permalink in notified:
            continue

        author_names = []
        for author_id in fm.get("authors", []):
            entry = authors.get(author_id, {})
            author_names.append(entry.get("name", author_id))

        new_posts.append(
            {
                "title": fm.get("title", slug),
                "permalink": permalink,
                "date": date.isoformat(),
                "authors": author_names,
                "feature": fm.get("feature"),
                "tags": fm.get("tags", []),
            }
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(new_posts, indent=2), encoding="utf-8")

    # Only ever grows for permalinks we've actually seen live; safe to
    # persist the full live set each run.
    args.state_file.parent.mkdir(parents=True, exist_ok=True)
    args.state_file.write_text(
        json.dumps(sorted(notified | live_permalinks), indent=2), encoding="utf-8"
    )

    print(f"Found {len(new_posts)} newly-public post(s).", file=sys.stderr)


if __name__ == "__main__":
    main()
