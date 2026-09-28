# Acceptance checklist

Tick every item in the final message, with a one-line note if something differs.

**The file**
- [ ] One HTML file opens offline and makes no network requests (network log checked).
- [ ] Under 1.5 MB; all six photos embedded.
- [ ] No console errors after a full click-through.

**Shell and home**
- [ ] Looks like Zaapi: nav rail, trial banner, Inter or system font, 14px root, AI gradient on AI-made content.
- [ ] Setup home shows: progress, next step card, the 7-step tracker, the sale banner and the plan card with the Kit panel.
- [ ] Mini tracker on every step screen, linking back home.
- [ ] Once all 7 steps are done, the home turns into the dashboard.

**Switcher**
- [ ] Six merchants ordered by impact score (Jo 9.0, Nattaya 8.4, Aisha 7.6, Linh 7.2, Budi 7.0, Pranee 6.2), each with its score.
- [ ] Aisha flagged "Shows the most features".
- [ ] "How we score impact" opens the scoring table.
- [ ] Each merchant keeps its own progress; reset works.

**The bet, per merchant**
- [ ] Jo: everything drafted (under 300 a month); the cancel rule is drafted from her DMs; the reservation conflict is resolved; score 77 → 92.
- [ ] Nattaya: "We read 7 of 12 pages"; confirm products; route to the beauty advisor; score 89 → 96.
- [ ] Aisha:
  - WhatsApp 180-day history ✓;
  - 3 conflicts;
  - the RM15 wrong answer shown beside "Today's check: Groundedness ✓";
  - East Malaysia shipping off at go-live;
  - the Kit offered for the topics not drafted;
  - score 70 → 88.
- [ ] Linh: order status toggle labelled "Projected"; the staff "Cancel order" button in the handoff; reply check blocking "I'm checking"; score 53 → 81.
- [ ] Budi: campaign mode banner, trial paused, canned lines flagged, 10-minute out-of-hours launch, "finish on 14 Nov" reminder; score 68 → 86.
- [ ] Pranee:
  - the LINE limitation explained, with the Kit's export offered as optional;
  - the guided questions;
  - "92% Thai. Your agent will reply in Thai";
  - the "speaks as a woman" field;
  - score 85 → 90.

**Aisha's conflict**
- [ ] Conflict 1 resolves through all six parts: stakes, pick (including "Ask a teammate" with Farah), fill the gap, which source wins, fix at the source with "Copy updated text", and a quick re-test showing 18 of 18.
- [ ] Conflicts 2 and 3 resolve.
- [ ] Step 2 isn't ticked until all three are resolved.

**Presenter sidebar**
- [ ] It's on by default and collapsible, and styled as presenter notes rather than Zaapi UI.
- [ ] The text matches `07_sidebar_copy.md` word for word, updating per screen and per merchant.
- [ ] The running tracker "Changes shown: X of 10" ticks as screens are visited.
- [ ] The banned-phrase grep on the whole file returns nothing (command and result reported).

**Honesty**
- [ ] Simulated, demo and projected numbers are labelled (an "About this prototype" panel, plus a "Projected" chip where a feature doesn't exist yet).
- [ ] No invented facts about Zaapi beyond `03_merchants.md`.
- [ ] Plain wording throughout (see the table in `02_flow_and_screens.md`); British spelling; no AI clichés.

**Deliverables**
- [ ] `prototype/README.md`: how to open it, what's simulated, a 2-minute click path per merchant (Aisha's full tour first), decisions made while building, photo credits.
- [ ] Private Artifact link returned.
- [ ] Prompt log entry 19 added.
