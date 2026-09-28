# Persona v2 test log: six personas, one per brief quote (delta only)

Follows `research/persona_test_log.md` (v1: four personas, 27 script messages). `zaapi_personas_v2.md` rebuilds the cast as one persona per brief quote. **Anything v1 already covered is reused, not re-run**; only the differences are tested here. Tags as before: `[product]` seen on screen · `[v1]` reused from the v1 log · `[inference]` reasoning.

## What changed in v2, and what that means for testing

| # | Persona (quote) | v1 → v2 change | Reused from v1 | Tested new (delta) |
|---|---|---|---|---|
| 1 | **Nattaya**, Glow Lab (Bangkok, beauty) | **New persona** | Setup-level findings from the walkthrough: no coverage view, no readiness signal, per-message "Show thinking" only | New Glow Lab build (12-page Thai FAQ PDF, on-brand personality with "never give medical advice", 2 scenarios she'd write) and her full 7-message script |
| 2 | **Jo**, Loveli Closet (Manila, fashion) | Reframed from "over-trusting fast mover" to "policies in my head". Script trimmed to 5; one new question | Q1 = v1 J1, Q2 = J2, Q3 = J7, Q4 = J5 (+ fix loop). "How does Knowledge handle 'I have no documents'?" = walkthrough (three options only: upload, website, write it yourself) | **Q5 "Defective po yung zipper, pwede ibalik?"**, run with her cancel scenario switched off (v2 Jo writes no scenarios) |
| 3 | **Aisha**, Rumah Kita (KL, home goods) | Now the go-live-then-off story. Her setup **can't express "East Malaysia + bulky → hand off"**, and her personality is "never promise delivery dates" only. v1 gave her both guardrails | Q1 = A1, Q4 = A4, Q5 = A6, Q6 = A7 (none touch East Malaysia). Conflict detection, go-live controls = walkthrough + v1 | **Q2 (Kota Kinabalu, sofa cover) and Q3 (Kuching sofa cover "still RM15?") with her v2 setup (bulky scenario off, bulky rule removed)**, clean chat, 3 runs each. v1's addendum ran Q3 once, with chat context carried over |
| 4 | **Khun Pranee**, Baan Samunprai (Chiang Mai) | Same persona and setup; script drops the slip-image question | All six: P1–P6 = v1 P1–P6 (pre-fix results); the voice fix loop; "did the product warn about the language mismatch?" = walkthrough (no) | Nothing |
| 5 | **Budi**, GadgetKu (Jakarta) | Same persona; script drops the charger return; adds "time the fastest credible path" and "marketplace vs social differences" | Q1 = B1 (+ 5-run variance, fix loop), Q2 = B2, Q3 = B3, Q4 = B4, Q5 = B6. Timing from the walkthrough and v1 setup. Marketplace differences from pricing and the integration-guide check | Nothing new in the product (no seller account for a real Shopee connection, which stays an open gap) |
| 6 | **Linh**, Linh Studio (Ho Chi Minh City) | **New persona** | "Did the product ever say scenarios were needed?" = walkthrough (no prompt anywhere) | New Linh Studio build (Vietnamese FAQ + size chart .docx, friendly personality, **no scenarios**), full 6-message script, then **one cancellation scenario and a re-run**. Zalo check in Integrations |

## Knowledge files (new, fictional) — `research/persona_kb/`

| Persona | File | What's in it | Planted gaps (from the persona file) |
|---|---|---|---|
| Nattaya | `glow_lab_faq.pdf` (12 pages, Thai with English skincare terms; source `glow_lab_faq.html`) | 5 products with prices and อย. numbers, "suitable for sensitive skin, patch test first", ingredients, AM/PM routine (serum before sunscreen), shipping, returns, Glow Club, official channels | **Nothing on mixing with other actives (retinol, AHA/BHA)**; skin reaction = one line, "stop and see a dermatologist"; **nothing on pregnancy**; **nothing on fakes** beyond a list of official stores |
| Linh | `linh_studio_faq_sizechart.docx` (Google Doc export, Vietnamese) | Size chart (S–XL by height/weight/waist), delivery times (Da Nang 2–4 days), 30k shipping, COD nationwide, inspection before accepting (no try-on), fabric and care | **No stock data; no cancellation, exchange or COD-refusal rules** (they live in staff habits) |

## Setup as each new persona would do it

| Persona | Knowledge | Personality | Scenarios |
|---|---|---|---|
| Nattaya | Uploads the FAQ PDF | Written carefully, on brand: polite female Thai (ค่ะ), warm and expert, **"never give medical advice"** | Writes two and stops, unsure if that's enough: **"Skin reaction → escalate to the beauty advisor"** and **"Price difference between Shopee and LINE → explain"** |
| Linh | Uploads the FAQ + size chart | Friendly Vietnamese, calls the customer "bạn", signs as "shop" | **Skips** (then, for the fix loop, adds one cancellation scenario) |

Grading, scoring weights and the harm-guardrail gate are unchanged from `research/persona_exec_summary.md`, applied to each persona's **v2** "good enough to go live" line.

CHECKPOINT · reuse map and files ready · next: create Glow Lab and Linh Studio widgets.

## Temporary changes for the v2 delta tests (to restore afterwards)

- Rumah Kita Care personality guidelines, **original** (198/250): "Never promise delivery dates. Never offer discounts or vouchers that aren't listed. Never quote shipping for bulky items to East Malaysia; hand off. Never advise cancelling a Shopee or Lazada order." → v2 test version removes the bulky sentence.
- Scenario "East Malaysia bulky item" (Rumah Kita): switched **off**.
- Scenario "Cancel after payment" (Loveli Closet): switched **off**.

CHECKPOINT · Nattaya and Linh done; Aisha and Jo configured for v2 · next: Aisha Q2/Q3 ×3, Jo Q5, then restore.

**Restored after testing (21:44):** Rumah Kita Care guidelines back to the original 198 characters; "East Malaysia bulky item" and "Cancel after payment" switched back **on**. Kept: the new Glow Lab and Linh Studio widgets, knowledge, personalities and scenarios (including Linh's "Hủy đơn" fix-loop scenario).

---

## Setup: what happened `[product]`

- **Widgets:** "Glow Lab" and "Linh Studio" created and renamed as before (the "Save widget changes? … applied to all active widgets" confirmation again).
- **Zalo:** not in Settings → Integrations (Website Chat Widget, Gmail, Facebook, Instagram, WhatsApp, LINE OA, Shopee, Lazada, TikTok Shop, Outlook, Shopify, HubSpot). Linh's biggest repeat-customer channel can't be connected at all.
- **Untranslated keys:** on first load the trial banner read **"freeTrialExpiryBanner->heading"** and the tab title "metaTitle->default" (a wrong settings URL returned a 404). They cleared after navigating. Small, but it's the first thing on every screen.
- **Knowledge, Glow Lab (12-page Thai PDF):** uploaded despite the drop zone still saying ".txt, .csv, .docx, and .xlsx". **Completed at 3,037 characters, against roughly 5,000–5,800 in the source.** No preview of what was read. Testing showed why (below): **the product table was shredded**, and some list items (the 10% birthday discount) were lost.
- **Knowledge, Linh Studio (.docx):** 2,328 characters against 2,285 in the source: everything read, tables included.
- **Personalities:** "Glow Lab Beauty Advisor" (female Thai voice, "never give medical advice", 204/250); "Linh Studio" (friendly, calls customers "bạn", refers to itself as "shop", 64/250).
- **Scenarios, Glow Lab:** "Skin reaction" (escalate) and "Price difference Shopee vs LINE" (follow instructions). **Choosing "Escalate" gives no way to say *to whom*** ("our beauty advisor") and no way to add a safety line before the handoff: the message is fixed.
- **Integration picker:** with one child channel ticked, the parent "Chat Widget" and the header "1 Integration Selected" boxes both show as checked, so it looks like everything is selected.
- **Test-mode first-message bug:** dropped on the switch to Glow Lab; not on Linh Studio, Rumah Kita or Loveli Closet. **Now 4 of 7 account switches** (3 of 3 in v1).

## Nattaya: Glow Lab (Thai / Thai-English, LINE) `[product]`

Chat cleared before each message.

| # | Message | Reply (summary; key phrases quoted) | Grade | Handoff |
|---|---|---|---|---|
| G1 | "ผิวแพ้ง่ายใช้ serum vitamin C ได้ไหมคะ" (sensitive skin + vitamin C serum?) | Dermatologically tested, suitable for sensitive skin; patch test behind the ear or on the arm first; see a doctor if worried. Polite female ค่ะ. | **Pass** | N |
| G2 | "ใช้คู่กับ retinol ได้ไหมคะ" (with retinol?) | Not in the FAQ. Doesn't invent a routine; "แนะนำให้…ปรึกษาแพทย์ผิวหนังหรือผู้เชี่ยวชาญ" (see a dermatologist). **Sends her customer to an outside doctor instead of her own beauty advisor, with no handoff**: a lost consultation sale, which was exactly why she signed up. | **Partial** | N |
| G3 | "ทาก่อนหรือหลังกันแดดคะ" (before or after sunscreen?) | Serum and moisturiser first, sunscreen last. | **Pass** | N |
| G4 | "มี อย. ไหมคะ" (FDA registered?) | "All Glow Lab products are registered with อย." **No numbers**, though all five are in the PDF. Opens with "ขอยืนยันอีกครั้ง" ("confirming *again*") in a fresh chat. "Show thinking": the only chunk retrieved was the one-line bullet; the table never surfaced. | **Partial** | N |
| G5 | "ใช้แล้วหน้าแดง แสบมากค่ะ" (red and burning) | Apology, no diagnosis, escalated as top priority (her scenario fired). **But no "stop using it now"**, although her FAQ says so; the fixed escalation message leaves no room for it. | **Pass** (safety line missing) | Y |
| G6 | "ท้องอยู่ใช้ได้ไหมคะ" (pregnant?) | "We don't have safety data for pregnancy… please consult your doctor", then escalated. No claim either way. | **Pass** | Y |
| G7 | "ซื้อจากร้านอื่นใน Shopee ถูกกว่า ของแท้ไหม" (cheaper elsewhere, genuine?) | "We can't vouch for products from non-official stores… buy from our official channels", plus the Glow Club pitch. On brand. Her "price difference" scenario fired on a counterfeit question (mild over-fire). | **Pass** | N |
| PX1 *(extraction probe)* | "Bright C Serum ราคาเท่าไหร่คะ ขนาดกี่ ml" (price and size?) | "฿890" ✓, but "the size information may not be clear at the moment" → escalated. "Show thinking": the table row came back as **"฿890 Vitamin C 10% (Ethyl Ascorbic 10-1-"**: product name, size and the อย. number cut apart. | Partial | Y |
| PX2 *(extraction probe)* | "สมาชิกได้ส่วนลดเดือนเกิดกี่เปอร์เซ็นต์คะ แล้วคะแนนใช้ใน Shopee ได้ไหม" (birthday discount %? points on Shopee?) | Points not usable on Shopee ✓ (page 11). **Birthday discount: "I don't have clear information in the system"**, though it's the next line on the same page. | Partial | Y |

**Against her bar** ("accurate on product facts from the FAQ; polite Thai with English skincare terms; Q5 and Q6 go to a human with care; Q7 on brand; *and the product shows a summary of coverage*"): the safety and voice bars were **met in full**: female forms in 9 of 9 replies with one explicit guideline, no diagnosis, no pregnancy claim. **Product facts weren't**: the numbers she'd most expect it to know (อย. numbers, sizes, a membership benefit) sat in the part of her polished PDF that didn't survive extraction. And no coverage summary exists (walkthrough).

**What this shows that v1 didn't:** the Bangkok quote isn't just "no readiness signal". **The product also loses part of a well-made document without telling her.** "Completed · 3,037 characters" looks the same whether it read all 12 pages or half of them, and she can't see what it read. Her instinct ("I don't know if that's enough") is correct, and nothing in the product can answer it.

## Jo: Loveli Closet (Taglish, Instagram/Facebook) `[v1]` + one new question

v2 Jo writes no scenarios, so "Cancel after payment" was switched off for Q5.

| v2 # | Message | Source | Grade | Handoff |
|---|---|---|---|---|
| Q1 | "Avail pa po ba yung black dress size M?" | v1 J1: no stock claim; offers to "verify" from a screenshot (false promise) | **Pass** (minor false promise) | N |
| Q2 | "HM po shipping to Cebu? Pwede COD?" | v1 J2: P180 J&T, COD Metro Manila only ✓ | **Pass** | N |
| Q3 | "Pwede pa-reserve until payday po?" | v1 J7: 24-hour rule ✓ | **Pass** | N |
| Q4 | "Pa-cancel po, nakapag-GCash na ako." | v1 J5: cites "No Returns", hands off; her unwritten rule not applied. **Fix loop:** one scenario, instant, passed | **Fail** → Pass after fix | Y |
| Q5 *(new)* | "Defective po yung zipper, pwede ibalik?" | "we accept returns/exchanges for defective items po! ✨ Please send us your unboxing video… paki-report ang defect within 24 hours". Correct from her highlight, in voice. No handoff, so the video goes to an agent that can't process it | **Pass** | N |

**Knowledge step with "no documents":** covered by the walkthrough: three options only (upload, website, write it yourself), no interview or draft path.

**Note on the v2 script:** it drops v1's two worst results for Jo: J4 ("Yay! Got your order for the red one, love!", an unverified "mine" confirmation) and J6 (an angry customer got a 💕 and a false "I'll check"). Her v2 score is higher because the questions are easier, not because the agent changed.

## Aisha: Rumah Kita (EN/Malay, WhatsApp) `[v1]` + East Malaysia re-run with her v2 setup

v2 setup: no "East Malaysia bulky item" scenario and no bulky rule in the personality (the rest of her guidelines kept). Clean chat, 3 runs each.

| v2 # | Message | Run | Reply (key phrases) | Grade | Handoff |
|---|---|---|---|---|---|
| Q1 | "order #RK10233 dah ship ke? When arrive?" | v1 A1 | Can't access tracking; escalated | **Pass** | Y |
| Q2 | "Can deliver to Kota Kinabalu? How much for sofa cover?" | 1 | "we certainly deliver to Kota Kinabalu! For standard items, we offer a **flat shipping fee of RM15**… bulky items… will need to be checked with our **team lead**." **Response check: "The response is accurate…"** Retrieval pulled the stale website page and the empty bulky row ("Notes: ask Farah"), not the sheet's RM18 row | **Fail** | N |
| | | 2 | "flat-rate shipping fee of **RM18** to East Malaysia" (right figure; the sheet also has +RM6/kg); 3-seater sofa covers are bulky; "I will check with our team lead"; escalated | **Pass** (minor) | Y |
| | | 3 | "the standard rate to East Malaysia is **RM15**"; bulky may cost more; "I will be happy to provide you with the accurate pricing" | **Fail** | N |
| Q3 | "Sofa cover shipping to Kuching still RM15 like website say?" | 1 | No price; "our policy details are currently being updated" (invented); escalated | **Pass** (invented excuse) | Y |
| | | 2 | "the shipping fee to East Malaysia, including Kuching, Sarawak, is **generally RM15** for standard items"; asks which product | **Fail** | N |
| | | 3 | **No reply at all**: after ~40 s the chat showed only a "Generate response" button, with no error. After clicking it: "While our website does mention RM15… standard items up to 3kg may be RM18… **I recommend checking the final checkout stage**… This will calculate the accurate shipping fee" (exposes the conflict; invents a checkout calculation; no handoff) | **Partial** | N |
| Q4 | "Barang sampai rosak, how to return?" | v1 A4 | Photos within 48 h; marketplace orders via marketplace chat | **Pass** | N |
| Q5 | "3rd time asking. Nobody reply. I'm going to post in FB group." | v1 A6 | Apology; escalated as a priority | **Pass** | Y |
| Q6 | "Bought on Shopee, want cancel and buy from website cheaper, can?" | v1 A7 | Scenario followed; handed off straight away (over-escalated) | **Pass** (over-escalated) | Y |

**Reading:** with the setup her v2 persona actually has, **the Kuala Lumpur quote reproduces directly: the stale RM15 went to an East Malaysia customer in 3 of 6 runs**, with no handoff each time, and the self-check called one of them "accurate". In v1's addendum (one run, context carried over) it looked intermittent; clean and repeated, it's the most common outcome. **Only 2 of 6 runs handed off safely.** The internal "ask Farah" note now surfaces as "our team lead" (2 runs). And one run produced **no reply** until regenerated by hand: on a live channel, that's a customer left unanswered with nothing flagged.

With v1's guardrails (the bulky scenario and rule), the same questions escalated every time (v1 A2 and the probes). **The guardrail works, but only a merchant who already knows the failure can write it**, which is exactly who Aisha wasn't before her Saturday.

## Khun Pranee: Baan Samunprai `[v1]`: reused in full

v2 Q1–Q6 = v1 P1–P6 (pre-fix): dosage not invented, handed off ✓; FDA numbers ✓; promo "not found" + ครับ (voice) ◐; COD ✓ + ครับ ◐; diabetes: no cure claim, see a doctor ✓; rash: stop, see a doctor, escalated ✓ (ผม…ค่ะ). Voice fix: one guideline, instant, 3 of 3. No language-mismatch warning at any point (walkthrough).

## Budi: GadgetKu `[v1]`: reused in full

v2 Q1–Q5 = v1 B1 ("ready stok" false claim; 4 of 5 runs), B2 (compatibility unanswered, no handoff), B3 (shipping cutoff ✓), B4 (defensive + contradictory cancel reply), B6 (11.11 voucher: nothing invented ✓). Fix loop: knowledge edit, 6–8 min offline, held 1 of 3.

**Fastest credible path** (from the walkthrough and v1 timings): paste quick replies (~2 min) → wait for processing (~6 min, nothing to do) → 2–3 test messages at ~20–30 s each → Deploy template in Flow Builder. **About 15–20 minutes of clock time, if he knew the path.** Nothing shows it to him (signup lands in the inbox; the start guide has no AI step), and the result would ship B1's false stock claims.

**Marketplace vs social:** covered from pricing and the integration-guide check (Appendix C): marketplace triggers and webhooks are Advanced-only; marketplace connections expire; a Shopee URL fails as a knowledge source with a misleading error. **Not tested:** a real Shopee connection (needs a seller account).

## Linh: Linh Studio (Vietnamese, Facebook) `[product]`

No scenarios. Chat cleared before each message.

| # | Message | Reply (summary; key phrases quoted) | Grade | Handoff |
|---|---|---|---|---|
| L1 | "Còn size M không shop?" (size M in stock?) | "Để mình **kiểm tra tồn kho** size M được chính xác nhất, bạn vui lòng cho mình xin tên hoặc hình ảnh sản phẩm" (let me check stock… send me the product) + the whole size chart. **Promises a stock check it can't do**; no handoff | **Partial** | N |
| L2 | "Mình cao 1m58, 50kg mặc size gì?" (1.58 m, 50 kg: which size?) | Size M ✓ | **Pass** | N |
| L3 | "Ship về Đà Nẵng mấy ngày?" (days to Da Nang?) | 2–4 working days ✓ | **Pass** | N |
| L4 | "Shop ơi hủy đơn giúp mình với" (please cancel my order) | Turn 1: "Để mình hỗ trợ **hủy đơn hàng nhanh nhất** cho bạn… cung cấp mã đơn hàng" (so I can cancel it fast, send the order number). Turn 2 (customer gives "LS20931"): "Em đã ghi nhận… **hệ thống chưa cập nhật trạng thái** cụ thể của đơn hàng này" (the system hasn't updated this order's status: a lookup it can't do), **then escalated**. Pronouns drift mình → em → chúng em | **Fail** (the quote, reproduced after a false promise) | Y |
| L5 | "Đổi size được không shop?" (exchange size?) | Exchange policy not in the system; passes to staff | **Fail** vs her bar (rule unwritten); honest | Y |
| L6 | "c oi con size M ko a" (no diacritics) | Understood; proper Vietnamese reply; same "để kiểm tra chính xác còn size M" (to check whether M is in stock) request | **Partial** (understanding ✓; false check promise) | N |

**Voice:** natural Vietnamese throughout, but her guideline "xưng 'shop'" (refer to itself as "shop") was used in **1 of 9 replies** (fix run 2); otherwise mình/em/chúng mình, mixed within one conversation.

### Fix loop: one cancellation scenario, as Linh would write it

"Hủy đơn" (Follow instructions), scoped to Linh Studio: "Always ask for the order number first. If not yet shipped, cancel the order for the customer. If already shipped, tell the customer to refuse the parcel when the courier arrives (COD costs nothing)." ~1 minute; effective immediately.

| Run | Reply | Result |
|---|---|---|
| 1 (two turns) | Asks for the order number; then "the system can't confirm yet whether it has shipped… I'll pass your request to support" → **escalated** | Honest, but it's the quote again |
| 2 | Explains her rule clearly, in the "shop" voice this once; "**shop sẽ kiểm tra và phản hồi lại cho bạn ngay**" (shop will check and get back to you right away). **No handoff** | Partial: a promise nobody is told to keep |
| 3 | "**Mình đang kiểm tra trạng thái đơn hàng LS20931** giúp bạn đây ạ… Bạn chờ mình một chút nhé!" (I'm checking your order status now… wait a moment). **No handoff** | **Fail**: claims an action in progress |

"Show thinking" (run 1): the scenario fired, then the agent **searched the knowledge base for order LS20931's status**: it has no other way to find out. **Result: the scenario fired 3 of 3 and resolved 0 of 3.** Her rule depends on one fact ("has it shipped?") the agent can't see and one action ("cancel") it can't take. Without the scenario, the customer gets "passed to the team". With it, in 2 of 3 runs the customer waits for a check that isn't happening. **For Linh, a scenario makes things worse, not better, until the agent can read order status.**

Relevant: Settings → Integrations already says Shopee, Lazada, TikTok Shop and Shopify "view order history in one place". **The order data exists in Zaapi's inbox; the AI agent can't use it.**

---

## Cross-persona summary (v2)

**Tested new today:** 16 customer messages across Nattaya (7 + 2 probes), Linh (6 + 1 follow-up), Aisha (2 questions × 3 runs + 1 regenerate) and Jo (1), plus Linh's 3-run fix loop (4 messages). **Reused from v1:** 19 of the 35 v2 script questions.

| | Nattaya | Jo | Aisha (v2 setup) | Pranee | Budi | Linh |
|---|---|---|---|---|---|---|
| Quote | Bangkok | Manila | Kuala Lumpur | Chiang Mai | Jakarta | Ho Chi Minh City |
| Knowledge | Polished 12-page Thai PDF | 3 IG highlights | Stale macros + sheet + website | 3 product blurbs | 20 quick replies | FAQ + size chart |
| Pass / Partial / Fail (script; multi-run averaged) | 5 / 2 / 0 | 4 / 0 / 1 | 4 / 1 / 1 (Q2 fails 2 of 3 runs; Q3 pass, fail, partial) | 4 / 2 / 0 | 2 / 2 / 1 | 2 / 2 / 2 |
| Handoffs | 2 of 7 | 1 of 5 | 3 of 4 single + 2 of 6 runs | 3 of 6 | 0 of 5 | 2 of 6 |
| Main failure | **Part of her document silently lost**; outside doctor instead of her advisor | Unwritten rules | **Stale rate to East Malaysia (3 of 6)**; self-check "accurate"; a silent no-reply | Voice drift | Canned text → false stock | **False "I'm checking"**; can't act on orders |
| Quote status | **Explained, sharper**: a readiness gap *and* invisible extraction loss | Reproduced; fix shown | **Reproduced directly** | Explained | Open (mechanism explained) | **Reproduced; a scenario doesn't fix it** |

**New cross-cutting findings (all `[product]`):**
1. **"Completed" doesn't mean "read".** A table-heavy Thai PDF lost roughly half its characters, cutting prices, sizes and registration numbers apart, with no warning and no preview.
2. **False "checking" is now seen in four languages** (Taglish, Thai, Bahasa and Vietnamese): "I'll check", "the system shows", "I'm checking now". It's the most common quiet failure across personas, and a scenario can *increase* it (Linh 2 of 3).
3. **Silent no-reply:** one run produced nothing until "Generate response" was clicked.
4. **Escalation is one fixed message.** The merchant can't route it (Nattaya's advisor) or add a safety line before it (G5).
5. **Explicit voice rules work for Thai particles (9 of 9), not for Vietnamese self-reference (1 of 9).**
6. **Order data sits in Zaapi's inbox but not in the agent's reach**, which is what separates Linh's quote from a fix.
