# Zaapi AI Agent setup: design brief for Google Stitch

This file is the single design reference for generating the new AI Agent setup screens in Google Stitch. Give Stitch sections 1–6 as context. Then generate the screens one at a time with the prompts in section 8.

The designs feed a working prototype (spec in `../context/`). If this file and the context pack disagree on content, the context pack wins. This file covers look, layout and interaction.

---

## 1. What we're designing

Zaapi is a Bangkok-based customer chat platform for Southeast Asian online sellers. It puts LINE, WhatsApp, Facebook, Instagram, Shopee, Lazada, TikTok Shop and Shopify chats into one inbox, and adds an AI agent that replies to customers.

Merchants take a median of 19 days to get the AI agent live, and 39% never do. We're redesigning setup around one idea:

> **Zaapi drafts the agent from what the merchant already has, and shows them whether it's ready before any customer sees it.**

The redesign is a guided setup with seven steps:

1. Connect your chats
2. Check what your agent knows
3. Check what your agent does
4. Choose how it sounds
5. See if it's ready
6. Go live small
7. First week live

A setup home tracks them. It is the first screen after login, and it becomes a dashboard once setup is done.

## 2. Who uses it

- Owners and operations leads of small and mid-sized online shops in Thailand, Malaysia, Indonesia, the Philippines and Vietnam. Most don't have English as a first language.
- They are busy: 20–40 minutes at a time, often between other work, and often right before a big sale (11.11, 12.12).
- They are not technical. Their knowledge is in their heads, in chat replies and in the odd document.
- The careful ones won't launch until they're sure it's right. The fast ones launch everything at once and switch it off after the first mistake.

## 3. Design goals: more intuitive than today

Today's setup has these problems (seen in our walkthroughs). Each maps to a principle.

| Today | Principle for the redesign |
|---|---|
| Lands in the inbox; setup is tabs in any order, with no progress | **Always show where you are and what's next.** A tracker on the home screen and a mini tracker on every step. |
| Blank forms ("write your policies", "write a scenario") | **Review, don't write.** Zaapi drafts; the merchant accepts, edits or turns off. |
| Dense UI: 12.25px text, small targets, tables everywhere | **Readable first.** 14px body text minimum, generous spacing, cards where people scan, tables only for real comparisons. |
| Jargon: knowledge source, scenario, trigger, escalate, deploy, Flow Builder | **Plain words** (see the table in section 7). |
| "Completed" whether a file was fully read or half read | **Say what happened in words.** "We read 7 of 12 pages" beats a green pill. |
| AI output looks the same as facts the merchant typed | **Make AI work visible and checkable.** One AI style (section 4), a "Drafted by Zaapi" label, and the source shown ("from 14 of your replies"). |
| One primary button fights several others | **One primary action per screen.** Everything else is secondary or a text link. |
| Going live happens in a node-graph editor | **Plain choices with safe defaults.** Toggles and dropdowns; risky things off until the merchant turns them on. |
| Problems found by customers | **Show the consequence before the fix.** "Affects 6% of your chats" and "quoted RM15 in 3 of 6 answers" sit next to every fix. |
| Everything visible at once | **Summary first, detail on demand.** Expand rows for detail. |

## 4. Visual language

Keep Zaapi's brand, so it still feels like Zaapi, with a larger, calmer base than today.

**Colour**

| Role | Value |
|---|---|
| Brand teal | `#09C8AB` (600 `#00A892`, 700 `#008A77`) |
| AI gradient (primary buttons, AI accents) | `linear-gradient(94deg, #1ED1BB 0%, #5E40E1 140%)` |
| AI surface (anything the AI produced) | the same gradient at 8–10% opacity on white, with a 1px border at 25% |
| AI text accent (labels like "Drafted by Zaapi") | a gradient from `#008A77` to `#875BF7`, clipped to text |
| Text, primary | `#1D2939` |
| Text, secondary | `#475467` |
| Text, muted | `#667085` |
| Borders | `#EAECF0` |
| App background | `#F9FAFB`; cards white |
| Success | bg `#ECFDF3`, text `#067647` |
| Warning | bg `#FFFAEB`, text `#B54708` |
| Error / wrong answer | bg `#FEF3F2`, text `#B42318` |
| Neutral chip | bg `#F2F4F7`, text `#475467` |
| Projected (feature not built yet) | bg `#F4F3FF`, text `#5925DC`, dashed border |

**Type (Inter)**

| Style | Size / weight / line height |
|---|---|
| Page title (H1) | 24 / 600 / 32 |
| Section title (H2) | 18 / 600 / 26 |
| Card title (H3) | 15 / 600 / 22 |
| Body | **14 / 400 / 22** (today's is 12.25; go bigger) |
| Label, button | 14 / 500 |
| Caption, helper | 12 / 400 / 18 |
| Big number (scores) | 40 / 700 / 44 |

**Spacing, shape, depth**
- 4px base grid: 8, 12, 16, 24, 32, 48.
- Cards: 12px radius, 24px padding. Buttons and inputs: 8px radius, 40px height.
- Shadows: very soft (`0 1px 2px rgba(16,24,40,.06)`). Use borders more than shadows.
- Icons: outline style, 20px, 1.5px stroke (Lucide-like). The AI mark is a small ∞-style glyph in the gradient.

**Tone of on-screen copy:** plain English, British spelling, short sentences, speaking to "you". No exclamation marks and no hype words (seamless, effortless, unlock, empower). Numbers as digits.

## 5. Layout

- **Frame:** desktop 1440×900. It must also work at 1280×800.
- **Left nav:** 72px wide. Keep every item the real app has, so nothing looks removed. The list below was checked in the trial account on 28 Sep 2026, top to bottom:
  - **Icon only, with tooltips (as today):**
    - a store switcher (building icon, "Store: Rumah Kita");
    - a sidebar toggle ("Show AI Agent menu", ⌘B);
    - a divider;
    - Notifications (bell, with an unread dot);
    - Search;
    - a divider.
  - **Icons with short labels underneath** (today's are icons only): Tickets, AI Agent (active), Analytics, Automations, Broadcast, Contacts, Settings.
  - **Pinned to the bottom:** Live Chat Support (help icon).
  - **The AI Agent sub-menu** (Train: Knowledge Source, Scenario Handling, Personality; Launch: Test, Deploy; Monitor: Analyse) stays reachable through the sidebar toggle. Show it collapsed in these mock-ups.
- **Top bar:** 48px, across the full width. It carries the trial banner "Free trial ends in 6 days" with a dark "Subscribe now" button, centred.
- **Content:** max width 1040px, centred in the space left over, with 32px side padding.
- **Presenter sidebar (demo only):** 320px, fixed on the right. It must look separate from the product (see component 13).
- **Demo controls (demo only):** a small bar at the top right with a dashed outline and the label "Demo". It holds the merchant switcher, "Hide notes" and "Reset".

## 6. Components

1. **Primary button:** AI gradient fill, white text, 40px tall. One per screen.
2. **Secondary button:** white with a 1px border and primary text. **Text link:** teal 700.
3. **Status chip:** 24px pill, 12px text, with an icon. Set: Not started (neutral), In progress (teal), Needs attention (warning), Done (success), Wrong (error), Projected (dashed purple).
4. **Setup tracker (vertical stepper):** a numbered circle, then a step name (15/600), a one-line description, time ("5 min"), a status chip, and "Open" on the right. Circles are joined by a line; done steps get a filled teal circle with a tick. The current step is highlighted with an AI surface background.
5. **Mini tracker (horizontal):** 7 dots joined by a line, then "Step 3 of 7 · Next: choose how it sounds" and a "Back to setup" link. It sits under the page title on every step screen.
6. **Next step card:** large, on an AI surface: "Next: check what your agent knows · 10 min", one sentence of why, and the primary button.
7. **AI draft card:** AI surface, a "Drafted by Zaapi" label at the top left, the source ("From 14 of your replies") at the top right, the content, then Accept / Edit / Turn off.
8. **File row with "What we read":** file icon, name, size, a plain-words status ("Read all 4 pages" / "Read 7 of 12 pages") and an expand chevron. Expanded, it lists extracted items with a type chip (Fact / Rule / Live data) and a warning banner for anything missed, with a fix button.
9. **Conflict card:** a warning header "Your sources disagree: shipping to Sabah and Sarawak", then two source panels side by side with name, last-updated date and the quoted text. Under them, a consequence line: "Affects about 6% of your chats. In testing your agent quoted RM15 in 3 of 6 answers." Then the choice buttons (see screen 4).
10. **Readiness result:**
    - a score ring (40px number) with a verdict line ("Ready for a small launch");
    - three horizontal bars: correct / passed to your team / wrong;
    - a consistency line;
    - a by-topic table.
11. **Wrong answer card:** the customer's question as a chat bubble, "What your agent said" (error-tinted bubble), "What it should say", a cause line, and a Fix button.
12. **Toggle row:** label, one-line helper, and a switch on the right (on = teal). **Channel tile:** logo, name, status and a Connect button.
13. **Presenter sidebar (demo only):**
    - grey `#F2F4F7` background, dashed left border, small caps label "PRESENTER NOTES";
    - title "What's changed and why";
    - a merchant chip with photo, name, city and "Impact 7.6";
    - four labelled blocks: Today / The change / Why / Should move;
    - "In this demo";
    - pinned at the bottom: "Changes shown: 4 of 10", with a checklist.
    - It must never look like part of Zaapi.
14. **Merchant switcher (demo only):** a dropdown of six rows. Each row has a photo, name, city, a short quote snippet and an impact score chip. Aisha's row has a "Shows the most features" chip.
15. **Plan card:** "Your free setup drafts your top 6 topics" with a "What's in the AI Success Kit" link.
16. **Sale banner:** a slim warning-tinted bar: "11.11 is in 3 weeks. Add your vouchers and cut-offs so your agent gets them right." with an "Add sale info" button.

## 7. Plain words (use these, never the left column)

| Don't use | Use |
|---|---|
| Knowledge source | What your agent knows |
| Scenario / scenario handling | What your agent does / topics |
| Personality | How it sounds |
| Deploy / Let AI handle | Go live |
| Escalate | Pass to your team |
| Integrations | Your chat channels |
| Trigger | When a customer asks about… |
| Completed | Say what was read, e.g. "Read all 4 pages" |

---

## 8. Screens and ready-to-paste Stitch prompts

All mock-ups use **Aisha, Rumah Kita, Kuala Lumpur** (home goods, about 3,900 chats a month; WhatsApp, Shopee, Lazada, Instagram). Screen 11 uses Pranee. Generate each screen as a separate prompt. Each prompt below assumes Stitch has sections 1–6 as context. If it doesn't, paste sections 4–6 above the prompt.

### Screen 1: Setup home
> Desktop web app screen, 1440×900, Zaapi style (see design system). Left nav 72px with every item the real app has (see section 5): store switcher, sidebar toggle, Notifications, Search, then Tickets, AI Agent (active), Analytics, Automations, Broadcast, Contacts, Settings with labels, and Live Chat Support at the bottom. Top bar with trial banner "Free trial ends in 6 days" and a dark "Subscribe now" button. Presenter sidebar on the right (320px, grey, dashed left border, "PRESENTER NOTES").
>
> Main content, max 1040px:
> - Page title "Set up your AI agent" and subtitle "Rumah Kita · about 25 minutes in total".
> - Progress bar "Step 3 of 7".
> - A large Next step card on a light teal-to-purple gradient surface: "Next: check what your agent does · 10 min"; "We've drafted your top 6 topics from 3,480 WhatsApp chats. Review them before anything goes live."; primary gradient button "Review topics".
> - Beside it, a small plan card: "Your free setup drafts your top 6 topics", with a link "What's in the AI Success Kit".
> - A slim sale banner: "11.11 is in 3 weeks. Add your vouchers and cut-offs so your agent gets them right." with "Add sale info".
> - A vertical stepper of 7 steps, each with a name, one-line description, time, status chip and an "Open" button:
>   1. Connect your chats: Done
>   2. Check what your agent knows: Done
>   3. Check what your agent does: In progress (highlighted)
>   4. Choose how it sounds: Not started
>   5. See if it's ready: Not started
>   6. Go live small: Not started
>   7. First week live: Not started

### Screen 2: Step 1, Connect your chats
> Same shell. Mini tracker under the title (7 dots, "Step 1 of 7 · Next: check what your agent knows").
> - Title "Connect your chats"; subtitle "Connect the channels your customers use. Zaapi reads your past chats to draft your agent. Nothing is sent to customers."
> - A grid of channel tiles:
>   - WhatsApp: Connected; checkbox ticked "Share your last 6 months of chats"; "3,480 chats found".
>   - Shopee: "90 days imported · 2,610 chats".
>   - Lazada: "90 days · 1,140 chats".
>   - Instagram: "90 days · 220 chats".
>   - Website chat widget: "Connected automatically · connect the channels your customers use".
>   - LINE, TikTok Shop: Connect buttons.
> - A consent toggle row: "Let Zaapi read your past chats to draft your agent".
> - A result card on an AI surface: "About 3,900 chats a month. Your free setup drafts your top 6 topics."
> - Primary button "Continue".

### Screen 3: Step 2, Check what your agent knows
> Same shell, mini tracker (step 2).
> - Title "Check what your agent knows".
> - A file list, each row with a status in words:
>   - "CS macros.docx · edited Jan 2026 · Read all 6 pages";
>   - "Shipping matrix.csv · Read all 48 rows";
>   - "rumahkita.com/shipping-returns · Read the whole page".
> - One row expanded, showing extracted items with chips (Fact / Rule / Live data, never stated), e.g. "Returns within 14 days · Rule", "Stock levels · Live data, never stated".
> - A drop zone "Add a file or website" and a text link "Use sample files".
> - A section "3 things to settle before your agent uses them", with three conflict cards: the first expanded (see screen 4), the other two collapsed ("Returns: 7 days or 14?"; "A staff name appears in your data").
> - A disabled primary button "Continue" with the helper "Settle 3 conflicts to continue".

### Screen 4: Resolving a conflict (Aisha's shipping)
> A focused panel or modal over step 2. Warning header "Your sources disagree: shipping to Sabah and Sarawak".
>
> Two source panels side by side:
> - Left: "Website shipping page · updated Mar 2024": "Flat RM15 to Sabah and Sarawak".
> - Right: "Shipping sheet · updated Aug 2026": "RM18 for the first 3 kg, then RM6 per kg. Bulky items: ask Farah."
>
> Consequence line: "Affects about 6% of your chats. In testing your agent quoted RM15 in 3 of 6 answers."
>
> Below, numbered sections:
> 1. "Which is right?": options "Use the shipping sheet" (Recommended, newer and more detailed), "Use the website", "Write it yourself", "Ask a teammate" (avatar "Farah · Shipping").
> 2. "Bulky items aren't priced. What should your agent do?": "Pass it to your shipping team" (Recommended), "Quote from RM45", "Take the details and reply within 2 hours".
> 3. "Next time shipping sources disagree, trust:" a reorderable list "Shipping sheet → Website → CS macros", and a toggle "If sources still disagree when a customer asks, pass it to your team" (on).
> 4. "Your website still says RM15": a preview of corrected text and a "Copy updated text" button.
> 5. "Quick re-test": a result chip "18 of 18 correct or passed to your shipping team".
>
> Primary button "Save and re-test".

### Screen 5: Step 3, Check what your agent does
> Same shell, mini tracker (step 3).
> - Title "Check what your agent does"; subtitle "Drafted from your past chats. Accept, edit or turn off each topic."
> - A list of AI draft cards, each with the topic, share-of-chats chip, the drafted rule in plain words, the source ("From 212 of your replies"), "Pass to: [team]", and Accept / Edit / Turn off:
>   - Where's my order (31%, with a dashed "Projected: reads order status" chip);
>   - Shipping cost and time (17%);
>   - Damaged item or returns (11%);
>   - Sizing (9%);
>   - Vouchers (7%);
>   - COD (5%).
> - Below, a muted section "More topics we found (not in your free setup)": marketplace cancels 4%, bulk orders 3%, product care 3%, installation 2%. Two buttons: "Build it yourself" and "Have our team build these".
> - Primary button "Continue".

### Screen 6: Step 4, Choose how it sounds
> Same shell, mini tracker (step 4). Two columns.
>
> Left, form fields:
> - "Reply language": "Match the customer" (selected), with the helper "Your chats: 54% English, 38% Malay, 8% other";
> - "Your shop speaks as": a woman / a man / neutral (neutral selected);
> - "How it addresses customers": "you";
> - "Tone": Friendly / Warm and expert / Formal (Friendly);
> - "Emoji": None / A few / Lots (None).
>
> Right, a live preview in a phone-style chat. Customer: "Can deliver to Kota Kinabalu? How much for sofa cover?" Agent (AI style): "Hi! Yes, we deliver to Kota Kinabalu. Sofa covers are bulky, so our shipping team will send you the exact cost shortly."
>
> A reassurance line: "Your agent replies in the language each customer writes in." Primary button "Continue".

### Screen 7a: Step 5, See if it's ready (running)
> Same shell, mini tracker (step 5).
> - Title "See if it's ready".
> - A centred card: "Replaying 120 real questions from your last 90 days, 3 times each". A progress bar at 60%.
> - A ticker of question bubbles fading in: "Order #RK10233 dah ship ke?", "Can deliver to Kota Kinabalu?", "Queen size fit 6 feet bed ah?".

### Screen 7b: Step 5, result (the core screen)
> Same shell. Title "See if it's ready".
> - Top row:
>   - a score ring "70 / 100", with verdict "Fix 3 answers before you go live" (warning);
>   - three bars: Correct 61%, Passed to your team 27%, Wrong 12%;
>   - "Same answer on all 3 runs: 71%";
>   - a caption: "Your score shows how well your agent met your own go-live bar on real questions."
> - A section "3 wrong answers", with the first expanded as a wrong answer card:
>   - customer bubble: "Can deliver to Kota Kinabalu? How much for sofa cover?";
>   - "What your agent said" (red-tinted bubble): "We offer a flat shipping fee of RM15";
>   - "What it should say": "Bulky items to East Malaysia go to your shipping team";
>   - cause: "Your website and shipping sheet disagree";
>   - a small grey comparison chip, "Today's check: Groundedness ✓", crossed through next to "Readiness: Wrong";
>   - button "Fix".
> - A by-topic table: topic / questions / correct / passed on / wrong.
> - Secondary button "Re-run test".

### Screen 8: Step 6, Go live small
> Same shell, mini tracker (step 6). Two columns.
>
> Left, the settings:
> - "Channels": WhatsApp ticked; Shopee and Lazada unticked.
> - "Hours": "Out of hours only (00:00–09:00 and weekends)".
> - "Topics your agent handles": toggles: Where's my order on, Returns on, Sizing on, Vouchers on, COD on, "Shipping to East Malaysia" off (helper "Stays with your shipping team").
> - "I approve replies first" (on, "for the first 7 days").
> - "Monthly spend cap": 5,000 messages · $200.
> - "Who gets handoffs": Shipping → Shipping team; everything else → CS team.
> - "If your agent doesn't reply in 30 seconds, pass to a person" (on).
>
> Right, a sticky summary card on an AI surface: "Your agent will handle about 24% of WhatsApp chats. Everything else goes to your team." Then a small line "No Flow Builder needed" and the primary button "Go live".

### Screen 9: Step 7, First week live
> Same shell, mini tracker (step 7).
> - Stat cards: "1,120 chats handled", "58% resolved without your team", "470 passed to your team", "214 replies approved as-is · 19 edited".
> - A "Review 2 answers" list with Fix buttons.
> - A "Reply check" card: "Blocked 4 replies that used a staff name. They were passed to your team instead."
> - Reminders:
>   - "Shopee connection needs re-authorising in 11 months";
>   - "Lazada in 5 months";
>   - "212 of your 300 free messages used".
> - Sale prompt: "11.11 is in 3 weeks: add your vouchers. MERDEKA15 has expired."

### Screen 10: Dashboard (after setup)
> Same shell, no mini tracker.
> - Title "Your AI agent".
> - Channel status row: "WhatsApp · Live out of hours".
> - This week's numbers.
> - A review queue.
> - The sale prompt.
> - A card "4 more topics you could add" with "Build it yourself" / "Have our team build these".
> - A small "Setup complete ✓ · View setup" link.

### Screen 11: Guided questions (Pranee, no chat history)
> Same shell, mini tracker (step 2). Merchant: Baan Samunprai, Chiang Mai (herbal supplements).
> - A top notice: "LINE doesn't let us read chats from before you connected. We'll ask you a few questions instead." with a text link "Get your older LINE chats with the AI Success Kit".
> - A single-question card, conversational style, question 2 of 8: "What promotions are running now, and when do they end?" with a text field pre-filled "Buy 3 get 1, until 31 Oct".
> - A language toggle Thai / English at the top right.
> - Answered questions appear as fact cards on the right.
> - Primary button "Next question".

### Screen 12: AI Success Kit side panel
> A right-hand slide-over panel, 480px.
> - Title "AI Success Kit"; subtitle "Our team builds it with you".
> - "$1,900 · 60 days".
> - A checklist:
>   - conversation review;
>   - all topics drafted and tested;
>   - LINE history export (one month, ฿555, included);
>   - 30 days of live tuning;
>   - "30% of enquiries resolved or your money back".
> - A note "For Pro and Advanced plans with 300+ chats a month".
> - Primary button "Talk to us"; secondary "Build it myself".

## 9. Don'ts

- Don't copy today's dense 12px tables or icon-only nav.
- No node graphs or Flow Builder visuals in setup.
- Don't use the AI gradient for anything the AI didn't produce, apart from primary buttons.
- No more than one primary button per screen.
- No hype copy, exclamation marks or emoji in the UI chrome.
- Don't show "Completed" without saying what was read.

## 10. Hand-off

- Save the Stitch outputs to `prototype/stitch/`: exported HTML and CSS if Stitch offers it, plus PNGs named `01_setup_home.png` … `12_kit_panel.png`.
- Note any design decision that changes content or flow in `prototype/stitch/NOTES.md`, so the build session can reconcile it with `../context/`.
- The build session then uses these designs for the look, and the context pack for data and behaviour.
