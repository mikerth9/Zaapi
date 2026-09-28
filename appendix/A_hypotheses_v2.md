# Appendix A — Hypotheses before using the product (v2)

*Written before signing up to app.zaapi.com, from the brief and Zaapi's public help centre. The point is to have something the walkthrough can prove wrong, not to be right yet.*

**Source tags.** *Brief* = the take-home (fictional numbers, treated as real). `[help]` = help.zaapi.com, read 25 Sep 2026. It describes the real product, which may differ from the brief's scenario or lag behind the live app. `[ext]` = general outside knowledge, to verify in Perplexity before it reaches the memo.

## Current best guess

Setup asks merchants for their business knowledge in a form most of them don't have: structured, heading-based documents (no PDFs, and marketplace listings can't be scraped `[help]`). It then asks them to predict their customers' requests as scenarios. Those scenarios can follow instructions or escalate, but as far as the documentation shows they can't *do* anything, such as cancel an order `[help]`. At no point does setup tell merchants whether they have done enough. The conversations Zaapi already holds for some channels are shown in the inbox, and none of the documentation says setup uses them. So merchants either never start (setup looks like a project, and a campaign is usually coming), stall at scenarios (33 of 71 who set a persona didn't write one), or go live on hope and pull back after the first public mistake, because switching off is easier than finding and fixing the source. One fact may matter more than all of this: Zaapi's trial is 7 days `[help]` and the median go-live is day 19. Much of the "activation" problem may be happening after a payment decision, which I need to rule in or out first.

---

## 1. Reading the funnel as data

| Step (brief order) | Reached | Of previous row | Lost | Of 100 |
|---|---|---|---|---|
| Connected ≥1 channel | 94 | — | 6 | 94% |
| Added any knowledge | 79 | 84% | 15 | 79% |
| Set a persona | 71 | 90% | 8 | 71% |
| **Wrote ≥1 scenario** | **38** | **54%** | **33** | 38% |
| Ran ≥1 test conversation | 66 | *174% (rises)* | +28 | 66% |
| Went live on any channel | 61 | 92% of testers* | 5 | 61% |
| Still live at 30 days | 52 | 85% | 9 | 52% |

\* Only if everyone who went live had tested. The brief doesn't say they did.

**Observations (not causes):**

- **O1 · It's not a sequence.** Testing (66) exceeds scenarios (38), so scenarios can be skipped. At least 23 of the 61 who went live never wrote one, and at least 14 of the 52 still live have none. The help centre supports this: knowledge, scenarios and personality sit as three tabs on one Train page, in that order, not persona-then-scenarios `[help]`. The brief's step order may not match the screen.
- **O2 · The loss sits at authoring and after launch, not at the launch decision.** 71 → 38 at scenarios and 61 → 52 after launch. Testers almost all launch.
- **O3 · The denominator is odd.** The 100 are merchants who "start setting up an AI Agent", yet 21 never add any knowledge and 6 never connect a channel. So I need to know what counts as "starting". It may just be visiting the AI section, which would mean the 39% includes merchants who only looked around.
- **O4 · The 4-day "first step" may be a Helpdesk number.** Connecting a channel counts as a setup step, and it's "mostly already done via Helpdesk". If so, the 4 days may measure Helpdesk onboarding, and the first AI-specific action could come even later.
- **O5 · Most of the delay is probably waiting, not working.** 19 elapsed days for work the brief suggests takes "half an hour" to try. I need active-time data.
- **O6 · The trial ends before the median go-live.** A 7-day free trial with full access `[help]`, against a 19-day median. Most go-lives happen after the trial ends.
- **O7 · After launch, loss is sudden.** Most of the 9 switch-offs happen within 72 hours. That looks like one event breaking trust, not value slowly fading.

**Correlations that could be selection rather than cause:**

- **Scenarios ↔ staying live.** Committed merchants probably do every step. The link could also run backwards: "wrote at least one scenario" may include scenarios written *after* launch by merchants who were already staying.
- **Campaign signup ↔ worse activation.** Merchants who sign up during a campaign may be a different kind of merchant: reactive, mostly on marketplaces, high volume. That overlaps with the channel effect, so the two findings may be one finding.
- **Messaging channels ↔ faster go-live.** Merchants choose which channel to launch on, and social-first brands differ from marketplace resellers in size, catalogue and staffing. The comparison also counts only merchants who got there.
- **Live and kept live ↔ renewal** (brief §01). Engaged merchants both activate and renew. Activation may be a marker of that engagement more than a lever for it.

**Bias in the evidence:**

- **The quotes.** Six of them, all from stalled accounts, all second-hand via the commercial team, all mid-to-large (800–9,000 orders/mo), with no successful merchants for contrast. Each maps neatly to one funnel step, which suggests they were picked to illustrate, not sampled. The smallest SMBs, who get no hands-on help, aren't heard from at all.
- **One quote doesn't fit its label.** The brief calls the six "never got an agent live", but Kuala Lumpur *did* go live ("We turned it on Friday"), so it belongs with the 9 switch-offs.
- **The help centre.** It describes intended use, is written to cut support load, and may be out of date. It shows how the product *should* work, not where merchants struggle.

---

## 2. Hypotheses

Confidence: **H** = several independent signals · **M** = one clear signal and a plausible mechanism · **L** = inference only.
*✎ = one of my own four notes from reading the brief, rewritten as a cause (see the note under H2).*

### A. Never starting (39 never go live · 4-day median to first step)

**H1 · Setup looks like a project, so merchants put it off.** · **M**
Merchants see setup as a multi-session job and wait for a quiet week that doesn't come.
- *Evidence:* 4 days to first step, 19 to live (O5); Jakarta quote.
- *Why M:* the delay is clear, but I can't yet separate "put off" from "hard" (H3–H6).
- *Wrong if:* active setup time is also long, or merchants who start on day 0 aren't much faster to go live.
- *Test:* data on active minutes vs elapsed days; time-to-live split by the day of first AI action; my own minutes per step in the walkthrough.

**H2 ✎ · Setup takes longer than the run-up to the next campaign, so it gets overtaken by it.** · **M** `[ext]`
Merchants sign up when chat volume starts to rise, which is also when they have the least time. Setup then runs into the campaign peak, and once the peak has passed, the reason they signed up goes with it.
- *Evidence:* worse activation for campaign-period signups; Jakarta ("Double 11 and I had no time… sitting there since November"). If double-date sales run most months `[ext]`, "after the campaign" may never arrive for marketplace sellers.
- *Why M:* one quote and one correlation, and the correlation could be selection (see above).
- *Wrong if:* activation doesn't improve as the gap between signup and the next campaign grows (e.g. 6 weeks out does no better than 1 week out), or campaign signups who *start* setup finish as fast as anyone else.
- *Test:* activation and time-to-live by days from signup to the next campaign peak, split by marketplace-led vs social-led; Perplexity PX-02 for the calendar and seller run-up times.
- *Note:* "Merchants should set up 4–6 weeks before a campaign" is a solution, so I've parked it for step 3. The hypothesis above is the cause it would address.

### B. Stalling mid-setup (scenarios: 71 → 38)

**H3 ✎ · The knowledge the agent needs isn't written down, and what does exist is in the wrong format.** · **H**
Merchants' policies and edge cases live in people's heads. What *is* written down is often in forms the product can't use well.
- *Evidence:* Manila ("our policies are just things we know"); Bangkok ("added our FAQ document but I don't know if that's enough"). `[help]` Uploads accept .txt/.csv/.docx/.xlsx only, **no PDF**. **Marketplace pages can't be scraped.** Answers depend on proper headings, because bold text doesn't create chunks, and a plain "Q: … A: …" FAQ can mix up answers. So Bangkok's FAQ doc may really be performing badly, not just feeling uncertain.
- *Why H:* two quotes plus the product's own documented limits.
- *Note:* 84% get past the knowledge step, so H3 predicts *thin or badly structured* knowledge, which shows up later as uncertainty (H8) and wrong answers (Kuala Lumpur), not as a drop at the knowledge step itself.
- *Wrong if:* knowledge added by merchants who stall is about as large and well structured as that of merchants who stay live.
- *Test:* data on knowledge volume, source type, heading structure, and failed PDF uploads; in the walkthrough, upload a plain-format FAQ and test it.

**H4 ✎ · Zaapi holds real conversations for some channels, and setup doesn't use them.** · **M, and the most important to check**
Past chats contain the team's actual answers, policies in practice, tone, language and escalation habits. Setup starts from empty fields instead.
- *Evidence:* `[help]` Shopee, Lazada and TikTok Shop import **90 days of history** on connection. There is no documented way to turn history into knowledge or scenarios; training takes files, URLs or typed text.
- *Why M:* the docs don't mention it, but that's absence, not proof, and it's also a counter-signal: LINE brings in **no history** unless the merchant manually imports a backup, which needs a verified account and the OA Chat package `[help]`, and the new signups in this funnel may have little Helpdesk history of their own.
- *Wrong if:* the product already drafts from history, or merchants have little usable history when they start AI setup (days, not months, or mostly LINE).
- *Test:* walkthrough (look anywhere for "learn from past chats"); data on conversation volume and history age per merchant at the first AI action, by channel.

**H5 ✎ · Merchants treat scenarios as optional because the product presents knowledge as the core.** · **M**
Nothing in setup shows which customer requests will fail without a scenario, so skipping them looks safe. This is a problem of *perceived value*, not difficulty.
- *Evidence:* Ho Chi Minh City ("I thought the knowledge would be enough"). `[help]` Knowledge is called "the brain" and scenarios are for "common, predictable situations". Templates exist ("Check order status", "Return or refund"), so this is **not** a blank-page problem.
- *Why M:* one quote and the framing in the docs.
- *Wrong if:* most of the 33 opened the scenario tab or a template and then left (that points to H6 or H7, not awareness).
- *Test:* data on the share of the 33 who opened the scenario tab, opened a template, or saved a draft; walkthrough on whether the product prompts me towards scenarios at all.

**H6 · Writing a scenario is prompt engineering disguised as a form.** · **M**
Merchants have to predict how customers will phrase requests and write instructions for the agent. That is a skill they don't have, and they can't tell when a scenario is good enough.
- *Evidence:* Manila ("wasn't sure what I was supposed to write"). `[help]` When scenarios misfire, the documented fix is to broaden the trigger description with more phrasings, which shows that quality depends on how well the merchant writes.
- *Why M:* the mechanism is documented, but the only direct signal is one quote.
- *Wrong if:* merchants who open a scenario usually finish and save it, and templates are used unedited without problems.
- *Test:* data on scenario starts vs saves, template edits, and scenario count among the 38; walkthrough on writing a refund scenario and testing three phrasings.

**H7 · Scenarios can instruct but can't act, so the requests that cost merchants the most still end up with a human.** · **L–M** `[ext]`
Cancelling, changing an address and processing refunds need order actions. If the agent can only follow instructions or escalate, a scenario mostly makes the handover smoother, and the merchant sees little saving for the effort.
- *Evidence:* Ho Chi Minh City ("the moment someone asks to cancel… it'll pass them to the team. Which is us"). `[help]` A scenario's response is either "Follow instructions" or "Escalate to a human agent immediately". No order actions are documented.
- *Why L–M:* this rests on the docs being silent. Actions may exist through Shopify or Flow Builder HTTP nodes, and marketplace APIs may not allow them anyway `[ext]`.
- *Wrong if:* the walkthrough shows scenarios can look up and change orders on the merchant's main channel.
- *Test:* walkthrough (Shopify vs marketplace); PX-01 on what marketplace APIs let third parties do; data on the intent mix of escalated chats.

### C. Not knowing if it's ready, then pulling it after launch (9 of 61 switch off, mostly < 72h)

**H8 · Merchants can't tell when the agent is ready, so testing is for show.** · **H**
Testing is a blank chat. Merchants ask what they already know it can answer and get no measure of how much it covers.
- *Evidence:* Bangkok ("How do I know it's ready? I don't want to find out from a customer"); 9 switch-offs *after* testing. `[help]` The test page is free-form chat with "Show thinking" and a checklist. No coverage score and no testing against real conversations are documented.
- *Why H:* a quote, the funnel, and the documented design all point the same way.
- *Wrong if:* merchants who switched off had tested the exact topic that later failed, or test depth doesn't predict switch-off.
- *Test:* data on test conversations per merchant, topics covered, and time spent testing; walkthrough (is there any readiness signal?).

**H9 · Going live exposes every topic at once, and narrowing it means building automation logic.** · **M**
Merchants can't cheaply launch on the topics the agent handles well and hold back the rest. They accept all the risk or give up.
- *Evidence:* Kuala Lumpur (a wrong East Malaysia shipping answer on day one). `[help]` Going live happens in **Flow Builder**: "AI handles all new chats" is the recommended template, and narrowing means keyword routing in custom flows. The docs also warn that active flows with conflicting triggers "can cause unpredictable behavior", and Helpdesk users probably already run greeting and assignment automations. **The docs don't mention the brief's "share of conversations" control.** That discrepancy needs checking.
- *Why M:* one quote, and the product may differ from the docs.
- *Wrong if:* merchants who launched narrowly (low share, keyword fallback, one channel) switch off as often as those who launched on everything; or go-live happens within a day of the last test (in which case Flow Builder isn't adding delay).
- *Test:* data on launch configuration vs switch-off and time from last test to live; walkthrough of go-live with a pre-existing greeting automation.

**H10 · After a public mistake, switching off is easier than fixing it.** · **M**
Fixing a wrong answer means finding the conversation, reading the reasoning, going to the Train page and editing the right section of a document. Turning the agent off is one click, and the team is panicking.
- *Evidence:* Kuala Lumpur ("my team panicked, so we turned it off. Maybe we try again later"); brief ("rarely come back"). `[help]` The documented fix runs from Analyse logs → "Show thinking" → back to Train. **Analyse only shows closed chats**, so a bad answer in an open Saturday chat may not appear in the logs when the team goes looking.
- *Why M:* one quote plus a documented multi-step path.
- *Wrong if:* the merchants who switched off used the correction path first, or switched off for other reasons (cost, customer complaints about AI).
- *Test:* data on switch-off reasons and whether knowledge was edited before switch-off; walkthrough (from a bad test answer to a fix: how many steps and minutes?).

### D. Cross-cutting

**H11 · The agent's language is set by what the merchant writes, not by what customers write.** · **M** `[ext]`
Language is a free-text guideline, and merchants fill it in using the language of the interface. They can't tell what the default does, and that uncertainty is enough to stop them.
- *Evidence:* Chiang Mai ("I set it up in English because that's what the form was in. But 90% of our customers write in Thai"). `[help]` Language sits under "Custom guidelines", and the docs' own example is "Always respond in English". Code-switching (Thai-English, Taglish) makes this harder `[ext]`.
- *Why M:* one quote, but a clear mechanism in the docs.
- *Wrong if:* with no guideline set, the agent replies in the customer's language. Then the problem is a lack of reassurance, not capability.
- *Test:* walkthrough (English knowledge, no language rule, test in Thai and code-switched Thai); PX-04.

**H12 · Marketplace merchants are slower because their knowledge and their requests both sit where the product reaches least.** · **M** `[ext]`
Marketplace-only sellers keep product information in listings the product can't scrape. Their chats are mostly about orders (H7), and the platforms limit what replies can do.
- *Evidence:* marketplace go-lives are slower (brief). `[help]` Marketplace sites can't be scraped; Shopee replies are capped at 600 characters and allowed only within 7 days of the buyer's last message. There's a pull in the other direction too: AI replies count towards Shopee's response rate, which gives marketplace sellers a reason to activate.
- *Why M:* the mechanisms are documented, but the brief gives only a direction of effect.
- *Wrong if:* the marketplace delay sits in connection and authorisation (e.g. TikTok Shop owner-only authorisation, Lazada's six-month re-authorisation `[help]`), not in knowledge or scenarios.
- *Test:* data on time per step by channel, and knowledge source type by channel; PX-01.

**H13 · SMB merchants are doing a services job on their own.** · **M**
What the commercial team does for enterprise accounts (probably drafting knowledge, choosing scenarios, and making the go-live call) is exactly where SMBs stall.
- *Evidence:* brief §02 ("SMB merchants are largely on their own"). Note that all six quotes come from accounts the commercial team deals with.
- *Wrong if:* enterprise accounts activate at similar rates and speeds.
- *Test:* data on activation and time-to-live by segment; ask the commercial team what an assisted setup actually involves and how long it takes.

---

## 3. Other explanations to rule out first

Any of these would make much of the above irrelevant:

1. **The trial boundary (O6).** A 7-day trial against a 19-day median go-live `[help]`. What happens to AI Agent at day 7: does it stay, get limited, or need a plan upgrade? If merchants lose AI access or have to decide to buy before they've gone live, the "stall" is partly a purchase decision. PX-00 on pricing.
2. **AI Agent is a paid add-on or runs on credits.** If so, "never live" partly means "never paid". PX-00.
3. **Channel approval delays.** Mostly ruled out by the docs: marketplace connection is self-serve OAuth, and Meta Business Verification only restricts broadcasts and templates `[help]`. It still needs a check for WhatsApp numbers new to the API.
4. **Merchants who never meant to use AI.** 15 connected a channel but never added knowledge. If they signed up for Helpdesk, the 39% partly measures intent, not friction (O3).
5. **Measurement.** If "live" means "published a flow containing a 'Let AI handle' node", then keyword-fallback setups, paused flows or conflicting flows could be miscounted as live or switched off. What event defines "live" and "switched off"?
6. **The brief and the product differ.** The brief describes a share-of-conversations dial and a persona-before-scenarios order that the help centre doesn't show. My hypotheses need to be tested against the product as it really is.

## 4. Walkthrough checklist

Log active minutes and screenshots at each step.

1. **Trial and plan:** what the signup screen says about the trial length and whether AI is included after the trial (alternatives 1–2).
2. **Entry point:** where AI setup starts, what counts as "started", and whether progress or a checklist is shown (O3, H1).
3. **Knowledge:** the empty state and templates; upload a plain "Q: A:" FAQ, a PDF, and a marketplace listing URL. What errors or warnings appear? (H3, H12)
4. **History:** anywhere that offers to learn from past chats (H4).
5. **Scenarios:** how visible the tab is and whether anything prompts me to it. Build a refund scenario from a template and test three phrasings. Can it look up or change an order? (H5–H7)
6. **Persona and language:** default language behaviour with no rule set; test in Thai and code-switched Thai (H11).
7. **Test:** any readiness or coverage signal; any way to test against real conversations (H8).
8. **Go-live:** the Flow Builder path; is there a share %, per-topic or per-channel control? Do it with a greeting automation already running (H9).
9. **After a bad answer:** steps and minutes from a wrong test answer to a fix; does an open chat appear in Analyse? (H10)

## 5. Data questions for Zaapi (covering email)

1. **Denominator and events:** what counts as "started setting up", "live" and "switched off"?
2. **Trial:** what happens to AI Agent at day 7, and what share of go-lives come after the first payment?
3. **Time:** active minutes in setup vs elapsed days, and the median gap between each pair of steps.
4. **Scenarios:** of the 33 who didn't write one, how many opened the tab, opened a template, or started a draft? Were the 38 scenarios written before or after go-live?
5. **Selection check:** does the scenario–retention link hold after controlling for knowledge volume and test count?
6. **Knowledge:** size, source type and structure for merchants who went live vs those who stalled; rate of failed uploads.
7. **History:** conversation volume and history age per merchant at the first AI action, by channel.
8. **Switch-offs:** reasons for the 9 and launch configuration (share, flow type, channel); was knowledge edited before they switched off?
9. **Segments:** activation and time-to-live by SMB vs enterprise, primary channel, and days from signup to the next campaign.

## 6. `[ext]` items to verify in Perplexity

| Claim | Used in | Prompt |
|---|---|---|
| Marketplaces run double-date or payday sales most months; typical seller run-up | H2 | PX-02 |
| Most commerce chat is order or action requests, not information | H7, H12 | PX-01 / PX-03 |
| Marketplace APIs restrict third-party order actions and chat content | H7, H12 | PX-01 |
| Code-switched chat is common in SEA and hard for LLMs | H11 | PX-04 |
| AI Agent pricing and packaging after the trial | Alt. 1–2 | PX-00 |
