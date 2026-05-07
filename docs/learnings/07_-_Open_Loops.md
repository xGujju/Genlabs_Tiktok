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
<!-- ZG-2026-05-07-0009-GROWTH-CHECK -->
- [x] Superseded by 2026-05-07 01:31/01:32 Breakout Watch confirmed baseline; current evidence lives in `ZG-2026-05-07-0131-BREAKOUT-WATCH`. No public posting/spend/generation.


<!-- ZG-FACTORY-PAUSE-AUDIT -->
- [x] Zernio factory pause audit superseded by Sway no-pause KPI rule: do not keep hourly draft factory `a97a7703af32` paused as a safety shortcut. Production must stay enabled/scheduled in draft-only safety mode while reconciliation/source-topic QA continues.
<!-- ZG-FACTORY-RECONCILE-WHILE-ACTIVE -->
- [x] Superseded hourly factory readback catch-up: latest current evidence moved to `ZG-FACTORY-SOURCE-TOPIC-QA` on 2026-05-07T10:39:42Z. The exact factory command first returned `draft_count=0`; recovery rerun found YouTube fallback `yt-2ONRbv-XzH0` but failed during FAL/GPT Image 2 edit before manifest/Zernio. Previous safe draft `69fc21af9702cb029115225a` / Airtable `recbospvb489IyDWw` / source `kpi050705-canvap` remains draft-safe but not KPI-ready because Canva/Magic Design source-topic fit failed.


<!-- ZG-FACTORY-SOURCE-TOPIC-QA -->
- [ ] Factory copy/source QA remains open for editorial polish/anti-repetition. Latest safe draft is `2026-05-07T15:56:43.287790+00:00` / Zernio `69fcb639c8e9e6c70a69c24a` / Airtable `recQbcvo3MVmkSYaO` / source `ai-word-api-plain-human`; API AI-word topic fit and draft safety passed, with minor Thai spacing/naturalness/caption-depth polish for Sway review. Production remains enabled/draft-only; scheduler watch below is resolved by this run.

<!-- ZG-SCHEDULER-CADENCE-WATCH-2026-05-05 -->
- [x] Scheduler readback watch resolved by 2026-05-07T12:54Z exact factory evidence: `draft_count=1`, Airtable/Zernio draft verified, no lingering `scheduled_ai_social_draft_factory.py` process, production cron remains enabled/scheduled. No scheduler repair/public posting/spend/live publishing.
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
- [x] Superseded by 2026-05-06 14:30 Breakout Watch: 14:42 baseline had no current candidate, but 14:30 normal baseline confirmed onboarding/docs and prompt-context movement; current evidence lives in `ZG-2026-05-06-1430-BREAKOUT-WATCH`. No public posting/spend/generation; keep result-closure/factory QA gates open.
<!-- ZG-2026-05-06-1430-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 16:30/16:32 Breakout Watch: 14:30 and 15:44 positive baselines are previous context only; current evidence lives in `ZG-2026-05-06-1701-BREAKOUT-WATCH` after the 16:32 import moved onboarding/docs to 7,526/58 (+75) and prompt-context to 617/9 (+26).
<!-- ZG-2026-05-06-1544-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 16:30/16:32 Breakout Watch: 15:44 onboarding/docs +107 and prompt-context +54 are previous positive context only; 17:01 confirmed baseline is the current watch state. Current evidence lives in `ZG-2026-05-06-1701-BREAKOUT-WATCH`.


<!-- ZG-2026-05-06-1601-GROWTH-CHECK -->
- [x] Superseded by 2026-05-06 16:30/16:32 Breakout Watch: 16:30 normal baseline confirmed zero, then import `2026-05-06_16-32-20.md` moved onboarding/docs to 7,526/58 (+75 refresh-window) and prompt-context to 617/9 (+26). Current evidence lives in `ZG-2026-05-06-1701-BREAKOUT-WATCH`; no public posting/spend/generation.

<!-- ZG-2026-05-06-1630-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 17:01 Breakout Watch: 16:30/16:32 import-window evidence is now confirmed by the 17:01 normal baseline; current evidence lives in `ZG-2026-05-06-1701-BREAKOUT-WATCH`.

<!-- ZG-2026-05-06-1701-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 17:30/17:31/17:38 Breakout Watch: 17:30 normal baseline had no top-level candidate, then direct import/live snapshot found refresh-window candidates. Current evidence lives in `ZG-2026-05-06-1730-BREAKOUT-WATCH`; no public posting/spend/generation.


<!-- ZG-2026-05-06-1730-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 18:30/18:32 Breakout Watch: 17:51 confirmed movement and 18:01 no-change are previous context; the 18:30 zero baseline plus 18:32 import-window movement is current under `ZG-2026-05-06-1830-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-1830-ISSUE-CHECK -->
- [x] 2026-05-06 18:30/18:31/18:35 UTC Issue Check superseded/resolved by final readback: 18:30 baseline confirmed zero/no top-level breakout, then import output `2026-05-06_18-32-34.md` updated Airtable and read-only comparison found refresh-window movers: onboarding/docs `7635310153126087954` 7,555/58 (+11), prompt-context `7636609137673014535` 672/9 (+24), meeting-notes `7634893611389259016` 1,609/15 (+7), primary KPI `7634027210248097042` 15,893/240 (+0). Factory recovered with safe review-only draft `69fb8760f83e92d74dd610da`; source-topic/tip-count QA remains open. Scheduler readback is resolved_current_tick (import/factory future; current breakout output in-flight until delivery). CTA guard unsafe count=0; no public posting/spend/generation.

<!-- ZG-2026-05-06-1830-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 19:00 Breakout Watch: 18:30/18:32 import-window movement did not become a current candidate; the 19:00 baseline returned no breakout candidates and 19:02 direct import found no post-baseline movement. Current evidence lives in `ZG-2026-05-06-1900-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-1900-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 19:30/19:32 Breakout Watch: 19:00 no-candidate/no-change is historical; direct/scheduled import `2026-05-06_19-32-16.md` moved meeting-action `7635243951582088456` and two secondary posts into refresh-window candidates. Current evidence lives in `ZG-2026-05-06-1930-BREAKOUT-WATCH`.
<!-- ZG-2026-05-06-1930-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 20:00/20:02 Growth Check: 19:32 refresh-window meeting-action candidate was demoted; 20:00 baseline returned `breakout_candidates=[]`, confirmed `7635243951582088456` only +4 (~7.97/hr), and direct import `2026-05-06T20:02:08.166781+00:00` found zero movers. Current evidence lives in `ZG-2026-05-06-2000-BREAKOUT-WATCH` / `ZG-2026-05-06-2000-GROWTH-CHECK`.
<!-- ZG-2026-05-06-2000-GROWTH-CHECK -->
- [x] Superseded by 2026-05-06 22:00/22:02 Breakout/Growth readback: 20:00 and 20:30/20:32 candidate evidence is historical; current evidence lives in `ZG-2026-05-06-2200-GROWTH-CHECK` after import `2026-05-06_22-02-01.md` moved meeting-action to 2,375/22 (+5 import-window). No public posting/spend/generation.


<!-- ZG-2026-05-06-2200-BREAKOUT-WATCH -->
- [x] Superseded/merged into `ZG-2026-05-06-2200-GROWTH-CHECK`: same 22:00/22:02 evidence is tracked by the single active result-closure task. Meeting-action `7635243951582088456` moved to 2,375/22 (+5 import-window), prompt-context `7636609137673014535` to 678/9 (+4), and no public posting/spend/generation was triggered.

<!-- ZG-2026-05-06-2330-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 01:01/01:02 Breakout Watch: 00:11/00:17 confirmed candidates are historical; direct import moved onboarding/docs `7635310153126087954` to 7607/58 (+27 import-window) and prompt-context `7636609137673014535` to 741/10 (+34 import-window). Current evidence now lives in `ZG-2026-05-07-0400-GROWTH-CHECK`. No public posting/spend/generation.

<!-- ZG-2026-05-07-0101-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 01:31/01:32 Breakout Watch: 01:31 normal baseline confirmed onboarding/docs and prompt-context candidates; 01:32 import found 0 post-baseline movers. Current evidence now lives in `ZG-2026-05-07-0400-GROWTH-CHECK`.

<!-- ZG-2026-05-07-0131-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 02:00/02:01 Growth Check: 02:00 normal baseline confirmed zero/no formal breakout, then import `2026-05-07_02-01-39.md` moved onboarding/docs to 7634/58 (+27 refresh-window) and prompt-context to 771/11 (+30 refresh-window). Current evidence now lives in `ZG-2026-05-07-0400-GROWTH-CHECK`; no public posting/spend/generation.
<!-- ZG-2026-05-07-0200-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 03:00/03:02 Breakout Watch: the 02:01 refresh-window movers are context only after the 03:00 confirmed zero baseline plus 03:02 import no-change verification. Current evidence now lives in `ZG-2026-05-07-0400-GROWTH-CHECK`; no public posting/spend/generation.


<!-- ZG-2026-05-07-0200-GROWTH-CHECK -->
- [x] Superseded by 2026-05-07 03:00/03:02 Breakout Watch: latest confirmed state is no current breakout candidate; scheduled import at 03:02 found zero watched-post movers. Current evidence now lives in `ZG-2026-05-07-0400-GROWTH-CHECK`; result closure and factory QA remain open.

<!-- ZG-2026-05-07-0300-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 03:30/03:31 Breakout Watch: 03:00/03:02 no-current-candidate evidence is historical; current evidence lives in `ZG-2026-05-07-0400-GROWTH-CHECK` after import `2026-05-07_03-31-27.md` moved Claude app-brief `7633636619869900040` to 3848/25 (+422 refresh-window), prompt-context to 789/11 (+18), and onboarding/docs to 7649/58 (+15). No public posting/spend/generation.

<!-- ZG-2026-05-07-0330-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 04:03/04:05 Growth Check: 03:31 import-window Claude movement is now confirmed by normal baseline `2026-05-07T04:03:59.353161+00:00`; current evidence lives in `ZG-2026-05-07-0400-GROWTH-CHECK`. No public posting/spend/generation.

<!-- ZG-2026-05-07-0400-GROWTH-CHECK -->
- [x] Superseded by 2026-05-07 06:00 Growth Check: 04:03 Claude and 05:00 ChatGPT movements are previous context; current evidence now lives in `ZG-2026-05-07-0730-BREAKOUT-WATCH` after the 06:00 baseline confirmed digital-product workflow. No public posting/spend/generation.

<!-- ZG-2026-05-07-0430-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 06:00 Growth Check: 04:30 import-window and 05:00 ChatGPT evidence are previous context; current evidence now lives in `ZG-2026-05-07-0730-BREAKOUT-WATCH`. No public posting/spend/generation.

<!-- ZG-2026-05-07-0500-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 06:00 Growth Check: 05:00 ChatGPT productivity +917 is previous positive context; 06:00 confirmed digital-product workflow `7634047103488068871` +55 as current movement. Current evidence now lives in `ZG-2026-05-07-0730-BREAKOUT-WATCH`; no public posting/spend/generation.

<!-- ZG-2026-05-07-0534-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 06:00 Breakout Watch: 05:34/05:36/05:38 refresh-window candidates are context; the 06:00 normal baseline confirmed digital-product workflow `7634047103488068871` as the sole formal breakout candidate at 1589/12 with +55 (~129.12/hr). Current evidence now lives in `ZG-2026-05-07-0730-BREAKOUT-WATCH`. No public posting/spend/generation.

<!-- ZG-2026-05-07-0600-GROWTH-CHECK -->
- [x] Superseded by 2026-05-07 06:30/06:33 Issue Check: 06:30 normal baseline had no formal breakout/current delta 0, then import `2026-05-07_06-33-20.md` produced refresh-window movers. Current evidence lives in `ZG-2026-05-07-0802-BREAKOUT-WATCH`; no public posting/spend/generation.
<!-- ZG-2026-05-07-0600-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 06:30/06:33 Issue Check: 06:00 digital-product +55 is previous context; 06:30 baseline confirmed no formal breakout and 06:33 import moved onboarding/docs/prompt-context refresh-window candidates. Current evidence lives in `ZG-2026-05-07-0802-BREAKOUT-WATCH`; no public posting/spend/generation.
<!-- ZG-2026-05-07-0630-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 07:10/07:12 Breakout Watch: 06:30 import-window evidence is historical; 07:10 normal baseline confirmed onboarding/docs/prompt-context/visual-brief candidates, and 07:12 import found no post-baseline movement. Current evidence lives in `ZG-2026-05-07-0802-BREAKOUT-WATCH`; no public posting/spend/generation.

<!-- ZG-2026-05-07-0630-ISSUE-CHECK -->
- [x] Superseded by 2026-05-07 07:10/07:12 Breakout Watch: issue-check fixed import freshness and logged refresh-window movers, but 07:10 now confirms formal candidates and 07:12 import found no additional movers. Current evidence lives in `ZG-2026-05-07-0802-BREAKOUT-WATCH`; source-lane QA/result-closure remain open; no public posting/spend/generation.

<!-- ZG-2026-05-07-0710-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 07:30/07:32 Breakout Watch: 07:10 confirmed candidates are previous context; 07:30 baseline had zero formal candidates, then import `2026-05-07_07-32-44.md` moved onboarding/docs/prompt-context/meeting-action as import-window candidates. Current evidence lives in `ZG-2026-05-07-0802-BREAKOUT-WATCH`; no public posting/spend/generation.
<!-- ZG-2026-05-07-0730-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 08:02 Growth Check: 07:30/07:32 onboarding/docs import-window evidence is context; 08:02 confirmed prompt-context `7636998390286437650` +28 as current formal candidate. Current evidence lives in `ZG-2026-05-07-0802-BREAKOUT-WATCH` and same-window `ZG-2026-05-07-0800-GROWTH-CHECK`; no public posting/spend/generation.

<!-- ZG-2026-05-07-0802-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 09:00 Breakout Watch: 08:02 prompt-context confirmed baseline and 08:42 onboarding/docs import-window evidence are previous context; 09:00 normal baseline confirmed prompt-context `7636998390286437650` +24 (~66.71/hr). Current evidence lives in `ZG-2026-05-07-0930-BREAKOUT-WATCH`; no public posting/spend/generation.
<!-- ZG-2026-05-07-0800-GROWTH-CHECK -->
- [x] Superseded by 2026-05-07 09:00 Breakout Watch confirmed baseline: 08:02 prompt-context +28 and 08:42 onboarding/docs import-window evidence are previous context; current evidence lives in `ZG-2026-05-07-1000-GROWTH-CHECK`. Scheduler cadence resolved; result-closure and factory source-lane QA remain open. No public posting/spend/generation.
<!-- ZG-2026-05-07-0842-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 09:00 Breakout Watch: 08:42 onboarding/docs import-window evidence is previous context; 09:00 normal baseline confirmed prompt-context `7636998390286437650` +24 (~66.71/hr) as the current formal candidate. Current evidence lives in `ZG-2026-05-07-0930-BREAKOUT-WATCH`; no public posting/spend/generation.

<!-- ZG-2026-05-07-0900-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 09:30/09:32/09:33 Breakout Watch: 09:00 prompt-context +24 is previous positive context; 09:30 baseline returned no current breakout candidate and direct import found 0 movers. Current evidence lives in `ZG-2026-05-07-0930-BREAKOUT-WATCH`; no public posting/spend/generation.
<!-- ZG-2026-05-07-0930-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 12:00/12:02 Growth Check: 09:30/09:33 no-current-candidate and 10:14/11:02 import-window evidence are historical; latest current evidence lives in `ZG-2026-05-07-1400-GROWTH-CHECK` after import `2026-05-07_12-02-05.md` moved onboarding/docs to 7808/58 (+26) and Excel/CSV to 263/1 (+151). No public posting/spend/generation.
<!-- GL-SIR-2026-05-07-1000-3DAY -->
- [x] Superseded by 2026-05-07 12:00/12:02 Growth Check: 10:14 self-improvement and 11:00/11:02 breakout evidence are historical; latest current evidence lives in `ZG-2026-05-07-1400-GROWTH-CHECK`. No public posting/spend/generation.

<!-- ZG-2026-05-07-1100-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 12:00/12:02 Growth Check: 11:00/11:02 onboarding/docs import-window primary and 11:32 Excel/CSV confirmed baseline are previous context. Current evidence lives in `ZG-2026-05-07-1230-BREAKOUT-WATCH` after import `2026-05-07_12-02-05.md` moved onboarding/docs to 7808/58 (+26) and Excel/CSV to 263/1 (+151). No public posting/spend/generation.

<!-- ZG-2026-05-07-1132-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 12:00/12:02 Growth Check: 11:32 Excel/CSV `7637050938162711816` +38 (~71.58/hr) is previous positive momentum; 12:02 import made it strongest raw mover (263/1/+151) but still secondary by KPI leverage/share depth. Current evidence lives in `ZG-2026-05-07-1230-BREAKOUT-WATCH`; result closure + factory copy QA remain gates. No public posting/spend/generation.

<!-- ZG-2026-05-07-1200-BREAKOUT-WATCH -->
- [x] Superseded by current growth-check import-window readback: 12:00 no-candidate baseline is preserved as latest_confirmed_delta=0, but import `2026-05-07_12-02-05.md` completed after the baseline and produced refresh-window movers. Current evidence lives in `ZG-2026-05-07-1230-BREAKOUT-WATCH`.

<!-- ZG-2026-05-07-1200-GROWTH-CHECK -->
- [x] Superseded by 2026-05-07 12:30 Issue Check confirmed baseline: 12:00/12:02 import-window evidence is historical; latest current evidence lives in `ZG-2026-05-07-1400-GROWTH-CHECK` after normal baseline `2026-05-07T12:30:21.153446+00:00` confirmed onboarding/docs `7635310153126087954` +26 and Excel/CSV `7637050938162711816` +151. No public posting/spend/generation.


<!-- ZG-2026-05-07-1230-ISSUE-CHECK -->
- [x] Superseded by 2026-05-07 13:17 Breakout Watch final baseline: 12:30 issue-check confirmed onboarding/docs 7635310153126087954 7808/58/+26 and Excel/CSV 7637050938162711816 263/1/+151, but 13:03 import + 13:17 final snapshot is now current. Latest current evidence lives in `ZG-2026-05-07-1400-GROWTH-CHECK`.

<!-- ZG-2026-05-07-1230-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 13:17 Breakout Watch final baseline: 12:30 onboarding/docs candidate remains historical context; latest current evidence lives in `ZG-2026-05-07-1400-GROWTH-CHECK`. Factory 13:01 safe draft remains historical editorial context; the later 14:01 scheduler watch was resolved by the 14:32 exact factory run under `ZG-SCHEDULER-CADENCE-WATCH`.

<!-- ZG-2026-05-07-1303-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 14:00/14:02 Breakout Watch: 13:17 confirmed candidates are previous_positive_momentum only after the 14:42 baseline returned no current candidate and import `2026-05-07_14-02-57.md` found 0 watched-post movers. Current evidence lives in `ZG-2026-05-07-1400-GROWTH-CHECK` / `ZG-2026-05-07-1400-BREAKOUT-WATCH`; no public posting/spend/generation.

<!-- ZG-2026-05-07-1400-GROWTH-CHECK -->
- [x] Superseded by 2026-05-07 14:44/14:51 Breakout Watch import-window readback: 14:00/14:02 no-current-candidate state is historical; current evidence lives in `ZG-2026-05-07-1444-BREAKOUT-WATCH`. No public posting/spend/generation.

<!-- ZG-2026-05-07-1400-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 14:44/14:51 import readback: 14:00/14:02 no-mover context is historical; current evidence lives in `ZG-2026-05-07-1444-BREAKOUT-WATCH` after onboarding/docs moved to 7884/60/+43. Factory scheduler resolved by `2026-05-07_14-41-45.md`; no public posting/spend/generation.

<!-- ZG-2026-05-07-1442-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 14:44/14:51 import readback: 14:42 no-candidate baseline remains latest confirmed delta=0, but import `2026-05-07_14-44-38.md` moved onboarding/docs to 7884/60/+43. Current evidence lives in `ZG-2026-05-07-1444-BREAKOUT-WATCH`; no public posting/spend/generation.

<!-- ZG-2026-05-07-1444-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 15:02 Breakout Watch confirmed baseline: 14:44 import-window onboarding/docs movement is now formal current evidence under `ZG-2026-05-07-1502-BREAKOUT-WATCH`; no public posting/spend/generation.

<!-- ZG-2026-05-07-1502-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 16:06 Breakout Watch: 15:02 onboarding/docs `7635310153126087954` 7884/60/+43 and 15:30/15:31 refresh-window evidence are previous context; 16:06 normal baseline confirmed onboarding/docs 7932/60/+48 as current formal evidence. Current evidence lives in `ZG-2026-05-07-1606-BREAKOUT-WATCH`; no public posting/spend/generation.

<!-- ZG-2026-05-07-1530-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 16:06 Breakout Watch confirmed baseline: the 15:30/15:31 refresh-window onboarding/docs movement is now formal current evidence under `ZG-2026-05-07-1606-BREAKOUT-WATCH`; no public posting/spend/generation.

<!-- ZG-2026-05-07-1600-GROWTH-CHECK -->
- [x] Superseded by 2026-05-07 16:30/16:33 Breakout Watch: 16:06 confirmed onboarding/docs evidence is previous_positive_momentum; current actionable evidence lives in `ZG-2026-05-07-1630-BREAKOUT-WATCH` after import `2026-05-07_16-33-12.md` moved onboarding/docs to 7972/61/+40. No public posting/spend/generation.
<!-- ZG-2026-05-07-1606-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-07 16:30/16:33 Breakout Watch: 16:06 baseline candidate is previous positive context; current evidence lives in `ZG-2026-05-07-1630-BREAKOUT-WATCH` after the 16:30 zero baseline and late import `2026-05-07_16-33-12.md` produced refresh-window movers. No public posting/spend/generation.

<!-- ZG-2026-05-07-1630-BREAKOUT-WATCH -->
- [ ] 2026-05-07 16:30/16:33 Breakout Watch: formal baseline `2026-05-07T16:30:01.269666+00:00` returned no top-level breakout candidates, then late import `2026-05-07_16-33-12.md` / comparison `2026-05-07T16:34:20.459250+00:00` moved onboarding/docs `7635310153126087954` to 7972/61/+40 and meeting/action `7635243951582088456` to 2617/23/+39. Treat rates as import-window inflated until next normal baseline; update existing onboarding/docs task only; result closure/backfill/editorial QA gates remain open. No public posting/spend/generation/live schedule.

## Rules
- If an item becomes a commitment, move it into a project note.
- If an item becomes a decision, log it in [[Aion OS/02 - Decision Log]].
- If an item is stale, archive or delete it.

## 2026-05-02 Zernio breakout tasks
- [x] Superseded by 21:02/21:03 no-current-candidate evidence: meeting-action `7635243951582088456` is watch-only at 2,370/22 with +4 below threshold; keep result closure above and wait for a future normal baseline before scaling.
- [ ] Growth check task: create 3 draft-only ChatGPT productivity remixes from true winner 7634027210248097042: self-review from work evidence, 30-day onboarding plan, and project brief/action-items workflow. Do not reuse protected GenLabs CTA as hook/topic evidence; measure against channel average and current 16810-view ChatGPT productivity leader.
- [x] Superseded by the refreshed single current task above for TikTok 7635243951582088456; avoid three near-duplicate remixes until result closure confirms the meeting-action variant should scale.
- [ ] Zernio amplification: draft 3 ChatGPT practical-work remixes from TikTok 7634027210248097042 (self-review, onboarding plan, project brief/action items); add save/comment prompts; verify 2h/24h metrics. Created 2026-05-02T15:30:55Z.
- [ ] 2026-05-02 Growth check: close the active ChatGPT productivity remix task before creating more near-duplicate experiments. Measure whether self-review/onboarding/project-brief variants beat the 817-view channel average and the 6,482-view winner pattern; decide continue/stop/remix after 4h/24h data.

## Zernio growth-check 2026-05-02 — ChatGPT productivity breakout amplification
- Status: open
- Created: 2026-05-02 growth-check cron
- 2026-05-07T16:33Z update: current actionable evidence is the 16:30 zero baseline plus 16:33 post-import refresh-window movers. Onboarding/docs `7635310153126087954` is 7972/61/+40 (import-window inflated); best ChatGPT productivity `7634027210248097042` remains 16810/255/+0 and the protected CTA is promo copy only. Close result loops/backfill and wait next normal baseline before generating; scheduler readback is resolved/current; factory `2026-05-07_16-05-49.md` / `69fcb639c8e9e6c70a69c24a` is scheduler-safe/editorial-QA-open. No public posting/spend/generation.

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
<!-- ZG-2026-05-07-1200-EXPERIMENT-CREATOR -->
- [ ] 2026-05-07 12:00 Experiment Creator/growth gate update, refreshed by 16:30/16:33 breakout readback: exactly 3 draft-only recovery backlog specs remain staged — 1) ChatGPT Image Ad Critique — 8 checks (8/8 tips); 2) NotebookLM PDF Comparison Decision Table — 7 tips (7/7 tips); 3) Gemini Sheets Sales Report Cleanup — 7 tips (7/7 tips). Latest KPI evidence: ChatGPT productivity winner `7634027210248097042` is 16810/255/gap 83190 with +0; onboarding/docs `7635310153126087954` is post-import refresh-window watch at 7972/61/+40 pending next normal baseline. Factory `2026-05-07_16-05-49.md` is safe/editorial-QA-open; result closure, editorial polish/source QA, structured backfill, and next-baseline confirmation remain open. Source IDs after gates close: kpi-exp-0507-1200-chatgpt-image-ad-critique, kpi-exp-0507-1200-notebooklm-pdf-comparison, kpi-exp-0507-1200-gemini-sheets-sales-report.


<!-- ZG-2026-05-06-1400-GROWTH-CHECK -->
- [x] 2026-05-06 14:00/14:01 Growth Check sync is superseded by the 2026-05-06 17:30/17:31/17:38 Breakout Watch refresh-window evidence under `ZG-2026-05-06-1730-BREAKOUT-WATCH`; existing result-closure/factory/scheduler tasks are updated.


<!-- ZG-2026-05-06-2000-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 20:30/20:32 Breakout Watch: 20:00 no-candidate/no-change evidence is historical; current evidence lives in `ZG-2026-05-06-2030-BREAKOUT-WATCH` after import catch-up moved meeting-action and landing-page into refresh-window candidates. No public posting/spend/generation.

<!-- ZG-SCHEDULER-CADENCE-WATCH -->
- [x] Scheduler readback resolved at 2026-05-07T16:38:59Z: import `2026-05-07_16-33-12.md` next `2026-05-07T17:00:00+00:00`, latest completed breakout `2026-05-07_16-23-23.md` next `2026-05-07T17:00:00+00:00`, growth `2026-05-07_16-23-45.md` next `2026-05-07T18:00:00+00:00`, and factory `2026-05-07_16-05-49.md` next `2026-05-07T17:05:50.133057+00:00` are observed/enabled/scheduled. Current 16:30 breakout output is in-flight until delivery; latest refresh-window evidence lives in `ZG-2026-05-07-1630-BREAKOUT-WATCH`. Latest factory draft `69fcb639c8e9e6c70a69c24a` / Airtable `recQbcvo3MVmkSYaO` remains draft-only with editorial QA open. No matching import_zernio_analytics_to_airtable.py / zernio_growth_snapshot.py / zernio_obsidian_daily_log.py / scheduled_ai_social_draft_factory.py / staged_ai_signal_radar.py process at 2026-05-07T16:38:59Z. No public posting/spend/live scheduling.
<!-- ZG-2026-05-06-2030-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 21:30/21:32 Breakout Watch: the 20:30/20:32 refresh-window and 21:02 +4 meeting-action evidence are historical; the 21:30 baseline had `breakout_candidates=[]`, all watched posts had delta=0, and 21:32 import/read-only comparison found zero post-baseline movers. Current evidence lives in `ZG-2026-05-06-2200-GROWTH-CHECK`.
<!-- ZG-2026-05-06-2102-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 22:00/22:02 Breakout Watch: 21:02 +4 meeting-action evidence is historical; current evidence lives in `ZG-2026-05-06-2200-GROWTH-CHECK` after import-window movement moved meeting-action to 2,375/22 (+5).
<!-- ZG-2026-05-06-2130-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 22:00/22:02 Breakout Watch: the 21:30 no-candidate/no-change evidence is historical; current evidence lives in `ZG-2026-05-06-2200-GROWTH-CHECK` after import `2026-05-06_22-02-01.md` moved meeting-action `7635243951582088456` to 2,375/22 (+5). No public posting/spend/generation.
<!-- ZG-2026-05-06-2300-BREAKOUT-WATCH -->
- [x] Superseded by 2026-05-06 23:30/23:32 Breakout Watch: 23:02 import-window candidate is context only; current evidence lives in `ZG-2026-05-06-2330-BREAKOUT-WATCH` after import `2026-05-06_23-32-17.md` found zero post-baseline movers. No public posting/spend/generation.
