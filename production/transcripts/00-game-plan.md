---
episode: 0
slug: game-plan
title: "The Game Plan: format, multiple-response items, and how to read a question"
description: "How the CCAR-P exam is built, where the marks sit, how to handle choose-two items, and a four-question method for dissecting any item, demonstrated on the three official samples."
domain: "All domains"
weight: "100%"
target_minutes: 14
---

## In this episode

SAM: Welcome to Pass the Architect. This is episode zero, the game plan, and there is no domain content in it at all.

ALEX: Then what is it for?

SAM: By the end you'll be able to say what you're walking into on exam day and what the pass mark means, rank the seven domains by weight, handle a choose-two item without filling the slot, pace yourself against the clock, and take any item apart with four questions. Then we test those four questions on the three official sample items, and finish with how to use the rest of the series.

ALEX: That matters because marks leak here for reasons that have nothing to do with knowledge. Misreading how many to pick, or bringing in a requirement the stem never stated, costs the same as not knowing the answer.

SAM: So we open the way the exam does, with a scenario and four options. [sting]

## Cold open, format and weights

SAM: Before anything else, an item. A team runs a customer-support agent that can read tickets, draft replies, issue refunds, and delete user accounts. Support staff only ever read tickets and draft replies. Applying least privilege, which change best reduces risk?

SAM: Option A, add logging to the refund and delete tools so misuse can be audited later. Option B, remove the refund and delete tools from the agent's configuration. Option C, keep all the tools but add a confirmation prompt before refunds and deletions. Option D, replace the agent with a larger model that follows instructions more reliably.

ALEX: I want C. Confirmation prompts are what I'd actually ship. Nobody loses a refund path if a manager needs it one day.

SAM: Hold that. We come back to it in ten minutes, and by then you should be able to say exactly why it loses. This is the official sample item for Integration, and it carries most of what this episode is about.

ALEX: Then start with the shape of the thing. What am I walking into on Tuesday?

SAM: Sixty-three items in a hundred and twenty minutes. That is just under two minutes an item, call it one minute fifty to leave room for review. It is proctored, online or at a Pearson VUE test centre.

ALEX: And the pass mark?

SAM: A scaled score of seven hundred and twenty on a range of one hundred to one thousand. It is criterion-referenced: you are measured against a fixed standard, not against the other people sitting it that week. The report gives pass or fail, the scaled score, and your percent correct in each domain. Those domain percentages are for your information; the pass decision uses only the total.

ALEX: Seven domains. Give me the weights and what they mean for effort.

SAM: Integration is nineteen percent. Solution Design and Architecture, seventeen. Evaluation, Testing and Optimization, sixteen. Governance, Safety and Risk, fourteen. Stakeholder Communication and Lifecycle, fourteen. Models, Prompting and Context Engineering, thirteen. Developer Productivity, seven.

ALEX: So the top three are over half the paper.

SAM: Fifty-two percent. In rough item counts: about twelve Integration, eleven Solution Design, ten Evaluation, nine each for Governance and Stakeholder, eight for Models and Prompting, and four for Developer Productivity. The blueprint calls those weights approximate, so treat the counts as a guide, not a promise.

ALEX: Which says spend the most time on Integration.

SAM: It says Integration gets two episodes in this series, and if you re-listen to anything, re-listen to those. But notice the flatness in the middle. Governance and Stakeholder together are twenty-eight percent. Engineers skip the stakeholder material because it sounds soft. It is nine items, and they are some of the most predictable on the paper.

ALEX: Who is the exam written for?

SAM: The guide calls it the minimally qualified candidate: a mid-to-senior architect who takes a business problem to a production system and understands trade-offs across cost, latency, performance, safety and maintainability. It is explicitly not for people whose job is prompt writing in isolation.

ALEX: Meaning it is not a trivia test.

SAM: Meaning almost every item is a scenario with a constraint, and four options that each sound like something a competent engineer might do. You are being asked which one an architect would choose, and the guide's own answer key tells you how that architect thinks. [sting]

## Choose-two items and pacing

ALEX: Now the part that worries me. Multiple-response items.

SAM: Each item tells you how many to select. Read that number first, before the scenario. Then judge every option on its own, true or false, against this scenario. Not "is this a good idea in general", but "is this right here, given what the stem said".

ALEX: So it is really four or five little true-or-false questions stapled together.

SAM: Exactly that. The common way to lose marks is picking one strong option and then a second that is merely reasonable, because you felt you had to fill the slot. If the item says choose two, you pick the two that survive on their own merits. The guide does not say whether partial credit exists, so behave as if one wrong pick costs the whole item.

ALEX: Time strategy?

SAM: Budget one minute forty-five an item. Checkpoints: item twenty-one by thirty-seven minutes, item forty-two by seventy-three, item sixty-three by a hundred and ten, leaving ten minutes for flagged items. If an item is eating more than that, choose your best answer, flag it, and move on. The Review button lists every item and jumps straight to flagged or unanswered ones. Either way, commit an answer before you leave the screen. A blank can never score, and the guide describes no penalty for a wrong answer. Answer all sixty-three. [sting]

## The four-question method

ALEX: Now the method. How do you take an item apart?

SAM: Four questions, in order. One: what are the constraint words? "Least privilege", "most directly addresses both", "first place to investigate", "after a document refresh". Those words decide the answer, so underline them in your head before you read the options.

ALEX: Two?

SAM: Which component does the trigger actually touch? If something changed and then a symptom appeared, the answer lives in the component that change reached. An option that blames something the trigger never touched is a distractor, however plausible.

ALEX: Three?

SAM: Prefer removing the risk at its root over watching it or compensating for it. Logging, alerts, confirmations and dashboards are detective or compensating controls. They have their place, but when an option removes the cause, it usually beats an option that monitors the cause.

ALEX: And four?

SAM: Reject two families on sight unless the stem forces them. "Use a bigger or different model" when nothing points at model capability. And blunt cuts that hit the stated constraint by throwing away something the scenario said was required.

ALEX: So, back to the support agent. Constraint words: "least privilege", and "staff only ever read and draft".

SAM: Good. Component: the agent's tool configuration. It holds two tools the role never uses. Root versus detective: logging, option A, tells you after the fact that a refund was misused. Confirmation, option C, puts a speed bump in front of a capability that should not exist.

ALEX: And D is the bigger-model family.

SAM: Model size has nothing to do with authorization scope. A better model with a delete tool still has a delete tool. The answer is B: remove the refund and delete tools. Least privilege means the capability is gone, so the attack surface is gone.

ALEX: I said C. And my reason, "a manager might need it one day", is not in the stem.

SAM: That is the trap in one sentence. You brought in a requirement the scenario never stated. If the item wanted a manager path, it would say so. Answer the scenario on the page. [sting]

## Samples two and three

ALEX: Second sample.

SAM: An application sends the same eight-thousand-token system prompt and policy document on every request, followed by a short user message that changes each time. Latency and cost are both concerns. Which optimization most directly addresses both? A, truncate the policy document to the first one thousand tokens. B, switch to the smallest available model regardless of task fit. C, put the static system prompt and policy before the dynamic content and enable prompt caching. D, move the policy document into a few-shot example block.

ALEX: Constraint words: "same on every request", "both latency and cost", "most directly". That is caching. C.

SAM: Right, and walk the others.

ALEX: A is a blunt cut. It saves tokens by throwing away policy the app needs. B is the model family, and "regardless of task fit" is the giveaway. D moves the text but does not create a cacheable prefix.

SAM: Good. The mechanism to carry into the exam: caching keys off a stable prefix, so the fixed content goes first and the varying content goes after it. On the Anthropic API the cache has to be marked explicitly; savings are not automatic. A cache hit cuts input cost on the reused part and reduces time to first token.

ALEX: And if someone put a timestamp at the top of that system prompt?

SAM: The prefix changes on every call and the cache never hits. That exact shape shows up in Models and Prompting, and again in Evaluation as a "why did cost rise" diagnosis. Third sample.

SAM: A rag system suddenly returns confident but incorrect answers after a document refresh. Latency and model version are unchanged. What is the most likely first place to investigate? A, the model weights have silently changed. B, the retrieval or indexing step is returning irrelevant or stale chunks. C, the temperature setting is too low. D, the context window has shrunk.

ALEX: Trigger: document refresh. Component it touched: the index. B.

SAM: Yes. And look at what the stem eliminated for you. "Model version unchanged" kills A. Nothing about a refresh changes temperature or the context window, so C and D are causes unrelated to the trigger. A broken re-index or mismatched embeddings feed the model poor context, and the model answers fluently from it.

ALEX: Confident and wrong is the giveaway.

SAM: It is the signature rag failure: a confident answer built on the wrong chunk. Confidence is not correctness, and you will hear that idea in nearly every episode.

ALEX: So the three samples are three of your four questions.

SAM: Sample one is root removal over detective and compensating controls. Sample two is fixing the constraint without discarding required content. Sample three is diagnosing the component the trigger touched. And all three include the bigger-model or wrong-component distractor somewhere. Expect that pattern across the paper. [sting]

## Using the series

ALEX: How should I use the rest of the series?

SAM: Episodes one to five today: Solution Design, Models and Prompting, the two Integration episodes, then Evaluation. Governance, Stakeholders and Developer Productivity this evening. The final drill the night before, and again on the morning of the exam.

ALEX: And when you say "pause here"?

SAM: Pause. Say your answer out loud before we give ours. Recalling an answer does more for you than hearing it twice. In the choose-two drills, say true or false for every option, not just the two you pick.

ALEX: Give me the method once more, short enough to keep in my head on Tuesday.

SAM: Constraint words. Component the trigger touched. Remove the root, not watch it. Reject the bigger model and the blunt cut. And read how many to choose before you read anything else. [sting]

## Recap: the exam tells

SAM: Before the tease, a test. Pause and name the topics this episode covered, with the giveaway for each if you can. [pause]

ALEX: The format and pass mark. The domain weights. Choose-two items. Timing. The four questions. And the three sample items, each one a question from the method.

SAM: Good. Now the same ground as exam tells. If you catch yourself spending more than about one minute forty-five on an item, choose your best answer, flag it and move on, and never leave a blank.

ALEX: If I'm deciding what to re-listen to, think Integration first at nineteen percent, and don't skip Governance and Stakeholder, twenty-eight percent between them.

SAM: If the item says choose two, read that number first, then judge every option true or false on its own against this scenario.

ALEX: If an option logs, alerts or adds a confirmation, ask whether another option removes the cause.

SAM: If something changed and then a symptom appeared, look at the component the change touched. A rag system that turns confident and wrong after a document refresh points at retrieval and the index.

ALEX: If a fixed block repeats on every request and both cost and latency hurt, think a stable prefix and prompt caching, not truncation.

SAM: And if an option says bigger model with nothing pointing at capability, or cuts content the scenario called required, reject it. If you're tempted by a requirement the stem never stated, answer the scenario on the page.

ALEX: Next?

SAM: Next episode, Solution Design: deciding what Claude should own before you choose a single pattern, and why the honest answer is often "not that part".
