# Prompt for the prototype build session

Start a new Claude Code session with the working folder **`/Users/miker/Documents/Zaapi`**. It picks up `CLAUDE.md` there automatically. Use the strongest model available. Paste everything below the line.

---

I'm doing the Zaapi Head of Product take-home. The memo is finished. I now need deliverable 2: a working prototype of the main change.

**Read these before you write any code:**
- the context pack: `prototype/context/`, starting with `00_README.md`;
- the Stitch designs: `prototype/stitch/NOTES.md` first, then all 13 PNGs in `prototype/stitch/` (`01_setup_home.png` to `12_kit_panel.png`).

**What to build**

A single self-contained HTML file, `prototype/zaapi_setup_prototype.html`. It recreates Zaapi's AI Agent setup as the memo proposes:

1. A setup home with a 7-step tracker. It's the first screen after login, and it turns into a dashboard once setup is done.
2. All 7 steps working, with simulated AI output:
   - drafting from past chats;
   - "what we read" for each file;
   - conflict flags;
   - drafted topics;
   - voice fields;
   - a readiness score with Fix buttons and a re-run;
   - go live small;
   - first week live.
3. Pranee's guided-questions screen for merchants with no chat history, and the AI Success Kit side panel.
4. A merchant switcher with all six merchants (one per quote in the brief), ordered by impact score. Aisha is flagged "Shows the most features".
5. Aisha's shipping conflict, settled in a side panel. The merchant:
   - sees what's at stake;
   - picks a source or asks a teammate;
   - fills the gap;
   - sets which source wins next time;
   - fixes it at the source;
   - gets a quick re-test.
6. A presenter sidebar, "What's changed and why", on every screen. It explains each screen (today, the change, why, what should move) and keeps a running tracker of the 10 changes. Use the text in `07_sidebar_copy.md` word for word.

The main change it has to show, from the memo: *"Zaapi drafts the agent from what the merchant already has, and shows them whether it's ready before any customer sees it."* Step 5, "See if it's ready", is the core screen.

**Which source wins**

- **Look and layout come from the Stitch designs:** spacing, type sizes, cards, the left rail, sticky footers, the conflict side panel, the "Drafted by Zaapi" AI surfaces. Where they differ from `design_system.md`, the designs win (see `05_build_rules.md`). Match the PNGs closely.
- **Data, wording and behaviour come from the context pack.** Take every number, name and message from `03_merchants.md` and the screen rules from `02_flow_and_screens.md`. Don't copy Stitch's placeholder content; `NOTES.md` lists it under "Content Stitch invented".
- **Adopt the 12 design decisions in `NOTES.md`,** with these exceptions:
  - use the real data wherever a decision has a placeholder number (e.g. "42 facts", "about 85");
  - drop the "Weekly performance check" card.
- **Build the left rail exactly as the finished PNGs show it.** It has the real app's 12 items in order: store switcher, sidebar toggle, Notifications, Search, then Tickets, AI Agent, Analytics, Automations, Broadcast, Contacts, Settings, and Live Chat Support at the bottom. Nothing may look removed.
  - Items other than AI Agent get a "Not part of this prototype" tooltip.
  - The sidebar toggle opens the AI Agent sub-menu (Train, Launch, Monitor) as a collapsed panel.
  - The icons are inline SVGs; reuse the `ICONS` set in `prototype/stitch/fix_and_render.py`.
- **Use the Stitch HTML in `prototype/stitch/html/` for reference only.** It loads Tailwind from a CDN, so rewrite the CSS by hand. Open a file only when you need an exact measurement.

**Rules**

- Follow `05_build_rules.md` for how to build and verify.
- One file, and no network requests at runtime: no CDN, no web fonts, no icon fonts.
- You can download the six Unsplash photos listed in `03_merchants.md` from images.unsplash.com, at 160×160, and embed them as base64. No other downloads.
- Label anything simulated, demo or projected as the context files say. Don't invent facts about Zaapi.
- All on-screen copy is plain English, British spelling, in my voice, with no AI clichés. Run the banned-phrase check from `07_sidebar_copy.md` on the whole file and report the result.
- Build Aisha end to end first, then add the other five merchants.

**Check it works**

1. Serve the folder locally and click through every merchant and every step in the built-in browser.
2. Check the console for errors, and check the network log shows no external requests.
3. At 1440×900, compare each screen side by side with its Stitch PNG and fix any obvious drift.
4. Also check 1280×800.
5. Go through `06_acceptance_checklist.md` and report each item in your final message.

**Outputs**

1. `prototype/zaapi_setup_prototype.html`
2. `prototype/README.md`, with:
   - how to open it;
   - what's simulated;
   - a 2-minute click path per merchant, Aisha's full tour first;
   - decisions made while building, including anything you changed from the Stitch designs and why;
   - photo credits.
3. A private Artifact link to the same file. Load the `artifact-design` skill first.
4. Prompt log entry 19 in `prompts/prompt_log.md`, in the existing format, with this prompt copied in.

**How to work with me**

Once you've read everything, give me a short plan (10 lines at most), then start building without waiting. Post a one-line progress update every few minutes. Only stop to ask me if a choice would change what the prototype argues. For anything else, pick sensibly and record it in the README.
