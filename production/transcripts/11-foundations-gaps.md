---
episode: 11
slug: foundations-gaps
title: "Closing the Foundations Gaps"
description: "A bonus episode on the applied configuration and API mechanics that both Architect exams test inside their scenarios: enforcement versus guidance, settings and M C P scope, tool sequencing, the agentic loop, extraction schemas, review routing and feedback loops."
domain: "Cross-domain (Domains 2, 3, 4, 5, 7)"
weight: "applied mechanics"
target_minutes: 25
---

## In this episode

SAM: Welcome to Pass the Architect. This one is Closing the Foundations Gaps.

ALEX: Where does it take me?

SAM: By the end you'll be able to tell guidance from enforcement and pick the hook or permission that guarantees a rule. Put an M C P server at the right scope without committing a secret. Write tool descriptions and structured errors the model can act on, and enforce tool order in code. Run the agentic loop on stop reasons and resend the history. Design extraction schemas that give missing data a legal value, route review where it is needed, and feed corrections back. And refine and resume sessions without wasting work.

ALEX: For the exam, this is the mechanics layer. You won't be asked to define a hook; you'll get a symptom inside a scenario, and the trap is fixing it with louder wording or a bigger model.

SAM: Like a refund that sometimes comes before the lookup.

ALEX: Let's hear it. [sting]

## Cold open: refund before lookup

SAM: A bank's support agent can look up customers and issue refunds. The system prompt says to look up the customer first. In about one conversation in a hundred, it issues the refund before any lookup. What fixes it? Option A, rewrite the instruction in capitals and add three few-shot examples showing the lookup first. Option B, make the refund tool reject any call that does not carry a customer ID returned by a successful lookup in this session, and return an error telling the model to look the customer up. Option C, remove the refund tool and send every refund to a human. Option D, move to a larger model that follows instructions more reliably.

ALEX: A. Few-shot examples are the strongest lever on behaviour I know.

SAM: Hold that. It comes back at the end.

ALEX: Why a bonus episode?

SAM: Because Foundations marks leaked on mechanics, not principles. Foundations tests that layer directly, and Professional assumes it and tests it inside its own domains: tool configuration in Integration, schemas and review gates in Evaluation and Governance, team setup in Developer Productivity. You will not get "what is a hook". You will get "formatting keeps drifting, what do you change". So every segment today starts with a symptom.

SAM: Segment one. Symptom: a field-service company's repository has a line in its CLAUDE dot md saying "always run the formatter after editing". Code review keeps finding unformatted files. What is wrong?

ALEX: My instinct is the wording. Make it "you must run the formatter after every edit", put it at the top, and the drift mostly stops. That worked on my last team.

SAM: It probably did help. Clear, firm instructions raise compliance, and for conventions and style they are the right tool.

ALEX: But?

SAM: But "keeps finding" tells you mostly is not enough. Louder guidance is still guidance: the model follows it most of the time, not every time. CLAUDE dot md guides. Permissions, hooks and managed settings enforce.

ALEX: So what is the tell?

SAM: "Always", "every time", "keeps happening". When the stem needs it every time, an answer that only rewords CLAUDE dot md is a probabilistic fix for a deterministic need.

SAM: A hook is deterministic code that fires on a defined event, a rule the model cannot skip. The prep course files hooks under "guarantee". For "after every edit", the event is PostToolUse: it runs after a tool call completes. Match it to the file-edit tools and have it run the formatter, the linter, or the affected tests.

ALEX: And it goes in the project settings so everyone gets it.

SAM: Yes. The distractors: louder wording in CLAUDE dot md, which is still guidance; a CI check that rejects the pull request, which is deterministic but catches the drift after the fact instead of preventing it; and "remind the model in every prompt". The exam's rule is the smallest mechanism that guarantees the outcome at the point it happens.

ALEX: I'd push on the CI one. We already gate every pull request in CI. It is deterministic, it lives in one place, and nothing unformatted merges. Why add a hook?

SAM: On "deterministic" you are right. CI is not guidance, and that makes it the strongest distractor of the three.

SAM: The difference is when it fires. CI rejects the pull request after the drift has happened, so it detects the problem instead of preventing it. The hook stops it at the edit.

ALEX: So the tell is timing.

SAM: The tell is "after every edit". When the stem names the moment, the answer acts at that moment, and a later check is a detective control dressed as a fix.

ALEX: What about "never touch the migrations folder"?

SAM: A permission deny rule. That blocks the action itself. If the pattern match is not precise enough, say you need to inspect a full shell command with its flags, a PreToolUse hook reads the call before it runs and can block it. And if the rule must hold across the whole organisation, managed settings sit at the top of the precedence order and no developer can override them. Interleave this with Governance: the course puts tool-call authorization in deterministic checks because it has to be auditable.

ALEX: So guidance for conventions and style, enforcement for anything that must happen every time. [sting]

## Segment two: configuration scope

SAM: Segment two, scope. Symptom: a new hire clones the repo and the team's issue-tracker M C P server is not there. Everyone else has it.

ALEX: Someone configured it at user scope, on their own machine, so it never reached the repo.

SAM: Right. Two scopes to hold apart. Project scope is shared and version-controlled: the project settings file in the repo's dot claude folder, and a dot M C P dot json file checked into the project for M C P servers. User scope is personal: it follows you across every project and nobody else sees it. There is also a local settings file for your personal overrides inside one project, kept out of version control.

ALEX: Precedence?

SAM: Managed first, then command-line arguments, then local, then project, then user. User is the lowest; it applies only when nothing else sets the value. One nuance: permission allow and deny lists accumulate across sources, and a deny wins over an allow.

ALEX: The server needs a token, though. The repo is private. Put the API key in the shared config and it works on clone, with no setup step for the new hire.

SAM: The convenience is real, and a private repo does narrow who can see it.

SAM: But a credential committed to version control is a Governance failure on top of a config one, and you do not need it. The shared config names the server and references the secret through a dollar-brace placeholder for an environment variable. Each developer sets their own token in their environment. The config is shared; the credential is not.

ALEX: And the exam will not care that the repo was private.

SAM: The stem rarely says it is, and supplying that yourself is importing a constraint. The tell is an option with "committed" next to "token" or "key": strike it out before you read further.

ALEX: And the reverse case? I want to try an experimental server without pushing it on the team.

SAM: User scope, or local. The test the exam uses is who needs it. Everyone on this repository: project. Only you, everywhere: user. Only you, here: local. A distractor that puts a personal experiment in the shared file, or a team dependency in someone's personal config, fails the same test from opposite ends.

ALEX: And if the server is connected but Claude never uses it?

SAM: Tool discovery. Check the server is actually connected, the slash M C P command shows it, and then read the tool descriptions. The model picks tools from their descriptions. A connected server with vague descriptions is invisible in practice.

SAM: Pause here and answer before we go on. A healthcare software team of eight wants every developer to use the same code-hosting M C P server. Each developer has a personal access token. Today two developers have it configured; the rest do not. What should the architect do? A, add the server to the project's dot M C P dot json with the token committed, so it works on clone. B, add the server to the project's dot M C P dot json, referencing each developer's token through an environment-variable placeholder. C, ask each developer to add the server at user scope on their own machine. D, describe the server and its setup steps in CLAUDE dot md. [pause]

ALEX: B.

SAM: B. Shared, versioned, no secret in the repo. A leaks a credential into version control, a Governance failure on top of a config one. C is how the team got here: eight personal setups that drift. D is guidance about configuration, not configuration. [sting]

## Segment three: tool descriptions

SAM: Segment three, tools. Symptom: a retail agent has two tools, one that looks up an order and one that looks up a customer. Asked "where is my order", it often calls the customer tool. Diagnosis?

ALEX: The descriptions overlap. The model cannot tell them apart.

SAM: So the fix lives in the descriptions. Say what each tool does and when to use it rather than the other one. Give the input format, for example "an order number starting with O R D, not an email address", and a short example call. If two tools genuinely overlap, rename or merge them. The distractors are a routing classifier in front of the model, which is over-engineering, and a system-prompt paragraph, which is guidance about a problem the descriptions should solve at source.

ALEX: Where do structured errors come in?

SAM: Symptom: the agent tells a customer "you have no orders" when the order database was down. The tool returned an empty list on failure. The model cannot tell "nothing found" from "could not look". Return failures as a tool result flagged as an error, with a category such as transient, validation or permission, whether a retry makes sense, and a message the model can act on. A valid empty result stays a success. Generic "operation failed" strings lose because the model cannot choose between retrying, asking the user, or escalating.

SAM: Pause here and answer before we go on. A utility company's field-service agent calls an M C P tool to book engineer visits. When the scheduling system times out, the tool returns the text "request failed", and the agent either gives up or retries a booking the customer's plan does not allow, again and again. What is the best change? A, return errors as results flagged as errors, with a category, whether a retry is appropriate, and a short explanation the agent can act on. B, have the tool retry silently up to ten times before returning anything. C, add a system-prompt instruction telling the agent never to retry. D, return an empty result on any failure so the agent moves on. [pause]

ALEX: B. Timeouts are transient, so retry them inside the tool. I would ship that: the agent never even sees the blip.

SAM: Half of that is right. A timeout is worth a retry. Now read B again.

ALEX: [sighs] Silently, ten times, on any failure. Including the booking the plan does not allow.

SAM: That is miss pattern two: one correct clause welded to a wrong one. The answer is A, because the agent cannot tell a timeout from a policy refusal unless the error says which. A timeout is transient and worth a retry; a plan restriction is a business rule and never is. B hides the failure and still retries the unretryable one. C overcorrects, so the transient failure that one retry would fix now goes unfixed. D is the worst of them: an empty result reads as success.

ALEX: Now the cold open. Sequencing.

SAM: First the parameter. Tool choice has four settings: auto, the default, where the model decides; any, which forces some tool call; tool, which forces one named tool; and none, which stops tool calls. Forcing guarantees a call happens. It does not guarantee the arguments are valid; strict tool use does that. And it forces one call on one turn. It does not enforce an order across a conversation.

ALEX: So I could force the lookup on the first turn.

SAM: You could, and it helps. But when the order matters, as in money moving, the guarantee belongs in code: the refund handler checks for a verified customer ID from a successful lookup, or a PreToolUse hook blocks the call, and either way returns an error that tells the model what to do first. Order that must hold lives in your code. [sting]

## Segment four: the agentic loop

SAM: Segment four, the loop itself. Symptom: an agent stops mid-task with half an answer. The loop code says "if the response isn't end turn, treat it as a tool call". What broke?

ALEX: It hit max tokens. There was no tool call to run.

SAM: Yes. The loop continues while the stop reason is tool use: run the tools, send the results back, call again. End turn means done. Max tokens means truncated, so continue or raise the limit; do not treat it as a tool call. A refusal stop reason means the classifiers intervened and needs its own route. With server-side tools such as web search, pause turn also means continue. The distractor is parsing the model's text for "I'm done". Check the stop reason, not the prose.

SAM: Pause here and answer before we go on. A public-sector benefits assistant asks a citizen for their case number, calls a lookup tool, and three turns later asks for the case number again. Logs show each request carries the system prompt and only the latest user message. What is the root cause and fix? A, the context window is too small; move to a model with a larger window. B, the Messages API keeps no memory between calls; the application must resend the full conversation, including the earlier tool call and its result, on every request. C, the model is ignoring earlier turns; add an instruction to remember case numbers. D, raise the maximum output tokens so the model can hold more state. [pause]

ALEX: B. The API is stateless.

SAM: B. A standard Messages API call keeps nothing between requests. Your code holds the history and sends all of it, every turn. A blames capacity when nothing was ever sent. C asks the model to remember text it never received. D changes output length, not input. And the interleave with Domain two: because the full history is resent, context grows every turn. That is why prompt caching and context trimming matter in long sessions. [sting]

## Segment five: extraction

SAM: Segment five, extraction. Symptom: an insurance pipeline extracts claim forms. When the policy number is missing, the output contains a plausible policy number anyway.

ALEX: The schema makes the field required, so the model has to put something there.

SAM: Exactly the mechanism. A required, non-nullable field is an instruction to produce a value. Make fields optional or nullable where the source may lack them, and say in the prompt that absent means null. For categories, add an "unknown" value, and an "other" value with a free-text detail field, so a currency or claim type outside your list has somewhere honest to go instead of the nearest wrong option.

ALEX: Let me argue the other side. The claims team would rather have the model's best guess than a blank. A guessed policy number is often close, and a null just creates work.

SAM: A blank does create work, and nobody likes an empty field.

SAM: The problem is that a guessed value looks exactly like an extracted one. Nothing downstream can tell them apart, so the invention enters the claims system as fact. A null says "not on the form" and lets review deal with it.

ALEX: And strict schema enforcement does not fix that by itself.

SAM: No. Strict mode guarantees the shape. It cannot stop a well-shaped invented value. That is a schema design problem, and the tell is "missing" or "plausible" in the stem: give absence a legal value, never a better guesser.

ALEX: Then I would make every field nullable. Required fields are where invention comes from.

SAM: Careful, that is the new rule outrunning its scope. The fix is nullable where the source may lack the value. A field every form carries can stay required.

ALEX: Miss pattern four.

SAM: Yes. Watch for "every" in an option. "Make every field" anything is a blanket rule; the right answer is scoped to the field the stem names.

SAM: Pause here and answer before we go on. Choose two. A procurement team extracts supplier invoices. Two failure patterns: a purchase order number appears on invoices that have none, and currencies outside the five listed are reported as the closest listed currency. Which two changes address the root causes? A, make the purchase order field nullable and instruct the model to return null when it is absent. B, add an "other" value to the currency enum with a free-text field for the actual currency. C, make every field required so missing data is caught. D, move to a larger model. E, add a second model pass that rewrites any value it suspects was invented. [pause]

ALEX: A and B.

SAM: Both. A gives absence a legal value; B gives an unlisted currency one. C is the cause, not the fix. D is scale instead of structure. E is a compensating control that adds a second probabilistic step to fix the first.

ALEX: Then which extractions does a person check?

SAM: Symptom: everything goes to review, the queue floods, and reviewers start approving without reading. The course names it: volume forces reviews to collapse into approvals. Route by confidence, by reversibility, and by the cost of a wrong answer. In extraction, that means field-level confidence, calibrated against a labelled set rather than taken at face value, because confidence is not correctness. Route by document type: a handwritten form or a type the system has rarely seen goes to a person. And route by field ambiguity: two candidate dates, a value that conflicts with another field. Keep a small sample of the auto-approved stream under review so you can measure the error rate you are not seeing.

SAM: Pause here and answer before we go on. Choose two. A lender's document pipeline sends all four thousand daily extractions to three reviewers. Errors still reach the loan system. Which two changes best focus review where it is needed? A, route individual fields whose confidence falls below a threshold calibrated on labelled documents. B, always route document types with a history of low accuracy, such as handwritten income statements. C, add five more reviewers so every extraction is still checked. D, use the model's own stated confidence with a fixed threshold, without calibration. E, stop human review entirely and rely on the schema. [pause]

ALEX: A and B.

SAM: Both. They put attention on low confidence and high-risk document types. C is scale instead of structure; the volume still collapses review. D trusts a number nobody has checked. E removes the gate the stakes require.

SAM: Last part of the segment, feedback loops. Symptom: the same extraction errors recur month after month. Reviewers fix them in the queue and leave a free-text comment.

ALEX: The corrections never reach the system.

SAM: Right. Capture each failure as structured metadata: document type, field, failure category such as missing, invented or wrong format, the prompt version, and the source snippet. Aggregate it. The top categories become targeted changes: a field made nullable, a real failing case added as a few-shot example, a prompt clarification, and the case added to the eval set so it cannot regress. This is the "feedback loop" stage of the Domain one architecture, and the "iterative improvements" task in Domain four. The distractors: free-text comments nobody aggregates, fine-tuning as a first move, and a bigger model. [sting]

## Segment six: refinement and resumption

SAM: Segment six, refinement and resumption. Symptom: a developer asks Claude Code to transform an API response into a new shape. Three rounds of "closer, but the dates are still wrong" go nowhere.

ALEX: Show it. One concrete input and the exact output you want.

SAM: Concrete input-output examples beat prose descriptions of a format. Feedback names the specific case and the expected result, not "still wrong". And batch the issues that interact: if the date format and the timezone handling depend on each other, raise them in one message, because fixing one alone breaks the other. Independent issues can go one at a time.

ALEX: And resumption?

SAM: Symptom: an agent reviewed a twelve-file service yesterday. Overnight, three files changed. Resume the session, tell it exactly which three files changed, and ask it to re-analyse those in the light of its earlier findings. Starting fresh throws away valid work. Resuming without naming the change leaves it reasoning over stale tool results. When most of the context is stale, the better move is a fresh session seeded with a structured summary of the findings.

SAM: Back to the cold open. Alex, you picked A.

ALEX: I did, and I will defend it. A prompt change ships today, B is engineering work, and one in a hundred down to one in a thousand is a good result for most products.

SAM: For most products it is, and speed to ship matters to a real client.

SAM: But this is a bank, and money moves on that call. So, B. The refund tool checks for a verified customer ID and returns an actionable error, so the order holds every time. A improves the odds but cannot guarantee them; one in a hundred becomes one in a thousand, and a bank still has a problem. C removes a capability the business needs, the blunt cut that loses something required. D is "use a bigger model", which is never the answer to an enforcement gap.

ALEX: So what should have stopped me?

SAM: The word "first", followed by an action that moves money. A required order before that action is a deterministic need, and order that must hold lives in code. [sting]

## Five to remember

SAM: Five to remember. One: CLAUDE dot md guides; permissions, hooks and managed settings enforce. "After every edit" is a PostToolUse hook in project settings.

ALEX: Two: project scope is shared and versioned, user scope is personal. Shared M C P servers go in the project's config, with secrets as environment-variable placeholders.

SAM: Three: tool choice forces a call on a turn; order that must hold is checked in code. Loop while the stop reason is tool use, and resend the full history every request.

ALEX: Four: missing data needs a legal value. Nullable fields and "unknown" or "other" enum values stop invention. Route review by calibrated confidence, document type and ambiguous fields.

SAM: Five: failures captured as structured metadata become schema changes, real examples and eval cases. Refine with concrete examples and targeted feedback, and resume sessions by naming exactly what changed.

## Recap: the exam tells

SAM: Before we wrap, pause and name the six segments from today, each by the symptom that opened it. [pause]

ALEX: Unformatted files despite a CLAUDE dot md line. A new hire missing the M C P server. The wrong tool called, and no orders reported when the database was down. An agent stopping with half an answer. Invented policy numbers. And three rounds of still wrong on a data transform.

SAM: Good. Now as exam tells. If a question says always, every time, or after every edit, think hook or permission, not louder wording. A CI check is detective; the hook acts at the edit.

ALEX: If an option commits a token or key to the repo, strike it. Shared config, an environment-variable placeholder, and scope set by who needs it.

SAM: If the model picks the wrong tool, think descriptions. If it cannot tell empty from failed, think errors flagged with a category and whether a retry makes sense.

ALEX: If an order must hold before money moves, think a check in code, not tool choice alone.

SAM: If an agent stops mid-task, check the stop reason. If it forgets earlier turns, the API is stateless and the history was not resent.

ALEX: If the stem says missing or plausible, think nullable fields and an other or unknown value. If reviewers rubber-stamp, route by calibrated confidence, document type and ambiguous fields.

SAM: And if the same errors recur, think structured failure metadata. If refinement stalls, think one concrete input and output. If a session resumes after files changed, name exactly which ones.

ALEX: That closes the gaps. The final drill puts these mechanics back in the mix.
