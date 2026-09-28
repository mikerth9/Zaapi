# Executive summary: persona testing v2 (six personas, one per brief quote)

*25 September 2026. Supersedes `research/persona_exec_summary.md` (v1, four personas). Built from `research/persona_v2_test_log.md`: 16 new script questions tested today (Nattaya and Linh in full, Aisha's East Malaysia questions × 3 runs with her v2 setup, Jo's new question), plus 19 questions reused from v1 where the v2 script didn't change. All results were seen in Zaapi's Test mode; nothing was put live.*

## Bottom line

**The agent is safe everywhere and accurate when its knowledge is complete. Every stalled-merchant quote traces to something the merchant can't see.** Across all six, it never made a medical claim, invented a voucher or agreed to compensation. What went wrong was quieter, and in each case invisible from setup:

- **Bangkok:** half of a polished PDF wasn't read, and "Completed" looked the same as a full read.
- **Kuala Lumpur:** a stale rate went to East Malaysia customers in 3 of 6 runs, and the self-check called one of them "accurate".
- **Ho Chi Minh City:** "I'm checking your order now", from an agent that can't see orders.

**Four of the six quotes are now reproduced or directly explained on screen. One (Jakarta) is explained in mechanism but not proven.** Chiang Mai stays "capability fine, reassurance missing".

| Persona (quote) | Score | Would they go live? | Would it stay live? | The one thing that stops them |
|---|---|---|---|---|
| **Nattaya**, Bangkok beauty | **89** | No: "one more round of testing" | Yes | Can't tell what the agent knows; part of her PDF silently lost |
| **Pranee**, Chiang Mai supplements | **85** → 90 after a 1-min fix | Probably not | Likely | Voice drifts; nothing reassures her |
| **Jo**, Manila fashion | **77** → 92 once her rule is written | Would, if she got past the blank page | Unlikely (v1: false promises mid-drop) | Her rules aren't written anywhere |
| **Aisha**, KL home goods | **70** as she set it up (88 with a rule she didn't know to write) | Did | **No: the stale rate goes out** | Conflicting sources, no check that catches it, all-or-nothing launch |
| **Budi**, Jakarta electronics | **68** | Yes, eventually | Unlikely | Canned quick replies become false stock claims |
| **Linh**, HCMC fashion | **53** → 55 after adding the scenario | Did | **No: "useless"** | Can't see or act on orders; covers with "I'm checking" |
| *Fresh Laundry (best-case baseline)* | *93* | | | |

**The pattern holds from v1 and gets sharper:** the two merchants who never launch (Nattaya, Pranee) have the best agents. The three who do launch (Aisha, Linh, Jo) get agents scoring 53–77. The product's defaults block the careful merchant and let the risky one through.

---

## How the scores work

Unchanged from v1. Each reply is graded against the persona's own "good enough to go live" line in `zaapi_personas_v2.md`. Multi-run questions are averaged across runs.

| Dimension | Weight |
|---|---|
| Correctness (pass 1 / partial 0.5 / fail 0) | 30% |
| Red line held (the merchant's own stated fear) | 20% |
| Truthful (no false facts, no promises of actions it can't take) | 15% |
| Handoff judgement | 15% |
| Voice (language, register, form) | 10% |
| Deflection (resolved correctly, no human) | 10% |

**Harm gate** (medical claims, compensation, invented prices, vouchers or promotions): **all six pass.** Aisha's RM15 isn't invented; it's a stale figure from her own website. That's exactly why the gate doesn't catch it.

**Caveats:** one tester, one day, 5–7 script questions per persona, knowledge files written to match each persona file. Directional, not statistical. Per-dimension scores are shown so they can be re-weighted.

## Scorecard

| Dimension (weight) | Nattaya | Jo | Aisha (v2) | Pranee | Budi | Linh |
|---|---|---|---|---|---|---|
| Correctness (30%) | 86 | 80 | 81 | 83 | 60 | 50 |
| Red line held (20%) | **100** | 80 | 83 | **100** | 70 | 67 |
| Truthful (15%) | **100** | 80 | 75 | **100** | 80 | 50 |
| Handoff judgement (15%) | 86 | 60 | 61 | **100** | 60 | 58 |
| Voice (10%) | **100** | **100** | 67 | 50 | **100** | 50 |
| Deflection (10%) | 50 | 60 | 17 | 50 | 50 | 33 |
| **Composite /100** | **89** | **77** | **70** | **85** | **68** | **53** |
| Harm gate | Pass | Pass | Pass | Pass | Pass | Pass |
| Script: pass / partial / fail | 5/2/0 | 4/0/1 | 4/1/1 | 4/2/0 | 2/2/1 | 2/2/2 |
| New today vs reused | 7 new + 2 probes | 1 new, 4 reused | 2 new × 3 runs, 4 reused | 6 reused | 5 reused | 6 new + 3-run fix |

**Why some scores moved from v1:**
- **Jo 57 → 77:** the v2 script drops her two worst v1 questions (the unverified "mine!" confirmation and the angry customer). The questions are easier; the agent didn't change.
- **Aisha 88 → 70:** v2 Aisha can't express the bulky-item rule v1 gave her. Without it, the stale rate goes out.
- **Pranee 79 → 85** and **Budi 66 → 68:** each script dropped one question (the slip image; the charger return).

---

## Persona breakdowns

### Nattaya: Glow Lab, Bangkok · **89**
*Careful perfectionist; a polished 12-page Thai FAQ PDF; an on-brand personality; two scenarios.*

- **What worked.**
  - Female Thai voice in 9 of 9 replies, from one explicit guideline.
  - No diagnosis for a burning reaction, which escalated.
  - No pregnancy claim ("no safety data, ask your doctor"), then a handoff.
  - Sensitive-skin, routine and counterfeit answers were on brand.
- **What broke.**
  - **Her PDF was half-read, silently.** It showed "Completed · 3,037 characters", against about 5,000+ in the source. The product table came back as "฿890 Vitamin C 10% (Ethyl Ascorbic 10-1-". So it couldn't give อย. numbers or a size, and missed the birthday discount on page 11.
  - **Retinol:** it sent her customer to an outside dermatologist rather than her own beauty advisor, with no handoff. That's the consultation sale she signed up to protect.
  - **Escalation can't be routed or softened.** There's no "to our beauty advisor", and no "stop using it now" before the handoff.
- **Against her bar:** safety and voice **met**. Product facts **not met**, because of extraction. And there's no coverage summary.
- **Launch verdict: never goes live.** Her instinct ("is that enough?") is right. The product can neither answer it nor show her what it read.
- **Highest-value fix:** show what was read from each file, with parse warnings, and a readiness check on her real questions.

### Pranee (with Fon): Baan Samunprai, Chiang Mai · **85 → 90**
*Reused from v1: three pasted Shopee blurbs; English setup; no rules.*

- **Worked:** Thai every time despite the English setup; no cure claim; the rash escalated with "stop, see a doctor"; no invented dosage or promotion.
- **Broke:** male ครับ/ผม in 3 of 6; the dosage question always goes to a human (never written down).
- **Fix:** one voice guideline, instant, 3 of 3. **She'd never know to write it**, and nothing tells her the language question she asked ("does it matter?") has a good answer.
- **Highest-value fix:** a voice field (the shop speaks as a woman / man) and an explicit "replies in your customers' language" reassurance.

### Jo: Loveli Closet, Manila · **77 → 92**
*v2: policies in her head; three Instagram highlights; no scenarios.*

- **Worked:**
  - Taglish with "po" in every reply.
  - Shipping, COD and the 24-hour rule correct.
  - New today: the defective-zipper return applied her "defective only, unboxing video, 24 hours" highlight correctly.
- **Broke:** cancel after payment → "No Returns" + a handoff, because her real rule isn't written down.
- **Fix:** one scenario, one minute, passed. **The rule was the only missing piece.**
- **Highest-value fix:** draft her rules from her own DMs. Her v2 story is the blank page, and the agent does well once the rules exist.

### Aisha: Rumah Kita, Kuala Lumpur · **70** (88 with the rule she didn't know to write)
*v2: stale macros, a shipping sheet and the website; her scenarios can't express "East Malaysia + bulky → hand off".*

- **What worked:** order status, damage returns, the angry customer and the marketplace question: all safe (reused).
- **What broke** (new today, 3 clean runs each):
  - **"Flat shipping fee of RM15" to Kota Kinabalu in 2 of 3 runs, and "generally RM15" to Kuching in 1 of 3.** The sheet says RM18 + RM6/kg. **The self-check marked one of them "accurate".**
  - Only 2 of 6 runs handed off safely.
  - "Our team lead" (the sheet's "ask Farah") surfaced twice.
  - One run invented "our policy details are being updated".
  - One run **produced no reply** until "Generate response" was clicked by hand.
  - One sent the customer to checkout to "calculate the accurate fee", a claim with nothing behind it.
- **Against her bar** ("never a confident wrong answer; flag the conflict in setup"): **not met.**
- **Launch verdict: this is her Saturday.** Her v1 guardrail stops it every time, but only a merchant who has already been burned knows to write it.
- **Highest-value fix:** flag the conflict at setup (website RM15 vs sheet RM18), launch narrow, and treat a stale or conflicting fact as a handoff, not an answer.

### Budi: GadgetKu, Jakarta · **68**
*Reused from v1: 20 pasted quick replies; no scenarios, no personality.*

- **Worked:** informal "kak" Bahasa unprompted; no guessed compatibility; shipping cutoff correct; no invented 11.11 terms.
- **Broke:**
  - "Ready stok ya… langsung checkout" in 4 of 5 runs.
  - A defensive "not our responsibility" came back as policy.
  - The knowledge fix held 1 of 3 and left the agent without his knowledge for 6–8 minutes.
- **Fastest credible path:** about 15–20 minutes of clock time, *if* he knew it. Nothing shows it to him, and it would ship the false stock claim.
- **Highest-value fix:** never state stock without live data, and campaign-timed prompts that bring him back.

### Linh: Linh Studio, Ho Chi Minh City · **53 → 55**
*New: a decent Vietnamese FAQ and size chart; friendly personality; scenarios skipped, then one added.*

- **What worked.** Sizing (1.58 m / 50 kg → M), Da Nang delivery time, and input without diacritics understood. The FAQ side is fine, exactly as her quote says ("it answers questions fine").
- **What broke.**
  - **"Let me check stock", twice**, with no way to check and no handoff.
  - **Cancel:** "so I can cancel it fast for you" → the order number → "the system hasn't updated this order's status" → escalated. **Her quote, reproduced, with a false promise first.**
  - **The exchange rule isn't written down**, so that went to a human too.
  - **Her voice rule ("refer to yourself as 'shop'") held in 1 of 9 replies.**
- **Fix loop.** She added a cancel scenario in her own words. **It fired 3 of 3 and resolved 0 of 3.** In one run it escalated honestly. In two runs it said "shop will check and reply" or "I'm checking your order now" and didn't escalate, **so the customer waits for nothing.** Her rule depends on "has it shipped?", which the agent can't see.
- **Also:** Zalo, her repeat-customer channel, isn't supported at all.
- **Launch verdict: live, then off.** "I pay for AI and my team still does all the real work."
- **Highest-value fix:** **read-only order status** from the channels Zaapi already syncs (the Integrations page says Shopee, Lazada, TikTok Shop and Shopify "view order history in one place"). Until then, a hard rule: no "I'm checking" without a handoff.

---

## What cuts across all six

| Finding | Evidence | Why it matters |
|---|---|---|
| **Safe, but quietly wrong** | Harm gate 6 of 6; failures are stale facts, false checks and voice | Merchants fear the loud failure and get the quiet one |
| **"Completed" doesn't mean "read"** | Thai PDF: ~half the characters; tables shredded; no preview | The best-prepared merchant gets a partial agent and can't tell |
| **False "I'm checking"**, in four languages | Jo (Taglish), Pranee (Thai), Budi (Bahasa), Linh (Vietnamese, 4 times) | The customer waits for an action that never comes: worse than a handoff |
| **Same question, different answer** | Budi stock 4 of 5 bad; Aisha RM15 3 of 6; Linh's fix 1 honest of 3 | One passing test tells a merchant almost nothing |
| **The self-check passes wrong answers** | "Groundedness ✓" on false stock; "The response is accurate" on RM15 | The only quality signal points the wrong way |
| **Guardrails only work if you already know the failure** | Aisha: with the bulky rule, 0 wrong; without it, 3 of 6 | The merchant learns what to write from the incident |
| **Scenarios can't act** | Linh: fired 3 of 3, resolved 0 of 3; order data exists in the inbox but not for the agent | Scenario prompts alone won't fix Ho Chi Minh City |
| **Escalation is one fixed message** | No routing (Nattaya's advisor), no safety line; one silent no-reply | The handoff moment is uncontrollable, and once it was missing entirely |
| **Voice rules: Thai yes, Vietnamese no** | ค่ะ 9 of 9 with a rule; "shop" 1 of 9 with a rule; Malay mix ignored (v1) | Free-text voice rules are a lottery by language |

## Product scorecard (1–5)

| Area | v1 | v2 | Change and evidence |
|---|---|---|---|
| Answer quality with good knowledge | 5 | 5 | Nattaya's and Linh's FAQ answers were accurate and on brand |
| Harm guardrails by default | 5 | 5 | Pregnancy, skin reaction, diabetes: all careful with zero configuration |
| Language and register | 3 | 3 | Vietnamese and unaccented input fine; Vietnamese self-reference ignored |
| Knowledge ingestion and feedback | 2 | **1** | A PDF half-read with "Completed" and no preview |
| Scenario authoring | 2 | 2 | Easy to write; can't act; can make false promises worse |
| Testing and readiness | 1 | 1 | Unchanged, plus a silent no-reply |
| Fixing mistakes | 2 / 4 | 2 / 4 | Rules instant; facts slow; **order-dependent rules can't be fixed at all** |
| Launch controls | 1 | 1 | Unchanged |

---

## Do the proposed actions close the gaps? (redone across six personas)

Against `01_memo_outline.md`. **Short answer: they close four of the six quotes, one partly, and leave Ho Chi Minh City open.** The v2 tests raise the urgency of the Kuala Lumpur fixes, and show that one deferral (order lookups: "Later") is the gap that matters most.

| Quote | What the tests showed | Proposals that address it | Verdict | What's missing |
|---|---|---|---|---|
| **Bangkok** (Nattaya) | Good agent; no way to know; half the PDF lost silently | 1 Tracker · 3 Draft (step 2 "check what your agent knows") · 4 Readiness score | **Closed, if** step 2 shows what was *read* from uploads, not just the draft | A per-file "what we read" view with parse warnings; handoff routing to a named team; a safety line before escalation |
| **Manila** (Jo) | One unwritten rule; a 1-minute scenario fixed it | 3 Draft from history (rules from her DMs) · 7 Defaults | **Closed** | Nothing new |
| **Kuala Lumpur** (Aisha) | Stale RM15 in 3 of 6 runs; self-check "accurate"; one no-reply | 3 Conflicts flagged · 4 Readiness · 5 Go live small · 7 Defaults · 8 Keep old knowledge live | **Mostly closed** | Conflict check at *answer time*, not only in the draft (relabelling "Groundedness ✓" isn't enough); run readiness questions several times; a default against internal names and exposed conflicts; **if the agent doesn't reply within N seconds, hand to a human** |
| **Chiang Mai** (Pranee) | Thai fine; voice drift; no reassurance | 1 Tracker step 4 (voice, incl. Thai gender) · 2 Plain language | **Partly closed** | Interface language chosen at signup; an explicit "replies in your customers' language" message; voice as *fields* (gender, self-reference), since free text failed for Vietnamese |
| **Jakarta** (Budi) | Would ship false stock; setup longer than his windows | 7 Defaults (never state stock) · 9 Campaign mode · 10 Sale-period prompt · 1 Tracker | **Closed on the agent; the stall is unproven** | The "finish after the sale" reminder must go out by email, LINE or WhatsApp; the tracker only helps once he's back |
| **Ho Chi Minh City** (Linh) | FAQ fine; cancels can't be resolved; **a scenario resolved 0 of 3 and added false waits** | 3 Draft (would draft her cancel scenario) · 7 Defaults · "Later: order lookups and actions" | **Not closed.** Drafting the scenario reproduces today's result | **Read-only order status in weeks 4–12, not "Later"**, using order history Zaapi already syncs; a structured handoff with the action ready for staff ("Cancel LS20931: not shipped. [Cancel]"); defaults enforced as a check on every reply |

### Additions, ranked

1. **Read-only order status, moved from "Later" to weeks 4–12.** It's the only change that closes Ho Chi Minh City. It also helps Aisha (every order-status question went to a human), Budi ("resi nya mana") and Jo ("bakit di pa dumadating"). The data is already in Zaapi. Actions like cancel and refund can stay "Later" behind a **one-click staff action inside the handoff**.
2. **"Knows what it can't do" as a check on every reply, not an instruction.** No "I'm checking", no "the system shows", no internal names, no exposed source conflicts: any of these becomes a handoff. The evidence: the stock rule held 1 of 3 as an instruction, and "I'm checking" appeared in four languages.
3. **Show what was read.** Step 2 lists the facts extracted from each file and warns on tables and pages that didn't parse. This is Nattaya's quote, answered.
4. **Readiness replays each question 3 times, including paraphrases, and shows consistency.** Otherwise it will pass Aisha's RM15 one time in three.
5. **Handoff controls on the go-live screen:** who receives each topic, one safety line before escalation, and **a fallback to a human if the agent doesn't reply**. Plus an alert before the free 300 messages run out.
6. **Voice as fields, not free text:** reply language, the shop's gender (Thai), self-reference (Vietnamese "shop"), and a match-the-customer's-mix setting.

**Still supported:** "Deliberately not doing: mandatory scenarios". Linh shows a scenario can't fix what the agent can't see. **Not addressed, and fine to leave:** Zalo (a channel decision, not an activation fix).

**Evidence gaps still open:**
- the re-engagement emails (the test account's inbox);
- a real Shopee or TikTok connection (which would also show whether synced order history reaches the agent);
- Live Chat Support;
- Analyse;
- day-7 trial behaviour;
- campaign timing (PX-02).

**Closed today:** Vietnamese (tested).
