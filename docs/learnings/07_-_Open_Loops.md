# Open Loops

Track unresolved items that are active but not yet durable decisions or completed tasks.

## Current Open Loops
- [x] KPI blocker watch resolved: 2026-05-04T19:37Z hourly Zernio draft factory produced no draft because FAL/GPT Image 2 timed out during image generation for `evergreen-chatgpt-image-analysis-ad-critique`; partial folder had 5 PNGs/no manifest and no Airtable/Zernio record. Partial-generation guard was patched/tested, and the follow-up 2026-05-04T20:48Z factory run created verified draft `69f906012500d70628fa4ddb` from `evergreen-canva-ai-7-promo-design-tips`; production cron remained enabled/scheduled.
- [ ] Decide whether to use one master project hub or domain-specific folders.
- [ ] Decide when to automate note creation or summaries.
- [ ] Define the first free GenLabs resource for the TikTok funnel.
- [ ] Decide the minimum human-review threshold before auto-posting.
- [ ] Define the TikTok analytics ingestion path for the learning loop.
- [x] Zernio analytics sync watch: confirmed `dataStaleness.staleAccountCount=0`, `syncTriggered=false`, and fresh import at 2026-04-30T00:37Z.
- [x] Monitor the patched `AI Signal Radar scheduled dry-run` lightweight official-source slice for one successful scheduled run after 2026-05-03T00:43Z. Evidence: broad `--query-limit 8 --max-items 150 --cleanup-apply` timed out repeatedly; verified slice `context-openai,context-anthropicai,context-cursor_ai` succeeded in 30.086s with raw_seen=1/candidates=1/a_tier=0/no publish/no cleanup. 2026-05-03T18:31Z issue-check verified the scheduled dry-run job last_status=ok, so the monitor condition is satisfied; keep the separate broad-collector repair loop open. Owner: Hermes issue-check. Deadline: closed.
- [ ] Repair broad AI Signal Radar collection separately: root-cause repeated Apify collect timeouts before restoring `--query-limit 8 --max-items 150 --cleanup-apply`; keep the cron on the lightweight no-publish/no-cleanup slice until the broad collector passes a tracked verification run. Owner: Hermes trend system. Deadline: 2026-05-04.
<!-- ZG-2026-05-05-2200-GROWTH-CHECK -->
- [ ] Add experiment result tracking for active Zernio remixes: 16:32 import evidence moved onboarding/docs `7635310153126087954` to 7,526/58 (+75 refresh-window) and prompt-context `7636609137673014535` to 617/9 (+26) after the 16:30 zero baseline. Result closure remains required before new near-duplicate ChatGPT/onboarding/software-tip variants; no duplicate generation.
<!-- ZG-FACTORY-PAUSE-AUDIT -->
- [x] Zernio factory pause audit superseded by Sway no-pause KPI rule: do not keep hourly draft factory `a97a7703af32` paused as a safety shortcut. Production must stay enabled/scheduled in draft-only safety mode while reconciliation/source-topic QA continues.
<!-- ZG-FACTORY-RECONCILE-WHILE-ACTIVE -->
- [x] Latest hourly factory status resolved: 2026-05-06 16:54 run created verified review-only draft `69fb7225b55ece7737abf0dd` from `kpi050616-perplex` / Airtable `reciwZq75OIk2mJqG`. Manifest has 7 content slides plus reusable CTA = 8 media; live/rebuilt safety passed (`status=draft`, no `publishNow`, outbound payload omitted `scheduledFor`, TikTok draft true, media_count=8, TikTok/Facebook/Instagram accounts verified, FB/IG first comments exact-match). Public text/prompt leakage scan clean. Cron `a97a7703af32` remains enabled=True/state=scheduled/schedule=every 60m/next_run_at=`2026-05-06T17:46:36.427335+00:00`; no lingering factory process found.
<!-- ZG-FACTORY-SOURCE-TOPIC-QA -->
- [ ] Factory source-topic routing QA remains active: 2026-05-06 16:54 draft `69fb7225b55ece7737abf0dd` / source `kpi050616-perplex` should teach Perplexity, citations, source-checking, and market/competitor research, but the public/rendered carousel teaches generic AI prompt-context (`บริบทก่อน คำสั่งทีหลัง`) and does not visibly mention the expected Perplexity workflow. Treat as draft-safe but **not KPI-ready**; repair KPI/backstop source-topic routing and copy generation before counting these software-tip drafts as ready. Keep the hourly cron enabled/scheduled; do not pause production as a safety shortcut.
<!-- ZG-SCHEDULER-CADENCE-WATCH-2026-05-05 -->
- [x] Superseded scheduler readback history: 09:35 resolved_current_tick is historical; current scheduler truth is tracked under `ZG-SCHEDULER-CADENCE-WATCH`.
<!-- PROMPT-DROP-MANIFEST-SCHEMA-BLOCKER-2026-05-03 -->
- [ ] Prompt Drop QA/Zernio verification blocker + latest production update: 2026-05-06T13:36Z batch `prompt-drop-20260506T1304Z-latest-slate-slots01-05` generated 5 complete GPT Image 2 low native sets from validated latest-slate slots `1,2,4,5,6` after slot 3 (`03-graduation-beauty-portrait-kit`) failed GPT Image 2/FAL 422 on slide 1. Dry-run/payload gates passed 5/5: long Thai prompt-giveaway descriptions 3966 chars with hashtags, visual intention and packaging/service rules present, exact default hashtags, no public GenLabs/genlabs.in.th/no-prompt promo, `isDraft=true`, `tiktokSettings.draft=true`, no outbound `publishNow`/`scheduledFor`.
  - Fresh visual QA: PASS 4 / WARN 1 / FAIL 0. Clean PASS drafts created only for `02-moving-day-kit` → `69fb4222c02731101190b321`, `04-florist-care-card-kit` → `69fb4223c02731101190b378`, `05-sneaker-care-box` → `69fb4224c02731101190b3b4`, and `06-reservation-table-kit` → `69fb42253e9d661e0a81e923`. API evidence: HTTP 200, `status=draft`, TikTok draft true, photo media_count=5, publishAttempts=0, no public promo. Server `scheduledFor` metadata is safe echo because draft flags/status are true and outbound payload omitted scheduling.
  - Manual-review/no-draft rows: `01-pore-safe-refill-calendar` is dry-run safe but visual WARN due acne/skin-treatment claim review risk and blemish macro imagery; no Zernio draft created. `03-graduation-beauty-portrait-kit` has no complete manifest and no draft after GPT Image 2/FAL 422.
  - Report: `/home/clawd/.hermes/ai_signal_radar/prompt_drop/production/2026-05-06T1336Z-prompt-drop-latest-slate-slots01-02-04-05-06-production.md`; JSON: `/home/clawd/.hermes/ai_signal_radar/prompt_drop/production/2026-05-06T1336Z-prompt-drop-latest-slate-slots01-02-04-05-06-production.json`; contact sheet: `/home/clawd/.hermes/ai_signal_radar/prompt_drop/production/contact_sheets/2026-05-06T1327Z-prompt-drop-slots01-02-04-05-06-contact-sheet.jpg`.
  - Older blockers still stand: old rejected `thai-realistic-skin-serum-prompt-drop-2026-05-03` / `69f706f2fc6b7a5c36445f00`, Flux/generic-generator coffee replacement `69f71c2ae923876e52080cc1`, `rainy-bangkok-streetwear-lookbook` API-403 draft `69f761d47aa7b46ff03d2598`, and prototype/style-exploration folders remain blocked. WARN rows are not clean Prompt Drop review volume until Sway manually accepts or they are regenerated. Owner: Hermes Prompt Drop verifier/factory. Deadline: before next Prompt Drop review batch.
<!-- ZG-2026-05-06-0034-ISSUE-CHECK -->
- [x] Superseded by 2026-05-06 11:30/11:33 Breakout Watch: latest normal baseline has `breakout_candidates=[]`; direct import `2026-05-06_11-33-05.md` plus Airtable comparison `2026-05-06T11:34:01.365430+00:00` found zero movers. Earlier positive movement is context only; see `ZG-2026-05-06-1130-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-0330-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 11:30/11:33 Breakout Watch: latest normal baseline has `breakout_candidates=[]`; direct import `2026-05-06_11-33-05.md` plus Airtable comparison `2026-05-06T11:34:01.365430+00:00` found zero movers. Earlier positive movement is context only; see `ZG-2026-05-06-1130-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-0400-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 11:30/11:33 Breakout Watch: latest normal baseline has `breakout_candidates=[]`; direct import `2026-05-06_11-33-05.md` plus Airtable comparison `2026-05-06T11:34:01.365430+00:00` found zero movers. Earlier positive movement is context only; see `ZG-2026-05-06-1130-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-0400-GROWTH-CHECK -->
- [x] Superseded by 2026-05-06 11:30/11:33 Breakout Watch: latest normal baseline has `breakout_candidates=[]`; direct import `2026-05-06_11-33-05.md` plus Airtable comparison `2026-05-06T11:34:01.365430+00:00` found zero movers. Earlier positive movement is context only; see `ZG-2026-05-06-1130-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-0600-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 11:30/11:33 Breakout Watch: latest normal baseline has `breakout_candidates=[]`; direct import `2026-05-06_11-33-05.md` plus Airtable comparison `2026-05-06T11:34:01.365430+00:00` found zero movers. Earlier positive movement is context only; see `ZG-2026-05-06-1130-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-0600-GROWTH-CHECK -->
- [x] Superseded by 2026-05-06 11:30/11:33 Breakout Watch: latest normal baseline has `breakout_candidates=[]`; direct import `2026-05-06_11-33-05.md` plus Airtable comparison `2026-05-06T11:34:01.365430+00:00` found zero movers. 11:01 positive momentum is context only; see `ZG-2026-05-06-1130-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-0630-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 11:30/11:33 Breakout Watch: latest normal baseline has `breakout_candidates=[]`; direct import `2026-05-06_11-33-05.md` plus Airtable comparison `2026-05-06T11:34:01.365430+00:00` found zero movers. 11:01 positive momentum is context only; see `ZG-2026-05-06-1130-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-0731-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 11:30/11:33 Breakout Watch: latest normal baseline has `breakout_candidates=[]`; direct import `2026-05-06_11-33-05.md` plus Airtable comparison `2026-05-06T11:34:01.365430+00:00` found zero movers. 11:01 positive momentum is context only; see `ZG-2026-05-06-1130-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-1000-GROWTH-CHECK -->
- [x] Superseded by 2026-05-06 11:30/11:33 Breakout Watch: latest normal baseline has `breakout_candidates=[]`; direct import `2026-05-06_11-33-05.md` plus Airtable comparison `2026-05-06T11:34:01.365430+00:00` found zero movers. 11:01 positive momentum is context only; see `ZG-2026-05-06-1130-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-1000-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 11:30/11:33 Breakout Watch: latest normal baseline has `breakout_candidates=[]`; direct import `2026-05-06_11-33-05.md` plus Airtable comparison `2026-05-06T11:34:01.365430+00:00` found zero movers. 11:01 positive momentum is context only; see `ZG-2026-05-06-1130-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-1101-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 11:30/11:33 Breakout Watch: latest normal baseline has `breakout_candidates=[]`; direct import `2026-05-06_11-33-05.md` plus Airtable comparison `2026-05-06T11:34:01.365430+00:00` found zero movers. 11:01 positive momentum is context only; see `ZG-2026-05-06-1130-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-1130-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 13:02 Breakout Watch: 13:02 normal baseline confirmed the onboarding/docs (+51), prompt-context (+86), and brand-direction/logo (+131) movements; 13:05 import found no post-baseline movement. Current evidence lives in `ZG-2026-05-06-1302-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-1302-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 14:30 Breakout Watch: latest confirmed baseline evidence is under `ZG-2026-05-06-1430-BREAKOUT-WATCH`; 13:02 candidate numbers are previous context only.
<!-- ZG-2026-05-06-1400-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 14:30 Breakout Watch: 14:00 baseline had no current candidate, but 14:30 normal baseline confirmed onboarding/docs and prompt-context movement; current evidence lives in `ZG-2026-05-06-1430-BREAKOUT-WATCH`. No public posting/spend/generation; keep result-closure/factory QA gates open.
<!-- ZG-2026-05-06-1430-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 16:30/16:32 Breakout Watch: 14:30 and 15:44 positive baselines are previous context only; current evidence lives in `ZG-2026-05-06-1630-BREAKOUT-WATCH` after the 16:32 import moved onboarding/docs to 7,526/58 (+75) and prompt-context to 617/9 (+26).
<!-- ZG-2026-05-06-1544-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 16:30/16:32 Breakout Watch: 15:44 onboarding/docs +107 and prompt-context +54 are previous positive context only; 16:32 import movement is the current watch state. Current evidence lives in `ZG-2026-05-06-1630-BREAKOUT-WATCH`.


<!-- ZG-2026-05-06-1601-GROWTH-CHECK -->
- [x] Superseded by 2026-05-06 16:30/16:32 Breakout Watch: 16:30 normal baseline confirmed zero, then import `2026-05-06_16-32-20.md` moved onboarding/docs to 7,526/58 (+75 refresh-window) and prompt-context to 617/9 (+26). Current evidence lives in `ZG-2026-05-06-1630-BREAKOUT-WATCH`; no public posting/spend/generation.

<!-- ZG-2026-05-06-1630-BREAKOUT-WATCH -->
- [ ] 2026-05-06 16:30/16:32 UTC Breakout Watch: onboarding/docs `7635310153126087954` is the current post-import refresh-window candidate at 7,526 views/58 shares/gap 92,474 (+75 after `2026-05-06_16-32-20.md`); prompt-context `7636609137673014535` is secondary at 617/9 (+26). Keep 16:30 confirmed baseline delta=0 and treat hourly rates as import-window inflated until next >15m baseline. Update existing result-closure/amplification task; no duplicate generation, public posting, or spending.

## Rules
- If an item becomes a commitment, move it into a project note.
- If an item becomes a decision, log it in [[Aion OS/02 - Decision Log]].
- If an item is stale, archive or delete it.

## 2026-05-02 Zernio breakout tasks
- [ ] Zernio breakout watch: draft-only amplify post 7635243951582088456 (meeting-summary → action-list/saveable workflow) with one remix, one follow-up post, and a pinned/comment prompt. Evidence: 112 views at 2.75h, 3 shares, 10.71% engagement, 2.679% share rate on 2026-05-02.
- [ ] Growth check task: create 3 draft-only ChatGPT productivity remixes from true winner 7634027210248097042: self-review from work evidence, 30-day onboarding plan, and project brief/action-items workflow. Do not reuse protected GenLabs CTA as hook/topic evidence; measure against channel average and current 15,893-view ChatGPT productivity leader.
- [ ] 2026-05-02 Breakout watch: create 3 draft-only remixes for TikTok 7635243951582088456 (meeting summaries → decisions/action items/owners/deadlines), and add one comment/save CTA prompt if posting permissions allow. KPI reason: 366 views at 3.74h, +254 since baseline, ~584 views/hr, 5.74% engagement.
- [ ] Zernio amplification: draft 3 ChatGPT practical-work remixes from TikTok 7634027210248097042 (self-review, onboarding plan, project brief/action items); add save/comment prompts; verify 2h/24h metrics. Created 2026-05-02T15:30:55Z.
- [ ] 2026-05-02 Growth check: close the active ChatGPT productivity remix task before creating more near-duplicate experiments. Measure whether self-review/onboarding/project-brief variants beat the 817-view channel average and the 6,482-view winner pattern; decide continue/stop/remix after 4h/24h data.

## Zernio growth-check 2026-05-02 — ChatGPT productivity breakout amplification
- Status: open
- Created: 2026-05-02 growth-check cron
- 2026-05-06T16:32Z breakout-watch update: import `2026-05-06_16-32-20.md` moved onboarding/docs `7635310153126087954` to 7,526/58 (+75 refresh-window) and prompt-context `7636609137673014535` to 617/9 (+26) after the 16:30 zero baseline. Factory remains active/recovered; latest verified draft-only run is `69fb7225b55ece7737abf0dd` from `kpi050616-perplex` with draft safety passed but source-topic QA caveat, and cron stays enabled/scheduled. Result-closure remains the main growth gate; scheduler readback is resolved_current_tick.
- Task: create draft-only remix/follow-up set from the true winning educational pattern, not the protected GenLabs CTA.
- Drafts to create next production cycle:
  1. “ChatGPT ตรวจงานตัวเองก่อนส่งให้หัวหน้า” — self-review from real work evidence.
  2. “ChatGPT ทำแผน onboarding 30 วันให้พนักงานใหม่” — department/team practical workflow.
  3. “เปลี่ยนงานกว้าง ๆ เป็น project brief + action items ด้วย ChatGPT” — vague task to concrete execution.
- Amplification: add/save/comment prompt asking viewers which workflow they want as a template; repurpose best variant into Thai narration slideshow if velocity continues.
- Close condition: 4h/24h analytics captured and decision marked continue/stop/remix.
- [x] 11:30/11:33 breakout-watch zero baseline plus `2026-05-06_11-33-05.md` no-change verification supersedes the earlier 11:01 candidate evidence; 11:56 factory run resolved the scheduler-watch concern, while factory editorial/source-topic QA remains open.


<!-- ZG-2026-05-03-1200-EXPERIMENT-CREATOR -->
- [x] Superseded historical experiment-creator marker; see the current 2026-05-06 experiment-creator marker for the 10:00 confirmed growth gate. No duplicate active task.
<!-- ZG-2026-05-04-0000-EXPERIMENT-CREATOR -->
- [x] Superseded historical experiment-creator marker; see the current 2026-05-06 experiment-creator marker for the 10:00 confirmed growth gate. No duplicate active task.
<!-- ZG-2026-05-04-1200-EXPERIMENT-CREATOR -->
- [x] Superseded historical experiment-creator marker; see the current 2026-05-06 experiment-creator marker for the 10:00 confirmed growth gate. No duplicate active task.
<!-- ZG-2026-05-05-0008-EXPERIMENT-CREATOR -->
- [x] Superseded historical experiment-creator marker; see the current 2026-05-06 experiment-creator marker for the 10:00 confirmed growth gate. No duplicate active task.
<!-- ZG-2026-05-06-0011-EXPERIMENT-CREATOR -->
- [ ] 2026-05-06 16:32 UTC Experiment Creator/growth gate update: ChatGPT productivity winner remains under result-closure; post-import evidence moved onboarding/docs `7635310153126087954` to 7,526/58 (+75 refresh-window) and prompt-context `7636609137673014535` to 617/9 (+26), but rates are import-window inflated after the 16:30 zero baseline. Factory `a97a7703af32` remains enabled/scheduled and latest output created verified draft-only `69fb7225b55ece7737abf0dd` from `kpi050616-perplex` with source-topic QA caveat; do not public post, spend, or generate extra near-duplicate variants until result-closure gates close. Scheduler readback is resolved_current_tick.
<!-- ZG-2026-05-06-1400-GROWTH-CHECK -->
- [x] 2026-05-06 14:00/14:01 Growth Check sync is superseded by 16:30/16:32 Breakout Watch evidence under `ZG-2026-05-06-1630-BREAKOUT-WATCH`; 16:32 import movement is the current watch state and existing result-closure/factory/scheduler tasks are updated.
<!-- ZG-SCHEDULER-CADENCE-WATCH -->
- [x] Scheduler readback resolved_current_tick at 2026-05-06T16:39:33Z: analytics import output `2026-05-06_16-32-20.md` is observed with status ok/fresh (41 seen, 0 created, 41 updated) and Airtable Imported At `2026-05-06T16:31:59.942998+00:00`; read-only comparison `2026-05-06T16:32:27.832147+00:00` found post-import movement versus the 16:30 live zero baseline. Import job last_run_at=2026-05-06T16:32:20.434165+00:00 next_run_at=2026-05-06T17:00:00+00:00; current breakout-watch report is in-flight until delivery while latest completed output remains `2026-05-06_16-00-36.md` and next_run_at=2026-05-06T17:00:00+00:00; growth-check latest output `2026-05-06_16-13-12.md` next_run_at=2026-05-06T18:00:00+00:00; factory latest verified run `2026-05-06T16:54Z` / draft `69fb7225b55ece7737abf0dd`, next_run_at=2026-05-06T17:46:36.427335+00:00. No scheduler repair, pause, public posting, spending, or extra generation was triggered.
