---
episode: "K06"
series: "FIELD"
slug: coding-agents
title: "Coding agents: Claude Code and the field"
description: "Codex, GitHub Copilot, Antigravity, Kiro, Cursor and the open-source agents against Claude Code: what has converged on shared standards like AGENTS dot md, skills and M C P, what still differs, and how to read the adoption numbers."
domain: "Coding agents"
weight: ""
target_minutes: 20
---

## In this episode

SAM: Welcome to Know the Field, from Pass the Architect. This is episode six: coding agents, Claude Code and the field.

ALEX: The layer I know best. What will I be able to do by the end?

SAM: Name what every serious coding agent now shares, and the open standards that carry it: AGENTS dot md, skills, hooks, subagents and M C P. Say where OpenAI's Codex beats Claude Code, and where it does not. Place the agents the platform vendors ship: GitHub Copilot, Google's Antigravity, and Kiro from A W S. Read the adoption numbers without being fooled by them. And know when the honest advice is someone else's tool.

ALEX: Which matters, because "why not just use Cursor?" is a question I get every week.

SAM: Then we start there. [sting]

## Cold open: the new owner

SAM: A payments company has four hundred developers on Cursor, and they like it. Its vendor-risk team has just noticed that Cursor changed owner in August, and asks what to do. Option A, move everyone to Claude Code now, before the next audit. Option B, keep Cursor for now, re-run due diligence on where code and prompts are routed, the sub-processors and the default models, and keep instructions in AGENTS dot md so a later switch stays cheap. Option C, do nothing, because a change of owner does not change the product. Option D, move everyone to Roo Code, because an open-source tool has no owner to change.

ALEX: A. A clean break, and the developers get the first-party harness.

SAM: Hold that. We come back to it at the end.

ALEX: Which of the six layers are we in today?

SAM: The coding agent, layer four. But it drags in two more: the model inside the agent, and the route to market, because several of these agents now bill through the customer's existing cloud. [sting]

## Segment one: the convergence

SAM: Segment one. Put Claude Code, Codex, Copilot and Antigravity side by side and the shape is the same. A project instruction file. Layered settings for user, project and administrator. Skills. Hooks at fixed points in the loop. Subagents defined as files. Plugins that bundle the lot. And M C P for tools.

ALEX: Most of which Claude Code shipped first. They copied the homework.

SAM: Some of it started at Anthropic and some did not. The AGENTS dot md file came from OpenAI, and since September Claude Code reads it when a repository has no CLAUDE dot md. Ideas are moving in both directions. Call it convergence, because a customer who has used Codex will hear "copying" as sour grapes.

ALEX: Fair. Who governs the shared pieces?

SAM: A neutral home: the Agentic A I Foundation, a Linux Foundation fund launched in December twenty twenty-five. Its founding projects were M C P from Anthropic, AGENTS dot md from OpenAI, and goose from Block. A W S, Google, Microsoft and OpenAI sit at the top membership tier beside Anthropic.

ALEX: And skills?

SAM: Anthropic published the skill format, a folder with a SKILL dot md file, as an open standard in December twenty twenty-five. It was reportedly handed to the same foundation in October. Codex, Copilot, Cursor and Antigravity are among the tools reported to support it.

ALEX: So what does a customer actually get from all this?

SAM: Portable content, not portable configuration. Instruction files and skills now move between tools. Hooks do not, quite. Codex uses near-identical event names, pre tool use, post tool use, stop, but its own config files, and it runs only shell commands and M C P tool calls as handlers. Claude Code also accepts prompt and agent handlers.

SAM: The question to ask the customer: how many coding agents do your teams run today, and where do their instructions live?

SAM: Pause here and answer before we go on. For each statement, say true or false. One: Claude Code reads an AGENTS dot md file when a repository has no CLAUDE dot md. Two: M C P is still governed by Anthropic alone. Three: the SKILL dot md format is supported by Codex, Copilot and Antigravity, though folder locations can differ between tools. Four: hooks written for Claude Code run unchanged in Codex. [pause]

ALEX: True, false, true. And true for four, because the event names match.

SAM: Three out of four. Four is false. The names match, but the config files differ, and Codex skips any handler that is not a shell command or an M C P call. Port the logic, not the file. [sting]

## Segment two: Codex

SAM: Segment two, OpenAI's Codex, the closest rival. It runs as a mode in the ChatGPT desktop app, as a command-line tool, an I D E extension and a cloud service, with GitHub, Slack and Linear integrations, an S D K and a GitHub Action.

ALEX: And it ships all the way down to ChatGPT's free tier.

SAM: A reach Claude Code does not match. Two more things Codex does better. The command-line client is open source, Apache two point oh, written in Rust, and among the most-starred repositories in the category. And the sandbox is the default boundary. Out of the box Codex writes in the workspace and nowhere else, enforced by the operating system on Mac, Linux and Windows, with approvals layered on top.

ALEX: Claude Code has an operating-system sandbox too, and permission modes. The Codex default is mostly friction.

SAM: Claude Code has both, so the gap is smaller than it sounds. But defaults are what a security team signs off. Codex subagents also inherit the parent's sandbox and cannot loosen it. For a regulated customer, "safe unless someone opens it" reads better than "safe once someone configures it". Give Codex that one.

ALEX: Noted. And the cloud route?

SAM: Codex has been generally available on Amazon Bedrock since June, so its spend can sit on an A W S commitment. The old line that only Claude runs on the customer's own cloud is gone.

ALEX: So where does Claude Code stay ahead?

SAM: Two places, with sources. Harness depth: the handler limit we just named is in OpenAI's own Codex documentation. And independent boards, the Artificial Analysis index and the Arena agent board, currently put Claude models on top. Those are independent runners, and ranks move. OpenAI's own Terminal-Bench claims put its model ahead, but that is vendor-reported, and against an older Claude.

SAM: The question for the customer: does your security team need the sandbox on by default, or the client's source code in hand?

SAM: Pause here and answer before we go on. A defence contractor's security team will approve a coding agent only if they can audit and build the client from source. The spend must draw down the company's A W S commitment, and the developers are content with OpenAI models. What fits? A, Claude Code through Amazon Bedrock. B, Codex pointed at Amazon Bedrock. C, Gemini C L I, which is also open source. D, Claude Code with a locked-down managed settings file. [pause]

ALEX: A. Bedrock covers the commitment, and Claude leads the independent boards.

SAM: That answers the question you prefer, not the one asked. The constraint is an auditable client. Claude Code is not open source, so A and D both fail, and managed settings constrain behaviour, not auditability. C is open source, but it now serves Google's paid tiers and keys, not an A W S bill. B meets both constraints. The answer is B.

ALEX: Loyalty to the model, not fit to the customer.

SAM: That is the miss. [sting]

## Segment three: the platform vendors' agents

SAM: Segment three, the agents the platform vendors ship. Start with GitHub Copilot.

ALEX: Autocomplete with a chat window.

SAM: That picture is years out of date. Copilot now hosts other vendors' agents. Through what GitHub calls Agent H Q, the Claude and Codex coding agents reached public preview in February, beside GitHub's own, under an agent control plane that is generally available. It offers Claude, G P T and Grok models. Its code review gained skills and M C P in July. And it reportedly has around fifty million users, counting the free tier.

ALEX: Then what does it do better than Claude Code?

SAM: Two things. Governance and distribution: the customer already has the seats, the identity set-up and the audit trail in GitHub. And choice: one bill, many models, several agents. Since June, billing is usage-based, credits metered on tokens at each model's A P I rate, with completions still free.

ALEX: And where Claude Code wins?

SAM: Copilot resells Claude; Claude Code is the first-party harness, with the full set of skills, hooks, subagents and plugins, and new features the day they ship. Check the data terms too. According to GitHub's model documentation, Anthropic retains data by default for the Fable models in Copilot, with zero data retention only under a time-bound exemption. A direct contract may read differently.

SAM: Now Google. Ask a customer about Google's coding agent and you may hear Gemini C L I. That is out of date. In May, Google moved individual users from Gemini C L I to the Antigravity C L I and cut off the personal tier in June. Gemini C L I stays open source, but only for paid Code Assist tiers and paid keys. And Jules went read-only on the eleventh of November, and shuts at the end of December.

ALEX: That is the case against Google in one sentence. They keep killing the tool.

SAM: The churn is real, and worth naming to a customer. But do not stop there. Antigravity is now Google's single harness: a desktop app with parallel agents and scheduled background tasks, the C L I, and an S D K. It reads AGENTS dot md and the skill format, and bundles skills, subagents, hooks and M C P into plugins. And on paid plans it offers Claude Opus and Sonnet beside Gemini.

ALEX: Claude inside Google's own tool.

SAM: Which is one of Google's two real strengths here: model choice inside one harness, Claude included. The other is Gemini's cost per task, which on independent indexes sits well below Claude's top models. The weaknesses: the Antigravity C L I is closed source, users have reported quota complaints, and the churn.

SAM: Last, A W S. Amazon Q Developer is being retired. New sign-ups closed in May, and its I D E plugins and paid subscriptions reach end of support on the thirtieth of April twenty twenty-seven. Claude models from Opus four point seven onward are already Kiro-only. Kiro is the successor: an I D E and a C L I built around spec-driven development.

ALEX: Spec-driven is plan mode with a nicer name.

SAM: Close, but not the same. Kiro makes the specification the centre of the product, not a step before the work. For a team that wants the spec kept as an artefact, that is an honest fit. And it is A W S's own product, with a GovCloud option.

SAM: The question for the customer: which of these vendors do you already pay, and is the tool you use being retired?

SAM: Pause here and answer before we go on. Choose two. A logistics company has six hundred developers on Amazon Q Developer Pro in their I D Es, and they want newer Claude models than Q Developer offers. Which two pieces of advice are right? A, plan the move now: Q Developer's I D E plugins reach end of support on the thirtieth of April twenty twenty-seven. B, buy more Q Developer seats for a team joining next quarter. C, evaluate Kiro, the A W S successor, which carries the newer Claude models. D, stay on Q Developer and wait for the newer Claude models to arrive there. E, move the developers to personal Gemini C L I accounts. [pause]

ALEX: A and C. B fails because sign-ups closed in May. D, because the newer models are Kiro-only. E, because the personal tier is gone.

SAM: A and C. And notice the right answer is A W S's own tool. If a team prefers Claude Code, it can run against Claude on Bedrock and the same commitment, but that is a second evaluation, not a reason to skip the first. [sting]

## Segment four: the independents and the adoption data

SAM: Segment four, the independents. Cursor rebuilt itself as agent-first with Cursor three in April, and trains its own Composer models. Menlo reports that Composer two was built on Kimi K two point five, an open-weight model from Moonshot. And in August, SpaceX closed its purchase of Cursor.

ALEX: Cursor is a V S Code fork that resells Claude.

SAM: Less so every quarter. It builds its own models and offers other labs' models beside them, and it is a strong product. The question it raises now is ownership, not quality. Cursor sits in the same corporate group as Grok. Ask where code and prompts are routed, and what the model defaults are, since the acquisition.

SAM: Cognition sells Devin and Windsurf, and its Devin desktop app is reportedly built on Windsurf. On the open-source side, Cline and Kilo Code carry on; Roo Code reportedly shut down in the spring. Many of these run on cheap open-weight models through routers, which is where episode five's licence questions come back.

ALEX: Now the numbers. Who is winning?

SAM: Three sources, three caveats. As of November twenty twenty-six, Stack Overflow's survey of more than thirty thousand developers has Claude Code as the most-used coding agent, at sixty-six percent of A I users, with GitHub Copilot at fifty-nine. That is independent, and it measures use, not spend. Many developers use both.

ALEX: Sixty-six to fifty-nine. That settles it.

SAM: It is the strongest independent signal for Claude Code, so use it. But a year earlier the same survey had Cursor ahead of Claude Code, so this moves fast. And seven points is not a rout when Copilot comes with the GitHub contract.

SAM: Second, Menlo Ventures' enterprise report. Menlo is an Anthropic investor, and says so. It puts Claude Code and Codex together at about seventy percent of coding application spend, but it does not split the two, and it rests on a survey of about four hundred U S enterprises.

SAM: Third, vendor counts. OpenAI says Codex has more than five million weekly users; a reported April figure put it near four million weekly developers. Copilot's reported user count includes the free tier. Treat each as the vendor's own number.

ALEX: So what do customers actually adopt?

SAM: More than one tool. The same survey says twenty-seven percent of organisations already use different models for different work. That is why the shared standards matter: instruction files and skills survive a change of tool.

SAM: Pause here and answer before we go on. A C I O cites the Menlo figure, Claude Code and Codex at about seventy percent of coding spend, and wants to standardise on Claude Code on that basis alone. What is the best response? A, agree: the report settles it. B, point out that the figure does not separate Claude Code from Codex, that Menlo is an Anthropic investor, and that a pilot on the company's own repositories is the better basis. C, dismiss the report as investor marketing. D, use Open Router's token rankings instead, since they are measured rather than surveyed. [pause]

ALEX: B. Though A tempted me, because it helps us.

SAM: B. A leans on a number that cannot choose between the two products. C throws away real evidence along with its bias. D is measured, but Open Router traffic skews to cost-sensitive developers on cheap models, not enterprise spend. [sting]

## Cold open: the verdict

SAM: Back to the payments company. Alex, you picked A, move everyone to Claude Code.

ALEX: And nothing in the scenario said Cursor had failed. The risk team asked a question, and I answered it with a migration.

SAM: The answer is B. A change of owner is a reason for due diligence, not a verdict: check data routing, sub-processors and model defaults, then decide. A spends four hundred developers' goodwill before anyone has an answer. C skips the question a risk team is right to ask. D fails twice: Roo Code reportedly shut down this spring, and an open-source client still sends code to whichever model it calls.

ALEX: And if the review comes back badly?

SAM: Then the AGENTS dot md file pays off. Codex, Copilot and Cursor read it natively, and Claude Code reads it when there is no CLAUDE dot md, so the instructions move with the team. That is the moment to pilot Claude Code against the alternatives on their own repositories. [sting]

## Five to remember

SAM: Five to remember. One: coding agents have converged. Instruction file, skills, hooks, subagents, plugins and M C P are now the common shape.

ALEX: Two: M C P and AGENTS dot md sit in the Agentic A I Foundation, and skills reportedly joined them. Content moves between tools; hook configuration does not.

SAM: Three: Codex is stronger on a sandbox by default, an open-source client, and reach down to ChatGPT's free tier. Claude Code is stronger on harness depth and on independent agentic rankings.

ALEX: Four: Copilot sells governance, seats and model choice, and hosts the Claude agent. Google moved from Gemini C L I to Antigravity, and A W S from Q Developer to Kiro.

SAM: Five: read adoption numbers by what they measure. Stack Overflow measures use, Menlo surveys spend and is an Anthropic investor, and vendor counts are the vendor's.

## Recap: conversation tells

SAM: Recall first. Pause and name the four segments, and the customer question each one hands you. [pause]

ALEX: The convergence, Codex, the platform vendors' agents, and the independents with the data. Where do your instructions live; do you need the sandbox on by default or the source; which vendor do you already pay, and is your tool retiring; and what does this number measure.

SAM: Now as conversation tells. If a customer says "we run three agents and the instructions drift", ask whether one AGENTS dot md can carry them.

ALEX: If security says "we need an auditable client", ask whether Codex fits better, and say so out loud.

SAM: If they say "we're all on GitHub", ask what Copilot already governs before you sell seats. If they say "we use Gemini C L I", ask which tier, because Antigravity replaced it for most users.

ALEX: If they say "we're on Q Developer", ask about their plan for April twenty twenty-seven. If they say "we standardised on Cursor", ask where it routes data under its new owner.

SAM: And if they quote a market share, ask who measured it, and whether it splits the products.

ALEX: Next, episode seven: the objections drill.
