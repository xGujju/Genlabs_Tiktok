#!/usr/bin/env python3
"""Generate a STAGED cutover for the Hermes cron config.

This script does NOT touch the live ~/.hermes/cron/jobs.json. It produces
a candidate `jobs.staged.json` plus a human-readable diff so Sway can
review before applying. Apply is a separate manual motion.

Mutations produced:

  1. Pause Apify cron `49635741c14a` (already paused, just stays paused).
  2. Strip the "Prioritize ChatGPT and NotebookLM" priority text from the
     hourly factory cron `a97a7703af32` and the daily review cron
     `717b2450e89d`. Replace with avatar-rotation language and an
     explicit candidates-queue-first selection rule.
  3. Add three NEW crons: x-discover (2h), voice-listen (4h), idea-mint
     (2h offset 1h). All disabled by default so they require explicit
     enable.
  4. Leave analytics import, breakout watch, and Zernio crons untouched.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

JOBS_LIVE_PATH = Path("/home/clawd/.hermes/cron/jobs.json")
STAGE_DIR = Path("/home/clawd/.hermes/genlabs_state/staged_cutover")
STAGE_JOBS = STAGE_DIR / "jobs.staged.json"
STAGE_DIFF = STAGE_DIR / "diff.txt"


HOURLY_FACTORY_PROMPT_NEW = """\
CONTEXT: You are Aion operating Sway's GenLabs AI Learning hourly Zernio draft factory.
Sway publishes manually; never publish live. The factory consumes the avatar-aware
candidates queue produced by genlabs-idea-mint. Selection priority and tool emphasis
are now DERIVED FROM AVATAR FIT + NOVELTY, not hardcoded tools.

NON-NEGOTIABLE SAFETY:
- Zernio output must be draft-only/review-only.
- Never send publishNow=true.
- Never intentionally schedule live publication.
- TikTok must use tiktokSettings.draft=true.
- Facebook/Instagram first comments must use platforms[].platformSpecificData.firstComment when included.
- Preserve duplicate guards and source traceability.

TASK:
1. Work from /home/clawd/.hermes/hermes-agent using the venv.
2. Read the top candidate from /home/clawd/.hermes/genlabs_state/candidates_queue.jsonl.
   If the queue is empty or stale (>4h old), report a soft warning and stop;
   do NOT fall back to legacy ChatGPT/NotebookLM evergreen content.
3. Verify the candidate's novelty is still valid (re-check the cooldown DB).
   If it is now blocked, drop it and take the next candidate.
4. Build a Thai carousel for the candidate using its avatar's voice register,
   locked phrases, hook-frame affinity, and format affinity. Honor the variety
   rules from config/avatars/_index.yaml: max 2 posts per avatar per day,
   max 3 posts per format per day, max 1 post per primary tool per day.
5. Run vision QA on hook + middle + CTA slides before declaring ready.
6. Send to Zernio as draft.
7. Final Discord output: status, draft ID, avatar, hook, format, primary tool,
   final score, novelty hook_j + containment, blocker if any, next action.
   Never dump raw JSON, secrets, full payloads, or stack traces.
"""


DAILY_REVIEW_PROMPT_NEW = """\
CONTEXT: You are the daily GenLabs self-improvement analyst. Goal: increase
qualified-SME-owner reach for GenLabs AI Learning and improve the avatar-led
content engine. Use genlabs_airtable_snapshot.py and the cooldown DB as
machine evidence. Do NOT pre-decide that any one tool is the winning topic.

TASK: Diagnose what worked, what failed, and what Aion should change.
Output concise sections:
  1. KPI/status (views, qualified-DM rate, follower growth)
  2. Strongest avatar this week (with evidence)
  3. Weakest avatar this week (with evidence)
  4. Strongest format / hook frame this week
  5. Weakest format / hook frame this week
  6. One concrete next-week experiment (avatar × format × hook frame)
  7. One system fix (engine bug, broken well, missing skill)

Drift warnings:
- If you find yourself recommending "more ChatGPT/NotebookLM tips", stop:
  that is the failure mode of the old system. Recommend by avatar+pain.
- If 0 candidates were minted today, the problem is upstream (discovery)
  not downstream (production). Direct the fix to the discovery wells.
"""


def load_live_jobs() -> dict:
    if not JOBS_LIVE_PATH.exists():
        raise FileNotFoundError(f"live jobs file not found: {JOBS_LIVE_PATH}")
    return json.loads(JOBS_LIVE_PATH.read_text(encoding="utf-8"))


def find_job(jobs: list[dict], job_id: str) -> dict | None:
    for j in jobs:
        if j.get("id") == job_id:
            return j
    return None


def stage_mutations(live: dict) -> tuple[dict, list[str]]:
    """Return (staged_config, list_of_changes_description)."""
    staged = copy.deepcopy(live)
    jobs: list[dict] = staged.get("jobs", [])
    changes: list[str] = []

    # 1. Apify radar — make sure it stays paused, and note the reason.
    apify = find_job(jobs, "49635741c14a")
    if apify is not None:
        apify["enabled"] = False
        apify["state"] = "paused"
        apify["paused_at"] = apify.get("paused_at") or datetime.now(timezone.utc).isoformat()
        apify["paused_reason"] = "Replaced by genlabs-x-discover (cutover 2026-05-W3)."
        changes.append("[PATCH] 49635741c14a (Apify radar) — paused with new reason.")

    # 2. Hourly factory — replace prompt + swap skill order.
    factory = find_job(jobs, "a97a7703af32")
    if factory is not None:
        factory["prompt"] = HOURLY_FACTORY_PROMPT_NEW
        skills = factory.get("skills") or []
        # Replace apify-ai-signal-radar with genlabs-idea-mint as primary.
        new_skills: list[str] = []
        for s in skills:
            if s == "apify-ai-signal-radar":
                new_skills.append("genlabs-idea-mint")
            else:
                new_skills.append(s)
        if "genlabs-idea-mint" not in new_skills:
            new_skills.insert(0, "genlabs-idea-mint")
        factory["skills"] = new_skills
        factory["skill"] = new_skills[0]
        changes.append("[PATCH] a97a7703af32 (hourly factory) — prompt rewritten; primary skill → genlabs-idea-mint.")

    # 3. Daily review — replace prompt.
    review = find_job(jobs, "717b2450e89d")
    if review is not None:
        review["prompt"] = DAILY_REVIEW_PROMPT_NEW
        skills = review.get("skills") or []
        new_skills = [s for s in skills if s != "apify-ai-signal-radar"]
        if "genlabs-nightly-learning" not in new_skills:
            new_skills.insert(0, "genlabs-nightly-learning")
        review["skills"] = new_skills
        review["skill"] = new_skills[0]
        changes.append("[PATCH] 717b2450e89d (daily review) — prompt rewritten; bias text removed.")

    # 4. NEW: x-discover cron (disabled by default).
    if not find_job(jobs, "genlabs-x-discover"):
        jobs.append({
            "id": "genlabs-x-discover",
            "name": "GenLabs X discover (native x_search)",
            "prompt": "Run skill `genlabs-x-discover`. Report a concise Discord summary.",
            "skills": ["genlabs-x-discover"],
            "skill": "genlabs-x-discover",
            "script": None,
            "schedule": {"kind": "interval", "minutes": 120, "display": "every 120m"},
            "schedule_display": "every 120m",
            "enabled": False,
            "state": "paused",
            "paused_reason": "New cron — Sway to enable manually after first manual dry-run.",
            "deliver": "discord:#trend-scouter",
        })
        changes.append("[ADD]   genlabs-x-discover — every 2h, DISABLED by default.")

    # 5. NEW: voice-listen cron (disabled by default).
    if not find_job(jobs, "genlabs-voice-listen"):
        jobs.append({
            "id": "genlabs-voice-listen",
            "name": "GenLabs Thai voice listen (Pantip + future FB)",
            "prompt": "Run skill `genlabs-voice-listen`. Report a concise Discord summary.",
            "skills": ["genlabs-voice-listen"],
            "skill": "genlabs-voice-listen",
            "script": None,
            "schedule": {"kind": "interval", "minutes": 240, "display": "every 240m"},
            "schedule_display": "every 240m",
            "enabled": False,
            "state": "paused",
            "paused_reason": "New cron — Sway to enable manually after first manual dry-run.",
            "deliver": "discord:#trend-scouter",
        })
        changes.append("[ADD]   genlabs-voice-listen — every 4h, DISABLED by default.")

    # 6. NEW: idea-mint cron (disabled by default).
    if not find_job(jobs, "genlabs-idea-mint"):
        jobs.append({
            "id": "genlabs-idea-mint",
            "name": "GenLabs idea mint (avatar-fit × novelty)",
            "prompt": "Run skill `genlabs-idea-mint`. Report a concise Discord summary.",
            "skills": ["genlabs-idea-mint"],
            "skill": "genlabs-idea-mint",
            "script": None,
            "schedule": {"kind": "interval", "minutes": 120, "display": "every 120m"},
            "schedule_display": "every 120m",
            "enabled": False,
            "state": "paused",
            "paused_reason": "New cron — Sway to enable manually after first manual dry-run.",
            "deliver": "discord:#trend-scouter",
        })
        changes.append("[ADD]   genlabs-idea-mint — every 2h, DISABLED by default.")

    return staged, changes


def write_stage(staged: dict, changes: list[str], live: dict) -> None:
    STAGE_DIR.mkdir(parents=True, exist_ok=True)
    STAGE_JOBS.write_text(json.dumps(staged, ensure_ascii=False, indent=2), encoding="utf-8")
    diff_lines = [
        "GenLabs cutover — staged changes",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Live source:   {JOBS_LIVE_PATH}",
        f"Staged target: {STAGE_JOBS}",
        "",
        "Changes:",
        *changes,
        "",
        f"Live job count:   {len(live.get('jobs', []))}",
        f"Staged job count: {len(staged.get('jobs', []))}",
        "",
        "To apply (after review):",
        "  1. Stop the Hermes gateway (or pause running crons).",
        "  2. Backup:  cp ~/.hermes/cron/jobs.json ~/.hermes/cron/jobs.backup.json",
        f"  3. Copy:    cp {STAGE_JOBS} ~/.hermes/cron/jobs.json",
        "  4. Restart the gateway.",
        "  5. Smoke-test the new crons manually before enabling them.",
        "",
        "To revert:  cp ~/.hermes/cron/jobs.backup.json ~/.hermes/cron/jobs.json",
    ]
    STAGE_DIFF.write_text("\n".join(diff_lines), encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser(description="Stage GenLabs cutover (no live changes)")
    p.add_argument("--live", type=Path, default=JOBS_LIVE_PATH)
    p.add_argument("--print-diff", action="store_true")
    args = p.parse_args()

    live = load_live_jobs()
    staged, changes = stage_mutations(live)
    write_stage(staged, changes, live)

    print(f"Staged: {STAGE_JOBS}")
    print(f"Diff:   {STAGE_DIFF}")
    print()
    print("\n".join(changes))
    if args.print_diff:
        print()
        print(STAGE_DIFF.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
