# 2026-04-27 - Overdelivery Principle

## Trigger
Sway corrected Aion after seeing a trend-scouter/draft-factory mindset that skipped hashtag refresh, source scraping, comment/thread hydration, FAL image generation, Airtable writes, and Zernio draft creation because the day was already over the 10-draft target.

## Decision
`10 Zernio-ready drafts/day` is now treated as the **minimum floor**, not the ceiling.

Aion should overdeliver intelligently:
- close the 10/day minimum first;
- after hitting 10, keep learning, scouting, hydrating, improving, and building backlog;
- create extra draft-only Zernio posts when quality is high and safety checks pass;
- stretch target: up to ~20/day when strong sources/assets exist;
- never lower quality or create filler just to increase count.

## New Default Question
After every target is reached, Aion must ask internally:
- What is the next step?
- What can we do more?
- What can improve trend probability?
- What can make tomorrow easier?
- What did we learn that should change the system?

## Valid Overdelivery
- hashtag refresh
- new source scraping
- comment/thread/reply hydration
- source-image analysis
- Airtable backlog/pipeline/experiment writes
- FAL image generation when quality source exists
- extra Zernio Creator Inbox drafts
- better Thai captions/descriptions
- new hooks and format tests
- free-resource funnel planning
- performance review and durable rule updates

## Safety Boundaries
Overdelivery must remain safe:
- no live publishing or scheduling without explicit approval;
- Zernio drafts only: `isDraft=true`, `tiktokSettings.draft=true`;
- no `publishNow`, no `scheduledFor`;
- duplicate guards stay active;
- source attribution stays internal;
- max 5 hashtags public;
- vision QA required for generated images;
- no low-quality filler.

## System Changes Made
- Updated Aion `SOUL.md` to treat stated goals as floors and keep asking what else can be done.
- Updated Hermes user memory: Aion should be overdelivering.
- Patched `apify-ai-signal-radar` skill to replace the old stop-at-10 rule.
- Updated distributed draft factory cron `04e890514b13`.
- Updated evening catch-up cron `049d2b9987ed`.
- Created overdelivery scout/backlog cron `4297f1fb331a`, every 180m, delivered to `#trend-scouter`.
- Triggered the overdelivery scout immediately.
