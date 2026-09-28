# Zaapi AI Agent: Test Personas

For the Zaapi Head of Product take-home. Four merchant personas to walk through AI Agent setup (connect → knowledge → persona → scenarios → test → go live) and log where things break.

---

## Prompt used

> I'm doing a take-home for a Head of Product role at Zaapi, a Bangkok-based platform that lets Southeast Asian online sellers manage customer chats from LINE, WhatsApp, Facebook, Instagram, Shopee, Lazada, TikTok Shop and Shopify in one inbox. They've launched an AI Agent that answers customers automatically, but of the merchants who do get it live, the median is 19 days after signup, and around 39% never get it live at all. Median time from signup to touching any setup step is 4 days. Setup goes: connect a channel, add knowledge, set a persona, write scenarios, test, go live.
>
> I want to walk through the setup as different merchants to see where real people would get stuck. Can you create four personas I can use to role-play through the product?
>
> A few things matter to me:
> - They should feel like Zaapi's actual core customers: SMB and mid-market e-commerce sellers across Thailand, Indonesia, Malaysia, the Philippines and Vietnam. Think fashion, beauty, supplements, home goods, electronics accessories. Mostly social-commerce and marketplace sellers, not big enterprises.
> - Spread them across different levels of tech and AI confidence. I'd like one who's quite sophisticated and sceptical, one who's capable but time-poor, one who's a bit lost with software, and one somewhere else interesting. Don't make any of them a caricature.
> - Give each one enough depth that you could stay in character and make realistic decisions for them. For each, include: who they are; channels; customer languages incl. code-switching; what their "knowledge" looks like in reality; the 5–8 most common customer questions in the customer's own words plus 2–3 tricky ones; why they signed up, what would make them trust the AI and what would make them switch it off; time and patience for setup and busiest periods; likely behaviour in each of the six steps; one fear and one "win".
> - Make sure between them they cover different channels (at least one marketplace-heavy seller and one LINE/social-first seller), different countries, and at least one who's non-English-first.
>
> After the four personas, add a short test script for each: the exact test conversations they'd run in test mode (in their customers' language), and what a "good enough to go live" answer would look like to that merchant.
>
> Keep it practical. I'm going to use these to actually click through the platform and note where things break.

---

## At a glance

| | Aisha (KL) | Budi (Jakarta) | Khun Pranee (Chiang Mai) | Joanna (Manila) |
|---|---|---|---|---|
| Archetype | Sophisticated sceptic | Capable, time-poor | Lost with software | Over-trusting fast mover |
| Category | Home goods | Electronics accessories | Herbal supplements | Fashion (live selling) |
| Orders/mo | ~5,000 | ~9,000 | ~1,200 | ~800 |
| Main channels | Shopify, WhatsApp, Shopee, Lazada | Shopee, TikTok Shop, Lazada | LINE OA, Facebook | Instagram, Facebook, TikTok Live |
| Customer language | English, Malay, some Chinese | Bahasa Indonesia (informal) | Thai only | Taglish |
| AI confidence | High, but distrusts vendors | Medium | Low | High, uncritical |
| Most likely failure | Never feels "ready enough" | Stalls in campaign season | English setup, Thai customers | Skips scenarios, goes live, switches off |

---

## Persona 1: Aisha Rahman, the sophisticated sceptic

**Who she is.** 34, Head of Operations at *Rumah Kita*, a Kuala Lumpur home goods brand (bedding, storage, kitchenware). ~5,000 orders/month, RM 1.2M/month GMV. Ex-Lazada category manager, so she knows marketplace rules better than most vendors. Team of 5 CS agents in two shifts (9am–midnight), plus a team lead. She reports to the founder, who pushed for "AI to cut CS headcount".

**Channels.** Own Shopify store (40% of revenue) with WhatsApp Business as main support channel; Shopee and Lazada (55%); a little Instagram. ~60% of chats come via WhatsApp, 35% marketplace chat.

**Languages.** English and Malay, often mixed in one message ("Hi, barang saya belum sampai lagi, can check?"). ~10% Chinese-speaking customers write in simplified Chinese or Manglish.

**What her knowledge really looks like.** Better than most: a Google Doc of CS macros (~60 canned replies), a shipping matrix spreadsheet (West vs East Malaysia rates and lead times, bulky-item surcharges), returns policy on the Shopify site. But the macros are 8 months stale, and the East Malaysia rules (Sabah/Sarawak, bulky items shipped via a different courier) live mostly in her team lead's head.

**Top customer questions.**
1. "Hi, my order #RK10233 dah ship ke? When will arrive?"
2. "Can deliver to Kota Kinabalu? How much shipping?"
3. "Is the bedsheet 100% cotton or blend?"
4. "Queen size fit for 6 feet bed ah?"
5. "Got COD or not?"
6. "Barang sampai rosak, how to return?"
7. "Voucher code tak boleh pakai, why?"

**Tricky ones.**
- "I ordered on Shopee but want to change to your website price, cheaper. Can cancel and reorder?" (channel conflict, marketplace rules)
- "Sofa cover shipping to Kuching still RM15 like website say?" (bulky item + East Malaysia surcharge, a known source of wrong answers)
- An angry customer on WhatsApp: "3rd time asking. Nobody reply. I will post on FB group."

**Why she signed up.** Founder wants CS cost down 30%. She wants the agent to take the "where's my order" and sizing questions so humans handle exceptions.

**What would make her trust it.** Proof, not promises: seeing it answer 50+ real past questions correctly, a clear view of what it will and won't answer, control over handoff rules, and gradual rollout (e.g. 10% of WhatsApp only).

**What would make her switch it off.** One wrong shipping or pricing answer that costs money or triggers a marketplace penalty. Anything that makes her look bad to the founder.

**Time and patience.** Willing to spend 3–4 focused hours but wants structure. Busiest: 11.11, 12.12, Ramadan/Raya (big for home goods), and payday weekends.

**Behaviour through setup.**
1. Connect: already done via Helpdesk. Will check which channels the agent can act on.
2. Knowledge: uploads macros doc, shipping sheet, points crawler at the Shopify site. Then worries about conflicts between sources ("which one wins if the macro and website disagree?").
3. Persona: sets tone carefully, adds "never promise delivery dates, never offer discounts". Will look for per-channel or per-language settings.
4. Scenarios: writes several, but gets frustrated if she can't express rules like "if East Malaysia AND bulky item → hand off".
5. Test: runs a lot of tests, hunting for failures. Can't tell what share of real traffic she has covered; keeps testing and never feels done.
6. Go live: wants to start at a small share on one channel. If the % control isn't obvious or there's no "suggest only" mode, she delays.

**Fear.** "It confidently tells a Sabah customer the wrong shipping price and I only find out from a 1-star review."
**Win.** "WISMO chats down 60% in the first month with zero escalations from the AI." She'd present that to the founder and tell her ex-Lazada network.

---

## Persona 2: Budi Santoso, capable but time-poor

**Who he is.** 29, founder-owner of *GadgetKu*, Jakarta. Phone cases, chargers, earbuds, cables. ~9,000 orders/month, low AOV (~IDR 85k). Team of 3 admins answering chats, plus warehouse staff. He does everything else: ads, sourcing from Shenzhen, marketplace campaigns.

**Channels.** Marketplace-heavy: Shopee (60%), TikTok Shop (30%, growing fast via live selling), Lazada (10%). A WhatsApp number for resellers. Nearly all customer chat is inside marketplace chat.

**Languages.** Informal Bahasa Indonesia with slang and abbreviations ("kak", "gan", "ready?", "brp lama sampe"). Nearly no English.

**What his knowledge really looks like.** Product compatibility lives in the listing titles and admins' heads ("case iPhone 15 fits 15 Pro? No"). Marketplace quick-reply templates (~20) exist inside Shopee Seller Centre. No written policy doc; returns follow each marketplace's own rules.

**Top customer questions.**
1. "Kak, ready stok ga?"
2. "Ini bisa buat iPhone 15 Pro gak kak?"
3. "Kapan dikirim kak? Udah bayar dari kemarin."
4. "Resi nya mana kak?"
5. "Ada warna hitam gak?"
6. "Garansi berapa lama gan?"
7. "Bisa COD?"

**Tricky ones.**
- "Kak mau cancel aja deh, salah pilih tipe." (cancel request: the agent must know marketplace cancel rules and whether it can act)
- "Barangnya rusak kak, charger nya ga ngecas. Mau retur." (return via marketplace flow, needs photo/video evidence)
- During 11.11: "Voucher 11.11 kok ga bisa dipake kak??" (campaign-specific)

**Why he signed up.** Admins drown during campaigns; response-time metrics on Shopee drop and hurt his store rating. He wants replies within 5 minutes, 24/7.

**What would make him trust it.** Fast setup that "just works" with his products, and seeing the chat response-rate metric improve.

**What would make him switch it off.** Wrong compatibility answers that cause returns, or anything that risks marketplace penalties.

**Time and patience.** 20–30 minutes, in fragments, often on his phone at night. Busiest: 9.9, 10.10, 11.11, 12.12, payday sales (25th–5th), Ramadan/Harbolnas. Signed up in late October and immediately hit 11.11.

**Behaviour through setup.**
1. Connect: marketplace channels connected via Helpdesk. May not realise agent capabilities differ by channel.
2. Knowledge: pastes his quick replies. Tries the URL crawler on his Shopee store and isn't sure it worked. Doesn't have a compatibility list.
3. Persona: picks defaults quickly. May not notice the language default.
4. Scenarios: skips ("nanti aja", later). Doesn't see why they're needed.
5. Test: sends 2–3 messages, looks OK, but he's interrupted.
6. Go live: intends to come back after 11.11. Doesn't. The agent sits unused for 6 weeks.

**Fear.** "It says a case fits the wrong phone and I get 200 returns during a campaign."
**Win.** "My Shopee chat response rate stayed above 95% during 11.11 without hiring temp admins."

---

## Persona 3: Khun Pranee Srisuk, a bit lost with software

**Who she is.** 52, co-owner of *Baan Samunprai*, a Chiang Mai herbal supplements brand (turmeric capsules, collagen drinks, herbal balms). ~1,200 orders/month. She answers most chats herself, with her niece Fon (24) helping in the evenings. Fon set up Zaapi after a Facebook ad; Pranee is the one who actually knows the answers.

**Channels.** LINE Official Account (70% of chats, mostly repeat customers), Facebook Page and Messenger (25%), a small Shopee store.

**Languages.** Thai only, with polite particles ("ค่ะ/ครับ"), stickers, voice notes, photos of product labels. Some customers are elderly and write in long, informal messages.

**What her knowledge really looks like.** Almost entirely in her head and in years of LINE chat history. Product details are on the packaging and in Thai FDA (อย.) registration documents. Promotions are announced in LINE broadcasts. Nothing is written as a policy.

**Top customer questions (Thai).**
1. "สวัสดีค่ะ ขมิ้นชันทานวันละกี่เม็ดคะ" (How many turmeric capsules a day?)
2. "มีเลข อย. ไหมคะ" (Does it have an FDA number?)
3. "ส่งของวันไหนคะ ได้เลขพัสดุหรือยัง" (When do you ship? Is there a tracking number?)
4. "โปรซื้อ 3 แถม 1 ยังมีอยู่ไหมคะ" (Is the buy 3 get 1 promo still on?)
5. "เก็บเงินปลายทางได้ไหมคะ" (Can I pay cash on delivery?)
6. "คอลลาเจนทานคู่กับยาความดันได้ไหม" (Can I take the collagen with blood-pressure medicine?)

**Tricky ones.**
- "กินแล้วหายเบาหวานไหมคะ" (Will it cure my diabetes?). This is a regulatory red line: under Thai FDA rules the agent must never make medical claims.
- "ทานแล้วมีผื่นขึ้นค่ะ ทำยังไงดี" (I got a rash after taking it, what should I do?). Must hand off to a human and advise seeing a doctor.
- "โอนเงินแล้วนะคะ" + payment slip photo (payment confirmation, needs a human or order lookup).

**Why she signed up.** Fon said it would let the shop reply at night. Pranee is tired of answering the same dosage question 40 times a day.

**What would make her trust it.** Seeing it reply in natural, polite Thai like she does, and never saying anything about curing illness.

**What would make her switch it off.** Rude or robotic Thai, or any health claim. Losing the personal relationship with regular customers.

**Time and patience.** Low for software; high for customers. Fon has an hour on Sunday evenings. Busiest: Songkran and New Year gift season, Mother's Day (August), and LINE broadcast promo days.

**Behaviour through setup.**
1. Connect: Fon connected LINE and Facebook. Pranee doesn't know what "channel" means in the UI.
2. Knowledge: Fon pastes a few product descriptions from Shopee. The dosage and "never say" rules aren't there because nobody has written them down.
3. Persona: the form is in English, so Fon sets it up in English, without realising the agent may default to English or stiff Thai.
4. Scenarios: "What's a scenario?" The concept doesn't map to how Pranee thinks. Skipped.
5. Test: Fon types a test in English; it looks fine. Nobody tests in Thai, or asks the medical question.
6. Go live: Pranee is nervous and asks Fon to wait. It never goes live.

**Fear.** "It tells a customer our turmeric cures diabetes and we get reported to อย."
**Win.** "It answers the dosage question at 11pm in polite Thai, and my regular customers don't notice it's not me."

---

## Persona 4: Joanna "Jo" Villanueva, the over-trusting fast mover

**Who she is.** 27, founder of *Loveli Closet*, Manila. Affordable women's fashion, new drops every Friday via Instagram and Facebook Live, growing on TikTok Live. ~800 orders/month but chat-heavy: most orders start in DMs ("mine!" culture). Team: herself and two part-time VAs.

**Channels.** Instagram DMs (45%), Facebook Messenger (35%), TikTok Shop (20%). Payment via GCash, Maya and COD.

**Languages.** Taglish, very informal: "Hi po! Avail pa po ba yung black dress? Pwede COD?"

**What her knowledge really looks like.** Uses ChatGPT every day for captions. Policies exist only as Instagram story highlights ("How to order", "Shipping", "No returns unless defective"). Sizes are in product images, not text. Rules change every drop ("reservation holds for 24h only").

**Top customer questions.**
1. "Avail pa po ba?"
2. "HM po? Magkano shipping to Cebu?"
3. "Pwede po COD?"
4. "Size chart po? Kasya kaya sa 5'2, 55kg?"
5. "Mine po yung red one! How to pay?"
6. "Kailan po ship out?"
7. "GCash po ba or Maya?"

**Tricky ones.**
- "Pa-cancel po, nagbago isip ko" (I changed my mind, please cancel): the agent must follow her no-cancel-after-payment rule, not just hand off.
- "Bakit di pa dumadating?! 2 weeks na!" (angry, delayed Lazada/J&T parcel).
- "Pwede pa-reserve until payday?" (reservation rules change per drop).

**Why she signed up.** She misses sales at 2am after Friday drops, and her VAs make mistakes. She thinks AI "already knows how to sell".

**What would make her trust it.** It sounds like her ("po", emojis, friendly) and closes "mine!" orders.

**What would make her switch it off.** If it keeps handing everything to "the team" (which is her), or gets a price or availability wrong during a drop.

**Time and patience.** High enthusiasm, low patience for forms. Sets up in one 40-minute burst. Busiest: every Friday drop, 9.9, 11.11, 12.12, and payday (15th and 30th).

**Behaviour through setup.**
1. Connect: IG and FB connected via Helpdesk.
2. Knowledge: points the crawler at her Instagram (which may not work) or pastes a few highlights. Assumes the AI will figure out the rest.
3. Persona: has fun with this, naming it "Lovi" with a Taglish, emoji-friendly tone.
4. Scenarios: skips entirely. "The knowledge should be enough."
5. Test: asks 3 easy questions, all fine.
6. Go live: 100% of conversations on the Friday drop. By Saturday it has handed off every cancel and reservation question and quoted old stock. She switches it off within 48 hours. This is the 72-hour churn pattern in the brief.

**Fear.** "It tells 30 people something is available when it's sold out, during a live."
**Win.** "Lovi closed 50 'mine!' orders overnight after a drop while I slept."

---

## Test scripts

Run each in test mode, in the persona's customer language. Note: pass / partial / fail, whether it handed off, and whether the merchant would feel safe.

### Aisha (English / Malay, WhatsApp)

1. "Hi, order #RK10233 dah ship ke? When will arrive?"
2. "Can deliver to Kota Kinabalu? How much shipping for sofa cover?"
3. "Queen size bedsheet fit for 6 feet bed ah?"
4. "Barang sampai rosak, how to return?"
5. "Voucher RAYA20 tak boleh pakai, why?"
6. "3rd time asking already. Nobody reply. I'm going to post in FB group."
7. "Bought on Shopee, want cancel and buy from your website cheaper, can?"

**Good enough to go live:** correct West/East Malaysia shipping, or an explicit handoff when unsure. Never invents a price or delivery date. Replies in the customer's language mix. Hands off the angry customer immediately with empathy. Won't advise cancelling a marketplace order to buy elsewhere. She'd need about 90% correct or safely handed off on 50 real past chats.

### Budi (Bahasa Indonesia, Shopee / TikTok Shop)

1. "Kak, ready stok ga case iPhone 15 Pro warna hitam?"
2. "Ini case bisa buat iPhone 15 Pro gak kak? Atau cuma iPhone 15?"
3. "Kapan dikirim kak? Udah bayar dari kemarin."
4. "Kak mau cancel aja deh, salah pilih tipe."
5. "Charger nya ga ngecas kak, mau retur."
6. "Voucher 11.11 kok ga bisa dipake kak??"

**Good enough to go live:** replies in informal Bahasa with "kak". Never guesses compatibility; if unsure, it says so and hands off. Explains the marketplace cancel/return process correctly. Fast replies. He'd go live if it gets the top 5 questions right and doesn't make up compatibility.

### Khun Pranee (Thai, LINE)

1. "สวัสดีค่ะ ขมิ้นชันทานวันละกี่เม็ดคะ"
2. "มีเลข อย. ไหมคะ"
3. "โปรซื้อ 3 แถม 1 ยังมีอยู่ไหมคะ"
4. "เก็บเงินปลายทางได้ไหมคะ"
5. "กินแล้วหายเบาหวานไหมคะ"
6. "ทานแล้วมีผื่นขึ้นค่ะ ทำยังไงดี"
7. "โอนเงินแล้วนะคะ" (with a payment slip image, if the test mode supports images)

**Good enough to go live:** replies in polite, natural Thai (ค่ะ) even though setup was done in English. Never makes a medical claim; for Q5 it says the product is a dietary supplement, not a cure, and suggests seeing a doctor. Q6 goes straight to a human. Doesn't invent a promo that isn't in its knowledge. Pranee would trust it only if Fon reads the answers aloud and they "sound like us".

### Joanna (Taglish, Instagram / Facebook)

1. "Hi po! Avail pa po ba yung black satin dress size M?"
2. "HM po shipping to Cebu? Pwede COD?"
3. "Kasya kaya sa 5'2, 55kg yung size S?"
4. "Mine po yung red one! How to pay po?"
5. "Pa-cancel po, nagbago isip ko. Nakapag-GCash na ako."
6. "Bakit di pa dumadating?! 2 weeks na!"
7. "Pwede pa-reserve until payday po?"

**Good enough to go live:** matches her Taglish, "po" tone. Doesn't claim stock it can't verify. Q4 gives clear payment steps. Q5 applies her rule (no cancel after payment; offer an exchange or store credit) instead of handing off. Q6 apologises and hands off. Q7 applies the 24-hour reservation rule. Jo would go live if it handles the "mine!" flow alone; she'd switch off if it hands off more than a few chats a day.

---

## What to capture per persona

- Time spent in each step, and where the persona would quit or postpone.
- Anything confusing in the copy or UI, from that persona's point of view.
- Whether the product ever tells the merchant it's "ready", or what's missing.
- Language handling: setup language vs reply language.
- Whether scenarios can express the persona's real rules.
- Go-live controls: % of traffic, per-channel settings, suggest/draft mode, rollback.
- Test results in the table format above: question, answer, pass/partial/fail, handoff Y/N.
