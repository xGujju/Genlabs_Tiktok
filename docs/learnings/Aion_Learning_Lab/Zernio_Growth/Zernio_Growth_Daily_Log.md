# Zernio Growth Daily Log

Purpose: daily durable summaries for the 100k-view KPI loop. This note is generated/updated by Hermes.

## 2026-04-29

### KPI status
- Goal: one TikTok post reaches **100,000 views**.
- Best post: ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 @GenLabs.th —- 👋 หลายคนเห็น Claude สร้างแอปได้ แล้วรีบพิมพ์ว่า “ช่วยทำแอป…
- Current best views: 1204
- Gap to 100,000: 98796
- Closest post views: 1204
- Strongest velocity post: ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 @GenLabs.th —- 👋 หลายคนเห็น Claude สร้างแอปได้ แล้วรีบพิมพ์ว่า “ช่วยทำแอป…
- Recent 72h post count: 18
- Snapshot time: 2026-04-29T23:55:49.358637+00:00

### Signals learned today
- Winning hook samples:
- ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 @GenLabs.th —- 👋 หลายคนเห็น Claude สร้างแอปได้ แล้วรีบพิมพ์ว่า “ช่วยทำแอป…
- ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 genlabs.in.th @GenLabs.th —- 👋 เหมาะกับใคร: คนเริ่มใช้ AI, เจ้าของร้าน, ค…
- ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 genlabs.in.th @GenLabs.th —- 👋 เหมาะกับใคร: คนเริ่มใช้ AI, เจ้าของร้าน, ค…
- Weak hook samples:
- None
- Protected CTA note: Sway-added CTA phrase is protected and must not be treated as a weak pattern.
- Protected CTA occurrences in low-view sample: 5
- Breakout candidates: 0
- Current issue count: 0

### Mistakes / weak spots to correct
- No data reliability issue detected; main weakness is insufficient breakout velocity so far.

### Rule / memory update
- Lesson: No post is near breakout yet; prioritize more shots on goal and remix the best practical-business hook.
- Decision rule: If no post is on pace for 100k, increase experiment volume and remix the best specific business-use hook instead of passively waiting.

### Next action
- Create 3 new experiments from the best current pattern; favor specific Thai SME/freelancer AI outcomes.

### Links
- Memory note: [[Aion OS/Aion Learning Lab/Zernio Growth/Zernio Growth Memory]]
- Master state: [[Aion OS/Projects/genlabs-ai-learning-state]]
- Self-improvement SOP: [[Aion OS/SOPs/genlabs-ai-learning-self-improvement-system]]

## Growth Check — 2026-04-29T08:18:40.284687+00:00
- KPI: best post at 1,012 views; gap 98,988 to 100,000.
- Best/closest/early post: product-photo 10-baht/no-prompt hook, post 69f17d4f985e734bf3d221fc.
- Signal: 14 posts in 72h; current winner has 5.24% engagement and 5 shares, but no new snapshot velocity. A 4.23h post in the same family has 681 views, 5.73% engagement, and strongest share rate among top recent posts (0.734%).
- Lesson: product-photo/10-baht/no-prompt remains the strongest topic family, but near-duplicate hooks appear in both winners and weak posts. The next push should keep the concrete product-photo benefit while changing first line, audience, and use-case.
- Action: create three remix tasks: online seller before/after, mistake/fix prompt-context, and LINE shop promo+reply workflow. Stop exact duplicate “เหมาะกับใคร” opener variants until one remix beats 700 views in 4h or 1,200 views in 24h.
- Issue: no saves and zero comments on the best post; add explicit save/comment CTA in remix scripts. Analytics freshness acceptable (~54 min).
## 2026-04-29 10:00 UTC — Growth Check
- KPI: best post is product-photo/10-baht/no-prompt at 1,013 views; gap 98,987 to 100k.
- Signal: no breakout candidate; best recent early post has 683 views at ~5.9h with 5.71% engagement and 0.73% share rate.
- Lesson: repeated product-photo opener appears in both winner and weak samples; preserve the concrete benefit but stop exact duplicate first lines.
- Action: next experiment should remix product-photo hook for one specific SME audience with explicit comment/save CTA.
- Rule: no more exact “AI สร้างภาพสินค้า แค่ 10 บาท / ไม่ต้อง prompt” openers until a remix beats 700 views in 4h or 1,200 views in 24h.

## 2026-04-29 12:10 UTC — Growth Check
- KPI: best/closest post remains the Claude/app + product-photo CTA post at 1,014 views; gap 98,986 to 100k.
- Signal: no breakout candidate and zero delta velocity since the previous snapshot, but engagement is still useful at 5.23% with 5 shares.
- Weak spot: saves/comments remain zero, so the current hook is getting some reach but not enough participation or saving behavior.
- Action: added active experiment “Claude app mistake → SME product-photo remix with save/comment CTA”. It keeps the proven concrete SME/product-photo benefit while changing the first line, audience/use-case, and CTA.
- Rule: if a >5% engagement best post has zero delta velocity plus zero saves/comments, treat it as a benchmark to remix with explicit save/comment prompts, not as a breakout to simply repost.

## 2026-04-29 12:31 UTC — Issue Check Fix
- Issue: `hermes-breakout-watch` was configured as `0 */6 * * *` even though the Zernio growth loop requires 30-minute breakout checks. This could delay amplification while a post is gaining early velocity.
- Fix: changed `hermes-breakout-watch` in `~/.hermes/cron/jobs.json` to `*/30 * * * *` and moved the next run to 2026-04-29T13:00:00+00:00.
- Issue: repeated `zernio_growth_snapshot.py` invocations in the same few minutes were overwriting `last_snapshot.json`, flattening velocity deltas and hiding breakout candidates.
- Fix: added a 15-minute minimum velocity-baseline update window; rapid re-runs still update KPI memory but do not reset the delta baseline.
- Prevention: issue-check should verify cron cadence and snapshot baseline behavior before trusting “no breakout” when several growth jobs run close together.



## 2026-04-29T16:08:10Z — Growth Check

- KPI: best post 1,059 views; gap 98,941 to 100,000.
- Breakout detected: post 69f1f53b985e734bf3d5442e at 550 views after 4.57h, +121 views since baseline, ~205.5 views/hour short-window velocity.
- Secondary candidate: post 69f1b217985e734bf3d352f9 at 870 views after 12.06h, 7 shares, 5.75% engagement, ~117.2 views/hour.
- Lesson: product-photo/no-prompt/10-baht remains the reach leader, but exact opener repetition is appearing across both winners and weak samples; next lift should come from SME-specific remixes with a new first line and explicit save/comment CTA.
- Action/task: create one draft-only remix for online sellers/LINE shops: “รูปสินค้าธรรมดา 1 รูป → ภาพขาย 3 แบบ + แคปชั่น + LINE reply” and use a pinned comment prompt asking viewers to comment their product type.
- Rule update: do not ship another exact product-photo/10-baht opener; preserve the benefit but change first line, audience/use-case, and CTA until a remix beats 700 views in 4h or 1,200 views in 24h.


## 2026-04-29 18:15 UTC — Growth Check

KPI: best post 1,117 views; gap 98,883 to 100,000.
Signal: top post is 2.05x account average views (1,117 vs 544), but latest snapshot velocity is 0 and saves/comments remain weak. A 14h post has 928 views with stronger share rate (0.862%), making product-photo/no-prompt still useful but too duplicated.
Action: stop exact duplicate first-line CTA/openers; next production cycle must create a distinct use-case remix: Thai online seller product photo → 3 marketplace images + captions + LINE reply. Add explicit save/comment prompt.
Task: Create one draft-only remix from post 69f17d4f985e734bf3d221fc with hook “รูปสินค้าธรรมดา 1 รูป → ภาพขาย 3 แบบ + แคปชั่น + LINE reply” and target >700 views in 4h, >0.7% share rate, at least 1 save/comment.
Lesson: The protected GenLabs CTA can stay, but the educational hook before it must vary by audience/use-case to avoid near-duplicate fatigue.

## 2026-04-29 18:31 UTC — Issue Check Fix
- Issue: the scheduled analytics import was fresh in Airtable after rerun, but Zernio reported `dataStaleness.staleAccountCount=1` and `syncTriggered=true`; analytics timestamps still lagged by ~61 minutes. This is not yet a data outage, but it can hide the true early velocity window if it persists past the next import cycle.
- Fix: manually reran `scripts/import_zernio_analytics_to_airtable.py --days 365`, verified snapshot compile/run, verified no duplicate Zernio IDs/platform IDs/analytics keys, verified no missing required Airtable fields, and refreshed the Obsidian daily log/memory note.
- Task: next import/issue check should confirm `dataStaleness.staleAccountCount` returns to 0 or analytics age stays under 180 minutes; if not, create a Zernio sync investigation task for the TikTok account.
- Prevention: issue-check should treat `syncTriggered=true` as a watch condition even when Airtable `Imported At` is fresh, because import freshness and TikTok analytics freshness are separate failure modes.

### 2026-04-29 22:03 Growth Check Action
- KPI: best post 1,173 views; gap 98,827 to 100,000; no breakout candidate.
- Signal: newer 981-view post at 17.98h has 5.61% engagement and 0.815% share rate, above account average share rate 0.621%.
- Action: created draft-only remix task `Share-rate remix from 981-view 18h post: product photo → caption + LINE reply` using product photo → caption + LINE reply variants with explicit save/comment CTA.
- Stop/avoid: no more exact duplicate CTA-first / generic “เหมาะกับใคร” educational openers as the first line; protected GenLabs CTA can remain, but the lesson hook must change.
- Lesson: At 22:03 UTC, the 981-view/18h post has the strongest actionable share signal (0.815% vs 0.621% average) while the 1,173-view leader is stalled; remix the shareable SME-use-case angle, not just the absolute leader.
- Rule update: When absolute-best velocity is zero but a newer post beats average share rate, prioritize a draft-only remix of the newer shareable angle with a concrete save/comment CTA; do not repeat generic “เหมาะกับใคร” audience-list intros as the first educational line.


## 2026-04-29T22:31:22+00:00 — Breakout Watch
- Breakout candidate: TikTok post 7634194104599022866 / Zernio 69f22cf2985e734bf3d79c56.
- Signal: 543 views at 7.65h; +27 views since prior snapshot; 58.65 views/hour vs recent average 633 views/post and stronger than current leader velocity.
- Pattern: product-photo/no-prompt utility is still the highest-reach family, but exact opener repetition is risky; amplify with specific SME use-case remix and explicit save/comment prompt.
- Draft-only next action: create/use-case remix around “รูปสินค้าธรรมดา 1 รูป → ภาพขาย 3 แบบ + แคปชั่น/LINE reply” and add comment prompt asking sellers to name their product.

## 2026-04-30

### KPI status
- Goal: one TikTok post reaches **100,000 views**.
- Best post: ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 @GenLabs.th —- 👋 หลายคนเห็น Claude สร้างแอปได้ แล้วรีบพิมพ์ว่า “ช่วยทำแอป…
- Current best views: 2122
- Gap to 100,000: 97878
- Closest post views: 2122
- Strongest velocity post: ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 genlabs.in.th @GenLabs.th —- 👋 เหมาะกับใคร: คนเริ่มใช้ AI, เจ้าของร้าน, ค…
- Recent 72h post count: 17
- Snapshot time: 2026-04-30T23:55:54.670066+00:00

### Signals learned today
- Winning hook samples:
- ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 @GenLabs.th —- 👋 หลายคนเห็น Claude สร้างแอปได้ แล้วรีบพิมพ์ว่า “ช่วยทำแอป…
- ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 genlabs.in.th @GenLabs.th —- 👋 เหมาะกับใคร: คนเริ่มใช้ AI, เจ้าของร้าน, ค…
- ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 genlabs.in.th @GenLabs.th —- 👋 เหมาะกับใคร: คนเริ่มใช้ AI, เจ้าของร้าน, ค…
- Weak hook samples:
- None
- Protected CTA note: Sway-added CTA phrase is protected and must not be treated as a weak pattern.
- Protected CTA occurrences in low-view sample: 5
- Breakout candidates: 2
- Current issue count: 0

### Mistakes / weak spots to correct
- No data reliability issue detected; main weakness is insufficient breakout velocity so far.

### Rule / memory update
- Lesson: Best-performing practical AI/business transformation hooks remain the current remix base.
- Decision rule: If no post is on pace for 100k, increase experiment volume and remix the best specific business-use hook instead of passively waiting.

### Next action
- Amplify the top breakout candidate with a remix, follow-up hook, and comment/repurpose plan.

### Links
- Memory note: [[Aion OS/Aion Learning Lab/Zernio Growth/Zernio Growth Memory]]
- Master state: [[Aion OS/Projects/genlabs-ai-learning-state]]
- Self-improvement SOP: [[Aion OS/SOPs/genlabs-ai-learning-self-improvement-system]]

## 2026-05-01

### KPI status
- Goal: one TikTok post reaches **100,000 views**.
- Best post: ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 @GenLabs.th —- 👋 หลายคนเห็น Claude สร้างแอปได้ แล้วรีบพิมพ์ว่า “ช่วยทำแอป…
- Current best views: 2307
- Gap to 100,000: 97693
- Closest post views: 2307
- Strongest velocity post: ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 @GenLabs.th —- 👋 หลายคนเห็น Claude สร้างแอปได้ แล้วรีบพิมพ์ว่า “ช่วยทำแอป…
- Recent 72h post count: 16
- Snapshot time: 2026-05-01T10:01:09.046904+00:00

### Signals learned today
- Winning hook samples:
- ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 @GenLabs.th —- 👋 หลายคนเห็น Claude สร้างแอปได้ แล้วรีบพิมพ์ว่า “ช่วยทำแอป…
- ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 genlabs.in.th @GenLabs.th —- 👋 เหมาะกับใคร: คนเริ่มใช้ AI, เจ้าของร้าน, ค…
- ✅AI สร้างภาพสินค้า แค่ 10 บาท ❌ไม่ต้อง prompt ก็ได้ภาพ 👉 genlabs.in.th @GenLabs.th —- 👋 เหมาะกับใคร: คนเริ่มใช้ AI, เจ้าของร้าน, ค…
- Weak hook samples:
- None
- Protected CTA note: Sway-added CTA phrase is protected and must not be treated as a weak pattern.
- Protected CTA occurrences in low-view sample: 5
- Breakout candidates: 1
- Current issue count: 0

### Mistakes / weak spots to correct
- No data reliability issue detected; main weakness is insufficient breakout velocity so far.

### Rule / memory update
- Lesson: Best-performing practical AI/business transformation hooks remain the current remix base.
- Decision rule: If no post is on pace for 100k, increase experiment volume and remix the best specific business-use hook instead of passively waiting.

### Next action
- Amplify the top breakout candidate with a remix, follow-up hook, and comment/repurpose plan.

### Links
- Memory note: [[Aion OS/Aion Learning Lab/Zernio Growth/Zernio Growth Memory]]
- Master state: [[Aion OS/Projects/genlabs-ai-learning-state]]
- Self-improvement SOP: [[Aion OS/SOPs/genlabs-ai-learning-self-improvement-system]]

### 3-Day Self-Improvement Review — 2026-05-01 10:00 UTC
- KPI status: best post is at 2,307 views, gap 97,693 to the 100,000-view milestone.
- Overall read: the system is learning, but current posts are still far from breakout; the strongest signal is a product-photo/no-prompt SME angle with one high-velocity variant at 1,921 views and 19 shares.
- What is working: concrete Thai SME/product-photo usefulness plus GenLabs no-prompt positioning is outperforming generic education and producing above-average share signals.
- What is not working: repeated near-identical first lines/audience-list intros are saturating without creating saves/comments, so volume needs more distinct use-case remixes rather than duplicate openers.
- Keep rule: protect the Sway-added GenLabs CTA from being misclassified as a weak pattern; judge the educational hook/body separately.
- Change rule: stop shipping exact duplicate product-photo/10-baht openers; require a new first line, use-case, and save/comment CTA until a remix beats the early benchmark.
- Test: three distinct SME visual-use-case remixes — marketplace before/after, LINE shop promo pack, and product-photo mistake/fix — each with explicit comment/save prompt and 4h/24h closure.
- Next 3-day focus: amplify the 1,921-view high-share/high-velocity post, close active experiments with 4h/24h results, and increase experiment volume only with distinct Thai-useful angles.
