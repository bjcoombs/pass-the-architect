---
episode: 8
slug: dev-productivity
title: "Developer Productivity & Operational Enablement"
description: "The smallest domain, covered tight: shared Claude Code configuration and Skills distribution for teams, keeping engineering judgment in AI-assisted workflows, and turning operational symptoms into architecture causes."
domain: "Developer Productivity & Operational Enablement"
weight: "7%"
target_minutes: 14
---

## In this episode

SAM: Welcome to Pass the Architect. This is episode eight, Developer Productivity and Operational Enablement.

ALEX: The smallest domain. What do I get from it?

SAM: By the end you'll be able to set up a shared Claude Code baseline and tell guidance from enforcement. You'll pick the right way to get a Skill to a team, and roll it out through champions inside a spend posture. You'll keep engineering judgment in an AI-assisted workflow with a four-part checklist. And you'll turn an operational symptom into its architecture cause, then leave the team a runbook.

ALEX: Seven percent, so four or five items, but they are quick marks once the mechanism is clear. The trap it fixes is choosing by reach, or by a bigger model, when the stem is really asking about governance or diagnosis.

SAM: Which is what today's opener tests.

ALEX: Go on, then. [sting]

## Cold open: the shared procedure

SAM: A hospital group's platform team wrote a procedure that checks code changes for patient data leaking into logs. Six product teams must run it the same way. Last month a shared prompt edit gave every team bad output for a week before anyone could undo it. How should the procedure reach the teams? Option A, upload it as an org-provisioned Skill under Organization settings. Option B, bundle it into a plugin assigned to all six teams' groups, with version-controlled updates from a connected repository and a named owner. Option C, copy it as a project Skill into each team's repository. Option D, add a paragraph describing it to each team's CLAUDE dot md file.

ALEX: Everyone needs it, so A. Org-wide reach in one upload.

SAM: Hold that. We come back to it at the end.

ALEX: Domain seven. Seven percent, the smallest.

SAM: Four or five items out of sixty-three. Three task statements: configure Claude tools for teams, improve developer workflows with AI tooling, and support debugging and operational issues. The system is built; now the team must adopt it and run it without you.

SAM: Segment one, team setup. For a team, the unit is a shared configuration: one baseline everyone starts from. In Claude Code that means a project CLAUDE dot md, an agreed set of tools and M C P servers, and a permission posture, all in the repository, reviewed and versioned once for everyone.

ALEX: Rather than forty engineers each tuning their own? My teams work in different stacks. Let each one pick its own setup. A forced baseline slows down the people who know what they need.

SAM: Part of that holds. Conventions do differ by team, and a project Skill in that team's repo is built for exactly that.

ALEX: So why not stop there?

SAM: Because personal setups drift apart and cost far more to reconcile later, and nothing gets reviewed once for everyone. Team conventions sit on top of the shared baseline; they do not replace it.

SAM: The tell: when an item says "consistent", "the same way" or "across teams", pick the shared baseline in the repository. An option built on personal preference is the drift.

ALEX: And inside that baseline, what actually binds?

SAM: CLAUDE dot md is guidance. The model usually follows it, but it enforces nothing. Permission rules and hooks are the deterministic layer. If an item says engineers must never touch production config, the answer is permissions or managed settings, not a sentence in CLAUDE dot md.

ALEX: Managed settings being the admin layer.

SAM: They sit at the top of the precedence order and a developer cannot override them. Note that server-managed settings are a settings channel, not a way to distribute Skills.

ALEX: Then how do Skills reach a team?

SAM: Four mechanisms, and the exam tests the governing factor. An org-provisioned Skill reaches everyone at once. But there is no version pinning and no native rollback; an update is a manual re-upload. A plugin bundles Skills and is assigned to groups or org-wide, with install preferences such as required or available, and version-controlled updates from a connected repository. A Claude Code project Skill lives in the repo and versions with it: one team's conventions. An API Skill is called by the organisation's own products, machine to machine, with explicit version pinning.

ALEX: So two questions. Who needs to reach it, and who must be able to update or revoke it.

SAM: Those two. Then rollout: not an all-hands switch-on. Enable a champion per department first. They prove a real workflow, absorb early friction, become first-line support, and seed adoption in batches. And set the spend posture before the first bill: model defaults, model allowlists, effort guidance, and spend, rate and per-user caps.

ALEX: The tempting wrong answer being "give everyone the best model so they adopt it."

SAM: It ignores spend posture and does nothing for adoption. Unmanaged model choice routes work to a pricier tier, multiplied across every person and request. Same rule as Domain two: match the tier to the task. [sting]

## Segment two: developer workflows

SAM: Segment two, developer workflows. AI tooling pays off inside the workflow that already exists: the editor, the review process, the test loop. Encode conventions into Skills and project configuration, and good practice travels with the tooling.

ALEX: Failure modes?

SAM: Two named ones. Lumpy adoption: a few heavy users, the rest barely touch it, so the practice never standardises. Champions and batches fix that. And stalling at basic chat: Claude as a question box, never reaching tool use, repository-aware assistance or packaged Skills, because nobody enabled them. Access is not adoption.

ALEX: And keeping engineering judgment in the loop?

SAM: The course word is diligence, one of the four AI Fluency competencies: taking responsibility for verifying and vouching for what you use or share. Its deliverable is a verification checklist that AI-generated code must pass before production. Four dimensions. Correctness: tests exist and pass, behaviour matches the requirement, edge cases included. Security: no secrets in code, inputs validated, least-privilege access for tools and external calls. Maintainability: reads clearly, follows conventions, no unexplained complexity. Human understanding: the person submitting can explain what it does and why, including inputs it was never tested against.

ALEX: The fourth is the one people skip.

SAM: And the one the exam leans on. Green tests are not understanding. If the author cannot explain a change, hold it. The failure is judgment erosion: shipping output that looks right and passes shallow checks until an input nobody reasoned about reaches production. Automate what you can, with tests and eval sets as gates on every change, and keep human review before edits are committed.

ALEX: Let me argue the other side. If the tests pass, ship it. Tests are the spec written down, "can the author explain it" is a judgment call, and the review queue is already the bottleneck.

SAM: Tests are the strongest gate you can automate, and the checklist says automate what you can. No argument there.

SAM: But tests cover only what someone thought to test. The understanding dimension exists for the inputs nobody tested against, which is exactly where judgment erosion ships.

SAM: The tell: if the stem says the author could not explain the change, more automation is the wrong layer. Pick the understanding gate.

ALEX: Distractors?

SAM: A linter catches known patterns but cannot make the author understand what shipped. A review rule that exempts small AI changes is the gap, not the fix. A newer model does not replace reviewer discipline. Compensating controls dressed as fixes. [sting]

## Segment three: debugging support

SAM: Segment three, debugging and operational support. The team brings you a symptom. Your job is translation: connect it to an architecture cause. Four pairings to know cold. Gradual quality decline, no code change: a model or prompt change, or retrieval drift as the corpus grew. Compare against an eval set. Latency spike: context grew, a tool got slow, or the cache stopped hitting. Use traces to find the slowest span. Intermittent tool failures: authorization, rate limits, or an unhandled error path. Trace one failed call end to end. Cost up with flat usage: the model tier crept up or caching regressed. Check per-request tier and cache hit rate.

ALEX: And the trap for quality drift is a bigger model.

SAM: A bigger model does not fix an index that fell behind its corpus. Turning off caching to cure "stale content" fails too: exact-match caching only hits on identical prompt segments, so it cannot serve changed content. And rolling back the last deploy does nothing when the scenario says no code changed. Diagnose the component the trigger touched.

ALEX: How do you run the diagnosis itself?

SAM: Write down the reporter's own words. Name three hypotheses before looking at evidence. Gather the system prompt, the tool descriptions and the execution traces. Evidence must point at a specific line, and the fix is scoped: which artifact, which line, what change.

SAM: Fixing the incident yourself is firefighting. Lasting support is a runbook of symptom, cause and action, plus an escalation path naming who handles what and when an issue leaves the team. When you mentor, surface evidence and ask questions rather than hand over the answer. The goal: a team that needs you only for new problems.

SAM: Pause here and answer before we go on. A retail bank's internal coding assistant has slowed noticeably over three weeks. Nothing was deployed; the team recently pointed it at a much larger document set. What should the architect do first? A, switch to a smaller, faster model. B, use request traces to find the slowest span, checking tokens per request, the slowest tool call and cache behaviour. C, raise client timeouts so requests stop failing. D, roll back to the previous release and re-run integration tests. [pause]

ALEX: A. It's slow, so make it faster. A smaller model is the first thing I'd try on a live system.

SAM: It might even help. But nothing has been diagnosed yet. That is miss pattern one, instinct over the stem, and the distractor is scale instead of structure: turn the model dial, ignore the cause.

ALEX: So B.

SAM: B. Latency maps to context growth, a slow tool or a cache miss, and the larger document set points at context. A guesses a cause before any diagnosis. C hides the symptom. D has nothing to act on; no code changed. When the stem says "first" and nobody has diagnosed anything, pick the option that gathers evidence.

SAM: Pause here and answer before we go on. Choose two. A field-service company gave three hundred engineers Claude Code two months ago. Usage sits with a handful of people, and last week a generated change merged that its author could not explain. Which two actions address the root causes? A, name a champion in each team who converts a real workflow, then seeds adoption in batches. B, adopt a verification checklist covering correctness, security, maintainability and human understanding, with tests and evals automating what they can. C, exempt changes under fifty lines from security review to keep queues moving. D, default every session to the most capable model so first impressions are strong. E, let each engineer build their own configuration to suit personal style. [pause]

ALEX: A and B.

SAM: Both right. A fixes lumpy adoption; B adds the missing understanding gate. C widens the gap that let the bad change through. D ignores spend posture. E is the drift a shared baseline prevents. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Alex, you picked A.

ALEX: I'll defend it. A shared Skill is fine. Everyone gets it, and if an update goes bad I re-upload the old file. Why a plugin?

SAM: Re-uploading does get you back eventually. But it is manual, with no version pinning and no native rollback, and the stem says last month's bad edit ran for a week before anyone could undo it.

ALEX: So A reaches everyone but repeats last month.

SAM: It does. So, B. A plugin gives group targeting, versioned updates from a repository, a path back, and a named owner. C scatters six copies with no single place to update or revoke. D is advisory text, not a governed procedure.

SAM: The tell: "could not undo it" plus "a named owner" means governance decides, and governance means a plugin.

ALEX: So the deciding factor was the need for governance, not the size of the audience. A plugin can go org-wide. Org-provisioned Skills are a trap, then.

SAM: Too far. If an item needs only reach and says nothing about updating or revoking, the org-provisioned Skill is the simple answer. Do not import a rollback requirement the stem never stated. [sting]

## Five to remember

SAM: Five to remember. One: team setup is a shared baseline in the repo, CLAUDE dot md, tools and M C P servers, permissions. CLAUDE dot md guides; permissions, hooks and managed settings enforce.

ALEX: Two: choose the Skills mechanism by who needs it and who must update or revoke it. Central versioning and rollback for a human-facing procedure means a plugin.

SAM: Three: roll out through a champion per team, then batches, inside a spend posture. Access is not adoption.

ALEX: Four: green tests are not understanding. The checklist has four dimensions, and if the author cannot explain it, it does not merge.

SAM: Five: translate symptom to cause, diagnose what the trigger touched, and leave a runbook and an escalation path behind.

## Recap: the exam tells

SAM: Before the recap, pause and name the three task statements from today, and one mechanism that belongs to each. [pause]

ALEX: Configuring tools for teams, with a plugin for governed Skills. Improving developer workflows, with the verification checklist. And debugging and operational support, with a runbook and an escalation path.

SAM: Good. Now as exam tells. If a question says consistent, the same way, or across teams, think shared baseline in the repository.

ALEX: If it says engineers must never do something, think permissions, hooks or managed settings, not a sentence in CLAUDE dot md.

SAM: If it says a bad update could not be undone, or asks for a named owner, think plugin with versioned updates. If it needs only reach, the org-provisioned Skill is enough.

ALEX: If usage sits with a handful of people, think lumpy adoption, fixed by a champion per team seeding batches.

SAM: If the author could not explain the change, think understanding gate, not more automation.

ALEX: If quality slips with no code change, think model, prompt or retrieval drift, checked against an eval set. If latency climbs, think traces and the slowest span. If cost rises on flat usage, think model tier and cache hit rate.

SAM: And if the stem says first and nothing has been diagnosed, pick the option that gathers evidence.

ALEX: Next time, your five miss patterns, then closing the Foundations gaps, and after those, the final drill.
