---
episode: "A07"
series: "CCAO-F"
slug: troubleshooting
title: "Troubleshooting and optimisation"
description: "Diagnose a poor output by finding what changed, match each symptom to its fix, turn feedback into a tested change, and streamline a repeated workflow without overspending."
domain: "Troubleshooting and Optimization"
weight: "10%"
target_minutes: 14
---

## In this episode

SAM: Welcome to Pass the Architect, Associate Foundations. This is episode seven: troubleshooting and optimisation.

ALEX: And by the end?

SAM: You'll be able to find the cause of a poor output by asking what changed, and match the common symptoms to their fixes. You'll turn vague feedback into a specific change and test it before you trust it. And you'll streamline a workflow you repeat every week, without paying for more model than the work needs.

ALEX: Ten percent, about six items. The trap it fixes: reaching for a stronger instruction or a bigger model before anyone has found the cause.

SAM: So we start with proposals that miss a new service. [sting]

## Cold open: the missing tier

SAM: Here is your opening item. An account manager uses a Claude Project to draft client proposals. The Project's instructions haven't changed, and the service catalogue was uploaded to its knowledge in January. In March, the company launched a premium support tier and announced it on the intranet. Since then, proposals never mention the new tier, even for clients who asked about support. What should she do? Option A: switch the Project to a more capable model. Option B: replace the catalogue in the Project's knowledge with the current version, then test a proposal. Option C: add "always include our newest services" to the Project instructions. Option D: stop using the Project and write proposals by hand.

ALEX: C. It's one line, it takes ten seconds, and it tells Claude exactly what we want.

SAM: Hold that. We come back to it at the end.

ALEX: What are the objectives?

SAM: Three. Identify, diagnose and resolve issues with underperforming prompts or poor outputs. Adjust your approach based on feedback and results. And optimise workflows for efficiency and effectiveness.

ALEX: Start with diagnosis.

SAM: Ask one question first: what changed, or what is missing? Then check the parts in order. The request: is the task, audience or format unclear? The material: is it missing, out of date, or buried in noise? The setup: do Project instructions conflict, or carry an old rule nobody needs now? The conversation: has a long chat piled up drafts and corrections that now contradict each other? And the task itself: is it something a prompt can't fix?

ALEX: What can't a prompt fix?

SAM: Capability. Telling Claude it's critical to get a calculation right doesn't make it better at mental arithmetic. The fix is a mechanism that computes, such as the spreadsheet itself or Claude's code execution feature. Same with knowledge: no instruction makes Claude know a document it was never given.

ALEX: And the symptom list?

SAM: Anthropic's prompting advice maps them. Too generic: add specifics or an example. Off-topic: state the real goal and why you're asking. Inconsistent format: add examples. Made-up details: give permission to say "I don't know", and restrict it to the documents you supplied. Too long or over-built: simplify, because longer prompts are not always better. Suggestions when you wanted action: ask for the change directly.

ALEX: When it goes wrong, I usually just rewrite the whole prompt from scratch. Clean slate, no baggage.

SAM: Sometimes the prompt deserves it. A messy prompt that mixes instructions and data is worth restructuring.

ALEX: So what's wrong with starting over?

SAM: You throw away what worked, and you never learn what broke. If the new one fails too, you're back where you started. The exam rewards the diagnosis. The tell: "most likely cause" or "first step". Find the part that changed and fix that one.

SAM: Pause here and answer before we go on. For each symptom, choose the fix: add examples of the output you want, restrict Claude to the supplied documents and allow it to say it doesn't know, or state the audience and purpose. One: weekly status reports come back in a different layout each week. Two: a contract summary cites a clause number that isn't in the contract. Three: a board briefing reads like an engineering note. Four: customer reply drafts are structured three different ways across the team. [pause]

ALEX: Examples, restrict, audience, examples.

SAM: All four. Layout drift is a format problem, so show the format. An invented clause is a grounding problem, and whoever sends it still checks it against the contract, which is domain two. The wrong register means Claude doesn't know who's reading. [sting]

## Adjusting to feedback

ALEX: Second objective. Adjusting to feedback and results.

SAM: Feedback arrives vague. "It doesn't sound like us." "Too long." Your job is to turn it into a specific instruction with a reason, or into an example. Ask the reviewer for one piece they'd call good, and what exactly is off.

ALEX: My manager said the summaries were too long. So I put "be concise" at the top, in capitals. Isn't that adjusting to feedback?

SAM: It's a start, and capitals do get noticed.

ALEX: But not enough?

SAM: "Concise" has no target. Give one, and the reason: "one paragraph of no more than five sentences, because directors read these on their phones". Anthropic's guidance is that Claude generalises from the reason, not just the rule. The tell: when feedback is vague, pick the option that turns it into something specific you can check.

ALEX: Then I'd make every complaint a new instruction. Feedback in, rule added.

SAM: That rule just went too far. A prompt that grows a patch for every complaint ends up with rules that fight each other. Worse, an old defensive rule keeps applying after the problem it fixed has gone. Claude then deflects or hedges where it could have answered.

ALEX: So the fix can be a deletion.

SAM: Often. Keep a short note of why each instruction was added, so you can tell later whether it's still needed. And when an instruction weighs a cost, state both sides. Say only "avoid this unless absolutely necessary" and Claude avoids it even when it's right. The tell: "overly cautious", "refers people elsewhere even when it could answer". Look for an old or one-sided rule.

ALEX: And results?

SAM: Test a change on a handful of past cases, including ones that already worked, so you see whether the fix broke something else. And when feedback shows the problem is beyond a prompt, say, the workflow needs connecting to a company system, that goes to a Developer or Architect.

SAM: Pause here and answer before we go on. Choose two. A customer service team lead keeps a saved prompt for drafting complaint replies. Two months ago someone added "never mention refunds unless the customer insists". Quality reviewers now report that replies are evasive and never offer refunds that policy allows. Which two actions should she take? A: rewrite that instruction to give both sides: offer the refund when policy allows it, and explain why when it doesn't. B: test the revised prompt on a set of past complaints, including ones it handled well. C: add "be less evasive" in capitals. D: move to a larger model. E: have reviewers rewrite every reply by hand from now on. [pause]

ALEX: A and E. Domain two says high-stakes output gets human review. Refunds are money.

SAM: Review has its place. But E is a compensating control dressed as a fix. It treats the symptom forever, while the cause, a one-sided instruction, keeps producing it.

ALEX: So swap E for B.

SAM: A and B. A removes the cause, B proves it's gone without breaking anything. C patches the patch. D is a bigger model for an instruction problem. [sting]

## Optimising the workflow

ALEX: Last objective. Optimising workflows.

SAM: Efficiency and effectiveness together. Fewer minutes per task, and output that needs less rework. Three moves. First, stop retyping. A prompt you've tested and use every week belongs in a Project, with the prompt as its instructions and the reference documents as its knowledge, which is domain five.

ALEX: Second?

SAM: Match the model to the work. Faster, lower-cost models for high-volume, straightforward tasks; the most capable for complex reasoning. That's domain three.

ALEX: Here I'd simply use the best model for everything. Less rework, fewer surprises, and my time costs more than tokens.

SAM: For a quarterly strategy analysis, I'd agree. Quality matters more there than speed.

ALEX: And for the rest?

SAM: Reformatting three hundred supplier records a week into the house layout is simple, repetitive work. The top model adds cost and wait without adding quality the task needs. The tell: "high volume", "routine", "speed matters" points to a faster, lower-cost model. "Complex reasoning" or "nuanced judgement" points to the most capable one.

ALEX: Third move?

SAM: Manage the conversation. When a long chat has drifted, ask Claude for a summary of the decisions so far, and start a fresh chat with it. That gives it one clean version instead of six contradictory drafts.

ALEX: I'd rather keep going. The old chat has all the history.

SAM: History helps until it holds three versions of the brief. The tell: "long conversation", "started ignoring", "drifted". Summarise and restart.

ALEX: And measuring it?

SAM: Before and after, on the same measure: minutes per report, edits per draft, errors caught in review. Keep human review where the stakes need it, and don't add it where they don't. That's proportionate.

SAM: Pause here and answer before we go on. Every Monday an operations lead spends forty minutes pasting the same long prompt and the same three reference files into a new chat to produce a supplier report. When colleagues cover for her, their reports come out differently. What is the best optimisation? A: set up a Project with her tested prompt as its instructions and the three files as its knowledge, and share it with the colleagues who cover. B: keep one long chat running for every week's report. C: move to the most capable model. D: go back to writing the report by hand. [pause]

ALEX: A.

SAM: A. It removes the retyping and gives everyone the same setup, so the reports match. B piles up weeks of history. C doesn't explain why colleagues differ. D throws away a working process.

SAM: One more, quickly. Pause here and answer before we go on. A marketing team produces two hundred short product descriptions a week from spec sheets, and one strategy analysis each quarter. Which setup balances quality, speed and cost? A: the most capable model for both. B: a faster, lower-cost model for the descriptions and the most capable model for the strategy analysis. C: the lowest-cost model for both. D: research mode for the descriptions. [pause]

ALEX: B.

SAM: B. Match each task to its needs. A overspends on routine work, C underpowers the reasoning, and D adds web lookups the spec sheets don't need. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Alex, you chose C, an instruction to include the newest services.

ALEX: Let me defend it. It costs nothing and it states the intent. Surely it's at least part of the answer?

SAM: The intent is right. But the only catalogue Claude can see is the January one in the Project's knowledge. Telling it to include the newest services is asking for a document it was never given. Instructions can't add knowledge.

ALEX: So B.

SAM: B. The trigger was the launch, so fix the part it touched: replace the knowledge file, then test. A is a bigger model reading the same old file. D abandons a setup that works once its knowledge is current.

ALEX: And the tell?

SAM: "Since then". When a stem names a change and the date the problem started, diagnose the part that change touched. [sting]

## Five to remember

SAM: Five to remember. One: diagnose before you fix. Ask what changed, then check the request, the material, the setup, the conversation and the task.

ALEX: Two: match symptom to fix. Inconsistent format, examples. Invented details, restrict to supplied documents and allow "I don't know". Wrong register, audience and purpose.

SAM: Three: instructions can't add knowledge or capability. Missing or stale material needs the right material; calculations need something that computes.

ALEX: Four: turn vague feedback into a specific instruction with a reason, remove old or one-sided rules, and test on past cases that already worked.

SAM: Five: optimise by saving tested prompts in a Project, matching the model to the work, and restarting long chats from a summary.

## Recap: the exam tells

SAM: Your turn. Pause and name the three objectives, and the first question each one asks. [pause]

ALEX: Diagnosis: what changed? Feedback: what exactly is wrong, and did the fix break anything? Optimisation: where is time or money going on work that doesn't need it?

SAM: Now as exam tells. If the stem names a change and when the trouble started, think the part that change touched.

ALEX: If an option tells Claude to use information it doesn't have, think instructions can't add knowledge.

SAM: If feedback is vague, think turn it into a specific, checkable instruction with a reason.

ALEX: If replies have become evasive or over-cautious, think an old or one-sided rule to fix or remove.

SAM: If someone retypes the same prompt every week, or colleagues get different results, think a shared Project.

ALEX: If it's high volume and routine, think a faster, lower-cost model. And if a long chat has drifted, summarise and restart.

SAM: Next, episode eight: the Associate final drill, every domain at exam pace.
