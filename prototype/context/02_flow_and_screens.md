# Flow and screens

## App shell (copy the real app)

- **Left nav rail** (72px, labels under the seven sections, as in the Stitch designs; today's app is about 56px and icons only). Keep every item the real app has, so nothing looks removed. Checked in the trial account on 28 Sep 2026, top to bottom:
  - store switcher;
  - sidebar toggle (opens the AI Agent sub-menu: Train, Launch, Monitor);
  - Notifications;
  - Search;
  - Tickets;
  - AI Agent (active);
  - Analytics;
  - Automations;
  - Broadcast;
  - Contacts;
  - Settings;
  - Live Chat Support, pinned to the bottom.

  Only AI Agent is live; the others show a "Not part of this prototype" tooltip.
- **Top banner:** "Free trial ends in 6 days" with a dark "Subscribe now" button. Style it exactly as `design_system.md` describes (the upsell gradient). For Budi, it reads "Trial paused until 18 Nov (sale period)".
- **Top right: a demo control bar**, visibly separate from the app (e.g. a dashed outline, labelled "Demo controls"). It holds:
  - the merchant switcher: a dropdown ordered by impact score, each row showing name, city, quote snippet and impact score; Aisha's row carries the "Shows the most features" chip;
  - "Show notes" / "Hide notes" (controls the presenter sidebar);
  - "Reset this merchant".
- Root font size **14px** (see `design_system.md`); Inter, falling back to the system font.

## Setup home (the first screen after login)

This screen is the landing page until setup is done. Then it becomes the dashboard (see below).

- **Title:** "Set up your AI agent", with a subtitle naming the merchant and "about 25 minutes in total".
- **Progress:** "Step 3 of 7" and a bar.
- **Next step card:** big, with a primary gradient button, e.g. "Next: check what your agent knows · 10 min".
- **Sale banner** (from `03_merchants.md`), e.g. "11.11 is in 3 weeks. Add your vouchers and cut-offs so your agent gets them right." with an "Add sale info" button that opens a small form.
- **Plan card:** "Your free setup drafts your top 6 topics" (300+ merchants) or "Your free setup drafts everything" (under 300). It has a "What's in the AI Success Kit" link opening a side panel: the $1,900 done-for-you setup, 60 days, deeper topics, and the LINE history export for LINE merchants.
- **The 7-step tracker:** a vertical list. Each row shows the step name, a one-line description, time, status (Not started / In progress / Done / Needs attention) and an "Open" button. Steps can be opened in any order, but the next step card always points to the recommended one. A step is ticked **only when it's actually ready** (e.g. step 2 isn't done while a conflict is unresolved).

| # | Step (plain name) | Done when |
|---|---|---|
| 1 | Connect your chats | At least one channel customers use is connected (the website widget alone doesn't count), and past chats are shared or the guided questions are started |
| 2 | Check what your agent knows | Every file has been reviewed and every conflict resolved |
| 3 | Check what your agent does | Drafted topics accepted or edited |
| 4 | Choose how it sounds | Voice fields set; preview seen |
| 5 | See if it's ready | Readiness test run; no open "wrong" answers on the top topics |
| 6 | Go live small | Channel, hours and topics chosen; spend cap set |
| 7 | First week live | Reviewed the flagged answers |

**Mini tracker:** on every step screen, a compact bar at the top ("Step 3 of 7 · Next: choose how it sounds") with 7 dots. Clicking it returns to the setup home.

## Step screens

Use Zaapi's layout: page title at 21px/500, cards, and tables with the header styling from the design system. Anything AI-produced uses the **light AI gradient surface and gradient text**.

**Step 1: Connect your chats.**
- A grid of channel tiles for the channels in the merchant's data.
- The website widget tile shows "Connected automatically. Connect the channels your customers use."
- A consent toggle: "Let Zaapi read your past chats to draft your agent", with a line on what's read and that nothing is sent to customers.
- After "Connect", simulate: "Reading your chats…", then per channel the result from `03_merchants.md` (chats found, how far back, or the limitation).
- **LINE:** "LINE doesn't let us read chats from before you connected. We'll use the 12 days since you connected. Want more? The AI Success Kit includes a one-month LINE history export, which costs ฿555 a month on its own." (optional)
- **Order:** LINE first, WhatsApp second, then the merchant's own channels, then Gmail, then the website widget. LINE, WhatsApp and Gmail appear for every merchant (optional where they aren't that merchant's channel).
- **Tile copy:** a channel that isn't connected shows three short bullets: "Message customers through Zaapi", "We'll find your top topics for AI to handle", "Key facts go into your knowledge base".
- **LINE as an option for everyone:** merchants whose main channels are elsewhere still see a LINE tile, marked Optional, alongside the others. Its bullets state the limitation (chats only from the day you connect) and the cost of LINE's own export (฿555 a month). Under them, an upsell strip: "AI Success Kit includes one month of LINE history. Saves ฿555." with a See the Kit button. Opening the Kit from there shows a banner with the saving at the top of the panel. Connecting LINE adds 0 readable chats and doesn't change the tier.
- **WhatsApp:** a "Share your last 6 months of chats" checkbox, ticked, with "Found N chats".
- It ends with the **tier result**, e.g. "About 3,900 chats a month. Your free setup drafts your top 6 topics."
- **No-history case (Pranee):** "We'll ask you a few questions instead" leads into the guided interview (step 2 variant).

**Step 2: Check what your agent knows.**
- **Three ways to teach your agent**, shown as a row at the top for every merchant, with the one that applies highlighted: (1) Upload files: FAQs, price lists, shipping sheets, macros or a website link; (2) Answer a few questions: no files? We ask the 8 things customers ask most and pre-fill what we can (the live route for Pranee; a demo note for the others); (3) Let Zaapi draft it: a first attempt from the connected channels, with the plan limit stated (under 300 chats a month everything is drafted; over 300 the top topics, the Kit covers the rest; Pranee: LINE can't share history, so Facebook and Shopee plus questions).

- **Files list:** each file with a status pill and a **"What we read"** panel that expands to show the extracted facts, with a warning banner where something wasn't read (e.g. "Page 3: product table not read. 5 products, prices partly read, sizes and อย. numbers missing"). Each warning has a fix action: "Confirm these 5 products" (editable table) or "Upload as .docx".
- A drop zone, plus "Use sample files".
- **Conflicts:** a card per conflict. Resolving one has six parts:
  1. **The stakes:** both sources side by side, with last-updated dates, plus how many chats the conflict affects and what happened in testing.
  2. **Pick the answer:** "Use [source A]" (recommended, with the reason), "Use [source B]", "Write it yourself", or **"Ask a teammate"**. The last one assigns it to a named teammate: the card shows "Waiting for Farah", and in the demo it auto-confirms after about 3 seconds.
  3. **Fill the gap** if the chosen source is incomplete, e.g. a follow-up question with three options.
  4. **Which source wins next time:** a small ordered list ("When shipping sources disagree, trust: Shipping sheet → Website → Macros"). Plus a setting, on by default: "If sources still disagree when a customer asks, pass it to your team instead of guessing."
  5. **Fix it at the source:** "Your website still says RM15, so customers see it there too." A "Copy updated text" button shows the corrected wording and copies it to the clipboard.
  6. **Quick re-test:** re-run just the affected questions, 3 times each, with a short loader, then show the result (e.g. "18 of 18 correct or passed to your shipping team").

  The step isn't done until every conflict is resolved.
- **Facts vs rules vs live data:** show three chips on the extracted items ("Fact", "Rule", "Live data, never stated"), e.g. stock is "Live data".
- **Guided interview variant** (Pranee): about 8 questions, one at a time, in Thai with an English toggle. Each answer adds a fact card.

**Step 3: Check what your agent does.**
- A table of drafted topics: topic, share of chats, drafted rule (in plain words), "Drafted from 14 of your replies", and Accept / Edit / Turn off.
- For 300+ merchants, below the drafted topics: **"More topics we found (not drafted in your free setup)"**, with share of chats and two buttons: "Build it yourself" (opens a blank topic editor with a hint) and "Have our team build these" (the AI Success Kit panel).
- Handoff routing on each topic: "Pass to: [team]".

**Step 4: Choose how it sounds.**
- Fields, not free text:
  - reply language ("Match the customer" as default, with the detected mix, e.g. "92% Thai");
  - "Your shop speaks as" (a woman / a man / neutral);
  - self-reference (e.g. Vietnamese "shop");
  - how it addresses customers;
  - tone (Friendly / Warm and expert / Formal);
  - emoji (None / A few / Lots).
- A **live preview** of a real customer question answered in the customer's language, updating as fields change.
- The reassurance line, e.g. "92% of your chats are in Thai. Your agent will reply in Thai."

**Step 5: See if it's ready (the core screen).**
- Start button, then a simulated run: "Replaying 120 real questions from your last 90 days, 3 times each…" with a progress bar and a ticker of questions (about 4–6 seconds).
- **The result:**
  - a big readiness score with a verdict ("Ready for a small launch" / "Fix 2 things first");
  - three bars: answered correctly / handed off correctly / wrong;
  - consistency ("Same answer on all 3 runs: 71%");
  - a by-topic table (topic, questions, correct, handed off, wrong);
  - a one-line explanation of the score.
- **Wrong answers list:** each shows the customer question, what the agent said, what it should say, the cause (e.g. "Your website and shipping sheet disagree"), and a **Fix** button that jumps to the right step or applies the fix inline.
- The self-check contrast: show the old "Groundedness ✓" beside "Wrong: stale rate" to make the point (Aisha).
- After fixes: "Re-run" shows the after numbers from `03_merchants.md`.
- Merchants with no history see: "Based on a standard set of supplement questions, plus 12 days of your chats. It'll get better after 30 days live."

**Step 6: Go live small.**
- A form:
  - channels (checkboxes);
  - hours (All day / Out of hours only / Custom);
  - topics the agent handles (toggles; defaults from the readiness result, with risky topics off);
  - "I approve replies first" (on by default for the first week);
  - a monthly spend cap (messages and cost at $40 per 1,000);
  - who gets each handoff;
  - "If the agent doesn't reply within 30 seconds, pass to a human" (on).
- A live summary: "Your agent will handle about 24% of chats: WhatsApp, out of hours, 5 topics. Everything else goes to your team."
- A "Go live" button.
- Small print: "No Flow Builder needed. Pro users can edit the flow later."

**Step 7: First week live.** Simulated stats:
- chats handled, resolved without a human, handoffs, and replies approved or edited;
- 2–3 flagged answers to review, each with "Fix";
- the reply check log (e.g. "Blocked 6 replies that promised to check an order; passed them to your team");
- reminders ("Shopee connection needs re-authorising in 11 months"; "212 of your 300 free messages used");
- a sale prompt.

## Dashboard (after setup)

Once all 7 steps are done, the home becomes "Your AI agent". It shows:
- live status per channel;
- this week's numbers;
- the review queue;
- the sale-period prompt;
- the remaining topics upsell;
- a small "Setup complete ✓", with a link back to the tracker.

## Presenter sidebar

A right-hand panel, "What's changed and why", on by default and collapsible. It explains each screen:
- **Today:** what happens now;
- **The change:** what's different;
- **Why:** the evidence, with its source;
- **Should move:** which measure should change;

plus the current merchant's line and a running tracker of the 10 changes shown. **Use the layout and text in `07_sidebar_copy.md` word for word.** The "Notes" lines in `03_merchants.md` are background for the README; the sidebar text in `07_sidebar_copy.md` takes priority. Leave room for the sidebar: the app content area shrinks, and must still not overflow at 1280px wide.

## Wording rules (plain names)

| Don't use | Use |
|---|---|
| Knowledge Source | What your agent knows |
| Scenario Handling | What your agent does / topics |
| Personality | How it sounds |
| Deploy / Let AI handle | Go live |
| Escalate | Pass to your team |
| Integrations | Your chat channels |
| Trigger | When a customer asks about… |
| Groundedness ✓ | Only in the step 5 contrast, labelled "Today's check" |
| Chunking, H1/H2 | Never shown |
