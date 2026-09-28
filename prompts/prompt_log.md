# Prompt log (raw working record)

*Every AI interaction used on this exercise, in order: tool, purpose, prompt as sent, and what was done. This is the working log, kept as it was. The "What I did with it" placeholders below are answered in `master_prompts.md`, which is the version to read.*

**Tools and why each one**
- **Claude** handles reasoning, synthesis, critique, writing, and building the prototype, working from my files and the brief.
- **Perplexity** handles facts from the outside world that need current sources and citations. I use it for anything Claude would otherwise answer from memory (marketplace platform rules, campaign calendars, competitor patterns, Zaapi's own public positioning).
- **Rule:** Claude marks any claim that depends on outside knowledge `[ext]`. Each `[ext]` item goes to Perplexity before it reaches the memo.

---

## 01 · Claude · Pre-walkthrough hypotheses

**Why:** Write down what I believe *before* using the product, so the walkthrough tests my assumptions instead of shaping them unnoticed.
**Input:** brief PDF attached.

```
Context
I'm doing the Head of Product take-home for Zaapi (SEA commerce chat: Helpdesk +
AI Agent across WhatsApp, LINE, FB, IG, Shopee, Lazada, TikTok Shop, Shopify).
Brief attached. The numbers and quotes are fictional; treat them as real.

I haven't used the product yet, on purpose. I want my hypotheses written down
first so the walkthrough can prove them wrong. This goes in the memo appendix.

Task
Generate falsifiable hypotheses for why merchants take a median 19 days to go
live and 39% never do.

How to work
1. Read the funnel as data before telling any story. Compute step-to-step
   conversion. Call out anything odd (ordering, non-monotonic steps) and what it
   implies about how the product actually works.
2. Group hypotheses by where in the lifecycle they bite: never starting /
   stalling mid-setup / going live then retreating. Then anything cross-cutting.
3. For each: one-sentence claim written so it could be wrong; evidence from the
   brief (cite the row or quote); confidence H/M/L and why; what would disprove
   it; how I'd test it (walkthrough / data I'd request / external research).
4. Flag any correlation in the brief that could be selection rather than cause.
5. List alternative explanations that would make the whole frame irrelevant
   (e.g. plan gating, technical approval delays).

Constraints
- No solutions. If a hypothesis only makes sense with a fix attached, it's a
  solution in disguise. Rewrite it.
- Restating the funnel is not a cause. "People drop at scenarios" is an
  observation.
- Use the brief only. Anything that depends on general knowledge of SEA commerce
  or marketplace platforms, tag [ext] so I can verify it in Perplexity.
- 10–13 hypotheses max. Sharp beats comprehensive.
- Note any bias in the evidence itself (who the quotes come from, how).

Output
Markdown. One-paragraph "current best guess" first. Then funnel table +
observations, hypotheses, alternatives to rule out, a walkthrough checklist, and
the data questions I'd send Zaapi.
```

**What I did with it:** Kept the structure. Pushed harder on H8 (the share dial controls volume, not risk) and H12 (unused Helpdesk history), which I think are the sharpest. Sent `[ext]` items to Perplexity (PX-01 to PX-04). → `appendix/A_hypotheses.md`

---

## 01b · Claude · Hypotheses v2: my own notes plus the help centre

**Why:** Re-run P01 with my own pre-reading hypotheses and Zaapi's public help centre as extra input, so the list tests what I actually believe and the real product as documented, not only the brief.
**Input:** same prompt as 01, plus:

```
My current working hypothesis, from my notes reading the brief, before trying
the product -
* knowledge base is reliant on the customer having this written down in some
  form of digital format which a lot of SMEs may not have
* that when connecting systems it is not pulling any historic info to create a
  knowledge base
* that getting users to setup just before a campaign period is likely to result
  in less completions, instead it should be as part of a considered build up
  before the period e.g. 1 month ahead, 6 weeks ahead - may need to do some
  research to consider this
* That scenarios aren't prominent enough or explained well enough to the
  customer.

Additionally we should use - https://help.zaapi.com for additional context.
```

**What I did with it:** *(to fill)* → `appendix/A_hypotheses.md` (v1 kept as `A_hypotheses_v1.md`)

---

## 02 · Claude Sonnet 5 + Claude in Chrome · Product walkthrough (one run, four persona lenses)

**Why:** Test hypotheses H1–H13 against the real product in one pass. The agent is built as Fresh Laundry (the best case, everything written down). Each screen is also assessed through the four personas, and help.zaapi.com is checked wherever a persona gets stuck. What was seen on screen, what came from the help centre, and what was inferred stay separate.
**Model choice:** Sonnet 5 rather than Opus, to fit a long browser session inside Claude Pro limits. It writes a checkpoint after every step so the run can resume after a limit.
**Prompt:** see `prompts/02_walkthrough_prompt.md`.
**What I did with it:** *(to fill)* → `research/walkthrough_log.md`

---

## PX-00 · Perplexity · Zaapi context before walkthrough

**Why:** Know the company's positioning, pricing and AI Agent packaging before I judge the product. This also checks the plan-gating alternative.

```
What is Zaapi (zaapi.com), the SEA conversational commerce platform? I need:
- products and how the AI Agent is packaged (included, add-on, credits, trial limits)
- pricing tiers and which include AI Agent
- supported channels and markets
- target merchant segments
- AI Agent launches or updates in 2025–2026
- what reviewers (G2, Capterra, app stores, Shopify app store) say about setup
Cite sources. Mark anything older than 12 months. If pricing isn't public, say
so rather than estimating.
```

**What I did with it:** *(to fill after running)*

---

## PX-01 · Perplexity · Marketplace chat constraints (tests H7, H12)

```
For Shopee, Lazada and TikTok Shop in Thailand, Malaysia, Indonesia, the
Philippines and Vietnam:
1. Do their open platform / partner APIs allow third-party tools to send
   automated or AI-generated replies in buyer–seller chat? Any restrictions on
   content, links, or response timing?
2. Can a third-party app read order data and take actions (cancel, return,
   update address) through the API, or only read?
3. How do chat response rate/time metrics affect seller status (e.g. Shopee
   Preferred Seller, Lazada LazMall)?
4. How long does app authorisation typically take for a seller?
Prefer official seller centre / open platform docs. Give dates. Flag where
rules differ by country.
```

**What I did with it:** *(to fill)*

---

## PX-02 · Perplexity · Campaign calendar and seller workload (tests H2)

```
How often do major marketplace sales campaigns run in Southeast Asia (Shopee,
Lazada, TikTok Shop), 2025–2026? List the recurring ones: monthly double-date
sales (1.1–12.12), payday sales, 11.11, 12.12, Ramadan/Harbolnas, Songkran and
similar. For each: typical run-up period for sellers, and any published data on
how much customer chat volume rises during campaigns.
I'm trying to establish whether "campaign period" is a rare event or effectively
most of the year for an active marketplace seller. Cite sources.
```

**What I did with it:** *(to fill)*

---

## PX-03 · Perplexity · How other AI agents get SMBs live (tests H4, H8, H9)

```
How do AI customer-service agents for SMB/ecommerce onboard merchants to their
first live conversation? Compare Intercom Fin, Zendesk AI agents, Gorgias AI
Agent, Tidio Lyro, respond.io and SleekFlow on:
- drafting knowledge or guidance from past support conversations/tickets
- testing against real historical conversations (simulation, replay, test sets)
  vs free-form test chat
- partial rollout controls: by topic/intent, channel, hours, % of traffic,
  draft/suggest mode for human agents
- readiness or coverage indicators before going live
- stated time-to-value claims
Cite product docs or changelogs where possible, with dates. Separate what's
documented from marketing claims.
```

**What I did with it:** *(to fill)*

---

## PX-04 · Perplexity · Language in SEA commerce chat (tests H11)

```
How do online shoppers in Thailand, Indonesia, Vietnam, Malaysia and the
Philippines write in customer-service chat? I'm interested in code-switching
(Thai-English, Taglish, Manglish), romanised Thai, slang and abbreviations,
and polite particles. What published evaluations exist of how well current LLMs
handle these in customer-service settings? Cite research or credible industry
sources, 2024 onwards.
```

**What I did with it:** *(to fill)*

---

## 03 · Claude Opus 5.5 (Claude Code + Claude in Chrome) · Walkthrough vs hypotheses

**Why:** Test every hypothesis in Appendix A against the walkthrough, my own separate walkthrough notes, and Zaapi's public pricing page. Confirm, kill or revise each one, then group what survives into root causes.
**Model choice:** switched to Opus for this step. It's synthesis and judgement over a lot of material, not a long browser session.
**Input:** `research/walkthrough_log.md`, `appendix/A_hypotheses.md` (v2), plus:

```
please can you now test against my hypothesis too. also the below -

* It defaulted me to thai on setup stages and i had no way to change to thai on
  those screens
* Scanned the qr and it immediately took me from the setup channel step losing
  the in moment opportunity
* Helpdesk info for the creating flows doesn't read very user friendly as a SME
* IN the flow builder there needs to be some support to understand the intent of
  the user, potentially have an AI agent that can redesign based on the users
  instructions?
* Each AI response is ~35c/1250baht before vat
* When setting up widget I selected english as an extra language and it kept the
  original language (thai) in the english field
* In the demo screen it doesnt allow change to english but also is mixing
  english and thai
* The quick setup is gone - there is no step by step guide to go through. There
  is one on the help centre but it's not for the AI tool. The AI tool info is
  useful there but again isn't in a user friendly format thinking about personas.
* First page coming in doesn't show you steps left to complete/helpful dashboard
  to keep going or suggestions/nudges on what to do next just straight into your
  inbox.
```

The agent also read zaapi.com/en-sg/pricing to check the pricing and plan-gating alternatives (it partly answers PX-00).

**Output:** `appendix/A_hypotheses.md` v3 (v2 kept as `A_hypotheses_v2.md`), `appendix/B_root_causes.md`, and addenda A (my notes) and B (pricing) in `research/walkthrough_log.md`.
**What I did with it:** *(to fill)*

---

## 04 · Claude Opus 5.5 (Claude Code + Claude in Chrome) · Full persona test scripts

**Why:** The walkthrough only applied the personas as a lens to a best-case agent. This step runs each persona's full test script against a separate agent built the way that persona would build it, with the knowledge they'd realistically have.
**Prompt as sent:**

```
please test the full scripts as i've bought the max plan on claude. Also generate
different FAQ/knowledge files for each type of business if needed.
```

**What the agent did:** wrote realistic knowledge files for each business in `research/persona_kb/`, with gaps and conflicts planted from each persona file (stale macros, unconditional "ready stok", no dosage, rules only in Joanna's head). Created one chat widget per business so knowledge doesn't mix. Set up each business as its persona would (Aisha writes scenarios; Budi and Pranee skip them). Ran all 27 script messages, clearing the chat between customers, plus two probes and an isolation check. Then ran three fix loops (H10).
**Output:** `research/persona_test_log.md`; evidence tagged `[persona]` in `appendix/A_hypotheses.md` and `appendix/B_root_causes.md`.
**What I did with it:** *(to fill)*

---

## 05 · Claude Opus 5.5 (Claude Code + Claude in Chrome) · Check my working view before the memo

**Why:** Before drafting, test my own three-point view of the root causes against everything in the folder, and get suggestions for what it misses. Core thinking first, then I challenge it, then we write the memo.
**Prompt as sent:**

```
using all the information in this folder help me synthesise the memo -
[memo brief: what's going wrong / what you'd change / what you'd do first / how you'd know it worked]

My working view is that there are some core issues preventing customers from
getting the best outcomes and staying live -

* No landing page helping them see the steps needed for success - this should be
  a user friendly guided and likely have a trailing pop up on other screens to
  show the current progress and quick nav
* While existing data can be pulled from integrations there isn't the ability to
  have that turned into their knowledge base and scenarios - I think the journey
  should be they connect their integrations, website and any other documents
  together, and they give permission for the Zaapi AI to read historic
  interactions and data to then pull together the historic interactions,
  resolutions, key info and create the knowledge base for the customer to review
  and scenarios.
* In the workflows they should have easy language to follow and easy language
  should be in the help site too, we should pull some examples where it gets
  quite technical for an SME business. (feel free to use the chrome browser to
  check these)

Check these against what you've seen and give me suggestions for any additional.
Lets get the core thinking done now and i'll challenge then we can move to
populating the memo
```

**What the agent did:** read the brief, Appendices A and B, the walkthrough and persona logs, and the competitor and market research. Pulled the AI and Flow Builder help articles from help.zaapi.com (via llms.txt) for language examples.
**Output:** `research/help_centre_language_examples.md`; the core-thinking critique in chat.
**What I did with it:** *(to fill)*

---

## 06 · Claude Opus 5.5 (Claude Code + Claude in Chrome, web fetch) · Integration guides vs provider docs

**Why:** Integration setup is friction before the AI Agent even starts. Check whether Zaapi's integration guides still match what each provider documents today.
**Prompt as sent:**

```
also something to check, it can go in the appendix but is friction, check all the
integration guides on the help page then review each providers help guide and
determine where this isn't correct e.g. the Line one is out of date as this info
cant be pulled from dev site anymore.
```

**What the agent did:** downloaded all 50 integration articles from help.zaapi.com (via llms.txt). Checked each claim against LINE Developers (and LINE's markdown docs), Meta for Developers (WhatsApp, Messenger, Instagram), Shopee's seller hub and CRR guide, and LINE for Business Thailand. Tested the outbound links.
**Output:** `appendix/C_integration_guides_check.md`.
**What I did with it:** *(to fill)*

---

## 07 · Claude Opus 5.5 (Claude Code, web fetch) · AI Success Kit

**Prompt as sent:**

```
tell me more about - Zaapi's paid "AI Success Kit" (a done-for-you service)
```

**What the agent did:** read the pricing page and the AI services page (`zaapi.com/en-sg/ai-services`).
**Output:** Addendum C in `research/walkthrough_log.md`; analysis in chat.
**What I did with it:** *(to fill)*

---

## 08 · Claude Opus 5.5 (Claude Code) · Tiered setup model that protects the AI Success Kit

**Why:** Shape the main change so it fixes setup for every merchant without undercutting Zaapi's paid AI services.
**Prompt as sent:**

```
Ok lets work this through, we don't want to cannibilise the AI services/kit. So we
should be looking to -

* solve the friction of set up for all customers
* for SMB under a certain size provide the basic support to get a knowledge base
  and basic scenarios set up
* improve the language/intuitiveness of the workflow builder with suggested flows,
  user still to set up from the data
* for customers that are larger than the set size only a proportion of their data
  would be used/limited scenarios or for SMBs looking for more scenarios and deeper
  knowledge bases we would immediately identify and do the upsell - we can give
  them the starting info (additional initial suggested scenarios to explore and X
  amount of data to also review. This would then mean they aren't left feeling
  they're forced to pay but also shows the value add of it.
* This means very small businesses can set up quickly without worry, the larger
  ones can still not pay extra if they don't want and have some signposting of
  where to look.
* For the companies without any historic info beyond brief say a messenger app we
  should have a guided wizard to help them put in information they know then an
  AI sweep to give them the basics too.

* Activation rate is materially worse for accounts that signed up during a
  marketplace campaign period (Double 11, 12.12, Ramadan sale).
   * for this i think we say campaigns should start earlier than the timings and
     also with those connecting prompt them to connect their busiest channel
   * the improvements suggested should also help
```

**Output:** critique and tier model in chat.
**What I did with it:** *(to fill)*

---

## 09 · Claude Opus 5.5 (Claude Code) · Lock decisions into a memo outline

**Prompt as sent:**

```
so i think we have this idea but we should also have the step by step tracker on
the landing page for easy setup, simplify language.

1. keep the conversations a month
2. top topics then they self serve or upgrade
3. yes
```

**Output:** `01_memo_outline.md` (agreed decisions, tracker steps, wording table, order of work, measures, prototype choice).
**What I did with it:** *(to fill)*

---

## 10 · Claude Opus 5.5 (Claude Code) · Sale-period update prompt

**Prompt as sent:**

```
we should also include a prompt to add information for the sales periods when
they're coming up
```

**Output:** change 10 in `01_memo_outline.md`, a recurring tracker step, a line in the order of work, and a new measure.
**What I did with it:** *(to fill)*

---

## 10a · Claude Opus 5.5 (Claude Code + Claude in Chrome) · Design system pass and brief coverage check

**Why:** (1) Capture enough of Zaapi's design system for a faithful prototype. (2) Check that every friction point and piece of merchant feedback in the brief is covered by evidence, and close any gap that could be tested cheaply.
**Prompt as sent:**

```
ok do the pass. also check the case study and the customer feedback and make sure
you've properly captured anything related to their friction/feedback
```

**What the agent did:** read the app's Tailwind theme variables and sampled computed styles on seven screens (skipping the inbox because a real Gmail account is connected), then removed its temporary local-storage keys. It mapped every quote, product claim, funnel row and commercial statement in the brief to the evidence. It reproduced the Kuala Lumpur quote by temporarily switching off Aisha's guardrails, then restored them.
**Output:** `prototype/tokens.css`, `prototype/design_system.md`, `appendix/D_brief_coverage.md`, and an addendum in `research/persona_test_log.md`.
**What I did with it:** *(to fill)*

---

## 11 · Claude Opus 5.5 (Claude Code + Claude in Chrome) · Draft memo

**Prompt as sent:**

```
ok lets pull together all the sources and create a draft memo. we should cover the
problem statement, what the diagnosis is for whats going wrong, include a brief
section on the personas tested and key findings. find a small image for each using
unsplash.

Then what I'd change

page 2 the sequencing and the how i'd know it worked.
```

**What the agent did:** built the memo from `01_memo_outline.md`, Appendices A–C, the persona summary and the Kit research. The Unsplash connector refused (the Unsplash account email isn't confirmed), so persona photos were picked from Unsplash's public search (free licence) and hotlinked. Laid out as A4 HTML, printed to PDF with headless Chrome, and checked for fit: exactly 2 pages.
**Output:** `memo/zaapi_memo.html`, `memo/zaapi_memo.pdf`.
**What I did with it:** *(to fill)*

---

## 12 · Claude Opus 5.5 (Claude Code) · Memo revision: voice, method, visual "what I'd change"

**Prompt as sent:**

```
take out the reference to help centre being wrong just should refer to the language.

can you explain the what you wouldn't do they don't all make sense.

Review all the language and take out any AI sounding language or tells, make it more like my voice.

Give some more context on how i did the walkthroughs, using the customer feedback to create personas with perplexity and then claude code to do the live monitored runthrough.

can we make the what i'd change more compelling and visually easier to follow
```

**What the agent did:** removed the help-centre accuracy points (kept the wording and mixed-language point). Rewrote the "not do" list with a reason for each: dropped two weak items and added "order actions first" and "faster launches on their own". Rewrote all the copy in plainer first-person language. Added a method box. Rebuilt "What I'd change" as the 7-step tracker graphic plus a problem → change table and the three tiers. Re-checked the fit: exactly 2 pages.
**Output:** `memo/zaapi_memo.html`, `memo/zaapi_memo.pdf`.
**What I did with it:** *(to fill)*

---

## 13 · Claude Opus 5.5 (Claude Code + Claude in Chrome) · Fact-check and evidence pass

**Prompt as sent:**

```
on the what's going wrong can you fact check that again check the portal too as isn't the free trial of basic or is it a higher version?

Also remember the chat isn't one channel it needs another connected beyond.

going wrong 2 i think should be easier ways for merchants to test as per the what would change

3 there is a score but no explain on how the score is derived

what i'd change - 1 also have that as the landing page when they login and then maybe it changes to the dashboard after that.

the what i wouldn't do is seeming to state things as a fact, if it's doing that it needs to have a reference to back it up e.g. most merchants open flow builder to go live - but it's nott avaiklable in the basic package i thought?

anything you need evidence or to check do so through either the brief, the claude connector to chrome
```

**What the agent found (app.zaapi.com and zaapi.com/en-sg/pricing, 25 Sep 2026):**
- Billing shows the plan only as "Free trial", with no tier named. The trial account can build and publish Flow Builder flows, which is a Pro-and-above feature. The pricing comparison shows Flow Builder not on Basic but "AI deployment" ticked on Basic, while the Deploy page only offers Flow Builder routes. How a Basic merchant goes live is unclear, so it's added to the week 0–2 questions.
- The Deploy templates do let you pick channels, and there's an out-of-hours template. RC3 was corrected: the gap is topics, approving replies first, a spend cap, and plan access.
- One flow in the account is Active, attached only to the Baan Samunprai test chat widget (no real customers). "Nothing went live" changed to "No real customers were involved".

**Edits:** RC1 adds the pre-connected website widget. RC2 becomes "no easy way to test it". RC3 corrected as above. RC4 now uses the re-authorisation intervals. The method box explains how the scores are built. Change 1 makes the setup home the first screen after login, then the dashboard. Every "not do" item now names its source (brief, Deploy page, pricing page, competitor review, platform docs, AI services page). Still 2 pages.
**What I did with it:** *(to fill)*

## 14 · Claude Opus 5.5 (Claude Code + Claude in Chrome) · Persona testing v2: six personas, delta only

```
please redo this with the personas_v2 - if any of the areas have already been covered off in the previous testing just reuse that in the output. Only test the delta. There should be the output across all 6 personas
```

**What the agent did:** compared `zaapi_personas_v2.md` with v1 and mapped which v2 script questions v1 had already covered (19 of 35 reused). Built two new knowledge files: a 12-page Thai FAQ PDF for Glow Lab and a Vietnamese FAQ and size chart .docx for Linh Studio. Set up two new chat widgets with their personalities and scenarios. Tested the delta in Test mode:
- Nattaya's full script plus 2 extraction probes;
- Linh's full script plus a 3-run cancellation-scenario fix loop;
- Aisha's East Malaysia questions × 3 runs, with her v2 setup (bulky guardrails temporarily off, restored afterwards);
- Jo's new defective-zipper question.

It then re-scored all six personas and redid the "do the proposals close the gaps" check.

**Key new findings:**
- The Thai PDF was about half-read ("Completed", no preview, tables shredded).
- Aisha's stale RM15 went out in 3 of 6 runs, and the self-check called one "accurate".
- Linh's cancel scenario fired 3 of 3 and resolved 0 of 3, adding false "I'm checking" replies.
- One silent no-reply.
- Zalo isn't supported.

**Outputs:** `research/persona_v2_test_log.md`, `research/persona_v2_exec_summary.md`, `research/persona_kb/glow_lab_faq.pdf` (+ .html), `research/persona_kb/linh_studio_faq_sizechart.docx`.
**What I did with it:** *(to fill)*

---

## 15 · Claude Opus 5.5 (Claude Code) · Review the Perplexity memo review and persona v2, suggest memo changes

**Prompt as sent:**

```
there is a memo review from perplexity in the folder now. also the persona walkthroughs of the product have been updated.

Review these and give suggestions on how to update and improve the memo
```

**Input read:** `memo_review.md`, `research/persona_v2_exec_summary.md`, `research/persona_v2_test_log.md`, `zaapi_personas_v2.md`, `appendix/D_brief_coverage.md`, current `memo/zaapi_memo.html`.
**Output:** suggestions in chat (which review points to accept, partly accept or push back on; what the v2 results change in each memo section; a layout plan). No memo edits yet.
**What I did with it:** *(to fill)*

---

## 16 · Claude Opus 5.5 (Claude Code + Claude in Chrome) · Memo v3: review fixes and six personas

**Prompt as sent:**

```
xx1 ok
2 yes
3 keep for now make smaller
```

(Answers to prompt 15: 1 = headline target 30+ of 100 live by day 7 and still live at day 30, and 15% → 30% AI resolution; 2 = move read-only order status to weeks 6–12; 3 = keep the photos, smaller.)

**What the agent did:** rebuilt the memo on the six v2 personas (two new Unsplash photos: Dynamic Wang, Elist Nguyen) and reframed the opening. Restructured the four causes so each quote maps to one, moved the 71 → 38 point to the authoring cause, and softened the Basic/Flow Builder claim. Led section 4 with the one bet. Added "what it read", 3× readiness runs, handoff controls, the reply check and read-only order status. Moved the tiers to page 2 with Kit-as-upgrade framing. Phases are now 0–2 / 2–6 / 6–12 / later. Rewrote the slider item to acknowledge Aisha. Fixed the targets and guardrail baselines, and put the evidence-bias caveat in the footer. Still 2 pages. Previous version kept as `memo/memo_draft_v2_backup.html`.
**What I did with it:** *(to fill)*

---

## 17 · Claude Opus 5.5 (Claude Code) · Fix the persona testing commentary

**Prompt as sent:**

```
the testing commentary doesn't make sense e.g. why high scores don't launch and have high scores despite issues. and why the ones who launch have bad agents
```

**What the agent found:** the cards and the takeaway disagreed. The takeaway named Jo as a launcher while her card said she was stuck. Budi (68, never launched) scored below Aisha (70, went live), so "the ones who launch have bad agents" didn't hold.
**What changed:** launch status now comes from the brief's quotes: only Kuala Lumpur and Ho Chi Minh City went live, the other four didn't. Each card has a "Didn't launch" or "Went live, then off" tag. The method line explains what a score means. The takeaway is now "Agent quality and launch decisions didn't line up: the best agent (89) never launched because its owner couldn't see it was good; the weakest (53) went live because nothing warned her." Still 2 pages.
**What I did with it:** *(to fill)*

---

## 18 · Claude Opus 5.5 (Claude Code + Claude in Chrome) · Prototype plan, context pack and build prompt

**Prompt as sent:**

```
yes lets make it to include the optional uplift for line (and include it in the higher tier AI package). For the prototype include them all but front load the highest impact (have an impact score on each)

Let's have a prompt I can start a new chat using that's still attached to the project.

Please give me a comprehensive prompt for the protype, confirm with me any objectives and outputs to be created and if needed have a folder with context MDs to maximise the prototype chance of success which the prompt will call on.
```

Confirmed with me: order by impact score, with Aisha flagged as showing the most features; embed the six Unsplash photos; outputs are the self-contained HTML, a README with demo script, and a private web link.
**What the agent did:**
- Memo: the LINE one-month export added to the AI Success Kit; WhatsApp 180-day history added to weeks 2–6; the prototype line updated. Still 2 pages.
- Appendix C: added a history addendum.
- Wrote `prototype/context/` (00–06: goal and scope, flow and screens, merchant data, impact scoring, build rules, acceptance checklist).
- Wrote `prompts/prototype_session_prompt.md` for the build session.
**What I did with it:** *(to fill)*

---

## 18b · Claude Opus 5.5 (Claude Code) · Aisha's conflict flow and presenter sidebar

**Prompt as sent:**

```
i think we should also include a way to resolve aisha's conflict, any ideas?

additionally we should have a running side bar which explains the changes and impact. it should be QC for aI language and use my tone of voice.
```

**What the agent did:**
- Proposed a six-part conflict flow: stakes, pick or ask a teammate, fill the gap, which source wins, fix at the source, quick re-test. Wrote it into `prototype/context/02` and `03`.
- Wrote `prototype/context/07_sidebar_copy.md`: the sidebar layout, all sidebar text (today / the change / why / should move, per screen and per merchant), and the 10-change running tracker.
- Language QC: banned-phrase grep clean; sentences cut to about 20 words.
- Updated the build rules, checklist and `prompts/prototype_session_prompt.md`.
**What I did with it:** *(to fill)*

---

## 18c · Claude Opus 5.5 (Claude Code) · Design brief for Google Stitch

**Prompt as sent:**

```
ok i'm going to try using google stitch first through the MCP to create the UI and designs. we should look to make it more intuitive than the existing design. Please create a design MD to use with stitch
```

**What the agent did:** wrote `prototype/stitch/DESIGN.md`:
- context and users;
- design goals mapping today's problems to principles (e.g. review not write, say what happened in words, one primary action, readable 14px base);
- visual language based on Zaapi's tokens but larger and calmer;
- layout and 16 components;
- the plain-words table;
- 12 ready-to-paste screen prompts using Aisha's real content (plus Pranee's guided questions and the Kit panel);
- don'ts and hand-off.

Language check: no banned phrases.
**What I did with it:** *(to fill)*

---

## 18d · Claude Opus 5.5 (Claude Code + Google Stitch MCP, Gemini 3.8 Flash) · Stitch designs from DESIGN.md

**Prompt as sent:**

```
using the files for stitch in the zaapi folder, most importantly the design.md please use the MCP to google stitch to create uplifted intuitive designs from the spec. We should be looking to ensure users find it as easy as possible to use the new functionality.
```

(Follow-up after a dropped connection: "Try again".)

**What the agent did:**
- Created the Stitch project "Zaapi AI Agent setup" and a design system from DESIGN.md sections 1–7 and 9 (Inter, teal #00A892, purple #5E40E1, 8px radius, type scale).
- Generated 13 screens, one prompt each. It started from DESIGN.md section 8 and added ease-of-use changes:
  - "Nothing is sent to customers until you choose Go live" on home and step 1;
  - time left and "Progress saved · leave any time";
  - a sticky footer with one primary action;
  - conflicts above the file list, in a drawer with recommended answers pre-selected;
  - review progress on topics;
  - live counters while the test runs, and "you can leave this page";
  - a "fix these and you reach about 85" hint.
- Ran a Stitch edit pass for consistency. It changed the screens in Stitch but not the exports, so the same fixes were applied locally with `prototype/stitch/fix_and_render.py`, which also re-renders the PNGs at 1440px with headless Chrome. Originals are in `prototype/stitch/original/`.
- Removed copy Stitch made up and we can't support: "256-bit encryption", trend badges, "Zero disruption…", quota rules.
- Wrote `prototype/stitch/NOTES.md`: file list, fixes, 12 design decisions that differ from the context pack, and placeholder content to replace.

**What I did with it:** *(to fill)*

---

## 18e · Claude Opus 5.5 (Claude Code + Claude in Chrome) · Full left rail in the Stitch designs

**Prompt as sent:**

```
the left navigation bar doesn't have all the options that the existing site has, we don't need to replicate the pages but it shouldn't look like functionality removed. you can check the left bar through claude chrome connection if needed.
```

**What the agent did:**
- Read the live rail in the trial account in Chrome, via the buttons' aria-labels. Top to bottom:
  - Store, Toggle sidebar (⌘B), Notifications, Search;
  - Tickets, AI Agent, Analytics, Automations, Broadcast, Contacts, Settings;
  - Live Chat Support.
  - The sidebar toggle opens the AI Agent sub-menu: Train, Launch, Monitor.
- Put that full rail on all 13 screens with `fix_and_render.py`. The seven sections have labels; the utility icons stay icon-only, as today. The AI Agent sub-menu shows as collapsed, and "Inbox" became "Tickets".
- Corrected the nav item list in `stitch/DESIGN.md` (section 5, screen 1 prompt), `context/02_flow_and_screens.md` and the Stitch design system, so future screens and the build match.
- Updated `stitch/NOTES.md`.

**What I did with it:** *(to fill)*

---

## 19 · Claude Opus 5.5 (Claude Code, desktop app) · Prototype build

**Prompt as sent:**

```
please run the prototype session prompt from the file, using all the designs brought in from stitch
```

The prompt it ran, from `prompts/prototype_session_prompt.md`:

```
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
```

**What the agent did:**
- Read the context pack (00–07), `stitch/NOTES.md` and `DESIGN.md` sections 4–6, and all 13 Stitch PNGs. Then gave a short plan and built without stopping.
- Downloaded the six approved Unsplash photos at 160×160 into `prototype/assets/`, and embedded them as base64.
- Built `prototype/zaapi_setup_prototype.html`: one file of about 295 KB, with hand-written CSS and plain JS, and no network requests.
  - All merchant content is in one `MERCHANTS` block, and all sidebar text in one `SIDEBAR` block, word for word from `07_sidebar_copy.md`.
  - It has the real app's 12-item rail, the setup home that becomes a dashboard, all 7 steps and Aisha's six-part conflict drawer.
  - Also Pranee's guided questions, the Kit panel, the switcher ordered by impact, demo shortcuts, per-merchant reset and the presenter tracker.
- **Stitch decisions:** adopted all 12, with real numbers in place of the placeholders (7 facts for Aisha, "about 88"). Dropped the "Weekly performance check" card, and replaced every piece of content Stitch invented.
- **Readiness:** moves only as fixes are applied. A re-run after every fix gives each merchant's "after" score. The by-topic split is derived from the totals and labelled demo data.
- **Checks:**
  - Clicked every merchant through every step in the browser pane, through the real buttons: all six reached their "after" score (Jo 92, Nattaya 96, Aisha 88, Linh 81, Budi 86, Pranee 90), with zero console errors.
  - The network log showed only the HTML file.
  - Compared screenshots at 1440×900 with each Stitch PNG, and checked 1280×800 and 1024.
  - The banned-phrase grep on the whole file returned no matches. The one em dash is Linh's verbatim quote.
- Wrote `prototype/README.md`: how to open it, what's simulated, a 2-minute click path per merchant (Aisha first), the decisions and changes from Stitch, the checks run, and photo credits.
- Published a private Artifact: https://claude.ai/artifact/Phpqmhaiv2d9dmMaLwmqjM
- **For Mike to check:** the Thai strings on Pranee's setup home and guided questions are Claude's own, and need a Thai speaker's check.

**What I did with it:** *(to fill)*

---

## 20 · Claude Opus 5.5 (Claude Code + built-in browser) · Check the prototype against the memo

**Prompt as sent:**

```
ok can you now look at the prototype created and match that up to the memo. Any issues to call out?
```

**What the agent did:** read `prototype/README.md` and the data in the HTML. It clicked through Aisha's path (all 7 steps, the test run, go live, week one) and grepped the file for each claim in the memo.

**Main findings:**
1. Week-one numbers are 4–10× too high for each merchant's monthly volume and launch share. This came from `03_merchants.md`.
2. Week one doesn't link to the memo's value target (15% in 30 days).
3. Order status appears in a launch that the memo sequences as weeks 6–12.
4. The readiness test doesn't mention the rewordings the memo describes.
5. The "before" readiness score treats order-status answers as correct.
6. "Basic plan included" isn't shown.
7. The Thai strings are unchecked.

No edits made.
**What I did with it:** *(to fill)*

---

## 20b · Claude Opus 5.5 (Claude Code) · Fix prompt for the prototype session

**Prompt as sent:**

```
ok give me a complete prompt for the fixes as i'll use that in the prototype session
```

**What the agent did:**
- Wrote `prompts/prototype_fixes_prompt.md`.
- It fixes entry 20's findings in both `03_merchants.md` and the HTML. While doing the maths, it found that the step 1 channel counts also didn't add up to the monthly totals, so it rebuilt all the numbers from one method:
  - weekly = monthly ÷ 4.3;
  - handled = weekly on the live channel × the go-live estimate.
- Sanity-checked with a script: monthly totals are within 3%, and each value line matches the handled and resolved figures.
- The prototype session logs as entry 21.
**What I did with it:** *(to fill)*

---

## 21 · Claude Opus 5.5 (Claude Code, desktop app) · Prototype fixes after the memo check

**Prompt as sent:**

```
please read the prototype fixes prompt and resolve.
```

The prompt it ran, from `prompts/prototype_fixes_prompt.md`:

```
I've checked the prototype against the memo. Please fix the issues below in **both** `prototype/context/03_merchants.md` (the source of truth, so a rebuild doesn't bring the errors back) and `prototype/zaapi_setup_prototype.html`. Then re-verify, update the README, and republish to the **same** Artifact URL.

Read `prompts/prompt_log.md` entry 20 for the background. Don't change the memo, the sidebar copy (`07_sidebar_copy.md`) or anything not listed here. Keep every other number as it is.

## 1. Make the chat numbers add up

Two problems. Step 1 chat counts don't add up to each merchant's monthly total. Week-one numbers are 4–10× what the monthly volume and the go-live estimate allow.

**Method, so it stays consistent:**
- weekly chats = monthly ÷ 4.3;
- handled in week one = weekly chats on the live channel(s) × the go-live estimate;
- resolved = handled × the week-one resolution rate;
- passed on = handled − resolved.

Keep each merchant's existing go-live estimate and resolution rate. Use these numbers exactly.

**Step 1: chats found per channel**

| Merchant | Channel counts (replace the current ones) | Monthly total shown |
|---|---|---|
| Jo | Instagram 480 and Facebook 360, both 90 days (unchanged) | about 280 (unchanged) |
| Nattaya | **LINE 790** (18 days since connecting), **Shopee 1,800**, **TikTok Shop 1,080**, **Instagram 360** (all 90 days) | about 2,400 (unchanged) |
| Aisha | **WhatsApp 15,300** (last 6 months), Shopee 2,610, Lazada 1,140, Instagram 220 (90 days, unchanged) | about 3,900 (unchanged) |
| Linh | **Facebook 2,570**, **Shopee 1,430**, **TikTok Shop 1,140** (90 days); Zalo not supported | **about 1,700** (was 1,900: update the tier line and plan card; still 300+) |
| Budi | Shopee 11,300, TikTok Shop 5,800, Lazada 1,900 (90 days, unchanged) | about 6,500 (unchanged) |
| Pranee | **LINE 270** (12 days since connecting), Facebook 640 and Shopee 120 (90 days, unchanged) | about 900 (unchanged) |

**Step 7: week one**

| Merchant | Live on | Weekly chats there | Go-live estimate | Handled | Resolved | Passed on | Other week-one figures |
|---|---|---|---|---|---|---|---|
| Jo | Instagram + Facebook | ~65 | 41% | **27** | **17** (64%) | **10** | 2 flagged; "Blocked 3 replies that claimed stock"; **"108 of your 300 free messages used"** (was 212) |
| Nattaya | LINE, out of hours | ~307 | 22% | **68** | **48** (71%) | **20** | 3 flagged |
| Aisha | WhatsApp, out of hours | ~590 | 24% | **140** | **81** (58%) | **59** | **"128 replies approved as-is · 12 edited"** (approve-first is on, so approved + edited must equal handled); 0 East Malaysia rate errors; 2 flagged |
| Linh | Facebook | ~200 | 33% | **66** | **34** (52%) | **32** | **"6 cancel requests passed on, button ready"** (was 23); reply check blocked **4** "I'm checking" replies (was 11) |
| Budi | Shopee, out of hours, 11.11 week (about 3× a normal week) | ~2,630 | 18% | **470** | **287** (61%) | **183** | 0 stock claims; Shopee response rate 96% (demo) |
| Pranee | LINE, evenings and night | ~157 | 35% | **55** | **37** (68%) | **18** | **"12 dosage questions answered"** (was 74); 0 medical claims |

Mark all of these as demo data, as now.

## 2. Link week one to the memo's value measure

The memo measures "share of enquiries the AI resolves with no human" on the channels where it's live. The first-month target is 15%.

Add one line to each merchant's week-one screen, directly under the stat cards, styled as a quiet info line (not a new card):

| Merchant | Line to add |
|---|---|
| Jo | "About 26% of all your Instagram and Facebook chats were resolved by AI this week. First-month target: 15%." |
| Nattaya | "About 16% of all your LINE chats were resolved by AI this week. First-month target: 15%." |
| Aisha | "About 14% of all your WhatsApp chats were resolved by AI this week. First-month target: 15%." |
| Linh | "About 17% of all your Facebook chats were resolved by AI this week. First-month target: 15%." |
| Budi | "About 11% of all your Shopee chats were resolved by AI during 11.11, out of hours only. First-month target: 15%." |
| Pranee | "About 24% of all your LINE chats were resolved by AI this week. First-month target: 15%." |

Mirror the same figure on each merchant's dashboard in one short line.

## 3. Order status is weeks 6–12 in the memo

The memo schedules read-only order status for weeks 6–12. The prototype currently shows it working at launch.

- **Label:** change every "Projected" chip that relates to order status to **"Projected · weeks 6–12"**.
  - Aisha: "Where's my order".
  - Linh: the cancel topic and the order status toggle.
  - Anywhere else it appears.
- **Aisha, step 3 sample reply:**
  - Replace the tracking-link reply with what the agent does *until* order status arrives: "Thanks. I've passed order RK10233 to our team, and they'll reply with the tracking details shortly."
  - Add a small line under it: "With order status (weeks 6–12): shares the status and tracking link from Shopee or Lazada."
- **Aisha, step 6:** "Where's my order" stays on, but its row description says it passes the order number to the CS team until order status is available.
- **Linh** keeps her projected order-status toggle and projected "after" score (81), as now, with the new chip wording.

## 4. The readiness "before" score assumes order status works

Aisha's by-topic table currently counts "Where's my order" as 31 of 47 correct. Today's agent can't see orders, so these questions are handed off.

- **Before and after runs, for every merchant whose order-status toggle isn't on:** count order-status questions as **"Passed to your team"** (a correct handoff), not "Correct".
- **Topic sizes:** each topic's question count should follow its share of chats. For Aisha's 120 questions: Where's my order 37, Shipping 20, Damaged/returns 13, Sizing 11, Vouchers 8, COD 6, and the remaining 25 spread across the undrafted topics or shown as "Other".
- **Headline stays the same:** the overall percentages and the score (61/27/12, score 70; after 88) don't change. Rebalance the split across the other topics so the totals still match.
- Keep the "Demo data: split from the totals above" label.

## 5. Readiness mentions rewordings

The memo says the test "replays real past questions, three times each with rewordings". Update the step 5 intro and the run line for every merchant:
- intro: "We'll replay 120 real questions from your last 90 days, 3 times each, with rewordings";
- run line: "Run 1 · 120 real questions, 3 times each with rewordings".

Use each merchant's own question count. Pranee's standard-set wording also gets "with rewordings".

## 6. Show that the free setup is on every plan, including Basic

Add "Free on every plan, including Basic." to the plan card on the setup home, as the second line, for every merchant. In the AI Success Kit panel's "Free setup" column, add "Every plan, including Basic." The Kit's own "Pro or Advanced, 300+ chats a month" wording stays as it is.

## 7. Thai text to check

Don't change the Thai. Add a README section, "Thai to check before the interview": a table of every Thai string in the file, with the English it's meant to say and where it appears (screen and element). I'll get a Thai speaker to check it.

## Checks (report each in your final message)

1. **Consistency check:** for each merchant, recompute and show in a small table: monthly total ≈ sum of step 1 channel counts (90-day counts ÷ 3, 6-month count ÷ 6, and the LINE days scaled to a month). Also check week-one handled ≈ weekly chats on the live channel × go-live estimate. Every row should be within 10%.
2. **Aisha's step 7:** approved as-is + edited = handled (128 + 12 = 140).
3. **Click-through:** all six merchants, all steps, including the test run, every Fix, the re-run, go live, week one and the dashboard. No console errors, and no network requests apart from the HTML file.
4. **Banned-phrase grep** from `07_sidebar_copy.md` on the whole file: report the command and the result.
5. **Order status:** grep that every order-status "Projected" chip now reads "Projected · weeks 6–12".
6. **Screenshots:** Aisha's steps 3, 5 and 7 at 1440×900.

## Outputs

- `prototype/context/03_merchants.md` updated with the new numbers and wording.
- `prototype/zaapi_setup_prototype.html` fixed.
- `prototype/README.md` updated:
  - the demo-data section with the new numbers;
  - a "Fixes after the memo check (entry 21)" list;
  - the new "Thai to check before the interview" table.
- Republished to the **same** private Artifact URL as before (`https://claude.ai/artifact/Phpqmhaiv2d9dmMaLwmqjM`). Report it.
- Prompt log entry **21** in `prompts/prompt_log.md`, in the existing format, with this prompt copied in.
```

**What the agent did:**
- Fixed all seven items in both `prototype/context/03_merchants.md` and `prototype/zaapi_setup_prototype.html`:
  - step 1 and week-one numbers from the stated method;
  - the value line under week one and on the dashboard;
  - "Projected · weeks 6–12" on every order-status chip, plus Aisha's new sample reply and step 6 row;
  - the readiness by-topic split rebuilt (order-status questions passed on, counts by share, "Other" row, headline unchanged);
  - "with rewordings" on the intro, running screen and run line;
  - "Free on every plan, including Basic." on the plan card and in the Kit panel;
  - a README table of every Thai string.
- **Also changed:**
  - Aisha's drafted "Where's my order" rule no longer claims to share order status before weeks 6–12;
  - her "Order dah ship ke?" test question now shows as passed on;
  - Linh's reply-check example is labelled "Proposed", not "Projected", as it isn't order status.
- **Conflict found:** Aisha's 27% handoff rate is 32 of 120 questions, but "Where's my order" has 37. The headline was kept, so 32 are handoffs and 5 count as general delivery questions answered. Noted in the README and in `03_merchants.md`.
- **Checks:**
  1. Step 1 counts are within 3% of each monthly total, and week-one handled figures within 2%.
  2. Aisha: 128 + 12 = 140.
  3. All six merchants were clicked through every step in the browser pane with no console errors. Only the HTML file was requested.
  4. Banned-phrase grep: 0 matches.
  5. Every order-status chip reads "Projected · weeks 6–12".
  6. Screenshots of Aisha's steps 3, 5 and 7 at 1440×900.
- Updated the README: demo-data numbers, "Fixes after the memo check (entry 21)", "Thai to check before the interview", and the re-run checks.
- Republished to the same private Artifact, version 2: https://claude.ai/artifact/Phpqmhaiv2d9dmMaLwmqjM

**What I did with it:** *(to fill)*

---

## 22 · Claude Opus 5.5 (Claude Code) · Final clarity sweep of the memo

**Prompt as sent:**

```
ok do one more sweep of the memo, does it all make sense easy to follow, easy to understand
```

then:

```
please resolve
```

**What the agent did:** read the whole memo as a first-time reader from Zaapi and listed 14 clarity issues, then made all of them:
- the Kit line;
- "4 (continued)" on the tiers box;
- the value measure is now "on the channels where it's live";
- the same cause names in section 2 and the change table;
- quotes for Manila and Chiang Mai, and the full Ho Chi Minh City quote;
- plain wording for step 1, tone and language, handoffs and order status;
- "ready stok" explained;
- "the Kit's own eligibility line" and "fixing a wrong answer from the answer itself";
- the weeks 0–2 and 2–6 rows;
- the date set to 28 September 2026, with "Draft" removed.

Trimmed a few phrases to keep it on 2 pages (page 1 ends at 290mm; the PDF is 2 pages).
**What I did with it:** *(to fill)*

---

## 23 · Claude Fable 5.1 (Claude Code, desktop app) · QA of every output and the master prompt list

**Prompt as sent:**

```
Please play the role of QA for the Case Study. Check all the outputs in the folder and make sure everything is resolved. Also create a master list of prompts used by claude and perplexity. Make sure the prompts read clearly, ready for submission, and you can put a count of additional interactions post the main prompts if the additional ones aren't of substance. (this is for the submission).

The perplexity prompts i actually used are included in  prompt log as PX
```

**What the agent did:**
- Read every file in the folder against the brief and this log. Checked the memo's numbers against the brief's funnel and quotes, and Perplexity's review points against the current memo.
- Re-rendered `memo/zaapi_memo.html` at A4 with headless Chrome and counted the PDF: 2 pages.
- Loaded `prototype/zaapi_setup_prototype.html` in headless Chrome: renders, no console errors. Read the published Artifact back and confirmed it carries the entry-21 fixes.
- Rewrote `prompts/master_prompts.md` as the submission version: 29 substantive prompts in order (Claude, Perplexity and Stitch), each with why, prompt and outcome, plus a counted table of 13 short follow-ups. The two persona prompts were taken from the "Prompt used" sections of `zaapi_personas.md` and `zaapi_personas_v2.md`.
- Wrote `QA_report.md`: verdict per deliverable, five things to do before sending, two things to be ready to explain, what passed, and which working files to leave out.
- Housekeeping: moved the stale root `zaapi_memo.pdf` (25 Sep) to `memo/memo_draft_v1_25sep.pdf`; updated `CLAUDE.md` and `00_plan.md`.

**Open for Mike:** the Perplexity memo-review prompt isn't recorded anywhere (placeholder left in `master_prompts.md` entry 18); the tool behind the two research files (`zaapi_ai_agent_activation_research.md`, `research/competitors/`) isn't recorded; the Thai strings are still unchecked.

**What I did with it:** *(to fill)*

**Follow-up (same session):** "ok relabel the appendix as needed. Then give me a score overall for this case study. play the role of the existing head of product at Zaapi." The memo footer now says "Detail in Appendices A–D and the prompt list, available on request"; `appendix/README.md` added as an index; PDF re-printed and re-counted (2 pages). Score given in chat.

**Follow-up (same session):** six memo edits proposed one by one and approved: (1) sequencing rows "Now · weeks 0–2 / Next · weeks 2–6 / Then · weeks 6–12 / Later", When column 22mm; (2) "The order matters more than the dates, which assume the current team." added under the table; (3) method box tightened, keeping Perplexity and Claude Code; (4) "the built-in check once passed a stale shipping rate as 'accurate'"; (5) body type 8pt → 8.2pt, which pushed the PDF to 4 pages, so reverted to 8pt as agreed; (6) the "Went live, then off" tags left as they are. PDF re-printed: 2 pages, page 1 content ends at about 287mm.

**Follow-up (same session):** "line is missing from the prototype to connect and it should be an option to connect along side others but should highlight the limitation and the cost and be used as upsell for the package." LINE Official Account added as an optional tile on step 1 for Jo, Aisha, Linh and Budi, with the limitation (chats only from the day you connect), the cost of LINE's own export (฿555 a month) and the Kit including one month of it; Nattaya's and Pranee's notes and the Kit panel now state the cost; the sidebar LINE line shows for everyone. Context pack and README updated; smoke-tested in headless Chrome; republished to the same Artifact.

**Follow-up (same session):** "make the text for the line card easier to read also on the other cards say connect it - allows you to message customers through Zaapi / we'll tell you your top scenarios for AI automations / key information will be added to your knowledge base… make the upsell of the package more prominent and the saving for line if clicking it." Every unconnected tile now shows three bullets; the LINE tile has its own bullets plus a purple upsell strip ("AI Success Kit includes one month of LINE history. Saves ฿555." with a See the Kit button); opening the Kit from LINE shows a saving banner and the LINE row has a "Saves ฿555" chip. Context pack and README updated; smoke-tested; republished (version 4).

**Follow-up (same session):** "lets move line to be the first card and whatsapp where it is now, this is in line with a SE asia focus, we should also include a gmail card." Every merchant's step 1 grid now runs LINE, WhatsApp, own channels, Gmail, website widget. WhatsApp and Gmail are optional tiles where they aren't the merchant's channel, with their own bullets (6 months of chats; 7 days of email). Context pack and README updated; smoke-tested; republished (version 5).

**Follow-up (same session):** "for the knowledge base shouldn't we say upload files or if you have none there will be some guided questions or the AI can make a first attempt from the connections (up to restrictions on account)." Step 2 now opens with a "Three ways to teach your agent" row (upload files; answer a few questions; let Zaapi draft it, with the plan limit by tier), the applicable route highlighted per merchant. The setup home's step 2 line matches, with a Thai version for Pranee. Context pack and README updated; smoke-tested; republished (version 6).

**Follow-up (same session):** "for the master prompts file please can you make sure the prompts sound like i've given my own thinking etc and they're written more like my style." The framing around every prompt in `master_prompts.md` was rewritten in Mike's voice: each entry now opens with "What I wanted" (the thinking behind the ask, and what was Mike's own call) and closes with "What I did with it". The intro gained a "How I split the work" section. The prompts themselves are unchanged, verbatim as sent, checked by comparing every code block with the previous version.

**Follow-up (same session):** "can we publish this to my github repo under Zaapi. There should be a good readme file and clear labelling of everything and directories as needed." Root `README.md` written; the brief moved to `brief/`; the memo renamed `memo/zaapi_memo.pdf` and `.html` with every reference updated; a `.gitignore` for working files and the Stitch export folders; this log annotated as the raw record. Homebrew and the GitHub CLI installed and Mike signed in. Pushed to https://github.com/mikerth9/Zaapi (private), merging the repo's starter README.

**Follow-up (new session, 28 Sep):** "ok do one last review read it through the github connection for zaapi." The repo was read back from github.com with the GitHub CLI: tree, head commit, README, memo PDF (2 pages), prompt list, prototype README, and a tarball grep for placeholders, secrets and personal data. Found: the entry-18 placeholder, a table reference to the excluded `QA_report.md`, and the memo footer's "available on request". Then: "just remove it and renumber. rely on the HTML. Adjust the about line." Entry 18 (the Perplexity memo review, prompt never recorded) removed from `master_prompts.md` and entries 19–28 renumbered 18–27 with cross-references and totals updated (28 prompts: 20 Claude, 7 Perplexity, 1 Stitch); `memo_review.md` stays in the folder. The Artifact link removed from `prototype/README.md`, so the HTML file is the only way to open the prototype. Repo About line set. Score given in chat.
