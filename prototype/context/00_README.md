# Prototype context pack

Read these in order before building anything. They hold every decision already made, so the build session doesn't have to re-derive them.

| File | What it gives you | Must read? |
|---|---|---|
| `01_goal_and_scope.md` | What the prototype has to prove, what's in and out of scope, and the outputs to produce | Yes |
| `02_flow_and_screens.md` | The app shell, setup home, 7 steps, dashboard, merchant switcher, notes toggle, and the plain-wording rules | Yes |
| `03_merchants.md` | Six merchants with their preset "AI output": chats found, files read, conflicts, drafted topics, voice, readiness results, go-live, week one | Yes: it's the data |
| `04_impact_scoring.md` | How merchants are ordered and scored | Yes |
| `05_build_rules.md` | Single-file build, design tokens, images, state, how to verify | Yes |
| `06_acceptance_checklist.md` | What must work before it's called done | Yes, at the end |
| `07_sidebar_copy.md` | The "What's changed and why" presenter sidebar: layout, all the text to use word for word, and the language checks | Yes |

**Other sources.** Open these only if something here is unclear:

- `../design_system.md` and `../tokens.css`: Zaapi's design system. Use the tokens directly.
- `../../memo/zaapi_memo.html`: the memo the prototype supports (section 4 is the change being prototyped).
- `../../research/persona_v2_exec_summary.md` and `../../research/persona_v2_test_log.md`: where the merchant results come from.
- `../../zaapi_personas_v2.md`: full persona detail and each merchant's own test questions.
- `../../appendix/C_integration_guides_check.md`: channel facts (LINE history, WhatsApp 180-day history, re-authorisation).

**Rules that apply throughout:**

- **Numbers:** anything the product shows as a result is simulated, and must look plausible and match `03_merchants.md`. Don't invent new facts about Zaapi; if something is needed that isn't here, ask Mike.
- **Copy:** plain English, British spelling, short sentences, in Mike's voice. Avoid AI tells: no "It's not X, it's Y", no clever reversals, no slogans, no "seamless", "effortless" or "empower".
- **Prompt log:** log this session in `../../prompts/prompt_log.md`, using the existing format, as the next number (19).
