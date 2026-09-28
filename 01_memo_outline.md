# Memo outline: agreed decisions

*Working outline for the memo (≤2 pages). Evidence lives in Appendices A–C and `research/`. Updated 25 Sep 2026 after prompts 05–10.*

## 1. What's actually going wrong

**One line:** Zaapi asks a small business to write an AI agent from scratch, gives them no way to know if it's any good, then only lets them launch all of it at once. It's a services job presented as self-serve. Zaapi's own $1,900 AI Success Kit does these steps by hand.

- **RC1 · No path to a live agent.** Signup lands in the inbox; AI isn't mentioned; setup is unordered tabs.
- **RC2 · Merchants write everything, and nothing tells them if it works.** No readiness view; answers vary run to run; the self-check passes false answers.
- **RC3 · Going live is all or nothing, paid, and done in Flow Builder** (which Basic doesn't have).
- **RC4 · The agent's reach stops at marketplaces and order actions,** and marketplace connections expire without warning.
- **Making them worse:** technical wording, and help articles that are wrong about costs and settings (Appendix C); gaps in mixed-language and Thai voice handling.

## 2. What I'd change: one tiered setup

**Free gets every merchant live and safe. Paid gets them further.**

1. **Step-by-step tracker on a setup home page**, plus a small progress tracker on every screen (see below).
2. **Plain language throughout:** setup screens, Flow Builder and the help centre (see the wording table).
3. **Draft from history.** The merchant connects channels, website and documents and gives Zaapi permission to read past chats. Zaapi then drafts the knowledge, scenarios and tone of voice. Facts, rules and live data (stock, order status) are kept apart, and conflicts are flagged.
   - **Under 300 conversations a month:** all history is used; the draft covers the main topics.
   - **300 or more a month** (the kit's own eligibility line): the draft covers the **top topics** only. The remaining topics are listed with their share of chats: **build them yourself, or upgrade** (plan or AI Success Kit).
   - **No usable history:** a guided wizard in the merchant's own language, plus an AI sweep of their website, listings and quick replies.
   - **Basic plan included.**
4. **Readiness score, free for everyone.** Replay real past questions and show answered / handed off / wrong, with a link to the fix for each.
5. **Simple go-live screen, not Flow Builder:** channel, hours (out-of-hours first), topics, a "draft, you approve" mode and a spend cap. It creates the flow behind the scenes.
6. **Suggested flows from the merchant's own data**, in plain language. The merchant builds them; the ones that need Pro or Advanced are plan upsells.
7. **"Knows what it can't do" defaults:** never state stock or order status without live data; never promise an action it can't take.
8. **Keeping it live:**
   - Warn before a connection expires; reconnect in one click.
   - Fix a bad answer from the answer itself.
   - Keep the old knowledge live while an edit reprocesses.
9. **Campaign mode:**
   - Zaapi's own marketing starts 6–8 weeks before the big sales.
   - Prompt the merchant to connect their busiest channel.
   - Campaign pack of ready-made scenarios, plus a 10-minute out-of-hours launch.
   - "Finish after the sale" reminder.
   - Trial clock pauses for campaign-period signups.
10. **Sale-period update prompt, for live merchants.** About 2–3 weeks before each marketplace sale (and Ramadan), prompt: "11.11 is in 3 weeks. Add your vouchers, promo terms, shipping cut-offs and stock limits." It's a short form in the merchant's language.
    - **Pre-filled where Zaapi already has the information:** broadcasts sent through Zaapi (LINE and WhatsApp promos), marketplace vouchers where the API allows, and last year's campaign questions from history.
    - **Campaign info gets an end date,** so an expired voucher stops being quoted automatically.
    - **Includes the campaign pack of scenarios:** voucher not working, delays, order status, stock.
    - **Evidence:**
      - The persona agents didn't know Aisha's current RAYA20 voucher, and her only listed voucher (MERDEKA15) had expired.
      - Pranee's buy-3-get-1 offer lived only in LINE broadcasts, so the agent said it couldn't find it.
      - Budi's 11.11 voucher question got a generic answer.
      - Voucher and shipping questions spike during sales, when admins have the least time.

**Upsell moments:** at the readiness score (topics not yet covered) and after two weeks live ("AI resolved 22%; a full setup typically reaches 60–80%"). Never before the merchant has seen value.

### The tracker

| Step | Plain name | Done when | Time |
|---|---|---|---|
| 1 | Connect your chats | At least one channel connected, and permission given to read past chats (or the wizard started) | 5 min |
| 2 | Check what your agent knows | Draft knowledge reviewed; conflicts resolved | 10–15 min |
| 3 | Check how it handles requests | Top-topic scenarios reviewed, including when to pass to your team | 10 min |
| 4 | Choose how it sounds | Language, voice (including male or female in Thai), tone | 3 min |
| 5 | See if it's ready | Readiness score run; no open "wrong" answers on top topics | 5 min |
| 6 | Go live, small | Channel, hours and topics chosen; spend cap set | 3 min |
| 7 | First week live | Reviewed flagged answers; kept it on | ongoing |
| ↻ | Get ready for [11.11] | Campaign info added, with an end date. Shown 2–3 weeks before each sale | 5 min |

- Every screen shows a small tracker: "Step 3 of 7 · Next: check how it handles requests". It opens the full tracker on a click.
- Works on mobile, can be resumed, and shows "remind me after 11.11" during campaign periods.
- The upsell list appears at step 5; the two-week result appears at step 7.

### Wording: from → to

| Today | Plain |
|---|---|
| Knowledge Source | What your agent knows |
| Scenario Handling | How it handles requests |
| Personality | How it sounds |
| Deploy / Let AI handle / Let AI Respond / Let AI reply | Go live (one name) |
| Escalate to a human agent | Pass to your team |
| Integrations | Your chat channels |
| "When this scenario should trigger" | "When a customer asks about…" |
| Groundedness ✓ | "Based on your info. Not checked against live stock or orders" |
| "Trigger once every new open chat" | Chosen by the go-live screen; not shown |
| Chunking, H1/H2/H3 | Not needed: the draft is structured for them |

## 3. What I'd do first

| When | What |
|---|---|
| Weeks 0–2 | Data pull: whether switch-offs line up with the free messages running out; active setup time vs days elapsed; go-live by plan; campaign-period signups; connection expiries; **kit vs self-serve outcomes** |
| Weeks 0–2 | Correct the wrong help articles; warn before connections expire |
| Weeks 0–6 | Tracker and plain-language pass; go-live screen; "knows what it can't do" defaults; campaign mode and the sale-period update prompt (both before 11.11 / 12.12) |
| Weeks 4–12 | Draft from history and the readiness score, with the tiering. Start with Shopee (90 days already imported) or LINE |
| Later | Order lookups and actions (Shopify, marketplaces) |

**Deliberately not doing:**
- an AI assistant that redesigns Flow Builder (the go-live screen removes the need for it);
- a percentage-of-traffic slider;
- mandatory scenarios;
- more personality fields;
- translating the help centre before fixing what it says;
- anything that undercuts the AI Success Kit (the free tier caps how much data is used, never quality or safety).

## 4. How we'd know it worked

- **Headline measure:** share of signups live within 7 days and still live at day 30.
- **Measure of value:** Zaapi's own bar, ≥30% of enquiries resolved by AI without a human within 30 days of going live.
- **Early signs:**
  - time to the first AI action;
  - tracker completion by step;
  - share of drafted content accepted;
  - readiness score at launch;
  - share of merchants who launch narrow first;
  - share of live merchants who update campaign info before a sale, and wrong or "not found" answers on voucher and promo questions during it.
- **Commercial:**
  - upsell prompt → kit or plan purchase;
  - kit purchases before vs after the change;
  - AI message revenue per activated merchant.
- **Guardrails:** wrong-answer rate, handoff rate, switch-offs within 72 hours, lapsed connections.
- **Wrong if:**
  - drafts don't speed up going live;
  - the readiness score doesn't predict staying live;
  - narrow launches switch off as often as full ones;
  - switch-offs line up with free messages running out (then it's pricing, not trust);
  - **kit purchases fall** (then the free tier is too generous).

## Prototype

1–2 screens: **the setup home with the tracker**, and **step 5, "See if it's ready"**: readiness score, top topics covered, the list of topics not yet covered with its "build it yourself / upgrade" choice, and the small tracker on screen.
