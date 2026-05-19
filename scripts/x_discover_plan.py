#!/usr/bin/env python3
"""Emit the X discovery search plan as JSONL.

Each line is one search query the caller should run via Hermes x_search.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from genlabs_engine.avatars import AvatarRegistry  # noqa: E402
from genlabs_engine.discovery.plan import build_x_queries, plan_summary  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description="Emit X-search plan as JSONL")
    p.add_argument("--min-likes", type=int, default=25)
    p.add_argument("--max-results", type=int, default=20)
    p.add_argument("--lookback-hours", type=int, default=72)
    p.add_argument("--avatar", action="append", help="filter to this avatar id (repeatable)")
    p.add_argument("--summary", action="store_true", help="print human summary instead of JSONL")
    args = p.parse_args()

    registry = AvatarRegistry.load()
    plan = build_x_queries(
        registry,
        min_likes=args.min_likes,
        max_results=args.max_results,
        lookback_hours=args.lookback_hours,
        avatar_filter=args.avatar,
    )

    if args.summary:
        print(f"X-search plan: {len(plan)} queries across {len(plan_summary(plan))} avatars")
        for aid, n in sorted(plan_summary(plan).items()):
            print(f"  {aid:30s}  {n} themes")
        return 0

    for q in plan:
        print(json.dumps(asdict(q), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
