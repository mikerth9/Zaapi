# Sidebar copy: "What's changed and why"

**Use this text word for word.** It's written in Mike's voice and has been checked for AI-sounding language. If a screen needs a line that isn't here, write it in the same style and run the checks at the end of this file.

## Layout

- **Position:** a right-hand panel, about 300px wide, the full height under the trial banner.
- **Styling:** it must look like presenter notes, not part of Zaapi. Use a light grey background, a dashed left border, and the label "Presenter notes" in small caps at the top.
- **Behaviour:** on by default. A "Hide notes" button collapses it to a thin tab, and "Show notes" in the demo controls brings it back.
- **Content order, top to bottom:**
  1. **Title:** "What's changed and why".
  2. **Merchant chip:** name, city, and "Impact 7.6".
  3. **Four blocks** for the current screen, each with a small bold label:
     - **Today:** what happens now;
     - **The change:** what's different;
     - **Why:** the evidence, with its source in grey brackets;
     - **Should move:** which measure should change.
  4. **"In this demo":** the current merchant's line for this screen, if there is one.
  5. **Running tracker**, pinned to the bottom: "Changes shown: 4 of 10". It lists the 10 changes with a tick once the demo has visited the screen that shows each one. Ticks are kept per merchant; there's also a combined count across all merchants.

## The 10 changes (running tracker labels)

1. Setup home and tracker
2. Draft from past chats
3. What we read, and conflicts settled
4. Voice set with fields
5. Readiness score
6. Go live small, on every plan
7. Reply check (knows its limits)
8. Read-only order status
9. Stays live (reminders, review, alerts)
10. Sale periods

Which screen ticks which change: home → 1; step 1 → 2; step 2 → 3; step 3 → 2 (and 8 for Linh); step 4 → 4; step 5 → 5; step 6 → 6; step 7 → 7 and 9; the sale banner or campaign mode → 10.

---

## Per screen

### Setup home
- **Today:** New merchants land in the inbox. Nothing mentions the AI agent, and setup is a set of tabs with no order.
- **The change:** This setup home is the first screen after login. Seven steps, a clear next step, and a small tracker on every other screen. A step only ticks when that part is actually ready.
- **Why:** The median merchant waits 4 days before any setup step. 21 of 100 never add knowledge (brief).
- **Should move:** First AI step on day 0. Share of sign-ups live by day 7.

### Step 1: Connect your chats
- **Today:** Connecting a channel is part of inbox onboarding. A website widget comes connected already, and past chats are never used to set up the AI.
- **The change:** Merchants connect the channels their customers use and let Zaapi read their past chats. Zaapi says what it found and what the free setup covers.
- **Why:** Facebook, Instagram and the marketplaces already bring in 90 days of chats. WhatsApp offers 180 days, but Zaapi's guide tells merchants to decline it (Zaapi help, Meta docs).
- **Should move:** Share of merchants with a draft agent on day 0.
- **Extra line, every merchant:** LINE is offered alongside the other channels, but it can't share old chats through its API. LINE's own export costs ฿555 a month; the AI Success Kit includes one month of it.

### Step 2: Check what your agent knows
- **Today:** Merchants upload files and see "Completed". They can't see what was read, and nothing flags two sources that disagree.
- **The change:** Zaapi shows what it read from each file and warns about anything it missed. Conflicts get settled before the agent uses them.
- **Why:** A 12-page Thai PDF showed "Completed" with about half its text read. A stale RM15 rate went to East Malaysia customers in 3 of 6 test runs (our tests).
- **Should move:** Wrong-answer rate. Switch-offs within 72 hours.

### Step 2, while a conflict card is open
- **The change:** Four ways to settle it: pick the right source, ask a teammate, set which source wins next time, or fix it at the source. A quick re-test then shows it worked.
- **Why:** In testing, only a rule Aisha would have had to know to write stopped the RM15 answer. This finds the problem for her (our tests).

### Step 3: Check what your agent does
- **Today:** Scenarios start from a blank form, and nothing suggests which ones matter. Only 38 of 100 merchants write one (brief).
- **The change:** Zaapi drafts the main topics from the merchant's own replies and shows the share of chats each covers. Over 300 chats a month, the top topics are free. The rest are listed to build yourself or hand to the AI Success Kit.
- **Why:** Jo's cancel rule was in 14 of her own messages. Once it was written down, her agent went from 77 to 92 (our tests).
- **Should move:** Share of merchants with topics set up. Kit and plan upgrades.

### Step 4: Choose how it sounds
- **Today:** Voice is a 150-character style box and a 250-character rules box. Nothing tells the merchant which language the agent will reply in.
- **The change:** Voice is set with fields: language, how the shop speaks, how it addresses customers. There's a live preview and a plain statement of the reply language.
- **Why:** Thai replies slipped into male forms until a rule was added. A free-text Vietnamese rule held in 1 of 9 replies (our tests).
- **Should move:** Voice errors in the readiness test.

### Step 5: See if it's ready
- **Today:** Test mode takes one typed message at a time. There's no score, and the only check marked a wrong answer "Groundedness ✓".
- **The change:** A readiness score replays real past questions three times each. It shows what the agent answers, passes on or gets wrong, with a fix for each wrong answer.
- **Why:** The same question got different answers on different runs. The two careful merchants never launched because they couldn't tell if it was ready (our tests, Bangkok quote).
- **Should move:** Launch rate among merchants who test. Readiness score at launch.

### Step 6: Go live small
- **Today:** Going live means one of two templates inside Flow Builder, which isn't on the Basic plan. There's no way to limit topics, approve replies first or cap spend.
- **The change:** A go-live screen on every plan. Pick channels, hours and topics. Approve replies for the first week, set a spend cap, and choose who gets each handoff.
- **Why:** 9 of the 61 merchants who go live switch off, most within 72 hours (brief). Aisha wanted to start small.
- **Should move:** Switch-offs within 72 hours. Still live at day 30.

### Step 7: First week live
- **Today:** After launch there's no review of what the agent said. Shopee and Lazada connections expire after 12 and 6 months.
- **The change:** A first-week review with flagged answers. A reply check that turns "I'm checking" into a handoff. Reminders before connections expire, and an alert before the free messages run out.
- **Why:** In our tests the agent said "I'm checking" in four languages, and nobody was told to follow up.
- **Should move:** Still live at day 30. Share of chats the AI resolves.

### Dashboard (after setup)
- **The change:** Once setup is done, the home becomes the agent's dashboard, with the review queue and the next sale prompt.
- **Should move:** Still live at day 30.

### Sale banner and campaign mode
- **Today:** Merchants who sign up just before a big sale rarely finish setup, and nothing brings them back.
- **The change:** A 10-minute campaign setup before the sale, the trial clock paused, and a reminder to finish afterwards. Live merchants get a prompt 2–3 weeks before each sale to add vouchers and cut-offs.
- **Why:** Activation is materially worse for accounts that sign up during a campaign period (brief).
- **Should move:** Activation of sale-period sign-ups.

---

## "In this demo" lines, by merchant

**Jo (impact 9.0)**
- Home: Jo gets about 280 chats a month, so everything is drafted. That includes rules that were only in her head.
- Step 3: Watch the cancel rule. It's drafted from 14 of her own replies.

**Nattaya (impact 8.4)**
- Home: Nattaya never launched because she couldn't tell if her agent was ready.
- Step 2: Only 7 of her 12 pages were read. Today she'd see "Completed".
- Step 5: This screen answers her question directly.

**Aisha (impact 7.6, shows the most features)**
- Home: Aisha went live on a Friday and switched off on the Saturday. This run shows almost every change.
- Step 2: Three conflicts, including the RM15 rate behind her Saturday.
- Step 5: Today's check passes the wrong answer. The readiness score catches it.
- Step 6: East Malaysia shipping stays with her team until she's ready.

**Linh (impact 7.2)**
- Home: Linh's agent answered questions well but couldn't do anything with orders.
- Step 3: The cancel topic only works with order status, which Zaapi already syncs. Marked as projected.
- Step 7: The reply check stops "I'm checking your order" going out with nobody following up.

**Budi (impact 7.0)**
- Home: Budi signed up three days before 11.11. Campaign mode gets him live in 10 minutes and brings him back afterwards.
- Step 2: His canned "ready stok" line is flagged, so the agent won't claim stock.

**Pranee (impact 6.2)**
- Home: Most of Pranee's chats are on LINE, which can't share its history. Zaapi asks her a few questions instead.
- Step 4: It tells her plainly that 92% of her chats are in Thai, so the agent will reply in Thai.

---

## Quality checks (run these on any new or changed sidebar text)

The build session must run these on the final HTML and report the result.

1. **Banned words and phrases** (case-insensitive grep; there should be no matches in the sidebar text):
   - seamless, effortless, empower, unlock, leverage, robust, game-changer, supercharge, streamline, cutting-edge, revolutionise;
   - delve, holistic, synergy, elevate, harness, journey, landscape, "in today's";
   - "it's not just", "not only", "more than just", "whether you're";
   - em dashes (—). The one exception is verbatim brief quotes, e.g. Linh's.
2. **Structure:** no "It's not X, it's Y" lines, no rhetorical questions, no three-part slogans, no exclamation marks.
3. **Style:** British spelling (-ise, colour, catalogue), numbers as digits, and short sentences (roughly 20 words or fewer).
4. **Evidence:** every "Why" line names its source in brackets: (brief), (our tests), (Zaapi help), (pricing page) or (Meta docs).
