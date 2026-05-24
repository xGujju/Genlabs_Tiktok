## Current Zernio Growth Summary — 2026-05-24

### KPI status
- Goal: one TikTok post reaches **100,000 views**.
- Best post: ChatGPT 8 productivity tips for work: self-review, onboarding plan, project brief, feedback/action items
- Current views: 32,072
- Gap to 100,000: 67,928
- Shares: 429
- Snapshot/verification time: normal baseline `2026-05-24T16:39:12.331820+00:00`; latest scheduled import `2026-05-24_16-41-12.md` with Airtable Imported At `2026-05-24T16:40:27.892436+00:00` and read-only comparison `2026-05-24T16:41:27.182674+00:00` found zero watched/all-post movers; latest completed breakout `2026-05-24_16-18-13.md` delivered no candidate; growth output `2026-05-24_16-12-50.md` delivered/current; issue `2026-05-24_12-39-53.md`; experiment `2026-05-24_12-19-41.md`; factory scheduled output `2026-05-24_16-38-11.md` / state `latest_social_draft_factory.json@2026-05-24T16:30:43.781194+00:00`; final process check `2026-05-24T16:47:39Z`.

### Current signal
- Breakout state: **no formal breakout at the 16:39 normal baseline**.
- Previous below-threshold mover watch: `7641239648790007048` — AI prompt/context checklist: give role, goal, context, examples, output format, and ask-back rule before trusting the answer; 1,830 views / 12 shares, no post-baseline movement after import `2026-05-24_16-41-12.md`. Watch-only; no amplification draft.
- Current best/closest watch: `7634027210248097042` at 32,072 views / 429 shares / gap 67,928; ChatGPT practical productivity/workflow evidence, not CTA evidence.
- No posts in the last 72h, so production blockers and source quality remain the biggest growth bottleneck.

### Current blockers
- Active issue count: 7. Main blockers: no posts in 72h, source-lane exhaustion/anti-repetition guard saturation, overdue result closure/backfill, separate prior Zernio POST 403/account access, separate prior editorial/source-topic QA, structured learning-loop backfill, and zero-metric/CTA guard monitoring.
- Factory current readback: scheduled output `2026-05-24_16-38-11.md` reports zero-draft/source-lane exhaustion. State token `latest_social_draft_factory.json@2026-05-24T16:30:43.781194+00:00` has `draft_count=0/results=[]`; no current-run `auto-*` folder/manifest/media, no Airtable Carousel Posts row, no outbound Zernio payload, and no Zernio draft was created.
- Factory scheduler cadence: resolved/current; cron `a97a7703af32` remains enabled/future-scheduled next `2026-05-24T17:38:12.025887+00:00`; no lingering factory/radar/import/snapshot process at `2026-05-24T16:47:39Z`.

### Readback split
- Scheduler/readback: latest scheduled import `2026-05-24_16-41-12.md`, latest completed breakout `2026-05-24_16-18-13.md`, growth `2026-05-24_16-12-50.md`, issue `2026-05-24_12-39-53.md`, experiment `2026-05-24_12-19-41.md`, and factory scheduled output `2026-05-24_16-38-11.md` are current. Current breakout report is in-flight until delivery and is not a scheduler miss.
- Safety: no generation/media/outbound payload; no public posting, no `publishNow`, no intentional scheduling, and no Zernio send.

## 2026-05-24

### Links
- Compact memory: `/home/clawd/.hermes/zernio_growth/memory.json`
- Open loops: `Aion OS/07 - Open Loops.md`

<!-- ZG-DLOG-2026-05-24-1639-BREAKOUT-WATCH -->
### Breakout watch 16:39 UTC — no breakout candidate after 16:41 import no-change
- KPI: best `7634027210248097042` / 32,072 views / 429 shares / gap 67,928. The reusable GenLabs CTA is protected promo copy; the winner remains ChatGPT productivity/workflow content.
- Signal: no formal breakout candidates at normal baseline `2026-05-24T16:39:12.331820+00:00`. Previous below-threshold mover `7641239648790007048` is watch-only at 1,830 views / 12 shares, with no post-baseline movement after import `2026-05-24_16-41-12.md`.
- Final readback: scheduled import `2026-05-24_16-41-12.md` / Imported At `2026-05-24T16:40:27.892436+00:00` completed after the baseline; read-only comparison `2026-05-24T16:41:27.182674+00:00` found zero watched/all-post movers and zero candidates. Latest completed breakout `2026-05-24_16-18-13.md` returned no candidate; current breakout output is in-flight until delivery, not a scheduler miss.
- Factory/readback: scheduled factory output `2026-05-24_16-38-11.md` delivered zero-draft/source-lane exhaustion from state token `latest_social_draft_factory.json@2026-05-24T16:30:43.781194+00:00`; cron next `2026-05-24T17:38:12.025887+00:00`; no lingering factory/radar/import/snapshot process at `2026-05-24T16:47:39Z`.
- Action: normalized compact memory, tasks, Zernio Growth Memory, Daily Log, Open Loops, and the factory run log to latest import/breakout/factory readbacks. No generation, spend, public posting, or Zernio send.
- Blockers: source-lane exhaustion, result-closure/backfill, prior Zernio POST 403, prior source-topic QA, no posts in 72h, and zero-metric/CTA guard remain tracked separately.
- Safety: draft-only; no generation, spend, public posting, or Zernio send.

<!-- ZG-DLOG-2026-05-24-1630-FACTORY-ZERO-DRAFT-SOURCE-LANE -->
### Historical factory manual exact+required recovery 16:30 UTC — zero-draft source-lane exhaustion; superseded by 16:38 scheduled output
- Command/readback: ran exactly `venv/bin/python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality low --send-to-zernio` from `/home/clawd/.hermes/hermes-agent`. Initial tracked run returned `draft_count=0/results=[]` at `latest_social_draft_factory.json@2026-05-24T16:28:30.261915+00:00`; diagnosis confirmed source exhaustion/anti-repetition saturation, so the required recovery rerun used the same exact command and also returned `draft_count=0/results=[]` at `latest_social_draft_factory.json@2026-05-24T16:30:43.781194+00:00`. The openclaw.bash startup warning was unrelated.
- Verification: no new current-run `auto-*` folder/manifest/media since 16:27:49Z, Carousel Posts count stayed 215, no outbound Zernio payload/Zernio draft, and no lingering factory/radar process at `2026-05-24T16:36:23Z`. Zernio/platform verification is not applicable because no payload/post exists; no public posting, no `publishNow`, and no intentional scheduling occurred.
- Diagnosis: source-lane exhaustion / anti-repetition guard saturation. Canonical 0/98 eligible (overlapping gates: 12 duplicate source IDs, 42 repeat-family/duplicate, 12 no educational value, 98 not A/B, 98 watch-for-corroboration); Evergreen 0/42; AI Words 0/8; current-hour KPI backstop 0/8; Carousel Posts 215; partial-generation quarantines 30; blocked content-family keys 68; YouTube fallback produced no usable non-duplicate source in the exact factory runs.
- Scheduler/process: cron `a97a7703af32` remains enabled/scheduled next `2026-05-24T17:27:14.547520+00:00`; scheduler cadence is current/resolved for this tick while source-lane exhaustion remains open. Keep production enabled/draft-only.
- Next action: Feed fresh non-repeating practical Thai software-tip/service-industry sources; prioritize ChatGPT and NotebookLM, then Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude Artifacts/Projects, and Zapier/Make.

<!-- ZG-DLOG-2026-05-24-1600-GROWTH-CHECK -->
### Growth check 16:00 UTC — no formal breakout; below-threshold mover watch and factory output current
- KPI: best `7634027210248097042` / 32,072 views / 429 shares / gap 67,928. The reusable GenLabs CTA is protected promo copy; the winner remains ChatGPT productivity/workflow content.
- Signal: no formal breakout candidates. Normal baseline `2026-05-24T16:00:16.529874+00:00` found `7641239648790007048` at 1,830 views / 12 shares / +12 (~24.3/hr), still below threshold; watch-only/no amplification.
- Final readback: scheduled import `2026-05-24_16-01-56.md` / Imported At `2026-05-24T16:01:28.859656+00:00` completed after the baseline; read-only comparison `2026-05-24T16:09:46.950662+00:00` found zero watched/all-post movers. Latest completed breakout `2026-05-24_15-31-35.md` returned no candidate; growth output `2026-05-24_16-12-50.md` delivered/current.
- Action: normalized compact memory, tasks, Zernio Growth Memory, Daily Log, Open Loops, and the factory run log to latest import/breakout/factory readbacks. No generation, spend, public posting, or Zernio send.
- Blockers: source-lane exhaustion, result-closure/backfill, prior Zernio POST 403, prior source-topic QA, no posts in 72h, and zero-metric/CTA guard remain tracked separately.
- Safety: draft-only; no generation, spend, public posting, or Zernio send.

<!-- ZG-DLOG-2026-05-24-1526-FACTORY-ZERO-DRAFT-SOURCE-LANE -->
### Factory scheduled output 15:26 UTC — zero-draft source-lane exhaustion; scheduler cadence current
- Readback: scheduled factory markdown `prior scheduled factory output superseded by 16:30 manual readback` delivered and confirmed zero-draft/source-lane exhaustion. State JSON remains `prior zero-state superseded by 16:30 manual readback` with `draft_count=0/results=[]`.
- Verification: no new current-run `auto-*` folder/manifest/media, no Airtable Carousel Posts row, no outbound Zernio payload/Zernio draft, and no lingering factory/radar/import/snapshot process at `2026-05-24T16:36:23Z`. Zernio/platform verification is not applicable because no payload/post exists; no public posting, no `publishNow`, and no intentional scheduling occurred.
- Diagnosis: source-lane exhaustion / anti-repetition guard saturation. Canonical 0/98 eligible; Evergreen 0/42; AI Words 0/8; current-hour KPI backstop 0/8; Carousel Posts 215; partial-generation quarantines 30; blocked content-family keys 68.
- Scheduler/process: cron `a97a7703af32` remains enabled/scheduled next `2026-05-24T17:27:14.547520+00:00`; scheduler cadence is current/resolved for this tick while source-lane exhaustion remains open. Keep production enabled/draft-only.
- Next action: feed fresh non-repeating practical Thai software-tip/service-industry sources, prioritizing ChatGPT and NotebookLM, then Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude Artifacts/Projects, and Zapier/Make.

<!-- ZG-DLOG-2026-05-24-1400-GROWTH-CHECK -->
### Growth check 14:00 UTC — delivered; no formal breakout and post-baseline import no-change
- KPI: best `7634027210248097042` / 32,072 views / 429 shares / gap 67,928. The reusable GenLabs CTA is protected promo copy; the winner remains ChatGPT productivity/workflow content.
- Signal: no formal breakout candidates. Normal baseline `2026-05-24T14:41:12.091852+00:00` found `7641239648790007048` at 1,818 views / 11 shares / +9 (~13.36/hr), still below threshold; watch-only/no amplification.
- Final readback: scheduled import `2026-05-24_16-01-56.md` / Imported At `2026-05-24T16:01:28.859656+00:00` completed after that baseline and read-only comparison `2026-05-24T14:44:28.210084+00:00` found 0 post-baseline movers. Growth output `2026-05-24_14-24-50.md` delivered/current; current breakout-watch markdown is in-flight until delivery, not a scheduler miss.
- Action: normalized compact memory, tasks, Zernio Growth Memory, Daily Log, and Open Loops to latest import/growth/factory readbacks. No generation, spend, public posting, or Zernio send.
- Blockers: source-lane exhaustion, result-closure/backfill, prior Zernio POST 403, prior source-topic QA, no posts in 72h, and zero-metric/CTA guard remain tracked separately.
- Safety: draft-only; no generation, spend, public posting, or Zernio send.

<!-- ZG-DLOG-2026-05-24-1504-FACTORY-ZERO-DRAFT-SOURCE-LANE -->
### Historical factory manual exact+recovery 15:04 UTC — zero-draft source-lane exhaustion; superseded by 15:26 scheduled output
- Command/readback: ran exactly `venv/bin/python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality low --send-to-zernio` from `/home/clawd/.hermes/hermes-agent`. Initial tracked run returned `draft_count=0/results=[]` at `latest_social_draft_factory.json@2026-05-24T15:00:43.967197+00:00`; diagnostics confirmed source exhaustion, so the required recovery rerun used the same exact command and also returned `draft_count=0/results=[]` at `prior zero-state superseded by 16:30 manual readback`. The openclaw.bash startup warning was unrelated.
- Verification: no new current-run `auto-*` folder/manifest/media since 15:00:10Z, no Airtable Carousel Posts row since 15:00:10Z, no outbound Zernio payload/Zernio draft, and no lingering factory/radar process at `2026-05-24T16:36:23Z`. Zernio/platform verification is not applicable because no payload/post exists; no public posting, no `publishNow`, and no intentional scheduling occurred.
- Diagnosis: source-lane exhaustion / anti-repetition guard saturation. Overlapping selector gates: Canonical 0/98 eligible (12 missing/duplicate source, 42 repeat-family/duplicate, 12 no educational value, 98 not A/B, 98 watch-for-corroboration); Evergreen 0/42; AI Words 0/8; current-hour KPI backstop 0/8; Carousel Posts 215; partial-generation quarantines 30; blocked content-family keys 68.
- Scheduler/process: cron `a97a7703af32` remains enabled/scheduled next `2026-05-24T17:27:14.547520+00:00`; scheduler cadence is current/resolved for this tick while source-lane exhaustion remains open. Keep production enabled/draft-only.
- Separate prior blockers: prior 09:12 manifest `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260524T085532Z-yt-3L7ANFrR7-c/manifest.json` / Airtable `recQQk3TboovxgSV9` hit Zernio POST 403 because Instagram is missing from the active key, and that generated n8n source output remains review-only/not KPI-ready; those are separate from the current zero-draft tick.
- Next action: feed fresh non-repeating practical Thai software-tip/service-industry sources, prioritizing ChatGPT and NotebookLM, then Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude Artifacts/Projects, and Zapier/Make.

<!-- ZG-DLOG-2026-05-24-1358-FACTORY-ZERO-DRAFT-SOURCE-LANE -->
### Historical factory scheduled output 13:58 UTC — zero-draft source-lane exhaustion; superseded by 15:26 scheduled output
- Historical output/readback: the 13:58 scheduled factory markdown delivered a zero-draft exact+recovery state, later superseded by the 16:30 manual exact+recovery readback above.
- Historical verification: no Airtable row/outbound Zernio payload/Zernio draft existed for that tick, and no lingering factory/radar process was found in the later readback. Zernio/platform verification was not applicable because no payload/post existed; no public posting, no `publishNow`, and no intentional scheduling occurred.
- Historical diagnosis: source-lane exhaustion / anti-repetition guard saturation; same blocker is now refreshed under the 16:30 readback above.
- Historical scheduler/process: the old due time was superseded by the current future schedule `2026-05-24T17:27:14.547520+00:00`; keep production enabled/draft-only.
- Separate prior blockers: prior 09:12 manifest `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260524T085532Z-yt-3L7ANFrR7-c/manifest.json` / Airtable `recQQk3TboovxgSV9` hit Zernio POST 403 because Instagram is missing from the active key, and that same generated n8n source output remains review-only/not KPI-ready; those are separate from the current zero-draft tick.
- Next action: feed fresh non-repeating practical Thai software-tip/service-industry sources, prioritizing ChatGPT and NotebookLM, then Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude Artifacts/Projects, and Zapier/Make.

<!-- ZG-DLOG-2026-05-24-1400-BREAKOUT-WATCH -->
### Breakout watch 14:30 UTC — no formal breakout; post-baseline import found no movers
- Evidence: normal baseline `2026-05-24T14:41:12.091852+00:00` found `breakout_candidates=[]`. Strongest movement was `7641239648790007048` at 1,818 views / 11 shares / +9 (~13.36/hr normal-baseline), below breakout threshold. Best remains `7634027210248097042` ChatGPT productivity/workflow at 32,072 views / 429 shares / gap 67,928.
- Final import check: latest import `2026-05-24_16-01-56.md` / Airtable `Imported At 2026-05-24T16:01:28.859656+00:00` completed after the baseline; read-only comparison `2026-05-24T14:44:28.210084+00:00` found 0 post-baseline movers and 0 candidates.
- Action: stored the mover as below-threshold watch-only context; no amplification draft, generation, spend, public posting, or Zernio send. Current breakout-watch markdown is in-flight until delivery, not a scheduler miss.
- Scheduler split: import `2026-05-24_16-01-56.md`, growth `2026-05-24_14-24-50.md`, issue `2026-05-24_12-39-53.md`, and experiment `2026-05-24_12-19-41.md` delivered/current; factory state is refreshed by the 16:30 manual exact+recovery readback above.
- CTA guard: unsafe_count=0; protected GenLabs product-photo/no-prompt CTA remains promo copy only and is not classified as winner/hook/topic/weak pattern.
- Safety: draft-only; no generation, spend, public posting, or Zernio send.

<!-- ZG-DLOG-2026-05-24-1230-ISSUE-CHECK -->
### Issue check 12:30 UTC — late import movement superseded by 13:00 no-breakout baseline
- Evidence: import `2026-05-24_16-01-56.md` is now the latest import readback. It refreshed Airtable after the 13:00 baseline and read-only comparison now shows 0 post-baseline movers and zero breakout candidates. The earlier 12:31 movement for `7641239648790007048` remains below-threshold watch-only, not a current breakout candidate. Best remains `7634027210248097042` ChatGPT productivity/workflow at 32,072 views / 429 shares / gap 67,928.
- Fix applied: current state now uses the 13:00 no-formal-breakout baseline plus delivered import `2026-05-24_16-01-56.md`, prior breakout `2026-05-24_15-31-35.md`, growth `2026-05-24_14-24-50.md`, issue `2026-05-24_12-39-53.md`, experiment `2026-05-24_12-19-41.md`, and the current 15:04 factory exact+recovery readback; older factory readbacks are historical.
- CTA guard: unsafe_count=0; protected GenLabs product-photo/no-prompt CTA remains promo copy only and is not classified as winner/hook/topic/weak pattern.
- Safety: draft-only; no generation, spend, public posting, or Zernio send.

<!-- ZG-DLOG-2026-05-24-1200-EXPERIMENT-CREATOR -->
### Experiment creator 12:00 UTC — exactly 3 draft-only software-tip specs created
- Specs: `kpi-exp-0524-1200-chatgpt-live-sale-order-closeout` (ChatGPT live-sale order closeout), `kpi-exp-0524-1200-notebooklm-renovation-contractor-answer-book` (NotebookLM renovation/contractor answer book), and `kpi-exp-0524-1200-gemini-sheets-stock-expiry-reorder-board` (Gemini Sheets stock/expiry reorder board).
- Evidence: no formal breakout at the 12:06 snapshot; best remains ChatGPT productivity/workflow `7634027210248097042` at 32,072 views / 429 shares / gap 67,928; no posts in last 72h; factory source-lane exhaustion remains current under the 16:30 exact+recovery readback.
- Gate: draft-only backlog; no generation/posting/spend/Zernio send until source-lane, result-closure, Zernio account/API, and editorial gates clear. Experiment output `2026-05-24_12-19-41.md` delivered; not a scheduler miss.

<!-- ZG-DLOG-2026-05-24-1200-GROWTH-CHECK -->
### Growth check 12:00 UTC — delivered; later 12:31 import superseded no-mover evidence
- KPI: best `7634027210248097042` / 32,072 views / 429 shares / gap 67,928. The reusable GenLabs CTA is protected promo copy; the winner remains ChatGPT productivity/workflow content.
- Signal: no formal breakout candidates. `7641239648790007048` is watch-only at 1,793 views / 11 shares; latest import `2026-05-24_12-09-06.md` / Imported At `2026-05-24T12:08:36.431220+00:00` found no threshold-clearing breakout candidate, and breakout `2026-05-24_12-07-36.md` returned no candidate.
- Action: synced compact memory, tasks, Zernio Growth Memory, Daily Log, Open Loops, and the factory run log to import `2026-05-24_12-09-06.md`, breakout `2026-05-24_12-07-36.md`, and later factory readbacks. No generation, spend, public posting, or Zernio send was triggered.
- Blockers: source-lane exhaustion is active; prior Zernio POST 403/account access and prior source-topic/editorial QA remain separate; result-closure/backfill and prior experiment API failure is resolved by the delivered 12:19 output; source/result/Zernio/editorial gates remain open.
- Verification: process readback `2026-05-24T12:23:41Z` found no lingering factory/radar/import/snapshot process; CTA unsafe_count=0.

<!-- ZG-DLOG-2026-05-24-1154-FACTORY-ZERO-DRAFT-SOURCE-LANE -->
### Historical factory manual exact+recovery 11:54 UTC — zero-draft source-lane exhaustion superseded by 12:05 factory output
- Command/readback: ran exactly `venv/bin/python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality low --send-to-zernio` from `/home/clawd/.hermes/hermes-agent`. Initial tracked run returned `draft_count=0/results=[]` at `latest_social_draft_factory.json@2026-05-24T11:52:05.008679+00:00`; diagnosis showed source exhaustion, so the required recovery rerun used the same exact command and also returned `draft_count=0/results=[]` at `historical 11:54 zero-state superseded by 13:30 manual readback`. The openclaw.bash startup warning was unrelated.
- Verification: no new `auto-*` folder/manifest/media since 11:51Z, Carousel Posts count stayed 215, no current Airtable row/outbound Zernio payload/Zernio draft exists, and no lingering factory/radar process at `2026-05-24T11:55:07Z`. Zernio/platform verification is not applicable for this tick because no payload/post exists.
- Diagnosis: source-lane exhaustion / anti-repetition guard saturation. Overlapping selector gates: Canonical 0/98 eligible (17 missing/duplicate source, 46 repeat-family/duplicate, 12 no educational value, 98 not A/B, 98 watch-for-corroboration); Evergreen 0/42; AI Words 0/8; current-hour KPI backstop 0/8; Carousel Posts 215; partial-generation quarantines 30; blocked content-family keys 68. YouTube fallback produced no usable non-duplicate candidate in the exact factory run.
- Scheduler/process: cron `a97a7703af32` remains enabled/scheduled next `historical 12:51 schedule superseded by 13:05 current factory next_run_at`; scheduler cadence is current/resolved for this tick while source-lane exhaustion remains open. Keep production enabled/draft-only.
- Separate prior blockers: prior 09:12 manifest `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260524T085532Z-yt-3L7ANFrR7-c/manifest.json` / Airtable `recQQk3TboovxgSV9` hit Zernio POST 403 because Instagram is missing from the active key, and that same generated n8n source output remains review-only/not KPI-ready; those are separate from the current zero-draft tick.
- Next action: Feed fresh non-repeating practical Thai software-tip/service-industry sources, prioritizing ChatGPT and NotebookLM, then Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude Artifacts/Projects, and Zapier/Make.

<!-- ZG-DLOG-2026-05-24-1031-FACTORY-ZERO-DRAFT-SOURCE-LANE -->
### Historical factory manual exact+recovery 10:31 UTC — zero-draft source-lane exhaustion superseded by 11:54 readback
- Command/readback: ran exactly `venv/bin/python scripts/scheduled_ai_social_draft_factory.py --limit 1 --apply --quality low --send-to-zernio` from `/home/clawd/.hermes/hermes-agent`. Initial tracked run returned `draft_count=0/results=[]` at `historical 10:29 initial zero-state superseded by 11:54 readback`; diagnosis showed source exhaustion, so the required recovery rerun used the same exact command and also returned `draft_count=0/results=[]` at `historical 10:31 zero-state superseded by 11:54 readback`. The openclaw.bash startup warning was unrelated.
- Verification: no new `auto-*` folder/manifest/media since 10:28Z, Carousel Posts count stayed 215, no current Airtable row/outbound Zernio payload/Zernio draft exists, and no lingering factory/radar process at `historical 10:48 process check superseded by 11:55 readback`. Zernio/platform verification is not applicable for this tick because no payload/post exists.
- Diagnosis: source-lane exhaustion / anti-repetition guard saturation. Canonical 0/98 eligible (12 missing/duplicate source, 30 repeat-family, 8 no educational value, 48 not A/B); Evergreen 0/42; AI Words 0/8; current-hour KPI backstop 0/8; Carousel Posts 215; partial-generation quarantines 30; blocked content-family keys 68. YouTube fallback produced no usable non-duplicate candidate in the exact factory run.
- Scheduler/process: cron `a97a7703af32` remains enabled/scheduled next `historical 11:22 due time superseded by 12:51 future schedule`; scheduler cadence is current/resolved for this tick while source-lane exhaustion remains open. Keep production enabled/draft-only.
- Separate prior blockers: prior 09:12 manifest `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260524T085532Z-yt-3L7ANFrR7-c/manifest.json` / Airtable `recQQk3TboovxgSV9` hit Zernio POST 403 because Instagram is missing from the active key, and that same generated n8n source output remains review-only/not KPI-ready; those are separate from the current zero-draft tick.
- Next action: Feed fresh non-repeating practical Thai software-tip/service-industry sources, prioritizing ChatGPT and NotebookLM, then Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude Artifacts/Projects, and Zapier/Make.

<!-- ZG-DLOG-2026-05-24-1000-GROWTH-CHECK -->
### Growth check 10:00 UTC — no formal breakout; readbacks current; factory later refreshed
- KPI: best `7634027210248097042` / 32,072 views / 429 shares / gap 67,928. The reusable GenLabs CTA is protected promo copy; the winner remains ChatGPT productivity/workflow content.
- Signal: no formal breakout candidates. `7641239648790007048` is watch-only at 1,793 views / 11 shares; latest import `2026-05-24_10-02-48.md` did not create a threshold-clearing mover.
- Action: synced compact memory, tasks, Zernio Growth Memory, Daily Log, Open Loops, and the factory run log to import `2026-05-24_10-02-48.md`, breakout `2026-05-24_10-12-32.md`, and the then-current 10:31 factory state; this was later superseded by the 11:54 factory readback above.
- Blockers: Source-lane exhaustion was active; prior Zernio POST 403/account access and prior source-topic/editorial QA remained separate; result-closure/backfill and experiment API failure remained open. That 10:31 factory readback is historical; use the 11:54 entry above as the current factory/source-lane state.
- Verification: `zernio_growth_snapshot.py` py_compile=0; CTA unsafe_count=0; historical factory/process readback was later superseded by the 11:55 no-lingering-process check.

<!-- ZG-DLOG-2026-05-24-0912-FACTORY-MANIFEST-ZERNIO-403 -->
### Historical/prior factory scheduled output 09:12 UTC — manifest+Airtable generated, separate Zernio POST 403 blocker
- Cron output: prior 09:12 factory run generated manifest `/home/clawd/.hermes/ai_signal_radar/carousels/auto-20260524T085532Z-yt-3L7ANFrR7-c/manifest.json` and Airtable `recQQk3TboovxgSV9` from `yt-3L7ANFrR7-c` / `How to Automate Your Small Business with n8n (3 Workflows That Save 10+ Hours a Week)`, then Zernio POST `/v1/posts` returned HTTP 403.
- Safety verification: Airtable status `not_sent`, no Zernio Draft ID, rebuilt payload draft-only (`isDraft=true`, `tiktokSettings.draft=true`, no `publishNow`, no `scheduledFor`), media_count=9, FB/IG first-comment SHA-256 exact-match, and no hidden Zernio draft found by recent scan.
- Content QA: public leak scan found 0 source/meta labels/URLs; vision QA readable/leak-free. Editorial caveat remains: generated output is a generic AI Agent/checklist lesson, not concrete n8n workflow/node/trigger instruction.
- Scheduler/process: this 09:12 output is a separate prior Zernio/account + editorial blocker; its factory-current wording was superseded by the 11:54 zero-draft/source-lane readback above. Use the 11:54 entry for current factory state and 12:51 future schedule.

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
- historical factory source-lane exhaustion / anti-repetition guard saturation from earlier 02:22 evidence; superseded by the 07:33 manual exact+recovery zero-draft readback in the current 2026-05-24 summary
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
- Supersession: source-lane zero-state from the initial exact command was superseded by the recovery manifest+Airtable+403 state, and that prior recovery state is now separate from the current factory state `historical 07:41 zero-draft output superseded by 09:01 manifest+403` / `historical 07:33 zero-state superseded by 09:01 manifest+403`. Current factory blocker is source-lane exhaustion from the 07:33 manual exact+recovery zero-draft readback; prior blockers are Zernio account/API access and source-topic routing.

### Links
- Memory note: [[Aion OS/Aion Learning Lab/Zernio Growth/Zernio Growth Memory]]
- Master state: [[Aion OS/Projects/genlabs-ai-learning-state]]
- Self-improvement SOP: [[Aion OS/SOPs/genlabs-ai-learning-self-improvement-system]]



## Historical 2026-05-24 section superseded by current summary

<!-- ZG-DLOG-2026-05-24-1000-BREAKOUT-WATCH -->
- 10:00 Breakout Watch: no formal breakout after import `2026-05-24_10-02-48.md` / Airtable `2026-05-24T10:01:31.944012+00:00`; read-only comparison found 0 movers. Best post remains ChatGPT productivity/workflow `7634027210248097042` at 32,072 views / 429 shares / gap 67,928. Factory current state is `historical 10:31 zero-state superseded by 11:54 readback` zero-draft/source-lane exhaustion; prior 09:12 Zernio POST 403 is separate. CTA guard unsafe_count=0. Factory process check `historical 10:48 process check superseded by 11:55 readback`.

<!-- ZG-DLOG-2026-05-24-0635-ISSUE-CHECK -->
### Issue-check 06:35 UTC — CTA guard clean; later readbacks superseded scheduler watch
- CTA guard: unsafe_count=0; `7634027210248097042` remains ChatGPT productivity/workflow evidence, not product-photo/no-prompt CTA evidence.
- Analytics: earlier issue-check no-breakout evidence was superseded by latest import `2026-05-24_10-02-48.md` and comparison `2026-05-24T08:39:12.373669+00:00`, which found only below-threshold movement `7641239648790007048` +3 to 1772. Best remains 32,072 views / 429 shares / gap 67,928.
- Scheduler/readbacks: the watch opened by issue-check is resolved by later import `2026-05-24_10-02-48.md`, breakout `2026-05-24_10-12-32.md`, issue `2026-05-24_07-11-22.md`, and factory `historical 07:41 zero-draft output superseded by 09:01 manifest+403` readbacks. Current growth-check output is in-flight until delivery, not a scheduler miss.
- Safety: no generation, no public posting, no spend, no Zernio send.

<!-- ZG-DLOG-2026-05-24-0700-SCHEDULER-READBACK-WATCH -->
### Scheduler readback 07:00 UTC — resolved by growth-check final readback
- Evidence: import `2026-05-24_10-02-48.md` and breakout `2026-05-24_10-12-32.md` delivered; live jobs are enabled/scheduled/last_status=ok and future-scheduled (`import 2026-05-24T08:30:00+00:00`, `breakout 2026-05-24T08:30:00+00:00`). Issue-check `2026-05-24_07-11-22.md` also delivered.
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
- Readback: growth `2026-05-24_08-15-07.md` delivered; current breakout-watch markdown is in-flight until delivery, not a scheduler miss. No generation, public posting, spend, or Zernio send.

<!-- ZG-DLOG-2026-05-24-0841-FACTORY-SCHEDULER-WATCH -->
### Factory scheduler 08:41 UTC — factory-only readback watch open
- Evidence: final breakout-watch readback `historical 08:46 process check superseded by 09:09 readback` crossed factory due `historical 08:41 due time superseded by 09:01 readback`; factory output is superseded by 09:01 manifest+403 `historical 07:41 zero-draft output superseded by 09:01 manifest+403` and 09:01 manual exact readback produced manifest+Airtable before Zernio POST 403; no lingering process remains.
- Split truth: analytics remains no-candidate after import `2026-05-24_10-02-48.md` / comparison `2026-05-24T08:39:12.373669+00:00`; current breakout markdown is in-flight until delivery, not a scheduler miss. Factory scheduler watch is separate from breakout evidence.
- Action: historical scheduler concern was later resolved by the 13:30 manual exact+recovery readback; no generation, public posting, spend, or Zernio send occurred.

<!-- ZG-DLOG-2026-05-24-0000-EXPERIMENT-CREATOR -->
### Historical experiment creator 00:00 UTC — API failure superseded by 12:00 specs
- Previous output `2026-05-24_12-19-41.md` failed after 3 API retries; this is now historical context.
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
