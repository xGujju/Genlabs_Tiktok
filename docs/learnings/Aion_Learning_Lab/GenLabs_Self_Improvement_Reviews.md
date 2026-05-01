# GenLabs Self Improvement Reviews

## 2026-04-28 06:52 UTC — Draft-factory quality/pacing review
- KPI evidence: Airtable `Carousel Posts` has 4 records created today (UTC) and 4 Zernio-ready drafts (`Zernio Draft ID` present or `Zernio Draft Status=draft_created`) by 06:52 UTC. Linear pace for 10/day is about 2.9 by this time, so volume is ahead/on pace; quality still needs intervention.
- Bottleneck shifted: 2026-04-27 failures were mostly FAL HTTP 422/504 partial generations and Apify comment hydration limits. Current 2026-04-28 run created Zernio drafts, but the quality bottleneck is now generic draft templating. Recent manifests reused the same hook/title family (`workflow: เทรนด์นี้กำลังมา...`) and generic problem/CTA slides across different sources (`sig-21`, `sig-42`, `sig-44`, `sig-47`).
- Caption quality gap: Generated descriptions are ~1,100–1,400 characters, below the GenLabs rule of ~2,500–3,500 Thai characters for how-to/resource/workflow posts. These are likely too generic to maximize saves/follows even though they are technically Zernio-ready.
- Source/context gap: The source supply includes useful X workflow posts and official/course/privacy signals, but factory manifests do not show enough source-specific recovered resources, author follow-ups, repo/docs/prompt links, or concrete examples in the public descriptions. Hydration wins from 2026-04-27 (36 comments, 19 author follow-ups, two related resources) should become caption/slide substance when available; when Apify is blocked, mark links unavailable rather than replacing with a generic workflow template.
- Rule: Count a draft as operationally ready only after Zernio draft creation AND source-specific hook/slide/caption QA. A Zernio success with repeated generic copy should be considered “created but needs editorial review,” not proof the content engine is healthy.
- Next 24h focus: fix prompt/factory specificity before increasing volume; prioritize privacy/checklist, logo-animation workflow, and free AI Agents course topics because they have mass-audience Thai usefulness and clear save/share/resource angles.

## 2026-04-29 03:12 UTC — Hourly draft factory no-eligible-source check
- Draft factory command: `python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality medium --send-to-zernio` exited `status=ok` but `draft_count=0`, so no Airtable Carousel Post, manifest, media, or Zernio draft was created.
- Selector recount scanned 98 Canonical Signals and 38 Carousel Posts: `eligible_count=0`; blockers were `not_a_or_b_bucket=98`, `watch_for_more_corroboration=98`, `duplicate_existing_carousel_post=11`, and `no_educational_reasons=6`.
- Recovery scout run: `creator-claude-code-tips` collected 10 items and scored 10 candidates, but `a_tier=0`; top items remained C-bucket because they were single-source/uncorroborated or low velocity.
- Decision: do not fabricate a filler Zernio draft and do not loop more paid generation from this backlog. Next recovery should use stronger curated lanes: Sway-approved accounts, official first-party practical releases, or the YouTube practical workflow lane.



## 2026-04-29T04:25Z scheduled draft factory zero-draft recovery
- Ran exactly one Airtable-first hourly draft command: `python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality medium --send-to-zernio`.
- Result: `status=ok`, `draft_count=0`, `results=[]`; no carousel manifest, Airtable Carousel Posts record, or Zernio draft was created.
- Selector verification after recovery checked 98 Canonical Signals: 0 eligible; blocker counts: {'not_a_or_b_bucket': 98, 'watch_for_more_corroboration': 98, 'no_educational_reasons': 6, 'duplicate_existing_carousel_post': 11}.
- One narrow recovery scout ran `creator-ai-media-prompts` with `--query-limit 1 --max-items 10 --recent-days 2`; collection/scoring completed with staged `a_tier_count=0` and top candidates still C-bucket / Watch for more corroboration.
- Recovery decision: do not fabricate or force weak media-prompt/DM-gated X posts into Zernio. Next recovery should use the YouTube practical workflow lane or Sway-approved accounts, then only draft if source quality is A/B and educational.


## 2026-04-29T06:56Z daily self-improvement review — KPI behind, source/backlog bottleneck
- KPI evidence: Airtable `Carousel Posts` API returned 38 total records, 37 with `Zernio Draft Status=draft_created`; **0 records created on 2026-04-29 UTC**. The last confirmed draft-created record in Airtable was `yt-Q07rFZtc2Ao` at 2026-04-28T13:25Z. Current 10/day KPI is behind for the new UTC day.
- Hourly factory evidence: 03:10, 04:21, and 05:26 UTC runs all exited `status=ok` with `draft_count=0`, `results=[]`; no Airtable Carousel Post, manifest, media, or Zernio draft was created. Selector recounts showed 98 Canonical Signals, 0 eligible; blockers were `not_a_or_b_bucket=98`, `watch_for_more_corroboration=98`, `duplicate_existing_carousel_post=11`, `no_educational_reasons=6`.
- Recovery scout evidence: `creator-claude-code-tips`, `creator-ai-media-prompts`, and `creator-ai-coding-workflows` each collected/scored narrow slices but produced `a_tier=0`; do not keep looping paid draft attempts from these X lanes.
- Broad radar evidence: latest production scout/cleanup cron failed at collect with `subprocess.TimeoutExpired` after 600s, so cleanup/scoring did not run for that broad pass. Treat this as Apify/broad-collect reliability risk, but the hourly draft bottleneck is still source eligibility/backlog quality rather than Zernio.
- YouTube fallback QA finding: local planned manifests from 2026-04-29 around 06:41-06:46 UTC show practical business/AI-workflow topics, but public descriptions still contain raw source metadata (`YouTube title:`, `Channel:`, `Description:`) and slide objects have no concrete Thai `title`/`main_text` copy. These are not Zernio-ready and should be rejected before FAL/Zernio until template/source cleanup is fixed.
- Content quality priority: injected Airtable snapshot has stronger manual/source-grounded topics ready to promote or repair into drafts: OpenAI Privacy Filter safety checklist, GPT Image 2 + Seedance logo animation workflow with hydrated steps, and Google/Kaggle AI Agents course. Dedupe duplicate Google/Kaggle signals before drafting.
- Durable updates from this review: patched repo runbook `docs/superpowers/runbooks/ai-channel-radar.md`; patched Hermes skill `genlabs-carousel-copywriting`; Airtable Decision `recdTPLni9ZsGr4qP` records the YouTube fallback dry-run quality gate.
- Next 24h operating rule: if X selector is empty, switch to YouTube/Sway-approved/official practical lanes, but require cleaned source metadata, concrete Thai slide copy, max 5 Thai-first hashtags, long useful `tiktokSettings.description`, and Creator Inbox draft-only safety. No live publishing.


### 2026-04-29T07:03Z addendum — one YouTube draft created but needs editorial review
- A scheduled draft factory process that was still running during review completed at 2026-04-29T07:00Z. Latest state: `status=ok`, `apply=true`, `send_to_zernio=true`, `draft_count=1`, source `yt-fr78adfAnuA`, Airtable `recF9CeGJDbhCp9EE`, Zernio draft `69f1ac877deb182037d84b7e`, manifest `auto-20260429T064645Z-yt-fr78adfAnuA/manifest.json`.
- Airtable count updated: 1 draft-created Carousel Post on 2026-04-29 UTC; still behind 10/day pace.
- Safety verification: locally rebuilt outbound payload had `isDraft=true`, `tiktokSettings.draft=true`, 8 media assets, `content` length 90, no `publishNow`, and no outbound `scheduledFor`. Zernio GET returned `status=draft`, 8 media items; Zernio echoed `scheduledFor` as expected for draft UI semantics.
- Editorial QA: vision QA on hook/middle/CTA found readable GenLabs-style Thai sketchnote images with useful workflow examples, but public description still contains raw `YouTube title:` / `Channel:` / `Description:` metadata and manifest slide objects lacked concrete Thai slide-copy fields (`slides_with_missing_copy=8/8`). Treat this as a created draft that needs editorial review/polish, not a fully quality-cleared production win.


## 2026-04-29T09:43Z scheduled draft factory timeout — no current draft created
- Ran exactly one Airtable-first hourly draft command: `python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality medium --send-to-zernio`.
- Result: Hermes tool timed out after 600s. Post-run verification found no lingering `scheduled_ai_social_draft_factory.py`, `staged_ai_signal_radar.py`, or carousel-generation processes.
- Current-run partial asset folder: `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260429T093234Z-yt-Y3PcRp5RFzk` with `slide-1.png` through `slide-5.png`, but no `manifest.json`. The set is not publishable and was not sent to Zernio.
- `latest_social_draft_factory.json` remained stale from 2026-04-29T07:00Z (`yt-fr78adfAnuA`), so it is not current-run evidence.
- Airtable verification found no `Carousel Posts` record for `Source ID=yt-Y3PcRp5RFzk`; therefore no Airtable record ID, no Zernio Draft ID/status, and no current-run media count exists.
- Recovery decision: do not retry broad/live generation in this cron. Source `yt-Y3PcRp5RFzk` is practical AI automation, but prior/current attempts timeout before manifest; next recovery should repair/shorten YouTube fallback generation/copy sanitizer or publish only from a complete manifest after QA, preserving draft-only safety.


## 2026-04-29 11:36 UTC — Hourly Zernio draft factory failure
- Command: `python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality medium --send-to-zernio`
- Result: failed during live FAL GPT Image 2 generation with HTTP 500 before `manifest.json` was written and before Airtable/Zernio publish stage.
- Current source selected: `yt-Y3PcRp5RFzk`; partial folder: `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260429T113028Z-yt-Y3PcRp5RFzk` with `slide-1.png` to `slide-3.png` only.
- Verification: no Airtable `Carousel Posts` record found for `Source ID=yt-Y3PcRp5RFzk`; latest social draft factory state file remains stale from 2026-04-29T07:00:24Z (`yt-fr78adfAnuA`); no `scheduled_ai_social_draft_factory.py` process remained after failure.
- Decision: do not force a media-less Zernio draft and do not retry the same live generation inside this cron cycle; next recovery should retry a fresh high-quality source/generation pass or route through a complete manifest before Zernio.


## 2026-04-29 12:49 UTC — Hourly Zernio draft factory cron result
- Command run from `/home/clawd/.hermes/hermes-agent`: `python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality medium --send-to-zernio`
- Result: timed out after 600s during live FAL/image generation; stdout JSON was not produced.
- Current partial folder: `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260429T123815Z-yt-Y3PcRp5RFzk` with `slide-1.png` through `slide-5.png`, no `manifest.json`.
- Verification: `latest_social_draft_factory.json` is stale from 2026-04-29T07:00:24Z and must not be used as current-run evidence. Airtable `Carousel Posts` has no record for `Source ID=yt-Y3PcRp5RFzk`; therefore no Zernio draft was created for this run.
- Quality blocker: older planned manifest for the same source leaks source metadata (`YouTube title`, `Channel`, description/redirect fragments) and repeats fallback copy; do not force this source into Zernio until the YouTube/public-copy sanitizer and selector/generator are repaired.
- Recovery action: next recovery should avoid reselecting the same partial `yt-Y3PcRp5RFzk` path; use a cleaner YouTube practical workflow source or Sway-approved-account lane, and require manifest/public-caption QA before live image generation/Zernio.

## 2026-04-29 15:31 UTC — Hourly Zernio draft factory QA
- Ran one scheduled AI social draft factory cycle. Output source: `evergreen-chatgpt-custom-gpt-customer-support`; Airtable record `reczZWZMp6ZSMWg6o`; Zernio draft `69f223a02b14dce1de519fa0`; manifest `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260429T151622Z-evergreen-chatgpt-custom/manifest.json`.
- Safety verified from local payload: `isDraft=true`, `tiktokSettings.draft=true`, `publishNow` omitted, `scheduledFor` omitted; live Zernio GET returned `status=draft`, 8 media items, 0 publish attempts. Zernio echoed `scheduledFor`, consistent with known API behavior for drafts.
- Content value: practical Thai SME/customer-support workflow for Custom GPT + LINE OA; not a generic launch/news/funding post.
- QA learning: hook and action slides passed vision QA; middle checklist slide was readable and matched the workflow but had minor wording polish issues (`กำหนดช่องคำตอบ` would be clearer as `กำหนดโหมดคำตอบ`; `ห้ามสัญญา` could be `ห้ามรับปากเกินจริง`). Future generator copy should prefer natural Thai operational wording for support workflows before image generation.

## 2026-04-29T20:45Z hourly draft factory created but source-specific QA failed
- Command: `venv/bin/python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality medium --send-to-zernio` from `/home/clawd/.hermes/hermes-agent`.
- Result: `status=ok`, `draft_count=1`; source `evergreen-ai-competitor-research-marketing`; Airtable `recVzyh85hdR4F7eU`; Zernio draft `69f26cf54a69771aaa0ac3df`; manifest `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260429T203102Z-evergreen-ai-competitor-/manifest.json`.
- Safety verification: rebuilt outbound payload had `isDraft=true`, `tiktokSettings.draft=true`, 8 media assets, content length 63, 5 hashtags, no `publishNow`, and no outbound `scheduledFor`; live Zernio GET returned `status=draft` and 8 media items. Zernio echoed `scheduledFor`, consistent with known draft UI behavior.
- Editorial QA: hook and core prompt checklist slides were readable/useful Thai, but the manifest/source ID promises competitor-research/marketing while the generated lesson drifts into generic AI prompting and broad business use cases. Caption length is ~1.1K chars, below the preferred long educational caption depth for workflow posts. Treat this as draft-created but needing editorial review, not a fully quality-cleared KPI-ready post.
- Recovery/fix direction: patch the evergreen fallback/copy planner so source-specific seeds preserve the actual workflow (e.g. competitor matrix, offer/hook/channel gap analysis, non-copy positioning) through slides and long caption before creating more Zernio drafts from evergreen sources.

## 2026-04-30T00:46Z hourly Zernio draft factory run
- One draft-only Zernio carousel was created from `source_id=evergreen-ai-admin-document-summary`; Airtable `Carousel Posts` record `recSpu6FyhN6Zuern`, Zernio draft `69f2a657247bf556edd05b45`, manifest `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260430T003605Z-evergreen-ai-admin-docum/manifest.json`.
- Safety verification: locally rebuilt payload omitted `publishNow` and `scheduledFor`, used `isDraft=true`, `tiktokSettings.draft=true`, 8 media items, title/content length 82; live Zernio GET returned `status=draft` and 8 media items. Zernio echoed `scheduledFor`, but outbound payload was omission-safe.
- QA: hook/middle/action slides were square, readable, on-brand, no external URLs/handles/source metadata. Minor editorial polish opportunities: mixed English terms (`notes`, `action`, `follow-up`), an extra space in `ลองใช้ แบบนี้`, and the evergreen source label says admin document summary while the rendered lesson focuses on meeting-notes-to-action workflow. Treat as acceptable Creator Inbox draft but review wording before posting if possible.



## 2026-04-30T04:35:24.105545+00:00 — hourly Zernio draft factory timeout
- Command shape: `scheduled_ai_social_draft_factory.py --limit 1 --apply --quality medium --send-to-zernio`.
- Outcome: Hermes terminal timed out after 600s during live generation; no fresh `latest_social_draft_factory.json` was written.
- Evidence: partial folder `auto-20260430T042427Z-evergreen-chatgpt-email-` has 6 PNGs, no `manifest.json`; exact Airtable `Carousel Posts.Source ID=evergreen-chatgpt-email-inbox-triage` not found; no lingering `scheduled_ai_social_draft_factory.py` process.
- Blocker classification: FAL/image-generation timeout before publish stage, not Zernio publish failure.
- Next improvement: inspect why the evergreen email triage source times out repeatedly and avoid retry loops without a complete manifest.
