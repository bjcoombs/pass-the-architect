---
episode: "A04"
series: "CCAO-F"
slug: workflows
title: "Bringing Claude into a workflow"
description: "Pulling requirements out of messy notes without settling the arguments, research and process optimisation that start from real detail, prototyping versus escalating, augmenting a step versus redesigning a process, and explaining Claude's value and limits to a sponsor."
domain: "Workflow Integration and Solution Design"
weight: "16%"
target_minutes: 18
---

## In this episode

SAM: Welcome to Pass the Architect, Associate Foundations. This is episode four: bringing Claude into a workflow.

ALEX: What will I be able to do by the end?

SAM: Pull requirements out of messy notes without letting Claude settle the arguments. Use research mode, and give Claude a real process to improve. Tell a prototype you build yourself from work for an Architect or Developer. Choose between adding Claude to one step and redesigning the process. And explain Claude's value and limits to a sponsor without overselling.

ALEX: Sixteen percent, so about ten of the sixty items. The trap here is the option that sounds most ambitious: automate the lot, starting today.

SAM: Starting with a report everyone hates writing.

ALEX: Go on. [sting]

## Cold open: the weekly report

SAM: Here is your opening item. An operations lead at a logistics firm wants Claude to speed up the weekly supplier-performance report. Today an analyst pulls figures from three spreadsheets, writes two pages of commentary, a manager checks it, and it goes to the procurement director. What should the operations lead do first? Option A: have Claude draft the commentary every week from now on, since writing is where the hours go. Option B: ask Claude to design a new report format and switch to it next week. Option C: map the current steps with the time each takes and where errors creep in, choose the step where Claude helps most while keeping the manager's check, and pilot it for a few weeks against the current report. Option D: hand it to the I T team to build an automated pipeline, because it touches three data sources.

ALEX: A. The commentary is obviously the slow part. Why study it?

SAM: Hold that. We come back to it at the end.

ALEX: So this is domain four. What does the guide actually list?

SAM: Five tasks. Use Claude to analyse requirements and use cases. Use it for research, planning and process optimisation. Use it to support solution design, development and iteration. Integrate it into existing workflows to augment or redesign them. And communicate Claude's value and limitations to stakeholders.

ALEX: Ten items, five tasks. About two each.

SAM: Roughly, and they share one shape. The right answer understands the work before changing it, keeps a human where accountability sits, and measures the result. Distractors rush to automate or refuse to start. [sting]

## Requirements and use cases

ALEX: Start with requirements. What does Claude add there?

SAM: It reads faster than you. Give it interview notes or a meeting transcript, and ask for each requirement, who raised it, where people conflict, and what nobody has said. Then have it draft your follow-up questions.

ALEX: Why not just ask it to write the requirements document?

SAM: Because a finished document reads as settled. If two managers disagree about who approves new suppliers, Claude can lay out both positions, but deciding belongs to the people who own the process. Claude surfaces the conflict; they resolve it.

ALEX: In my job a draft spec gets people talking faster than a list of questions. Put something on the table and they argue with it.

SAM: That works in plenty of meetings, and a strawman draft is a real technique.

ALEX: But not on the exam?

SAM: Not when the stem tells you the inputs conflict. A draft that quietly picks one side buries the conflict inside a document people skim. The tell is "the notes disagree" or "stakeholders want different things": pick the option that flags the conflict and takes it back to the owners.

ALEX: And use cases? How do I judge whether a task suits Claude at all?

SAM: Four questions. Is it mostly language work: reading, summarising, drafting, comparing? Does it repeat enough to be worth setting up? Can a person check the output before it matters? And does Claude have what it needs, or does it depend on systems it cannot see? A weekly status summary from meeting notes passes all four. Final sign-off on a payment run fails: high stakes, and the accountability is a person's.

ALEX: Test me.

SAM: Pause here and answer before we go on. An H R partner has interview notes from five managers about a new onboarding process. Two want laptops ready on day one, two say the first week is fine, and one never mentions equipment. What is the best use of Claude? A: ask Claude to write the final onboarding requirements, resolving the disagreements. B: ask Claude to extract each manager's requirements, flag the conflicts and gaps, and draft follow-up questions, then confirm with the managers. C: use only the most senior manager's notes, to avoid conflict. D: ask Claude which managers are right. [pause]

ALEX: B.

SAM: B. Claude does the reading and sorting; the people who own onboarding settle the conflict. A hides the disagreement in a finished-looking document. C throws away four sets of needs. D hands the model a call that belongs to the business. And the silent manager is a gap to ask about, not a vote. [sting]

## Research, planning and process optimisation

ALEX: Second task. Research, planning, process optimisation.

SAM: For research, match the tool to the question. A quick fact is an ordinary chat with web search. A question that needs many sources, compared and cited, is what research mode is for: Claude runs a series of searches that build on each other and returns a report with citations.

ALEX: And because it's cited, it can go straight into the deck.

SAM: That's domain two calling. Citations make checking possible, not unnecessary. A figure going to a client still gets checked against the source it cites.

ALEX: Fair. Planning?

SAM: Claude breaks a goal into steps, dependencies, owners and risks, and asks what you have not planned for. Give it the real constraints. "Plan our office move" gets a generic plan. "Forty people, two floors, a server room, lease ends on the thirtieth" gets yours.

ALEX: Same for process optimisation, I assume.

SAM: The same, and it is where people under-feed it most. "How can we make invoicing better?" gets general good practice. Describe each step, who does it, how long it takes, how often it bounces back and where the handoffs are, and Claude can point at the actual bottleneck. What you give it is the ceiling on the advice.

ALEX: That's a lot of effort. I'd ask the open question and add detail if the answer is generic.

SAM: Iterating is a good habit, and it is a domain one skill.

ALEX: Then why is it wrong here?

SAM: Because the exam asks for the best move, and generic advice can look plausible enough to act on. If one option gives Claude the real steps, times and pain points, it beats the open question. The tell is "specific to our process": the answer feeds Claude the process.

ALEX: Drill.

SAM: Pause here and answer before we go on. Choose two. A consultant is preparing a client deck on entering a new regional market and needs current competitor and regulation information. Which two steps are most appropriate? A: use research mode, so Claude searches across many sources and returns a cited report. B: check the key figures and regulatory claims against the sources Claude cites before they go into the deck. C: ask Claude to rate its confidence in each claim and keep only the high ones. D: paste the client's confidential pricing model into a personal Claude account for richer analysis. E: use a fast model with web search turned off, to save time. [pause]

ALEX: A and C. Research mode, then filter by confidence. That's efficient.

SAM: A is right. C is the trusting-the-model's-confidence distractor: a model's rating of its own answer is not evidence. The second answer is B, checking the claims against the cited sources.

ALEX: So I picked a shortcut that looks like diligence.

SAM: That's the family. D puts confidential client material in an account the firm doesn't control, episode six territory. E removes what the question needs: current information. [sting]

## Supporting design and iteration

ALEX: Third task. Design and iteration, for someone who doesn't write code?

SAM: Claude gets you from an idea to something people can react to. It generates several options, critiques a draft against your criteria, and builds things you can show: a checklist, a template, or a mock-up of an intake form as an artifact.

ALEX: And iteration means?

SAM: Small, tested steps. Put a version in front of its users, collect what goes wrong, feed it back, and change one thing at a time so you know what helped.

ALEX: Where does it stop being my job?

SAM: The guide is explicit: Associates escalate complex or technical work to Claude Architects and Developers. Connecting to company systems, acting on its own across tools, running for every customer, building against the A P I: their scope.

ALEX: But with artifacts I can build a working tool in an afternoon. A team I worked with ran a quote calculator built in a chat for months. Why hand that to someone else?

SAM: Building it was the right move, and a working prototype is the best brief a Developer can get.

ALEX: Then what's the problem?

SAM: The months. Once it produces real customer quotes, someone has to own its accuracy, data and upkeep, and change it safely. The tell is "production", "integrate with" or "automatically" next to a company system: build the prototype, then escalate.

ALEX: Give me a dropdown one.

SAM: Pause here and answer before we go on. On the exam this comes as four statements, each with its own dropdown. For each, choose: do it yourself with Claude; do it with Claude, with a named reviewer checking before it goes out; or escalate to an Architect or Developer. One: summarise your own notes from yesterday's internal workshop. Two: draft a notice telling customers about a price change. Three: have Claude's replies post automatically into the company's customer system with nobody in between. Four: build an artifact mock-up of a new expense form to gather stakeholder feedback. [pause]

ALEX: One, yourself. Two, reviewer. Three, escalate. Four, yourself.

SAM: All four. One is internal and low stakes. Two goes to customers with a commercial commitment, so someone accountable reads it first. Three connects to a company system and removes the human: integration work. Four is a prototype built to be critiqued. [sting]

## Augment or redesign

ALEX: Fourth task. Augmenting a workflow, or redesigning it.

SAM: Augment means Claude takes on a step inside a process that otherwise stays the same. Redesign means the process changes shape because Claude is there: steps merge, reorder or disappear, and people move from writing to reviewing.

ALEX: How do I choose?

SAM: Look at where the pain is. If the process works and one step is slow, augment that step. If the pain is structural, with handoffs, rework loops, or the same data retyped three times, speeding one step just moves the queue. That calls for a redesign.

ALEX: Either way, what has to be true?

SAM: Three things. A baseline, measured before you change anything, so you can show the difference. A human checkpoint wherever judgement or accountability sits. And a pilot on real work before the whole team switches.

ALEX: I'd go further. If Claude can do the step, take the human out. A reviewer on every draft halves the time saved.

SAM: For some steps, yes. Nobody approves a brainstorm, and over-reviewing kills adoption.

ALEX: So where's the line?

SAM: Where the output carries a commitment, a decision about a person, or a figure someone will rely on. Those keep a checkpoint, and the saving comes from reviewing a draft instead of writing one. The tell is who receives the output: a customer, a regulator or an executive means the checkpoint stays.

ALEX: And the opposite habit? Redesigning everything because it sounds more strategic?

SAM: Also a trap. If the process works and one task eats the hours, a full redesign is overspend. Match the change to the problem.

ALEX: Drill.

SAM: Pause here and answer before we go on. A sales lead's team spends about three hours per account writing summaries before each quarterly business review. The reps say the rest of the review process works well. What is the best way to bring Claude in? A: redesign the whole review process around Claude before changing anything else. B: set up a Project with the summary template and guidance, have Claude draft each summary from the account notes, have the rep review and edit it, and compare the time spent with the current three hours. C: stop writing summaries, since Claude can answer questions live in the meeting. D: wait for a full integration with the sales system so summaries produce themselves. [pause]

ALEX: B. One slow step, so augment it, keep the rep's review, and measure against the three hours.

SAM: Right. A redesigns what the stem says works. C drops the preparation and puts unchecked answers in front of a client. D waits for integration the problem doesn't need. [sting]

## Communicating value and limits

ALEX: Last task. Explaining all this to the people who pay for it.

SAM: Value first, in their terms: hours saved, turnaround, consistency, fewer errors reaching the client, measured against the baseline. "Forty minutes instead of three hours" beats "Claude is very powerful".

ALEX: And the limits?

SAM: Plainly. Claude can be confidently wrong, including on figures and citations. It knows its training, plus what you give it or let it search. Its drafts are checked and owned by people. And some decisions stay with a person.

ALEX: If I open with hallucinations, the director cancels the pilot. Shouldn't the risks wait until they've seen the benefit?

SAM: Order matters, and a bare list of risks can scare a sponsor off a good idea.

ALEX: But?

SAM: A sponsor who finds the limits later feels misled. The exam's answer pairs each limit with the control that handles it: the review step, the source check, the human sign-off. The tell is a sponsor asking for a promise, "no errors" or "no more checking": answer with the value, the limit and the control together.

ALEX: Last drill.

SAM: Pause here and answer before we go on. A finance director asks whether Claude can prepare the month-end variance commentary automatically, so the team can stop checking it. What is the best response? A: yes, Claude is accurate enough that checking is no longer needed. B: no, A I should not be used anywhere near financial reporting. C: explain that Claude can draft the commentary and flag unusual movements, which saves time, while the team still checks the figures and signs off, and propose a pilot measuring time saved against the current process. D: tell the director to raise it with the I T team. [pause]

ALEX: C.

SAM: C. It sells the real value and keeps the control where the accountability sits. A overpromises, and the first wrong figure costs the project its credibility. B abandons the task. D passes on a business question. [sting]

## Cold open: the verdict

ALEX: Back to the cold open, then. I said A, draft the commentary every week. Let me defend it. Everyone on that team knows where the hours go.

SAM: Everyone thinks they know, and they are often right. That's why A is tempting.

ALEX: So why isn't it the answer?

SAM: Because nobody has measured. The hours might be in pulling figures from three spreadsheets, and the errors in the copying and pasting. C is the answer: map steps, times and error points, pick the step where Claude helps most, keep the manager's check, and pilot against the current report, so a baseline proves the gain. A jumps to a fix with no before and after. B redesigns the output before anyone knows the problem. D escalates something that needs no integration to start.

ALEX: And the tell?

SAM: The word "first". When an item asks what to do first, the answer understands the current process before changing it. [sting]

## Five to remember

ALEX: Five to remember. One: Claude extracts requirements, conflicts and gaps from messy notes; the people who own the process settle the conflicts.

SAM: Two: research mode for questions that need many sources and citations, and citations make checking possible, not optional. For process advice, give Claude the real steps, times and pain points.

ALEX: Three: build the prototype yourself, then escalate anything that connects to company systems, runs on its own or goes into production, to an Architect or Developer.

SAM: Four: augment one slow step when the process works; redesign when the pain is in handoffs and rework. Either way, a baseline first, a checkpoint where accountability sits, and a pilot.

ALEX: Five: sell value in measured business terms, and pair every limit with the control that handles it. Never promise "no checking".

## Recap: the exam tells

SAM: Your turn first. Pause and name the five tasks we covered, and the habit that wins each one. [pause]

ALEX: Requirements: surface conflicts, don't settle them. Research and process work: give Claude the real detail and check the sources. Design: prototype, then escalate. Augment or redesign: match the change to the pain, with a baseline. Stakeholders: value, limits and controls together.

SAM: Good. Now as exam tells. If a stem says the notes disagree, think flag the conflict and take it back to the owners.

ALEX: If it says "specific to our process", think give Claude the steps, times and handoffs, not an open question.

SAM: If an option filters claims by Claude's own confidence, think distractor, and check against the cited source instead.

ALEX: If you see "integrate with", "automatically" or "production" next to a company system, think prototype yourself, then escalate.

SAM: If the process works and one step eats the hours, think augment that step. Handoffs and rework, think redesign.

ALEX: If a sponsor wants a promise of no errors or no checking, think value, limit and control together.

SAM: And if the item asks what to do first, think map and measure the current process before changing it.

SAM: Next time, episode five: Projects, knowledge and connectors, and keeping a setup current once people depend on it.
