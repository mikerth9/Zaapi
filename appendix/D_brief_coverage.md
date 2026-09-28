# Appendix D — Does the evidence cover everything the brief says?

*A line-by-line check of the take-home brief against what we've tested: the walkthrough (`[product]`), your walkthrough (`[mike]`), the persona tests (`[persona]`), the help centre (`[help]`) and the pricing page (`[pricing]`). Status key: **Reproduced** = we saw it happen · **Explained** = we found the mechanism on screen · **Partly** = some of it is evidenced · **Open** = needs data or wasn't testable. The last section lists what's still missing and how to close it.*

## 1. The six merchant quotes (section 04)

| Quote | Status | What we found | Where |
|---|---|---|---|
| **Bangkok, beauty, ~3,000/mo:** "I added our FAQ document but I don't know if that's enough. How do I know it's ready? I don't want to find out from a customer." | **Explained** | Nothing in the product ever says "ready": no coverage view, no rollup, per-message "Show thinking" only. A plain Q&A FAQ uploads and says "Completed", with no view of what was extracted. The same question gives different answers across runs, and the self-check passed a false answer as "Groundedness ✓". | H8; RC2; `[product]` `[persona]` |
| **Manila, fashion, ~800/mo:** "I wasn't sure what I was supposed to write… our policies are just things we know. Nobody has written them down." | **Reproduced** | Joanna's cancel rule lived only in her head, so the agent cited "No returns" and handed off (J5). Budi's knowledge was canned quick replies, which became false facts (B1). The only authoring guidance is "use proper headings". | H3, H6; RC2; `[persona]` |
| **Kuala Lumpur, home goods, ~5,000/mo:** "We turned it on Friday. On Saturday it told a customer the wrong thing about our shipping to East Malaysia, my team panicked, so we turned it off." | **Partly reproduced** | With stale macros and website text saying "flat RM15", the agent **drafted RM15 once**, and the self-check passed it as grounded. Only a merchant-written rule stopped it. Other runs gave the correct RM18, or escalated while exposing "an inconsistency in our current information" and an internal name ("Farah"). The "turned it on Friday… turned it off" part is explained by all-or-nothing launch (two templates, no share dial) and slow fact-fixing (6–8 minutes of reprocessing, fix held 1 of 3). *Note: this merchant did go live, so it belongs with the 9 switch-offs, not the "never live" group.* | H8, H9, H10; RC2, RC3; persona log addendum |
| **Chiang Mai, supplements, ~1,200/mo:** "I set it up in English because that's what the form was in. But 90% of our customers write in Thai. I'm not sure whether that matters." | **Explained (capability fine; reassurance missing)** | With no language setting, the agent replied in Thai every time. But the default is stated only once, in small print; Thai help searches didn't find it; and gender forms drifted (ครับ, ผม) until a rule was added. In your session the setup screens were stuck in Thai, so interface language is assigned, not chosen. Her "I'm not sure whether that matters" is exactly the gap: nothing tells her. | H11; `[product]` `[persona]` `[mike]` `[help]` |
| **Jakarta, electronics, ~9,000/mo:** "I signed up and then it was Double 11 and I had no time. It's been sitting there since November." | **Open (mechanism partly explained)** | There's no path or nudge from signup to AI setup (lands in the inbox; the start guide has no AI step; the QR code pulls you out of setup), and best-case setup took 60–90 active minutes against Budi's 20–30-minute sessions. **Not tested:** whether campaign timing drives the stall, or whether Zaapi sends any re-engagement emails. | H1, H2; RC1; `[product]` `[mike]` `[help]` |
| **Ho Chi Minh City, fashion, ~2,500/mo:** "I skipped the scenarios part — I thought the knowledge would be enough. It answers questions fine, but the moment someone asks to cancel an order it just says it'll pass them to the team. Which is us." | **Reproduced, and the fix shown** | Nothing prompts scenarios, and the agent handles most things without them, so skipping looks safe. Cancels went to a human without a scenario (Joanna J5). A one-minute scenario fixed it (it offered an exchange or store credit, with no handoff). Scenarios still can't *act* on an order (cancel or refund need Advanced-plan webhooks). | H5, H7; RC2, RC4; `[persona]` `[pricing]` |

**Evidence bias to keep in the memo (Appendix A):** all six quotes come from accounts the commercial team deals with (800–9,000 orders a month), with no successful merchants for contrast and no small SMBs. **None of our personas is Vietnamese**, and no Vietnamese messages were tested.

## 2. What the brief says about the product (section 02)

| Brief says | Status | Reality |
|---|---|---|
| "Six steps… the sequence a merchant works through" | **Contradicted** | Tabs, not a sequence: Train (Knowledge, Scenarios, Personality), then Test and Deploy, with no order, progress or checklist. Channel connection happens in Helpdesk onboarding, before AI is mentioned. `[product]` |
| Step 1: connect a channel; "most merchants have already done this… for our Helpdesk" | **Explained, with a twist** | A website chat widget is **auto-connected on signup**, so "connected ≥1 channel" may count merchants who did nothing. `[product]` |
| Step 2: "paste text, upload files, or point us at a URL" | **Confirmed, with caveats** | All three exist. PDFs work despite the copy. Marketplace URLs are warned against, accepted, and then fail with a misleading error. An Instagram crawl says "Completed" with no view of the content. `[product]` `[persona]` |
| Step 3: persona: "name… language, tone, how formal, things it must never say" | **Partly** | Name, a 150-character style box and a 250-character rules box. **No language field** (the default follows the customer); one personality per channel; no AI-disclosure signature by default. `[product]` |
| Step 4: scenarios, "including when to hand the conversation to a human" | **Confirmed** | Instruct or escalate only. Escalation wording is fixed. Matching is loose and phrasing-sensitive. `[product]` `[persona]` |
| Step 5: test mode | **Confirmed, with gaps** | Free chat, per-message "Show thinking", no coverage view, no image input; first message after an account switch dropped (3 of 3). `[product]` `[persona]` |
| Step 6: "turn the agent on for a chosen channel, and set what share of incoming conversations it handles" | **Contradicted** | **No share control exists.** Two all-or-nothing Deploy templates in Flow Builder; narrowing means building flow logic (Pro plan and up). `[product]` `[pricing]` |
| "Support is available throughout" | **Not tested** | A "Live Chat Support" icon is in the nav rail on every screen. Not used, since that would contact Zaapi staff. `[product]` |
| "Enterprise accounts get hands-on help… SMB merchants are largely on their own" | **Confirmed** | Dedicated account manager and Flow Builder consultation are Enterprise-only; SMBs can buy an "AI Success Kit" (results in 60 days). `[pricing]` |
| "Half an hour in the product will tell you far more…" | **Contradicted for setup** | 60–90 active minutes for the best case, plus 1–9 minutes of knowledge processing and about 20–30 seconds per test reply. `[product]` `[persona]` |

## 3. The funnel and its notes (section 03)

| Brief figure | Status | Explanation from the evidence |
|---|---|---|
| Connected ≥1 channel: **94** | **Explained** | The widget auto-connects; connection is Helpdesk onboarding, not AI setup. |
| Added any knowledge: **79** | **Partly** | No path leads to AI setup (RC1). Also: the system seeded a "Quick replies" source on this account (probably on all), so "added any knowledge" may count it. *Data question.* |
| Set a persona: **71** | **Explained** | Personality is optional: agents answer without one (Budi). |
| **Wrote ≥1 scenario: 38** (the biggest drop) | **Explained** | Nothing prompts scenarios; the agent handles angry customers and unknowns without them, so skipping looks safe; writing them is prompt engineering, with invisible and phrasing-sensitive effects (H5, H6). |
| Ran ≥1 test: **66** (more than scenarios) | **Explained** | Tabs, not a sequence: Test is reachable without scenarios. |
| Went live: **61**, median **19 days** | **Partly** | All-or-nothing launch in Flow Builder; no readiness signal; trial countdown and metered AI tokens (300 free, then $40 per 1,000). Elapsed time can't be measured in a walkthrough. |
| Still live at 30 days: **52**; of 9 switch-offs, most within **72h** | **Partly, plus a new alternative** | A first mistake is public (all-or-nothing), and fixing a fact is slow and unreliable while switching off is instant. **New alternative:** the free 300 messages running out could register as a "switch-off". *Data question.* |
| Median **4 days** to first setup step | **Explained** | You land in the inbox, with no dashboard, no steps left and no nudges; the QR code pulls you out of setup; the start guide has no AI step. `[product]` `[mike]` `[help]` |
| "Strongly correlated with staying live" (scenarios) | **Partly** | Scenarios fix the cancel case and keep rules explicit (Joanna, Pranee). But selection bias is plausible (Appendix A) and needs data. |
| Messaging channels faster than marketplaces | **Explained** | Marketplace URLs can't be crawled (misleading error); order actions and marketplace triggers are Advanced-only; no Bahasa, Vietnamese or Tagalog help centre. **Not tested:** a real Shopee/Lazada/TikTok connection and its imported history (H4). |
| Worse activation for campaign-period signups | **Open** | Needs data and PX-02 (campaign calendar). |

## 4. The commercial framing (section 01)

| Brief says | Status | Evidence |
|---|---|---|
| Live and kept live → higher renewal | **Open** | Data only. |
| "The ones who stall rarely come back… on their own initiative" | **Partly** | No in-product re-engagement seen: no dashboard, no nudges, no "steps left" `[product]` `[mike]`. **Not checked: emails.** The test account's inbox would show whether Zaapi sends any setup nudges over the next few days. |
| "Paying for a platform they're only half using" | **Explained** | The trial countdown and "Subscribe now" start on screen one; AI replies are billed separately as tokens, so an un-launched agent costs nothing extra, but a launched one costs per message with no cap `[product]` `[pricing]`. |

## 5. Still missing, and how to close it

| Gap | Why it matters | How to close it | Effort |
|---|---|---|---|
| Re-engagement emails | Tests "rarely come back on their own" (H1) | **Check the test account's inbox** over the next 3–7 days for Zaapi setup or AI nudges | You, a few minutes |
| Campaign timing | Jakarta quote; H2 | PX-02 in Perplexity + data question 9 | Perplexity, 10 minutes |
| Real marketplace connection and history | H4, H12; half the channel mix | Connect a Shopee or TikTok Shop test store (OAuth: yours to do) and look for imported history in setup | Needs a seller account |
| Vietnamese | HCMC is the only Vietnam data point | Run 5 Vietnamese messages on an existing agent | Me, 10 minutes |
| "Live Chat Support" | "Support is available throughout" | Open it and ask a setup question; time the reply | You (contacts Zaapi) |
| Analyse and open chats | H10: can a merchant find the bad answer from Saturday? | Visit Analyse after test chats | Me, 5 minutes |
| Day-7 trial behaviour | Alternative explanation 1; token billing | Revisit the account after the trial ends | You, in 6 days |
| Failed and Pending pill colours; hover states | Prototype polish only | Next time a source fails or is pending | Minor |
