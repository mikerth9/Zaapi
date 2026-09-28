# Prompt: prototype fixes after the memo check

Paste everything below the line into the prototype session (working folder `/Users/miker/Documents/Zaapi`).

---

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
