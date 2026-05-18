#!/usr/bin/env python3
"""CLI for the cooldown DB.

Examples:
    python scripts/cooldown_cli.py stats
    python scripts/cooldown_cli.py check --topic "ใช้ ChatGPT ตอบลูกค้า" --tool chatgpt --avatar jay-noi-salon-clinic
    python scripts/cooldown_cli.py repeated-hooks --limit 20
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))

from genlabs_engine.cooldown import CooldownDB  # noqa: E402


def cmd_stats(args: argparse.Namespace, db: CooldownDB) -> int:
    payload = {
        "total_posts": db.total_posts(),
        "posts_last_7d": db.posts_in_window(7),
        "posts_last_30d": db.posts_in_window(30),
        "by_source_type": db.posts_by_source_type(),
        "by_primary_tool": db.posts_by_primary_tool(),
        "today_variety": db.daily_counts(),
    }
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0


def cmd_check(args: argparse.Namespace, db: CooldownDB) -> int:
    result = db.check_novelty(
        topic=args.topic,
        hook=args.hook,
        primary_tool=args.tool,
        avatar_id=args.avatar,
        lookback_days=args.lookback_days,
        hook_block_threshold=args.hook_threshold,
        containment_block_threshold=args.containment_threshold,
    )
    json.dump(result.to_dict(), sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0 if result.is_novel else 1


def cmd_repeated_hooks(args: argparse.Namespace, db: CooldownDB) -> int:
    rows = db.top_repeated_hooks(limit=args.limit)
    for hook, count in rows:
        print(f"{count:3d}  {hook}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="GenLabs cooldown DB CLI")
    p.add_argument("--db", type=Path, default=None, help="DB path (default: $GENLABS_COOLDOWN_DB)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("stats", help="Print DB stats as JSON")
    s.set_defaults(func=cmd_stats)

    c = sub.add_parser("check", help="Check novelty of a candidate idea")
    c.add_argument("--topic", required=True, help="Topic / clean headline")
    c.add_argument("--hook", default=None, help="Hook slide thai_copy (default: --topic)")
    c.add_argument("--tool", default=None, help="Primary tool key (e.g. chatgpt, claude_code)")
    c.add_argument("--avatar", default=None, help="Avatar id (e.g. jay-noi-salon-clinic)")
    c.add_argument("--lookback-days", type=int, default=30)
    c.add_argument("--hook-threshold", type=float, default=0.35,
                   help="Block if hook_jaccard >= this (default 0.35)")
    c.add_argument("--containment-threshold", type=float, default=0.80,
                   help="Block if containment >= this (default 0.80)")
    c.set_defaults(func=cmd_check)

    r = sub.add_parser("repeated-hooks", help="Show hooks that appear multiple times")
    r.add_argument("--limit", type=int, default=15)
    r.set_defaults(func=cmd_repeated_hooks)

    args = p.parse_args()
    db = CooldownDB.open(args.db)
    try:
        return args.func(args, db)
    finally:
        db.close()


if __name__ == "__main__":
    sys.exit(main())
