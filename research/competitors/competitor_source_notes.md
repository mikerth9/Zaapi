# Competitor onboarding research: source notes (25 Sept 2026)

Per-page extraction notes behind competitor_ai_agent_onboarding.md. These are LLM summaries of each page, so check the page before quoting.

## Intercom Fin

### https://www.intercom.com/help/en/articles/7120684-fin-ai-agent-explained
Indexed date: 2026-09-23

- **Knowledge from past conversations:** Suggestions recommends content improvements from conversations Fin couldn’t resolve; it can update or create content and flag duplicates. Content can also be imported from support inboxes or other sources for batch testing.
- **Guidance/procedures:** Guidance adds custom answer instructions and support policies. Procedures use a document-style editor with code and data connectors for complex processes.
- **Testing:** Simulations test real-world scenarios and edge cases. Batch testing evaluates imported or manually added conversations. Fin preview provides real-time test chats.
- **Rollout controls:** Deployment can target audiences, regions, and channels. Usage limits can trigger notifications or stop AI Answers.
- No readiness/coverage/quality score, percentage-traffic, hours, topic/intent, draft, shadow, or copilot rollout control is stated.
- No time-to-value or numeric resolution-rate claim is stated; Fin for Service is described as having a “high resolution rate.”
- No page or announcement date is shown.

### https://www.intercom.com/help/en/articles/10521711-batch-test-fin-ai-agent
Indexed date: 2026-05-13

- **May 13, 2026** — Batch test simulates Fin’s responses to real customer questions before deployment.
- Questions can be generated from **all past conversations** (up to 50, based on recent conversations from 30–90 days) or from a specific **AI topic**.
- Test groups can contain and save up to **50 questions and responses**; settings, including simulated user, are retained for reruns.
- Tests can simulate a **user/lead, audience, or preview user**, and can be configured for different brands.
- The page does not document knowledge-generation, test-chat comparisons, rollout percentages/hours/channels, draft/suggest/shadow/copilot modes, readiness or coverage scores, or time-to-value/resolution-rate claims.

### https://www.intercom.com/help/en/articles/9440354-knowledge-sources-to-power-ai-agents-and-self-serve-support
Indexed date: 2026-06-23

- Fin AI Agent onboarding requires adding at least one knowledge source; Intercom recommends adding more sources to optimize Fin.
- The page does not state that Fin AI Agent can generate knowledge, guidance, or procedures from past conversations or tickets.
- Past Messenger conversations and customer tickets can be enabled as conversation history for Copilot, not Fin AI Agent.
- The page does not document replay/simulation testing, test sets, test chat, rollout controls, readiness or coverage scores, quality scores, time-to-value claims, or resolution-rate claims.
- No page date or announcement date is shown.

### https://www.intercom.com/help/en/articles/8286630-deploy-fin-ai-agent-over-chat
Indexed date: 2026-08-27

- Fin Testing can generate questions from previous conversations, accept bulk-uploaded CSV questions, or use manually added test questions; responses can be marked “Good” or “Poor.”
- Live-environment testing uses a small test/internal audience, such as yourself and teammates, through the Messenger.
- Rollout controls include audience rules, channels (Web, iOS, Android, Slack, SMS), workflow branches by audience/topic, and handover/escalation settings.
- The page does not document hours, percentage traffic, draft/suggest/shadow/copilot modes, or pre-launch coverage/quality scores.
- Intercom reports “an increase in answer rate, confirmed resolutions, and CSAT,” without quantified figures.
- No page or announcement date is shown.

### https://www.intercom.com/help/en/articles/15645477-simulation-testing-for-fin-for-sales
Indexed date: 2026-07-30

- Published July 30, 2026.
- Simulations are automated tests of individual sales conversations; Fin’s AI plays the lead.
- Simulations use the live Fin for Sales content and Playbook.
- Each simulation evaluates routing outcome, what Fin said, data collected, or expected data-connector actions.
- Simulations run in isolated test conversations; no messages go to real people.
- Results include a transcript, routing decision, and pass/fail status for each criterion.
- No readiness scores, rollout controls, historical-conversation replay, or resolution-rate/time-to-value claims are documented.

### https://www.intercom.com/learning-center/fin-ai-agent-copilot-reduce-handle-time-boost-productivity
Indexed date: 2026-07-08

- Page date: July 8, 2026.
- Connect your knowledge base and set up Procedures for multi-step workflows; test using Simulations before going live.
- Deploy Fin AI Agent against highest-volume, highest-effort topics, including WISMO queries, password resets, billing questions, and return requests.
- Run the Fin Flywheel weekly: review Topics Explorer, apply Recommendations, test changes with Simulations, and redeploy.
- Teams using Fin Professional Services reach 68% resolution in 20 days on average, versus 59% in 33 days for self-managed deployments.
- The page does not document generating knowledge, guidance, or Procedures from past conversations or tickets; replaying historical conversations/test sets; pre-launch readiness, coverage, or quality scores; or rollout controls for audience, percentage traffic, draft, suggest, or shadow modes.

### https://www.intercom.com/help/en/articles/8587194-how-to-use-copilot
Indexed date: 2026-06-30

- Page date: June 30, 2026.
- Copilot can use the last 4 months of the team’s chat conversation and ticket history as knowledge sources. Conversations via email are not considered.
- Copilot can use the last 4 months of the team’s Customer ticket history.
- Copilot Guidance is in closed beta and allows custom instructions for specific question types.
- The page does not document historical-conversation replay or simulation testing, test sets, rollout controls, readiness or coverage scores, time-to-value claims, or resolution-rate claims.

### https://www.intercom.com/help/en/articles/10697275-deploy-fin-voice
Indexed date: 2026-09-11

- Fin can be tested in the web app’s Voice Playground, which simulates voice calls and lets users hear responses.
- The page does not document replaying historical conversations, testing against real tickets, or creating test sets.
- Guidance can customize communication style, clarification questions, and content/source usage; Voice-specific guidance applies only to Fin Voice.
- Fin Voice Procedures connect to systems via API for actions such as refunds, subscription updates, and order edits; currently closed beta.
- Rollout controls include phone number, office hours, 24/7 availability, audience targeting, detected categories/intents, Voice channel, and percentage traffic allocation.
- Recommended initial traffic allocation is 5–10%.
- No readiness/coverage/quality score or draft, shadow, or copilot mode is documented.
- Fin answers calls instantly, operates 24/7, and the resolution-rate metric is calculated as Assumed Resolution + Confirmed Resolution.
- Reports apply to calls made on or after 11 June 2025.

### https://community.intercom.com/fin-faqs-97
Indexed date: 2026-09-10

- Fin reads knowledge-base structure, tags, and outcomes rather than the knowledge base “the way a person does.”
- Fin uses the hierarchy **Collection → Section → Article** to understand scope and context before answering.
- Intercom also supports a simplified **Collection → Article** structure without a Section.
- Migration quality affects resolution rate; incorrect category mapping can cause orphaned articles to be placed in a default folder.
- Across Intercom’s customer base, Fin averages a **67% resolution rate**.
- Top-performing teams achieve **80% or higher** resolution rates.

### https://www.intercom.com/help/en/articles/11769044-introduction-to-deploy
Indexed date: 2026-05-14

- Fin can answer repetitive topics using existing support content and conversation history.
- Before launch, review and expand content for Fin ingestion to support high-quality, accurate answers.
- Rollout can be limited to specific channels, audiences, segments, or topics.
- Simple deployment and Workflows can deploy Fin on desired channels; Simple deployment takes priority when both target the same channel and audience.
- Fin can be previewed across different customer segments before redeployment.
- The page does not document generating procedures or guidance from past conversations, historical-conversation replay, simulation/test sets, test chat, hours or percentage controls, draft/suggest/shadow/copilot modes, readiness scores, coverage scores, quality scores, time-to-value, or resolution-rate claims.
- Page date: May 14, 2026.

### https://community.intercom.com/product-updates
Indexed date: 2026-08-10

- **Apr 17, 2026 — Mastering Fin Procedures Course:** The course covers setting escalation rules, Human-in-the-loop carve-outs for sensitive topics, and testing procedures with simulations before going live.
- The course advises users who are close to launching to use simulations to test edge cases properly.
- The course covers launching Fin on email by turning it on for all email volume from day one.
- No documented facts on generating guidance or procedures from past conversations or tickets; historical-conversation replay/test sets; topic, intent, hours, audience, or traffic-percentage controls; readiness, coverage, or quality scores; or quantified time-to-value or resolution-rate claims.

### https://www.intercom.com/help/en/articles/10118495-fin-for-platforms-explained
Indexed date: 2026-09-23

- Fin learns from existing support content; Salesforce, HubSpot, and Freshdesk integrations state that it syncs Help Center or knowledge-base content instantly.
- Setup is stated to take “under an hour”; Intercom deployment can be set up “in minutes.”
- You can control Fin’s tone of voice, answer length, actions, and routing to human agents.
- The page claims Fin delivers “higher-quality answers” and “resolves more complex queries than any other AI agent on the market.”
- No replay/simulation testing, test sets, test chat, readiness/coverage/quality scores, or topic, hours, audience, or percentage-traffic rollout controls are documented.
- Page status: “Updated yesterday.”

### https://www.intercom.com/help/en/articles/16248514-fin-voice-faqs
Indexed date: 2026-09-03

- Voice Procedures can be tested in the Voice Testing Playground.
- Simulations in the Procedure editor test flows before and after going live without real calls.
- The Voice Testing Playground simulates calls in-browser and lets users hear Fin’s responses before deployment.
- The Playground ignores audience rules and pulls all available knowledge-base content; live calls enforce audience rules.
- Simple-deploy rollout is controlled by a percentage slider: above 0% sends calls to Fin; 100% sends all calls on the line to Fin.
- Fin Voice supports complex multi-step workflows through Procedures.

### https://www.intercom.com/help/en/articles/14420740-set-up-fin-for-ecommerce-on-a-shopify-store
Indexed date: 2026-09-23

- Fin for Ecommerce guidance is configured manually for communication style, conversation strategy and flow, situation handling and edge cases, and context and clarification rules.
- Procedures support post-purchase workflows including order tracking, returns, refunds, exchanges, and order updates or cancellations. Procedures may be automatically live or created in draft mode; drafts require review and **Set live**.
- Testing uses a **Preview** panel with sample shopping conversations; it can test recommendations, discovery questions, cart and checkout actions, support requests, and combined shopping/support queries.
- A test Fin audience can be applied to ecommerce workflows and content for live-environment testing.
- Deployment supports Messenger, audience selection, and workflows, but the page does not specify topic/intent, hours, traffic-percentage, shadow, copilot, or readiness-score controls.
- The page makes no time-to-value or resolution-rate claims.
- The page was updated yesterday; no publication or announcement date is shown.

## Zendesk AI agents

### https://support.zendesk.com/hc/en-us/articles/10169333291290-About-voice-AI-agents
Indexed date: 2026-01-13

- AI agents can use existing knowledge sources, policies, and procedures; generative procedures guide actions.
- Before deployment, voice AI agents can be tested from the AI agents workspace. After a live test call, recordings are available on the associated ticket and in conversation logs.
- Test calls should mimic real customer scenarios.
- Zendesk QA can evaluate interactions over time and identify improvement opportunities.
- The page does not document generating guidance or procedures from past conversations or tickets, historical-conversation replay, simulation, test sets, test chat, rollout controls, pre-launch readiness/coverage/quality scores, or time-to-value/resolution-rate claims.
- No page date or announcement date is shown.

### https://support.zendesk.com/hc/en-us/articles/11126903515034-Using-the-conversation-simulator-to-test-your-AI-agents-EAP
Indexed date: 2026-08-13

- Conversation simulator is in an Early Access Program (EAP).
- It generates realistic customer conversations from defined fictional customer profiles and scenarios, or from an AI-generated prompt.
- It runs multi-turn conversations against live AI agent configurations.
- It estimates automated resolution rates and conversation quality.
- It requires a messaging AI agent and is incompatible with other AI agent types.
- Scenarios can be run with selected customer profiles, scenario versions, and a configured number of conversations.
- The page contains no information about generating guidance or procedures from past conversations or tickets, historical-conversation replay, test-chat mode, rollout controls, readiness or coverage scores, or time-to-value claims.

### https://support.zendesk.com/hc/en-us/articles/8357758879130-Testing-conversation-flows-in-AI-agents
Indexed date: 2024-11-11

- The test widget simulates the current customer experience of interacting with the AI agent, starting from the welcome reply and including all currently active settings, including instructions.
- Test conversations are recorded in conversation logs for later review.
- End-to-end conversations, specific dialogues, and dialogue branches can be tested through the widget.
- The widget supports restarting chats, changing session parameters, and opening logged conversations.
- The page does not document replaying historical conversations, generating knowledge/guidance/procedures from past conversations or tickets, rollout controls, readiness/coverage/quality scores, time-to-value, or resolution-rate claims.
- No page date or announcement date is shown.

### https://support.zendesk.com/hc/en-us/articles/10487730059034-Announcing-expanded-access-to-AI-agent-capabilities-for-all-Zendesk-customers
Indexed date: 2026-09-22

- Announced March 30, 2026.
- Initial AI-agent setup and configuration will move to a guided, self-service setup flow for simpler use cases across email and messaging.
- AI-agent configuration and management will have a consistent experience across messaging, email, and voice (in EAP) channels.
- Expert guidance remains available for more complex implementations and deployments at scale.
- The page does not document generating knowledge, guidance, or procedures from past conversations or tickets; historical-conversation replay, simulation, test sets, test chat, rollout controls, readiness/coverage/quality scores, or quantified time-to-value or resolution-rate claims.

### https://support.zendesk.com/hc/en-us/articles/10488757995034-Creating-an-AI-agent-to-automatically-resolve-customer-issues
Indexed date: 2026-03-30

- The connected brand knowledge base enables AI-generated answers; external website content can be added through existing or newly created web crawlers.
- At least one connected knowledge source—an active help center or web crawler—is required before continuing.
- The page offers optional testing of the AI agent but does not document replaying or simulating historical conversations, testing real tickets, or test sets.
- Activation is controlled by selecting channels or phone lines. One AI agent can be active per messaging channel, support email address, web form, or phone line.
- Topic/intent, hours, audience, traffic percentage, draft, suggest, shadow, and copilot controls are not documented.
- Readiness or coverage scores, time-to-value, and resolution-rate claims are not documented.
- No page date or announcement date is shown.

### https://support.zendesk.com/hc/en-us/articles/10543162665242-Migrating-to-the-new-AI-agents-experience
Indexed date: 2026-04-13

- New AI agents can generate responses based on connected knowledge sources.
- Advanced capabilities include dialogue builder, use cases, generative procedures, and richer automation.
- Legacy **Answers** map to new **Dialogues**; legacy **Intents** map to **Use cases**.
- Bot-builder steps can be recreated in Dialogue Builder, including generative replies, integrations or action flows, escalation, conditionals, and availability.
- Each new AI agent supports only one channel.
- When activating a new agent for a channel, Zendesk recommends publishing during low-traffic hours.
- Packaging rollout: May 11–June 12, 2026.
- Technical development ends August 31, 2026; listed legacy features are removed in December 2026.
- The page gives no historical-conversation replay, test-set, test-chat, percentage-traffic, audience, readiness-score, or resolution-rate claims.

### https://support.zendesk.com/hc/en-us/articles/10904648529690-Announcing-the-removal-of-AI-agents-Essential-and-legacy-functionality-Important-dates-and-migration-guidance
Indexed date: 2026-09-21

- Announced on June 23, 2026.
- Zendesk created tailored, step-by-step migration guidance for each type of legacy functionality.
- Customers are recommended to migrate to the upgraded AI agent experience before August 31, 2026; migration is required before December 10, 2026.
- Zendesk states the upgraded experience can “automate more complex requests, resolve issues faster across channels, and scale support with expanded access to agentic capabilities,” helping deliver “more resolutions with less effort.”
- No documented details on generating procedures from past conversations, historical-conversation replay or simulation, test sets, test chat, rollout controls, readiness or coverage scores, or specific time-to-value or resolution-rate percentages.

## Gorgias AI Agent

### https://docs.gorgias.com/en-US/ai-agent-explained-497772
Indexed date: 2026-09-08

- Page status: **Updated 9 days ago**; no announcement date is shown.
- AI Agent uses knowledge from help center articles, website content, documents, guidance, and Shopify data.
- Skills provide instructions for specific conversation types; merchants can start with a few types, such as returns or order status, and expand coverage over time.
- Handover rules can be configured in AI Agent settings.
- The page does not document generating knowledge from past tickets, replaying historical conversations, test sets, test-chat workflows, rollout controls, readiness or quality scores, time-to-value claims, or resolution-rate claims.

### https://updates.gorgias.com/publications/ai-generated-guidance-1
Indexed date: 2025-07-12

- AI-Generated Guidance is available for all Automate subscribers.
- It uses historical ticket data to create detailed instructional content for the AI Agent and CX team.
- It generates pre-written, customizable responses based on successful past interactions.
- AI analyzes past tickets to generate ready-to-use resources.
- The page states that the content is based on actual customer interactions.
- No testing against historical conversations, test-chat functionality, rollout controls, readiness or coverage scores, time-to-value claims, or resolution-rate claims are stated.
- No announcement date is shown.

### https://docs.gorgias.com/en-US/gaia-explained-6646561
Indexed date: 2026-09-23

- Gaia can use real ticket data to identify gaps in an AI Agent setup and improve underperforming skills.
- Gaia can draft a new skill for recurring support topics.
- Gaia can review existing guidance and convert what it can into skills.
- The page does not document replaying or simulating real historical conversations, test sets, test chat, rollout controls, readiness/coverage/quality scores, or time-to-value or resolution-rate claims.
- Page updated 3 hours ago; no announcement date is shown.

### https://helpcenter.gorgias.com/en-US/continuously-improve-ai-agent-with-opportunities-(beta)-4858461
Indexed date: 2026-07-13

- Opportunities are generated from past customer conversations where AI Agent was unable to fully resolve requests.
- AI Agent learns from how the team resolves these cases, suggesting opportunities such as knowledge gaps or conflicting information.
- Opportunities can direct users to create or update AI Agent guidance addressing a knowledge gap.
- The page documents no historical-conversation replay, simulation, test sets, test chat, rollout controls, readiness or coverage scores, or time-to-value/resolution-rate claims.

### https://docs.gorgias.com/en-US/preview-ai-agent-responses-with-test-conversations-828087
Indexed date: 2026-09-11

- Updated 6 days ago; no announcement date is shown.
- Test conversations occur in the Playground and let users preview AI Agent responses, evaluate reasoning, and test skills, content, actions, tone of voice, and settings.
- An **existing ticket** target can re-simulate a conversation where AI Agent initially responded unexpectedly after knowledge or settings changes.
- Test channels include Email, Chat, SMS, Instagram DM, Facebook Messenger, and WhatsApp.
- Draft skills, guidance, and help center articles can be tested before publishing; only one draft can be tested at a time.
- The page does not document knowledge generation from past conversations, rollout percentages, topic/intent controls, operating hours, readiness or coverage scores, time-to-value claims, or resolution-rate claims.

### https://www.gorgias.com/blog/inside-the-ai-agent-benchmark
Indexed date: 2026-09-15

- The benchmark tests AI agents on 200+ live ecommerce stores and has evaluated more than 8,000 conversations.
- Each conversation runs against the live widget on a real storefront, using the same AI deployment customers interact with.
- Each conversation starts fresh, with no browsing history or prior context; test shoppers type every question in their own words.
- Testing uses hard, compound, multi-constraint questions with objections and edge cases.
- The benchmark blind-scores conversations using 26 yes/no rubric checks across shopping and support.
- No historical-conversation replay, onboarding controls, pre-launch readiness score, rollout percentage, or time-to-value claim is documented.
- Page updated and created: September 15, 2026. Board referenced: September 9, 2026.

### https://www.gorgias.com/blog/ai-agent-guardrails
Indexed date: 2026-05-15

- Page created May 8, 2026; updated May 15, 2026.
- Guidance Opportunities detects recurring questions AI Agent could not confidently answer and suggests new Guidance. Users can review, edit, approve, or dismiss; nothing is added without sign-off.
- Monthly review includes flagged “Automated” tickets, ratings of good, ok, or bad, and reasons such as wrong answer, wrong tone, or should have escalated.
- **AI Agent > Test** provides simulated conversations without affecting real tickets, reporting, or customers. Test conversations do not count toward automated interaction billing.
- Email, chat, and SMS are disabled by default and enabled manually per channel.
- No historical-conversation replay, readiness score, coverage score, traffic percentage, audience rollout, draft mode, shadow mode, or copilot mode is described.

### https://docs.gorgias.com/en-US/articles/test-ai-agent-362667
Indexed date: 2026-09-11

- Test conversations preview how AI Agent would respond to real customer questions and scenarios.
- They allow users to ask AI Agent questions, evaluate its reasoning, and confirm its content, actions, and tone of voice.

### https://www.gorgias.com/blog
Indexed date: None

- Gaia for Zendesk analyzes up to 90 days of real ticket history and generates guidances, 15 AI Agent instructions, voice-of-customer insights, and 10 Copilot procedures; every output requires review and approval.
- Gaia identifies missing intents, unclear instructions, outdated logic, escalation patterns, and knowledge gaps.
- Gorgias AI Agent includes testing to preview responses to real customer questions before launch or after changes.
- Cornbread’s rollout: audit the knowledge base, launch, then optimize; it conducted weekly reviews for three to four weeks, followed by biweekly audits and daily AI feedback.
- Gaia installation takes about five minutes; first analysis can run in under a minute.
- Gaia produces “implementation-ready content” in hours, not weeks.
- No readiness, coverage, or quality score is stated for pre-launch onboarding.
- The benchmark’s September 9, 2026 board used fresh live-widget conversations, not historical replay or test-chat simulation.

### https://docs.gorgias.com/en-US/ai-agent-by-my-askai-1194779
Indexed date: 2026-02-03

- Updated 7 months ago; no announcement date is shown.
- Setup: sign up for a free 30-day trial, train on the store website and FAQ pages, then connect Gorgias.
- The AI is trained on Gorgias help docs and company knowledge.
- Guidance can adapt replies to the brand’s style and tone.
- The page does not document generating knowledge, guidance, or procedures from past conversations or tickets.
- The AI Copilot Chrome Extension lets support teams test the AI agent; replay, simulation, or historical test-set testing is not documented.
- By default, replies are created as internal notes for agent review; after confidence is established, the AI can reply directly to customers.
- Topic/intent, channel, hours, audience, traffic-percentage, shadow, or draft-mode rollout controls are not documented.
- No pre-launch readiness, coverage, or quality scores are documented.
- “CREATE YOUR AI AGENT IN 10 MINS.”
- The AI answers “over 80% of questions accurately”; adopting businesses see “human” support tickets fall “by 80%.”

### https://www.gorgias.com/blog/ai-copilot-customer-service
Indexed date: 2026-08-31

- **Page dates:** Updated August 31, 2026; created July 21, 2026 (July 20, 2026 also displayed).
- Gaia analyzes real ticket data, conversations, skills, knowledge, and actions to identify uncovered recurring requests, unnecessary escalations, and knowledge gaps.
- Gaia runs one-click audits and proactively surfaces missing automation.
- Gaia recommends or generates new Skills and Actions for review; every proposed change requires explicit approval before going live.
- Customer testimonial: “Within minutes it generated a detailed, ready to use draft.”
- The page does not document replay/simulation testing, historical test sets versus test chat, readiness or coverage scores, traffic percentages, channel/topic/hour/audience rollout controls, or draft/suggest/shadow/copilot modes.

### https://www.gorgias.com/ai-agent
Indexed date: None

- Gaia learns from the team’s help center, catalog, policies, and past conversations.
- Gaia can audit AI Agent skills and recent tickets, identify skills with high handover rates, and flag knowledge gaps or duplicates with a ready-to-use draft.
- Sandbox mode runs AI Agent against real tickets so teams can review every response before launch.
- Teams choose which intents AI Agent owns; other intents go to the team with full context.
- Gorgias states AI Agent can be live “in under an hour.”
- The page reports a “60% average automation rate across 5 brands” and “53% conversations automated by AI Agent” for Fashion & Apparel.
- No page or announcement date is shown.

### https://www.gorgias.com/blog/our-ai-approach
Indexed date: 2025-05-12

- AI Agent can use owned data, including Help Center articles, order data, brand voice, conversation history, Shopify storefront/backend, and other brand-content URLs.
- Guidance lets teams provide procedures such as asking follow-up questions, confirming details, and applying different handling based on order age, customer spend, or domestic/international status.
- Teams can set conditions specifying when and for whom individual Actions may execute.
- During alpha testing, brands automated up to 30% of email tickets; Gorgias envisioned over half of customer tickets handled by AI Agent by the end of 2024.
- Within two months, Psycho Bunny’s AI Agent resolved tickets in under 2 minutes versus human agents’ 4+ hours; AI Agent received 4.67/5 CSAT.
- Page updated May 12, 2025; created July 15, 2024.

### https://docs.gorgias.com/en-US/set-up-and-go-live-with-ai-agent-500219
Indexed date: 2026-09-09

- Knowledge can include store website content, help center articles, documents, URLs, and custom guidance.
- Guidance templates provide instructions for common scenarios; the page does not describe generating knowledge, guidance, or procedures from past conversations or tickets.
- Playground test conversations let you enter questions and adjust channel and audience settings; they are not billed, do not affect reporting, and do not send real shopper messages.
- The page does not describe replaying historical conversations, simulations, or test sets.
- Rollout is controlled by enabling channels: Email, Chat, SMS, Instagram DMs, Facebook Messenger, and WhatsApp.
- No topic/intent, hours, traffic-percentage, draft, suggest, shadow, or copilot rollout modes are documented.
- No readiness, coverage, quality, time-to-value, or resolution-rate claims are documented.
- Updated 14 days ago.

### https://www.gorgias.com/blog?9ad712ec_page=2
Indexed date: None

- Gaia for Zendesk analyzes up to 90 days of historical Zendesk tickets and generates ready-to-review guidances, 15 AI Agent instructions, voice-of-customer analysis, and 10 Copilot procedures.
- Outputs are drafts; nothing is applied without approval.
- Gaia “installs in five minutes” and can run its first analysis “in under a minute.”
- AI Agent Test Mode previews responses to real customer questions before launch or after changes; the page does not document historical-conversation replay or simulated test sets.
- Test Mode checks Help Center sources, Guidance adherence, excluded-topic escalation, and tone of voice.
- The page documents excluded topics and automatic handover for low confidence or angry customers, but no readiness/coverage/quality score or percentage-traffic rollout control.

### https://docs.gorgias.com/en-US/explore-ai-agent-performance-by-ticket-topic-1024587
Indexed date: 2026-08-21

- Page updated a month ago.
- The Intents page identifies gaps in AI Agent’s knowledge; improving its knowledge can help address common customer questions and increase ticket coverage and success rate.
- The performance section measures how improvements to knowledge sources and setup affect coverage, automated interactions, success rate, and CSAT.
- Adding Knowledge, Guidance, and connecting AI Agent to other apps can increase the number of tickets it fully automates.
- Some tickets initially classified as `Other` may be grouped into more specific topics as AI Agent learns from past tickets.
- The page provides no documented details about generating knowledge, guidance, or procedures; replay or simulation testing; test sets versus test chat; rollout controls; pre-launch readiness or quality scores; time-to-value; or resolution-rate claims.

### https://updates.gorgias.com/
Indexed date: None

- **Knowledge/settings:** AI Agent on WhatsApp (beta) uses existing knowledge, policies, tone, and settings for on-brand replies.
- **Handover:** On Chat, teams can require shopper confirmation before handover or have handover start immediately; confirmation is the default.
- **Testing, historical replay/simulation, test sets, rollout by topic/intent/channel/hours/audience/traffic, draft/suggest/shadow/copilot modes, readiness/coverage/quality scores, and time-to-value or resolution-rate claims:** Not documented in the provided page content.
- **Announcement dates:** Not shown; entries display numeric identifiers only.

### https://www.gorgias.com/onboarding
Indexed date: None

- During implementation, Gorgias says it will “Configure AI Agent, set up ticket workflows, and train your team to use Gorgias.”
- “Average time to launch is 60 days, even for brands with multiple stores and complex setups.”
- Premium “50-in-50 implementation” promises to “Automate 50% of your support in 50 days.”
- The page does not document generating AI-agent knowledge, guidance, or procedures from past conversations or tickets; historical-conversation replay/simulation/test sets; test chat; rollout controls; readiness, coverage, or quality scores; or an AI-agent-specific resolution-rate claim.
- No page date or announcement date is shown.

### https://docs.gorgias.com/en-US/set-up-and-use-ai-agent-on-chat-828220
Indexed date: 2026-08-21

- **Onboarding:** AI Agent can be onboarded with knowledge from a Help Center or website, or by creating Guidance. Onboarding provides information about the brand, products, and support processes.
- The page does not document generating knowledge, Guidance, or procedures from past conversations or tickets.
- The page does not document replay, simulation, historical-conversation testing, or test sets; it only describes AI Agent responding on Chat.
- **Rollout:** Deployment is configured for one or more Chat channels using an ON/OFF toggle.
- No topic/intent, hours, audience, percentage-traffic, draft, suggest, shadow, or copilot controls are documented.
- No readiness, coverage, quality-score, time-to-value, or resolution-rate claims are documented.
- Page status: **Updated a month ago**.

## Tidio Lyro

### https://help.tidio.com/hc/en-us/articles/14543666652316-Data-sources-Lyro-s-knowledge-base
Indexed date: 2025-06-12

- Lyro automatically scans solved live conversations for useful knowledge; Helpdesk tickets/emails are not scanned.
- Extracted Q&A pairs appear in Suggestions with a “Pre-filled” label and are disabled by default for review.
- Agents can modify extracted questions/answers and activate them with “Save as a Q&A”; activated Q&As are used in future conversations.
- Unanswered live-conversation messages can be converted into Q&As using “Create answer.”
- Lyro can be tested in the Playground test widget; unanswered questions there offer an “Add answer” button.
- No documented replay/simulation test sets, rollout controls, readiness/coverage/quality scores, or time-to-value/resolution-rate claims.
- No page date or announcement date is shown.

### https://www.tidio.com/blog/lyro-ai-training/
Indexed date: 2024-07-11

- Updated: Oct 6, 2025.
- Lyro analyzes completed live conversations to extract knowledge and generate suggested question-and-answer pairs, labeled “Inbox” in the Q&A tab.
- Learning from Historical Conversations activates automatically after a sufficient number of conversations; suggested Q&A pairs remain disabled pending review.
- Teams can edit and preview suggested content before adding it to Lyro’s active knowledge base.
- Lyro’s FAQs should be thoroughly tested with real user queries; testing identifies gaps and problematic areas.
- The page reports Lyro can automate “up to 85% of service requests.”
- No documented replay/simulation test sets, topic/channel/hours/audience/traffic rollout controls, readiness scores, coverage scores, quality scores, or time-to-value claim.

### https://www.tidio.com/pricing/
Indexed date: 2018-08-27

- Lyro AI Agent learns from support content and uses artificial intelligence and natural language processing to understand questions and provide appropriate answers.
- Lyro understands customer-question intent and uses solely the support content provided to generate personalized responses.
- Lyro is not restricted to predefined questions and can answer complex questions in a human-like manner based on supplied information.
- Tidio states Lyro can “solve up to 67% of customer problems.”
- No information is provided about generating procedures from past conversations or tickets, historical-conversation replay or simulation, rollout controls, readiness or coverage scores, or time-to-value.
- No page date or announcement date is shown.

### https://help.tidio.com/hc/en-us/articles/9003475527196-Lyro-the-conversational-AI-agent
Indexed date: 2025-07-04

- Knowledge can be added manually, automatically via auto-generated suggestions, by extracting knowledge from solved chats, or by importing from external platforms.
- The Hub provides a **knowledge score** showing how well Lyro’s data sources are configured and offers actionable improvement tips.
- The Playground tests Lyro in a test environment by typing questions or selecting examples; unanswered questions can be added as question-and-answer pairs.
- Guidance lets users create detailed instructions for Lyro’s communication and behavior.
- Rollout controls include responding always or only when offline, selecting channels, and configuring handoff audiences using conditions such as language, location, or Contact Properties.
- Lyro can handle up to **70% of common customer questions** and answer within milliseconds.
- No page date or announcement date is shown.

### https://www.tidio.com/blog/ai-chatbot-integration/
Indexed date: 2025-06-02

- Updated: Jun 3, 2025.
- Lyro knowledge onboarding uses “Data sources”: manually uploaded content, website sync, or direct imports from platforms such as Zendesk.
- Unanswered questions can be reviewed and added as new Q&A pairs.
- Testing can use internal scenarios, real conversations in a small test group, and simulated conversations in Lyro’s “Playground.”
- Lyro shows which data source answered each question; unanswered questions appear in “Suggestions.”
- Rollout guidance: start with a high-traffic page or specific support use case, then expand to email, chat, or social.
- The page provides no readiness/coverage/quality scores, percentage-traffic controls, hours/audience controls, shadow/copilot mode, or quantified time-to-value or resolution-rate claims.

### https://www.tidio.com/ai-agent/
Indexed date: 2025-02-14

- Add Lyro to a website “in a few clicks, without technical knowledge.”
- Feed Lyro with support content; it uses that content as its knowledge base.
- Lyro answers questions using only the provided content.
- Review conversations, add missing knowledge, and modify guidances to improve performance.
- Lyro can learn from a human agent’s response when it cannot answer from the support content.
- The page states users can “get resolutions from day one” and “Improve your service in minutes.”
- Lyro boosts the resolution rate to “67% on average.”
- The page does not document historical-conversation replay/simulation test sets, pre-launch readiness scores, or rollout controls by topic, channel, hours, audience, traffic percentage, or draft/shadow/copilot mode.
- No page date or announcement date is shown.

### https://help.tidio.com/hc/en-us/articles/15126324714012-Lyro-Copilot
Indexed date: 2025-06-24

- Copilot is a component of Lyro and uses the same knowledge; enable Lyro and add data sources to set it up.
- Data sources appear in the Lyro AI Agent’s Data sources tab.
- Individual Q&A pairs can be enabled for Copilot by toggling on the Copilot tag.
- Copilot generates suggested responses for incoming chat messages and tickets on request; agents can review, modify, send, or discard them.
- Copilot can automatically suggest a response when an agent joins a live conversation and the visitor asks a question.
- Copilot can improvise when no information is available; these suggestions require review and modification.
- No historical-conversation replay/testing, readiness scores, rollout controls, or resolution-rate claims are documented.

### https://www.tidio.com/blog/lyro-review/
Indexed date: 2025-10-06

- Page updated: October 6, 2025.
- Lyro requires no training; users can upload help-center content, website content, PDFs, or CSV files and start automating support.
- Lyro can be up and running within minutes; one user reported it was “ready on the site within half an hour.”
- Lyro can automate up to 67% of customer queries.
- Axioma achieved an 89% AI resolution rate after implementing Lyro.
- Gecko Hospitality reported approximately 90% of conversations handled by Lyro, with responses audited daily.
- The page documents no historical-conversation replay, simulation/test-set testing, readiness or coverage scores, or controls for rollout by topic, channel, hours, audience, traffic percentage, draft, shadow, or copilot mode.

### https://www.tidio.com/blog/ai-copilot-for-customer-service/
Indexed date: 2025-06-26

- AI copilots can surface information from past chats, help documents, connected knowledge bases, and internal systems.
- Message autocomplete draws on similar past replies or recognized phrasing patterns.
- Lyro Copilot generates suggestions from existing company content or improvises drafts; agents can edit or use them directly.
- The page does not document generating procedures from historical conversations, replay or simulation testing, test sets, rollout controls, readiness or coverage scores, or quality scores.
- It states copilots enable faster replies but provides no quantified time-to-value or resolution-rate claim.
- No page date or announcement date is shown.

### https://www.tidio.com/solutions/customer-service/
Indexed date: 2024-12-19

- Lyro AI uses only the business’s data to answer questions.
- Users can test Lyro with public support content through chatbot demos.
- Lyro has an average resolution rate of 67%.
- Tidio guarantees Lyro will resolve at least 50% of customer inquiries for Plus or Premium users, usually within a month after implementation.
- Premium includes custom setup and implementation by Tidio’s team.
- The page does not document generating guidance from past conversations/tickets, historical replay or simulation test sets, rollout controls, or pre-launch readiness/coverage/quality scores.
- No page or announcement date is shown.

### https://www.tidio.com/blog/category/product-news/
Indexed date: 2025-03-31

- Lyro AI achieves a 64% average customer-support resolution rate, peaking at 90%, and is described as outperforming competitors such as Intercom.
- No page date or announcement date is shown.
- The page does not document historical-conversation knowledge generation, replay/simulation testing, test sets, test chat, rollout controls, readiness/coverage/quality scores, or time-to-value claims.

### https://help.tidio.com/hc/en-us/articles/15607494952604-Lyro-a-quick-setup
Indexed date: 2024-09-02

- Lyro can be set up and operational in **10 minutes**.
- Add website URLs as data sources for Lyro’s knowledge base.
- Upload internal knowledge as question-and-answer pairs for more accurate responses.
- Test Lyro in the **Playground** by asking questions customers might submit and reviewing its answers.
- Edit, delete, or add responses to correct irrelevant, missing, or inaccurate information.
- Configure when Lyro takes over, handoff behavior, and the channels where it is active.
- Lyro can be activated through **Configure**; activation disables existing **Visitor says** flows, which can be re-enabled.
- The free trial includes **50 Lyro conversations** at no cost.

### https://www.tidio.com/faq/
Indexed date: 2025-04-01

- Lyro can be trained from ticket or conversation history by extracting questions from previous customer inquiries; historical CRM, ticketing, or chat-platform data can be used as training information.
- FAQ knowledge can be added through a webpage URL, manual Q&As, CSV Q&As, or Zendesk articles.
- Lyro can be trained on an entire website.
- Setup requires no coding.
- Testing is documented through the Lyro demo, AI playground, or website widget; replay or simulation against historical conversations is not documented.
- Lyro can resolve up to 67% of inquiries; Premium subscribers receive a guaranteed 50% resolution rate.
- No readiness or coverage score is documented.

### https://updates.tidio.com/en/lyro-ai-meet-proactive-lyro
Indexed date: 2026-06-11

- Announcement date: June 11, 2026.
- Lyro can proactively start conversations instead of only responding.
- Triggers can automatically start a conversation before customers ask a question.
- Setup: **Lyro → Behavior → Proactive Roles**.
- Users choose when Lyro starts, craft the first message, and provide guidance for handling the conversation.
- Proactive roles can be created from scratch or from a pre-built template.
- Proactive Roles use the Lyro Flows quota.
- No information is provided about historical-conversation knowledge generation, replay/simulation testing, test sets, channels, hours, audience percentages, draft/suggest/shadow/copilot modes, readiness scores, coverage or quality scores, time-to-value, or resolution-rate claims.

## respond.io

### https://respond.io/ai-agents
Indexed date: 2026-09-18

- Copilot can build a tested, ready-to-publish AI Agent draft from a plain-language description; no prompt-writing skill is required.
- Teams can choose role-based templates for sales, receptionist, or support.
- AI Agents can be tested extensively before going live in a dedicated testing environment.
- “Most customers have a working AI Agent live in the same session.”
- Knowledge is grounded in approved sources using continuous RAG synchronisation; no retraining is required.
- The page does not document historical-conversation replay, ticket-based procedure generation, readiness/coverage scores, or rollout controls by traffic percentage, audience, hours, channel, topic/intent, draft, shadow, or copilot mode.
- No page date or announcement date is shown.

### https://respond.io/help/quick-start/responding-to-messages
Indexed date: 2026-05-28

- Page date: **15 Aug 2026**.
- Published AI Agents appear in the Inbox assignment dropdown; assigning a conversation to one starts handling immediately.
- AI Agents can assign conversations to human agents or teams using **Assign to agent or team**.
- **Takeover** stops an AI Agent from replying and reassigns the conversation to the user; it will not respond again unless reassigned.
- AI Agents with **Close Conversation** enabled can close resolved conversations, generate a summary, and select a closing note.
- **AI Assist** drafts replies based on knowledge sources.
- No documentation is provided on historical-conversation replay, simulation/test sets, rollout controls, readiness or coverage scores, or time-to-value/resolution-rate claims.

### https://respond.io/team-inbox
Indexed date: 2026-09-23

- AI Agents handle product questions, FAQs, and order tracking, including during peak demand.
- AI Agents qualify leads, route them to sales, and follow up instantly.
- AI Agents require no prompting and can be built in minutes with Copilot.
- No information is provided about generating knowledge from past conversations or tickets, testing against historical conversations, rollout controls, readiness or coverage scores, or resolution-rate claims.
- No page date or announcement date is shown.

### https://respond.io/
Indexed date: 2026-09-22

- AI Agent onboarding can start with templates or involve customizing an agent to business needs.
- The page does not document generating knowledge, guidance, or procedures from past conversations or tickets.
- The page does not document testing against historical conversations, replay, simulation, test sets, or test chat.
- The page does not document rollout controls by topic/intent, channel, hours, audience, traffic percentage, draft, suggest, shadow, or copilot mode.
- The page does not document pre-launch readiness, coverage, or quality scores.
- The page does not provide time-to-value or resolution-rate claims for AI agent onboarding.

### https://respond.io/help/ai-agents/how-to-test-ai-agents
Indexed date: 2025-09-23

- The page is dated **17 Aug 2026**.
- AI Agents can be tested in the setup flow using a simulated Contact and the **Test AI Agent** chat panel; no live Contacts or workarounds are required.
- Tests support text, files, audio messages, and simulated calls.
- Test conversations do not appear in Inbox and do not affect live Contact data.
- Unpublished AI Agents can be tested before publishing.
- The page does not document generating guidance from historical conversations or tickets, replaying historical conversations, test sets, rollout controls, readiness/coverage/quality scores, time-to-value claims, or resolution-rate claims.

### https://respond.io/help/ai-agents/getting-started-with-ai-agents
Indexed date: 2025-08-27

- Page date: **05 Sept 2026**.
- Knowledge sources can be added by uploading documents or URLs; examples include business information, FAQs, help articles, troubleshooting playbooks, and policy documentation. No generation from past conversations or tickets is documented.
- Testing is through a **Test AI Agent** chat, including uploaded PDFs, images, or documents; replaying historical conversations or test sets is not documented.
- Rollout options documented: manual assignment, default assignee, or Workflow assignment. Topic, channel, hours, audience, traffic percentage, draft, suggest, shadow, and copilot controls are not documented.
- Readiness/coverage/quality scores and resolution-rate claims are not documented.
- The guide claims AI Agents save team time and improve response consistency.

### https://respond.io/help/ai-agents
Indexed date: 2026-09-22

- “Managing AI Knowledge Sources” explains how to add, manage, and optimize knowledge sources so AI delivers more accurate, reliable, and context-rich answers.
- “How to Test AI Agents” describes safely testing an AI Agent by simulating conversations and previewing actions without affecting real customers.
- No information is provided about generating knowledge from past conversations or tickets, replaying historical conversations, test sets, rollout controls, readiness/coverage/quality scores, time-to-value, resolution-rate claims, or dates.

### https://respond.io/help/quick-start/using-copilot
Indexed date: 2026-08-07

- Copilot can structure AI Agent instructions and actions from the desired outcome, including context, communication style, conversation flows, and scenarios.
- Copilot creates relevant test cases and runs them in the **Test AI Agent** panel.
- Copilot reviews the AI Agent’s replies and reports whether each test passed.
- Copilot tests are not a replacement for live testing; test with a real Contact before publishing or wider use.
- The page does not document generating guidance from past conversations or tickets, replaying historical conversations, rollout controls, readiness or coverage scores, time-to-value claims, resolution-rate claims, or an announcement date.

### https://respond.io/blog/whatsapp-business-solution-provider
Indexed date: 2026-05-04

- Page date: **07 Sept 2026**.
- During a proof-of-concept, test AI with **real scenarios from support and sales queues**.
- Validate **lead qualification**, **FAQ deflection**, **human handoff**, **multi-format understanding** (images, PDFs, voice notes), and **workflow triggers**.
- Good containment rate: **40–60%+ of conversations resolved by AI alone**.
- Human handoff should preserve **full conversation context** and AI should **stop immediately**.
- The page does not document generating AI knowledge or procedures from past conversations/tickets, historical-conversation replay or simulation test sets, rollout controls by topic, channel, hours, audience or traffic percentage, or pre-launch readiness/coverage/quality scores.

### https://respond.io/blog/conversational-sales-platform
Indexed date: 2026-05-15

- Page date: **04 Sept 2026**.
- “A basic setup with one or two channels, contact import and team access can go live in days.”
- “A simple rollout can show impact quickly,” while deeper CRM sync, routing rules and AI Agent logic take longer because they need testing.
- Before launch, teams should define when AI Agents qualify, route and hand off to human reps.
- The page does not document knowledge generation from past conversations or tickets, historical-conversation replay/testing, traffic rollout modes, or pre-launch readiness/coverage/quality scores.

### https://respond.io/faqs/how-fast-can-we-go-live-on-respondio
Indexed date: 2026-09-23

- Teams can connect a channel, import contacts and deploy an AI Agent on respond.io in one day.
- Most teams can launch an AI Agent template within an hour.
- Users can select ready-made templates such as AI Receptionist or AI Sales Agent.
- Users can link a website or help documents to begin automating FAQs.
- Routing rules can assign complex questions or high-value inquiries to the appropriate human team for follow-up.
- No information is provided about generating procedures from past conversations or tickets, replay/simulation testing, rollout controls, readiness or quality scores, or resolution-rate claims.

### https://roadmap.respond.io/changelog/all-new-ai-agents-have-arrived
Indexed date: 2019-03-08

- AI Agents are powered by GPT-5.
- Ready-to-use sales and support templates can be customized.
- Knowledge sources can include uploaded files and websites.
- AI Agents can be set as the default to handle every new conversation.
- The page does not document generating guidance or procedures from past conversations/tickets, historical-conversation replay or simulation, test sets, topic/channel/hour/audience/traffic rollout controls, draft/suggest/shadow/copilot modes, readiness or coverage scores, or time-to-value/resolution-rate claims.
- No announcement date is shown.

### https://respond.io/help/workflows/how-to-migrate-ai-objective-legacy-workflows-to-ai-agents
Indexed date: 2025-12-11

- Page date: **17 Aug 2026**.
- AI Agents can use multiple knowledge sources, including **Help Center articles, product or policy guides, company FAQs, and internal documents**.
- AI Agents cannot use **Snippets** as knowledge sources; copy Snippet content into a document or the Agent’s Instructions.
- Testing is optional and uses a **test conversation** to check knowledge-base answers, contact-detail collection, and human escalation.
- Conversations can be routed manually from **Inbox → Assign → AI Agent Name**.
- Automatic routing supports **Unassigned Contacts only** (default) or **All new conversations**.

### https://respond.io/faqs/is-there-a-learning-curve-in-using-respondio
Indexed date: 2026-09-22

- AI Agents can be trained to qualify leads, recommend products, book appointments, facilitate payments, and hand off to human agents.
- The in-workspace Copilot acts as an interactive AI Agent builder with no coding required; it says users can get an AI Agent running “on the same day.”
- Eligible businesses receive onboarding specialists’ guidance through AI Agent training.
- The onboarding program “reduces the time-to-value” of the platform’s full feature set.
- The page does not document generating guidance from past conversations or tickets, historical-conversation replay or simulation, rollout controls, readiness/coverage/quality scores, or resolution-rate claims.
- No page date or announcement date is shown.

### https://respond.io/help/quick-start/getting-started-with-respondio
Indexed date: 2026-05-28

- Page date: 17 Aug 2026.
- Step 3 instructs users to click **Set up AI Agent** to create their first AI Agent.
- AI Agents can reply to customers 24/7 and assign conversations to other agents or teams.
- The page states AI Agents can reduce manual workload and improve response times.
- No documented information is provided about generating knowledge from past conversations or tickets, historical-conversation testing, rollout controls, readiness or coverage scores, or time-to-value or resolution-rate claims.

### https://respond.io/why-choose-respondio
Indexed date: 2026-09-22

- Respond.io’s AI Agents work within knowledge sources, CRM data and conversation history to retain context across channels or handoffs.
- Teams can launch AI Agents quickly using templates for workflows such as routing, lead qualification and FAQ responses.
- AI Agent knowledge can be updated with new products, languages or sales processes without coding.
- Teams can connect channels, sync data and start responding to chats or calls “within hours or days.”
- No page date or announcement date is shown.
- No documented details are provided on historical-conversation replay/simulation, test sets, rollout controls, readiness or coverage scores, or resolution-rate claims.

## SleekFlow

### https://help.sleekflow.io/authors/1279280
Indexed date: None

- **Create an AI agent with conversational setup** — Updated September 23rd, 2026. AgentFlow uses a description and available business information to understand the use case, ask follow-up questions when needed, and generate an initial playbook and persona.
- **Set up your AI agent’s behavior and knowledge** — Updated September 23rd, 2026. “Rules” define behavior; “Knowledge” provides information the agent can use.
- **Test and deploy your AI agent** — Updated September 23rd, 2026. Testing and deployment have two stages: test and improve responses, then deploy by choosing where, when, and which conversations the agent should respond to.
- No documented facts were provided about historical-conversation replay, ticket-based training, readiness scores, traffic percentages, shadow/copilot modes, or time-to-value/resolution-rate claims.

### https://sleekflow.io/en-us/faq
Indexed date: 2026-08-31

- AI Agents learn from company information through a dynamic knowledge base.
- Supported knowledge sources include PDFs, Excel/CSV files, Google Docs, Google Sheets, text files, and URLs.
- Up to 10 files may be uploaded, with a maximum total size of 20MB and 1,000 pages per file.
- AI Agents automatically learn and adapt when uploaded files are updated.
- Testing involves sending sample messages, rating responses with thumbs up/down, refining based on feedback, and iterating until satisfied.
- The page documents deployment to WhatsApp, Instagram, or other channels.
- No historical-conversation replay, simulation, test-set, topic/intent rollout, hours, audience, traffic-percentage, draft, suggest, shadow, or copilot controls are documented.
- Businesses using AI Agents reportedly see human agent workload reduced by ~50%, top-funnel expansion by ~70%, and off-hours conversion increased by ~30%.

### https://help.sleekflow.io/agentflow/set-up-test-deploy-and-manage-an-agentflow-ai-agent?kb_language=en_US
Indexed date: 2026-05-27

- SleekFlow may generate articles from ingested knowledge-source content; articles structure and organize content for agent reference.
- Playbooks define conversation instructions, including tone, general behavior, restrictions, scenario handling, and information to collect.
- Testing includes chat simulation and response batch tests using auto-generated questions based on knowledge sources; historical conversations or tickets are not mentioned.
- Deployment controls include channel selection, reply days/hours, overnight windows, and custom audiences based on phone number, keyword, or contact label.
- No topic/intent targeting, traffic-percentage rollout, draft/suggest/shadow/copilot modes, readiness/coverage scores, time-to-value claims, resolution-rate claims, or page date are stated.
- Batch testing provides an overall confidence score and confidence categories such as “Excellent” and “Needs attention.”

### https://help.sleekflow.io/en_US/agentflow/set-up-test-deploy-and-manage-an-agentflow-ai-agent
Indexed date: 2026-03-23

- Updated September 23, 2026.
- AgentFlow requires at least one Knowledge Base source before testing; sources may include uploaded files, web pages, live web search sources, custom answers, and existing sources.
- Playbook instructions define conversation guidance and permitted actions.
- Testing includes simulated chat and response batch tests using auto-generated questions based on uploaded knowledge sources; the page does not document replaying or testing against historical conversations or tickets.
- Deployment controls include channel, active days/hours, custom audience conditions (phone number, keyword, contact label), and exit conditions.
- The page does not document topic/intent targeting, percentage traffic, draft/suggest/shadow/copilot modes, readiness/coverage scores, time-to-value claims, or resolution-rate claims.

### https://help.sleekflow.io/en_US/agentflow/create-and-set-up-your-ai-agent-with-conversational-setup-tool
Indexed date: 2026-06-18

- Updated September 23, 2026.
- AgentFlow uses the described use case and available business information to generate an initial playbook.
- It automatically generates an agent persona.
- Procedures are generated only for use cases involving structured steps or workflows; simpler FAQ use cases may not include procedures.
- AgentFlow does not use previous customer conversations to generate the playbook.
- Agents should be tested before deployment, but the page specifies no historical-conversation replay, simulation, test sets, or test-chat method.
- No rollout controls, readiness or quality scores, time-to-value claims, or resolution-rate claims are documented.

### https://sleekflow.io/agentflow
Indexed date: 2026-08-31

- AgentFlow crawls websites and scans internal documents to generate structured AI knowledge articles; users can review, edit, and manage the AI’s memory.
- It analyzes every conversation to identify patterns and gaps, then supports approval of knowledge updates, playbook refinements, and tone adjustments.
- Human feedback can flag knowledge gaps, correct misunderstandings, and provide exemplary replies.
- The page documents no historical-conversation replay/simulation, test sets, test chat, rollout controls, readiness scores, time-to-value, or resolution-rate claims.
- Reported metrics: 80% of conversations fully handled by AI; 2× more qualified leads; 150% sales conversion rate.

### https://sleekflow.io/partner
Indexed date: 2026-08-31

- Inbound Agent supports control over persona, tone, and SOPs; it qualifies leads, recommends products, scores intent, and hands off to a human.
- Copilot surfaces customer insights, suggests replies, pulls verified sources, and supports drafting, research, and translation.
- The page does not document onboarding from past conversations or tickets, historical-conversation replay/simulation, rollout controls, readiness/coverage/quality scores, time-to-value, resolution-rate claims, or an announcement date.

### https://sleekflow.io/faq
Indexed date: 2026-08-31

- AI Agents can use uploaded PDFs, Excel/CSV files, Google Docs, Google Sheets, text files, and URLs; limits are 10 files, 20MB total, and 1,000 pages per file.
- Knowledge updates automatically when source files are updated.
- Setup includes configuring tone, response length, behavior, constraints, objectives, guardrails, and human-agent handoff logic.
- Testing is documented as sending sample messages, rating responses with thumbs up/down, refining, and iterating.
- Deployment can publish agents to WhatsApp, Instagram, or other channels.
- No historical-conversation/ticket replay, simulation, test-set workflow, readiness/coverage/quality score, traffic-percentage rollout, or draft/suggest/shadow/copilot mode is documented.
- Claimed results: workload reduced by “~50%,” top funnel expanded by “~70%,” and off-hours conversion increased by “~30%.”

### https://sleekflow.io/
Indexed date: 2021-08-21

- AI agents can be trained on a company’s website and data.
- Users can track AI-agent performance and review AI-driven improvements.
- AI agents resolve issues instantly and route only high-priority cases to human teams, helping maintain high resolution rates.
- The page does not document onboarding from past conversations or tickets, historical-conversation replay or simulation, test sets or test chat, rollout controls, readiness/coverage/quality scores, or time-to-value/resolution-rate figures.
- No page date or announcement date is shown.

### https://sleekflow.io/en-us/blog/live-chat-automation
Indexed date: 2026-03-19

- Page updated **06 May 2026**.
- Audit **90 days of support tickets**; identify the top **15–20 query types** by volume and rank by frequency × simplicity.
- Automated live chat can use **AI or a knowledge base** to answer routine questions.
- The page does not document replay/simulation/testing against historical conversations or test sets; it only mentions test chat generally.
- Automation can trigger by **time on page, page type, referral source, incoming message, lead-score threshold, or exit intent**.
- Bots can operate **24/7**, across website chat, WhatsApp, Instagram, and Messenger.
- Benchmarks: **50–70%+ bot resolution**, **40–60% containment**, and **<5 seconds** first response time.
- Teams typically see measurable deflection and cost reduction within **30–60 days**; full ROI usually takes **3–6 months**.

### https://help.sleekflow.io/configuring-your-ai-agent-with-basic-mode?kb_language=en_US
Indexed date: 2025-09-17

- Knowledge sources can be uploaded, imported from website URLs, or selected from the Global knowledge base; the page does not mention generating guidance or procedures from past conversations or tickets.
- Performance testing automatically generates sample questions from linked documents and evaluates responses; it does not describe replaying or simulating historical conversations.
- The AI agent Playground supports manually sending test messages and previewing responses in real time.
- Flow Builder determines when the agent enters a chat, its channel (for example, WhatsApp), and human handoff.
- No topic/intent, hours, audience, traffic-percentage, draft, suggest, shadow, or copilot rollout controls are documented.
- No pre-launch readiness, coverage, or quality scores, time-to-value, or resolution-rate claims are stated.
- No page date or announcement date is shown.

### https://sleekflow.io/en-us/blog/whatsapp-business-platform
Indexed date: 2023-02-28

- Last updated: 16 Jun 2026.
- AgentFlow, SleekFlow’s AI agent platform, allows users to create a team of AI agents that provide intelligent reply suggestions, automate responses, and help human agents handle more conversations efficiently.
- AI features include sentiment analysis, smart message routing, and conversation summarization.
- The page does not document AI-agent onboarding from past conversations or tickets, historical-conversation replay or simulation, test sets, rollout controls, readiness or coverage scores, or time-to-value or resolution-rate claims.

### https://sleekflow.io/blog/podium-comparison
Indexed date: 2026-09-21

- Page last updated: **21 Sep 2026**.
- SleekFlow AI agents crawl a business’s website and scan internal documents, converting both into structured knowledge articles.
- Premium includes **60-day dedicated onboarding** covering channel setup, AI agent training and automations.
- Every AI response shows its source, referenced knowledge article and interpretation of the customer’s intent.
- No documented generation from past conversations or tickets, historical-conversation replay/simulation, test sets, rollout controls, readiness/coverage/quality scores, or resolution-rate claims.
- Stated time-to-value claim: **“Launch your WhatsApp Business API account in 10 minutes.”**

### https://sleekflow.io/id-id/customer-success-onboarding
Indexed date: 2026-07-21

- SleekFlow Pro users can join the weekly “Automasi dan AI Masterclass.”
- The session teaches users to “Tugaskan AI Agent” and use agentic AI to handle customer questions intelligently 24/7 with human-like intelligence.
- The page does not document knowledge generation from past conversations or tickets, historical-conversation replay/simulation/testing, rollout controls, readiness/coverage/quality scores, time-to-value, or resolution-rate claims.
- No page date or announcement date is shown.

### https://sleekflow.io/en-gb/blog/sierra-comparison
Indexed date: 2026-07-28

- Last updated: 23 Sept 2026.
- SleekFlow: crawl your site and documents into a knowledge base, set playbooks, connect Shopify, HubSpot, or Salesforce, and test an agent before it reaches customers.
- SleekFlow’s AgentFlow shows each reply’s source for auditing and improvement.
- Sierra’s Agent OS supports composing agents from skills, setting guardrails, and running simulations; Agent Studio enables no-code edits.
- SleekFlow can launch in days; Sierra’s vendor-led implementation typically takes several months.
- SACES: SleekFlow agents handle more than 60% of incoming enquiries; 75% of qualified leads convert.
