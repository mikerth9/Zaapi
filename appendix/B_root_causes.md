# Appendix B — Root causes

*Built from Appendix A v3. A root cause here has to explain more than one symptom in the funnel, rest on evidence from the product rather than the brief alone, and be something Zaapi controls. Source tags as in Appendix A: `[product]` `[mike]` `[help]` `[pricing]` `[persona]` `[inference]`.*

## The short version

The agent is good once it's built well. With a well-written knowledge base it answered 10 of 10 test messages correctly, in three languages `[product]`. With the thin knowledge the four personas realistically have, it stayed safe, but it went quietly wrong. It stated canned text as fact, promised actions it can't take, drifted in voice, and gave different answers to the same question on different runs `[persona]`. Merchants are lost at four points around it:

| # | Root cause | Funnel symptom it explains | Hypotheses | Hits hardest | Confidence |
|---|---|---|---|---|---|
| **RC1** | **No path from signup to a live agent.** The product never says "here's what's left". | 4 days to first step; 21 of 100 add no knowledge; 19-day median | H1, H5, O1, O4 | Budi, Pranee/Fon | High |
| **RC2** | **Setup asks merchants to write, but never tells them if what they wrote works.** | Scenarios 71 → 38; "how do I know it's ready?"; testing that never ends; switch-offs after the first mistake | H3, H6, H8, H10 | Aisha, Pranee/Fon, Budi | High |
| **RC3** | **Going live is one all-or-nothing, paid decision, made in a different tool.** | 19-day median; switch-offs within 72 hours | H9, H13, H14 | Aisha, Joanna | High (mechanism); Medium (effect) |
| **RC4** | **The agent's reach stops where much of the work is: marketplaces and order actions.** | Marketplace merchants slower; "it passes cancels to the team, which is us" | H4, H7, H12 | Budi | High |

**Contributing, not root:** language and localisation (H11) make RC1 and RC2 worse for non-English merchants, but the agent's own language handling mostly works.

**How they compound.** RC2 and RC3 together are the core: merchants can't tell when the agent is ready, and they can't launch a small part of it to find out. So they either keep testing (Aisha) or launch everything and pull back at the first mistake (Joanna, and the Kuala Lumpur quote). RC1 decides how many merchants ever reach that point; RC4 decides how much the agent can do for them once they do.

```
signup ──RC1──▶ start setup ──RC2──▶ "is it ready?" ──RC3──▶ launch all or nothing ──RC3/RC4──▶ first mistake or bill ──▶ switch off
          │                     │                          │
     never starts         stalls at scenarios        tests forever
     (21 of 100)          (33 of 100)                (Aisha)
```

---

## RC1 · No path from signup to a live agent

**What's going on.** A new merchant lands in the Helpdesk inbox. Nothing on screen says the AI Agent exists, what setting it up involves, or what's left to do. Once inside AI Agent, setup is five screens in no particular order, with no progress, checklist or next step. Getting started depends entirely on the merchant's own initiative.

**Evidence**
- Signup lands on the inbox. The onboarding modal asks for your name, team size and a channel, and never mentions AI `[product]`.
- No dashboard, "steps left" or nudges on the first screen. The quick setup is gone `[mike]`.
- The help centre's start guide has six steps, all Helpdesk: account, channel, team, inbox, analytics, mobile app `[help]` `[mike]`.
- Scanning the onboarding QR code takes you out of the setup step at the moment of highest interest `[mike]`.
- AI Agent opens on Knowledge Source with no ordering between Train, Test and Deploy, and no indication of what's done `[product]`.
- The trial countdown and "Subscribe now" appear from the first screen: the clock starts before any value has been shown `[product]`.

**What it explains.** The 4-day wait before any setup step (O4), the 21 of 100 who never add knowledge, and part of the 19-day median. It also explains why scenarios get skipped (H5): without a path, nothing tells you scenarios come next or matter.

**Who it hits.** Budi, most: he has 20–30 minutes at a time and needs the next step handed to him. Pranee/Fon, who don't know what they're meant to be doing. Aisha, least: she brings her own structure.

**Wrong if.** Merchants who start AI setup on day 0 go live no faster than others; or most first AI actions already come from a Zaapi email or account manager, in which case the gap is in outreach, not the product.

---

## RC2 · Setup asks merchants to write, but never tells them if what they wrote works

**What's going on.** Every setup step is authoring: knowledge documents, free-text scenario triggers, instructions, a 250-character rules box. None of them gives feedback on whether the writing did its job. Knowledge loads with no progress, fails with the wrong explanation, or silently takes nine minutes. Scenarios fire in ways that only loosely follow what was written. The test screen checks one message at a time and never says how much is covered. So merchants can't tell good work from bad, and can't tell when they're done.

**Evidence**
- No readiness or coverage view anywhere in setup, test or deploy `[product]`.
- Knowledge loading took 1–2 minutes for a large file and 8–9 minutes for small ones, with no progress or estimate `[product]`.
- A Shopee URL, warned against on the same screen, was accepted and then failed with a message blaming character limits `[product]`.
- The upload copy says PDFs aren't accepted; they are. The product's own guidance is wrong in both directions `[product]`.
- The "Cancel after pickup" scenario handed off earlier than instructed; the angry-customer handoff fired with "no relevant scenario was found" `[product]`.
- "Show thinking" is a real three-step trace, but only for one message at a time `[product]`.
- The only fix path is a generic "Train your AI" link, not a link to the source that produced the answer `[product]`.
- **The same question gives different answers.** Budi's stock question: "ready stok" in 4 of 5 runs, a handoff in 1 `[persona]`. A merchant's one passing test is a coin toss.
- **The self-check passes false answers:** "Groundedness ✓ · No issues found" on a false stock claim, because it checks the answer against the knowledge, not against reality `[persona]`.
- **Conflicting sources aren't detected.** Aisha's stale 7-day and current 14-day return policies were both loaded; the answer depended on which one retrieval surfaced `[persona]`.
- **Thin knowledge fails confidently, not visibly.** Budi's canned "Ready stok kak" became a stock claim; every source said "Completed" `[persona]`.
- **Facts and rules fix very differently, and nothing says which you're dealing with.** A rule (scenario or guideline) took a minute and held. A fact (knowledge edit) sent the source back to 0 characters for 6–8 minutes, degraded the agent meanwhile, and the fix held in 1 of 3 runs `[persona]`.

**What it explains.** The biggest drop in the funnel, 71 → 38 at scenarios: writing them is effortful and the benefit is invisible. The Bangkok quote ("How do I know it's ready?"). Aisha's endless testing. It probably explains part of the switch-offs too: merchants launch without knowing what's uncovered, then find out from a customer.

**Who it hits.** Aisha, most: she wants proof and gets none, and her own guardrail over-fired on a bedsheet. Budi: his 2–3 test messages would likely show his own quick replies coming back fluently, which looks right to him. Pranee/Fon: the medical red line held by default `[persona]`, but her real risks (a male voice for a woman-run shop, a false "checked the system") are ones nobody would think to test.

**Wrong if.** Merchants who switched off had tested the topic that later failed; or merchants who test more don't switch off less.

**Note on H3.** The v2 belief that file format is the gate is dead: the product accepts almost anything `[product]`. What remains is that accepting everything and checking nothing moves the problem downstream, into RC2.

---

## RC3 · Going live is one all-or-nothing, paid decision, made in a different tool

**What's going on.** The brief says merchants choose what share of conversations the agent handles. The product has no such control. Going live means choosing between "AI handles all new tickets" and "AI handles tickets out of hours" in Flow Builder, an automation editor built for operations users. Narrowing the launch means building your own flow logic; that editor isn't on the Basic plan, and its help isn't written for SMEs. Every AI reply beyond the trial's 300 free ones is charged separately. So the first launch is also the biggest possible launch, with no ceiling on risk or cost.

**Evidence**
- Deploy offers exactly two templates; there's no share, topic or channel dial `[product]`.
- The template's only exits to a human are the AI's own judgement or an hour with no customer reply `[product]`.
- Basic has no Flow Builder or automations; the free Flow Builder consultation is Enterprise-only `[pricing]`.
- Flow Builder help isn't SME-friendly, and nothing helps a merchant express what they want the flow to do `[mike]`.
- AI tokens are sold separately: 300 free from the trial, then from $40 per 1,000 messages `[pricing]`.
- Zaapi sells a done-for-you "AI Success Kit" promising results in 60 days `[pricing]`: the company itself treats getting this right as a service job (H13).

**What it explains.** Part of the 19-day median: a merchant who's finished testing still faces a new tool and a financial decision. The switch-offs within 72 hours: an all-in launch means the first mistake is public and the whole agent comes off (Kuala Lumpur). Possibly some switch-offs are simply the free credits running out `[inference]` (Appendix A, data question 10).

**Who it hits.** Aisha, most: her condition for going live is starting small on one channel, which the product can't do without custom Flow Builder work. Joanna, in the opposite direction: nothing slows her, so she launches everything on a Friday drop.

**Wrong if.** Merchants who launched narrowly (out-of-hours template, or a custom flow) switch off as often as those who launched on everything; or go-live timing doesn't cluster around the end of the trial or the first token purchase.

---

## RC4 · The agent's reach stops where much of the work is: marketplaces and order actions

**What's going on.** For marketplace-led merchants, the product can't read the content they already have (listings) and can't act on the requests their customers most often make (cancel, return, refund). Scenarios can only say things or hand off. Order actions exist only through webhooks and marketplace triggers on the Advanced plan, and need a technical build. Conversations Zaapi already imports from marketplaces aren't offered as a starting point.

**Evidence**
- "Do not upload Shopee, Lazada, or similar links," then a Shopee URL accepted and failing `[product]`.
- Scenario responses are "Follow instructions" or "Escalate" only; there are no order actions in setup `[product]`.
- Webhook and HTTP actions and marketplace order triggers are Advanced-only `[pricing]`.
- No option to build knowledge or scenarios from past conversations `[product]`.
- **The agent doesn't know its own limits.** Without actions, it still promises them: "ma-check ko agad ang status", "isesend ko… sa DM", "saya akan cek ketersediaan". Mostly with no handoff, so the customer waits for something that never happens `[persona]`.
- The help centre is English and Thai only: nothing in Bahasa, Vietnamese or Tagalog `[help]`.

**What it explains.** The brief's finding that marketplace merchants go live more slowly. The Ho Chi Minh City quote ("it'll pass them to the team. Which is us"). Part of RC3's switch-offs: requests the agent can't handle get handed straight back to the merchant.

**Who it hits.** Budi, almost entirely: his knowledge is in Shopee listings, his customers ask about cancels and returns, and there's no help in his language.

**Wrong if.** Marketplace merchants' delay sits in connection and authorisation rather than knowledge and scenarios; or Advanced merchants resolve order requests without a human at clearly higher rates without custom builds.

---

## Contributing factor · Language and localisation (H11)

The agent's own language handling mostly works: with no rule set, it replied in natural Thai and Bahasa `[product]`. What doesn't work is everything around it. The default is stated once in small print. Code-switched Taglish and Manglish get plain English. The setup screens' language is assigned, not chosen, and mixes Thai and English `[mike]`. In the persona tests, register came through only when the merchant knew to ask for it in the right field: Taglish with an explicit "Always reply in Taglish" guideline, but not Aisha's "mirror the mix" style note. Thai gender forms drifted until they were specified `[persona]`. The help centre stops at English and Thai `[help]`. None of this stops setup outright, but it makes RC1 and RC2 worse for exactly the merchants the brief's quotes come from: Chiang Mai ("I'm not sure whether that matters"), Manila, Jakarta.

## Ruled out or demoted

- **File format as a barrier** (H3, v2): PDFs and plain FAQs load `[product]`.
- **The agent replying in the setup language** (H11, v2): it matched the customer's language unprompted `[product]`.
- **Unsafe answers as a cause of switch-offs**: across 30 persona messages (27 script, 2 probes, 1 isolation check), no medical claims, no invented vouchers or prices, no agreed compensation, including for Pranee with no rules configured `[persona]`. The failures that would embarrass a merchant are quieter ones: false stock, false promises, the wrong voice (RC2, RC4).
- **Plan tier blocking AI outright** (alternative 1): AI training, testing and deployment are on every plan `[pricing]`. Cost (H14) and Flow Builder access (RC3) are the real constraints.

## Open questions that could reorder these

1. **Are the 72-hour switch-offs trust or credits?** If most coincide with the free 300 messages running out, RC3's cost side outranks its risk side.
2. **Is the delay waiting or working?** If active setup time is short and elapsed time long, RC1 dominates; if active time is long, RC2 does.
3. **Does plan tier predict go-live?** If Basic merchants (no Flow Builder) go live far less, RC3 is partly a packaging problem.
4. **Does the auto-connected widget inflate "connected a channel"?** If so, the funnel's first step overstates engagement and RC1 is larger than it looks.
5. **How much do live answers vary?** If the run-to-run variation seen in testing (Budi: 4 of 5 bad) holds in production, RC2 becomes a problem of predictability as much as authoring, and it would explain sudden switch-offs after an agent that "passed" testing.
