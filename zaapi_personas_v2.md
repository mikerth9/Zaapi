# Zaapi AI Agent: Test Personas (v2, one per merchant quote)

For the Zaapi Head of Product take-home. Six merchant personas, each built on one of the six stalled-merchant quotes in the brief, to walk through AI Agent setup (connect → knowledge → persona → scenarios → test → go live) and log where things break.

---

## Prompt used

> I'm doing a take-home for a Head of Product role at Zaapi, a Bangkok-based platform that lets Southeast Asian online sellers manage customer chats from LINE, WhatsApp, Facebook, Instagram, Shopee, Lazada, TikTok Shop and Shopify in one inbox. They've launched an AI Agent that answers customers automatically, but of the merchants who do get it live, the median is 19 days after signup, and around 39% never get it live at all. Median time from signup to touching any setup step is 4 days. Setup goes: connect a channel, add knowledge, set a persona, write scenarios, test, go live.
>
> The brief includes six quotes from merchants who stalled. I've pasted them below with their category, size and city. I want one persona per quote, so each persona is the real person behind that feedback. Keep the category, order volume and city from the brief, and make their story explain how they ended up saying exactly that.
>
> [six quotes pasted]
>
> A few things matter to me:
> - Spread them across different levels of tech and AI confidence, and don't make any of them a caricature.
> - Give each one enough depth that you could stay in character and make realistic decisions for them: who they are and who actually answers chats; channels; customer languages incl. code-switching; what their "knowledge" looks like in reality; the 5–7 most common customer questions in the customer's own words plus 2–3 tricky ones; why they signed up, what would make them trust the AI and what would make them switch it off; time, patience and busiest periods; likely behaviour in each of the six setup steps; one fear and one "win".
> - For each, name the root cause their quote points to, in product terms, and what the product would have needed to do to keep them.
>
> After the personas, add a short test script for each: the exact test conversations they'd run in test mode, in their customers' language, and what a "good enough to go live" answer would look like to that merchant.
>
> Keep it practical. I'm going to use these to actually click through the platform and note where things break.

---

## At a glance

| # | Persona | Brief quote (short) | Category · size · city | Main channels | Customer language | AI confidence | Root cause it points to |
|---|---|---|---|---|---|---|---|
| 1 | Nattaya | "How do I know it's ready?" | Beauty · ~3,000/mo · Bangkok | LINE OA, Shopee, TikTok Shop | Thai, Thai-English | High, risk-averse | No readiness signal |
| 2 | Jo | "Our policies are just things we know" | Fashion · ~800/mo · Manila | Instagram, Facebook Live | Taglish | Medium | Blank-page authoring |
| 3 | Aisha | "Told a customer the wrong thing about East Malaysia" | Home goods · ~5,000/mo · KL | WhatsApp, Shopify, Shopee, Lazada | English/Malay mix | High, sceptical | Unsafe go-live, no ramp or guardrails |
| 4 | Khun Pranee | "Set it up in English… customers write in Thai" | Supplements · ~1,200/mo · Chiang Mai | LINE OA, Facebook | Thai only | Low | Wrong language defaults |
| 5 | Budi | "Then it was Double 11 and I had no time" | Electronics accessories · ~9,000/mo · Jakarta | Shopee, TikTok Shop, Lazada | Informal Bahasa | Medium | Setup too long for campaign timing, no re-engagement |
| 6 | Linh | "I skipped the scenarios… it just passes to the team" | Fashion · ~2,500/mo · Ho Chi Minh City | Facebook, Zalo (not supported), Shopee, TikTok Shop | Vietnamese | Medium-high | Scenarios optional and poorly explained |

Note on persona 3: the brief lists these six as merchants who "never got an agent live", yet Aisha's quote describes going live and switching off. Treat her as the 72-hour switch-off pattern (9 of the 61 who went live). The inconsistency is worth a line in the memo or a question to Zaapi.

---

## Persona 1: Nattaya "Nat" Charoenwong, the careful perfectionist

> "I added our FAQ document but I don't know if that's enough. How do I know it's ready? I don't want to find out from a customer."

**Who she is.** 31, co-founder and head of brand at *Glow Lab*, a Bangkok skincare brand (serums, sunscreen, cleansers). ~3,000 orders/month, high repeat rate. Former marketing manager at a big Thai cosmetics group, so brand voice and reputation are everything to her. Four chat admins, plus a beauty advisor who handles skin-concern questions.

**Channels.** LINE Official Account (55%, loyal customers), Shopee Mall (25%), TikTok Shop (15%, from affiliate live sellers), Instagram DMs.

**Languages.** Thai, frequently mixed with English skincare terms: "ผิวแพ้ง่ายใช้ serum vitamin C ได้ไหมคะ" (Can sensitive skin use the vitamin C serum?).

**What her knowledge really looks like.** A polished 12-page FAQ PDF (ingredients, routines, shipping, returns) made for the website. Good on product facts, thin on edge cases: skin reactions, mixing with other actives, and fake products bought from unofficial sellers.

**Top customer questions.**
1. "ผิวแพ้ง่ายใช้ได้ไหมคะ" (Is it OK for sensitive skin?)
2. "ใช้คู่กับ retinol ได้ไหมคะ" (Can I use it with retinol?)
3. "ทาก่อนหรือหลังกันแดดคะ" (Before or after sunscreen?)
4. "มี อย. ไหมคะ" (Is it FDA registered?)
5. "ส่งกี่วันถึงคะ" (How many days to deliver?)
6. "ซื้อใน Shopee กับ LINE ราคาเท่ากันไหม" (Same price on Shopee and LINE?)

**Tricky ones.**
- "ใช้แล้วหน้าแดง แสบมากค่ะ" (My face is red and burning after using it): must hand off to the beauty advisor, never diagnose.
- "ซื้อจากร้านอื่นใน Shopee ถูกกว่า ของแท้ไหม" (Bought cheaper from another Shopee shop, is it genuine?): brand-protection wording.
- "ท้องอยู่ใช้ได้ไหมคะ" (Can I use it while pregnant?): medical-adjacent, must be careful.

**Why she signed up.** Admins answer the same routine questions 100 times a day. She wants them focused on skin consultations that convert.

**What would make her trust it.** Evidence that it's ready: a clear list of what it can answer, what it will hand off, and proof on real customer questions before a single customer sees it.

**What would make her switch it off.** Any off-brand or unsafe skin advice. One screenshot in a beauty Facebook group would be a disaster.

**Time and patience.** High patience and willing to spend hours, but only if she can see progress. Busiest: 11.11, 12.12, Songkran (sunscreen season), payday campaigns.

**Behaviour through setup.**
1. Connect: done via Helpdesk.
2. Knowledge: uploads the FAQ PDF. Then stops: "Is that enough?" Nothing in the product tells her.
3. Persona: carefully written, on-brand. Adds "never give medical advice".
4. Scenarios: writes 2–3, unsure how many is "enough".
5. Test: tests 20+ questions, finds one mediocre answer, loses confidence. No coverage or score to tell her where she stands.
6. Go live: never. She keeps meaning to "do one more round of testing".

**Root cause.** No readiness signal. The test step is a blank chat, so the merchant has to invent the exam and grade it herself.
**What would have kept her.** A readiness report run on her real past LINE questions: what share answered well, what's missing, and one-click fixes. Plus a suggest-only mode to build trust safely.

**Fear.** "A customer with a reaction gets told to 'keep using it' and posts it online."
**Win.** "It handled 70% of routine LINE chats, on-brand, and every skin concern went straight to our advisor."

---

## Persona 2: Joanna "Jo" Villanueva, the policies-in-my-head seller

> "I wasn't sure what I was supposed to write. It asked for our policies, but our policies are just things we know. Nobody has written them down."

**Who she is.** 27, founder of *Loveli Closet*, Manila. Affordable women's fashion, new drops every Friday via Instagram and Facebook Live. ~800 orders/month, but chat-heavy: most orders start in DMs ("mine!" culture). Team: herself and two part-time VAs she trained by example.

**Channels.** Instagram DMs (50%), Facebook Messenger (40%), a small TikTok Shop. Payment via GCash, Maya and COD.

**Languages.** Taglish, informal: "Hi po! Avail pa po ba yung black dress? Pwede COD?"

**What her knowledge really looks like.** Nowhere written. Rules live in Instagram story highlights, her VAs' memory and hundreds of past DM replies: reservations hold for 24 hours, no returns unless defective, shipping rates by island group, which courier for Mindanao.

**Top customer questions.**
1. "Avail pa po ba?"
2. "HM po? Magkano shipping to Cebu?"
3. "Pwede po COD?"
4. "Kasya kaya sa 5'2, 55kg?"
5. "Mine po yung red one! How to pay?"
6. "Kailan po ship out?"

**Tricky ones.**
- "Pwede pa-reserve until payday po?" (her 24-hour rule, sometimes bent for regulars)
- "Pa-cancel po, nakapag-GCash na ako." (no-cancel-after-payment rule, offer exchange)
- "Defective po yung zipper, pwede ibalik?" (returns only if defective, needs photo)

**Why she signed up.** She misses sales at 2am after drops, and VAs give inconsistent answers.

**What would make her trust it.** It "knows" her rules without her writing a manual, and sounds like her.

**What would make her switch it off.** Constant handoffs back to her, or wrong stock and price answers mid-drop.

**Time and patience.** Enthusiastic but hates forms. One 30–40 minute session. Busiest: every Friday drop, 9.9, 11.11, 12.12, paydays (15th and 30th).

**Behaviour through setup.**
1. Connect: IG and FB via Helpdesk.
2. Knowledge: faces empty "shipping policy / returns policy" boxes and freezes. Types two lines, feels it's not good enough, leaves.
3. to 6. Never reached.

**Root cause.** Blank-page authoring. The product asks for documents SMBs don't have, when the answers already exist in Zaapi's own Helpdesk chat history.
**What would have kept her.** "We read your last 90 days of chats and drafted your policies. Check these 8." Or an interview-style setup where the agent asks her questions in chat and writes the policy for her.

**Fear.** "Writing everything down will take a week I don't have."
**Win.** "It figured out my shipping rates and reservation rule from my old DMs, I just said yes."

---

## Persona 3: Aisha Rahman, burned by the first weekend

> "We turned it on Friday. On Saturday it told a customer the wrong thing about our shipping to East Malaysia, my team panicked, so we turned it off. Maybe we try again later."

**Who she is.** 34, Head of Operations at *Rumah Kita*, a Kuala Lumpur home goods brand (bedding, storage, kitchenware). ~5,000 orders/month. Ex-Lazada category manager. Five CS agents across two shifts; the founder wants "AI to cut CS cost".

**Channels.** WhatsApp Business (60% of chats) tied to her Shopify store, Shopee and Lazada (35%), a little Instagram.

**Languages.** English and Malay mixed: "Hi, barang saya belum sampai lagi, can check?" Around 10% of customers write in Chinese or Manglish.

**What her knowledge really looks like.** A decent CS macros doc and a shipping matrix spreadsheet. But the East Malaysia exceptions (Sabah/Sarawak surcharges, a different courier for bulky items, longer lead times) live in the team lead's head, and the website shipping page is out of date.

**Top customer questions.**
1. "Order #RK10233 dah ship ke? When arrive?"
2. "Can deliver to Kota Kinabalu? How much?"
3. "Queen size fit 6 feet bed ah?"
4. "Got COD?"
5. "Barang sampai rosak, how to return?"
6. "Voucher tak boleh pakai, why?"

**Tricky ones.**
- "Sofa cover shipping to Kuching still RM15 like website?" (bulky + East Malaysia: exactly what went wrong)
- "3rd time asking. Nobody reply. I post in FB group." (angry, needs immediate human)
- "Bought on Shopee, want cancel and buy from website cheaper?" (marketplace rules)

**Why she signed up.** Cut WISMO ("where is my order") volume so the team handles exceptions.

**What would make her trust it.** Controlled rollout, a small % first, with alerts on low-confidence answers and an easy review of what it said.

**What would make her switch it off.** What already happened: a wrong answer on a weekend with nobody watching.

**Time and patience.** Structured; will give 3–4 hours. Busiest: 11.11, 12.12, Raya, payday weekends.

**Behaviour through setup.**
1. Connect: done.
2. Knowledge: uploads macros, points the crawler at the website, so the old shipping page conflicts with the spreadsheet.
3. Persona: careful "never promise delivery dates".
4. Scenarios: a few, but can't express "East Malaysia + bulky → hand off".
5. Test: tests West Malaysia questions. Passes.
6. Go live: 100% of WhatsApp on a Friday. Wrong East Malaysia answer on Saturday. Off by Saturday night, and it never came back on.

**Root cause.** Go-live is all-or-nothing with no safety net: no staged rollout default, no conflict detection between sources, no low-confidence handoff, no weekend alerting. One error destroys trust.
**What would have kept her.** Suggest mode first, then 10–20% of traffic. Detecting conflicts between sources ("your website says RM15, your sheet says RM45 for Sabah"). Auto-handoff on low confidence. A "what the agent said today" digest. And a guided "fix and relaunch" path after a switch-off.

**Fear.** "It happens again and the founder decides AI doesn't work."
**Win.** "Two weeks at 20%, zero wrong answers, then we scaled up."

---

## Persona 4: Khun Pranee Srisuk, set up in the wrong language

> "I set it up in English because that's what the form was in. But 90% of our customers write in Thai. I'm not sure whether that matters."

**Who she is.** 52, co-owner of *Baan Samunprai*, a Chiang Mai herbal supplements brand (turmeric capsules, collagen drinks, herbal balms). ~1,200 orders/month. She answers most chats herself; her niece Fon (24) helps in the evenings and handled the Zaapi signup.

**Channels.** LINE Official Account (70%, many repeat and older customers), Facebook Messenger (25%), a small Shopee store.

**Languages.** Thai only, polite particles, stickers, voice notes, photos of labels and payment slips.

**What her knowledge really looks like.** In her head and years of LINE chats. Product facts on packaging and Thai FDA (อย.) documents. Promotions go out as LINE broadcasts.

**Top customer questions.**
1. "ขมิ้นชันทานวันละกี่เม็ดคะ" (How many capsules a day?)
2. "มีเลข อย. ไหมคะ" (Is there an FDA number?)
3. "ส่งของวันไหนคะ ได้เลขพัสดุหรือยัง" (When do you ship? Tracking?)
4. "โปรซื้อ 3 แถม 1 ยังมีไหมคะ" (Is buy 3 get 1 still on?)
5. "เก็บเงินปลายทางได้ไหมคะ" (Cash on delivery?)
6. "คอลลาเจนทานคู่กับยาความดันได้ไหม" (Can I take collagen with blood-pressure medicine?)

**Tricky ones.**
- "กินแล้วหายเบาหวานไหมคะ" (Will it cure my diabetes?): must never make medical claims under Thai FDA rules.
- "ทานแล้วมีผื่นขึ้นค่ะ" (I got a rash after taking it): immediate human handoff and advise a doctor.
- "โอนเงินแล้วนะคะ" + slip photo: payment confirmation.

**Why she signed up.** Fon said it would reply at night. Pranee answers the dosage question 40 times a day.

**What would make her trust it.** Natural, polite Thai that sounds like her, and never a health claim.

**What would make her switch it off.** Robotic or English replies to Thai customers, or any medical claim.

**Time and patience.** Low for software, high for customers. Fon has an hour on Sunday evenings. Busiest: New Year gift season, Songkran, Mother's Day (August).

**Behaviour through setup.**
1. Connect: Fon connected LINE and FB. Pranee doesn't know what "channel" means.
2. Knowledge: Fon pastes Shopee product descriptions (in Thai), with no dosage rules or "never say" list.
3. Persona: the form is in English, so Fon picks English everywhere. Nobody knows whether the agent will reply in Thai.
4. Scenarios: "What's a scenario?" Skipped.
5. Test: Fon tests in English. Looks fine. Nobody tests in Thai or asks the diabetes question.
6. Go live: Pranee isn't confident and says wait. It never goes live.

**Root cause.** Language defaults follow the UI, not the merchant's customers. The product never shows what the agent will actually sound like to her customers, or flags category risks (health claims).
**What would have kept her.** Detect the customers' language from chat history ("90% of your chats are Thai, reply in Thai?"). A Thai setup UI. Test previews in Thai using her real past questions. Category templates for supplements with regulatory "never say" rules pre-filled.

**Fear.** "It says our turmeric cures diabetes and we get reported to อย."
**Win.** "At 11pm it answered in polite Thai and my regular customers didn't notice it wasn't me."

---

## Persona 5: Budi Santoso, lost to Double 11

> "Honestly I signed up and then it was Double 11 and I had no time. It's been sitting there since November."

**Who he is.** 29, founder-owner of *GadgetKu*, Jakarta. Phone cases, chargers, earbuds, cables. ~9,000 orders/month, low AOV. Three chat admins plus warehouse staff; he runs ads, sourcing and campaigns himself.

**Channels.** Marketplace-heavy: Shopee (60%), TikTok Shop (30%, live selling), Lazada (10%). A WhatsApp number for resellers.

**Languages.** Informal Bahasa with slang: "kak", "gan", "ready?", "brp lama sampe".

**What his knowledge really looks like.** Compatibility in listing titles and admins' heads. ~20 quick-reply templates inside Shopee Seller Centre. Returns follow each marketplace's rules.

**Top customer questions.**
1. "Kak, ready stok ga?"
2. "Bisa buat iPhone 15 Pro gak kak?"
3. "Kapan dikirim kak? Udah bayar dari kemarin."
4. "Resi nya mana kak?"
5. "Garansi berapa lama gan?"
6. "Bisa COD?"

**Tricky ones.**
- "Kak mau cancel aja, salah pilih tipe." (marketplace cancel rules)
- "Charger nya ga ngecas, mau retur." (marketplace return flow, needs video evidence)
- "Voucher 11.11 kok ga bisa dipake kak??" (campaign-specific)

**Why he signed up.** Chat response rate on Shopee drops during campaigns and hurts his store rating. He signed up in late October, specifically to survive 11.11.

**What would make him trust it.** Live in under an hour with his products, and a visible response-rate improvement.

**What would make him switch it off.** Wrong compatibility answers causing returns, or marketplace penalties.

**Time and patience.** 20–30 minutes at a time, on his phone at night. Busiest: 9.9, 10.10, 11.11, 12.12, payday (25th–5th), Ramadan/Harbolnas.

**Behaviour through setup.**
1. Connect: marketplaces via Helpdesk. Doesn't realise agent capabilities differ by channel.
2. Knowledge: pastes quick replies; tries crawling his Shopee store and isn't sure it worked.
3. Persona: defaults.
4. Scenarios: "nanti aja" (later).
5. Test: two messages, then interrupted.
6. Go live: planned "after 11.11". Then 12.12. Then Harbolnas. Still sitting there.

**Root cause.** Setup takes longer than the window a merchant has before campaign season. The product doesn't know about marketplace calendars and doesn't re-engage stalled accounts. Marketplace channels also look harder to set up (order actions, platform rules), which explains why they're slower.
**What would have kept him.** A 15-minute "campaign-ready" quick start that covers the top 5 WISMO and stock questions from his history. Campaign-aware nudges ("11.11 is in 12 days, get your top questions covered now"). A win-back flow after the campaign, showing chats he could have automated.

**Fear.** "It tells people a case fits the wrong phone and I get 200 returns in a campaign."
**Win.** "Response rate stayed above 95% during 11.11 without temp admins."

---

## Persona 6: Nguyễn Thị Linh, skipped the scenarios

> "I skipped the scenarios part. I thought the knowledge would be enough. It answers questions fine, but the moment someone asks to cancel an order it just says it'll pass them to the team. Which is us."

**Who she is.** 30, owner of *Linh Studio*, a Ho Chi Minh City women's fashion brand (office wear, áo dài for Tết). ~2,500 orders/month. Tech-comfortable: uses Canva and ChatGPT, runs her own Facebook ads. Team of 3 chat staff.

**Channels.** Facebook Page and Messenger (45%), Shopee (25%), TikTok Shop (20%), and Zalo (a big share of repeat-customer chat, but not among Zaapi's supported channels, so she still answers it by hand).

**Languages.** Vietnamese, informal, often without diacritics: "c oi con size M ko a" (Is there still size M?).

**What her knowledge really looks like.** A decent Google Doc FAQ and size chart. Operational rules (cancellations, exchanges, COD refusals) live in staff habits.

**Top customer questions.**
1. "Còn size M không shop?" (Is size M in stock?)
2. "Mình cao 1m58, 50kg mặc size gì?" (I'm 1.58m and 50kg, what size?)
3. "Ship về Đà Nẵng mấy ngày?" (How many days to Da Nang?)
4. "Có COD không shop?" (Cash on delivery?)
5. "Được kiểm tra hàng trước khi nhận không?" (Can I inspect before accepting?)
6. "Chất vải có nhăn không?" (Does the fabric wrinkle?)

**Tricky ones.**
- "Shop ơi hủy đơn giúp mình với" (Please cancel my order): her rule is to cancel if not yet shipped, otherwise refuse the COD parcel. The agent hands off every time.
- "Đổi size được không?" (Can I exchange sizes?): exchange within 7 days, customer pays shipping.
- "Mình không nhận hàng được, bom hàng thì sao?" (What if I refuse delivery?): COD refusals are a big cost in Vietnam.

**Why she signed up.** Staff spend hours on repetitive chats; she wants the agent to handle whole conversations, not just FAQs.

**What would make her trust it.** Resolving operational requests (cancel, exchange) itself, following her rules.

**What would make her switch it off.** It's not that it's wrong, it's that it's useless: handing everything real back to her team, so there's no saving.

**Time and patience.** Moderate; one or two sessions. Busiest: Tết (biggest), 11.11, 12.12, mid-month and payday sales.

**Behaviour through setup.**
1. Connect: FB, Shopee, TikTok Shop. Asks where Zalo is.
2. Knowledge: uploads FAQ and size chart. Good.
3. Persona: friendly Vietnamese tone ("shop", "bạn").
4. Scenarios: skips. The step looks optional and she doesn't see what it adds beyond knowledge.
5. Test: FAQ questions pass.
6. Go live: goes live on Facebook, sees every cancel and exchange handed off. She calls it pointless and turns it off, or leaves it on with almost no value.

**Root cause.** Scenarios are optional and framed as extra work, but they're where the real value (and the retention correlation) sits. The product doesn't show the merchant which of her real conversations need a scenario, or that knowledge alone can't take actions.
**What would have kept her.** Suggested scenarios mined from her chat history ("23% of your chats are cancellations, here's a draft rule from how your team usually replies"). Showing "without this scenario, these conversations get handed off". Making the top 3 scenarios part of the core path, not optional.

**Fear.** "I pay for AI and my team still does all the real work."
**Win.** "It cancels unshipped orders and handles size exchanges on its own. My staff only see the weird ones."

---

## Test scripts

Run each in test mode, in the persona's customer language. Record: question, answer, pass / partial / fail, handoff Y/N, and whether the merchant would feel safe.

### 1. Nattaya (Thai / Thai-English, LINE)

1. "ผิวแพ้ง่ายใช้ serum vitamin C ได้ไหมคะ"
2. "ใช้คู่กับ retinol ได้ไหมคะ"
3. "ทาก่อนหรือหลังกันแดดคะ"
4. "มี อย. ไหมคะ"
5. "ใช้แล้วหน้าแดง แสบมากค่ะ"
6. "ท้องอยู่ใช้ได้ไหมคะ"
7. "ซื้อจากร้านอื่นใน Shopee ถูกกว่า ของแท้ไหม"

**Good enough to go live:** accurate on product facts from the FAQ. Polite Thai (ค่ะ), handling English skincare terms. Q5 and Q6 go to a human with care and no diagnosis. Q7 is on-brand and steers to official stores. Critically, she needs the product to show her a summary of coverage, not just individual answers.

### 2. Jo (Taglish, Instagram / Facebook)

1. "Hi po! Avail pa po ba yung black dress size M?"
2. "HM po shipping to Cebu? Pwede COD?"
3. "Pwede pa-reserve until payday po?"
4. "Pa-cancel po, nakapag-GCash na ako."
5. "Defective po yung zipper, pwede ibalik?"

**Good enough to go live:** matches her "po" tone. Doesn't invent stock. Applies her real shipping, reservation and returns rules. Since she never wrote them, the key test is whether the product helped her get those rules in at all. Record how the knowledge step handles "I have no documents".

### 3. Aisha (English / Malay, WhatsApp)

1. "Hi, order #RK10233 dah ship ke? When arrive?"
2. "Can deliver to Kota Kinabalu? How much for sofa cover?"
3. "Sofa cover shipping to Kuching still RM15 like website say?"
4. "Barang sampai rosak, how to return?"
5. "3rd time asking. Nobody reply. I'm going to post in FB group."
6. "Bought on Shopee, want cancel and buy from website cheaper, can?"

**Good enough to go live:** correct East Malaysia and bulky pricing, or an explicit handoff when unsure (never a confident wrong answer). Flags the conflict between website and spreadsheet during setup. Angry customer goes straight to a human. Check the go-live controls: % of traffic, suggest mode, alerts, rollback.

### 4. Khun Pranee (Thai, LINE), with setup done in English

1. "สวัสดีค่ะ ขมิ้นชันทานวันละกี่เม็ดคะ"
2. "มีเลข อย. ไหมคะ"
3. "โปรซื้อ 3 แถม 1 ยังมีอยู่ไหมคะ"
4. "เก็บเงินปลายทางได้ไหมคะ"
5. "กินแล้วหายเบาหวานไหมคะ"
6. "ทานแล้วมีผื่นขึ้นค่ะ ทำยังไงดี"

**Good enough to go live:** replies in natural polite Thai despite the English setup. Q5: no medical claim; says it's a supplement, not a cure, and suggests seeing a doctor. Q6: immediate human handoff. No invented promotions. Record whether the product warned about the language mismatch at any point.

### 5. Budi (Bahasa Indonesia, Shopee / TikTok Shop)

1. "Kak, ready stok ga case iPhone 15 Pro warna hitam?"
2. "Ini bisa buat iPhone 15 Pro gak kak? Atau cuma iPhone 15?"
3. "Kapan dikirim kak? Udah bayar dari kemarin."
4. "Kak mau cancel aja deh, salah pilih tipe."
5. "Voucher 11.11 kok ga bisa dipake kak??"

**Good enough to go live:** informal Bahasa with "kak". Never guesses compatibility. Explains marketplace cancel steps correctly. Time the whole setup: how long does the fastest credible path to a working agent take? Note anything that differs for marketplace channels vs social channels.

### 6. Linh (Vietnamese, Facebook), with scenarios skipped

1. "Còn size M không shop?"
2. "Mình cao 1m58, 50kg mặc size gì?"
3. "Ship về Đà Nẵng mấy ngày?"
4. "Shop ơi hủy đơn giúp mình với"
5. "Đổi size được không shop?"
6. "c oi con size M ko a" (no diacritics)

**Good enough to go live:** FAQ answers pass, including no-diacritic input. Record exactly what happens on Q4 and Q5 without scenarios. Then add one cancellation scenario and re-run, and compare. Note whether the product ever told her scenarios were needed for this.

---

## What to capture per persona

- Time spent in each step, and where the persona would quit or postpone.
- Confusing copy or UI from that persona's point of view.
- Whether the product ever signals "ready", or what's missing.
- Setup language vs reply language.
- Whether scenarios can express the persona's real rules, and whether skipping them is flagged.
- Go-live controls: % of traffic, per-channel settings, suggest/draft mode, alerts, rollback.
- Differences between marketplace and social channels.
- Test results in the format above.
