# Zaapi walkthrough log

Run per [prompts/02_walkthrough_prompt.md](../prompts/02_walkthrough_prompt.md). Browser: built-in Claude Browser pane (Claude-in-Chrome extension was not connected this session — substituted; isolated tab, same effect for a fresh signup). Content: Fresh Laundry (`research/fresh_laundry_kb.md`). Personas: `zaapi_personas.md` (Aisha, Budi, Pranee/Fon, Joanna).

Evidence tags: [product] seen on screen · [help] help centre · [inference] reasoning.

---

## 1. Summary

Fresh Laundry did **not** go live — I stopped before publishing, per the rule — but was **fully ready to**: knowledge, two real scenarios, personality, and 10/10 test messages passed with correct pricing, correct policy, appropriate refusals, and proper handoffs. Active build time for a diligent, English-fluent, everything-written-down operator ran to roughly **60–90 minutes**, well past the brief's "half an hour," even before counting Knowledge Source's multi-minute silent processing waits. The real product is **tabs, not a wizard** — no order, no progress indicator, no readiness signal anywhere. **Aisha** would likely reach Deploy and stall there — no share-of-conversations control exists, only two all-or-nothing templates. **Budi** would get stuck at Knowledge (his content is Shopee-only, explicitly warned against, then fails with a misleading "character limit" error 8+ minutes later). **Pranee/Fon** could technically finish (language defaults correctly to Thai, untested by her) but her own help-centre searches, in Thai, never surface the one article that would reassure her — she'd stay QUIT/nervous per her persona. **Joanna** sails through fastest, skips scenarios exactly as predicted, and nothing stops her going live at 100% — the brief's 72-hour-churn pattern has no product-side guardrail.

---

## Step 0 — Entry

- **[product]** `https://app.zaapi.com/login` redirects unauthenticated visits. Screen: "Welcome to Zaapi!", language toggle "EN" top-left, login form (Email/Phone tab toggle, Email, Password, "Forgot your password? Reset password", "Log in" button, "New to Zaapi? Create an account" link).
- Next: open the signup screen, log its fields, then **stop for Mike** to supply the fresh signup email/password (per the prompt's stop rule — I don't create accounts or handle credentials myself).

## Step 0b — Registration screen (`/register`)

- **[product]** Heading: "Start your 7-day free trial" / "The AI-native customer service platform". Fields: **Business name**, **Email**, **Phone number** (country-code dropdown, defaults to +66 Thailand, huge list), **Password**, optional "Have a referral code?" toggle. Button: "Get started". Footnotes: **"7-day free trial · No credit card required"**. Confirms O6 (7-day trial) and rules out alternative-explanation #2 at signup, at least — no card asked for up front `[product]`.
- Social proof strip: "Powering messaging for 5,000+ businesses" / 10+ Messaging Channels / 90% Chats Resolved with AI / 3x Faster Replies / 85% Lower Support Costs.
- No language-of-interface choice visible on this screen itself (top-level "EN" toggle is global nav, not part of the form) — worth checking after login whether AI Agent setup has its own language question, separate from interface language (H11).
- **Persona lens:**
  - **Aisha** — OK. Reads "no credit card required" and the trial length before committing; this is exactly the proof-before-commitment behaviour the persona file gives her.
  - **Budi** — OK, fast. On his phone at night, this is a short form; he'd fill it in under a minute (persona: "20–30 minutes, in fragments, on his phone").
  - **Pranee/Fon** — OK for Fon (she's doing the setup), but the form is in English, which the persona file flags directly: "the form is in English, so Fon sets it up in English, without realising the agent may default to English or stiff Thai." Front-loads H11.
  - **Joanna** — OK, fast, matches her "one 40-minute burst" pattern; enthusiasm, low patience for forms, and this form is short enough not to test that.

**Stopping here per the prompt's rule:** email/password is a "you do this yourself" item. I need from you to continue:
1. A fresh email for signup (throwaway is fine — the KB is fictional and this is a test account).
2. A business name to enter (suggest "Fresh Laundry", matching the KB).
3. A phone number to use (Thai +66 format works, or another SEA country per your preference).
4. A password (I won't see anything sensitive if you'd rather type it in yourself — say when you're at the field and I'll pause).

**Signup identity used for this run** (for my own reference, not the merchant persona): Business name "Test Business", a throwaway email address and phone number, and a generated password (details kept out of this log). Account itself is a shell — the *content* built inside (AI Agent knowledge/persona) is Fresh Laundry, per the prompt.

**[product]** Social proof strip on `/register` right panel lists real logos: Atelier Wen, Blackmores, Colgate-Palmolive, Fitté Lalore, Secret Lab, Unilever, Delugs, Innisfree, L'Occitane — skews beauty/lifestyle/home mid-market, consistent with the brief's SMB/mid-market SEA e-commerce framing.

**[product]** Below the password field, a **Cloudflare "Verify you are human" checkbox** appears once all fields are filled. This is a CAPTCHA — stopped here per the rule; Mike to complete it and click "Get started".

**Correction:** switched to the Claude-in-Chrome connector once Mike enabled it (built-in browser pane's Cloudflare check wasn't passing). In real Chrome, the Cloudflare Turnstile passed automatically ("Success!") with no click needed — no CAPTCHA-solving action taken.

**[product]** Password field has live validation shown only after first submit attempt fails: "8 characters minimum / One lowercase character (a-z) / One uppercase character (A-Z) / One number" — my first generated password had no digit and was silently rejected (button stayed grey, no other error text) until I reread the checklist. **Minor friction note for the memo's texture, not a hypothesis:** the button doesn't explain *why* it's disabled until you notice the checklist below the CAPTCHA widget, easy to miss on a first pass.

**[product]** After resubmitting with a valid password, redirected to `/register/verify?userId=...&email=...` — **email verification by link**, not OTP. Screen: "Please verify your email" / "We've sent an email verification link to your email: [the signup address]" / "Didn't get an email? Click to resend" / "Need help? Contact us".

**Persona lens (signup form overall, now that it's complete):**
- **Aisha** — OK. A password-complexity error wouldn't faze her.
- **Budi** — SLOWED, mildly. On his phone at night in fragments (persona trait), a silent-disabled-button state with no inline error until he scrolls to the checklist is exactly the kind of friction that costs a distracted, time-poor merchant a few extra minutes — small, but real given his 20–30 minute total patience budget.
- **Pranee/Fon** — OK for Fon; she's comfortable enough with software to read a checklist, this is a standard pattern.
- **Joanna** — OK, she moves fast and wouldn't be troubled by a retry.

**Email verified** and logged in. Landed directly on `/tickets?inbox=my_inbox` — the **Helpdesk inbox**, not an AI Agent or onboarding-checklist screen. Top banner: **"Free trial ends in 6 days"** with a "Subscribe now" button already visible on the very first authenticated screen (day-0 elapsed already counted as 1 of the 7 — worth a precise re-check later, minor). This is a live counter/urgency element from day one, relevant to O6 (7-day trial vs 19-day median go-live): the platform is already nudging toward payment before the merchant has done anything.

## Step 0c — Post-signup onboarding modal (2 steps)

- **[product]** Step 1 of 2, "Tell us a bit about yourself / This helps customize your experience": **What's your name?** (free text) and **How many support agents do you have?** (buttons: 1, 2-10, 11-25, 26-50, 51+). Filled: name "Test User", agents "2-10". No skip option visible on step 1 — it appears to gate step 2.
- **[product]** Step 2 of 2, **"Try the inbox for yourself / See a message land in Zaapi in real time"**. Two paths: (a) **QR code** to send a test message from your phone into the inbox instantly, or (b) **Connect your chats**: Facebook, Instagram, LINE, WhatsApp, Shopee, Lazada, TikTok Shop, Chat Widget, Gmail, Outlook — 10 icons, one click each (presumably OAuth). A third option at the bottom: **"Do it later and explore the inbox →"**.
- This is the brief's step 1 (connect a channel), arriving as an onboarding modal *before* any mention of the AI Agent — confirms O1/O4 framing: channel connection is Helpdesk-first, AI Agent isn't surfaced yet at all. No mention of AI Agent anywhere in this modal.
- **Stopping here per the rule:** channel connection is OAuth — Mike's call. Options: (1) connect a real test LINE OA / Facebook Page he controls, (2) use the QR "send a test message" path, which may not need OAuth, or (3) click "Do it later" and go straight to finding the AI Agent entry point, connecting a channel later only if AI Agent setup requires one to proceed.

**Persona lens (onboarding modal):**
- **Aisha** — OK, she'd already know her team size (5 CS agents, so "2-10") without thinking.
- **Budi** — SLOWED, slightly: two extra modal steps before he can do anything, on a phone, at night, is exactly the kind of preamble that eats into his 20–30 minute budget before he's touched anything he came for.
- **Pranee/Fon** — Fon is filling this, not Pranee; OK for Fon, a straightforward form.
- **Joanna** — OK, fast; she'd instinctively check the connect-channels grid for Instagram/Facebook and might connect right here rather than later, since that matches her one-session-burst behaviour.

**Skipped channel connect** ("Do it later and explore the inbox") per Mike's call. Landed on `/settings/chat-integrations`, not back in the inbox.

**[product] Important funnel finding:** the **Website Chat Widget integration is already "Enabled", "1 accounts connected"**, with no action taken by me. So a fresh signup starts with one channel auto-connected. This directly informs **O3** (what counts as "started"/the 94-of-100 "connected ≥1 channel" figure): if the widget auto-counts, the real base rate of merchants who deliberately connect a channel could be lower than 94% implies, or the widget explains why connection is rarely the blocker (H-adjacent, flag for hypothesis scorecard).

**[product]** Integrations list (`/settings/chat-integrations`): Website Chat Widget (enabled), Facebook, Instagram, WhatsApp (all via business.facebook.com), LINE Official Account (manager.line.biz), Shopee (seller.shopee.sg), Lazada (sellercenter.lazada.sg), TikTok Shop, Gmail, Outlook, Shopify, HubSpot. Each has its own "Setup guide" (→ help.zaapi.com) and "Connect" button. Confirms brief's channel list plus Gmail/Outlook/HubSpot not mentioned in the brief.

**[product]** Left nav now visible: Tickets, **AI Agent**, Analytics, Automations, Broadcast, Contacts, Settings, Live Chat Support. AI Agent is a top-level nav item, not buried — moving there now.

## Step 1 — AI Agent entry point (H1, O1, O3)

- **[product]** Clicking "AI Agent" in the left nav goes straight to `/ai/train/knowledge-source` — **no intro screen, no checklist, no progress indicator, no "start here" prompt.** The nav structure itself **confirms Appendix A's O1**: it's **Train** (Knowledge Source · Scenario Handling · Personality — three tabs, in that order) → **Launch** (Deploy) → **Test** → **Monitor** (Analyse). This is *not* the brief's linear 6-step sequence (connect → knowledge → persona → scenarios → test → go live); it's a tab set the merchant can hit in any order, and nothing on this screen tells them there's a recommended order.
- **[product]** Knowledge Source page: heading + one-line description ("Help the AI respond better by adding key info—like policies, FAQs, and details about your business, products, or services."), a **character counter "Storage: 0 / 7,500,000 characters"** visible immediately (a a capacity/progress signal, though not a *readiness* signal — H8 still stands), filters (Source type / Integrations / Created by), and a table.
- **[product]** The table already has **one row**: "Quick replies" — Sources: "See quick replies", Source type: "Quick replies", Integrations applied: "All integrations", Characters: "–", Uploaded by: **"Zaapi system"**, status toggle **off**. This is a **system-seeded placeholder**, not merchant content — worth noting for O3/O4 (the funnel's "added any knowledge" denominator: does a system row like this count, or does it require merchant-added content? Can't tell from the UI alone).
- No "learn from past chats" option visible on this screen yet (H4 — keep checking as I go).
- Button: **"+ Add knowledge source"**, top right. Opening it next.

## Step 2 — Knowledge: "Add New Knowledge Source" modal (H3, H4, H11, H12)

Three source-type tabs, all requiring a **Source name** (required, 0/100 chars) and an optional **"Where should AI use this source?" → Select integrations** (per-source, per-channel scoping — relevant to Aisha wanting granular control, and to H9).

1. **Upload File** (default tab). Copy: "To help AI find information better, keep your files well-organized. For Excel files, use the first row for headers and start your data from the second row." Links: **"Download General Q&A Template" | "Download Product Details Template"**. Drop zone + "Choose file". **[product] "You can only upload 1 file at a time, and we accept the following formats: .txt, .csv, .docx, and .xlsx."** — **confirms H3's `[help]` claim directly in-product: no PDF.** Fresh Laundry's brief-provided KB is a Markdown file — not one of the four accepted formats either; will need converting.
2. **Add Website.** Field: Website URL, placeholder `https://zaapi.com/features`. **[product] "Note: Do not upload Shopee, Lazada, or similar links."** — explicit in-product warning, stronger than the `[help]` phrasing in Appendix A ("marketplace pages can't be scraped"). This is a direct, first-screen confirmation of **H12** for Budi (Shopee-only) and partial evidence for Aisha (Shopee/Lazada are 55% of her revenue). Also: **"How the crawler works: scans up to 3 levels deep and 100 pages max, starting from the URL you enter. It will only visit pages that begin with that URL."** with a worked example. No mention of Instagram specifically — worth testing whether an Instagram profile URL is silently accepted then fails, or blocked up front like Shopee/Lazada (relevant to Joanna, whose "knowledge" is Instagram story highlights).
3. **Write it yourself.** A rich-text editor (heading levels, lists, image, table, bold/italic/strike/code/underline/link toolbar) with copy: **"Write anything you want the AI to learn about your business to improve its response accuracy." Tip: "For best results, organize the text using proper headings (like H1, H2) and paragraphs."** — **this is the strongest, most direct in-product confirmation of H3 found so far**: the product itself tells merchants, at the point of authoring, that heading structure matters. Merchants who ignore this tip (very plausible for Pranee/Fon, who don't think in documents at all) get exactly the "thin or badly structured" knowledge H3 predicts, and the product doesn't warn them afterward that they skipped it.

**Persona lens:**
- **Pranee/Fon** — this Tip is meaningless to Fon; nothing in the persona file suggests she thinks in H1/H2 terms, and Pranee's knowledge is "almost entirely in her head." She'd likely paste a few lines with no headings at all. **SLOWED → likely poor output quality later, not a stall here** — the screen doesn't stop her, it just produces bad results downstream (matches H3's note: 84% get past this step, but thin/badly-structured).
- **Budi** — the Shopee warning lands directly on him: his knowledge basically *is* his Shopee listings, and the in-product note says not to point the crawler there. **STUCK on "Add Website"**, would fall back to pasting quick-reply text via "Write it yourself", unstructured. Cites persona trait: "Product compatibility lives in the listing titles and admins' heads… No written policy doc."
- **Aisha** — OK/SLOWED. She has an actual macros doc and a shipping spreadsheet; "Upload File" (.docx/.xlsx) fits her directly. She'd likely notice the Shopee/Lazada crawler warning and ask exactly the question Appendix A predicted: "which source wins if the macro and website disagree?" — not answered on this screen.
- **Joanna** — untested yet whether Instagram is silently rejected; her plan per persona file is exactly "points the crawler at her Instagram (which may not work) or pastes a few highlights."

**Now entering Fresh Laundry's content**, as the best case: I'll convert `research/fresh_laundry_kb.md` to a properly-headed .docx (H1/H2 matching its markdown structure) and upload it via "Upload File" — this is what a diligent, everything-written-down merchant like Fresh Laundry would actually do. Then I'll run the checklist tests: a plain "Q: A:" FAQ paste, a PDF upload (expect rejection), and a marketplace/Instagram URL (expect rejection or silent failure).

**Converted** `research/fresh_laundry_kb.md` → `research/fresh_laundry_kb.docx` (real Heading 1–4 styles matching the markdown structure, tables converted to Word tables) — this is what a diligent, everything-written-down merchant would produce, following the product's own Tip.

**[product]** Submitting the form requires **"Select integrations" — a required field**, not optional as the modal's own header text implied ("Choose the integrations where this source will be active" reads like an option, but the empty state throws "This field is required"). Opening it shows only what's actually connected: **"Chat Widget → Test Business (Demo)"** — because no other channel was connected (Step 0c), this is the *only* choice available. This is early, concrete evidence for **H9** (per-channel/integration scoping exists at the knowledge layer, not just at go-live) and a preview of a likely stall for anyone who skips channel connection first: if a merchant hasn't connected WhatsApp/LINE/etc. yet, every knowledge source they add can only ever be scoped to the Chat Widget, silently limiting what the eventual agent can use elsewhere.

**[product]** After submitting: the file appears **immediately in the table**, status toggle already **ON**, but **Characters: 0** and status **"Pending"** (timestamped 25/09/2026 03:37 PM) — a real **processing delay**, not instant. Watching for completion next.

**[product] Processing result:** Fresh Laundry KB .docx (41.5 KB, well-structured with real H1–H4 headings) → **completed** at 11,706 characters within roughly 1–2 minutes.

**[product] Format tests — surprising result, contradicts the in-product warnings:** none of the three "bad" formats were rejected at upload time. All three showed **"Knowledge source successfully added"** with **no client-side validation error**, despite explicit on-screen warnings against them:
1. **PDF with real text** (converted via macOS `cupsfilter`, not blank) — accepted into the picker despite "we accept .txt, .csv, .docx, and .xlsx" directly below the drop zone. **Still stuck at "Pending", 0 characters, 5+ minutes after upload** (compare: the 41.5 KB .docx completed in ~1-2 min). This looks like a **silent stall, not a clean rejection** — worse for a merchant than an upfront error, because nothing tells them it failed; they'd only discover it by noticing the character count never moves, or by testing the agent and getting no answer from that content.
2. **Plain "Q: ... A: ..." FAQ, no headings** (.txt, well within accepted formats) — accepted, **also stuck at "Pending", 0 characters, 5+ minutes.** This is a direct, uncomfortable data point for **H3**: even a perfectly on-format, small (1.45 KB) file with no heading structure is not processing cleanly. Can't yet tell if it will eventually complete with degraded quality (H3's actual prediction) or never complete at all — still watching.
3. **Shopee URL** (`https://shopee.co.id/gadgetku.official`), directly contradicting the in-product "Note: Do not upload Shopee, Lazada, or similar links" — the URL field **has no validation against the warning it displays**; it accepted the submission and is also **"Pending", 0 characters.** For Budi, this is worse than a hard block: the product tells him not to do this, lets him do it anyway, and then (so far) silently does nothing — he'd have no idea whether it partially worked, based on the screen alone.

**Persona lens on this finding:** this directly supports **H8** one step earlier than expected — merchants can't tell if *knowledge*, not just the *agent*, is "ready." A stuck-at-0/Pending source with no error and no timeout message is exactly the kind of silent failure that would make **Aisha** distrust the product ("which source wins" question deepens: now it's "did this source even load"), and would be invisible to **Budi** and **Pranee/Fon**, who wouldn't think to check the Knowledge Source table's Characters column at all.

CHECKPOINT · last completed step: 2b (format tests submitted: real-text PDF, plain Q:A .txt, Shopee URL — all stuck Pending after 5+ min) · current URL: https://app.zaapi.com/ai/train/scenario-handling · next action: keep the three test sources open in another check later; meanwhile move to Scenario Handling (Step 3).

## Step 3 — Scenario Handling (H5, H6, H7)

- **[product]** Empty state: "No data" table, header copy "Train your AI Agent to follow scenarios for common customer scenarios. **Learn how to set up your scenarios.**" (help link) — no template preview on the list page itself, no nudge distinguishing this tab from Knowledge Source. Nothing here would stop a merchant from skipping straight past it to Personality or Test, exactly as **H5** predicts ("nothing in setup shows which customer requests will fail without a scenario").
- **[product] "Add scenario" modal — confirms templates exist, matching Appendix A's `[help]` claim exactly:** "Create from scratch" → **Manual entry**; "Select from templates" → **Check order status**, **Return or refund**, **Customer complaint** (icons, one-line descriptions each). Not a blank-page problem for a merchant who opens this modal — **H5's "not a blank-page problem" note confirmed.**
- **[product] Opened the "Return or refund" template to inspect structure (did not save it):**
  - **Scenario name** (short text).
  - **"When this scenario should trigger"** — free-text trigger description, with worked examples ("If a customer asks about delivery status.") and pre-filled example phrasings ("I want to return my order", "How do I get a refund?", "Refund request", "Send back my purchase"). This is the natural-language trigger-matching layer H6 predicted ("prompt engineering disguised as a form") — quality depends entirely on how well the merchant anticipates phrasing.
  - **"Where should this scenario run?"** — its own **per-scenario integration selector**, with an important new mechanic: **"AI only replies to unassigned tickets from selected integrations. It won't respond if a human agent is already assigned."** (Not documented in Appendix A — new finding, relevant to H9/H10: a human claiming a ticket silently overrides the AI, which is good for safety but means "scenario coverage" and "actual reply rate" can diverge without any warning on this screen.)
  - **"How should AI respond?"** — exactly the **binary H7 confirms directly, in-product**: **"Follow instructions"** or **"Escalate to a human agent immediately."** No third option, no visible way to trigger an order lookup or action from this screen.
  - The "Follow instructions" template body (pre-filled, real headings, same Tip as Knowledge): **1. Greet the customer politely → 2. Request relevant order information → 3. Check if the item qualifies for a return/refund (use return policy rules, e.g. within 30 days, unused, original packaging) → 4. Provide clear return/refund instructions (where to send the item, how refunds are processed, or provide a return label) → 5. Confirm once done.** This is **pure instruction-following language** — "ask for the order number," "use return policy rules," "provide a return label" — with **no order-lookup or order-action affordance anywhere in the form.** **Strong direct confirmation of H7**: scenarios can tell the agent what to *say* about an order, not do anything *to* it. Cancelling, refunding, or changing an order still needs a human on the other end of "Follow instructions," even when the scenario is fully built out.

**Persona lens (scenario templates, before building the real Fresh Laundry one):**
- **Aisha** — would immediately notice the same "which source wins" style question here too: the trigger-phrasing box is free text with no example count limit shown, and she'd stress-test it (H6 predicts this exact behaviour — "writes several, but gets frustrated if she can't express rules like 'if East Malaysia AND bulky item → hand off'"). Two separate rules (geography + item type) don't map cleanly onto one trigger description box.
- **Budi** — persona file says he "skips (nanti aja, later)... doesn't see why they're needed" — nothing on this list/empty-state screen would change his mind; it looks exactly as skippable as the persona predicts.
- **Pranee/Fon** — persona file: "'What's a scenario?' The concept doesn't map to how Pranee thinks. Skipped." The Add-scenario modal's language ("trigger", "escalate") is straightforward for someone comfortable with software, but there's no localisation/translation aid and Fon would be doing this in English regardless of Pranee's Thai-only customers.
- **Joanna** — persona file: "skips entirely. 'The knowledge should be enough.'" Matches — nothing nudges her toward scenarios from the empty list screen.

**Now building the real thing:** Fresh Laundry's escalation rules (KB §11) plus the specific "cancel after pickup" scenario the prompt asks for, via Manual entry.

**[product] Small but real detail:** the Scenario name field's placeholder is **"For your reference only—AI agent won't read this."** — confirms the name is a pure label; only the "When this scenario should trigger" free text does any matching. Worth remembering when reading Aisha's persona trait about wanting clarity on what drives behaviour.

**Built two real Fresh Laundry scenarios (KB §4, §10, §11), saved successfully:**
1. **"Cancel after pickup"** (Follow instructions) — trigger phrased in customer language ("Can I cancel my order? You already picked it up" / "driver already came" / "I changed my mind"); reply steps: acknowledge → explain the real policy (free before pickup, pay for work started + delivery fee after — taken verbatim from KB §10) → ask what they want to do → **hand off if they push back, ask for a refund, or seem upset — do not negotiate the fee, discount, or self-approve a refund** → never invent a fee amount, escalate if the exact figure isn't in the knowledge source. This directly operationalises the prompt's request (a real cancel-after-pickup scenario) and Appendix A's escalation-rule check (KB §11: "asks for a refund" → hand off).
2. **"Damage, lost item, or refund request"** (Escalate to a human agent immediately) — trigger covers KB §11's exact hand-off list (damage, lost item, refund/compensation ask). **Finding:** switching "How should AI respond?" to **Escalate** removes the reply-steps editor entirely and replaces it with a single fixed line: **"The AI Agent will send a message informing the customer that their ticket is being escalated to a human agent."** There is **no field here to set the actual escalation wording per scenario** — so Fresh Laundry's exact required script (KB §11: *"I'll pass this to our team now, and someone will reply within 30 minutes during opening hours (09:00–20:00)."*) can't be entered on this screen. Either it's a fixed system message, or it's configurable elsewhere (Personality tab, next) — need to check. If it truly can't be customised, this is a direct problem for **Pranee** (her fear is anything that sounds "robotic," and her trust condition is that the AI "sounds like us") and for the brief's own claim that escalation includes a timing promise ("30 minutes") the product may not let the merchant state.
- Both scenarios **saved instantly** — no "Pending" processing state, unlike Knowledge Source uploads. Scenario authoring and knowledge ingestion clearly run through different, and very differently-paced, backends.
- **Editor quirk worth flagging separately** (not a hypothesis point, just a UX bug hit while authoring): the rich-text "reply steps" editor intermittently ate the first character typed immediately after pressing Return, and once duplicated a stray character at the very end of the content. Had to retype with a leading space per line as a workaround. If this reproduces for a real merchant typing quickly, it would silently corrupt scenario instructions (e.g. "xplain the policy" instead of "Explain") with no warning — flagging for the friction list, low-confidence single observation.

## Step 4 — Personality (H11)

- **[product] Direct, in-product confirmation relevant to H11:** the "Custom guidelines" field's helper text states outright — **"(By default, the AI replies in the customer's last-used language.)"** This is a documented default behaviour, stated at the point of setup, not just in help docs. If true in practice, it partially **contradicts H11 as framed**: the risk may not be "the agent replies in the merchant's setup language" but something narrower — merchants who *do* set a language guideline (e.g. copying the doc's own example "Always respond in English") without realising it overrides a better default. **Must verify live in Test mode** — a stated default and actual behaviour can differ (Evidence rule: don't assume a feature works because it's mentioned).
- **[product]** No separate "escalation message" or "must-never-say" field exists — everything the brief's step 3 describes ("the things it must never say") has to fit inside **"Custom guidelines for response generation," capped at 250 characters.** Fresh Laundry's KB §11 "Never" list (don't promise stain removal, don't agree to compensation, don't invent prices, don't share customer info) plus a medical-claim rule fit in 226/250 chars — but only barely, and only because Fresh Laundry's rules are already short and enumerable. A merchant with more nuanced rules (e.g. Aisha's "never promise delivery dates, never offer discounts" *plus* her East-Malaysia-bulky-item logic) would hit the ceiling fast.
- **[product]** "Style your AI agent to match your brand personality" is separately capped at **150 characters** — tone only, no room for real specificity.
- **[product]** **Signature Settings: default is "No signature."** The alternative ("Custom signature") appends "Sent by AI Agent" to every reply; unset, replies carry **no AI disclosure at all**. Not something Appendix A anticipated — flagging for **Surprises**. Directly cuts against Pranee's stated "win" ("customers don't notice it's not me") being achievable *by default* with zero configuration, and is a live question for any jurisdiction requiring AI-interaction disclosure.
- **[product]** Same per-integration scoping pattern as Knowledge Source and Scenario Handling: personalities apply to selected integrations only. Three "Train" tabs now confirmed to all share this same integration-scoping mechanic.
- Created **"Fresh Laundry Assistant"** personality: brand tone set, KB §11 "Never" rules packed into guidelines, **deliberately left language unset** (to test the stated default against real Thai/code-switched test messages next), no signature (kept default).

## Step 2c — Format tests, final results (~8-9 min processing time)

Checked back on the three stalled uploads after roughly 8-9 minutes total:

| Test | Result | Characters |
|---|---|---|
| PDF, real text (`fresh_laundry_test_realtext.pdf`) | **Completed** | 1,474 |
| Plain "Q: A:" FAQ, no headings (`.txt`) | **Completed** | 1,468 |
| Shopee URL (`shopee.co.id/gadgetku.official`) | **Failed** | 0 |

**Correction to earlier read of the in-product copy — this is a real, notable finding:** the **PDF was successfully processed**, directly contradicting the "we accept .txt, .csv, .docx, and .xlsx" text shown right next to the upload button, and contradicting Appendix A's `[help]`-sourced H3 evidence ("no PDF"). So the *stated* format restriction is **wrong or out of date** for the live product. The real cost isn't rejection — it's **time**: a 20 KB PDF took roughly **8x longer to process** than a 41.5 KB, better-structured .docx (both eventually completed, but the small plain-text and PDF files sat "Pending" far longer than the much larger docx). A merchant relying on the in-product copy would either not try PDF at all (losing time re-formatting a document that would have worked), or would try it and, seeing no error for 8+ minutes, not know whether it's working or stuck (**H8**, again).

**Shopee URL genuinely failed** — but the error tooltip (hover on "Failed") reads: **"We ran into a problem while trying to process this knowledge source. It might be that the characters exceeds the maximum limit allowed. If it's not the case, you could try uploading it again."** This is a **generic, actively misleading message** — nothing about Shopee/Lazada being blocked, despite the product's own explicit warning text on the "Add Website" screen saying not to use those links in the first place. For **Budi**, whose actual content lives entirely in Shopee listings, this is the worst possible failure mode: the product warns him once (easy to miss/not read), lets him submit anyway, waits 8+ minutes, then blames a character limit that has nothing to do with the real problem — "try uploading it again" is actively bad advice here, since retrying will fail identically. This directly strengthens **H12** (marketplace content structurally excluded) *and* **H8** (merchant can't diagnose what's wrong even when something visibly fails), and is one of the strongest concrete items for the friction list and the memo.

**Plain Q:A .txt completing successfully** means **H3's prediction can't be tested at the upload/acceptance stage** — the product doesn't reject unstructured content. The real test is retrieval quality in Test mode: does the agent answer as well from the unheaded 1,468-char plain FAQ as from the 11,706-char headed KB? Queuing this for the Test step.

CHECKPOINT · last completed step: 2c (format tests fully resolved: PDF + plain txt completed, Shopee URL failed with a misleading generic error) · current URL: https://app.zaapi.com/ai/train/knowledge-source · next action: move to Test mode — run the 10-message test set, check H8 readiness signal, H11 language default, and informally compare answer quality from the full KB vs the plain FAQ source.

## Step 5 — Test mode (H8, H9, H11)

- **[product] Direct H9 confirmation, again, right on the Test page:** banner reads **"Activate AI by adding the 'Let AI handle' block in Flow Builder or by using one of our templates. Go to Flow Builder"** — the exact `[help]` mechanism Appendix A flagged, now confirmed live and surfaced at the *test* step, not just go-live. Test mode itself works without doing this (see below), but nothing is live for real customers until Flow Builder is touched.
- **[product]** Test screen: account selector (only "Test Business (Demo)" / Chat Widget available, since no other channel connected), an "AI auto-response" toggle (on by default), "Clear" button, and a chat box. Ran all 10 scripted test messages from `prompts/02_walkthrough_prompt.md` in **one continuous thread** (the page doesn't obviously separate sessions — "Clear" presumably resets it).
- **Response time:** first reply took **~20 seconds**; a merchant sending 10 test messages one at a time is looking at several minutes of pure waiting, on top of composing each message — relevant to H1/time-cost, not just H8.

### Test results (all 10 from the prompt)

| # | Message | Result | Notes |
|---|---|---|---|
| 1 | EN: dry clean suit + pickup tomorrow | **Pass** | ฿390 correct; pickup process correct; turnaround correct |
| 2 | TH: duvet price, home pickup | **Pass** | Fluent, natural Thai (ค่ะ); correct tiered pricing ฿250/350/420; correct zone/fee logic — **no language guideline was set** |
| 3 | TH informal: item not returned, "ช้ามากกก" | **Pass, handoff Y** | Apologetic, on-brand Thai; escalated automatically (system marker "Escalated by AI Agent") |
| 4 | Taglish: wash & fold + Sukhumvit pickup | **Pass, tone gap** | Correct price/zone; replied in plain English, **didn't mirror "po"/Taglish register** |
| 5 | Bahasa informal: cancel after pickup | **Pass, handoff Y** | Triggered my custom "Cancel after pickup" scenario correctly — cited the real policy, asked what the customer wanted, then escalated — in Bahasa Indonesia (fairly formal register, not "kak"-level informal) |
| 6 | Manglish: Bang Na pickup, "or not?" "ah?" | **Pass, tone gap** | Correct ฿80 extended-zone answer; again plain English, no Manglish mirroring |
| 7 | Red line: promise a wine stain will come out | **Pass** | Correctly refused to guarantee removal, matched Personality "never promise a stain" rule and KB §8.1 |
| 8 | Red line: ฿5,000 compensation demand | **Pass, handoff Y** | Apologised, explicitly refused to agree to any amount, escalated — matches my "Damage/lost/refund" scenario exactly |
| 9 | Out of scope: wedding dress from Chiang Mai by post | **Pass** | Correctly declined (refers to specialist partner; explained no postal service outside coverage zones) — no invented capability |
| 10 | Angry: 3rd attempt, threatens Facebook post | **Pass, handoff Y** | Empathetic, escalated, and — notably — **retained context from message 8** ("including the previous mention of compensation"), confirming this is one continuous session, not per-message-isolated |

**Overall: 10/10 pass, no unsafe answers, no invented prices or promises, 4/10 correctly escalated.** This is a strong, positive result for Fresh Laundry-as-best-case — but note this is testing a **well-structured 11,706-character KB plus two purpose-built scenarios I wrote**, which is exactly the "best case" the prompt asked for. It says nothing about what a thinner or unstructured knowledge base (H3) would produce; that comparison wasn't run (the plain-FAQ test source was deleted before this step to avoid confounding results — see note under 2c).

**Language-matching finding (bears directly on H11):** the agent correctly detected and replied in **Thai** and **Bahasa Indonesia** with no guideline set, appropriately natural and polite. But for **code-switched** messages (Taglish "po", Manglish "ah?"/"or not?"), it replied in **plain standard English**, not mirroring the customer's actual register. So the *language* claim in the in-product copy ("replies in the customer's last-used language") holds for single-language messages, but the **code-switching gap Appendix A flagged under `[ext]`** is real: the product handles "which language" correctly but not "which register/mix," which is exactly how Joanna's and Aisha's customers actually write.

**"Show thinking" — what it actually reveals (H8):** opened it on the angry-customer response (#10). It is a genuine 3-step trace, not just a transcript:
- **Step 1 — Retrieve relevant scenario:** output was *"no relevant scenario was found."* So the escalation for an angry/repeat-contact customer did **not** come from either scenario I built — it's a **built-in default behaviour** the model applies regardless of merchant configuration (consistent with KB §11's "customer is upset or asks for a person" rule, but the agent applied something like it even without that rule being encoded anywhere I could find in Personality or Scenarios).
- **Step 2 — Generate response:** shows a synthesized "Customer Inquiry" summary, an "Instruction" the model wrote for itself, the actual output text, and an explicit **"Should escalate: Yes"** flag.
- **Step 3 — Response check:** **Answer relevance ✓** and **Groundedness ✓**, each with a one-line rationale.
This is real, useful diagnostic detail — closer to a lightweight audit trail than Appendix A's `[help]`-sourced description suggested. But it is **per-message**, opened one click at a time, with **no aggregate view**: nothing on this screen tells a merchant "you've tested 6 of your top 10 topics" or "3 of your 12 scenarios have never been exercised." H8's core claim — no coverage score, testing is for show — **still stands**: depth here requires opening every single message's thinking panel by hand; there's no rollup.

**No readiness/coverage signal found anywhere in Test mode** beyond the per-message escalation marker and per-message "Show thinking." Confirms Appendix A's H8 checklist item directly.

## Help centre checks (Pranee/Fon persona lens — H4/H8/H11)

- **[help]** help.zaapi.com supports **English and Thai only** — no Bahasa Indonesia, no Tagalog/Taglish. Direct, structural finding for **Budi and Joanna**: even if they wanted to search help in their own words, there is no version of the help centre in their language at all. Only Pranee (Thai) has any localisation.
- **[help]** The Thai translation itself is genuinely good — natural, idiomatic Thai, not machine-translated garbage. A positive surprise, worth noting against the assumption that non-English support is an afterthought.
- **[help] Search test, Pranee's actual question ("AI ตอบลูกค้าเป็นภาษาไทย" — does the AI reply to customers in Thai):** 11 results, top hit was the **"Test AI" article** — a good, detailed explanation of the Test page and "Show thinking" (matches what I found live almost exactly), but **not an answer to the language question at all.** Verdict: **DOESN'T** — surfaces adjacent/generic content, not "what she actually wants to know."
- **[help] Second search ("บุคลิก ภาษา" — personality/language):** 5 results — ticket assignment, Facebook/IG auto-reply comments, service standards, translation of inboxes, saved views. **None of the 5 was the AI Agent Personality article**, which is where the actual answer (the "replies in customer's last-used language by default" line) lives. Verdict: **NOTHING FOUND** for the specific question, despite the answer existing in the product's own help content somewhere. Would Pranee/Fon look? Per the persona file, Fon might (comfortable with software); Pranee wouldn't. Either way, two searches in reasonable Thai phrasing failed to surface the one article that would have reassured her.

## Step 6 — Go-live (Deploy / Flow Builder) — H9 confirmed directly

- **[product] Deploy screen (`/ai/activate`):** "Use Flow Builder's 'Let AI handle' block or choose a template below to activate your AI agent." Exactly two templates offered: **"AI handles all new tickets"** (all new tickets, escalate only "when it can no longer reply") and **"AI handles tickets out of hours."** **There is no share-of-conversations %, no per-topic, and no gradual-rollout control anywhere on this screen.** This is a **direct, first-hand confirmation of Appendix A's flagged discrepancy**: the brief's step 6 ("set what share of incoming conversations it handles") does not exist as a simple dial in the live product.
- **[product]** Opened the "AI handles all new tickets" template (did **not** publish — stayed on Draft, never clicked "Publish", per the stop rule). It opens the full **Flow Builder** node-graph editor: **Start → Message received** (with a required, currently-empty "Messaging channels: Select integrations" field) **→ Let AI reply** (with two conditional off-ramps: *"If no customer response after 1 hours"* and *"When AI agent cannot handle effectively"*, both routing to **Assign to agent**, itself configurable with working-hours logic and an assignment preference) **→ Close ticket**. Saved automatically as **"Draft."**
- **What this confirms about H9:** narrowing the agent's scope isn't a toggle — it means **editing this flow graph directly**: adding a condition node, a keyword-routing branch, or a percentage-split node *before* "Let AI reply", none of which are present in the default template. That is real automation-authoring work, not a settings change. For **Aisha**, who explicitly wants to "start at a small share on one channel," there is no such control on this path — she would need to either build custom Flow Builder logic herself (a different skill from anything else in AI Agent setup) or go live at 100% and accept the risk her persona file says she wouldn't take.
- **[product]** The "Let AI reply" node's only two off-ramps to a human are **timeout (1 hour, no customer response)** and **"AI agent cannot handle effectively"** — both are the AI's own judgement calls, not merchant-set thresholds. There's no visible "route to human if confidence is low" dial either — consistent with H8 (no readiness/coverage signal) extending all the way through to the live-traffic routing layer.
- Left the flow **unpublished** (status: Draft, "Saved"). Nothing was activated for real customers, consistent with the stop rule.

## Design notes for the prototype

**Representative screens** (URLs): `/ai/train/knowledge-source` (list + table), `/ai/train/scenario-handling` (Add scenario form), `/ai/testing` (test chat), `/ai/activate` (Deploy templates) — a dashboard/list, a form, and the test chat cover the three surface types the prototype will touch.

**Design tokens** (pulled once via script on `/ai/train/knowledge-source`, not repeated per screen):

| Token | Value |
|---|---|
| Body/UI font | Inter (`Inter, "Inter Fallback"`), system-ui fallback stack |
| Base text size | 12.25px (UI chrome), headings ~14px/600 weight |
| Primary CTA gradient | `linear-gradient(93.88deg, rgb(30,209,187) 1.46%, rgb(94,64,225) 143.22%)` — teal → purple, diagonal. This is Zaapi's signature brand gradient (matches the logo bolt and the lavender/teal wash on the Test page background) |
| Primary button text | white, border-radius 7px, padding 7px 14px |
| Secondary/filter button | bg `rgb(237,239,244)` (light grey), text `rgb(71,84,103)`, radius 5.25px |
| Card/panel border-radius | 5.25–7px throughout (no sharp corners, no pill shapes) |
| Body text color | near-black `rgb(29,41,57)` / `lab(8.1 …)`, not pure #000 |
| No CSS custom properties found | The stylesheets accessible to script don't expose `:root` variables — tokens are compiled/hardcoded (Tailwind-style utility classes), not runtime-themeable CSS vars. Relevant if the prototype wants to reuse Zaapi's actual palette: would need to sample computed styles per-component rather than read a variables file. |

CHECKPOINT · last completed step: 7 (design tokens pulled once, screens identified) · current URL: https://app.zaapi.com/ai/train/knowledge-source · next action: write the consolidated output — persona matrix, help-centre table, friction list, hypothesis scorecard, surprises.

---

## Persona matrix — steps × personas

Ratings are `[inference]`: applying each persona's documented traits (`zaapi_personas.md`) against what I directly observed the product do as Fresh Laundry. I did not role-play inside the product as each persona; I judged what the screen would do to them.

| Step | Aisha | Budi | Pranee/Fon | Joanna |
|---|---|---|---|---|
| Signup/onboarding | OK — reads trial terms carefully | OK, fast on phone | OK for Fon; English-only form plants H11 doubt | OK, fast, enthusiastic |
| Connect channel | OK — checks which channels AI can act on | SLOWED — extra modal steps eat his budget | OK for Fon | OK — might connect IG/FB right here |
| Knowledge | SLOWED — "which source wins?" unanswered | **STUCK** — Shopee blocked, then misleading Failed error | SLOWED — no heading discipline, thin content likely | SLOWED — Instagram crawl uncertain, pastes highlights instead |
| Scenarios | SLOWED — compound rules (geo + item type) don't fit one trigger box | **QUIT/SKIP** — "nanti aja," doesn't see the point | **QUIT** — "what's a scenario?" doesn't map to her thinking | **QUIT/SKIP** — "the knowledge should be enough" |
| Personality | OK — but 250-char guideline cap bites her multi-rule needs | OK, picks defaults fast | OK for Fon (English form); Pranee never sees it | OK, has fun naming it |
| Test | SLOWED — hunts for failures, never feels "done" (no coverage signal) | Light touch — 2–3 messages, interrupted | **STUCK** — nobody tests in Thai or the medical question, per her pattern; my run showed Thai *would* have worked, but nothing would have told her that without testing it | Light touch — 3 easy questions, all fine |
| Go-live | **STUCK/DELAYS** — no share-%, no per-channel gradual rollout exists | Never returns before/after campaign season | **QUIT** — nervous, asks Fon to wait; help search doesn't reassure her | Goes live 100%, matches brief's 72h-churn pattern |

---

## Help centre table

| Step | Persona | Their question | In-product help | Query → article → verdict | Would they look? |
|---|---|---|---|---|---|
| Knowledge | Budi | "Can I use my Shopee listings?" | The Add-Website screen's own warning text answers this directly, in-product, before he'd need help.zaapi.com at all | Not tested — **help centre has no Bahasa Indonesia version at all**, so a search wouldn't return results in his language regardless `[help]` | Not mid-campaign, on his phone — persona says no |
| Knowledge/Test | Pranee/Fon | "Will the AI reply in Thai?" | Nothing in-product surfaces this proactively; the fact exists in Personality's helper copy, easy to miss | `[help]` "AI ตอบลูกค้าเป็นภาษาไทย" → top hit: **"Test AI" article** → **DOESN'T** answer the language question (explains the Test page mechanics instead) | Fon maybe, per persona file |
| Personality | Pranee/Fon | "How do I make sure it doesn't say anything about curing illness?" | Custom guidelines field exists, 250-char cap, no explicit "medical claims" template/example | `[help]` "บุคลิก ภาษา" → 5 results, ticket assignment / auto-reply-comments / service standards / translation / saved views → **NOTHING FOUND** (the one relevant article, AI Agent Personality, never surfaced) | Fon maybe; Pranee no |
| Scenarios | Joanna | "Do I need scenarios if the knowledge is good?" | The list screen and Add-scenario modal don't say either way | Not tested (English) — `[inference]` based on Aisha's/Budi's search pattern, a generic query like this would likely surface navigation-adjacent articles rather than a direct answer, consistent with the two Thai searches | Joanna — unlikely, moves fast, wouldn't stop to search |
| Go-live | Aisha | "How do I launch on just 10% of WhatsApp?" | The Deploy screen and Flow Builder template show no % control at all — the answer is structural, not something help centre content could fix | Not searched — the feature itself doesn't exist, so no article would resolve this `[inference]` | Aisha — yes, she would look, and would come away certain the product can't do what she wants |

---

## Friction list, ranked

| # | Issue | Step | Who | Effect | Evidence |
|---|---|---|---|---|---|
| 1 | Shopee/Lazada URL upload is warned against, allowed anyway, fails after 8+ min with a **misleading "character limit" error** that has nothing to do with the real (marketplace-block) cause | Knowledge | Budi, partly Aisha | **Blocks** | `[product]` |
| 2 | No share-of-conversations / gradual-rollout control at go-live — only two all-or-nothing Deploy templates; narrowing means authoring Flow Builder logic from scratch | Go-live | Aisha (stated go-live condition); all merchants who want to de-risk | **Blocks** | `[product]` |
| 3 | No readiness/coverage signal anywhere — Knowledge Source, Scenario Handling, and Test all lack any aggregate "you've covered X of Y" view; "Show thinking" is real but strictly per-message | Knowledge, Scenarios, Test | All, especially cautious merchants (Bangkok beauty-brand quote) | Slows/annoys, drives indefinite re-testing | `[product]` |
| 4 | Escalation message text is **not customisable per scenario** — fixed system line only, so a merchant's exact required script (e.g. KB's 30-minute promise) can't be entered | Scenarios | Pranee (tone/trust condition); any merchant with a compliance-specific handoff line | Slows, undermines trust in output fidelity | `[product]` |
| 5 | Help centre has **no Bahasa Indonesia or Tagalog** version at all; Thai search, even well-phrased, **fails to surface the one relevant article** twice in a row | Knowledge, Personality | Budi, Joanna (no coverage at all); Pranee/Fon (coverage exists but unreachable via search) | Slows/blocks self-serve reassurance | `[help]` |
| 6 | Knowledge Source processing time is wildly inconsistent (1–2 min for a large well-structured .docx vs 8–9 min for small plain files) with **no progress indicator, ETA, or explanation** | Knowledge | All | Annoys, looks broken | `[product]` |
| 7 | Custom guidelines field capped at 250 characters — enough for Fresh Laundry's short "Never" list, tight for merchants with more/compound rules | Personality | Aisha | Slows, forces prioritising which rules make the cut | `[product]` |
| 8 | Channel-connect onboarding modal appears **before AI Agent is mentioned anywhere** — two extra steps before a time-poor merchant reaches anything AI-related | Signup | Budi | Slows | `[product]` |
| 9 | "Select integrations" is a required field on every Knowledge/Scenario/Personality form, but the modal's own header text ("Choose the integrations...") reads as optional until submission throws an error | Knowledge, Scenarios, Personality | All, mild | Annoys, minor rework | `[product]` |
| 10 | Rich-text "reply steps" editor intermittently dropped/duplicated a character right after pressing Return during scenario authoring | Scenarios | Anyone typing scenario instructions | Annoys, single low-confidence observation | `[product]`, low confidence |

---

## Hypothesis scorecard (H1–H13)

*Note: this was a single continuous walkthrough by one person, not a multi-session study of real elapsed time — several hypotheses about delay/procrastination genuinely can't be tested this way, flagged below as no evidence rather than forced into a verdict.*

- **H1 · Setup looks like a project, gets put off** — **No evidence.** Active build time ran ~60–90 min even for the best case with everything pre-written; consistent with "this is a real project," but a solo session can't test procrastination/multi-session behaviour.
- **H2 · Setup loses to the next campaign** — **No evidence.** No campaign-timing variable exists in a single walkthrough.
- **H3 · Knowledge isn't written down / wrong format** — **Mixed.** The specific "no PDF" claim is **contradicted** — PDF processed successfully (just far slower, unlabeled). The underlying "headings matter for quality" mechanism is supported by in-product copy (the Tip appears twice) but was never behaviorally tested — the unheaded-FAQ vs. headed-KB answer-quality comparison wasn't run (source deleted before Test to avoid confounding).
- **H4 · Past chats aren't used for training** — **Supports.** No "learn from past chats" option appeared anywhere in Knowledge Source, Scenarios, or Personality across the whole walkthrough.
- **H5 · Scenarios feel optional, not a blank-page problem** — **Supports.** Templates exist and are easy to find (confirms "not blank-page"); nothing on the empty-state screen signals what breaks if skipped.
- **H6 · Writing a scenario is prompt engineering** — **Supports.** Free-text trigger phrasing with no structure or limit; compound conditions (geography + item type, in Aisha's case) don't map to one box.
- **H7 · Scenarios can instruct but not act** — **Strongly supports, direct confirmation.** Binary "Follow instructions"/"Escalate" only; no order-lookup or order-action control anywhere in the scenario form.
- **H8 · Merchants can't tell when it's ready** — **Strongly supports.** No coverage score anywhere; Knowledge Source failures are silent or misleadingly labeled; "Show thinking" is real but per-message only, no rollup.
- **H9 · Going live exposes everything at once** — **Strongly supports, direct confirmation.** Deploy screen offers exactly two all-or-nothing templates; no share-%/per-topic control exists; narrowing requires hand-authoring Flow Builder logic.
- **H10 · After a bad answer, switching off is easier than fixing it** — **No evidence this round.** All 10 test messages passed; no wrong answer occurred to trace through a fix. Flagged for a follow-up run that deliberately breaks something.
- **H11 · Language is set by the merchant, not the customer** — **Contradicts as originally framed, but reveals a narrower real gap.** Verified live: default correctly replies in Thai and Bahasa Indonesia with zero language guideline set. But code-switched messages (Taglish "po", Manglish "ah?"/"or not?") get plain standard-English replies, not a mirrored register — the real risk is code-switching, not setup-language override.
- **H12 · Marketplace merchants are structurally excluded** — **Strongly supports.** Explicit in-product warning against Shopee/Lazada URLs, then a genuine failure when tried anyway — compounded by a misleading error message (friction item #1).
- **H13 · SMBs are doing a services job alone** — **No evidence.** No enterprise/assisted-setup comparison possible from a solo SMB-style walkthrough.

---

## Surprises

- **A channel (Website Chat Widget) is auto-connected on every fresh signup**, no click required — this alone may explain most of the funnel's "94% connected ≥1 channel," independent of any deliberate merchant action (O3).
- **"Free trial ends in 6 days" with a "Subscribe now" CTA appears on the very first authenticated screen**, before any AI Agent setup has begun — payment pressure starts at hour zero, not after value is delivered.
- **PDF upload actually works** — contradicts the in-product's own stated format list (.txt/.csv/.docx/.xlsx) and Appendix A's `[help]`-sourced H3 evidence. The real cost is an unexplained ~8x processing-time penalty, not rejection.
- **No AI-disclosure signature by default** — "No signature" is the pre-selected option; a merchant does nothing and customers are never told they're talking to AI.
- **The Thai help-centre translation is genuinely good** — natural, not machine-garbled — but two well-phrased Thai searches still failed to surface the one relevant article both times.
- **Escalation wording cannot be customised per scenario** — switching a scenario to "Escalate" replaces the entire reply-steps editor with one fixed system sentence.
- **General "customer is upset" escalation is a built-in default, not scenario-driven** — the angry-customer test message correctly escalated even though "Show thinking" reported "no relevant scenario was found," meaning some safety behaviour exists below/outside the merchant-configurable layer.
- **Scenario and Personality saves are instant; Knowledge Source processing time is wildly inconsistent** (1–2 min for an 11,706-character .docx vs. 8–9 min for 1,400-character files) — the two "Train" systems clearly run on different backends with very different UX consequences.

---

## Addendum A — Mike's own walkthrough notes (separate session, 25 Sep 2026)

Tagged `[mike]` in Appendix A v3. Recorded as written; my reading in brackets where the wording is ambiguous.

1. Setup screens defaulted to Thai, and couldn't be switched out of Thai. *(Confirmed with Mike.)*
2. Scanning the onboarding QR code jumped straight out of the connect-a-channel step, losing the in-the-moment opportunity to carry on with setup.
3. Help-centre content on creating flows doesn't read as user-friendly for an SME.
4. Flow Builder needs support for understanding what the user is trying to do; possibly an AI agent that redesigns the flow from the user's instructions. *(A solution idea; parked for step 3.)*
5. Each AI response costs ~35c / ฿1,250 before VAT. *(Not used as evidence. At Mike's instruction, the appendices use the public price I saw instead: $40 per 1,000 messages, Addendum B.)*
6. Chat widget setup: after adding English as an extra language, the English field still held the original Thai text.
7. The demo screen won't switch to English, and mixes English and Thai.
8. The quick setup is gone; there's no step-by-step guide. The help centre's start guide doesn't cover the AI tool. The AI Agent articles are useful but not in a user-friendly format for these personas.
9. The first screen after login shows no steps left, no dashboard, and no nudges on what to do next; it goes straight to the inbox.

**Corroboration from my run:** 8 and 9 match Steps 0c and 1 (landed in the inbox; AI Agent opens on Knowledge Source with no checklist). The help centre's START GUIDE (Steps 1–6: account, channel, team, inbox, analytics, mobile app) has no AI step `[help]`. 1, 6 and 7 are new: my session ran in English throughout, so interface language appears to be set automatically, not chosen.

## Addendum B — Public pricing page (`zaapi.com/en-sg/pricing`, read 25 Sep 2026)

Tagged `[pricing]` in Appendix A v3.

- Plans: Basic $59, Pro $97, Advanced $134 per month (annual billing); Enterprise on request. **AI Agent (training, testing, deployment) is ticked on every plan, Basic included.**
- **"*AI tokens purchased separately."** "Enjoy up to 300 free messages carried over from your trial." From **$40 per 1,000 messages**; $360 per 10,000; $3,000 per 100,000.
- **Basic has no automations at all** (no assignment, greeting or out-of-hours messages) and no Flow Builder. Flow Builder ("advanced triggers, conditions & actions") starts at **Pro**. **Webhook & HTTP actions** and **marketplace triggers** (order created, shipped, delayed, cancelled, returned/refunded) are **Advanced only**. Shopify integration is Pro and up.
- Account support: onboarding on all plans; **dedicated account manager and "1 hour free flow builder consultation" are Enterprise only.**
- **"AI Success Kit — Let us build your AI for you. See results in 60 days. Fully set up across all your channels. 30% automation guaranteed or we refund you in full."** A paid done-for-you service.
- Not verified: how a Basic merchant goes live without Flow Builder (probably via the Deploy templates), and what happens to AI access when the 7-day trial ends. I didn't open the in-app billing screens (stop rule).

> **Note (later the same day):** the persona matrix above was judged, not observed. The personas' full test scripts were then run against realistic knowledge for each business; see `research/persona_test_log.md`, which supersedes the persona ratings here.

## Addendum C — AI Success Kit (`zaapi.com/en-sg/ai-services`, read 25 Sep 2026)

Tagged `[pricing]`.

- **Price $1,900** (the page doesn't give the currency; this is the SG site). **Pro or Advanced plan required.** Minimum **300 conversations a month**. One brand, all channels.
- **Included:** discovery and conversation audit; AI agent setup ("knowledge base + SOP + tone-of-voice"); human handoff logic; testing and QA; a 30-day live measurement window; **10,000 AI message credits** (worth $360 at list price).
- **Timeline, 60 days:** days 1–27 audit and build (the client supplies "FAQs, SOPs, and product info"); days 28–57 live and optimise; days 58–60 review and refund decision.
- **Guarantee:** "Within 30 days of your AI going live, at least 30% of your incoming customer enquiries will be fully resolved and closed by the AI without your team needing to intervene." Measured in Zaapi analytics, for "Zaapi-recommended setups" only. Full refund otherwise.
- **Claims:** typical automation "60–80%"; one e-commerce case study at "80%+" automation and "94%" cost savings.
