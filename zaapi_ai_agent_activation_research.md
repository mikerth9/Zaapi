# Zaapi AI Agent Activation: Research Brief

Prepared 25 Sep 2026 (v2, deeper pass) for the Zaapi Head of Product take-home. Hypothesis tested: the 19-day median time-to-live and 39% who never go live come from a confidence/readiness gap and blank-page authoring, not from funnel UX.

Legend: **[Unverified]** means I could not confirm it from a primary source. Blog and vendor-marketing numbers are labelled as secondary.

---

## Executive summary

1. **Supports: Zaapi gives merchants little evidence that the agent is ready.** Testing is a manual chat sandbox with a "Show thinking" trace ([Zaapi Help: Testing](https://help.zaapi.com/ai/testing-ai)). There's no batch test, no coverage score and no replay against historical chats. Intercom ([Evals & Releases](https://www.intercom.com/blog/announcing-evals-and-releases/)), SleekFlow ([batch tests with a confidence score](https://help.sleekflow.io/en_US/agentflow/set-up-test-deploy-and-manage-an-agentflow-ai-agent)), Gorgias ([sandbox on real tickets](https://www.gorgias.com/ai-agent)) and Zendesk ([automation potential report](https://support.zendesk.com/hc/en-us/articles/9877546283930-Viewing-and-using-the-automation-potential-report-to-create-or-enhance-AI-agents)) all offer this.
2. **Supports: authoring starts from a blank page.** Knowledge comes from files, a website import or manual writing. Only two scenario templates exist ("Check order status", "Return or refund"), and the docs mention no auto-drafting from past chats ([Zaapi Help: Training](https://help.zaapi.com/ai/training-ai)). Zaapi already holds merchants' chat history, but it isn't used to bootstrap setup.
3. **Supports: go-live is all or nothing.** Deployment is a Flow Builder template called "AI handles all new chats", or a "Let AI handle" node you add yourself ([Zaapi Help: Deploy](https://help.zaapi.com/ai/deploy-ai)). The docs don't describe suggest/copilot mode, a %-of-traffic ramp or confidence thresholds. Intercom offers gradual ramp, A/B testing and one-step rollback. Gorgias lets you set confidence thresholds and choose which intents the AI owns. Gorgias also tells merchants perfect configuration isn't needed: go live with the essentials, then review at least 10 tickets in week one ([Gorgias docs](https://docs.gorgias.com/en-US/set-up-and-go-live-with-ai-agent-500219)).
4. **Refines: Zaapi's own service design suggests the gap is partly about capability and effort, not only confidence.** Zaapi sells building the AI knowledge base as a paid service ([Service Standards](https://help.zaapi.com/zaapi-service-standards)). It also sells an "AI Success Kit" that promises results in **60 days** ([Pricing](https://www.zaapi.com/pricing)). That suggests Zaapi already knows many merchants can't or won't author the setup themselves.
5. **Challenges: pricing friction may be mistaken for hesitancy.** AI messages are metered separately: 300 free trial messages, then **$40 per 1,000** ([Pricing](https://www.zaapi.com/pricing)). On top of the Basic plan ($79/month), that is meaningful for Thai SMBs. Some merchants who never go live may be making a rational cost decision rather than holding back out of fear. Check this against cohort data.
6. **Challenges: marketplace channels are held back by platform limits, not by confidence.** Lazada caps unanswered seller messages at 5 per day and restricts seller-initiated chats ([Lazada IM API](https://open.lazada.com/apps/doc/doc?nodeId=10544&docId=120971)). TikTok Shop's customer-service API is gated behind **1,000+ authorised sellers or 1M API calls/day**, and order management is only partly supported ([TikTok Shop Partner docs](https://partner.tiktokshop.com/docv2/page/customer-service-api-overview)). At least one major vendor says Shopee SellerChat integration is unsupported ([Channel.io](https://docs.channel.io/help/ko/articles/Shopee-2daba32c)). Zaapi's blog does say its AI agent works on Shopee, Lazada and TikTok Shop with real-time catalogue data ([Zaapi blog, 23 Jul 2026](https://www.zaapi.com/blog/chatgpt-vs-a-proper-ai-agent-whats-the-difference-and-when-do-you-need-to-upgrade)). But Shopee's own rules say **auto-replies don't count towards Chat Response Rate**; only manual replies within 12 hours count, and Preferred Sellers need at least 90% ([Shopee MY CRR guide](https://deo.shopeemobile.com/shopee/seller/seller_cms/3dbc4003bbf8b2ef418c8c35ae0ec860/%5BMY%5D%20All%20about%20Chat%20Response%20Rate%20(CRR).pdf)). **[Unverified]:** whether Shopee classes replies sent through the API by a third-party AI as "auto" or as a seller reply. If they count as auto, a merchant's AI could hurt their seller metrics, and holding back would be the rational choice.
7. **Refines: the stakes are highest exactly when merchants have no time to set up.** Shopee reported **3.5B+ chat messages** over 11.11 ([Shopee MY](https://ms.shopee.com/ssr/news/7e1c54cffe39fa8963d645043e3051d3/)). TikTok Shop enforces a **12-hour response rate** (below 85% can trigger penalties, enforced from 6 Jul 2026) ([TikTok Shop PH](https://seller-ph.tiktok.com/university/essay?knowledge_id=8900239889549058&default_language=en&identity=1)). A bad AI answer during a sale carries real penalty risk, which is a rational reason to hold back.
8. **Refines: language is a readiness risk merchants can't judge for themselves.** Thai–English code-switching still degrades LLMs, especially smaller or quantised ones ([arXiv 2410.17145](https://arxiv.org/pdf/2410.17145)). A merchant chatting with a sandbox can't tell whether the agent will handle Thai slang and Thai-English mixing at scale. Replaying the merchant's own past chats would show them.
9. **Supports, with academic evidence: control drives adoption.** People are much more willing to use an imperfect algorithm if they can adjust its output, even slightly. How much they can adjust matters less than having some control at all ([Dietvorst et al., Management Science 2018](https://econpapers.repec.org/article/inmormnsc/v_3a64_3ay_3a2018_3ai_3a3_3ap_3a1155-1170.htm)). That points to suggest/edit-before-send mode as the lever for moving merchants from testing to live.
10. **Net verdict:** the hypothesis largely holds but needs two additions. (a) Readiness evidence should come from the merchant's own history, not from them typing test questions. (b) Some of the 39% are driven by channel coverage (marketplace API limits) and unit economics, which confidence-building won't fix. Segment the 39% by channel mix and plan before committing to a solution.

---

## 1. Zaapi today

### Positioning, pricing, segments, markets
- **Positioning:** "The All-In-One Conversational AI Platform". The AI agents cover FAQs, routine queries, appointments and lead qualification ([zaapi.com](https://www.zaapi.com/)). The homepage leans towards enterprise ("from global enterprises to growing businesses"). Third-party profiles describe the core base as e-commerce, marketplace and social sellers and SMB retail teams in **Thailand, Singapore, Malaysia and the Philippines**, founded 2021 and Singapore-registered ([Agentic Index](https://agenticindex.io/vendors/zaapi)). The about page lists offices in Singapore and Bangkok ([Zaapi About](https://www.zaapi.com/th/about-us)).
- **Pricing** ([zaapi.com/pricing](https://www.zaapi.com/pricing)), per month with 3 users included:

| Plan | Monthly | Annual (per month) | Extra user |
|---|---|---|---|
| Basic | $79 | $59 | $35 |
| Pro | $129 | $97 | $49 |
| Advanced | $179 | $134 | — (not captured) |

- AI is metered separately: $40 per 1k messages, $360 per 10k, $3,000 per 100k.
- Trial: 7 days with up to 300 free AI messages ([Service Standards](https://help.zaapi.com/zaapi-service-standards)).
- The Advanced plan adds AI auto-translation and Shopify features ([Pricing](https://www.zaapi.com/pricing)).
- Zaapi also sells done-for-you AI setup ([Service Standards](https://help.zaapi.com/zaapi-service-standards)) and an "AI Success Kit" with a 60-day promise ([Pricing](https://www.zaapi.com/pricing)).
- Support hours are Mon–Fri, 09:00–18:00 ICT. Human follow-up targets range from 4 business hours to 4 business days ([Service Standards](https://help.zaapi.com/zaapi-service-standards)). There is no weekend support, which is a problem for merchants going live before a weekend sale.

### What the help docs say about setup
- **Knowledge:** added under AI Agent › Train › Knowledge source. You can upload .txt, .csv, .docx or .xlsx files, import a website, or write it manually. PDFs are not supported. Each source can be assigned to specific integrations (Facebook Page, Instagram, LINE OA) to keep brands separate ([Training](https://help.zaapi.com/ai/training-ai)).
- **Scenarios:** "the playbook for your AI", written as step-by-step instructions. Only two templates exist: order status and return/refund. Scenarios can escalate to a human ([Training](https://help.zaapi.com/ai/training-ai)).
- **Personality:** tone, style and rules ([Training](https://help.zaapi.com/ai/training-ai)).
- **Testing:** a manual sandbox where you pick the integration. "Show thinking" shows which knowledge or scenario the agent used. The docs suggest checking accuracy, tone, vague questions and escalation by hand ([Testing](https://help.zaapi.com/ai/testing-ai), [Troubleshooting](https://help.zaapi.com/ai/troubleshooting-ai-issues)).
- **Go-live:** through Flow Builder. You either use the "AI handles all new chats" template or add a "Let AI handle" node. With "Trigger once every new open chat", the AI gets one chance per session. After escalation it only returns once the chat is closed ([Deploy](https://help.zaapi.com/ai/deploy-ai)).
- **Limits:** the AI can't send images, and LINE API messages count towards the merchant's LINE quota ([Service Standards](https://help.zaapi.com/zaapi-service-standards)).
- **Walkthrough video:** Zaapi's own [setup video](https://www.youtube.com/watch?v=OkCHq351Jzs) spends most of its time on writing the knowledge base, scenarios and personality.

Takeaway: all six steps are in the docs, but steps 2–4 are pure authoring, step 5 is manual, and step 6 switches the AI on for all new chats at once.

### Recent product direction (2026)
- **Marketplace AI:** Zaapi's blog says the agent works on LINE, Shopee, Lazada and TikTok Shop, reads context, uses real-time catalogue data and resolves cases 24/7. Setup is described as upload FAQs, connect the catalogue and give writing examples ([Zaapi blog, 23 Jul 2026](https://www.zaapi.com/blog/chatgpt-vs-a-proper-ai-agent-whats-the-difference-and-when-do-you-need-to-upgrade)). The Shopee integration page lists FAQs, shipping, refund requests and stock as automatable ([Zaapi Shopee](https://www.zaapi.com/integrations/shopee)). Shopee is connected through two separate authorisations, shop and chat, each set to 365 days ([Help: Shopee](https://help.zaapi.com/integrations/shopee/how-to-connect)).
- **Recent posts** ([Zaapi blog](https://www.zaapi.com/blog)):
  - "When AI Isn't Enough: How to Escalate to a Human", 13 Aug 2026.
  - "Is an AI Agent Worth It? The Honest Math", 25 Aug 2026, a cost model for 70,000 chats a month. Cost is clearly a live objection.
  - "3 Free AI Prompts to Analyse Your Chat Data", 10 Sep 2026, on finding knowledge gaps from chat history. Zaapi is already nudging merchants to mine their history, but manually.
- **Marketplace Review Automation:** the AI "determines when to reply automatically, and when to pause or escalate" ([Zaapi LinkedIn](https://www.linkedin.com/posts/zaapi-official_zaapi-marketplacereviews-automation-activity-7425011421848948737-skuE)). That kind of built-in judgement is the pattern the chat AI agent lacks.
- **Customer proof points** are framed around chat response rate: Panacee reached a 100% response rate, Karmart +30%, and VCommon doubled its Shopee response rating ([Zaapi SG](https://www.zaapi.com/en-sg)). Response-rate KPIs may be how merchants judge the AI.
- **WhatsApp cost change:** from 1 Oct 2026 Meta plans to charge for service replies inside the 24-hour window ([Zaapi blog](https://www.zaapi.com/blog)). That adds a second cost layer on WhatsApp-heavy MY/ID merchants. **[Unverified]:** the Meta primary announcement.

### News, funding, reviews
- **Funding:** $4M seed led by GFC, Flourish Ventures and Partech ($4.5M total). Other investors include 1982 Ventures, Kaya Founders, Iterative and Sequoia Surge ([Partech](https://partechpartners.com/news/zaapi-raises-a-total-of-us45m-to-empower-southeast-asias-small-businesses-through-mobile-first-e-commerce), [RYT9](https://www.ryt9.com/s/prg/3306406)). **[Unverified]:** any later round. I found none.
- **Recent product news:** automatic translation of incoming messages ([Zaapi LinkedIn](https://www.linkedin.com/posts/zaapi-official_zaapi-automation-ai-activity-7437774694788886529-tdNC)). The COO has run a webinar on AI escalation and the cost of AI support ([Zaapi blog](https://www.zaapi.com/blog)).
- **Reviews:** the sample is small and positive. Capterra shows 5.0 from about 11 reviews ([Capterra](https://www.capterra.com/p/10031470/Zaapi/)) and Software Advice 5.0 from 10 ([Software Advice](https://www.softwareadvice.com/product/530238-Zaapi/)).
  - One G2 reviewer says the AI "has proven to work very well, easy to train and update" but wants more conversational analytics ([G2](https://www.g2.com/products/zaapi/reviews/zaapi-review-12980232)).
  - Another likes marketplace integration but notes "we haven't used it yet" for some features ([G2](https://www.g2.com/products/zaapi/reviews/zaapi-review-13368756)).
  - **[Unverified]:** I found no public complaints about setup or AI accuracy on G2, Capterra, app stores or Facebook groups. The review base is too small and probably skewed (reviews look like they were solicited). Facebook groups couldn't be searched. Competitor Chatcone publishes a Chatcone-vs-Zaapi comparison ([Chatcone](https://www.chatcone.com/chatcone-vs-zaapi/)), which is marketing, not evidence.

---

## 2. How competitors onboard AI agents

| Vendor | How knowledge gets in | Readiness / evaluation | Go-live controls | Time-to-value claim |
|---|---|---|---|---|
| **Zaapi** | Files, website import, manual text; 2 scenario templates ([Help](https://help.zaapi.com/ai/training-ai)) | Manual sandbox, "Show thinking" ([Help](https://help.zaapi.com/ai/testing-ai)) | All new chats via a Flow template; one AI attempt per session; handover to agent or label ([Help](https://help.zaapi.com/ai/deploy-ai)) | None; AI Success Kit promises 60 days ([Pricing](https://www.zaapi.com/pricing)) |
| **respond.io** | Docs (pdf, docx, csv…), images, URLs ([Help](https://respond.io/help/ai-agents/managing-ai-knowledge-sources)); Receptionist, Sales and Support templates with pre-filled prompts ([Help](https://respond.io/help/ai-agents/getting-started-with-ai-agents)) | Automated config "Review" and "Apply fixes"; test simulator ([Help](https://respond.io/help/ai-agents/getting-started-with-ai-agents)) | Assign via workflow or default assignee; human Takeover ([Help](https://respond.io/help/ai-agents/getting-started-with-ai-agents)) | "Trained… in minutes" ([FAQ](https://respond.io/faqs/what-can-respondio-ai-agents-handle-and-how-are-they-trained)) |
| **SleekFlow** | Files, web pages, live web search, custom answers; auto-turns sources into knowledge articles ([AgentFlow](https://sleekflow.io/agentflow)); vertical templates (e-commerce, booking…) | **Batch tests generated from knowledge, with an overall confidence score and "Needs attention" flags** ([Help](https://help.sleekflow.io/en_US/agentflow/set-up-test-deploy-and-manage-an-agentflow-ai-agent)) | Per channel, active hours, **audience by label/keyword/phone**, exit conditions (same source) | 3-step wizard (same source) |
| **Intercom Fin** | Content, Procedures, Guidance, data connectors | **Batch tests from past conversations (30–90 days, up to 50 questions per group)** ([Help](https://www.intercom.com/help/en/articles/10521711-batch-test-fin-ai-agent)); simulations with LLM-judge Evals; Monitors on live chats ([Blog](https://www.intercom.com/blog/announcing-evals-and-releases/)) | **Releases: gradual traffic ramp, A/B test, pause, one-step rollback** (same blog) | "Under an hour" ([Help](https://www.intercom.com/help/en/articles/10118495-fin-for-platforms-explained)) |
| **Zendesk AI agents** | Help centre, gen-AI article drafts | **Automation potential report on the last 90 days of tickets, with gap detection** ([Help](https://support.zendesk.com/hc/en-us/articles/9877546283930-Viewing-and-using-the-automation-potential-report-to-create-or-enhance-AI-agents)); pre-publish testing ([Help](https://support.zendesk.com/hc/en-us/articles/9462994470810-Testing-an-AI-agent-before-publishing-it-for-customers-Legacy)) | Agent Builder for build/test/deploy ([Relate 2026](https://www.zendesk.com/newsroom/press-releases/relate-2026/)); new guided self-serve onboarding rolled out May–Jun 2026 ([Announcement](https://support.zendesk.com/hc/en-us/articles/10487730059034-Announcing-expanded-access-to-AI-agent-capabilities-for-all-Zendesk-customers)) | "Up and running faster" (no number given) |
| **Tidio Lyro** | Website URLs plus Q&A ([Help](https://help.tidio.com/hc/en-us/articles/9003475527196-Lyro-the-conversational-AI-agent)) | Playground ([Help](https://help.tidio.com/hc/en-us/articles/15607494952604-Lyro-a-quick-setup)) | Channel activation, handoff and online/offline settings (same source) | "In just 10 minutes" (same source) |
| **Gorgias AI Agent** | Shopify store data, help centre, catalogue, policies, **past conversations**; Gaia can draft a ready-to-use knowledge base ([Product](https://www.gorgias.com/ai-agent)); guidance and action templates ([Docs](https://docs.gorgias.com/en-US/set-up-and-go-live-with-ai-agent-500219)) | **Sandbox runs on real tickets before launch**; Playground (same sources) | Per channel; **confidence thresholds and owned intents**; handover with context; "review 10+ tickets in week 1" (same sources) | "Live in under an hour" ([Product](https://www.gorgias.com/ai-agent)) |
| **SEA local: Chatcone (TH)** | Unified inbox and AI chatbot for LINE OA, FB, IG, WeChat, web, TikTok ([Chatcone](https://www.chatcone.com/), [FAQ](https://www.chatcone.com/faq/)) | **[Unverified]** | **[Unverified]** | — |
| **SEA local: Botnoi (TH)** | No-code LINE, FB, WhatsApp bots, voicebot; GPT on LINE OA ([Botnoi](https://botnoi.ai/), [Blog](https://botnoigroup.com/blog/chatgpt-in-line-oa-nocode-100)) | **[Unverified]** | **[Unverified]** | "Create → Connect → Deploy in 3 steps" ([Botnoi](https://botnoi.ai/)) |
| **Omnichat (HK/SEA)** | Website-URL onboarding pulls in brand, tone and knowledge; natural-language objectives generate flows ([PR Newswire, 5 May 2026](https://www.prnewswire.com/apac/news-releases/omnichat-transforms-into-ai-native-customer-experience-platform-omni-ai-with-agentic-ai-workforce-302761252.html)) | Sandbox stress-testing before live (same source) | **Human "AI Supervisors" coach agents and approve critical actions** (same source) | "Concept to live in seconds" (same source) |
| **Oho Chat (TH)** | Connects external agent platforms (n8n, Make, Zapier) via webhook and API ([Oho](https://www.oho.chat/feature-page/chatbot)) | None found | Channels switched on and off individually; AI and admin take turns; handoff to admin (same source) | Up to 70% less night-shift load (same source) |
| **SEA local: Page365 (TH)** | Rule-based auto-reply for FB, LINE, IG; scheduled replies for holidays and nights ([Page365](https://www.page365.net/auto-respond-chatbot)) | None found | Schedule by date/time (same source) | — |

Outcome benchmarks are vendor-reported. Gorgias: about 10% average automation across 500+ brands, 30% for top performers, and +5% GMV in A/B tests ([SaaStr](https://www.saastr.com/rolling-out-ai-agents-to-16k-smb-brands-with-gorgias-cto/)). The Gorgias marketing page says 60% ([Gorgias](https://www.gorgias.com/ai-agent)). Treat the headline figures with caution.

### Patterns most relevant to Zaapi
1. **Readiness evidence from the merchant's own history.** Intercom batch tests, Zendesk automation potential and the Gorgias sandbox all replay the merchant's past conversations and report coverage. Zaapi already has these chats in its inbox.
2. **Generated drafts instead of blank pages.** SleekFlow turns sources into articles, Gorgias Gaia drafts the knowledge base, and respond.io and SleekFlow offer role and vertical templates. Zaapi's two scenario templates are thin by comparison.
3. **Graduated autonomy.** Intercom offers a traffic ramp and rollback. Gorgias offers confidence thresholds and owned intents. SleekFlow can target audiences and hours. Zaapi's model is effectively "AI handles all new chats".
4. **Automated config QA.** respond.io's "Review → Apply fixes" catches conflicting instructions before launch, which gives confidence without the merchant having to test by hand.
5. **"Launch small, refine live" plus a first-week review ritual** (Gorgias). The launch is framed as reversible, and that lowers the bar for going live.

---

## 3. SEA market context

### Channels by country
- **Thailand, LINE:** LINE Thailand reports **56M users** and **12B+ LINE OA conversations in 2025**, via Marketing Oops as summarised by [Relevant Audience](https://www.relevantaudience.com/digital-marketing-en/line-thailand-business-solutions-2026/). This is secondary reporting of a LINE disclosure. The country has 51.0M social media identities ([DataReportal 2025](https://datareportal.com/reports/digital-2025-thailand)).
- **Malaysia and Indonesia, WhatsApp:** about 92% (MY) and 91.3% (ID) of internet users use WhatsApp, citing Digital 2025 ([Moca, secondary](https://www.linkedin.com/posts/moca-advertising_messagingstrategy-southeastasiamarketing-activity-7356519033006968832-x-Dd)). **[Unverified]:** I didn't access the primary DataReportal page; figures vary across sources ([digiexe](https://digiexe.com/blog/whatsapp-users-statistics/)).
- **Philippines, Facebook and Messenger:** 94.9% of internet users are on Facebook and 90.6% on Messenger ([GMA News](https://www.gmanetwork.com/news/scitech/technology/991811/filipinos-time-tiktok-facebook-report/story/)).
- **Vietnam, Zalo:** 79.6M MAU and 2.1B+ messages a day as of end-2025 ([Vietnam.vn](https://www.vietnam.vn/en/79-6-trieu-nguoi-dung-zalo-thuong-xuyen-hang-thang), [Zalo](https://zalo.me/en/product/zalo/)). Zaapi doesn't appear to list Zalo or Vietnam ([Agentic Index](https://agenticindex.io/vendors/zaapi)).
- **Thai LINE chat commerce** (LINE Thailand at Bootcamp Day 2026): Thai brands close 85–98% of chat-commerce sales, 67% of customers rebuy through the same chat, 86% would pay more for faster chat, and LINE OA chats have grown about 6% a year over three years ([Brand Buffet](https://www.brandbuffet.in.th/2026/03/line-bootcamp-day-2026-chat-commerce-trends/)). In Thailand the chat is the checkout, so a wrong AI answer costs a sale, not just a support ticket.
- **Chat commerce adoption:** over 40% of Thai respondents have bought through conversational commerce, the highest in the region ([KrAsia](https://kr-asia.com/shoppers-in-southeast-asia-prefer-to-buy-using-chat-or-voice-applications-according-to-joint-study)).

### Marketplace chat APIs: can third parties take order actions?
- **Lazada:** the IM Open API supports sending messages, including order, refund and voucher cards (templates 10007, 10011, 10008). Restrictions:
  - Don't poll the API; permissions can be revoked immediately.
  - A seller can send at most 5 messages if the buyer hasn't replied within a day.
  - Seller-initiated chats need an order within 7 days.
  - Messages can't be recalled.

  Source: [Lazada Open Platform](https://open.lazada.com/apps/doc/doc?nodeId=10544&docId=120971), [SendMessage](https://open.lazada.com/apps/doc/api?path=/im/message/send). Order actions go through the separate Order APIs, not chat.
- **TikTok Shop:**
  - Access to the customer-service API needs 1,000+ authorised sellers or 1M API calls/day.
  - Text messages are capped at 2,000 characters.
  - Buyer outreach needs a prior chat within 30 days or an order within 60 days.
  - Conversations close 6 hours after the buyer stops replying.
  - You can send order cards, and order context comes via the Order API.

  Source: [TikTok Shop Partner](https://partner.tiktokshop.com/docv2/page/customer-service-api-overview). Sellers must respond within 12 hours ([TikTok Shop VN](https://seller-vn.tiktok.com/university/essay?knowledge_id=6837793230014209&lang=en)). From 6 Jul 2026, a 12-hour response rate below 85% can trigger penalties ([TikTok Shop PH](https://seller-ph.tiktok.com/university/essay?knowledge_id=8900239889549058&default_language=en&identity=1)).
- **Shopee:** the Open Platform covers orders, logistics, returns and refunds ([apis.io](https://apis.io/providers/shopee/)). Open API access is restricted to eligible seller or ISV types, at least in Taiwan ([Shopee TW guide](https://deo.shopeemobile.com/shopee/seller/seller_cms/b35f495dbde17396b6047c375cc2e04b/%5BOpen%20API%5DTW%20%E9%96%8B%E7%99%BC%E6%8C%87%E5%8D%97%20(2021_04_26).pdf)). Channel.io, a major vendor, says SellerChat 1:1 integration is **not supported** for its setup but order cancellation is ([Channel.io](https://docs.channel.io/help/ko/articles/Shopee-2daba32c)). **[Unverified]:** Shopee's chat API terms and rate limits for whitelisted partners like Zaapi. The primary docs require a login.
- **Response-rate rules (the hidden constraint):**
  - Shopee: Chat Response Rate counts replies within 12 hours over 90 days. **Auto-replies are excluded**, as are vacation-mode and FAQ Assistant replies. Preferred Sellers need at least 90% ([Shopee MY CRR](https://deo.shopeemobile.com/shopee/seller/seller_cms/3dbc4003bbf8b2ef418c8c35ae0ec860/%5BMY%5D%20All%20about%20Chat%20Response%20Rate%20(CRR).pdf)).
  - Shopee's 2.0 API does have a Chat module and a "Customer Service" app type, though at the time they were unavailable in Taiwan. So chat access varies by market ([Shopee TW API 2.0](https://deo.shopeemobile.com/shopee/seller/seller_cms/05c34d17a93e5cf73f77d0fcb8bb2b44/%5BTW%20Open%20API%5D%202.0%E6%8E%A5%E5%8F%A3%E4%BB%8B%E7%B4%B9.pdf)).
  - Lazada, per a secondary summary: a healthy average response time is 30 minutes or less, with a "10-minute response rate" (8am–11pm) of at least 50% and about 85%+ Chat Response Rate for Preferred Seller perks. It advises automating lookups and acknowledgements but keeping refunds and exceptions with humans ([Eleland](https://eleland.co/th/briefs/response-sla-automation-asian-marketplaces/)). **[Unverified]** against Lazada's own seller centre.
- **Implication:** marketplace chats are governed by platform rules, and order actions like cancel or refund are split across separate APIs with eligibility gates. Slower activation on those channels may be structural, whatever the merchant's confidence.

### Seller workload at mega-sales
- Shopee: 3.5B+ chat messages across 11.11 ([Shopee](https://ms.shopee.com/ssr/news/7e1c54cffe39fa8963d645043e3051d3/)).
- Vendors report chat spikes of 3–5x on Harbolnas 11.11 and 12.12 ([Udesk ID](https://id.udeskglobal.com/blog/siapkan-tim-cs-menghadapi-lonjakan-harbolnas-11-11-12-12)), and "up to 500%" in minutes ([Udesk](https://www.udeskglobal.com/blog/the-ultimate-guide-to-southeast-asia-ecommerce-customer-service-systems-scaling-lazada-shopee-and-tiktok-shop.html)). Both are vendor marketing and secondary.
- **Ramadan:** marketplace chat clusters at sahur (03:00–05:00) and after iftar (19:00–22:00), and flash sales produce hundreds of chats in a short window. The recommended response time is under 3 minutes ([Mekari, Indonesian vendor blog](https://mekari.com/blog/mengelola-chat-marketplace-dengan-tim-keci-saat-ramadhan/)). These are exactly the hours when SMB admins are offline, which is the strongest case for AI, but also when an unsupervised mistake is least likely to be caught.
- **[Unverified]:** quantified Ramadan and payday chat multiples from a primary source.

### Language realities
- Google's 2026 Gemini SEA report reportedly finds about 80% of AI interactions in Vietnam, Thailand and Indonesia happen in native languages ([LinkedIn summary, secondary](https://www.linkedin.com/posts/kaanthan_ai-businessautomation-suriasystems-activity-7483085082577272833-dYUa)). **[Unverified]:** the primary report.
- LLMs remain English-centric for SEA languages ([Carnegie](https://carnegieendowment.org/russia-eurasia/research/2025/01/speaking-in-code-contextualizing-large-language-models-in-southeast-asia)). Thai–English code-switching degrades translation quality, especially in compressed models ([arXiv](https://arxiv.org/pdf/2410.17145)).
- **Benchmarks:** on SEA-HELM, GPT-4o scores Indonesian 74.5, Filipino 73.0, Vietnamese 68.1 and **Thai 64.7**, so Thai is the weakest of the four. Dedicated 7–9B SEA-tuned models can close the gap ([SEA-HELM, arXiv 2502.14301](https://arxiv.org/html/2502.14301)). Zaapi's home market is its hardest language.
- **[Unverified]:** the share of Thai, Bahasa, Vietnamese and Tagalog in commerce chats. No public dataset found. Zaapi's own inbox data is the best source.

---

## 4. Evidence on activation

- **Benchmarks (secondary, vendor research):**
  - Userpilot: median time-to-value is about 1.5 days across 547 SaaS companies, and average activation is 37.5% across 62 B2B companies ([Userpilot](https://userpilot.com/blog/time-to-value/), [Userpilot metrics](https://userpilot.com/saas-product-metrics/)).
  - Reaching first value within 14 days is claimed to link to 80%+ month-12 retention, versus 35–50% for those who don't ([ReadSignal](https://www.readsignal.io/article/time-to-value-saas-retention-benchmark-2026)). The methodology is unclear, so treat it as directional.
  - Zaapi's median of 19 days is an order of magnitude slower than the Userpilot median, though AI-agent setup is heavier than typical SaaS activation.
- **Templates and pre-filled setup:** Reforge reports personalised onboarding templates lifted completion by 15%, but cut collaboration by 10% ([Reforge](https://www.reforge.com/artifacts/c/growth/user-onboarding)). That is a useful caution that templates can create shallow activation. Every major competitor now ships templates or auto-drafts (see section 2). That signals where the industry has converged, though it isn't causal proof.
- **Staged rollouts and trust:** Intercom says it built Releases because a 1% regression affects thousands of conversations ([Intercom](https://www.intercom.com/blog/announcing-evals-and-releases/)). Gorgias ties launch confidence to reviewing sandbox output from real tickets ([Gorgias](https://www.gorgias.com/ai-agent)). Enterprise Copilot rollouts ran in staged waves ([Accenture/Microsoft](https://adoption.microsoft.com/files/microsoft-365-community-conference/2026/pdf/MS84%20-%20From%20AI%20to%20Agentic_%20Accenture's%20Copilot%20Agent%20Journey.pdf)).
- **Control and trust (academic):** across three incentivised studies, people were considerably more likely to use an imperfect algorithm when they could modify it, even under tight limits. Satisfaction and continued use rose too ([Dietvorst, Simmons & Massey 2018](https://econpapers.repec.org/article/inmormnsc/v_3a64_3ay_3a2018_3ai_3a3_3ap_3a1155-1170.htm)). The implication is that a merchant who can edit AI drafts before sending should activate more readily than one offered only full autopilot.
- **Transparency:** 95% of consumers expect explanations for AI decisions ([Zendesk CX Trends 2026](https://www.zendesk.com/newsroom/press-releases/contextual-intelligence-becomes-the-new-standard-for-exceptional-customer-experience-in-2026/)). This is consumer-side, but it supports showing sources and reasoning to merchants too, as Zaapi's "Show thinking" already does.
- **What good looks like after launch:** Intercom reports an average Fin resolution rate of 67%, with top teams above 80% ([Intercom Community](https://community.intercom.com/fin-faqs-97)). Gorgias reports about 10% average automation for SMB brands ([SaaStr](https://www.saastr.com/rolling-out-ai-agents-to-16k-smb-brands-with-gorgias-cto/)). The spread shows that "live" and "valuable" are different milestones for SMBs.
- **[Unverified]:** I found no controlled public study showing that suggest mode or a %-of-traffic ramp lifts SMB activation. The evidence is vendor design choices and case studies. That gap is worth saying out loud in the interview.

---

## Questions for Zaapi

1. When you split the 39% who never go live by channel mix (LINE/FB/IG vs Shopee/Lazada/TikTok) and by plan, how much of the gap is channel coverage or AI cost rather than hesitancy?
2. Of the 19 days, where does the time actually go: time spent editing in the knowledge and scenario steps, or idle days between test and go-live? And what happens after a failed test answer?
3. How do merchants who used the paid AI setup service or the AI Success Kit compare with self-serve merchants on time-to-live and 90-day retention? That's a natural experiment on the "authoring gap".
4. Do AI replies sent through the Shopee, Lazada and TikTok APIs count towards each marketplace's response-rate metrics? Have merchants seen their Preferred Seller status affected after going live?
5. Can we legally and technically use a merchant's existing inbox history (within LINE, Meta and marketplace terms) to auto-draft knowledge and scenarios and run a pre-launch coverage score?
