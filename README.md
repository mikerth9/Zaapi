# Zaapi take-home: getting merchants live on the AI Agent

Mike Rourke · September 2026 · Head of Product, Bangkok

This is my answer to Zaapi's take-home exercise. The brief is in `brief/`. It asked for three things: a two-page memo, a rough prototype of the main change, and the prompts I used. All three are here, with the research and test evidence behind them.

## The three deliverables

| Deliverable | File | Notes |
|---|---|---|
| **1. Memo** (2 pages) | [`memo/zaapi_memo.pdf`](memo/zaapi_memo.pdf) | HTML source alongside it. Sections: the problem, what's going wrong, what I tested, what I'd change, what I'd do first, how I'd know it worked. |
| **2. Prototype** | [`prototype/zaapi_setup_prototype.html`](prototype/zaapi_setup_prototype.html) | A working setup flow, not wireframes. One self-contained file: download it and open it in a browser. [`prototype/README.md`](prototype/README.md) has a two-minute click path per merchant. |
| **3. Prompts** | [`prompts/master_prompts.md`](prompts/master_prompts.md) | The 29 substantive prompts in order, each with what I wanted, the prompt as sent, and what I did with what came back. The raw working log with every short follow-up is [`prompts/prompt_log.md`](prompts/prompt_log.md). |

## The short version

Of every 100 merchants who start setting up the AI Agent, 61 get it live, a median of 19 days after signup, and 52 are still live a month later. The agent itself is capable. Setup is the problem: it asks a small business to write its own AI agent from scratch, gives it no reliable way to check the result, and then only lets it switch the agent on for everything.

Four causes, each traced to the merchant quotes in the brief:

1. **No clear path in.** You land in the inbox and nothing mentions the AI Agent.
2. **Write it all, can't see it.** Policies often aren't written down, and a half-read file still shows "Completed".
3. **No real way to test.** One typed message at a time, and answers vary run to run.
4. **All or nothing, no orders.** Going live runs through Flow Builder, and the agent can't see orders.

The main change: **Zaapi drafts the agent from what the merchant already has, and shows them whether it's ready before any customer sees it.** Everything else in the memo supports that. The prototype shows it working for six merchants, one per quote in the brief.

## How to look at the prototype

1. Download `prototype/zaapi_setup_prototype.html` and open it in Chrome, Safari or Edge on a laptop. It makes no network requests.
2. The dashed box top right is the demo control. Click the merchant name to switch between the six merchants, ordered by impact score. Start with Aisha, who shows the most features.
3. Work through the seven steps. Step 5, "See if it's ready", is the core screen. The presenter sidebar on the right explains what changed on every screen and why.

Everything the product "finds" is simulated and labelled: **Sourced** (from the brief or my tests), **Demo data** (made up to be plausible) or **Projected** (needs a feature Zaapi doesn't have yet). The README in `prototype/` lists the numbers and where they come from.

## What's in the folder

| Folder | What it holds |
|---|---|
| `brief/` | Zaapi's take-home brief, as sent. |
| `memo/` | The memo, as PDF and as the HTML it was printed from. |
| `prototype/` | The prototype, its README, the context pack it was built from (`context/`), Zaapi's design tokens (`tokens.css`, `design_system.md`), the six persona photos (`assets/`) and the Google Stitch screen designs it follows (`stitch/`). |
| `prompts/` | The master prompt list, the raw prompt log, and the three long prompts kept as files: the product walkthrough, the prototype build and the prototype fixes. |
| `appendix/` | The evidence the memo cites. A: hypotheses written before touching the product, then tested. B: root causes. C: every integration guide checked against the providers' own docs. D: every quote and claim in the brief mapped to evidence. `appendix/README.md` indexes them. |
| `research/` | The test evidence. The product walkthrough log, two rounds of persona tests against my trial account with their summaries, the knowledge files each persona would really have (`persona_kb/`), the competitor research (`competitors/`), and the help-centre language examples. |
| Root files | `01_memo_outline.md`: the decisions the memo was written from. `memo_review.md`: Perplexity's independent review of the draft. `zaapi_personas.md` and `zaapi_personas_v2.md`: the four archetype personas, then the six built from the brief's quotes. `zaapi_ai_agent_activation_research.md`: the market and competitor brief. |

## How the work was done

- I wrote my hypotheses down before I touched the product, so the walkthrough could prove me wrong.
- I signed up for a trial, walked the product myself, and had Claude walk it again step by step with a log, judging every screen through the personas.
- Each of the six merchants in the brief became a persona with a test script in their customers' language. Each got an agent built the way that person would build it, with only the knowledge they'd have, and was tested in Zaapi's test mode. No real customers were involved.
- Every claim about Zaapi's product was checked on screen or in the brief before it went in the memo. Research files carry evidence tags: `[product]` seen on screen, `[help]` help centre, `[pricing]` pricing page, `[provider]` a platform's own docs, `[persona]` persona tests, `[mike]` my own walkthrough, `[inference]` reasoning.
- Anything that depended on outside knowledge was tagged and checked in Perplexity before it reached the memo.

The split of work between me, Claude, Perplexity and Google Stitch is set out at the top of `prompts/master_prompts.md`.

## Things to know

- **The scores are a guide, not statistics.** One tester, one trial account, five to seven questions per persona, knowledge files I wrote to match each persona. The memo says so in its footer.
- **The Thai strings in the prototype** (Pranee's screens) are machine-written and still to be checked by a Thai speaker. The prototype README lists every one with its intended English.
- **The brief is Zaapi's.** It's included so the memo and evidence can be read against it. The numbers and quotes in it are fictional, as the brief says, and I treated them as real.
- **Photos** in the memo and prototype are from Unsplash, for illustration only, credited in the prototype README. They don't show real merchants.
- **Not included:** my working notes and plan, the earlier memo drafts, and the Stitch export files that load from a CDN. Nothing in them changes the deliverables.

Questions: mikerth9@gmail.com
