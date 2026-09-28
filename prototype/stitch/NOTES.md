# Stitch output: notes for the build session

Generated 28 Sep 2026 in Google Stitch (Gemini 3.8 Flash) via the Stitch MCP, from `DESIGN.md`.

- **Stitch project:** "Zaapi AI Agent setup", `projects/9846307330937095495` (private).
- **Design system asset:** `assets/16680362975812584161` ("Zaapi AI Setup"), built from DESIGN.md sections 1–7 and 9.

As `DESIGN.md` says, the context pack (`../context/`) wins on content and behaviour. Use these files for the look only.

## Files

| Screen | PNG | HTML |
|---|---|---|
| 1 Setup home | `01_setup_home.png` | `html/01_setup_home.html` |
| 2 Step 1, Connect your chats | `02_connect_chats.png` | `html/02_connect_chats.html` |
| 3 Step 2, What your agent knows | `03_what_it_knows.png` | `html/03_what_it_knows.html` |
| 4 Settling Aisha's conflict | `04_conflict.png` | `html/04_conflict.html` |
| 5 Step 3, What your agent does | `05_what_it_does.png` | `html/05_what_it_does.html` |
| 6 Step 4, How it sounds | `06_how_it_sounds.png` | `html/06_how_it_sounds.html` |
| 7a Step 5, test running | `07a_readiness_running.png` | `html/07a_readiness_running.html` |
| 7b Step 5, result | `07b_readiness_result.png` | `html/07b_readiness_result.html` |
| 8 Step 6, Go live small | `08_go_live_small.png` | `html/08_go_live_small.html` |
| 9 Step 7, First week live | `09_first_week.png` | `html/09_first_week.html` |
| 10 Dashboard | `10_dashboard.png` | `html/10_dashboard.html` |
| 11 Guided questions (Pranee) | `11_guided_questions.png` | `html/11_guided_questions.html` |
| 12 AI Success Kit panel | `12_kit_panel.png` | `html/12_kit_panel.html` |

- `original/` holds Stitch's untouched exports.
- The top-level PNGs and `html/` are those exports after `fix_and_render.py`. That script applies the fixes below, then re-renders each page at 1440px wide (2x) with headless Chrome.
- Stitch's own edit tool changed the screens inside Stitch but not the exported files, so the fixes are applied locally. Re-run with `python3 fix_and_render.py`.
- The HTML loads Tailwind from its CDN, so it needs a network connection to render.

## Fixes applied after export

- Replaced Stitch's left rail with the real app's full rail on every screen. Stitch dropped five items and called Tickets "Inbox", which made it look as if features had gone. The rail was checked in the trial account on 28 Sep 2026:
  - store switcher, sidebar toggle, Notifications, Search (icon only, with tooltips, as today);
  - Tickets, AI Agent, Analytics, Automations, Broadcast, Contacts, Settings (with labels);
  - Live Chat Support at the bottom.
  - The AI Agent sub-menu (Train, Launch, Monitor) is shown collapsed behind the sidebar toggle, so Knowledge Source, Scenario Handling, Personality, Test, Deploy and Analyse are still reachable.
- Removed a "Production Preview" chip that Stitch added to every top bar. It's hidden, not deleted, so the trial banner stays centred.
- Primary buttons now use the AI gradient; Stitch drew several in flat teal.
- The demo control is the same dashed grey box on every screen: "DEMO · [merchant] ▾ | Hide notes · Reset".
- Step subtitles changed from "Merchant: Aisha · Rumah Kita (Kuala Lumpur)" to "Rumah Kita · Kuala Lumpur".
- Setup home: the time left now agrees ("about 21 minutes left" and "21 min"), and a stray "28% completed" is gone.
- Removed copy Stitch made up that we can't back up:
  - "All connections protected by 256-bit encryption";
  - "Sync frequency: Real-time";
  - "Target for launch: 80+";
  - "Zero disruption to live human agent shifts";
  - "+43%" and "+14% vs last week" trend badges;
  - "Healthy self-resolution rate" and "Safety filters active";
  - "Resets at the end of your trial cycle. Unused quota does not roll over."

## Design decisions that differ from the context pack (to reconcile)

1. **Left nav: 72px, labels under the seven sections.** Adopted for the build (28 Sep 2026); the context pack and build rules now say the same. The utility icons stay icon-only, as today.
2. **No presenter sidebar on step screens.** Only screen 1 shows it, as the reference, so the step screens could use the full 1040px. Reuse screen 1's sidebar styling on every screen in the build.
3. **Setup home time.** The context pack says "about 25 minutes in total"; the mock says "about 21 minutes left" because 2 steps are done. Showing time left is easier to act on. Keep it only if the build can count down.
4. **Sticky footer on every step** with Back, "Progress saved" and the one primary button. Not in the context pack. It's there so a busy merchant can leave at any point without losing work.
5. **Reassurance line on the setup home:** "Nothing is sent to customers until you choose Go live." It's also in the step 1 consent toggle. Not in the context pack.
6. **Step 2 puts conflicts above the file list**, with a summary card ("We read 3 sources and found 42 facts and rules. 3 need your decision"). "42" is a placeholder; take the real count from `03_merchants.md`.
7. **Conflict flow is a right-hand drawer** ("Thing 1 of 3 to settle") with the recommended answers pre-selected. Sections 3 and 4 are collapsed as optional. Same six parts as the context pack, just progressively disclosed.
8. **Step 3 adds review progress** ("2 of 6 reviewed", filter pills) and a sample customer question with the drafted reply on expanded topic cards.
9. **Step 4 uses segmented pills with "Picked from your chats" tags**, plus "Always English" / "Always Malay" as reply-language options.
10. **Step 5 running screen has live counters** and "You can leave this page. We'll let you know when your results are ready."
11. **Step 5 result adds a hint:** "Fixing all 3 should take you to about 85, ready for a small launch." The 85 is a placeholder; check it against the scoring in `03_merchants.md` before using it.
12. **Guided questions (Pranee) add quick-answer chips** and a live "What your agent knows so far" column.

## Content Stitch invented that still needs checking

Placeholders in the mock-ups. Replace them with context-pack data, don't copy them:

- Screen 2: WhatsApp number "+60 12-345 6789" and handles (RumahKita_Official, @rumahkitaboutique, rumahkita.my). The channel split bar is 47 / 35 / 15 / 3% of 7,450 chats. That adds up, but check it against the context pack.
- Screen 5: the rules for sizing, vouchers and COD (e.g. "WELCOME10", "FPX", "TikTok & Shopee only"), the Malay sample reply, and "Routing: Automated look-up".
- Screen 8: the helper lines under each topic toggle, and a "Weekly performance check: We will review resolution rates together after 7 days" card. That card implies a Zaapi team service; drop it unless it's the AI Success Kit.
- Screen 9: "214 / 233", and the voucher caption "Your agent currently passes voucher questions to staff because promo rules are out of date". (Stitch's "R" logo is gone: the rail now starts with the store switcher, as the real app does.)
- Screen 10: the two review-queue replies, "mostly complex orders", and "from bedsheet policy".
- Screen 11: "Estimated 2 mins left", and "You can add product sheets, PDFs, or website links later in setup".
- Screen 4 background, screen 12 background: blurred placeholder copy (not readable, so no action needed).
