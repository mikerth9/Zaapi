# Help centre: language and accuracy examples

Read from help.zaapi.com (the Markdown versions listed in `help.zaapi.com/llms.txt`), 25 Sep 2026. Tag: `[help]`. Quotes are short; the full articles are public.

## Jargon an SME owner has to get through to go live

| Article | What it asks of the merchant | Why it's hard for an SME |
|---|---|---|
| Deploy AI | Pick the "Message received" trigger node, then under Flow trigger settings choose "Trigger once every new open chat" | A trigger-frequency setting that decides whether the AI can come back into a chat. Get it wrong and the AI either keeps interrupting or never replies |
| Deploy AI | "make sure you don't have any other active flows with conflicting triggers… can cause unpredictable behavior" | The merchant has to audit their own automations before launch, with no tool to help |
| Deploy AI | Configure the node's "two main exit paths" | Graph-editor terms (nodes, paths, connectors) at the moment they are deciding whether to go live |
| Flow Builder › Set up guide | To test a flow: add a Message Content node with a keyword, **enable the flow on a real channel**, message it, then remove the node | Testing means switching the flow on for real customers. There is no safe test for a flow |
| Best Practices: Knowledge Sources | "Chunking"; use formal H1/H2/H3 headings, "not just bold text" | Asks shop owners to understand retrieval mechanics and document styles |
| Troubleshooting AI | If the AI must follow an exact script, "you may be better off using the Flow Builder" | Sends SMEs to the harder tool |

## One feature, several names

- Go-live node: "Let AI handle" (Deploy AI help), "Let AI Respond" (Action nodes help), "Let AI reply" (the product itself).
- Template: "AI handles all new **chats**" (help) vs "AI handles all new **tickets**" (product).

## Help that is wrong, or points merchants the wrong way

- **Training AI › Limitations: "PDF files cannot be uploaded."** PDFs load `[product]`.
- **The Personality section's example guideline is "Always respond in English."** A merchant who copies it overrides the default, which already matches the customer's language `[product]`. This is exactly the Chiang Mai merchant's worry.
- **Troubleshooting AI, on hallucinations:** for a one-off, "the best course of action is to monitor the situation." In the persona tests, the same question gave a false stock claim in 4 of 5 runs `[persona]`, so it isn't a one-off.

## Things the help centre knows that setup doesn't use

- **Shopee:** "the system will automatically import your past conversation history from the last 90 days" when the channel is connected.
- **LINE:** chat history can be imported (verified OA plus the Chat package, a .zip export, "a few hours").
- **Gmail:** email history import exists.
- **Shopee response rate:** automated messages don't count, but "Messages sent by the AI Agent are treated as human responses." This is a strong reason for marketplace sellers to go live, and it only appears in a Shopee *Limitations* article.

So for many merchants the conversation history is already inside Zaapi. AI setup never offers to use it.

## Coverage

- The help centre is in English and Thai only (walkthrough log).
- The Start guide has six steps (account, channel, team, inbox, analytics, mobile app) and no AI step.
