# How AI support agents take merchants to their first live conversation (September 2026)

Products covered: Intercom Fin, Zendesk AI agents, Gorgias AI Agent, Tidio Lyro, respond.io and SleekFlow (AgentFlow).

Sources: about 100 vendor pages (help centers, changelogs, product pages and blogs), read on 25 Sept 2026. Dates are the page's "updated" or announcement date where one was shown; otherwise the date the search index recorded. "Doc" means a help-center or changelog page. "Mktg" means a product page, blog post or FAQ.

Caveat: if I say something is "not found," it means I didn't see it in the pages I read, not that the feature doesn't exist. Before relying on any of those gaps, check them in a trial account.

---

## Summary matrix

| Capability | Intercom Fin | Zendesk | Gorgias | Tidio Lyro | respond.io | SleekFlow |
|---|---|---|---|---|---|---|
| Drafts knowledge or guidance from past conversations | **Yes** (doc) | Use cases only (doc) | **Yes**: guidance, and skills via Gaia (doc) | **Yes**: Q&As (doc) | No (not found) | **No**: stated explicitly (doc) |
| Tests on real historical conversations | **Yes**: batch test from past conversations (doc) | No; synthetic simulator in EAP (doc) | **Partial**: re-simulate one existing ticket (doc); "sandbox on real tickets" (mktg) | No | No | No |
| Synthetic or auto-generated test sets | Yes: Procedure simulations (doc) | Yes: simulator (EAP) | No | No | Yes: Copilot-generated test cases (doc) | Yes: batch tests generated from knowledge (doc) |
| Free-form test chat | Yes | Yes | Yes | Yes | Yes | Yes |
| Rollout by channel | Yes | Yes (one agent per channel) | Yes | Yes | Via assignment and Workflows | Yes (up to 3) |
| Rollout by topic or intent | Yes (workflows by topic) | Yes (use cases) | Yes (handover and excluded topics; intents "owned", mktg) | No | No | No |
| Rollout by hours | Yes (in/out of hours) | Not found | Chat online/offline handover only | Yes (always, or only when offline) | Only via instructions | **Yes** (days and hours, including overnight) |
| Rollout by audience or segment | Yes (audiences) | Not found | Test-time audience only | Yes (handoff audiences) | Not found | Yes (label, phone number, keyword) |
| Rollout by % of traffic | **Voice only** (slider; 5–10% recommended) | **A/B test split** (Advanced) | Not found | Not found | Not found | Not found |
| Draft or suggest mode for human agents | Separate Copilot product | Not found for the AI agent | My AskAI app: internal notes first (doc) | Separate Lyro Copilot | AI Assist drafts | Copilot suggests replies (mktg) |
| Readiness or coverage indicator | Content coverage from batch test; no score | Estimated resolution rate (simulator) | Coverage per intent, after launch only | **Knowledge score** | Pass/fail on Copilot tests | **Confidence score** (batch test) |

---

## Intercom Fin

### Documented
- **Knowledge from past conversations:** "Content from conversations" syncs Zendesk or Salesforce ticket history. It processes up to 20,000 conversations from the previous month, caps the first import at 200 snippets, and puts them in Train > Suggestions for review. Generation "usually" finishes within an hour. [Fin help (2025-07)](https://fin.ai/help/en/articles/10727368-content-from-conversations)
- **Improving after launch:** Recommendations find content gaps in conversations Fin handed off. [Intercom help (2026-05-14)](https://www.intercom.com/help/en/articles/11394959-use-ai-powered-content-recommendations-to-improve-fin)
- **Testing on real history:** Batch test builds up to 50 questions from conversations in the last 30–90 days, from all conversations, or from one AI topic. CSV upload also works. You can simulate a specific user, lead, audience or brand, and answers are graded Good or Poor. [Batch test (2026-05-13)](https://www.intercom.com/help/en/articles/10521711-batch-test-fin-ai-agent); [Deploy over chat (2026-08-27)](https://www.intercom.com/help/en/articles/8286630-deploy-fin-ai-agent-over-chat)
- **Simulations:** Full multi-turn simulations for Procedures, which are AI-generated or written by hand and run in the background. [Simulations (2026-08-10)](https://www.intercom.com/help/en/articles/12599517-run-simulations-for-fin-procedures). There is a similar pass/fail version for Fin for Sales. [(2026-07-30)](https://www.intercom.com/help/en/articles/15645477-simulation-testing-for-fin-for-sales)
- **Staged live test:** Launch first to an internal or test audience in Messenger. [Deploy over chat](https://www.intercom.com/help/en/articles/8286630-deploy-fin-ai-agent-over-chat)
- **Rollout controls:**
  - Channels, audiences and regions, plus workflow branches by audience or topic. [Introduction to Deploy (2026-05-14)](https://www.intercom.com/help/en/articles/11769044-introduction-to-deploy)
  - In-hours vs. out-of-hours behavior and quiet hours. [Choose channels (2026-05-18)](https://www.intercom.com/help/en/articles/13377077-choose-channels-to-deploy-fin-ai-agent)
- **% of traffic:** Documented only for Fin Voice. There is a traffic slider, and Intercom recommends starting at 5–10%. [Deploy Fin Voice (2026-09-11)](https://www.intercom.com/help/en/articles/10697275-deploy-fin-voice); [Fin Voice FAQs (2026-09-03)](https://www.intercom.com/help/en/articles/16248514-fin-voice-faqs)
- **Ecommerce:** Shopify Procedures can be created in draft mode and need "Set live." [Fin for Ecommerce on Shopify (2026-09-23)](https://www.intercom.com/help/en/articles/14420740-set-up-fin-for-ecommerce-on-a-shopify-store)
- **Draft or suggest mode:** Copilot is a separate agent-assist product. It uses the last 4 months of chat and ticket history. [How to use Copilot (2026-06-30)](https://www.intercom.com/help/en/articles/8587194-how-to-use-copilot)

### Time-to-value and marketing claims
- Setup "under an hour"; Intercom deployment "in minutes." [Fin for Platforms (2026-09)](https://www.intercom.com/help/en/articles/10118495-fin-for-platforms-explained)
- Average 67% resolution; top teams reach 80% or more. [Community FAQ (2026-09)](https://community.intercom.com/fin-faqs-97)
- Teams using Professional Services reach 68% resolution in 20 days, vs. 59% in 33 days for self-managed teams. [Learning center (2026-07-08)](https://www.intercom.com/learning-center/fin-ai-agent-copilot-reduce-handle-time-boost-productivity)

---

## Zendesk AI agents

### Documented
- **Use cases from past conversations:** AI suggests use cases (intents) from past conversations; you accept, edit or reject them. Knowledge itself comes from the help center or web crawlers. [Use cases (2025-11)](https://support.zendesk.com/hc/en-us/articles/9041901679130-Creating-use-cases-for-advanced-AI-agents-to-identify-what-customers-are-asking-about)
- **Conversation simulator (EAP):** Runs multi-turn conversations built from fictional profiles and scenarios against the live configuration, and estimates automated resolution and quality. It does not replay real tickets and works with messaging agents only. [Simulator (2026-08-13)](https://support.zendesk.com/hc/en-us/articles/11126903515034-Using-the-conversation-simulator-to-test-your-AI-agents-EAP)
- **Test chat:** "Test AI agent" button. Test tickets are excluded from reporting. [Testing (2026-01-22)](https://support.zendesk.com/hc/en-us/articles/9462994470810-Testing-an-AI-agent-before-publishing-it-for-customers)
- **Rollout controls:**
  - One agent per messaging channel, email address, web form or phone line. [Create an AI agent (2026-03-30)](https://support.zendesk.com/hc/en-us/articles/10488757995034-Creating-an-AI-agent-to-automatically-resolve-customer-is)
  - Zendesk recommends publishing during low-traffic hours. [Migration guide (2026-04-13)](https://support.zendesk.com/hc/en-us/articles/10543162665242-Migrating-to-the-new-AI-agents-experience)
  - A/B testing (Advanced) splits visitors between versions. [A/B testing](https://support.zendesk.com/hc/en-us/articles/8357758896410-Performing-A-B-testing-for-advanced-AI-agents)
- **Packaging changes:**
  - A guided self-service setup for email and messaging, announced 30 March 2026 and rolled out 11 May–12 June 2026. [Announcement](https://support.zendesk.com/hc/en-us/articles/10487730059034-Announcing-expanded-access-to-AI-agent-capabilities-for-all-Zendesk-customers)
  - Legacy "Essential" agents must be migrated by 10 Dec 2026. [Removal notice (announced 2026-06-23)](https://support.zendesk.com/hc/en-us/articles/10904648529690-Announcing-the-removal-of-AI-agents-Essential-and-legacy-)

### Time-to-value claims
- Automate "in just minutes." [Getting started](https://support.zendesk.com/hc/en-us/articles/8724978128282-Getting-started-with-AI-agents-for-customer-service)
- I found no resolution-rate figure in the docs.

---

## Gorgias AI Agent

### Documented
- **AI-Generated Guidance:** Built from historical ticket data and past successful interactions. [Changelog (2025-07)](https://updates.gorgias.com/publications/ai-generated-guidance-1)
- **Opportunities (beta):** Mines conversations the AI couldn't resolve and learns from how your team resolved them, then suggests new or updated guidance. Nothing is applied without sign-off. [Opportunities (2026-07-13)](https://helpcenter.gorgias.com/en-US/continuously-improve-ai-agent-with-opportunities-(beta)-4858461); [Guardrails blog (2026-05-15)](https://www.gorgias.com/blog/ai-agent-guardrails)
- **Gaia:** Uses real ticket data to find setup gaps, drafts new skills for recurring topics, and converts existing guidance into skills. [Gaia explained (2026-09)](https://docs.gorgias.com/en-US/gaia-explained-6646561)
- **Testing:**
  - Playground test conversations across Email, Chat, SMS, IG, Messenger and WhatsApp. An **"existing ticket" target re-simulates a real conversation** after you change knowledge or settings.
  - You can test draft skills, guidance or articles before publishing them, one draft at a time. [Test conversations (2026-09-11)](https://docs.gorgias.com/en-US/preview-ai-agent-responses-with-test-conversations-828087)
- **Rollout controls:**
  - Channels are turned on one by one. [Set up and go live (2026-09)](https://docs.gorgias.com/en-US/set-up-and-go-live-with-ai-agent-500219)
  - Handover and excluded topics. [Handover (2026-09-17)](https://docs.gorgias.com/en-US/customize-how-ai-agent-hands-over-to-your-team-6008591)
  - Skills let you start with a few conversation types and expand. [AI Agent explained (2026-09)](https://docs.gorgias.com/en-US/ai-agent-explained-497772)
- **Coverage:** Coverage and success rate by intent are shown after launch. [Intents (2026-08)](https://docs.gorgias.com/en-US/explore-ai-agent-performance-by-ticket-topic-1024587)
- **Suggest mode:** Only in the third-party My AskAI app, which posts internal notes before replying directly. [My AskAI (2026-02)](https://docs.gorgias.com/en-US/ai-agent-by-my-askai-1194779)

### Marketing claims
- "Sandbox mode runs AI Agent against real tickets," "teams choose which intents AI Agent owns," live "in under an hour," and "60% average automation rate across 5 brands." [gorgias.com/ai-agent](https://www.gorgias.com/ai-agent)
- Gaia "installs in five minutes." [Gorgias blog](https://www.gorgias.com/blog)
- Onboarding: "Average time to launch is 60 days" for the full platform, and "50% of your support in 50 days" on the premium implementation. [Onboarding](https://www.gorgias.com/onboarding)

---

## Tidio Lyro

### Documented
- **Q&As from solved chats:** Lyro automatically scans solved live chats and turns them into "Pre-filled" Q&A suggestions, which stay off until reviewed. Helpdesk tickets and emails are not scanned. [Data sources (2025-06)](https://help.tidio.com/hc/en-us/articles/14543666652316-Data-sources-Lyro-s-knowledge-base)
- **Unanswered questions:** Questions Lyro couldn't answer in the last 30 days can be turned into Q&As from the same page.
- **Knowledge score:** Rates how well the data sources are set up, with tips for improving them. [Lyro overview (2025-07)](https://help.tidio.com/hc/en-us/articles/9003475527196-Lyro-the-conversational-AI-agent)
- **Testing:** Free-form Playground only.
- **Rollout controls:** Respond always or only when offline; per-channel on/off; handoff audiences by language, location or contact properties.
- **Suggest mode:** Lyro Copilot suggests replies to human agents. Each Q&A can be enabled for Copilot. [Copilot (2025-06)](https://help.tidio.com/hc/en-us/articles/15126324714012-Lyro-Copilot)
- **Setup time:** Operational in "10 minutes"; the trial includes 50 Lyro conversations. [Quick setup](https://help.tidio.com/hc/en-us/articles/15607494952604-Lyro-a-quick-setup)
- **Changelog:** Proactive Lyro, 11 June 2026. [Changelog](https://updates.tidio.com/en/lyro-ai-meet-proactive-lyro)

### Marketing claims
- 67% average resolution; "resolutions from day one." [tidio.com/ai-agent](https://www.tidio.com/ai-agent/)
- **At least 50% resolution guaranteed** on Plus and Premium, "usually within a month." [Solutions page](https://www.tidio.com/solutions/customer-service/)
- "Up to 70%" [(help center)](https://help.tidio.com/hc/en-us/articles/9003475527196-Lyro-the-conversational-AI-agent) and "up to 85%" [(blog)](https://www.tidio.com/blog/lyro-ai-training/). These figures are not consistent with each other.

---

## respond.io

### Documented
- **Knowledge:** Documents and URLs only. I found no generation from past conversations. [Getting started (2026-09-05)](https://respond.io/help/ai-agents/getting-started-with-ai-agents)
- **Test chat:** Simulated contact, files, audio and simulated calls. Test conversations stay out of the Inbox. [How to test (2026-08-17)](https://respond.io/help/ai-agents/how-to-test-ai-agents)
- **Copilot builder:** Writes instructions, **creates test cases, runs them and reports pass or fail**. It explicitly says this is not a substitute for testing with a real contact. [Using Copilot (2026-08-07)](https://respond.io/help/quick-start/using-copilot)
- **Rollout controls:**
  - Manual Inbox assignment, or automatic for "Unassigned only" or "All new conversations." [Migration guide (2026-08-17)](https://respond.io/help/workflows/how-to-migrate-ai-objective-legacy-workflows-to-ai-agents)
  - Takeover stops the AI. AI Assist drafts replies for humans. [Responding to messages (2026-08-15)](https://respond.io/help/quick-start/responding-to-messages)

### Time-to-value claims
- "Most customers have a working AI Agent live in the same session." [AI Agents page (2026-09)](https://respond.io/ai-agents)
- A template launches "within an hour"; full go-live "in one day." [FAQ (2026-09)](https://respond.io/faqs/how-fast-can-we-go-live-on-respondio)

---

## SleekFlow (AgentFlow)

### Documented
- **Playbook generation:** The conversational setup builds a playbook and persona from the business description, the website and knowledge sources. It **does not use previous customer conversations**. [Conversational setup (2026-09-23)](https://help.sleekflow.io/en_US/agentflow/create-and-set-up-your-ai-agent-with-conversational-setup-tool)
- **Testing:**
  - Chat simulation, plus batch tests built from questions auto-generated from knowledge sources (or imported by CSV), each with an **overall and per-answer confidence score**.
  - Co-Pilot reviews suggest improvements.
- **Rollout controls:** Up to 3 channels; active days and hours, including overnight; custom audiences by phone number, keyword or contact label; exit conditions. [Set up, test and deploy (2026-09-23)](https://help.sleekflow.io/en_US/agentflow/set-up-test-deploy-and-manage-an-agentflow-ai-agent)
- **Knowledge articles:** Generated from ingested sources, not from conversations. [Knowledge base](https://help.sleekflow.io/en_US/sleekflow_ai/ai-knowledge-base)

### Marketing claims
- AgentFlow "analyzes every conversation to identify patterns and gaps" after launch, and 80% of conversations are fully handled by AI. [AgentFlow page](https://sleekflow.io/agentflow)
- Premium includes 60-day dedicated onboarding. [Podium comparison (2026-09-21)](https://sleekflow.io/blog/podium-comparison)
- Blog benchmarks: deflection within 30–60 days. [Live chat automation blog (2026-05)](https://sleekflow.io/en-us/blog/live-chat-automation)

---

## Takeaways

1. **Testing on real history is rare.** Only Intercom documents it at scale: batch tests from past conversations or topics. Gorgias documents re-simulating one ticket at a time, and its marketing claims a "sandbox" that runs on real tickets. Zendesk, respond.io and SleekFlow test against synthetic or knowledge-derived sets.
2. **Drafting from history** is documented by Intercom (snippets from Zendesk or Salesforce history), Gorgias (guidance and skills from tickets), Tidio (Q&As from solved chats) and Zendesk (use cases only). SleekFlow and respond.io start from websites and docs, and SleekFlow says so explicitly.
3. **%-of-traffic rollout** is almost absent for chat. The only documented examples are Zendesk's A/B split and Intercom's voice-only slider. Vendors mostly stage rollout by channel, topic, audience or hours.
4. **Pre-launch readiness scores** are thin: Tidio's knowledge score, SleekFlow's confidence score, and Zendesk's estimated resolution (EAP). The Gorgias and Intercom indicators mostly appear after launch or at the test level.
5. **Time-to-value:** Vendors claim "minutes to an hour" for setup, but meaningful resolution takes weeks. Intercom's own data shows 20–33 days to reach 59–68% resolution, Tidio guarantees 50% "within a month," and Gorgias quotes 50% in 50 days on its premium implementation.
