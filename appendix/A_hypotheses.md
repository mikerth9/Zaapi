# Appendix A — Hypotheses, tested against the product (v3)

*v2 was written before signing up. v3 tests each hypothesis against two walkthroughs and Zaapi's public pricing. What held up is marked confirmed, what didn't is killed or revised, and what a walkthrough can't test stays open. v2 is kept as `A_hypotheses_v2.md`.*

**Source tags.** *Brief* = the take-home (fictional numbers, treated as real). `[product]` = seen on screen in my walkthrough, 25 Sep 2026 (`research/walkthrough_log.md`). `[mike]` = Mike's own separate walkthrough, same day (log, Addendum A). `[help]` = help.zaapi.com. `[pricing]` = zaapi.com/en-sg/pricing, read 25 Sep 2026 (log, Addendum B). `[persona]` = the four personas' full test scripts, run against realistic knowledge for each business (`research/persona_test_log.md`). `[inference]` = reasoning, not observed. `[ext]` = outside knowledge, still to verify in Perplexity.

**Limits of this evidence.** Two people, one day, no real customer traffic. The persona tests use knowledge I wrote to match each persona file's description, not real merchants' content. My first agent used the best-case content (Fresh Laundry, everything written down); all agents used chat widgets only; I didn't connect a marketplace or messaging channel, publish a flow, or reach the end of the trial. None of this measures elapsed time, so anything about delay or procrastination stays open.

## Current best guess

Once it's set up, the product works better than the funnel suggests. With a well-written knowledge base, two scenarios and a personality, the agent answered 10 of 10 test messages correctly, in Thai and Bahasa as well as English, and handed off every case it should have `[product]`. The problem is getting there and staying there. Nothing leads a new merchant from signup to AI setup: they land in the inbox, the help centre's start guide has no AI step, and the onboarding QR test pulls them out of setup `[product]` `[mike]` `[help]`. Setup itself is three unordered tabs with no measure of progress or readiness, and failures are silent or mislabelled `[product]`. Going live is a separate, all-or-nothing choice made in Flow Builder, a tool built for a different user and missing from the Basic plan, and every AI reply after the trial's free 300 is paid for `[product]` `[pricing]`. So a merchant who starts still can't tell when to stop testing, can't launch small, and can't cap the cost. The brief's share-of-conversations dial doesn't exist. Two of my beliefs didn't survive: file format isn't the barrier (PDFs and plain FAQs load fine), and the agent picks the customer's language without being told. The sharpest new question is whether the 72-hour switch-offs are trust breaking, or the free messages running out.

The persona tests add the realistic picture `[persona]`. With the thin knowledge real merchants have, the agent stayed safe: no medical claims, no invented vouchers, no agreed compensation, even with no rules set. But it stated canned text as fact ("ready stok"), promised actions it can't take ("I'll check the status", "I'll DM you the details"), and gave opposite answers to the same question on different runs. So one passing test proves little, and its own self-check marked a false answer "Groundedness ✓". Fixing a behaviour rule took a minute and held; fixing a fact took minutes of reprocessing, during which the agent lost that knowledge, and the fix still didn't hold.

---

## Verdicts at a glance

| # | Hypothesis (short) | v2 | v3 | Verdict | Deciding evidence |
|---|---|---|---|---|---|
| H1 | Nothing carries merchants from signup to AI setup | M | **H** | **Revised, stronger** | Land in inbox, no checklist, start guide has no AI step, QR pulls you out `[product]` `[mike]` `[help]` |
| H2 | Setup gets overtaken by the next campaign | M | M | Open | Can't be tested in a walkthrough |
| H3 | Knowledge isn't written down; thinness shows up later | H | **H** | **Revised, then confirmed** | Format sub-claim killed (PDF loads) `[product]`; thin knowledge gave confident false facts `[persona]` |
| H4 | Setup ignores the conversations Zaapi already holds | M | M | Supported | No history option anywhere in Train `[product]`; not tested with a marketplace channel |
| H5 | Scenarios look optional | M | M | Supported | Nothing prompts you to them; Test and Deploy don't check for them `[product]` |
| H6 | Scenarios are prompt engineering in a form | M | **H** | **Confirmed** | Bulky-item rule fired on a bedsheet; "hand off if…" vs "don't hand off unless…" behave very differently `[persona]` |
| H7 | Scenarios can instruct but not act | L–M | **H** | **Confirmed, refined** | Two modes only; actions need Advanced-plan webhooks `[product]` `[pricing]`; the agent promises actions it can't take `[persona]` |
| H8 | Merchants can't tell when it's ready | H | H | **Confirmed, stronger** | No coverage view; same question gives different answers; self-check passes false answers `[product]` `[persona]` |
| H9 | Going live is all-or-nothing | M | **H** | **Confirmed, sharpened** | Two templates, no share dial; narrowing needs Flow Builder `[product]` `[pricing]` `[mike]` |
| H10 | Switching off is easier than fixing | M | M | **Supported for facts** | Fixing a fact: minutes of reprocessing, agent degraded meanwhile, held 1 of 3; fixing a rule: instant `[persona]` |
| H11 | Language is set by the merchant, not the customer | M | M | **Original killed, revised** | Agent matched Thai and Bahasa unprompted `[product]`; code-switching and Thai gender forms need explicit rules `[persona]`; setup screens' language uncontrollable `[mike]` |
| H12 | Marketplace merchants sit where the product reaches least | M | **H** | **Confirmed** | Shopee URL warned, accepted, failed with the wrong error `[product]` |
| H13 | SMBs are doing a services job alone | M | **H** | Supported | Zaapi sells setup as a service; consultation is Enterprise-only `[pricing]` |
| H14 | **New.** Going live is an uncapped spending decision | — | M | New | AI tokens sold separately; launch options are all-or-nothing `[pricing]` `[product]` |

---

## 1. The funnel, re-read

| Step (brief order) | Reached | Of previous row | Lost | Of 100 |
|---|---|---|---|---|
| Connected ≥1 channel | 94 | — | 6 | 94% |
| Added any knowledge | 79 | 84% | 15 | 79% |
| Set a persona | 71 | 90% | 8 | 71% |
| **Wrote ≥1 scenario** | **38** | **54%** | **33** | 38% |
| Ran ≥1 test conversation | 66 | *174% (rises)* | +28 | 66% |
| Went live on any channel | 61 | 92% of testers* | 5 | 61% |
| Still live at 30 days | 52 | 85% | 9 | 52% |

\* Only if everyone who went live had tested.

**What the walkthroughs added to the observations:**

- **O1 · It's not a sequence. Confirmed.** Train is three tabs (Knowledge Source, Scenario Handling, Personality), then Test and Deploy, with no order, no progress and no "next step" anywhere `[product]`. The brief's persona-before-scenarios order doesn't exist on screen.
- **O3 · The denominator. Sharper.** The website chat widget is **already connected on every new account**, with no action taken `[product]`. If it counts towards "connected ≥1 channel", the 94 includes merchants who did nothing.
- **O4 · The 4-day first step is probably a Helpdesk number. Supported.** The post-signup modal asks for your name, team size and a channel, and never mentions AI `[product]`. You land in the inbox `[product]` `[mike]`, and the start guide's six steps are all Helpdesk `[help]`.
- **O6 · The trial ends before the median go-live. Sharper.** "Free trial ends in 6 days" and a "Subscribe now" button appear on the first screen after signup `[product]`. AI replies are also metered: 300 free, then paid `[pricing]` (H14).
- **O7 · Loss after launch is sudden. New alternative.** A merchant with a few hundred chats a day could use the 300 free replies in a day or two `[inference]`. Some "switch-offs" within 72 hours may be credits running out, not trust breaking. Needs data (question 10).

---

## 2. Hypotheses

Confidence: **H** = several independent signals · **M** = one clear signal and a plausible mechanism · **L** = inference only.

### A. Never starting (39 never go live · 4-day median to first step)

**H1 · Nothing in the product carries a new merchant from signup to AI setup, so starting depends on their own initiative, and it gets put off.** · **H** *(revised; v2: "setup looks like a project, so merchants put it off")*
- *Evidence:* Signup lands in the inbox, not in AI setup `[product]`. No dashboard, steps left, or nudge on what to do next `[mike]`. The onboarding modal is Helpdesk-only and never mentions AI `[product]`. The quick setup is gone and the help centre's start guide has no AI step `[mike]` `[help]`. Scanning the onboarding QR code takes you straight out of the connect-a-channel step, so the moment of interest is lost `[mike]`. Inside AI Agent there's no checklist or progress `[product]`. Meanwhile the trial countdown starts on screen one `[product]`.
- *What's left of v2:* the "looks like a project" half still stands. Active build time for the best case was 60–90 minutes, against the brief's "half an hour" `[product]`. But the stronger finding is that nothing starts the project for you.
- *Why H:* my run, Mike's separate run and the help centre agree.
- *Wrong if:* merchants who start AI setup on day 0 go live no faster than others, or most first AI actions come from a Zaapi email or account manager rather than in-product.
- *Test:* data on time to first AI action by entry route (in-app, email, CSM); active minutes vs elapsed days.

**H2 · Setup takes longer than the run-up to the next campaign, so it gets overtaken by it.** · **M** `[ext]` · *Open*
- *Walkthrough:* nothing to test. The 60–90 minutes of active build time `[product]` would be several sessions for Budi (20–30 minutes at a time, on his phone), which makes the mechanism plausible `[inference]`.
- *Wrong if / test:* unchanged from v2 (activation by days from signup to the next campaign peak; PX-02).

### B. Stalling mid-setup (scenarios: 71 → 38)

**H3 · Most merchants' policies and edge cases live in people's heads, so what they upload is thin. The product accepts almost anything, so the thinness only shows up later, as wrong answers or uncertainty.** · **H** *(revised, then confirmed by the persona tests)*
- *Persona tests* `[persona]`: both halves of "wrong answers or uncertainty" showed up.
  - Budi's 20 pasted quick replies turned "Ready stok kak" (a canned line) into "saat ini ready stok ya… langsung checkout" in 4 of 5 runs.
  - Pranee's product blurbs had no dosage, so her most-asked question went to a human every time.
  - Joanna's cancel rule lived only in her head, so the agent cited "No Returns" and handed off: the Ho Chi Minh City quote, reproduced.
  - None of this is flagged at upload: every source showed "Completed".
- *Killed:* "what does exist is in the wrong format." The upload screen says it accepts only .txt, .csv, .docx and .xlsx, but a PDF loaded fine (1,474 characters), as did an unstructured "Q: A:" text file (1,468) `[product]`. Format isn't the gate; the copy is simply out of date.
- *Still standing:* the brief's quotes (Manila, Bangkok). The product tells you twice that headings matter ("organize the text using proper headings (like H1, H2)") but never checks or warns when content has none `[product]`.
- *Partly tested:* the persona runs show thin, unstructured content producing confident errors (above). A clean comparison of the same content with and without headings wasn't run.
- *Wrong if:* knowledge added by merchants who stall is about as large and well structured as that of merchants who stay live.
- *Test:* data on knowledge size, source type and structure at go-live vs stall; a second walkthrough comparing answers from the plain FAQ and the structured file.

**H4 · Zaapi holds real conversations for some channels, and setup doesn't use them.** · **M** · *Supported*
- *Evidence:* no "learn from past chats" option anywhere in Knowledge Source, Scenario Handling or Personality `[product]`. Sources are files, websites, typed text, or a "Quick replies" row added by the system.
- *Why still M:* I didn't connect a Shopee, Lazada or TikTok Shop account, so I couldn't see whether imported history is offered once it exists.
- *Wrong if / test:* unchanged from v2.

**H5 · Merchants treat scenarios as optional because nothing shows what breaks without them.** · **M** · *Supported*
- *Evidence:* the Scenario Handling tab opens on an empty table with a help link and nothing else `[product]`. Test and Deploy never check whether any scenarios exist `[product]`. Templates are one click away (Check order status, Return or refund, Customer complaint), so it isn't a blank page `[product]`. The agent also handled an angry customer well with no scenario at all `[product]`, which makes skipping them look safe.
- *Wrong if / test:* unchanged from v2.

**H6 · Writing a scenario is prompt engineering disguised as a form.** · **M** · *Supported*
- *Evidence:* the trigger is free text ("Describe the scenario… Think about what the customer might say") `[product]`. A compound rule like Aisha's "East Malaysia and a bulky item" has nowhere to go but prose. What happens only loosely follows what you write: my "Cancel after pickup" scenario handed off immediately, although I'd told it to hand off only if the customer pushed back, and the angry-customer handoff fired with "no relevant scenario was found" `[product]`. The only way to see the link between what you wrote and what happened is to open "Show thinking" on one message at a time.
- *Persona tests* `[persona]`: Aisha's "East Malaysia bulky item" rule fired on a question about a *bedsheet* to Kuching, and the model generalised it to "we do not quote shipping for these regions", blocking a question her own shipping sheet could answer. Phrasing changes behaviour a lot: scenarios that said "hand off *if* they push back" handed off on the first message (Aisha, Fresh Laundry), while "**do not** hand off unless the item is defective or the customer is angry" held (Joanna). Nothing in the form tells a merchant which phrasing does what.
- *Wrong if / test:* unchanged from v2.

**H7 · Scenarios can instruct or escalate but not act. Order actions exist only through Advanced-plan webhooks and marketplace triggers, which need a technical build.** · **H** *(confirmed and refined; up from L–M)*
- *Evidence:* a scenario's response is "Follow instructions" or "Escalate to a human agent immediately", nothing else `[product]`. The refund template's steps are all things to say ("ask for the order number", "provide a return label") `[product]`. Choosing "Escalate" replaces your instructions with a fixed line, "The AI Agent will send a message informing the customer that their ticket is being escalated", so Fresh Laundry's required wording ("someone will reply within 30 minutes") can't be set `[product]`. Webhook and HTTP actions and marketplace order triggers exist, but only on Advanced ($134/month) `[pricing]`.
- *Persona tests* `[persona]`: the agent doesn't know its own limits. With no way to act, it still *promises* to: "Para po ma-check ko agad ang status" (Joanna), "yung details isesend ko rin po sa DM mo" (Joanna), "saya akan cek ketersediaan" (Budi), "ยังไม่พบข้อมูลคำสั่งซื้อของลูกค้าในระบบ" (we haven't found your order in the system; Pranee). None of these handed off, so the customer waits for an action that never happens. That's worse than a clean handoff.
- *Wrong if:* Advanced merchants' agents close cancel or refund requests without a human at clearly higher rates, and without custom builds by Zaapi.
- *Test:* data on escalation intents by plan; PX-01 on what marketplace APIs allow.

### C. Not knowing if it's ready, then pulling it after launch (9 of 61 switch off, mostly < 72h)

**H8 · Merchants can't tell when the agent is ready, so testing is for show.** · **H** · *Confirmed*
- *Evidence:*
  - No coverage or readiness view anywhere: not in Knowledge Source, Scenario Handling, Test or Deploy `[product]`.
  - "Show thinking" is better than the docs suggest (a three-step trace: scenario retrieval, the instruction it wrote itself, and relevance and groundedness checks), but it's one message at a time, with no roll-up `[product]`.
  - Knowledge loading gives no progress or estimate: 1–2 minutes for an 11,706-character file, 8–9 minutes for 1,400-character ones `[product]`.
  - A Shopee URL, which the screen warns against, is accepted anyway and fails nine minutes later with an error about character limits: "It might be that the characters exceeds the maximum limit allowed… you could try uploading it again" `[product]`.
  - The test screen mixes English and Thai and can't be switched `[mike]`.
  - **The same question gives different answers.** Budi's stock question, same knowledge, five runs: "ready stok" 4 times, a handoff once `[persona]`. One passing test tells a merchant little, and nothing suggests re-running.
  - **The self-check passes false answers.** The false stock claim was marked "Answer relevance ✓ · Groundedness ✓ · No issues found", because groundedness is checked against the knowledge, not reality `[persona]`.
  - **The Kuala Lumpur failure, nearly reproduced.** With one guardrail off, Aisha's agent drafted "a flat rate of RM15" to Kuching (the stale figure) and the check marked it "Groundedness ✓". Only her personality rule stopped it. With no guardrails, it usually gave the right RM18, but once exposed "an inconsistency in our current information" and an internal name to the customer `[persona]`.
  - **Which source wins is left to retrieval.** Aisha's 7-day (stale macro) and 14-day (website) return policies were both loaded; the answer depended on which chunk retrieval surfaced, with no conflict warning `[persona]`.
  - Test mode takes no images (payment slips, label photos), and the first message after switching accounts was dropped in 3 of 3 cases `[persona]`.
- *Wrong if / test:* unchanged from v2.

**H9 · Going live sends everything to the AI at once, and the only way to narrow it is to build logic in Flow Builder, a tool made for a different user and missing from the Basic plan.** · **H** *(confirmed and sharpened)*
- *Evidence:* Deploy offers two templates, "AI handles all new tickets" and "AI handles tickets out of hours", and nothing else `[product]`. **There is no share-of-conversations control; the brief describes a feature the product doesn't have.** The template opens a Flow Builder graph (message received → Let AI reply → assign or close), and its only exits to a human are the AI's own judgement ("When AI agent cannot handle effectively") or an hour with no customer reply `[product]`. Basic has no Flow Builder or automations at all, and the free Flow Builder consultation is Enterprise-only `[pricing]`. The Flow Builder help isn't written for an SME, and nothing helps you express what you're trying to achieve `[mike]`.
- *Wrong if:* merchants who launched narrowly switch off as often as those who launched on everything, or go-live follows within a day of the last test.
- *Test:* data on launch configuration vs switch-off; time from last test to live; go-live rate by plan.

**H10 · After a public mistake, switching off is easier than fixing it.** · **M** · *Supported for facts, not for rules*
- *Walkthrough:* the only fix path offered is a generic line under each answer's reasoning, "AI can make mistakes. Response not what you expected? Train your AI", which links to the Knowledge Source list, not to the source that caused the answer `[product]`.
- *Persona fix loops* `[persona]`:
  - **Fixing a fact** (Budi's false stock): "Show thinking" does show which source was used, but the edit sends the source back to "Pending" with 0 characters for about 6–8 minutes. During that window the agent answered without Budi's knowledge and offered to "check the order in our system". After reprocessing, the fix held in 1 of 3 runs; one run now claimed the item was *out* of stock, from another canned line. Uploaded files can't be edited at all, only deleted and re-uploaded.
  - **Fixing a rule** (Joanna's cancel scenario; Pranee's voice guideline): about a minute each, effective immediately, and held on retest.
- *So:* for a wrong fact on a busy Saturday, the fix is slow, makes things briefly worse, and may not hold, while the off switch is instant. For a wrong behaviour, fixing is genuinely easy, if the merchant knows the problem is a rule and not a fact. Nothing tells them which is which.
- *Still untested:* whether an open chat appears in Analyse.

### D. Cross-cutting

**H11 · Merchants can't see or control which language the setup screens and the agent will use, so they don't trust it, even though the agent's reply language mostly works.** · **M** *(original killed, revised)*
- *Killed:* "the agent's language is set by what the merchant writes." With no language rule set and everything written in English, the agent replied in natural, polite Thai to Thai and in Bahasa to Bahasa `[product]`. v2's "wrong if" is met, so as v2 predicted, this is a reassurance problem, not a capability one.
- *What's left:*
  - The default is stated once, in small helper text on the Personality form: "(By default, the AI replies in the customer's last-used language.)" `[product]`. The form's own example rule, "Always respond in English", would override that default for a merchant who copied it.
  - Code-switched messages got plain English: Taglish ("po") and Manglish ("or not? … ah?") weren't mirrored `[product]`.
  - Persona tests `[persona]`:
    - **Informal Bahasa with "kak" came through unprompted** (Budi, 5 of 6).
    - **Taglish with "po" worked only with an explicit "Always reply in Taglish and use 'po'" in Custom guidelines** (Joanna, 7 of 7).
    - Aisha's "Mirror the customer's mix of English and Malay", written in the *style* field, was ignored: English in 9 of 9.
    - **Thai gender forms drifted:** ครับ and ผม…ค่ะ appeared for a woman-run shop until "always use ค่ะ and ดิฉัน" was added, after which it held (Pranee).
    - So the agent can do register, but only if the merchant knows to ask, in the right field, in the right words.
  - The setup screens' own language is assigned, not chosen. Mike's defaulted to Thai with no way to switch; mine ran in English `[mike]` `[product]`.
  - After English was added as a second widget language, its field still held Thai text, and the demo screen mixes the two `[mike]`.
  - The help centre is English and Thai only, and two Thai searches for Pranee's question never surfaced the Personality article `[help]`.
- *Wrong if:* merchants who never touch language settings go live as fast as those who do, or language settings are rarely changed.
- *Test:* data on language-rule edits and interface-language changes; a code-switched test set; PX-04.

**H12 · Marketplace merchants are slower because their knowledge and their requests sit where the product reaches least.** · **H** *(confirmed; up from M)*
- *Evidence:* "Note: Do not upload Shopee, Lazada, or similar links" on the website source screen, then a Shopee URL accepted anyway and failing with the wrong explanation `[product]`. Marketplace order triggers are Advanced-only `[pricing]`. There's no help centre in Bahasa or Tagalog, only English and Thai `[help]`.
- *Wrong if / test:* unchanged from v2.

**H13 · SMB merchants are doing a services job on their own.** · **H** *(supported; up from M)*
- *Evidence:* Zaapi sells the setup as a service: "AI Success Kit: Let us build your AI for you. See results in 60 days… 30% automation guaranteed or we refund you in full" `[pricing]`. A dedicated account manager and the free Flow Builder consultation are Enterprise-only `[pricing]`. The kit promises results in 60 days. That's a different measure from go-live, but it shows Zaapi doesn't expect this to be quick even when it does the work.
- *Wrong if:* enterprise and AI Success Kit accounts activate at similar rates and speeds to self-serve SMBs.
- *Test:* data on activation and 30-day retention for Success Kit accounts vs self-serve.

**H14 (new) · Going live is a spending decision with no cap. Every AI reply after the trial's 300 free ones is paid for, and the only launch options send all new or all out-of-hours tickets to the AI.** · **M**
- *Evidence:* "AI tokens purchased separately"; 300 free messages carried over from the trial; then from $40 per 1,000 messages `[pricing]`. Launch is all-or-nothing (H9) `[product]`, so the only way to limit spend is not to launch, or to build Flow Builder logic on Pro or above.
- *Scale* `[inference]`: at $0.04 a reply, 1,000 conversations of five AI replies each cost $200 a month, more than the Pro plan itself ($97). For a low-order-value seller like Budi (about IDR 85k per order), that's a real line item.
- *Why M:* the mechanism is documented, but there's no behavioural evidence yet.
- *Wrong if:* go-live timing doesn't cluster around trial end or first token purchase; merchants who stall haven't looked at AI pricing; or AI spend is small next to what these merchants pay agents.
- *Test:* data on go-lives before and after first token purchase; token balance at switch-off; AI spend vs plan price by segment.

---

## 3. Other explanations: where they stand

1. **The trial boundary. Partly answered.** AI training, testing and deployment are on every plan, Basic included `[pricing]`, so the plan tier doesn't lock AI out. But the trial countdown starts on the first screen `[product]`, and AI replies are metered separately (H14). Still unknown: what happens to AI at day 7 without a subscription.
2. **AI is a paid add-on or runs on credits. Confirmed.** Tokens are bought separately. Promoted to H14.
3. **Channel approval delays. Not tested.** I skipped OAuth. The widget needs no approval and is connected by default.
4. **Merchants who never meant to use AI. Sharper.** Because the widget auto-connects `[product]`, "connected ≥1 channel" may count merchants who took no action. That makes the brief's denominator question more urgent.
5. **Measurement. Two new cases.** "Live" means a published flow with a "Let AI reply" node `[product]`. A "switch-off" might also be free credits running out (O7). And the AI "only replies to unassigned tickets… It won't respond if a human agent is already assigned" `[product]`, so assignment rules can quietly bypass an agent that is technically live.
6. **The brief and the product differ. Confirmed.** No share dial, tabs rather than a sequence, knowledge before scenarios before personality, and go-live happens in Flow Builder, not an AI setting `[product]`.

## 4. Walkthrough checklist: results

1. **Trial and plan:** 7-day trial, no card; countdown and "Subscribe now" from the first screen. AI is on all plans; replies are metered, 300 free `[product]` `[pricing]`.
2. **Entry point:** lands in the inbox. AI Agent opens on Knowledge Source with no progress or checklist. "Started" is undefined on screen `[product]`.
3. **Knowledge:** the "no PDF" copy is wrong (PDF loads). A plain Q&A loads. A Shopee URL fails with a misleading error. Loading takes 1–9 minutes with no progress shown `[product]`.
4. **History:** no option to learn from past chats `[product]`.
5. **Scenarios:** easy to skip, and nothing prompts you. Three templates. Two modes: instruct or escalate. No order actions. Escalation wording is fixed `[product]`.
6. **Persona and language:** replies match Thai and Bahasa with no rule set; code-switching isn't mirrored; interface language can't be chosen `[product]` `[mike]`.
7. **Test:** 10 of 10 correct. Per-message "Show thinking" only. No readiness or coverage signal. About 20 seconds per reply `[product]`.
8. **Go-live:** two all-or-nothing templates in Flow Builder, no share dial. Left as an unpublished draft `[product]`.
9. **After a bad answer:** run in the persona tests. Facts are slow to fix and may not hold; rules are instant (H10) `[persona]`.
10. **Realistic knowledge (added):** four businesses, full persona scripts: 27 messages, 2 probes, 3 fix loops `[persona]`. Results in `research/persona_test_log.md`.

## 5. Data questions for Zaapi (covering email)

1–9 as in v2, plus:

10. **Credits:** what share of go-lives come after the first token purchase? Did the 9 switch-offs coincide with the free 300 running out? What does AI spend look like against plan price, by segment?
11. **Plan tier:** do Basic merchants, who have no Flow Builder, go live less often or more slowly?
12. **AI Success Kit:** time to live and 30-day retention against self-serve.
13. **Language:** how is the interface language set? What share of merchants change it, or add a language rule to the agent?
14. **Denominator:** does the auto-connected widget count towards "connected ≥1 channel"?

## 6. `[ext]` items to verify in Perplexity

| Claim | Used in | Prompt | Status |
|---|---|---|---|
| Marketplaces run double-date or payday sales most months; typical seller run-up | H2 | PX-02 | To run |
| Most commerce chat is order or action requests, not information | H7, H12 | PX-01 / PX-03 | To run |
| Marketplace APIs restrict third-party order actions and chat content | H7, H12 | PX-01 | To run |
| Code-switched chat is common in SEA and hard for LLMs | H11 | PX-04 | To run; the walkthrough supports the second half |
| AI Agent pricing and packaging after the trial | H14, alt. 1–2 | PX-00 | Largely answered by the pricing page; day-7 behaviour still open |
