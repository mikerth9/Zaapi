# Appendix A — Hypotheses before using the product

*Written before signing up to app.zaapi.com, from the brief alone. The point is to have something the walkthrough can prove wrong, not to be right yet.*

## Current best guess

Setup asks merchants to do the one thing they find hardest: write down knowledge that lives in their heads and predict the situations their customers will create. Then it gives them no way to tell when they've done enough before a launch that is all or nothing. The result is three failure modes. Some merchants never start, because setup looks like a project and there's always another campaign. Some stall at the writing step (scenarios lose 33 of 71). Some go live under-prepared and back off at the first public mistake (9 of 61, mostly within 72 hours). Underneath all three may sit one fact: Zaapi probably already holds most of what it asks merchants to type, in their Helpdesk conversation history. *(I still need to check this in the product.)*

---

## 1. Reading the funnel as data

| Step | Reached | Of previous step | Lost here |
|---|---|---|---|
| Connected a channel | 94 | — | 6 |
| Added any knowledge | 79 | 84% | 15 |
| Set a persona | 71 | 90% | 8 |
| **Wrote ≥1 scenario** | **38** | **54%** | **33** |
| Ran ≥1 test conversation | 66 | *(not sequential)* | — |
| Went live on any channel | 61 | 92% of testers | 5 |
| Still live at 30 days | 52 | 85% | 9 (mostly < 72h) |

**What the numbers themselves say (observations, not causes):**

- **O1 · The funnel isn't a sequence.** 66 merchants tested but only 38 wrote a scenario, so scenarios can be skipped. At least 23 of the 61 who went live had no scenario.
- **O2 · Testing doesn't act as a gate.** 92% of testers go live. Most loss happens before testing and after launch, not at the moment of deciding to launch.
- **O3 · Most of the delay is waiting, not working.** 4 days to the first step and 19 days to go live. If the active work takes hours, most of those days are spent doing nothing. *(I need active-time data to confirm.)*
- **O4 · Merchants who leave after launch leave fast.** Most switch-offs happen within 72 hours. That looks like a single loss of trust, not value slowly fading.
- **O5 · The scenario/retention link may be selection.** Committed merchants probably do every step. Scenarios could be a *marker* of commitment rather than a *cause* of staying live. I treat this as unproven until controlled for engagement.
- **O6 · The quotes aren't representative.** All six come second-hand via the commercial team, and all six accounts are mid-to-large (800–9,000 orders/mo). The smallest SMBs, who get no hands-on help, aren't heard from directly.

---

## 2. Hypotheses

Confidence: **H** = several independent signals in the brief · **M** = one clear signal, plausible mechanism · **L** = inference, worth checking.
`[ext]` = relies on outside knowledge; to verify via Perplexity.

### A. Never starting (39 never go live · 4-day median to first step)

**H1 · Setup looks like a project, not a switch, so merchants put it off.** *Confidence M*
Merchants see agent setup as a multi-session configuration job and wait for a quiet week that doesn't come.
- *Evidence:* 4 days to first step; 19 days to live; Jakarta quote.
- *Wrong if:* active setup time is also long (then setup really is hard, not just delayed), or merchants who start on day 0 aren't much faster.
- *Test:* active minutes in setup vs elapsed days; time-to-live split by day of first step.

**H2 · Campaigns are the normal calendar, not the exception.** *Confidence M* `[ext]`
SEA marketplaces run a double-date sale most months, plus payday and seasonal sales. For marketplace sellers, "after the campaign" may never arrive. There's a harsh irony here too: merchants sign up *because* chat volume spikes, which is exactly when they have no time to set anything up.
- *Evidence:* worse activation for campaign-period signups; Jakarta quote.
- *Wrong if:* campaign windows are rare, or signups outside those windows activate no better.
- *Test:* activation by signup week against the campaign calendar, split by marketplace-led vs social-led merchants.

### B. Stalling mid-setup (scenarios: 71 → 38)

**H3 · The product asks for knowledge that isn't written down.** *Confidence H*
Policies and edge-case handling live in the owner's and chat team's heads. A blank field asking for "your policies" turns the merchant into a technical writer.
- *Evidence:* Manila quote; Bangkok quote ("FAQ doc… is it enough?"). "Added *any* knowledge" says nothing about how complete it is.
- *Wrong if:* the knowledge merchants add is usually substantial and complete, and they stall somewhere else.
- *Test:* knowledge volume and sources per merchant; what the empty state asks for in the walkthrough.

**H4 · Scenarios look optional but hold most of the value.** *Confidence H*
Knowledge answers questions about information. Scenarios decide what happens with requests to *do* something (cancel, refund, where's my order), which are probably most of commerce chat `[ext]`. An agent without scenarios answers FAQs and hands back exactly the conversations that cost the team time, so the merchant saves no labour.
- *Evidence:* HCMC quote; scenarios can be skipped (O1); scenarios correlate with staying live.
- *Wrong if:* after controlling for engagement, escalation and switch-off rates are the same with and without scenarios.
- *Test:* escalation rate by number of scenarios; intent mix in Helpdesk conversations.

**H5 · Writing a scenario is really prompt engineering.** *Confidence M*
Merchants have to predict situations and write instructions for how the agent should behave. They don't know which scenarios matter, how many are enough, or what a good one looks like.
- *Evidence:* the size of the drop; Manila quote ("wasn't sure what I was supposed to write").
- *Wrong if:* templates or examples already exist and are used, and merchants still drop.
- *Test:* walkthrough (are there templates? examples? suggestions?); scenario count distribution among those who wrote any.

**H6 · Easy steps come first, so the agent feels finished before it's ready.** *Confidence L*
Persona is quick and satisfying, and it comes before scenarios, which are hard. Once an agent has a name and a voice it *feels* built, so skipping the hard step feels safe.
- *Wrong if:* scenario completion doesn't change when the step order changes.
- *Test:* walkthrough (how is progress shown?); A/B test on step order is cheap.

### C. Not knowing if it's ready, then pulling it after launch (9 of 61 switch off, mostly < 72h)

**H7 · Merchants can't tell when the agent is ready, so testing is for show.** *Confidence H*
Test mode is a blank chat. Merchants ask the questions they already know it can answer, skip the edge cases, and get no measure of coverage.
- *Evidence:* Bangkok quote ("How do I know it's ready?"); 92% of testers go live (O2); 9 switch-offs *after* testing.
- *Wrong if:* merchants who switched off had tested the exact topic that later failed.
- *Test:* test conversations per merchant and what they covered; walkthrough.

**H8 · Going live is all or nothing, and the "share" dial controls volume, not risk.** *Confidence M*
The product lets merchants set what share of conversations the agent handles. But a wrong answer at 20% is still a wrong answer sent to a real customer. There's no way to launch on the topics the agent handles well and hold back the rest.
- *Evidence:* KL quote (wrong shipping answer to East Malaysia → team panicked → switched off); switch-offs cluster at 72h.
- *Wrong if:* merchants who launched at a low share churn much less (then the dial works and just needs promoting).
- *Test:* share % at launch vs switch-off; switch-off reasons.

**H9 · After launch, switching off is the only fix merchants have.** *Confidence M*
When the agent gets something wrong, the merchant can't easily see it, correct it at the source and move on. So the only lever left is turning it off. Once it's off it stays off ("maybe we try again later"; "rarely come back").
- *Wrong if:* there's an easy correct-from-conversation flow and merchants who switched off didn't use it.
- *Test:* walkthrough (can I fix a bad answer from the conversation view?).

### D. Cross-cutting

**H10 · The form sets the language, not the customers.** *Confidence M*
Merchants configure the agent in the interface language, and setup doesn't use the language their customers actually write in. The merchant can't tell whether it matters, and that uncertainty alone is enough to stall. Code-switching (Thai-English, Taglish) makes it harder `[ext]`.
- *Evidence:* Chiang Mai quote.
- *Wrong if:* the agent already replies in the customer's language whatever the setup language. Then the problem is communication, not capability, which is cheaper to fix.
- *Test:* walkthrough (set up in English, test in Thai).

**H11 · Marketplace channels are slower because their conversations are about orders.** *Confidence M* `[ext]`
Shopee, Lazada and TikTok Shop chats are mostly about orders and actions, platform rules limit what can be said, and campaigns concentrate volume. So marketplace merchants hit H4 hardest, and possibly hit technical or API limits too.
- *Evidence:* marketplace go-lives are slower; the campaign effect.
- *Wrong if:* the delay is purely technical (API approval, authorisation), in which case it's an integration problem, not an authoring one.
- *Test:* time-to-live broken down by step and channel; Perplexity on platform chat rules.

**H12 · Zaapi already holds the answers and asks merchants to retype them.** *Confidence M, and the most important to check*
94% already use Helpdesk, so Zaapi probably holds real customer conversations: the team's actual answers, tone, language, and when they escalate. If setup starts from empty fields instead of drafting from this history, merchants are re-entering what the system already knows. This single cause would drive H3, H5, H7 and H10 at once.
- *Wrong if:* setup already mines history, or new signups have too little history to use (days of data, not months).
- *Test:* walkthrough; how long merchants have used Helpdesk before starting AI setup, and their conversation volume.

**H13 · SMBs are doing a services job on their own.** *Confidence M*
Enterprise accounts get hands-on help and SMBs don't. If enterprise activation is much better, the missing piece is the help, and the product should do what the commercial team does.
- *Evidence:* brief §02.
- *Test:* activation and time-to-live by segment; ask the commercial team what they actually do in an enterprise setup.

---

## 3. Other explanations to rule out first

These would make much of the above irrelevant, so I check them early:

- **Plan or credit gating.** Is AI Agent a paid add-on, or limited during a trial? If so, some of the "stall" may really be a buying decision.
- **Channel or API approval time.** Meta/WhatsApp Business verification and marketplace app authorisation can take days, which would inflate the 19-day median.
- **Signups who never intended to use AI Agent.** If most signups come for Helpdesk, the 39% partly measures a different kind of intent.

## 4. What I'm checking in the walkthrough

1. The empty state for knowledge and scenarios: what's asked, what's offered (templates, examples, imports).
2. Whether Helpdesk history is used anywhere in setup.
3. Whether the steps are gated, how progress is shown, and what "done" looks like.
4. Test mode: suggested questions, coverage or readiness signals, the ability to fix an answer in place.
5. Language: set up in English, test in Thai.
6. Go-live controls: share %, per-channel, per-topic, working hours, handover rules.
7. After launch: can I see and correct a bad answer?
8. Time: my own active minutes per step.

## 5. Questions for Zaapi (via the covering email)

1. Active time in setup vs elapsed days, for merchants who went live.
2. Activation split by segment (SMB vs enterprise) and by primary channel.
3. Scenario retention link: does it hold after controlling for knowledge volume and test count?
4. Switch-off reasons for the 9: any tagged cause?
5. Share % merchants choose at launch.
6. How much Helpdesk history a typical merchant has when they start AI setup.
