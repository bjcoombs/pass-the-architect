---
episode: "A08"
series: "CCAO-F"
slug: final-drill
title: "Associate final drill"
description: "Thirty-five quick items across all seven Associate domains, weighted like the paper, then the wrong-answer families to strike on sight, the exam-day essentials in brief, and one last retrieval before you sleep."
domain: "All domains"
weight: "100%"
target_minutes: 18
---

## In this episode

SAM: Welcome to Pass the Architect, Associate Foundations. This is episode eight, the final drill.

ALEX: The night before. What are we doing?

SAM: By the end you'll have answered thirty-five quick items across all seven domains, in the paper's proportions, and you'll know which one domain to replay in the morning. You'll name the wrong-answer families on sight and say why each loses. And you'll have the exam-day essentials in two minutes.

ALEX: Every family we name tonight turns up tomorrow in new clothes. Spotting one in seconds buys time for the hard items.

SAM: Then let's start. [sting]

## Drill: checking outputs

SAM: No new material tonight. I ask, you answer in the pause, then Alex answers. When he misses, one line to fix it, and we move on.

ALEX: And the tally?

SAM: By domain. The worst one is your only replay tomorrow: checking outputs, episode two; workflows, four; governance, six; prompting, one; products and models, three; Projects, five; troubleshooting, seven.

ALEX: Choose-two rules?

SAM: Read how many first, then call every option on its own. Output Evaluation and Validation, twenty-one percent, seven items.

SAM: A project status report from Claude gives the launch date as the fourteenth on page one and the twenty-first on page three. What is this, and what do you do? [pause]

ALEX: An inconsistency. I check the date in the project plan, not by asking Claude, and correct the report.

SAM: The same market-size question, asked three times, gives three figures. Two match. [pause]

ALEX: Go with the figure that came up twice.

SAM: Disagreement between runs flags the fact. Check it at the source; two matching runs are not evidence.

SAM: A procurement manager asks Claude, "why is Supplier C the strongest choice?", and Claude agrees. What went wrong? [pause]

ALEX: The prompt leaked the answer. Ask neutrally, apply the same criteria to every supplier, or ask for the case against C.

SAM: An H R partner wonders whether Claude's draft feedback wording shifts with the employee's gender. Quick test? [pause]

ALEX: Swap the name or the group, run it again, and see whether the wording changes.

SAM: Claude has summarised the termination terms of a new supplier contract for an operations director, who will decide from it whether to exit early. What review fits? A, a colleague checks spelling and layout. B, someone from legal checks the summary against the contract. C, Claude reviews its own summary. D, none, since it stays internal. [pause]

ALEX: B. A decision rides on legal content, so the reviewer must be able to tell if it's wrong.

SAM: B. A is a typo check. C asks the model to vouch for itself. D judges the reader, not the decision.

SAM: An investor relations note was rewritten to sound friendlier, and "subject to board approval" has gone. [pause]

ALEX: The rewrite is wrong. Compare it with the original for figures, commitments and caveats.

SAM: A dropdown. For each, choose inline, artifact or structured data. One, "which of these two dates is later?" Two, forty training sessions with date, trainer, room and capacity, to import into the booking tool. Three, a three-page client proposal you'll revise all week and then send. Four, a quick explanation of one term in a contract. [pause]

ALEX: Inline, structured data, artifact, artifact.

SAM: Four is inline. An artifact is for substantial, stand-alone work you'll revise, reuse or share. The other three are right. [sting]

## Drill: workflows and governance

SAM: Workflow Integration and Solution Design, sixteen percent, six items.

SAM: A finance team asks whether Claude should give the final sign-off on the weekly supplier payment run. [pause]

ALEX: No. High stakes, and the accountability is a person's. Claude can prepare it and flag anything unusual.

SAM: An office manager asks Claude, "how can we make expense approvals faster?", and gets generic good practice. Next move? [pause]

ALEX: Give it the real process: each step, who does it, how long it takes, how often it bounces back. What you give it is the ceiling on the advice.

SAM: Purchase orders are retyped into three systems, and half bounce back for rework. The team wants Claude to speed up the drafting step. [pause]

ALEX: Good plan. Drafting is the visible work.

SAM: Speeding one step just moves the queue. Retyping and rework are structural, so redesign, with a baseline, a checkpoint and a pilot. Connecting the systems is for an Architect or Developer.

SAM: An events coordinator built an artifact that works out event budgets, and finance now wants it pulling live figures from the accounting system for every event. [pause]

ALEX: The prototype was right, and it's the best brief there is. Live figures from a company system is integration: an Architect or Developer.

SAM: A sponsor asks how the pilot went. What goes in your answer? [pause]

ALEX: The value, measured against the baseline. Then the limits, each paired with the control that handles it.

SAM: Choose two. After a two-week pilot, a claims manager wants Claude drafting claim letters across the whole team. Which two belong in the rollout plan? A, the baseline measured before the pilot, and the same measure after rollout. B, a human checkpoint before any letter that decides a claim goes out. C, remove review to keep the full saving. D, promise the team there will be no errors. E, redesign every claims process at the same time. [pause]

ALEX: A and B. C drops the checkpoint where accountability sits, D overpromises, and E is a redesign nobody asked for.

SAM: Governance, Risk and Responsible Use, fifteen percent, five items.

SAM: Your company's A I policy says nothing about using Claude to draft performance improvement plans for staff. [pause]

ALEX: Then it's allowed. The policy was written before anyone used Claude, and not forbidden means allowed.

SAM: For low-stakes internal work, the policy probably does cover you. But this is a decision about a person. Silence is not permission: ask the policy owner first, and keep the clearly allowed work moving.

SAM: The company workspace is waiting on an approval, so a consultant drafts a client report in her personal Claude account. [pause]

ALEX: Shadow A I. A personal account sits under different terms, and the policy decides which data goes where. Use the approved workspace.

SAM: A dropdown. For each, choose disclose A I involvement, or no label needed. One, a routine internal email you drafted with Claude, reviewed and own. Two, a support chat where customers believe they are talking to a person. Three, a submission to a regulator whose guidance asks firms to declare A I use, drafted largely by Claude. [pause]

ALEX: No label, disclose, disclose.

SAM: All three. Disclose where the reader would act differently if they knew. A reviewed routine draft is yours.

SAM: Claude drafts first-round ratings for sixty grant applications against written criteria. Each rating looks reasonable on its own. [pause]

ALEX: Compare the ratings across the set, by applicant group; bias shows in the pattern. And a person makes each decision.

SAM: A sales lead wants Claude to write a post in the voice of a well-known industry figure endorsing the product, to publish as if that person wrote it. [pause]

ALEX: Not appropriate. It impersonates a real person and is designed to mislead, and no review fixes deception. [sting]

## Drill: prompting and models

SAM: Prompting and Task Execution, fourteen percent, five items.

SAM: Which works better: "under two hundred words", or "under two hundred words, because it goes out as a text message to field engineers"? [pause]

ALEX: The second. Claude generalises from the reason to cases you didn't list.

SAM: A policy analyst pastes an eighty-page tender, with her question typed above it. How should she order the prompt? [pause]

ALEX: Long material first, the question after it. And ask Claude to quote the relevant passages before it answers.

SAM: A team lead asks, "how could this summary be improved?", and gets a list of suggestions instead of a better summary. [pause]

ALEX: Ask for the change itself. "Revise it to one page, with the risks first."

SAM: One prompt asks for the market research, the pricing, the risk section and the cover letter at once, and the risk section keeps coming back thin. [pause]

ALEX: Break it into a chain. One stage per prompt, and check each stage before the next one builds on it.

SAM: Choose two. A trainer wants quiz questions in the company's exact format, and the format keeps drifting. Which two steps? A, include one finished question in the exact format. B, if it still drifts, add a few varied examples that show only the format you want. C, add "make it perfect" to the prompt. D, switch to the most capable model. E, add ten examples, including bad ones marked "don't do this". [pause]

ALEX: A and E. Show it what to do and what to avoid.

SAM: A and B. Claude copies examples closely, so show only what you want. C is a polite adjective, D the bigger-model reflex.

SAM: Product and Model Selection, twelve percent, four items.

SAM: A sales lead needs to confirm the date of a client's next public results announcement before a call in ten minutes. [pause]

ALEX: An ordinary chat with web search. Research mode is for many sources, compared and cited, and it uses your limits faster.

SAM: An analyst tried Sonnet on a tangled, multi-step analysis of a merger's knock-on effects, and it struggled. [pause]

ALEX: Opus. Deep, sustained reasoning, and work Sonnet struggled with.

SAM: A planner turns extended thinking up to its highest setting for every quick question. [pause]

ALEX: Save the highest setting for the hardest problems. Deeper thinking takes longer and uses more of your limit.

SAM: A consultant counts on Claude's memory to quote the client's rate card exactly in every chat of her Project. [pause]

ALEX: That's fine. Memory carries it from chat to chat.

SAM: Memory holds what came up, in Claude's words. A rate card quoted exactly belongs in the Project knowledge as the document itself. [sting]

## Drill: Projects and troubleshooting

SAM: Configuration and Knowledge Management, twelve percent, four items.

SAM: A finance analyst wants every answer she gets, in every conversation, to lead with the number. Where does that go? [pause]

ALEX: Her profile settings. It's her preference everywhere, not a rule for one Project.

SAM: A buyer asks Claude, through the Gmail connector, to analyse the spreadsheet attached to a supplier's email. [pause]

ALEX: Gmail shows the attachment's details, not its content. Upload the spreadsheet, or work from it in Drive.

SAM: A new analyst connects Google Drive, but Claude can't open the finance team's forecast folder. [pause]

ALEX: Claude sees only what her own Google account can. She asks the folder's owner for access.

SAM: Choose two. A policy Project serves a whole department, and last month someone's untracked edit brought back a rule that had been retired. Which two steps? A, name an owner who makes the updates. B, give the maintainers "can edit" and everyone else "can view". C, let anyone edit, so errors get fixed faster. D, add "ignore retired rules" to the instructions. E, switch the Project to Opus. [pause]

ALEX: B and C. Keep the editors tight, but let people fix what they spot.

SAM: A and B. C is how the retired rule crept back: users report, the owner updates. D asks Claude to guess, and E is a bigger model reading the same instructions.

SAM: Troubleshooting and Optimization, ten percent, four items.

SAM: The commission totals in a monthly summary are off by small amounts, and the prompt already says "double-check your arithmetic". [pause]

ALEX: Then it's a capability problem, so move to a stronger model.

SAM: Capability is the right diagnosis, which is why no instruction fixes it. The fix is a mechanism that computes: the spreadsheet itself, or Claude's code execution feature.

SAM: After a year of patches, a team's prompt runs to three pages of rules, and the outputs hedge and contradict themselves. [pause]

ALEX: Simplify; longer is not always better. Remove rules whose problem has gone, note why each survivor exists, and test on past cases, including ones that worked.

SAM: A client says the weekly briefings "don't sound like us". [pause]

ALEX: Ask for one briefing they'd call good, and what exactly is off. Turn that into an example or a specific instruction.

SAM: Customer quote drafts started using an old discount table the week someone uploaded a folder of archived quotes to the Project. First move? [pause]

ALEX: Diagnose what that change touched. Retrieval can pull the archive as easily as the current table, so remove the superseded material and retest.

SAM: Tally check. If checking outputs cost you two or more, episode two is your replay: it's a fifth of the paper. [sting]

## The distractor families

SAM: Now the families: the wrong answers that keep coming back. I name it, you give the reason it loses.

SAM: It trusts the model's confidence: it sounded sure, it rated itself highly, two runs agreed.

ALEX: Confidence and fluency are not accuracy. A specific that someone will rely on gets checked at the source.

SAM: It overspends: the top model on routine volume, research for one fact, review for a brainstorm.

ALEX: Match, don't maximise.

SAM: It reaches for a bigger model when the stem shows a vague prompt, a missing field or a stale file.

ALEX: No model knows a document it was never given. Fix the prompt or the material.

SAM: It asks the model to promise what a control should do: "don't keep this", "be fair", "use the latest version". Or it leans on an incognito chat.

ALEX: Instructions can't add knowledge or enforce a policy, and incognito isn't what the policy allows. Fix the data, the file or the process.

SAM: It adds polite adjectives: "be accurate", "be thorough", capitals.

ALEX: They name no gap. Add the missing audience, field, example or reason.

SAM: It offers volume as context: every document, the whole drive.

ALEX: Only what the task needs, and one current version of each.

SAM: It abandons a task that has a safe route: stop, skip, do it by hand.

ALEX: Find the proportionate step that lets the work go ahead. Escalate only what is beyond your role.

SAM: It polishes, adds a caveat, or puts a reviewer on rewrite duty forever.

ALEX: None of those fixes the cause. Polish changes how it sounds, not whether it's right.

SAM: It works around a setup: a personal account, files downloaded by hand every week.

ALEX: Go to whoever owns the setting, and set it up properly once.

SAM: And it rushes: automate the lot today, redesign what works, settle the stakeholders' argument inside a finished document.

ALEX: Map and measure first, let the owners settle conflicts, and keep a checkpoint where accountability sits. [sting]

## Exam day in brief

ALEX: Tomorrow, in brief.

SAM: Government-issued photo I D, unexpired, with the name exactly as registered. Check it tonight.

ALEX: The room?

SAM: Clear desk. Phones, smart watches, headphones and recording devices are prohibited. Online, stay in webcam view throughout. Arrive after the late-arrival window and the fee is forfeit. Decline the confidentiality agreement and the session ends with no refund.

ALEX: The clock?

SAM: It counts down. Item twenty at one hour twenty-three left, forty at forty-seven minutes, sixty at ten. Read how many to pick, and call each dropdown statement on its own. Reread a stem three times, or behind and past two minutes: best answer, flag, move on. No blanks.

ALEX: And the morning?

SAM: Episode nine, for the routine and the noteboard. Then your worst domain from tonight, if there's time, and nothing else. [sting]

## Final retrieval

SAM: One last retrieval before you sleep. Pause and name the seven domains in weight order, with one tell for each. [pause]

ALEX: Output Evaluation twenty-one, Workflow Integration sixteen, Governance fifteen, Prompting fourteen, Product and Model Selection and Configuration twelve each, Troubleshooting ten. Checking outputs: a confident specific gets checked at the source. You take the rest.

SAM: Checking outputs, then. If runs disagree on a fact, check that fact. If a rewrite drops a caveat, the rewrite is wrong.

ALEX: Workflows: one slow step, augment it. Retyping and rework, redesign. A prototype that must reach a company system, escalate.

SAM: Governance: a silent policy on a case about people, ask the owner. A reader who would think a human did it, disclose.

ALEX: Prompting: the reason behind each constraint, long material before the question, and a chain when one part comes back thin.

SAM: Products and models: one current fact, web search. Sonnet struggled on deep reasoning, Opus. Exact wording needed in every chat, Project knowledge, not memory.

ALEX: Projects: a preference everywhere goes in profile settings, and a shared Project gets an owner, with view access for everyone else.

SAM: Troubleshooting: arithmetic needs something that computes, and trouble that starts after a change points at what the change touched.

ALEX: And tonight?

SAM: Sleep. It will do more for your score than another hour of revision.

ALEX: Good luck to everyone sitting it.

SAM: Fluent is not correct. Sized to the stakes, not the maximum. Episode nine is waiting for the morning.
