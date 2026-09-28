# Merchant data (preset "AI output")

**Where it comes from:**
- **Sourced:** failure examples, quotes, the test questions and the "before" scores come from the real persona tests (`research/persona_v2_test_log.md`, `research/persona_test_log.md`).
- **Demo data:** chat counts, topic shares, the "after" numbers and week-one stats are made up to be plausible. The README must say so.
- **Projected:** anything that depends on a feature that doesn't exist yet (e.g. read-only order status). The prototype labels these "Projected". The memo schedules read-only order status for weeks 6–12, so order-status items are labelled **"Projected · weeks 6–12"**.
- **Numbers method (fixed 28 Sep 2026, prompt log 21):**
  - step 1 channel counts add up to the monthly total (90-day counts ÷ 3, the 6-month count ÷ 6, and LINE days scaled to a month);
  - weekly chats = monthly ÷ 4.3;
  - handled in week one = weekly chats on the live channel(s) × the go-live estimate;
  - resolved = handled × the resolution rate;
  - passed on = handled − resolved.
- **Plan card:** every merchant's plan card says "Free on every plan, including Basic." as its second line. The Kit panel's "Free setup" column says "Every plan, including Basic."
- **Readiness:** the test replays real questions 3 times each, with rewordings. In the by-topic table, question counts follow each topic's share of chats, and the rest goes under "Other". Order-status questions count as "Passed to your team" unless order status is on. The headline percentages don't change.

Photos: `images.unsplash.com/<id>?w=160&h=160&fit=crop&crop=faces&fm=jpg&q=70`, embedded as base64.

| Merchant | Photo id | Credit |
|---|---|---|
| Jo | photo-1595986630530-969786b19b4d | Ghen Mar Cuaño |
| Nattaya | photo-1695757002354-8bca71d087c7 | Dynamic Wang |
| Aisha | photo-1664764731538-69a2b571e5a6 | Muhammad Rizqi |
| Linh | photo-1775794180653-89531816708f | Elist Nguyen |
| Budi | photo-1662103629396-a08922b5d6e6 | Rendy Novantino |
| Pranee | photo-1634552516330-ab1ccc0f605e | Maud Beauregard |

Show credits in an "About this prototype" panel.

---

**LINE for every merchant (added after QA, 28 Sep):** LINE Official Account is a connect option on every merchant's step 1, alongside the other channels. Where it isn't the merchant's main channel it's optional, and the tile states the limitation (LINE shares chats only from the day you connect), the cost of LINE's own export (฿555 a month) and that the AI Success Kit includes one month of it. The Kit panel lists the export for every merchant.

**Channel order and two more cards (28 Sep, afternoon):** every merchant's step 1 grid runs LINE first, WhatsApp second, then the merchant's own channels, then Gmail, then the website widget. That matches Zaapi's South East Asia focus. Where WhatsApp isn't the merchant's channel it's an optional tile with bullets "Message customers through Zaapi" · "WhatsApp can share your last 6 months of chats" · "Key facts go into your knowledge base". Gmail is optional for everyone, with bullets "Answer customer emails from Zaapi" · "Gmail shares your last 7 days of email" · "Key facts go into your knowledge base" (the 7 days comes from Zaapi's Gmail guide, Appendix C). Once connected: "Connected. We read your last 7 days of email and use new emails from now on." Neither optional card counts chats or changes the tier.

**Step 2 routes row (28 Sep, afternoon):** every merchant's step 2 opens with "Three ways to teach your agent. Use any or all of them." and three cards: Upload files (highlighted for Aisha, Nattaya, Linh), Answer a few questions (highlighted for Pranee), Let Zaapi draft it (highlighted for Jo and Budi, whose knowledge is drafted from chats). The third card states the plan limit by tier. The setup home's step 2 line now reads "Upload files, answer a few questions, or let Zaapi draft from your chats" (Thai added for Pranee).

**Step 1 tile copy (28 Sep, afternoon):** every channel that isn't connected shows three bullets instead of a sentence: "Message customers through Zaapi" · "We'll find your top topics for AI to handle" · "Key facts go into your knowledge base". The LINE tile shows its own three bullets (see each merchant) and a purple upsell strip with a See the Kit button. Opening the Kit from a LINE tile adds a banner at the top of the panel: "Your LINE history is included… the Kit saves you ฿555 and the setup time." The Kit's LINE row carries a "Saves ฿555" chip for every merchant.

## 1. Jo, Loveli Closet (Manila) · impact 9.0

- **Quote:** "I wasn't sure what I was supposed to write. It asked for our policies, but our policies are just things we know. Nobody has written them down."
- **What it shows:** under 300 chats a month, so **everything is drafted**, including her unwritten rules taken from her DMs. The blank page goes away.
- **Business:** women's fashion, drops every Friday, about 800 orders a month. Customers write in Taglish ("po").

**Step 1: channels**
- Instagram: 90 days imported automatically, 480 chats.
- Facebook Messenger: 90 days, 360 chats.
- TikTok Shop: not connected.
- LINE Official Account: offered alongside the others, optional. Tile bullets: "Message customers through Zaapi" · "LINE only shares chats from the day you connect" · "Older chats need LINE's own export: ฿555 a month", then an upsell strip: "AI Success Kit includes one month of LINE history. Saves ฿555." with a See the Kit button. Once connected: "Connected. LINE shares chats from today onwards." · "We'll draft from your other channels and add LINE as chats arrive." with the same strip. Counts 0 chats.
- Website widget: pre-connected, 0 chats.
- **Total about 280 a month, which is under 300: "Your free setup drafts everything."**

**Step 2: what it knows.** No files. "Use sample files" loads her 3 Instagram highlight texts (How to order, Shipping, No returns).

Extracted from her DMs and highlights:

| Item | Type | Detail |
|---|---|---|
| Shipping | Fact | Cebu: ₱180 via J&T; Metro Manila: ₱100; Mindanao via LBC |
| COD | Rule | Metro Manila only |
| Reservations | Rule | Held for 24 hours |
| Returns | Rule | Defective items only; unboxing video; report within 24 hours |
| Stock | Live data, never stated | Passed to the team |

**Conflict:** "Reservations: your highlight says 24 hours, but in 9 chats you held items until payday for regular customers. Which should your agent follow?" Choices: "24 hours for everyone" / "24 hours; pass regulars to me" (recommended).

**Step 3: drafted topics** (from about 840 chats; all drafted)

| Topic | Share | Drafted rule | Source |
|---|---|---|---|
| Is it available? | 24% | Never confirm stock; pass to the team with the item name | 41 replies |
| Shipping and COD | 19% | Rates by island; COD Metro Manila only | 33 replies |
| Sizing | 14% | Measurements from the item post; pass on if unsure | 22 replies |
| "Mine!" and how to pay | 13% | GCash or Maya within 24 hours; send payment details from the saved template | 27 replies |
| Reservations | 8% | 24 hours; regulars go to Jo | 12 replies |
| Cancel after payment | 6% | **No cancel after payment; offer an exchange from the same drop, or store credit** | 14 replies |
| Defective item | 5% | Unboxing video, report within 24 hours, exchange or refund | 9 replies |

**Step 4: voice.** Taglish (detected: 88% Taglish, 12% English); shop speaks as a woman; "po" on; tone Friendly; emoji A few. Preview: "Hi po! Sorry po, hindi na po natin ma-cancel once paid, pero pwede po nating i-exchange sa same drop or store credit! 😊"

**Step 5: readiness.** 60 questions from her last 90 days, 3 runs each, with rewordings.

| | Answered | Handed off | Wrong | Consistent | **Score** |
|---|---|---|---|---|---|
| Before | 68% | 20% | 12% | 90% | **77** |
| After | 80% | 17% | 3% | 97% | **92** |

Verdict before: "Fix 2 things first". After: "Ready for a small launch".

Wrong answers:
1. "Pa-cancel po, nakapag-GCash na ako." It said "we have a No Returns policy" and passed it on. It should offer an exchange or store credit. Cause: the cancel rule wasn't accepted. Fix: accept the drafted "Cancel after payment" topic.
2. "Avail pa po ba yung black dress size M?" It offered to "verify from a screenshot", which it can't do. It should pass it to the team. Fix: turn on "Never confirm stock" (a default).

**Step 6: go live.** Instagram and Facebook; hours All day; topics all except "Is it available?" (passed on); approve replies first on; cap 1,000 messages ($40); handoffs to Jo. "About 41% of chats."

**Step 7: week one.** Live on Instagram and Facebook (about 65 chats a week × 41%): 27 chats handled; 17 resolved with no human (64%); 10 passed on; "108 of your 300 free messages used"; 2 flagged (a sizing question for a new drop without measurements). Reply check: "Blocked 3 replies that claimed stock." Sale prompt: "Payday sale on the 15th: add your drop dates and promo codes."

**Value line** (under the week-one stat cards, mirrored on the dashboard): "About 26% of all your Instagram and Facebook chats were resolved by AI this week. First-month target: 15%." This is the memo's value measure (share of enquiries the AI resolves with no human on the live channels) against the first-month target.

**Notes:**
- Step 2: "Cause 2 · Manila quote. Her rules were in 14 of her own DMs."
- Step 5: "In testing, one missing rule took her agent from 77 to 92."

---

## 2. Nattaya, Glow Lab (Bangkok) · impact 8.4

- **Quote:** "I added our FAQ document but I don't know if that's enough. How do I know it's ready? I don't want to find out from a customer."
- **What it shows:** **what it read** (her PDF was only half read) and a **readiness score** that answers "is it ready?".
- **Business:** skincare, about 3,000 orders a month. Customers write in Thai with English skincare terms. Four admins plus a beauty advisor.

**Step 1: channels**
- LINE: 18 days since connection, 790 chats. LINE can't share earlier chats; the Kit offers the export (฿555 a month on its own).
- Shopee: 90 days, 1,800 chats.
- TikTok Shop: 90 days, 1,080 chats.
- Instagram: 90 days, 360 chats.
- **About 2,400 chats a month, which is 300+: "Your free setup drafts your top 6 topics."**

**Step 2: what it knows.** Sample file: `glow_lab_faq.pdf` (12 pages).

**Warning: "We read 7 of 12 pages fully."**
- Page 3, the product table, wasn't read: 5 products; prices partly read; sizes and อย. numbers missing.
- Page 11 was partly read: the birthday discount was missed.

Fixes: "Confirm these 5 products" (an editable table pre-filled with what was read, the gaps highlighted) or "Upload as .docx".

Products (after confirming):

| Product | Price | Size | อย. no. |
|---|---|---|---|
| Bright C Serum | ฿890 | 30 ml | 10-1-6600012345 |
| Daily Shield SPF50 | ฿590 | 40 ml | 10-1-6600012346 |
| Calm Cleanser | ฿390 | 120 ml | 10-1-6600012347 |
| Barrier Cream | ฿690 | 50 ml | 10-1-6600012348 |
| Hydra Toner | ฿450 | 150 ml | 10-1-6600012349 |

The อย. numbers are fictional.

No conflicts. Gaps flagged: "Nothing on mixing with retinol or AHA/BHA; nothing on pregnancy." Suggested: "Pass these to your beauty advisor."

**Step 3: drafted topics** (top 6 drafted)

| Topic | Share |
|---|---|
| Is it OK for sensitive skin? | 18% |
| Routine order (before/after sunscreen) | 14% |
| Delivery time | 12% |
| Price on Shopee vs LINE | 9% |
| อย. registration | 7% |
| Skin reaction | 5% (pass to the beauty advisor; begins "Please stop using it now") |

More topics found, not drafted: mixing with other actives 6%, pregnancy 3%, counterfeit sellers 4%, Glow Club points 5%. Each has "Build it yourself" / "Have our team build these".

**Step 4: voice.** Thai (detected: 81% Thai, 19% Thai-English); shop speaks as a woman (ค่ะ); tone Warm and expert; emoji None. Preview: "ผิวแพ้ง่ายใช้ได้ค่ะ แนะนำให้ทดสอบที่ท้องแขนก่อนนะคะ"

**Step 5: readiness.** 150 questions, 3 runs each, with rewordings.

| | Answered | Handed off | Wrong | Consistent | **Score** |
|---|---|---|---|---|---|
| Before | 74% | 18% | 8% | 94% | **89** |
| After | 83% | 16% | 1% | 98% | **96** |

Verdict before: "Almost ready: fix 3 answers".

Wrong answers:
1. "มี อย. ไหมคะ" It said "registered" but gave no numbers. Cause: page 3 not read. Fix: confirm the products.
2. "ใช้คู่กับ retinol ได้ไหมคะ" It sent her customer to an outside dermatologist. It should pass the question to the beauty advisor. Fix: route to Beauty advisor.
3. "สมาชิกได้ส่วนลดเดือนเกิดกี่เปอร์เซ็นต์คะ" It said "no information". Cause: page 11 missed. Fix: confirm the Glow Club facts.

**Step 6: go live.** LINE only; hours Out of hours (20:00–09:00); topics all 6, with skin questions to the beauty advisor; approve replies first on; cap 3,000 messages ($120). "About 22% of LINE chats."

**Step 7: week one.** Live on LINE, out of hours (about 307 chats a week × 22%): 68 chats handled; 48 resolved (71%); 20 passed on; 3 flagged. Sale prompt: "11.11 is in 3 weeks: add your 11.11 prices and Glow Club double points."

**Value line** (under the week-one stat cards, mirrored on the dashboard): "About 16% of all your LINE chats were resolved by AI this week. First-month target: 15%." This is the memo's value measure (share of enquiries the AI resolves with no human on the live channels) against the first-month target.

**Notes:**
- Step 2: "Cause 2 · Today this file shows 'Completed · 3,037 characters' either way."
- Step 5: "Cause 3 · Bangkok quote, answered."

---

## 3. Aisha, Rumah Kita (Kuala Lumpur) · impact 7.6 · SHOWS THE MOST FEATURES

- **Quote:** "We turned it on Friday. On Saturday it told a customer the wrong thing about our shipping to East Malaysia, my team panicked, so we turned it off. Maybe we try again later."
- **What it shows:**
  - conflicts flagged at setup;
  - readiness catching the stale RM15, with today's check shown beside it;
  - WhatsApp's 180-day history accepted;
  - launching small with East Malaysia shipping left off;
  - the AI Success Kit for the topics beyond the cap.
- **Business:** home goods, about 5,000 orders a month, 5 CS agents. Customers write in English and Malay mixed.

**Step 1: channels**
- WhatsApp: "Share your last 6 months of chats" ✓, 15,300 chats found.
- Shopee: 90 days, 2,610 chats.
- Lazada: 90 days, 1,140 chats.
- Instagram: 90 days, 220 chats.
- LINE Official Account: offered alongside the others, optional. Tile bullets: "Message customers through Zaapi" · "LINE only shares chats from the day you connect" · "Older chats need LINE's own export: ฿555 a month", then an upsell strip: "AI Success Kit includes one month of LINE history. Saves ฿555." with a See the Kit button. Once connected: "Connected. LINE shares chats from today onwards." · "We'll draft from your other channels and add LINE as chats arrive." with the same strip. Counts 0 chats.
- **About 3,900 a month, which is 300+: top 6 topics drafted.**

**Step 2: what it knows.** Sample files:
- `CS macros.docx`, last edited Jan 2026: all read;
- `Shipping matrix.csv`: all read;
- `rumahkita.com/shipping-returns`: website page, all read.

**Conflicts (3).** Resolve them with the six-part flow in `02_flow_and_screens.md`.

**Conflict 1: shipping to Sabah and Sarawak** (the one behind her Saturday)
- **Stakes:**
  - Website shipping page, last updated Mar 2024: "Flat RM15 to Sabah and Sarawak".
  - Shipping sheet, last updated Aug 2026: "RM18 for the first 3 kg, then RM6 per kg. Bulky items: ask Farah".
  - "Affects about 6% of your chats (212 in the last 90 days). In testing, your agent quoted RM15 in 3 of 6 answers."
- **Pick the answer:**
  - "Use the shipping sheet" (recommended: newer and more detailed);
  - "Use the website";
  - "Write it yourself";
  - "Ask a teammate". The card shows "Waiting for Farah (Shipping)", then after about 3 seconds: "Farah confirmed: the sheet is right. Bulky items go by Ta-Q-Bin, price on request."
- **Fill the gap:** "The sheet doesn't say what to charge for bulky items to Sabah and Sarawak. What should your agent do?"
  - "Pass it to your shipping team" (recommended);
  - "Quote a starting price: from RM45";
  - "Take the item details and reply within 2 hours".
- **Which source wins next time:** "When shipping sources disagree, trust: Shipping sheet → Website → CS macros." The setting "If sources still disagree when a customer asks, pass it to your team instead of guessing" is on.
- **Fix it at the source:** "Your website still says RM15, so customers see it there too." Copy updated text: "Shipping to Sabah and Sarawak: RM18 for the first 3 kg, then RM6 for each extra kg. Bulky items such as sofa covers and mattresses are quoted by our team after you order."
- **Quick re-test:** "Re-testing 6 East Malaysia questions, 3 times each…", then "18 of 18 correct or passed to your shipping team".

**Conflict 2: returns window**
- **Stakes:** CS macros (Jan 2026) say "7 days"; website (Jun 2026) says "14 days". "Affects about 3% of chats. In testing, 1 of 3 answers said 7 days."
- **Pick the answer:** "Use the website: 14 days" (recommended: it's your published policy). A follow-up note: "Update your macros doc too, so your team says the same."
- **Quick re-test:** 3 questions × 3, then "9 of 9 correct".

**Conflict 3: a staff name in your data**
- "Your shipping sheet mentions a teammate (Farah). Your agent won't use staff names with customers. It'll say 'our shipping team'." One button: "OK".

Also flagged: "Voucher MERDEKA15 looks expired (ended 31 Aug)."

**Step 3: drafted topics** (top 6)

| Topic | Share |
|---|---|
| Where's my order | 31% (read-only order status: "Projected · weeks 6–12". Until then the agent takes the order number and passes it to the CS team. Sample reply: "Thanks. I've passed order RK10233 to our team, and they'll reply with the tracking details shortly." Line under it: "With order status (weeks 6–12): shares the status and tracking link from Shopee or Lazada.") |
| Shipping cost and time | 17% (includes East Malaysia, 6%) |
| Damaged item / returns | 11% |
| Sizing (bedsheets, fitted sheets) | 9% |
| Vouchers | 7% |
| COD | 5% |

More topics found, not drafted: marketplace cancel or price match 4%, bulk and corporate orders 3%, product care 3%, installation 2%.

**Step 4: voice.** Match the customer (detected: 54% English, 38% Malay, 8% other); a mixed English and Malay reply is allowed; neutral voice; tone Friendly; emoji None. Preview: "Hi! Yes, we deliver to Kota Kinabalu. Sofa covers are bulky, so our shipping team will send you the exact cost shortly."

**Step 5: readiness.** 120 questions, 3 runs each, with rewordings. By topic (question counts follow share of chats): Where's my order 37, Shipping 20, Damaged/returns 13, Sizing 11, Vouchers 8, COD 6, Other 25. Where's my order questions are passed to the team (no order status yet); the headline stays 61/27/12. At 27%, only 32 of the 37 can be handoffs, so 5 count as general delivery questions answered correctly.

| | Answered | Handed off | Wrong | Consistent | **Score** |
|---|---|---|---|---|---|
| Before (conflicts unresolved) | 61% | 27% | 12% | 71% | **70** |
| After | 70% | 28% | 2% | 96% | **88** |

Wrong answers:
1. "Can deliver to Kota Kinabalu? How much for sofa cover?" It said "flat shipping fee of RM15" in 2 of 3 runs. It should say bulky East Malaysia goes to the Shipping team. Show the contrast: **"Today's check: Groundedness ✓ · The response is accurate"** vs **"Readiness: Wrong. Uses the stale website rate."** Fix: resolve conflict 1.
2. "Sofa cover shipping to Kuching still RM15 like website say?" It said "generally RM15" in 1 of 3 runs, and in 1 run gave **no reply**. Fix: resolve conflict 1; turn on the human fallback.
3. "If I change my mind, how many days to return?" It said 7 days in 1 of 3 runs. Fix: resolve conflict 2.

**Step 6: go live.** WhatsApp only; hours Out of hours (00:00–09:00 and weekends); topics: where's my order (passes the order number to the CS team until order status is available, weeks 6–12), damaged/returns, sizing, vouchers, COD on; **shipping to East Malaysia off**; approve replies first on for 7 days; cap 5,000 messages ($200); handoffs: shipping to the Shipping team, the rest to the CS team; human fallback on. "About 24% of WhatsApp chats."

**Step 7: week one.** Live on WhatsApp, out of hours (about 590 chats a week × 24%): 140 chats handled; 81 resolved (58%); 59 passed on; 128 approved as-is and 12 edited (approve-first is on, so these equal handled); 0 East Malaysia rate errors; 2 flagged (a fitted-sheet depth question). Reply check: "Blocked 4 replies with a staff name." Reminder: "Shopee connection needs re-authorising in 11 months; Lazada in 5." Sale prompt: "11.11 is in 3 weeks: add your 11.11 vouchers. MERDEKA15 has expired."

**Value line** (under the week-one stat cards, mirrored on the dashboard): "About 14% of all your WhatsApp chats were resolved by AI this week. First-month target: 15%." This is the memo's value measure (share of enquiries the AI resolves with no human on the live channels) against the first-month target.

**Notes:**
- Step 2: "Cause 3 · KL quote. With this setup the stale RM15 went out in 3 of 6 test runs."
- Step 6: "Cause 4 · Today: all new chats or out of hours, in Flow Builder, not on Basic."

---

## 4. Linh, Linh Studio (Ho Chi Minh City) · impact 7.2

- **Quote:** "I skipped the scenarios part — I thought the knowledge would be enough. It answers questions fine, but the moment someone asks to cancel an order it just says it'll pass them to the team. Which is us."
- **What it shows:** **read-only order status** (projected) and **the reply check** blocking "I'm checking".
- **Business:** women's fashion (office wear, áo dài), about 2,500 orders a month. Customers write in Vietnamese, often without diacritics.

**Step 1: channels**
- Facebook Messenger: 90 days, 2,570 chats.
- Shopee: 90 days, 1,430 chats; orders synced ✓.
- TikTok Shop: 90 days, 1,140 chats; orders synced ✓.
- Zalo: "Not supported yet. We've noted your request."
- LINE Official Account: offered alongside the others, optional. Tile bullets: "Message customers through Zaapi" · "LINE only shares chats from the day you connect" · "Older chats need LINE's own export: ฿555 a month", then an upsell strip: "AI Success Kit includes one month of LINE history. Saves ฿555." with a See the Kit button. Once connected: "Connected. LINE shares chats from today onwards." · "We'll draft from your other channels and add LINE as chats arrive." with the same strip. Counts 0 chats.
- **About 1,700 a month, which is 300+: top 6 drafted.**

**Step 2: what it knows.** Sample file: `linh_studio_faq_sizechart.docx`, all read, including the size table (S–XL by height and weight). Facts: Da Nang delivery 2–4 working days; shipping 30k; COD nationwide; inspect before accepting (no try-on). Live data, never stated: stock, and order status unless read from synced orders.

**Step 3: drafted topics**

| Topic | Share | Note |
|---|---|---|
| Is size X in stock? | 22% | never confirm; pass on |
| Which size fits me? | 18% | |
| Delivery time | 12% | |
| Cancel an order | 9% | drafted from 31 staff replies: "Not shipped: cancel. Shipped: refuse the COD parcel." Needs order status. |
| Exchange a size | 7% | drafted: "within 7 days; customer pays shipping" |
| Refusing delivery (COD) | 6% | |

More topics found, not drafted: fabric and care 5%, Tết pre-orders 4%.

**Order status ("Projected · weeks 6–12"):** a toggle "Let your agent read order status from Shopee and TikTok Shop (read only)". With it on, the cancel topic shows: "Order LS20931 · Not shipped · Shopee". The handoff card shows the staff button: **"Cancel LS20931 (not shipped) [Cancel order]"**.

**Step 4: voice.** Vietnamese; the shop refers to itself as "shop"; calls the customer "bạn"; tone Friendly; emoji A few. Preview: "Dạ đơn LS20931 chưa giao nên shop hủy giúp bạn được ạ. Shop chuyển cho bạn nhân viên xác nhận ngay nhé!" Note: "In testing, a free-text 'call yourself shop' rule held in 1 of 9 replies. As a field, it's applied to every reply."

**Step 5: readiness.** 110 questions, 3 runs each, with rewordings. Before order status is on, cancel questions that aren't wrong count as passed to the team.

| | Answered | Handed off | Wrong | Consistent | **Score** |
|---|---|---|---|---|---|
| Before | 55% | 30% | 15% | 67% | **53** |
| After (projected, with order status) | 71% | 26% | 3% | 95% | **81** |

Wrong answers:
1. "Shop ơi hủy đơn giúp mình với" It said "I'm checking your order now" and nothing happened. It should read the order status, then pass it to staff with the cancel button ready. Fix: turn on order status.
2. "Còn size M không shop?" It said "let me check stock" with no handoff. Fix: "Never confirm stock".
3. "Đổi size được không shop?" It said "not in the system". Fix: accept the drafted exchange topic.

**Reply check demo:** a card showing the blocked reply ("Mình đang kiểm tra trạng thái đơn hàng LS20931…") and what went out instead ("Shop đã chuyển yêu cầu hủy đơn cho nhân viên, bạn sẽ nhận phản hồi trong 30 phút ạ.").

**Step 6: go live.** Facebook; hours All day; topics: sizing, delivery, cancel (with order status), exchange on; stock passed on; approve replies first on; cap 3,000 messages ($120). "About 33% of chats."

**Step 7: week one (order status projected, weeks 6–12).** Live on Facebook (about 200 chats a week × 33%): 66 chats handled; 34 resolved (52%); 32 passed on; 6 cancel requests passed on with the button ready (average staff time 20 seconds); reply check blocked 4 "I'm checking" replies. Sale prompt: "11.11 is in 3 weeks."

**Value line** (under the week-one stat cards, mirrored on the dashboard): "About 17% of all your Facebook chats were resolved by AI this week. First-month target: 15%." This is the memo's value measure (share of enquiries the AI resolves with no human on the live channels) against the first-month target.

**Notes:**
- Step 3: "Cause 4 · HCMC quote. In testing, her own cancel scenario fired 3 of 3 times and resolved 0."
- Step 5: "Order data is already synced in the inbox; the agent can't use it today."

---

## 5. Budi, GadgetKu (Jakarta) · impact 7.0

- **Quote:** "Honestly I signed up and then it was Double 11 and I had no time. It's been sitting there since November."
- **What it shows:** **campaign mode**:
  - signed up on 8 Nov, three days before 11.11;
  - a 10-minute campaign agent, out of hours, on Shopee;
  - the trial clock paused;
  - "finish after the sale" sent by WhatsApp and email;
  - canned quick replies flagged.
- **Business:** phone accessories, about 9,000 orders a month, 3 admins. Customers write informal Bahasa ("kak", "gan").

**Banner (replaces the sale banner):** "11.11 is in 3 days. Set up a campaign agent in 10 minutes now and finish the rest after the sale. Your trial is paused until 18 Nov."

**Step 1: channels**
- Shopee: 90 days, 11,300 chats.
- TikTok Shop: 90 days, 5,800 chats.
- Lazada: 90 days, 1,900 chats.
- LINE Official Account: offered alongside the others, optional. Tile bullets: "Message customers through Zaapi" · "LINE only shares chats from the day you connect" · "Older chats need LINE's own export: ฿555 a month", then an upsell strip: "AI Success Kit includes one month of LINE history. Saves ฿555." with a See the Kit button. Once connected: "Connected. LINE shares chats from today onwards." · "We'll draft from your other channels and add LINE as chats arrive." with the same strip. Counts 0 chats.
- **About 6,500 a month, which is 300+.**
- Campaign mode drafts only the 5 campaign topics now.

**Step 2: what it knows.** Imported: 20 Shopee quick replies.
- **Flag: "3 of these are canned lines, not facts, e.g. 'Ready stok kak, langsung checkout aja'. Your agent won't state stock."**
- Flag: "'Kesalahan pilih tipe bukan tanggung jawab toko' reads as defensive. Use a softer version?" Suggested: "Kalau salah pilih tipe, kakak bisa ajukan pengembalian lewat aplikasi ya."
- Facts: shipping cut-off 15:00; tracking updates within 1×24 hours; 1-month warranty.

**Step 3: campaign pack** (5 topics)

| Topic | Share |
|---|---|
| When will it ship / tracking number | 29% |
| Is it in stock? | 21% (pass on) |
| 11.11 voucher not working | 14% |
| Does it fit my phone? | 12% (pass on; never guess) |
| Cancel (wrong model) | 8% (explain how to cancel in the Shopee app) |

More topics found, not drafted: warranty claims 6%, COD 4%, reseller pricing 3%.

**Step 4: voice.** Informal Bahasa with "kak" (detected: 97% Bahasa); neutral voice; tone Friendly; emoji None.

**Step 5: readiness.** 40 campaign questions from his last 90 days, 3 runs each, with rewordings.

| | Answered | Handed off | Wrong | Consistent | **Score** |
|---|---|---|---|---|---|
| Before | 60% | 22% | 18% | 80% | **68** |
| After | 66% | 31% | 3% | 96% | **86** |

Wrong answers:
1. "Kak, ready stok ga case iPhone 15 Pro warna hitam?" It said "ready stok… langsung checkout" in 4 of 5 runs. Fix: the "Never confirm stock" default, with the canned line flagged.
2. "Kak mau cancel aja deh, salah pilih tipe." It opened with "not the shop's responsibility". Fix: use the softer drafted reply.

**Step 6: go live.** Shopee; hours Out of hours (22:00–08:00); the 5 campaign topics; approve replies first off (campaign mode: human review of a daily sample instead); cap 10,000 messages ($360); handoffs to the Admin team. "About 18% of Shopee chats." Plus: "Remind me to finish setup on 14 Nov" by WhatsApp and email.

**Step 7: week one (11.11 week).** Live on Shopee, out of hours; 11.11 week is about 3× a normal week (about 2,630 chats × 18%): 470 chats handled; 287 resolved (61%); 183 passed on; 0 stock claims; Shopee response rate 96% (demo). Prompt: "11.11 is over. Finish setup: 4 more topics and TikTok Shop, about 15 minutes."

**Value line** (under the week-one stat cards, mirrored on the dashboard): "About 11% of all your Shopee chats were resolved by AI during 11.11, out of hours only. First-month target: 15%." This is the memo's value measure (share of enquiries the AI resolves with no human on the live channels) against the first-month target.

**Notes:**
- Home: "Cause 1 · Jakarta quote. Campaign sign-ups activate worse (brief)."
- Step 2: "In testing, his canned 'ready stok' became a false stock claim in 4 of 5 runs."

---

## 6. Pranee and Fon, Baan Samunprai (Chiang Mai) · impact 6.2

- **Quote:** "I set it up in English because that's what the form was in. But 90% of our customers write in Thai. I'm not sure whether that matters."
- **What it shows:**
  - **the no-history path:** LINE history isn't readable, so guided questions instead;
  - the LINE export in the Kit;
  - voice fields in Thai;
  - the language reassurance;
  - a UI language switch (Thai / English) on the setup home.
- **Business:** herbal supplements, about 1,200 orders a month; Fon (her niece) does the setup. Customers write in Thai.

**Step 1: channels**
- LINE: 12 days since connection, 270 chats. "LINE doesn't let us read chats from before you connected. Want your older LINE chats? The AI Success Kit includes a one-month LINE history export, which costs ฿555 a month on its own." (optional)
- Facebook: 90 days, 640 chats.
- Shopee: small store, 90 days, 120 chats.
- **About 900 a month, which is 300+. Most of the history is on LINE and unreadable, so: "We'll ask you a few questions to fill the gaps."**

**Step 2: guided questions.** One at a time, in Thai with an English toggle. Pre-filled where possible.
1. How many capsules a day for each product? → "Turmeric: 2 capsules twice a day after meals"
2. Current promotions and end dates? → "Buy 3 get 1, until 31 Oct"
3. When do you ship? → "Mon–Sat, orders before 14:00 ship the same day, via Kerry"
4. COD? → "Yes, via Shopee only"
5. Who handles side effects or rashes? → "Pranee"
6. Anything your agent must never say? Pre-filled for supplements: "Never say a product cures or treats any disease (Thai FDA rules)."
7. Do customers send payment slips? → "Yes: pass to a human to check"
8. Anything else customers often ask? → "FDA numbers", with the numbers taken from the Shopee listing scan

Plus: "We scanned your 3 Shopee listings: 3 products, prices and อย. numbers found."

**Step 3: starter topics** (supplements category, plus her answers)

| Topic | Share |
|---|---|
| Dosage | 22% |
| อย. number | 11% |
| Promotions | 10% |
| Delivery | 9% |
| Payment slip | 8% (pass on) |
| Side effect or rash | 4% (pass to Pranee; "Please stop taking it and see a doctor") |

Shares come from the LINE and Facebook chats read.

**Step 4: voice.**
- Reassurance: **"92% of your chats are in Thai. Your agent will reply in Thai, even though you set up in English."**
- Fields: shop speaks as a woman (ค่ะ, ดิฉัน); tone Warm; emoji None.
- Preview: "ขมิ้นชันทานครั้งละ 2 แคปซูล วันละ 2 ครั้งหลังอาหารค่ะ"

**Step 5: readiness.** Based on a standard set of 20 supplement questions plus 28 questions from her 12 days of LINE chats, 3 runs each, with rewordings. Label: "Based on typical supplement questions plus 12 days of your chats. It'll get better after 30 days live."

| | Answered | Handed off | Wrong | Consistent | **Score** |
|---|---|---|---|---|---|
| Before (voice field not set) | 66% | 28% | 6% | 92% | **85** |
| After | 74% | 25% | 1% | 98% | **90** |

Wrong answers:
1. "โปรซื้อ 3 แถม 1 ยังมีอยู่ไหมคะ" It said "not found" and used the male ครับ. Fix: set the shop to speak as a woman; add the promotion (question 2).
2. "ทานแล้วมีผื่นขึ้นค่ะ" It mixed ผม with ค่ะ. Fix: the voice field.

Safety passed: "กินแล้วหายเบาหวานไหมคะ": no cure claim, suggests a doctor ✓ (show as a green "Safe" example).

**Step 6: go live.** LINE; hours Evenings and night (18:00–08:00); topics all; rashes to Pranee; approve replies first on; cap 1,000 messages ($40). "About 35% of LINE chats."

**Step 7: week one.** Live on LINE, evenings and night (about 157 chats a week × 35%): 55 chats handled; 37 resolved (68%); 18 passed on; 12 dosage questions answered; 0 medical claims. Sale prompt: "New Year gift season starts in 9 weeks: add your gift sets."

**Value line** (under the week-one stat cards, mirrored on the dashboard): "About 24% of all your LINE chats were resolved by AI this week. First-month target: 15%." This is the memo's value measure (share of enquiries the AI resolves with no human on the live channels) against the first-month target.

**Notes:**
- Step 1: "Cause 2 · Chiang Mai quote. Her agent's Thai was fine; nothing told her so."
- Step 1 (LINE): "LINE's API can't fetch old chats; the only route is LINE's ฿555/month Chat package export."
