# Review of the Zaapi memo draft

## Overall score: 7.5 / 10

I read the draft against the brief and everything in `~/Documents/Zaapi`: the appendices, persona logs, walkthrough, outline, research and prompts. It's well above a typical take-home. It's grounded in real product testing, it covers all four questions the brief asks, and it names what would prove you wrong and what you'd deliberately not do. What holds it back is that it tries to say too much, and a few claims either contradict your own evidence or aren't fully checked.

| Area | Score | Comment |
|---|---|---|
| Root causes | 8 | Real causes, not a restatement of the funnel. Strongest section. |
| What you'd change | 7 | Concrete, but it's about ten changes, not one clear bet. |
| What you'd do first | 8 | Good sequencing, and a data pull that could change the order is a strong move. |
| How you'd know it worked | 7 | Good section on being wrong. Some targets are weak or mixed up. |
| Evidence and accuracy | 7 | Mostly traceable. A few mismatches (below). |
| Readability | 6 | Very dense, small type, method detail takes up space on page 1. |

## Things I don't think are correct

1. **Aisha contradicts the Kuala Lumpur quote.** The memo says she "won't go live unless she can start small." But the KL merchant in the brief did go live ("We turned it on Friday"). Your own Appendix D says she belongs with the 9 who switched off, not the ones who never went live. Either reframe her as the switch-off case or stop tying her to that quote.
2. **You argue against the thing your persona needs.** Under "don't do," you reject a share-of-conversations slider. Yet the persona summary says Aisha's condition is "10% of WhatsApp first," and her fix is "a gradual rollout (share, channel or topic)." Your competitor argument is reasonable, but say you'd offer staging by channel, hours or topic instead of a percentage, and acknowledge the tension.
3. **The scenarios drop sits under the wrong problem.** Box 2 ("No easy way to test it") claims the 71 → 38 drop. Your Appendix D puts that drop down to nothing prompting scenarios and writing them being hard, which is box 1 and the authoring problem, not testing. Also, the funnel isn't a sequence (66 tested vs 38 wrote scenarios), so "71 to 38" suggests an order the data doesn't have.
4. **Basic and Flow Builder isn't checked yet.** RC3 says going live runs through Flow Builder and Basic doesn't have it. Your walkthrough log says "Not verified: how a Basic merchant goes live without Flow Builder (probably via the Deploy templates)." If Basic merchants go live through the Deploy templates, part of the argument weakens. Either check it or soften it to "appears to."
5. **Opening line vs findings.** "I don't think the agent is the main issue" sits uneasily next to "wrong in ways merchants wouldn't spot" and the stock claim that was false in 4 of 5 runs. A better framing: the agent is capable, but setup produces weak agents and hides it.
6. **The headline target mixes two measures.** "19-day median → under 7 days, 65+ at day 30" mixes a median with a share. Going from 19 days to under 7 is also a big claim with no reasoning behind it. Pick one measure (for example, % live by day 7 and still live at day 30) and give a baseline estimate.
7. **The 30% resolution target is borrowed from the Kit's guarantee.** That guarantee covers done-for-you setups for merchants with 300+ chats a month. Your research notes put Gorgias's average around 10%, with 30% for top performers. For self-serve, 30% is likely too high. A lower first target, or a range, is more believable.
8. **"No worse than today" for wrong answers.** There's no baseline for wrong answers today, so this guardrail can't be measured as written.

## What's missing

- **Evidence bias.** Appendix D says to keep in the memo that all six quotes come from accounts the commercial team deals with (800–9,000 orders a month), with no successful merchants and no small SMBs. The memo drops this. One sentence would show judgement.
- **No Vietnamese testing.** The Ho Chi Minh City quote gets mapped to Joanna in Manila. Say so in the caveats line.
- **The Chiang Mai language quote isn't answered directly.** "Choose how it sounds" should say explicitly: "Your agent replies in your customer's language. Here's a Thai test."
- **Readiness score with no chat history.** It "replays real past questions," but new merchants and those with no history have none. Say what they get instead (for example, a standard set of hard cases: cancel, angry customer, stock, sizing).
- **Renewal link.** The brief frames this as the company's biggest commercial problem. There's no line estimating the renewal or revenue value of moving the day-30 number.
- **Help-article fixes.** Your outline had "correct the wrong help articles" in weeks 0–2. It's cheap and backed by Appendix C, but it was dropped.

## What I'd change

- **Lead with one bet.** Say something like: "The main change: Zaapi drafts the agent and tells you whether it's ready. Everything else supports that." Right now section 4 has 7 steps, 4 problem rows, 3 tiers and a sale pack, and the reader has to find the thesis. It should also match the prototype (setup home plus "See if it's ready").
- **Cut section 3 by about half.** The scoring weights and the Perplexity/Claude Code method belong in an appendix or the prompt log. Keep one line on method plus the persona cards and the key takeaway, which is your best line: "the merchants most likely to launch got the weakest agents."
- **Tone about the brief.** "The brief describes one, but the Deploy page has none" is correct, but it reads as pointing out their mistake. Try "the product today offers only two options…"
- **Commercial framing of the Kit.** "Give away what the Kit sells" could read as protecting a $1,900 service ahead of activation. Frame it as: the free tier gets everyone safe and live, and the Kit becomes the upgrade for depth.
- **Layout.** Page 1 is very dense in small type. Page 2 has spare room at the bottom. Moving some content from page 1 to page 2 and dropping the photos would help readability.
- **Small things:** "Hard to go live in small steps" (box 3) and "Hard to start small" (table row) should use one name. "Weeks 0–6" overlaps "Weeks 0–2", so make the phases clear.

## What's working

These are accurate against your files and worth keeping:

- The $1,900 Kit and 300-chat eligibility line
- The 30% guarantee wording
- The 12- and 6-month re-authorisation limits (Appendix C)
- The auto-connected widget
- The self-check passing a false answer
- The 10/10 best-case result
- The "results that would change the order" paragraph
- Rolling out with a holdout group so a sale month doesn't skew results

Fix points 1–4 and cut the method section, and I'd put this at 8.5–9.
