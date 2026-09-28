# Goal and scope

## Why this prototype exists

It's deliverable 2 of the Zaapi Head of Product take-home: "show us the main change you'd make". The memo's main change, word for word:

> **Zaapi drafts the agent from what the merchant already has, and shows them whether it's ready before any customer sees it. Everything else supports that.**

Mike will click through it live in the interview. It has to feel like real Zaapi, work offline from one file, and let him jump straight from any of the brief's six merchant quotes to the fix for it.

## Objectives (agreed with Mike)

1. **Show the bet working.** Zaapi drafts the agent from the merchant's chats, files and listings. The merchant then sees what it read, and whether it's ready.
2. **Every quote leads to its fix.** Six merchants, one per brief quote, each highlighting the part of the fix their quote needs.
3. **Free vs paid is clear, and the upsell doesn't feel forced.** Three cases:
   - under 300 chats a month (everything drafted);
   - 300+ a month (top topics drafted, the rest listed to "build it yourself" or upgrade to the AI Success Kit, which includes the LINE history export);
   - no usable history (guided questions instead).
4. **It feels like Zaapi.** It uses Zaapi's design system and app shell, and the AI styling (a teal-to-purple gradient) marks everything the AI produced.
5. **Order by impact.** The merchant switcher lists merchants by impact score, highest first, with the score shown. Aisha is flagged "Shows the most features".

## In scope

- The app shell (nav rail, trial banner), the **setup home** with a 7-step tracker, all 7 steps working with preset data, a mini tracker on every step screen, and the setup home **turning into a dashboard** once setup is done.
- **Merchant switcher** with all six merchants, ordered by impact score.
- **Simulated AI:** loading states (e.g. "Reading 3 files…", "Replaying 120 questions, 3 times each…"), then preset results. Fix actions change the results, and a re-run shows the "after" numbers.
- **Dummy uploads:** a drop zone that accepts any file (nothing is read), plus "Use sample files" to load the merchant's preset files.
- **A presenter sidebar, "What's changed and why":** a right-hand panel, on by default and collapsible. For each screen it shows what happens today, what changes, the evidence and which measure should move. It also keeps a running tracker of the 10 changes shown. All its text is in `07_sidebar_copy.md`, to be used word for word.
- **Reset** for each merchant, and reset all.

## Out of scope

- Real AI calls, real uploads or parsing, any network calls, logins or payments.
- Mobile layout (Zaapi is desktop-only; minimum width 1024px is fine).
- Flow Builder, the inbox, analytics, broadcast. They can appear as nav icons, but they're inactive.
- Changing the memo. Mike's main session handles that.

## Outputs to produce

| # | Output | Where |
|---|---|---|
| 1 | **Self-contained prototype**: one HTML file with CSS, JS, data and six base64 photos inline, and no external requests | `/Users/miker/Documents/Zaapi/prototype/zaapi_setup_prototype.html` |
| 2 | **README with demo script**: how to open it, what's simulated, and a 2-minute click path per merchant (Aisha's full tour first, then the others in impact order) | `/Users/miker/Documents/Zaapi/prototype/README.md` |
| 3 | **Private web link**: the same file published as a private Artifact, so Mike can share a link | Link returned in chat |
| 4 | **Prompt log entry**, number 19 | `/Users/miker/Documents/Zaapi/prompts/prompt_log.md` |

Screenshots aren't needed.
