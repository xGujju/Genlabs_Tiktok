## Current Zernio Growth Summary — 2026-05-25

### KPI status
- Goal: one TikTok post reaches **100,000 views**.
- Best post: ChatGPT 8 productivity tips for work: self-review, onboarding plan, project brief, feedback/action items
- Current views: 32,072
- Gap to 100,000: 67,928
- Shares: 429
- Snapshot/verification time: growth-check snapshot `2026-05-25T16:00:49.857735+00:00`; scheduled import `2026-05-25_16-02-50.md` / live Imported At `2026-05-25T16:01:33.176584+00:00`; comparison `2026-05-25T16:02:34.193851+00:00`; final growth readback `2026-05-25T16:13:46Z`; factory/process readback `2026-05-25T16:51:47Z`.

### Current signal
- Breakout state: **no_formal_breakout_current_baseline_below_threshold_movement_post_import_no_change**.
- Current best/closest watch: `7634027210248097042` at 32,072 views / 429 shares / +0 views / gap 67,928.
- Strongest early-velocity signal: `7641239648790007048` +3 to 1,890 views / 13 shares at the baseline, below threshold/watch-only; live import at `2026-05-25T16:01:33.176584+00:00` found 0 further movers.
- Candidate count: 0 formal candidates; 0 refresh-window candidates.
- Protected CTA: Post `7634027210248097042` is ChatGPT productivity/workflow evidence; protected CTA is promo copy only.

### Weak spots / blockers
- no_posts_in_last_72h
- issue-check `2026-05-25_13-18-39.md` errored/no response
- zernio_factory_source_lane_exhaustion_current_2026_05_25_1650
- active_experiment_result_closure_overdue_or_blocked
- prior Zernio POST 403/account-access blockers from 2026-05-24 09:12 and 17:54 remain separate
- prior editorial/source-topic QA blockers remain separate
- learning_loop_structured_performance_experiments_backfill_missing
- zero-metric/protected CTA guard remains active and clean

### Action / memory update
- Used the 16:00 normal baseline and live post-import read-only comparison: no formal breakout; below-threshold mover only; no amplification/generation/public posting/spend/Zernio send.
- Resolved the prior 14:30 import+breakout scheduler watch after breakout `2026-05-25_16-01-42.md` delivered and live Airtable import refreshed at `2026-05-25T16:01:33.176584+00:00` with 0 movers.
- Refreshed factory state with current manual exact+required-recovery readback `manual-exact-run+recovery-2026-05-25T16:50Z_current-cron-delivery-pending` (zero-draft/source-lane exhaustion), state token `latest_social_draft_factory.json@2026-05-25T16:50:37.858469+00:00`, next_run_at `2026-05-25T17:47:30.923195+00:00`, no Airtable/Zernio payload/manifest/media.
- Kept issue-check error `2026-05-25_13-18-39.md` open for retry/debug.

### Next action
- Feed fresh non-repeating practical Thai ChatGPT + NotebookLM software-tip/service-workflow source IDs into the factory.
- Backfill/close active experiment result loops before scaling more variants.
- Keep production cron enabled/draft-only; do not pause, spend, publish, or send to Zernio from this growth-check.

## 2026-05-25

<!-- ZG-DLOG-2026-05-25-1600-GROWTH-CHECK -->
### Growth-check 16:00 UTC — no formal breakout; live import no-change; readbacks normalized
- KPI: best `7634027210248097042` remains ChatGPT productivity/workflow evidence at 32,072 views / 429 shares / gap 67,928; protected CTA unsafe_count=0.
- Signal: baseline `2026-05-25T16:00:49.857735+00:00` had 0 candidates; `7641239648790007048` moved +3 to 1,890 views / 13 shares but stayed below threshold; live import `2026-05-25T16:01:33.176584+00:00` and comparison `2026-05-25T16:02:34.193851+00:00` found 0 further movers.
- Readbacks: breakout `2026-05-25_16-01-42.md` delivered no candidate; factory manual exact+required-recovery readback `manual-exact-run+recovery-2026-05-25T16:50Z_current-cron-delivery-pending` delivered zero-draft/source-lane exhaustion with state `latest_social_draft_factory.json@2026-05-25T16:50:37.858469+00:00` and next `2026-05-25T17:47:30.923195+00:00`; issue-check `2026-05-25_13-18-39.md` remains error/no-response; latest scheduled import markdown `2026-05-25_16-02-50.md` is separate from the live 16:01 import refresh.
- Action: resolved prior 14:30 import+breakout scheduler watch, kept below-threshold watch-only/no amplification, updated compact memory/tasks/Zernio Growth Memory/Open Loops/run log; no generation/public posting/spend/Zernio send.

<!-- ZG-DLOG-2026-05-25-1650-FACTORY-ZERO -->
### 2026-05-25 16:50 UTC — manual exact + required recovery zero-draft/source-lane readback current
- Command/readback: ran exactly `venv/bin/python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality low --send-to-zernio` from `/home/clawd/.hermes/hermes-agent`; initial 16:48 run and required 16:50 recovery rerun both exited `status=ok` with `draft_count=0/results=[]`. The openclaw.bash startup warning was unrelated.
- Verification: fresh state `latest_social_draft_factory.json@2026-05-25T16:50:37.858469+00:00`; no new `auto-*` folder/manifest/media after `2026-05-25T16:48:00Z`; no Airtable Carousel Posts row after `2026-05-25T16:48:00Z`; no outbound Zernio payload/draft/media; no lingering factory/radar process at `2026-05-25T16:51:47Z`. Zernio/platform verification is not applicable because no outbound payload/post exists.
- Diagnosis: source-lane exhaustion / anti-repetition guard saturation. Canonical 0/98 eligible (overlapping blockers: 12 exact-existing, 42 repeat-family, 12 no educational value, all 98 not A/B and watch-more); deterministic lanes exhausted: evergreen 0/42 (40 exact-existing, 8 partial quarantined, 42 repeat-family), AI Words 0/8 (6 exact-existing, 8 repeat-family), KPI backstop 0/8 for current hour (all repeat-family); 30 partial source IDs quarantined.
- Scheduler/action: production cron remains enabled/state scheduled with next_run_at `2026-05-25T17:47:30.923195+00:00`. Source-lane replenishment remains the active KPI blocker; Feed fresh non-repeating practical Thai ChatGPT + NotebookLM-first software-tip/service-industry sources; keep production cron enabled/draft-only and do not force weak repeats.

<!-- ZG-DLOG-2026-05-25-1518-FACTORY-ZERO -->
### Historical 2026-05-25 15:18 UTC — cron exact + required recovery zero-draft/source-lane readback superseded by 16:50 current readback
- Command/readback: ran exactly `venv/bin/python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality low --send-to-zernio` from `/home/clawd/.hermes/hermes-agent`; initial 15:15 run and required 15:18 recovery rerun both exited `status=ok` with `draft_count=0/results=[]`. The openclaw.bash startup warning was unrelated.
- Verification: historical 15:18 state (superseded by 16:50 current readback); latest auto folder remains `auto-20260524T174823Z-yt-3JmIhEIqxBM` from 2026-05-24, so no current-run manifest/media was created; no current Airtable Carousel Posts row/outbound Zernio payload; no Zernio draft; no lingering factory/radar process at `2026-05-25T15:24:06Z`. Zernio/platform verification is not applicable because no outbound payload/post exists.
- Diagnosis: source-lane exhaustion / anti-repetition guard saturation. Canonical Signals 0/98 eligible (overlapping blockers: 17 duplicate/partial, 32 repeat-family/duplicate, 12 no educational value, all 98 not A/B/watch); deterministic lanes exhausted (evergreen 0/42, AI Words 0/8, current-hour KPI backstop 0/8; 30 partial source IDs quarantined).
- Scheduler/action: production cron remains enabled/state scheduled with next_run_at `2026-05-25T17:47:30.923195+00:00`. Source-lane replenishment remains the active KPI blocker; feed fresh non-repeating practical Thai ChatGPT/NotebookLM-first software-tip/service-industry sources.

<!-- ZG-DLOG-2026-05-25-1414-GROWTH-CHECK -->
### Growth-check 14:14 UTC — no formal breakout; below-threshold import mover; readbacks current
- Evidence: normal baseline `2026-05-25T14:14:26.814370+00:00` found 0 breakout candidates; import `2026-05-25_14-16-31.md` / Imported At `2026-05-25T14:15:36.160299+00:00` plus read-only comparison `2026-05-25T14:25:31.383388+00:00` found only `7641239648790007048` +3 to 1890 views / 13 shares, below threshold.
- KPI: best `7634027210248097042` remains ChatGPT productivity/workflow evidence at 32,072 views / 429 shares / gap 67,928; protected CTA is promo only; CTA unsafe_count=0.
- Readbacks: breakout `2026-05-25_14-14-52.md` returned no candidate; factory current state `latest_social_draft_factory.json@2026-05-25T16:50:37.858469+00:00` delivered zero-draft/source-lane exhaustion and next `2026-05-25T17:47:30.923195+00:00`; experiment `2026-05-25_12-46-16.md` delivered; issue-check `2026-05-25_13-18-39.md` errored with `(No response generated)` and needs retry/debug; current growth-check report is in-flight until delivery.
- Action: resolved the earlier import+breakout scheduler watch, then opened exactly one new 14:30 import+breakout readback watch after final boundary wait; kept the mover watch-only/no amplification; updated compact memory/tasks/Zernio Growth Memory/Daily Log/Open Loops; no generation/public posting/spend/Zernio send.
- Scheduler watch: import/breakout 14:30 readbacks were not observed by `2026-05-25T14:58:12Z`; latest import `2026-05-25_14-16-31.md` and breakout `2026-05-25_14-14-52.md` remain the current completed files.

<!-- ZG-DLOG-2026-05-25-1357-FACTORY-ZERO -->
### Historical 2026-05-25 13:57 UTC — manual exact + required recovery zero-draft/source-lane readback superseded by 15:18 current readback
- Command/readback: ran exactly `venv/bin/python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality low --send-to-zernio` from `/home/clawd/.hermes/hermes-agent`; initial 13:49 run and required 13:57 recovery rerun both exited `status=ok` with `draft_count=0/results=[]`. The openclaw.bash startup warning was unrelated.
- Verification: historical 13:57 state, superseded first by the 15:18 zero-state and now by the 16:50 current readback; no new `auto-*` folder/manifest/media after `2026-05-25T13:49:24Z`, no current Airtable Carousel Posts row/outbound Zernio payload, no Zernio draft, and no lingering factory/radar process at `2026-05-25T14:01:58Z`. Zernio/platform verification is not applicable because no outbound payload/post exists.
- Diagnosis: source-lane exhaustion / anti-repetition guard saturation. Canonical Signals 0/98 eligible (overlapping blockers: 12 duplicate, 46 repeat-family/duplicate, 12 no educational value, all 98 not A/B/watch); deterministic lanes exhausted (evergreen 0/42, AI Words 0/8, current-hour KPI 0/8; 30 partial source IDs quarantined).
- Scheduler/action: production cron remains enabled/state scheduled with next_run_at `2026-05-25T14:48:01.352646+00:00`. Source-lane replenishment remains the active KPI blocker; feed fresh non-repeating practical Thai ChatGPT/NotebookLM-first software-tip/service-industry sources.

<!-- ZG-DLOG-2026-05-25-1308-ISSUE-CHECK -->
### Issue-check 13:08 UTC — CTA guard clean; direct import below-threshold; import/breakout watch open
- Evidence: direct import `2026-05-25T13:08:01.608739+00:00` succeeded after scheduled import/breakout 13:00 readbacks were absent; read-only comparison `2026-05-25T13:08:37.331319+00:00` found `7641239648790007048` +1 to 1887 views / 13 shares and 0 breakout candidates.
- KPI: best `7634027210248097042` remains ChatGPT productivity/workflow evidence at 32,072 views / 429 shares / gap 67,928; protected CTA is promo only; CTA unsafe_count=0.
- Readbacks: growth `2026-05-25_12-25-59.md` and experiment `2026-05-25_12-46-16.md` delivered/current; import `2026-05-25_12-12-59.md` and breakout `2026-05-25_12-03-02.md` remain latest scheduled outputs with 13:00 next_run_at past at `2026-05-25T13:11:50Z`; issue-check output is in-flight; factory/source state is superseded by the 13:57 manual exact+required-recovery readback above.
- Action: opened exactly one scoped import+breakout scheduler watch; updated compact memory/tasks/Zernio Growth Memory/Daily Log/Open Loops/run log; no amplification/generation/public posting/spend/Zernio send.

<!-- ZG-DLOG-2026-05-25-1200-GROWTH-CHECK -->
### Growth-check 12:00 UTC — no formal breakout; scheduler readback normalized
- Evidence: normal baseline `2026-05-25T12:00:20.796266+00:00` found 0 breakout candidates and no current mover; latest import `2026-05-25_12-12-59.md` / Imported At `2026-05-25T12:06:47.168102+00:00` is fresh; breakout `2026-05-25_12-03-02.md` returned `No breakout candidate. Next check scheduled.`
- KPI: best `7634027210248097042` remains ChatGPT productivity/workflow evidence at 32,072 views / 429 shares / gap 67,928; protected CTA is promo only.
- Historical readback: the 12:00 growth-check/factory note is superseded by the 14:14 growth-check reconciliation, factory current readback `latest_social_draft_factory.json@2026-05-25T16:50:37.858469+00:00`, and issue-check `2026-05-25_13-18-39.md` error/no-response.
- Action: updated compact memory/tasks/Zernio Growth Memory/Daily Log/Open Loops to current readbacks; opened a then-temporary factory scheduler watch later superseded; no amplification/generation/public posting/spend/Zernio send.

<!-- ZG-DLOG-2026-05-25-1051-FACTORY-ZERO -->
### Historical 2026-05-25 10:51 UTC — manual exact + required recovery zero-draft/source-lane readback superseded by 13:57 manual readback
- Command/readback: ran exactly `venv/bin/python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality low --send-to-zernio` from `/home/clawd/.hermes/hermes-agent`; initial 10:44 run and required 10:51 recovery rerun both exited `status=ok` with `draft_count=0/results=[]`.
- Verification: fresh state `latest_social_draft_factory.json@2026-05-25T10:51:30.880543+00:00`; no new `auto-*` folder/manifest/media after `2026-05-25T10:43:48Z`, no current Airtable Carousel Posts row/outbound Zernio payload, no Zernio draft, and no lingering factory/radar process at `2026-05-25T13:11:50Z`. Zernio/platform verification is not applicable because no outbound payload/post exists.
- Diagnosis: source-lane exhaustion / anti-repetition guard saturation. Canonical Signals 0/98 eligible (overlapping blockers: 12 duplicate, 42 repeat-family/duplicate, 12 no educational value, all 98 not A/B/watch); deterministic lanes exhausted (evergreen 0/42, AI Words 0/8, current-hour KPI 0/8).
- Scheduler/action: historical factory-zero marker superseded by current factory current readback `latest_social_draft_factory.json@2026-05-25T16:50:37.858469+00:00`; live factory remains enabled/scheduled with next_run_at `2026-05-25T17:47:30.923195+00:00`. Source-lane replenishment remains the active KPI blocker.

<!-- ZG-DLOG-2026-05-25-0927-FACTORY-ZERO -->
### Historical 09:27 UTC — manual exact + recovery superseded by 11:09 scheduled factory readback
- Command/readback: ran exactly `venv/bin/python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality low --send-to-zernio` from `/home/clawd/.hermes/hermes-agent`; initial 09:23 run and required 09:27 recovery rerun both exited `status=ok` with `draft_count=0/results=[]`. The openclaw.bash startup warning was unrelated.
- Verification: fresh state `latest_social_draft_factory.json@2026-05-25T10:51:30.880543+00:00`; no new `auto-*` folder/manifest/media after `2026-05-25T09:27:36Z`, no Airtable Carousel Posts row/outbound Zernio payload, no Zernio draft, and no lingering factory/radar process at `2026-05-25T13:11:50Z`. Zernio/platform verification is not applicable because no payload/post exists; no public posting, no `publishNow`, no intentional schedule.
- Diagnosis: source-lane exhaustion / anti-repetition guard saturation. Canonical Signals 0/98 eligible; deterministic lanes exhausted (evergreen 0/42, AI Words 0/8, current-hour KPI 0/8). Static/YouTube fallback produced no usable non-duplicate source in the exact runs.
- Scheduler/action: historical factory-zero marker superseded by current factory current readback `latest_social_draft_factory.json@2026-05-25T16:50:37.858469+00:00`; live factory remains enabled/scheduled with next_run_at `2026-05-25T17:47:30.923195+00:00`. Source-lane replenishment remains the active KPI blocker.

<!-- ZG-DLOG-2026-05-25-0813-FACTORY-ZERO -->
### Historical 2026-05-25 08:13 UTC — scheduled zero-draft/source-lane exhaustion superseded by 11:09 scheduled factory readback
- Cron output: `historical 08:13 factory output superseded by 11:09 scheduled factory readback` delivered zero draft/source-lane exhaustion with state token `historical 07:49 zero-state superseded by 11:09 scheduled factory readback`; `draft_count=0/results=[]`.
- Verification: no outbound Zernio payload/draft exists; Zernio/platform verification is not applicable; no matching factory/radar process at `2026-05-25T09:03:47Z`.
- Historical cron/safety: this 08:13 scheduled output is superseded by the 09:27 manual exact+recovery readback above; production cron remains enabled/draft-only with next run now tracked in the current section.
- Next action: feed fresh non-repeating practical Thai software-tip/service-industry sources into production.

<!-- ZG-DLOG-2026-05-25-0800-BREAKOUT-WATCH -->
### Breakout-watch 08:00 UTC — no formal breakout; below-threshold movement only
- Evidence: final live snapshot `2026-05-25T08:00:27.423174+00:00` after scheduled import `2026-05-25_12-12-59.md` / Imported At `2026-05-25T07:44:32.118434+00:00` found 0 breakout candidates.
- KPI: best `7634027210248097042` remains ChatGPT productivity/workflow evidence at 32,072 views / 429 shares / gap 67,928; protected CTA is promo only.
- Watch-only context: `7641239648790007048` moved +14 to 1,879 views / 13 shares (~49.41/hr), below threshold; no amplification/generation.
- Readbacks: issue-check `2026-05-25_07-42-25.md` delivered; breakout markdown delivered; growth-check `2026-05-25_10-10-34.md` delivered/current. Prior 08:30 import resolved with `2026-05-25_12-12-59.md`; 09:00 import/breakout readback resolved by delivered import/breakout outputs; growth-check `2026-05-25_10-10-34.md` delivered; factory manual exact+recovery readback `2026-05-25_11-09-23.md` refreshed current source state.
- Safety/action: draft-only; no public posting, spend, generation, scheduler repair, or Zernio send.

<!-- ZG-DLOG-2026-05-25-1200-EXPERIMENT-CREATOR -->
### Experiment creator 12:00 UTC — exactly 3 draft-only practical software-tip specs
- Output/readback: current experiment-creator markdown is in-flight until delivery; prior delivered output `2026-05-25_12-46-16.md` remains historical.
- Specs: ChatGPT UGC/Influencer Brief for Local Shops — 7 tips; NotebookLM Employee Handbook / HR Policy Answer Book — 7 tips; Gemini in Sheets Staff Roster / Overtime Guard — 7 tips.
- Source IDs: `kpi-exp-0525-1200-chatgpt-ugc-influencer-brief-local-shops`, `kpi-exp-0525-1200-notebooklm-hr-employee-handbook-answer-book`, `kpi-exp-0525-1200-gemini-sheets-staff-roster-overtime-guard`.
- Gate: draft-only/no-generation/no-spend/no-public-posting/no-Zernio-send until result-closure/source-lane/Zernio/editorial gates clear.
- Scheduler readback: growth `2026-05-25_12-25-59.md` delivered/current; import `2026-05-25_12-12-59.md`, breakout `2026-05-25_12-03-02.md`, issue `2026-05-25_07-42-25.md`, and factory `2026-05-25_11-09-23.md` are resolved/current by live issue-check readback at `2026-05-25T13:11:50Z` because live jobs are future-scheduled or current issue-check is in-flight and no matching process is running.
- Safety: CTA guard unsafe_count=0; reusable GenLabs CTA is not counted as content tips.

<!-- ZG-DLOG-2026-05-25-0838-GROWTH-CHECK -->
### Growth-check 08:38 UTC — no formal breakout after direct import
- Evidence: direct import refreshed Airtable at `2026-05-25T08:46:32.713016+00:00` (`updated=47`, `created=0`); final snapshot `2026-05-25T09:03:47Z` found 0 breakout candidates and 0 posts in the last 72h.
- KPI: best `7634027210248097042` remains ChatGPT productivity/workflow evidence at 32,072 views / 429 shares / gap 67,928; protected CTA is promo only.
- Readbacks: breakout `2026-05-25_12-03-02.md` delivered; growth-check `2026-05-25_10-10-34.md` delivered; latest import output `2026-05-25_12-12-59.md` resolved the prior 08:30 import watch; final 09:00 import/breakout readback resolved by delivered import/breakout outputs; factory manual exact+recovery readback `2026-05-25_11-09-23.md` refreshed current source state.
- Action: updated compact memory, tasks, Zernio Growth Memory, Daily Log, and Open Loops; no amplification/generation/public posting/spend/Zernio send.

<!-- ZG-DLOG-2026-05-25-1000-GROWTH-CHECK -->
### Growth-check 10:00 UTC — no formal breakout; scheduler readback resolved/current
- Evidence: normal baseline `2026-05-25T10:00:36.179764+00:00` found 0 breakout candidates; strongest mover `7641239648790007048` was +4 to 1,883 views / 13 shares (~14.19/hr), below threshold. Latest scheduled import `2026-05-25_12-12-59.md` and live Imported At `2026-05-25T10:02:07.652259+00:00` produced no additional post-baseline movers.
- KPI: best `7634027210248097042` remains ChatGPT productivity/workflow evidence at 32,072 views / 429 shares / gap 67,928; protected CTA is promo only.
- Readbacks: breakout `2026-05-25_12-03-02.md` delivered `No breakout candidate. Next check scheduled.`; factory `2026-05-25_11-09-23.md` delivered/current zero-draft/source-lane exhaustion; growth-check `2026-05-25_10-10-34.md` delivered/current.
- Action: resolved the stale 09:00 import/breakout watch, updated compact memory/tasks/Zernio Growth Memory/Daily Log/Open Loops to current outputs, and kept no amplification/generation/public posting/spend/Zernio send.

<!-- ZG-DLOG-2026-05-25-1000-SELF-IMPROVEMENT -->
### 3-day self-improvement 10:00 UTC — ChatGPT proof, NotebookLM priority, production recovery
- KPI progress: no closer this window; best `7634027210248097042` stays at 32,072 views / 429 shares / gap 67,928, with 0 formal breakout candidates and 0 recent-72h posts.
- What worked: CTA-stripped ChatGPT practical numbered work-output tips remain the only direct proof; scheduler/readback ambiguity is resolved by import `2026-05-25_12-12-59.md`, breakout `2026-05-25_12-03-02.md`, growth `2026-05-25_10-10-34.md`, and factory `2026-05-25_11-09-23.md`.
- What failed: source-lane/anti-repetition exhaustion still produced zero drafts; result closure/backfill, prior Zernio POST 403, and editorial/source-topic QA remain open.
- Rule update: next 3 days bias production toward fresh non-repeating ChatGPT + NotebookLM practical numbered Thai service-workflow carousels; test Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude tools, and Zapier/Make only as distinct visible-tip software tests after gates clear.
- Next action: backfill active experiment results, replenish source IDs, fix Zernio POST/create permission and source-topic routing, and keep factory enabled/draft-only without forcing weak/repeated drafts.

### Links
- Memory note: [[Aion OS/Aion Learning Lab/Zernio Growth/Zernio Growth Memory]]
- Master state: [[Aion OS/Projects/genlabs-ai-learning-state]]
- Self-improvement SOP: [[Aion OS/SOPs/genlabs-ai-learning-self-improvement-system]]

## 2026-05-24

### Historical daily-log context superseded by 2026-05-25 current summary
- KPI snapshot remains useful: best `7634027210248097042` at 32,072 views / 429 shares / gap 67,928; protected CTA is promo copy only.
- Prior same-day factory zero-draft and scheduler-boundary details are historical; use the 2026-05-25 current summary above as the current-state anchor.
- Prior Zernio POST 403 and editorial/source-topic QA blockers remain separate prior issues.

## 2026-05-23

### KPI status
- Goal: one TikTok post reaches **100,000 views**.
- Best post: ChatGPT 8 productivity tips for work: self-review, onboarding plan, project brief, feedback/action items
- Current best views: 32072
- Gap to 100,000: 67928
- Closest post views: 32072
- Strongest velocity post: ChatGPT 8 productivity tips for work: self-review, onboarding plan, project brief, feedback/action items
- Recent 72h post count: 0
- Snapshot time: 2026-05-24T00:00:05.295991+00:00

### Signals learned today
- Winning hook samples:
- ChatGPT 8 productivity tips for work: self-review, onboarding plan, project brief, feedback/action items
- 👋 เหมาะกับใคร: คนเริ่มใช้ AI, เจ้าของร้าน, คนทำคอนเทนต์, ฟรีแลนซ์ หรือทีมเล็กที่อยากเอา AI ไปใช้กับงานจริง ไม่ใช่แค่ดูข่าวแล้วผ่านไป 💡 ไอเดียหลัก: พนักงานใหม่ต้…
- เหมาะกับใคร: คนเริ่มใช้ AI, เจ้าของร้าน, คนทำคอนเทนต์, ฟรีแลนซ์ หรือทีมเล็กที่อยากเอา AI ไปใช้กับงานจริง ไม่ใช่แค่ดูข่าวแล้วผ่านไป 💡 ไอเดียหลัก: หลายทีมประชุมแล…
- Weak hook samples:
- 👋 เหมาะกับใคร: คนเริ่มใช้ AI, เจ้าของร้าน, คนทำคอนเทนต์, ฟรีแลนซ์ หรือทีมเล็กที่อยากเอา AI ไปใช้กับงานจริง ไม่ใช่แค่ดูข่าวแล้วผ่านไป 💡 ไอเดียหลัก: หลายร้านมีข้อ…
- Prompt Drop: ยาดม/สมุนไพรไทยให้ดู Modern Wellness เซฟโพสต์นี้ไว้ถ้าคุณทำคอนเทนต์ขายของออนไลน์ แล้วอยากได้ภาพที่ดูเหมือนถ่ายแคมเปญจริง ไม่ใช่ภาพ AI พลาสติกหรือภา…
- 👋 เหมาะกับใคร: คนเริ่มใช้ AI, เจ้าของร้าน, คนทำคอนเทนต์, ฟรีแลนซ์ หรือทีมเล็กที่อยากเอา A
- Protected CTA note: Sway-added CTA phrase is protected and must not be treated as hook/topic signal; learn from educational_signal instead.
- Protected CTA occurrences in low-view sample: 3
- Breakout candidates: 0 current candidates; prior `7641239648790007048` movement is watch-only context until a later import/baseline confirms renewed velocity.
- Historical issue count at that snapshot: 8

### Mistakes / weak spots to correct
- no_posts_in_last_72h
- active_experiment_result_closure_overdue_or_blocked
- historical factory source-lane exhaustion / anti-repetition guard saturation from earlier 02:22 evidence; superseded by the 07:33 factory output zero-draft readback in the current 2026-05-24 summary
- separate prior Zernio POST 403 permission blocker from 01:08/04:52 (Instagram account missing from active key)
- separate prior source-topic routing mismatch from 01:08/04:52 (money-making YouTube source became HR scorecard)
- learning_loop_structured_performance_experiments_backfill_missing
- zernio_analytics_zero_metric_regression_guarded_2026_05_12_1415
- historical broad 00:00 scheduler watch superseded; breakout `2026-05-24_06-48-38.md` later delivered no candidate; current open scheduler issue is scoped only to missing 07:00 import/breakout readbacks

### Rule / memory update
- Lesson: Fix active source supply, result-closure, and factory QA gates before scaling more near-duplicate growth experiments.
- Decision rule: If no post is on pace for 100k, increase fresh practical ChatGPT/NotebookLM/software-tip source volume and remix the best specific business-use hook instead of passively waiting.

### Next action
- Replenish fresh non-repeating software-tip/service-industry sources, then close/mark blocked active 2h/4h/24h result loops and resolve Zernio/account/editorial QA before creating more near-duplicate drafts; keep any breakout amplification draft-only.



<!-- ZG-DLOG-2026-05-24-0452-FACTORY-RECOVERY-ZERNIO-403 -->
### Factory recovery 04:52 UTC — separate prior manifest+Airtable generated, Zernio POST 403
- Command/readback: initial exact command returned zero drafts (`latest_social_draft_factory.json@2026-05-24T04:45:48.667604+00:00`); required recovery generated manifest `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260524T044738Z-yt-5_1lz_bF9P8/manifest.json` and Airtable `reccDTyO2xUo6A4cl`, then POST `/v1/posts` returned 403.
- Safety/account verification: rebuilt outbound payload was draft-only (`isDraft=true`, `tiktokSettings.draft=true`, no `publishNow`, no `scheduledFor`), media_count=8, TikTok+FB+IG account IDs set, and FB/IG first-comment SHA-256 exact `c106abada72072b8911c42b91d45b949b7260d98fff37facd868979dfff56dd8`. Live account preflight showed Instagram missing from the active Zernio key; recent post scan found title-family matches but 0 non-CTA asset overlap, so no hidden draft was created.
- Editorial QA: no public source/meta leakage; hook/middle/CTA vision QA readable. Source-topic fit is weak/repetitive (`How To Use Blackbox AI for Earning Money (Full Guide) 2026!` became HR scorecard with generic workflow/Make chip), so this manifest remains review-only/not KPI-ready even after the account blocker is fixed.
- Supersession: source-lane zero-state from the initial exact command was superseded by the recovery manifest+Airtable+403 state, and that prior recovery state is now separate from the current factory state `historical 07:41 zero-draft output superseded by 09:01 manifest+403` / `historical 07:33 zero-state superseded by 09:01 manifest+403`. Current factory blocker is source-lane exhaustion from the 07:33 factory output zero-draft readback; prior blockers are Zernio account/API access and source-topic routing.

### Links
- Memory note: [[Aion OS/Aion Learning Lab/Zernio Growth/Zernio Growth Memory]]
- Master state: [[Aion OS/Projects/genlabs-ai-learning-state]]
- Self-improvement SOP: [[Aion OS/SOPs/genlabs-ai-learning-self-improvement-system]]



## Historical 2026-05-24 section superseded by current summary

<!-- ZG-DLOG-2026-05-24-1000-BREAKOUT-WATCH -->
- 10:00 Breakout Watch: no formal breakout after import `2026-05-24_10-02-48.md` / Airtable `2026-05-24T10:01:31.944012+00:00`; read-only comparison found below-threshold movement only. Best post remains ChatGPT productivity/workflow `7634027210248097042` at 32,072 views / 429 shares / gap 67,928. Factory current state is `historical 10:31 zero-state superseded by 11:54 readback` zero-draft/source-lane exhaustion; prior 09:12 Zernio POST 403 is separate. CTA guard unsafe_count=0. Factory process check `historical 10:48 process check superseded by 11:55 readback`.

<!-- ZG-DLOG-2026-05-24-0635-ISSUE-CHECK -->
### Issue-check 06:35 UTC — CTA guard clean; later readbacks superseded scheduler watch
- CTA guard: unsafe_count=0; `7634027210248097042` remains ChatGPT productivity/workflow evidence, not product-photo/no-prompt CTA evidence.
- Analytics: earlier issue-check no-breakout evidence was superseded by latest import `2026-05-24_10-02-48.md` and comparison `2026-05-24T08:39:12.373669+00:00`, which found only below-threshold movement `7641239648790007048` +3 to 1772. Best remains 32,072 views / 429 shares / gap 67,928.
- Scheduler/readbacks: the watch opened by issue-check is resolved by later import `2026-05-24_10-02-48.md`, breakout `2026-05-24_10-12-32.md`, issue `2026-05-24_07-11-22.md`, and factory `historical 07:41 zero-draft output superseded by 09:01 manifest+403` readbacks. Historical note: that run's growth-check output was delivery-pending then and has since been superseded by later delivered outputs.
- Safety: no generation, no public posting, no spend, no Zernio send.

<!-- ZG-DLOG-2026-05-24-0700-SCHEDULER-READBACK-WATCH -->
### Scheduler readback 07:00 UTC — resolved by growth-check final readback
- Evidence: import `2026-05-24_10-02-48.md` and breakout `2026-05-24_10-12-32.md` delivered; live jobs are enabled/scheduled/last_status=ok and boundary-watch pending (`import 2026-05-24T08:30:00+00:00`, `breakout 2026-05-24T08:30:00+00:00`). Issue-check `2026-05-24_07-11-22.md` also delivered.
- Action: closed the scoped scheduler watch as `resolved_current_tick_import_breakout_outputs_delivered`. No scheduler repair, generation, spend, public posting, or Zernio send was triggered. Current growth-check markdown remains in-flight until delivery, not missing.

<!-- ZG-DLOG-2026-05-24-0630-FACTORY-ZERO-SOURCE-LANE -->
### Factory 07:41 UTC — scheduled zero-draft delivered; historical source-lane zero-state superseded by 09:01 manifest+403
- Output/readback: `historical 07:41 zero-draft output superseded by 09:01 manifest+403` delivered the exact command + required recovery result with `draft_count=0/results=[]`; state file `historical 07:33 zero-state superseded by 09:01 manifest+403` remains the content-state evidence.
- Verification: no new `auto-*` folder/manifest/media, no Airtable `Carousel Posts` record, no outbound Zernio payload, and no Zernio draft. Zernio/platform verification is not applicable because no post/payload exists.
- Scheduler/process: cron `a97a7703af32` remains enabled/scheduled next `historical 08:41 due time superseded by 09:01 readback`; no lingering factory/radar process at `historical 08:46 process check superseded by 09:09 readback`.
- Diagnosis: source-lane exhaustion / anti-repetition guard saturation remains the active blocker.
- Next action: feed fresh non-repeating practical Thai software-tip/service-industry sources while keeping production enabled/draft-only.

<!-- ZG-DLOG-2026-05-24-0600-GROWTH-CHECK -->
### Growth-check 06:00 UTC — no formal breakout; later import found below-threshold movement
- Evidence: earlier growth `2026-05-24_08-15-07.md` delivered no formal breakout; later imports are superseded by current import `2026-05-24_10-02-48.md` / Imported At `2026-05-24T08:31:23.581457+00:00`, which found watch-only below-threshold movement, not a breakout.
- KPI: best `7634027210248097042` remains ChatGPT productivity/workflow at 32,072 views / 429 shares / gap 67,928; protected CTA is promo only.
- Action: no generation/spend/public posting/Zernio send from growth-check or issue-check.

<!-- ZG-DLOG-2026-05-24-0800-GROWTH-CHECK -->
### Growth-check 08:00 UTC — no formal breakout; below-threshold movement only
- KPI: best `7634027210248097042` remains ChatGPT productivity/workflow at 32,072 views / 429 shares / gap 67,928; protected CTA is promo only.
- Evidence: pre-run snapshot `2026-05-24T08:01:00.022372+00:00` was a normal baseline with 0 breakout candidates; latest import `2026-05-24_10-02-48.md` / Imported At `2026-05-24T08:31:23.581457+00:00` found only watch-only movement `7641239648790007048` +3 to 1772. Breakout `2026-05-24_10-12-32.md` also returned no candidate.
- Action: resolved stale scheduler watch from active issues/tasks, normalized latest import/breakout/issue/factory outputs, stored the below-threshold mover as watch-only, and kept all work draft-only/no-spend/no-public-posting.
- Next: source-lane replenishment + active experiment result closure/backfill before scaling more variants; continue ChatGPT/NotebookLM practical software-tip bias.

<!-- ZG-DLOG-2026-05-24-0830-BREAKOUT-WATCH -->
### Breakout-watch 08:30 UTC — no breakout after 08:32 import
- Evidence: pre-run snapshot `2026-05-24T08:30:09.358022+00:00` was a normal baseline with 0 breakout candidates. Scheduled import `2026-05-24_10-02-48.md` / Airtable `Imported At 2026-05-24T08:31:23.581457+00:00` completed after the baseline; read-only comparison `2026-05-24T08:39:12.373669+00:00` found no threshold-clearing breakout candidate / 0 candidates.
- KPI: best `7634027210248097042` remains ChatGPT productivity/workflow at 32,072 views / 429 shares / gap 67,928; protected CTA is promo only.
- Watch-only context: `7641239648790007048` had +3 to 1772 at the baseline but did not move after the latest import, so no remix/amplification is triggered.
- Readback: growth `2026-05-24_08-15-07.md` delivered; then-current growth-check output was delivery-pending at that historical readback. No generation, public posting, spend, or Zernio send.

<!-- ZG-DLOG-2026-05-24-0841-FACTORY-SCHEDULER-WATCH -->
### Historical factory scheduler 08:41 UTC — superseded readback context
- Evidence: final breakout-watch readback `historical 08:46 process check superseded by 09:09 readback` crossed factory due `historical 08:41 due time superseded by 09:01 readback`; factory output is superseded by 09:01 manifest+403 `historical 07:41 zero-draft output superseded by 09:01 manifest+403` and 09:01 manual exact readback produced manifest+Airtable before Zernio POST 403; no lingering process remains.
- Split truth: analytics remains no-candidate after import `2026-05-24_10-02-48.md` / comparison `2026-05-24T08:39:12.373669+00:00`; later breakout markdown delivered no-candidate; growth output 2026-05-25_08-43-12.md delivered; issue-check `2026-05-25_13-18-39.md` later errored/no-response; retry/debug needed. Factory scheduler watch is separate from breakout evidence.
- Action: historical scheduler concern was later resolved by the 13:30 factory output readback; no generation, public posting, spend, or Zernio send occurred.

<!-- ZG-DLOG-2026-05-24-0000-EXPERIMENT-CREATOR -->
### Historical experiment creator 00:00 UTC — API failure superseded by 12:00 specs
- Previous output `2026-05-25_00-29-31.md` failed after 3 API retries; this is now historical context.
- Supersession: the current 12:00 experiment creator created exactly 3 draft-only specs: `kpi-exp-0524-1200-chatgpt-live-sale-order-closeout`, `kpi-exp-0524-1200-notebooklm-renovation-contractor-answer-book`, and `kpi-exp-0524-1200-gemini-sheets-stock-expiry-reorder-board`. Current 12:00 markdown is in-flight until delivery, not a scheduler miss.
- Gate remains draft-only/no-generation/no-spend/no-public-posting/no-Zernio-send until result-closure/source-lane/Zernio permission/editorial gates clear.

<!-- ZG-DLOG-2026-05-24-0452-FACTORY-RECOVERY-ZERNIO-403 -->
### Factory recovery 04:52 UTC — separate prior manifest+Airtable generated, Zernio POST 403
- Prior recovery generated manifest `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260524T044738Z-yt-5_1lz_bF9P8/manifest.json` and Airtable `reccDTyO2xUo6A4cl`, then POST `/v1/posts` returned 403 because Instagram account is missing from the active API key.
- This remains a separate prior account/API blocker plus editorial/source-topic QA issue; it is not the current factory state after `historical 07:41 zero-draft output superseded by 09:01 manifest+403`.

### Links
- Memory note: [[Aion OS/Aion Learning Lab/Zernio Growth/Zernio Growth Memory]]
- Master state: [[Aion OS/Projects/genlabs-ai-learning-state]]
- Self-improvement SOP: [[Aion OS/SOPs/genlabs-ai-learning-self-improvement-system]]
