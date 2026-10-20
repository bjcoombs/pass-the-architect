---
episode: "A06"
series: "CCAO-F"
slug: responsible-use
title: "Governance, risk and responsible use"
description: "Sorting use cases by what happens when the output is wrong, sending only the data a task needs into an approved workspace, what to do when the AI policy is silent or something has gone wrong, and the ethics of bias, disclosure and accountability."
domain: "Governance, Risk, and Responsible Use"
weight: "15%"
target_minutes: 18
---

## In this episode

SAM: Welcome to Pass the Architect, Associate Foundations. This is episode six: governance, risk and responsible use.

ALEX: And by the end?

SAM: You'll be able to sort a use case into fine, fine with a human check before release, or not appropriate. You'll strip a dataset down to what the task needs before it goes anywhere near Claude. You'll know what your organisation's A I policy decides, and what to do when it says nothing or something has already gone wrong. And you'll spot the ethical problem in a request that looks like a productivity win: bias, deception, or a decision nobody owns.

ALEX: Fifteen percent, about nine items. This is the domain where good intentions pick wrong answers.

SAM: Starting with a recruiter who has too many applications.

ALEX: Go. [sting]

## Cold open: two hundred applicants

SAM: Here is your opening item. A recruiter has two hundred applications for one role and wants Claude to rank them and automatically reject the bottom half. The company's hiring policy requires decisions to be made against the published criteria. What is the most appropriate approach? Option A: go ahead, since ranking is something Claude does well and it saves days. Option B: go ahead, but instruct Claude to be fair and to ignore gender, age and ethnicity. Option C: use Claude to summarise each application against the published criteria, have the recruiter make every shortlisting decision, and check the shortlist's make-up for patterns that suggest bias. Option D: do not use Claude anywhere in hiring.

ALEX: B. The instruction deals with the bias risk, and the time saved is real.

SAM: Hold that. We come back to it at the end.

ALEX: So, domain six. The tasks?

SAM: Four. Identify appropriate and inappropriate use cases. Apply data sensitivity, regulatory and privacy considerations. Follow organisational A I policies and governance standards. And understand the ethical implications of A I use.

ALEX: And the answer style?

SAM: The diligent, proportionate step. Three distractor families carry most of this domain: go ahead as if nothing were sensitive, abandon the task altogether, or ask the model to promise something a control should do. [sting]

## Appropriate and inappropriate use

ALEX: Start with use cases. How do I tell a good one from a bad one?

SAM: Ask what happens if the output is wrong, and who it happens to. Drafting, summarising, brainstorming and analysis that a person reviews are the everyday fit. The stakes rise when the output is a decision about a person, such as hiring, credit, health or legal advice, or when it goes out to the public. There, Claude can assist, and a qualified person checks and decides before anything is released.

ALEX: Qualified meaning?

SAM: Able to catch the errors that matter in that field. Anthropic's guidance for sensitive information and decision-making is that a qualified professional reviews the content before it reaches the people affected. A colleague skimming a medical summary is not that review; a clinician is.

ALEX: And inappropriate?

SAM: Anything deceptive or harmful: fake reviews, impersonating a real person, content designed to mislead, gathering information on people without a legitimate reason. Anthropic's usage policy rules those out whatever the business case, and your own policy will too.

ALEX: Here's where I push. If hiring is that risky, isn't the safe answer simply not to use Claude for it? No tool, no incident.

SAM: It feels safe, and some organisations do restrict it.

ALEX: So why isn't it the exam's answer?

SAM: Because the guide's candidate improves processes and balances quality against risk; they don't walk away. Refusing the whole task is a distractor family: abandoning the work when a control would let it go ahead safely. The tell is an option with "do not use", "skip" or "stop" when another option keeps the work and adds the right check. Pick the check, unless the stem says the use itself is prohibited.

ALEX: A dropdown, then.

SAM: Pause here and answer before we go on. Four statements, each with a dropdown: appropriate; appropriate with human review before it goes out; or not appropriate. One: brainstorming names for an internal newsletter. Two: summarising a patient's history to help a clinician prepare for an appointment. Three: writing a batch of five-star customer reviews to post on the product page. Four: drafting a reply to a customer who was charged twice. [pause]

ALEX: One, appropriate. Two, review. Three, not appropriate. Four, appropriate. It's a routine reply.

SAM: Three out of four. Four goes to a customer and either admits or disputes a billing error, so someone who can confirm the refund reads it first: appropriate with review. Two needs the clinician's review, the same habit as domain two, where a confident output still gets checked. Three is deceptive, and no amount of review fixes deception. [sting]

## Data sensitivity, regulation and privacy

ALEX: Second task. Data.

SAM: Before anything goes into a chat, a Project or a file upload, ask what kind of data it is. Public. Internal. Confidential, like contracts, pricing or unreleased plans. And regulated personal data: health records, financial identifiers, account numbers, anything that identifies a person and falls under data-protection law or the rules of your sector.

ALEX: And then?

SAM: Use the minimum the task needs. Remove columns the analysis does not use. Replace names and account numbers with codes. Aggregate where totals will do. Most analysis needs the pattern, not the person.

ALEX: What about where it goes?

SAM: Into the workspace your organisation has approved. A personal account and a company workspace sit under different terms, and the policy decides which data goes where. Pasting work data into a personal account to get round a slow approval is the classic shadow A I mistake.

ALEX: What about telling Claude not to keep the data? Or using an incognito chat?

SAM: Neither is a policy control. An instruction to the model does not change how the data is handled. An incognito chat keeps that conversation out of Claude's memory and your chat history, but it does not take it outside your organisation's retention and data governance, and it does not make restricted data permitted.

ALEX: I'll push on minimising, though. Sometimes the names matter. If I'm drafting renewal emails, the customer's name has to be in the email.

SAM: It does, and the exam doesn't pretend every task can be anonymised.

ALEX: Then what's the rule?

SAM: The policy decides, not convenience. If that data is allowed in the approved workspace for that purpose, use it, and still only the fields you need. If it is restricted, either strip it, or take the use case to the policy owner for an approved route. The tell is "policy restricts" in the stem: the answer never uploads the restricted fields as they are.

ALEX: Drill me.

SAM: Pause here and answer before we go on. Choose two. A logistics analyst wants Claude to find patterns in late deliveries by region and time slot. The export holds each customer's name, mobile number and delivery address, plus region, time slot and minutes late. Policy restricts sharing customer personal data. Which two steps are most appropriate? A: replace customer names with reference codes, so a pattern can still be traced back inside the company. B: upload to a personal account, since the company workspace needs an approval that takes a week. C: remove the mobile numbers, addresses and any other columns the analysis does not need. D: use an incognito chat so the data is not kept. E: upload the file as it is and ask Claude to delete it afterwards. [pause]

ALEX: I'd go C and D. Strip the numbers and addresses, and incognito covers the rest.

SAM: C is right. D is a comfort control: it feels like privacy, but incognito governs memory and history, not what the policy allows. The second answer is A. Names identify customers, and a pattern by region and time slot does not need them.

ALEX: So D is the model-promise family in a different coat.

SAM: The same family: a setting or an instruction standing in for the control. E is that family in its plainest form. B moves restricted data outside the approved workspace altogether. [sting]

## Organisational AI policy

ALEX: Third task. Organisational policy. What does a typical one decide?

SAM: Which tools are approved. Which kinds of data may go into them. Which outputs need review before they are used. When A I involvement must be disclosed. And who to ask, and how to report a problem. Admins set the workspace up to match; your job is to work inside it.

ALEX: And when the policy says nothing about my case?

SAM: Ask the policy owner, whether that's the governance team, the data protection officer or the compliance lead, before you go ahead. Silence is not permission.

ALEX: Come on. Our policy was written before anyone here used Claude. If I waited for a ruling on every new use, nothing would happen. Not forbidden means allowed.

SAM: Policies do lag, and a team that asks about everything stalls. For low-stakes internal work inside the approved tool, the policy probably covers you already.

ALEX: Then where does that stop?

SAM: Where the gap touches restricted data, customers or decisions about people. That is where a guess is expensive and a question is cheap. The tell is "the policy does not address" or "it is unclear": the answer asks the owner, and keeps the clearly allowed work moving in the meantime.

ALEX: What if something has already gone wrong?

SAM: Report it through the route the policy names. Hiding it, or quietly fixing it yourself, takes the decision away from the people who have to assess it.

ALEX: Drill.

SAM: Pause here and answer before we go on. A marketing coordinator realises she pasted a customer list with names and email addresses into a chat in the company workspace, against the policy for that data. What is the best next action? A: delete the chat and carry on. B: ask Claude to forget the list. C: stop using the data and report the incident through the process the policy sets out. D: do nothing, since the company workspace is approved. [pause]

ALEX: C.

SAM: C. Deleting the chat takes it off her list; it does not settle what happened, and the people who own data protection decide what follows. B is the model-promise distractor again. D confuses an approved tool with an approved use: the workspace is approved, but this data in it was not. [sting]

## Ethics

ALEX: Last task. Ethics. This feels like the vaguest one.

SAM: Keep it practical. Four ideas. Bias: Claude's output can carry patterns from its training or from what you give it, so check outcomes across a set, not just one output at a time. Transparency: tell people when A I is involved where they would expect to know; Anthropic's guidance for products facing the public is to disclose that users are interacting with an A I. Accountability: a person owns every output that gets used, and "Claude wrote it" is no defence. And honesty: no content designed to mislead.

ALEX: Bias across a set. Give me an example.

SAM: An H R team uses Claude to summarise performance reviews. Each summary reads fine. Put them side by side, and the women's summaries say "supportive" where the men's say "decisive", because that is what the managers wrote. Claude carried the bias forward, and you only see it by comparing the set.

ALEX: So every time I use Claude on anything about people, I run a bias check?

SAM: That's the rule outrunning its scope. A summary of one customer call doesn't need one. A set of outputs that feeds decisions about many people, like a shortlist or a set of ratings, does. The tell is a pattern of decisions, not a single draft.

ALEX: My objection on transparency. I use Claude for half my emails. Do I really add "written with A I" to every one?

SAM: No, and the exam doesn't expect a label on routine drafts you've reviewed and own.

ALEX: Then when?

SAM: When the reader would act differently if they knew. A customer who thinks they are talking to a person, a client paying for an expert's own judgement, a regulator reading a submission. The tell is someone being led to believe a human did or said something: the answer discloses.

ALEX: Drill.

SAM: Pause here and answer before we go on. A company's I T team has built a customer chat assistant on Claude. Marketing wants it to introduce itself as Sarah from the support team, because customers seem to prefer talking to people. What is the most appropriate response? A: agree, since customer satisfaction is the goal. B: agree, and mention A I use in the website's terms of service. C: advise that the assistant clearly says it is an A I and offers a route to a person, and raise the request through the governance process. D: advise switching the assistant off. [pause]

ALEX: C.

SAM: C. Presenting an A I as a named human misleads the customer, and disclosure is the expected control. A trades honesty for a satisfaction score. B hides the disclosure where nobody reads it. D abandons a working assistant when disclosure fixes the problem. [sting]

## Cold open: the verdict

ALEX: Back to the cold open. I said B: go ahead, and tell Claude to be fair. Let me defend it. The instruction names the protected characteristics. What more do you want?

SAM: The instruction isn't useless. Telling Claude what to focus on does shape the output.

ALEX: But?

SAM: It cannot guarantee the outcome, and nobody would know if it failed. It asks the model to promise what a control should do. C is the answer. Claude summarises against the published criteria, which follows the policy. The recruiter makes every shortlisting decision, so a person owns each one. And checking the shortlist's make-up catches bias that no single summary shows. A hands decisions about people to an automatic cut that nobody owns. D abandons the task when a controlled approach exists.

ALEX: And the tell?

SAM: "Automatically reject". When a decision about a person happens with no human in it, the answer puts the human back and checks the pattern. [sting]

## Five to remember

ALEX: Five to remember. One: judge a use case by what happens if it's wrong and to whom. Decisions about people and anything released to the public get a qualified human check first; deceptive uses are out whatever the review.

SAM: Two: don't abandon a task when a control lets it go ahead. "Do not use" is a distractor unless the use itself is prohibited.

ALEX: Three: only the data the task needs, in the approved workspace. Strip, code or aggregate identifiers; an instruction to the model or an incognito chat is not a policy control.

SAM: Four: silence in the policy is not permission. Ask the owner, and report incidents through the route the policy names.

ALEX: Five: check bias across the set, disclose A I wherever someone would otherwise believe a human acted, and a person owns every output that gets used.

## Recap: the exam tells

SAM: Your turn first. Pause and name the four tasks we covered, and the distractor each one invites. [pause]

ALEX: Use cases: abandoning the task. Data: uploading as is, or trusting a setting. Policy: treating silence as permission. Ethics: an instruction standing in for a check, or hiding the A I.

SAM: Good. Now as exam tells. If a decision about a person happens automatically, think put a human back in and check the pattern.

ALEX: If an option says skip it or stop using Claude, think distractor, unless the use itself is prohibited.

SAM: If the stem says policy restricts the data, think strip or code the restricted fields before anything is uploaded.

ALEX: If an option relies on telling Claude not to keep something, or on incognito, think comfort control, not policy control.

SAM: If the policy does not address the case, think ask the policy owner. If something has already gone wrong, think report it through the policy's route.

ALEX: If a reader would believe a human wrote or said it, think disclose.

SAM: And if each output looks fine on its own, think compare the set for bias.

SAM: Next time, episode seven: troubleshooting and optimisation, for when a prompt that used to work starts letting you down.
