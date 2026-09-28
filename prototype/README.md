# Zaapi AI agent setup: working prototype

Deliverable 2 of the take-home. It shows the memo's main change working:

> Zaapi drafts the agent from what the merchant already has, and shows them whether it's ready before any customer sees it.

- **File:** `zaapi_setup_prototype.html`, one self-contained file (about 300 KB), built 28 Sep 2026 and fixed after the memo check the same day (entry 21).
- **Private link:** https://claude.ai/artifact/Phpqmhaiv2d9dmMaLwmqjM (private until you share it).

## How to open it

- **Offline:** double-click `zaapi_setup_prototype.html`. It opens in any modern browser and makes no network requests. The CSS, the JS, the data and the six photos are all inside the file.
- **Online:** use the private Artifact link.
- **Size:** it's built for a laptop. It looks best at 1440×900, works at 1280×800, and nothing overflows at 1024 wide.

**Demo controls** are in the dashed box at the top right. They aren't part of Zaapi.
- **The merchant name** opens the switcher: six merchants, one per brief quote, ordered by impact score. It also has "How we score impact" and the demo shortcuts:
  - Jump to step;
  - Complete all steps (shows the dashboard);
  - Reset all merchants;
  - About this prototype.
- **Hide notes / Show notes** collapses the presenter sidebar to a thin tab.
- **Reset this merchant** puts the current merchant back to the start.

Each merchant keeps their own progress when you switch. The last merchant you used is remembered in the browser if storage is allowed. The prototype works without it.

## What's simulated

| Label | Meaning |
|---|---|
| **Sourced** | Taken from the persona tests or the brief: the quotes, failure examples, test questions and "before" readiness scores. |
| **Demo data** | Made up to be plausible (see below). |
| **Projected · weeks 6–12** (dashed purple chip) | Depends on read-only order status, which the memo schedules for weeks 6–12. It affects Aisha's "Where's my order" topic, and Linh's cancel topic, "after" score and first week. |
| **Proposed** | Something the memo suggests adding. The LINE history export inside the AI Success Kit is the main one. |

**Demo data in this build:**
- **Chats and topics:** chat counts, topic shares and the "Drafted from N of your replies" counts. Only Jo's counts come from the context pack.
- **Drafted rules:** the wording for Nattaya's, Aisha's, Linh's, Budi's and Pranee's topics. Where the context pack gives the rule, I used it.
- **Readiness:** the "after" scores, the by-topic split (worked out from each merchant's totals, and labelled on screen), and the scores after a partial fix (see below).
- **Customer questions:** the ones in the live question stream, and the week-one review items.
- **Week one and the dashboard:** all the numbers. Since entry 21 they follow one method:
  - weekly chats = monthly ÷ 4.3;
  - handled = weekly chats on the live channel(s) × the go-live estimate;
  - resolved = handled × the resolution rate;
  - passed on = handled − resolved.

  | Merchant | Live on | Handled | Resolved | Passed on | Other week-one figures | AI share of all chats on the live channel(s) |
  |---|---|---|---|---|---|---|
  | Jo | Instagram + Facebook | 27 | 17 (64%) | 10 | 108 of 300 free messages used; 2 flagged | about 26% |
  | Nattaya | LINE, out of hours | 68 | 48 (71%) | 20 | 3 flagged | about 16% |
  | Aisha | WhatsApp, out of hours | 140 | 81 (58%) | 59 | 128 approved as-is, 12 edited; 0 East Malaysia rate errors | about 14% |
  | Linh | Facebook | 66 | 34 (52%) | 32 | 6 cancel requests with the button ready; 4 "I'm checking" replies blocked | about 17% |
  | Budi | Shopee, out of hours, 11.11 week | 470 | 287 (61%) | 183 | 0 stock claims; 96% response rate | about 11% |
  | Pranee | LINE, evenings and night | 55 | 37 (68%) | 18 | 12 dosage questions answered; 0 medical claims | about 24% |

- **Step 1 chat counts** add up to each merchant's monthly total (90-day counts ÷ 3, WhatsApp's 6 months ÷ 6, LINE days scaled to a month). Linh's total is now about 1,700 a month.
- **Nattaya's Glow Club birthday discount:** "10% off" is filled in by a "Fill in (demo)" button.
- **Previews:** Budi's Bahasa preview, and the English and Malay preview variants.
- **Connection reminders:** "Re-authorise in 12 months" for Nattaya, Linh, Budi and Pranee comes from Shopee's 12-month expiry. Aisha's 11 and 5 months come from the context pack.

**What isn't real:**
- **No AI runs.** Loaders are timers of 1 to 5 seconds, and results are preset.
- **Uploads aren't read.** The drop zone accepts any file and says so. "Use sample files" loads each merchant's preset files.
- **Nothing is sent anywhere.** "Talk to us", "Subscribe now", the other rail items and "Add a channel" show a "not part of this prototype" note.

**AI Success Kit facts** come from Zaapi's pricing and AI services pages, read on 25 Sep 2026 (`research/walkthrough_log.md`, Addendum C):
- $1,900, over 60 days;
- the guarantee: at least 30% of enquiries resolved within 30 days of going live, or a full refund;
- the Pro or Advanced plan, with 300+ conversations a month;
- 10,000 AI message credits.

## How the scores behave

Readiness reflects what's fixed at the moment you run the test.
- **Nothing fixed:** you get the merchant's "before" score from the persona tests.
- **Every wrong answer fixed:** a re-run gives the "after" score.
- **Some fixed:** the score sits proportionally in between, and the verdict says how many fixes are left.

So to show a "before" score, run step 5 before fixing anything. The click paths below do that. If you set up in strict step order, some fixes happen in steps 2–4 and the first run already scores higher. That's the product working, but it hides the jump.

## Two-minute click paths

Notes on every path:
- **Sidebar and tracker:** the sidebar explains every screen. "Changes shown" ticks off the 10 changes as you go.
- **Missing a step?** "Jump to step" in the switcher gets you anywhere.
- **Skipping to the end:** "Complete all steps" goes straight to the dashboard.

### 1. Aisha, Rumah Kita, Kuala Lumpur (impact 7.6, shows the most features)

Her quote: turned on Friday, off on Saturday, after a wrong East Malaysia shipping answer.

1. **Setup home.** Point out:
   - the 7 steps with time left;
   - "Nothing is sent to customers until you choose Go live";
   - the plan card ("Your free setup drafts your top 6 topics"), then open **What's in the AI Success Kit** and close it.
2. **Step 1.** Press **Connect all**, then **Read my past chats**.
   - WhatsApp's "Share your last 6 months of chats" is ticked: 15,300 chats found.
   - The result: about 3,900 chats a month, so the top 6 topics are drafted.
3. **Step 2.** Press **Use sample files**. Three sources are read, and there are **3 things to settle**. Leave them for now: Continue stays blocked.
4. **Step 5 (via Back to setup, or "Jump to step").**
   - Press **Start the test**. It replays 120 questions with live counters.
   - Score **70**, "Fix 3 answers before you go live".
   - Point at the RM15 answer, with **"Today's check: Groundedness ✓"** struck through beside **"Readiness: Wrong"**.
5. **Fix this answer** opens the conflict drawer on step 2, with the recommended answers already picked.
   - Choose **Ask a teammate**. After about 3 seconds Farah confirms.
   - Open **Your website still says RM15** and press **Copy updated text**.
   - Open part 3 to show which source wins, and the "pass it to your team" setting.
   - **Save and re-test**: 18 of 18. Then **Back to your test results**.
6. **The other two Fixes:**
   - Fix 2 turns on the human fallback.
   - Fix 3 opens the returns conflict. Save it (9 of 9).
   - Then go back and **Re-run test**: **88**, "Ready for a small launch".
7. **Step 2 again.** Settle the staff-name item (**OK**). Step 2 ticks on the home tracker.
8. **Step 3.** Show the draft card with "Projected · weeks 6–12": until then the agent passes the order number to the team. Then show the **More topics** row with **Have our team build these**. Then **Accept all** and **Continue**.
9. **Step 4.** "Picked from your chats" on every field, and the live WhatsApp preview. Change the language to **Always Malay** and the preview changes. Then **Continue**.
10. **Step 6.** WhatsApp only, out of hours. **Shipping to East Malaysia is excluded**; it stays with her shipping team. About 24% of WhatsApp chats. Then **Go live**.
11. **Step 7** (simulated week one). Show:
    - 140 chats handled, and the line under the cards: about 14% of all WhatsApp chats resolved by AI, against the 15% first-month target;
    - 0 East Malaysia rate errors;
    - the reply check that blocked the staff name;
    - the Shopee and Lazada reminders;
    - the 11.11 prompt, then **Add sale info** (ticks change 10).
    **Review answers**, mark both, then **Finish setup**.
12. **Dashboard.** Point out:
    - live status per channel;
    - the review queue;
    - the sale prompt;
    - "4 more topics you could add" with the Kit.

### 2. Jo, Loveli Closet, Manila (impact 9.0)

Her quote: "our policies are just things we know".

1. **Home.** The plan card says "Your free setup drafts everything" (about 280 chats a month).
2. **Step 1.** **Connect all**, then **Read my past chats**. Instagram has 480 chats and Facebook 360. TikTok Shop is optional.
3. **Step 2.** Her rules were read from her DMs:
   - shipping by island;
   - COD in Metro Manila only;
   - reservations held for 24 hours;
   - defective items only;
   - stock is live data and never stated.
   Settle the **reservations** conflict with "24 hours; pass regulars to me".
4. **Step 5.** **Start the test**: 77. The two wrong answers are the cancel after GCash and the stock check. Press **Fix** on both. That accepts the cancel topic and turns on "Never confirm stock". Then **Re-run test**: **92**.
5. **Step 3.** Open **Cancel after payment**: "Drafted from 14 of your replies", with the Taglish sample reply.

### 3. Nattaya, Glow Lab, Bangkok (impact 8.4)

Her quote: "How do I know it's ready?"

1. **Step 1.** LINE shows the note that it can only read the 18 days since connecting, with the optional Kit export.
2. **Step 2.** **Use sample files**. The PDF reads **"Read 7 of 12 pages"**, with two warnings.
   - Don't fix them yet. Press **Pass these to your beauty advisor** on the gaps card, or leave it for step 5.
3. **Step 5.** **Start the test**: 89, "Almost ready: fix 3 answers".
4. **Fix the three answers:**
   - Fix 1 opens **Confirm these 5 products**. Press **Fill the gaps (demo)**, then **Confirm 5 products**. You're taken back to the results.
   - Fix 2 routes to the beauty advisor.
   - Fix 3 opens the **Glow Club** facts. Press **Fill in (demo)**, then **Confirm**.
5. **Re-run test**: **96**.

### 4. Linh, Linh Studio, Ho Chi Minh City (impact 7.2)

Her quote: "it'll pass them to the team. Which is us."

1. **Step 1.** Shopee and TikTok Shop show "orders synced ✓". Zalo says "Not supported yet. We've noted your request."
2. **Step 5.** **Start the test**: 53. Wrong answers: "I'm checking your order now", "let me check stock", "not in the system".
   - The **Reply check** card below shows the blocked "I'm checking" line and what went out instead.
3. **Fix all three:** order status (projected, weeks 6–12), "Never confirm stock", and accept the exchange topic. **Re-run test**: **81** (projected).
4. **Step 3.** The order-status toggle is marked **Projected · weeks 6–12**. Open **Cancel an order** to show:
   - "Order LS20931 · Not shipped · Shopee";
   - the staff **Cancel order** button in the handoff.
5. **Step 4.** "How your shop refers to itself: shop" is a field. The note underneath: a free-text rule held in 1 of 9 replies.
6. **Step 7** (use **Complete all steps**, then open First week live from the tracker). The reply check blocked 4 "I'm checking" replies, and 6 cancel requests went to staff with the button ready.

### 5. Budi, GadgetKu, Jakarta (impact 7.0)

His quote: "then it was Double 11 and I had no time".

1. **Home.** Point out:
   - the trial banner: "Trial paused until 18 Nov (sale period)";
   - the campaign mode banner: 11.11 in 3 days, a 10-minute campaign agent;
   - step times that add up to 10 minutes.
2. **Step 2.** The **3 canned lines** ("Ready stok kak…") are flagged, and the defensive reply has a softer version.
3. **Step 5.** **Start the test**: 68. Fix the stock claim by flagging the canned lines, and use the softer reply. **Re-run test**: **86**.
4. **Step 6.** Shopee, 22:00–08:00, the 5 campaign topics. "I approve replies first" is off, with a daily sample instead. Tick **Remind me to finish setup on 14 Nov** (WhatsApp and email).
5. **Step 7 or the dashboard.** "11.11 is over. Finish setup: 4 more topics and TikTok Shop, about 15 minutes."

### 6. Pranee and Fon, Baan Samunprai, Chiang Mai (impact 6.2)

Her quote: "I'm not sure whether that matters".

1. **Home.** Switch the page to **ไทย**, then back.
2. **Step 1.** LINE has 12 days (310 chats). The note explains why LINE history can't be read, and offers the Kit's export as optional. The result: "We'll ask you a few questions instead."
3. **Step 5 first.** **Start the test**: 85.
   - The promotion was "not found", and the reply used the male ครับ.
   - The **Safe** example: no cure claim for diabetes.
   Press **Fix** on both. That sets the shop to speak as a woman and adds the promotion. **Re-run test**: **90**.
4. **Step 2.** The guided questions: one at a time, in Thai with an English toggle, with quick answers. Each answer becomes a fact or rule card on the right.
5. **Step 4.** The green line: **"92% of your chats are in Thai. Your agent will reply in Thai, even though you set up in English."** Show the **Your shop speaks as: A woman** field.

## Fixes after the memo check (entry 21)

Made on 28 Sep 2026 from `prompts/prototype_fixes_prompt.md`, in both `context/03_merchants.md` and the HTML.

1. **Chat numbers add up.**
   - Step 1 counts now add up to each monthly total. Changed: Nattaya's four channels, Aisha's WhatsApp (15,300 over 6 months), Linh's three channels (total now about 1,700), Pranee's LINE (270).
   - Week-one numbers follow the method above. Before, they were 4–10× what the volumes allowed.
   - Aisha's approved and edited replies now add up to what was handled: 128 + 12 = 140.
2. **Week one links to the memo's value measure.** A quiet line under the stat cards gives the share of all chats on the live channel(s) that the AI resolved, against the 15% first-month target. The dashboard repeats it in one line.
3. **Order status is weeks 6–12.**
   - Every order-status chip reads "Projected · weeks 6–12".
   - Aisha's "Where's my order" sample reply now passes the order to the team, with a line on what changes in weeks 6–12. Her step 6 row says the same.
   - Aisha's drafted rule for that topic now says the same. It had also claimed the agent shares order status.
   - Her "Order dah ship ke?" test question now shows as passed to the team.
4. **The readiness split no longer assumes order status.**
   - Order-status questions count as "Passed to your team" unless the toggle is on.
   - Topic question counts follow share of chats, with the rest under "Other".
   - The headline percentages and scores are unchanged.
   - **One conflict in the brief for this fix:** Aisha's 27% handoff rate is 32 of 120 questions, but "Where's my order" has 37. So 32 are shown as handoffs and 5 as general delivery questions answered correctly, and the other topics show no handoffs before the fixes. Passing all 37 would need the handoff rate at 31%, which changes the headline.
5. **Rewordings.** The step 5 intro, the running screen and the run line now say "3 times each, with rewordings", using each merchant's own question count. Pranee's standard set gets the same.
6. **Basic plan.** The plan card's second line reads "Free on every plan, including Basic." The Kit panel's Free setup column adds "Every plan, including Basic." The Kit's own Pro or Advanced line is unchanged.
7. **Thai.** Not changed. The table below lists every Thai string for a Thai speaker to check.

Also: the reply-check example in Linh's step 5 was labelled "Projected". The reply check isn't order status, so it's now labelled "Proposed", the memo's own change.

## Change after QA (entry 23): LINE for every merchant

Made on 28 Sep 2026 after the QA pass. LINE Official Account is now a connect option on every merchant's step 1, alongside the other channels, not only for Nattaya and Pranee.

- For Jo, Aisha, Linh and Budi the tile is marked **Optional** and says: LINE only shares chats from the day you connect, so nothing older comes across; LINE's own Chat package export costs ฿555 a month; the AI Success Kit includes one month of it. A link opens the Kit panel.
- Once connected it says LINE shares chats from today onwards, so the draft comes from the other channels and LINE is added as chats arrive. It counts 0 chats and doesn't change the tier or the share bar.
- Nattaya's and Pranee's LINE notes now state the export's cost as well.
- The Kit panel lists the LINE history export for every merchant, still marked "Proposed", with the ฿555 a month cost.
- The presenter sidebar's LINE line now shows for every merchant.
- **Step 2 routes row:** step 2 now opens with three cards, "Upload files", "Answer a few questions" and "Let Zaapi draft it", with the route that applies to the merchant highlighted and the plan limit stated on the third card. The setup home's step 2 line matches. One new Thai string (the step 2 line) is added to the table below.
- **Channel order and two more cards:** the grid now runs LINE, WhatsApp, the merchant's own channels, Gmail, website widget, for every merchant, in line with Zaapi's South East Asia focus. WhatsApp and Gmail are optional tiles where they aren't the merchant's channel, each with their own three bullets (WhatsApp can share 6 months of chats; Gmail shares 7 days of email). Aisha's WhatsApp keeps its 6-month checkbox and 15,300 chats.
- **Tile copy, second pass:** every unconnected channel tile now shows three bullets (message customers through Zaapi; we'll find your top topics for AI to handle; key facts go into your knowledge base) instead of a sentence. The LINE tile has its own three bullets and a purple upsell strip, "AI Success Kit includes one month of LINE history. Saves ฿555.", with a See the Kit button. Opening the Kit from a LINE tile adds a banner at the top of the panel spelling out the saving, and the Kit's LINE row carries a "Saves ฿555" chip. Nattaya's and Pranee's LINE tiles get the same strip after their chats are read, and Pranee's guided-questions banner has a button with the saving.
- Source of truth updated in `context/03_merchants.md`, `context/02_flow_and_screens.md` and `context/07_sidebar_copy.md`.

## Decisions made while building

**Where the look and the content came from**
- **Look:** the Stitch designs (`stitch/*.png`).
- **Data, wording and behaviour:** the context pack.
- **Sidebar text:** `07_sidebar_copy.md`, word for word.
- **Build:** one file, hand-written CSS, no framework.

**The 12 Stitch design decisions** in `stitch/NOTES.md` were all adopted, with these changes:
- **Placeholder numbers** use real data:
  - the step 2 summary counts the items actually shown (7 for Aisha, not "42");
  - "about 85" is each merchant's real "after" score (88 for Aisha).
- **Weekly performance check** is dropped. It implied a Zaapi service we can't back up.
- **The presenter sidebar is on every screen**, styled as notes, as the context pack asks. On the conflict drawer it shows the conflict's "The change" and "Why", with step 2's "Today" and "Should move".
- **Time left counts down** as steps are done. Step times per merchant add up to about 25 minutes, and 10 for Budi's campaign mode.

**Changes from the Stitch screens, and why**
- **Step 1 starts with channels not connected**, so the "Reading your chats…" simulation can run. "Connect all" speeds this up in the demo.
- **Stitch's invented content is replaced** with context-pack data. That covers the handles, the WhatsApp number, the COD and voucher rules (WELCOME10, FPX), "Routing: Automated look-up", the review-queue replies, "214 / 233", and Pranee's example facts.
- **"Resolve the 3 errors to unlock full launch"** became "Fix the wrong answers, then re-run", to keep banned words out.
- **Step 3 has a "Rules for every topic" card**, with "Never confirm stock" as a recommended toggle. The context pack's fixes for Jo, Linh and Budi need somewhere to switch it on.
- **Step 5 lists the wrong answers from the last run.**
  - The first open one is expanded. The others are rows with a Fix button.
  - A fix made after a run shows "Fixed · re-run to check".
  - The by-topic table is labelled demo data.
- **Step 6: the launch estimate updates** as you change topics or hours, and is labelled an estimate. For Aisha, "Shipping cost and time" stays on as a drafted topic, and East Malaysia is a separate excluded row. So it shows 6 on and 1 kept with the team, where Stitch showed 5 and 1.
- **Step 7:**
  - "108 of your 300 free messages used" only appears for Jo. The other merchants' volumes go past 300 free messages.
  - "Sync status healthy" and "All tokens active" are dropped. They weren't in the context pack.
- **The dashboard's fourth stat** follows each merchant's week-one data, not "replies blocked".
- **Kit panel:**
  - The guarantee and inclusions are reworded to match the pricing page.
  - "30 days of live tuning" became "30 days live, measured".
  - 10,000 credits were added.
  - The LINE export only shows for the LINE merchants, marked Proposed.
- **The AI Agent sub-menu** (sidebar toggle, or ⌘B) uses the plain step names under Train, Launch and Monitor. Today's labels (Knowledge Source and the rest) aren't used, per the wording rules.
- **Rail items other than AI Agent** show "Not part of this prototype" as a tooltip, and as a note if clicked.
- **Budi's "I approve replies first" is off**, with the context pack's daily sample instead.
- **Below 1180px wide** the two-column layouts stack, so 1024 doesn't overflow.
- **Pranee's Thai/English switch** translates the setup home. **The Thai strings are my own and should be checked by a Thai speaker before the interview.**
- **The top banner is 52px**, as in `design_system.md`, not Stitch's 48px.

## Checks run (28 Sep 2026)

**Re-run after the entry 21 fixes:**
- **Click-through:** all six merchants through every step, using the real buttons, with no console errors. The only network request was the HTML file.
- **Scores:** unchanged at Jo 92, Nattaya 96, Aisha 88, Linh 81, Budi 86 and Pranee 90. Aisha's first run still gives 70.
- **By-topic tables:** they add up to the headline numbers for all six merchants, before and after the fixes.
- **Consistency:** step 1 counts are within 3% of each monthly total, and week-one handled figures are within 2% of weekly chats × the go-live estimate.

**Original build:**

- **Full click-through, all six merchants**, driven through the real buttons in the browser pane:
  - connect and read chats;
  - files or guided questions;
  - accept topics and set the voice;
  - run the test, apply every Fix, re-run;
  - settle everything left in step 2;
  - go live, review week one, finish, then the dashboard.
  - Each re-run hit the "after" score: Jo 92, Nattaya 96, Aisha 88, Linh 81, Budi 86, Pranee 90.
  - No console errors.
- **Also tested:**
  - the sale form, impact table, About panel and Kit panel;
  - Build it yourself;
  - the notes toggle, Jump to step and the sub-menu;
  - rail tooltips, Reset and Reset all;
  - the Thai home and Complete all steps.
- **Network log:** only the HTML file was requested.
- **No `http` anywhere in the file**, so there are no external `src` or `href` values.
- **Screenshots at 1440×900**, compared with each Stitch PNG. Also checked at 1280×800 and 1024.
- **Banned-phrase check** (from `07_sidebar_copy.md`), run on the whole file:
  - **Command:** `grep -o -i -n -E "seamless|effortless|empower|unlock|leverage|robust|game-changer|supercharge|streamline|cutting-edge|revolutionis|delve|holistic|synergy|elevate|harness|journey|landscape|in today's|it's not just|not only|more than just|whether you're" zaapi_setup_prototype.html`
  - **Result:** no matches.
  - **Em dashes:** one, inside Linh's verbatim brief quote (the allowed exception).
  - **Exclamation marks:** they appear only inside simulated customer-facing replies taken from the context pack (Jo's and Aisha's previews, Linh's "nhé!"). None are in interface copy.

## Thai to check before the interview

Every Thai string in the file. "Source" says whether the text came from the persona tests via `context/03_merchants.md`, or was written by Claude. Prices in baht (฿890 and so on) and the LINE export price (฿555) are left out.

**Pranee's setup home, with the ไทย/English switch set to ไทย**

| Thai | Meant to say | Where | Source |
|---|---|---|---|
| อัปโหลดไฟล์ ตอบคำถามสั้นๆ หรือให้ Zaapi ร่างจากแชทของคุณ | Upload files, answer a few questions, or let Zaapi draft from your chats | Setup home (Thai), step 2 line |
| ไทย | Thai (language switch) | Setup home and guided questions, top right | Claude |
| ตั้งค่าผู้ช่วย AI ของคุณ | Set up your AI agent | Home, page title | Claude |
| เหลืออีกประมาณ N นาที | about N minutes left | Home, subtitle | Claude |
| บันทึกแล้ว · ออกได้ทุกเมื่อ | Progress saved · leave any time | Home, chip top right | Claude |
| ยังไม่มีข้อความใดถึงลูกค้า จนกว่าคุณจะกดเปิดใช้งาน | Nothing is sent to customers until you choose Go live. | Home, reassurance bar | Claude |
| เสร็จแล้ว N จาก 7 ขั้นตอน | N of 7 steps done | Home, progress label | Claude |
| ขั้นตอนถัดไป | Next step | Next-step card, label | Claude |
| Zaapi ร่างให้ | Drafted by Zaapi | Next-step card, label (steps 2–7) | Claude |
| ถัดไป: เชื่อมต่อแชทของคุณ (and the same pattern for each step) | Next: connect your chats | Next-step card, title | Claude |
| เชื่อมต่อช่องทางที่ลูกค้าของคุณใช้ เราจะอ่านแชทเก่าและร่างผู้ช่วยให้คุณจากแชทเหล่านั้น | Connect the channels your customers use. We'll read your past chats and draft your agent from them. | Next-step card, step 1 text | Claude |
| LINE ไม่ให้เราอ่านแชทเก่า เราจึงจะถามคำถามสั้นๆ 8 ข้อแทน | LINE can't share your older chats, so we'll ask you 8 short questions instead. | Next-step card, step 2 text | Claude |
| เราร่างหัวข้อหลักจากแชทเก่าของคุณแล้ว ตรวจก่อนเปิดใช้งาน | We've drafted your main topics from your past chats. Review them before going live. | Next-step card, step 3 text | Claude |
| เราตั้งน้ำเสียงจากคำตอบเก่าของคุณแล้ว ตรวจว่าเป็นแบบที่คุณพูดจริง | We've set your agent's voice from your past replies. Check it sounds like you. | Next-step card, step 4 text | Claude |
| เราจะเล่นคำถามจริงซ้ำและให้คะแนนคำตอบ ก่อนที่ลูกค้าคนไหนจะเห็น | We'll replay real questions and score the answers before any customer sees them. | Next-step card, step 5 text | Claude |
| เลือกว่าจะเริ่มที่ไหนและเมื่อไหร่ ส่วนที่เหลือทีมของคุณดูแล | Pick where and when to start. Your team handles everything else. | Next-step card, step 6 text | Claude |
| ผู้ช่วยของคุณใช้งานจริงแล้ว ตรวจคำตอบที่เราทำเครื่องหมายไว้ | Your agent is live. Review the answers we flagged. | Next-step card, step 7 text | Claude |
| ตรวจสิ่งที่ผู้ช่วยรู้ / ตรวจหัวข้อ / เริ่มทดสอบความพร้อม / ตรวจสัปดาห์แรก | Check what it knows / Review topics / Run the readiness test / Review week one | Next-step card, button | Claude |
| เชื่อมต่อแชทของคุณ | Connect your chats | Step 1 name (tracker and button) | Claude |
| ตรวจสิ่งที่ผู้ช่วยรู้ | Check what your agent knows | Step 2 name | Claude |
| ตรวจสิ่งที่ผู้ช่วยทำ | Check what your agent does | Step 3 name | Claude |
| เลือกน้ำเสียง | Choose how it sounds | Step 4 name | Claude |
| ดูว่าพร้อมหรือยัง | See if it's ready | Step 5 name | Claude |
| เริ่มใช้งานแบบเล็กๆ ก่อน | Go live small | Step 6 name | Claude |
| สัปดาห์แรกที่ใช้งานจริง | First week live | Step 7 name | Claude |
| เชื่อมต่อช่องทางที่ลูกค้าของคุณใช้ | Connect the channels your customers use | Step 1 description | Claude |
| ดูว่าเราอ่านอะไรได้บ้าง และตัดสินสิ่งที่ขัดกัน | See what we read, and settle anything that disagrees | Step 2 description | Claude |
| ตรวจหัวข้อที่เราร่างจากคำตอบของคุณ | Review the topics we drafted from your replies | Step 3 description | Claude |
| ภาษา น้ำเสียง โทน และอีโมจิ | Language, voice, tone and emoji | Step 4 description | Claude |
| เราเล่นคำถามจริงซ้ำและให้คะแนนคำตอบ | We replay real questions and score the answers | Step 5 description | Claude |
| เริ่มจากช่องทางเดียว พร้อมขีดจำกัดที่ปลอดภัย | Start on one channel, with safe limits | Step 6 description | Claude |
| ตรวจคำตอบที่ถูกทำเครื่องหมาย และแก้สิ่งที่ผิด | Review flagged answers and fix anything wrong | Step 7 description | Claude |
| ยังไม่เริ่ม / กำลังทำ / เสร็จแล้ว / ต้องตรวจ | Not started / In progress / Done / Needs attention | Tracker, status chips | Claude |
| คุณอยู่ตรงนี้ | You are here | Tracker, current step | Claude |
| ระหว่างสัปดาห์แรก | during week one | Tracker, step 7 time | Claude |
| นาที | min | Tracker and next-step card, times | Claude |
| เปิด / ดู | Open / View | Tracker, row buttons | Claude |
| 7 ขั้นตอนของคุณ | Your 7 steps | Tracker heading | Claude |
| เวลาที่เหลือโดยประมาณ: | Estimated total remaining: | Tracker heading, right | Claude |
| การตั้งค่าฟรีร่าง 6 หัวข้อหลักให้คุณ | Your free setup drafts your top 6 topics | Plan card, title | Claude |
| ประมาณ 900 แชทต่อเดือน ส่วนใหญ่อยู่ใน LINE เราจึงจะถามคำถามเพิ่มเล็กน้อย | About 900 chats a month. Most are on LINE, so we'll ask you a few questions too. | Plan card, text | Claude |
| AI Success Kit มีอะไรบ้าง | What's in the AI Success Kit | Plan card, link | Claude |
| ฤดูของขวัญปีใหม่เริ่มในอีก 9 สัปดาห์ เพิ่มชุดของขวัญของคุณเพื่อให้ผู้ช่วยตอบได้ถูก | New Year gift season starts in 9 weeks. Add your gift sets so your agent gets them right. | Sale banner | Claude |
| เพิ่มข้อมูลโปรโมชัน | Add sale info | Sale banner, button | Claude |

"Free on every plan, including Basic." on the plan card stays in English when the page is in Thai. It was added in entry 21, and the prompt said not to change the Thai.

**Pranee's guided questions (step 2, Thai is the default)**

| Thai | Meant to say | Where | Source |
|---|---|---|---|
| สินค้าแต่ละตัวทานวันละกี่แคปซูลคะ | How many capsules a day for each product? | Question 1 | Claude (from the English in 03) |
| ตอนนี้มีโปรโมชันอะไรบ้าง และหมดเขตเมื่อไหร่คะ | What promotions are running now, and when do they end? | Question 2 | Claude |
| ส่งของวันไหนบ้างคะ | When do you ship? | Question 3 | Claude |
| มีเก็บเงินปลายทางไหมคะ | Do you offer cash on delivery? | Question 4 | Claude |
| ถ้าลูกค้ามีผลข้างเคียงหรือผื่น ใครเป็นคนดูแลคะ | Who handles side effects or rashes? | Question 5 | Claude |
| มีอะไรที่ผู้ช่วยต้องไม่พูดเด็ดขาดไหมคะ | Anything your agent must never say? | Question 6 | Claude |
| ลูกค้าส่งสลิปโอนเงินมาไหมคะ | Do customers send payment slips? | Question 7 | Claude |
| มีคำถามอื่นที่ลูกค้าถามบ่อยไหมคะ | Anything else customers often ask? | Question 8 | Claude |

**Pranee's voice (step 4) and simulated chats**

| Thai | Meant to say | Where | Source |
|---|---|---|---|
| ดิฉัน / เรา / ทางร้าน | I (formal, female) / we / the shop | Step 4, "How your shop refers to itself" | Claude |
| ค่ะ, ครับ, ผม | polite endings (female, male) and "I" (male) | Step 4 field help, step 5 wrong answers, toasts | 03 |
| ขมิ้นชันทานยังไงคะ | How do I take the turmeric? | Step 4 preview, customer question; step 5 stream | Claude |
| ขมิ้นชันทานครั้งละ 2 แคปซูล วันละ 2 ครั้งหลังอาหารค่ะ | Take 2 turmeric capsules at a time, twice a day, after meals. | Step 4 preview reply (the ครับ and no-ending versions are the same sentence) | 03 |
| โปรซื้อ 3 แถม 1 ยังมีอยู่ไหมคะ | Is the buy 3 get 1 promotion still on? | Step 5 wrong answer 1 and stream | 03 |
| ทานแล้วมีผื่นขึ้นค่ะ | I got a rash after taking it. | Step 5 wrong answer 2 and stream | 03 |
| กินแล้วหายเบาหวานไหมคะ | Will it cure my diabetes? | Step 5 "Safe" example and stream | 03 |
| มีเลข อย. ไหมคะ | Do you have the FDA (อย.) number? | Step 5 stream | Claude |
| โอนแล้วค่ะ ส่งสลิปให้นะคะ | I've transferred the money. I'll send the slip. | Step 5 stream | Claude |
| ทานแล้วคันค่ะ ต้องทำยังไง | It makes me itch. What should I do? | Step 7 review item 1 | Claude |
| แพ้ขมิ้นทานได้ไหมคะ | I'm allergic to turmeric. Can I take it? | Step 7 review item 2 | Claude |

**Nattaya's simulated chats**

| Thai | Meant to say | Where | Source |
|---|---|---|---|
| ผิวแพ้ง่ายใช้ได้ไหมคะ | Is it OK for sensitive skin? | Step 3 sample question, step 4 preview question, step 5 stream | Claude |
| ผิวแพ้ง่ายใช้ได้ค่ะ แนะนำให้ทดสอบที่ท้องแขนก่อนนะคะ | Yes, it's fine for sensitive skin. We suggest a patch test on your inner arm first. | Step 3 sample reply, step 4 preview (ครับ and no-ending versions are the same sentence) | 03 |
| ใช้ serum ก่อนหรือหลังกันแดดคะ | Do I use the serum before or after sunscreen? | Step 5 stream | Claude |
| มี อย. ไหมคะ | Is it FDA (อย.) registered? | Step 5 wrong answer 1 and stream | 03 |
| ส่งกี่วันถึงคะ | How many days does delivery take? | Step 5 stream | Claude |
| ใช้คู่กับ retinol ได้ไหมคะ | Can I use it with retinol? | Step 5 wrong answer 2 and stream | 03 |
| ใช้แล้วแสบหน้าค่ะ | It stings my face when I use it. | Step 5 stream | Claude |
| สมาชิกได้ส่วนลดเดือนเกิดกี่เปอร์เซ็นต์คะ | What percentage discount do members get in their birthday month? | Step 5 wrong answer 3 | 03 |
| ท้องอยู่ใช้ Bright C Serum ได้ไหมคะ | I'm pregnant. Can I use Bright C Serum? | Step 7 review item 1 | Claude |
| ใช้คู่กับ AHA ได้ไหมคะ | Can I use it with AHA? | Step 7 review item 2 | Claude |
| ร้านนี้ของแท้ไหมคะ ทำไมใน Shopee ถูกกว่า | Is this shop genuine? Why is it cheaper on Shopee? | Step 7 review item 3 | Claude |
| อย. | Thai FDA registration | Nattaya's files, topics and product table; Pranee's topics | 03 |

## Photo credits (Unsplash)

The photos are illustrative and don't show the real merchants.
- **Jo:** photo by Ghen Mar Cuaño (photo-1595986630530-969786b19b4d)
- **Nattaya:** photo by Dynamic Wang (photo-1695757002354-8bca71d087c7)
- **Aisha:** photo by Muhammad Rizqi (photo-1664764731538-69a2b571e5a6)
- **Linh:** photo by Elist Nguyen (photo-1775794180653-89531816708f)
- **Budi:** photo by Rendy Novantino (photo-1662103629396-a08922b5d6e6)
- **Pranee:** photo by Maud Beauregard (photo-1634552516330-ab1ccc0f605e)

The 160×160 originals are in `assets/`.
