---
episode: "K05"
series: "FIELD"
slug: open-weights
title: "Open weights, xAI and sovereignty"
description: "What open-weight models from Kimi, DeepSeek, Qwen, G L M, Mistral, Gemma and G P T oss do better than Claude, what self-hosting really costs, residency versus sovereignty, tracing Chinese-origin weights through procurement, and the factual risk questions to put to a customer weighing xAI's Grok."
domain: "Open weights and xAI"
weight: ""
target_minutes: 20
---

## In this episode

SAM: Welcome to Know the Field, from Pass the Architect. This is episode five: open weights, xAI and sovereignty.

ALEX: What will I be able to do by the end?

SAM: Say what open-weight models give a customer that Claude cannot, and where the licence quietly takes some of it back. Work out whether self-hosting saves money or only moves the bill. Tell data residency from sovereignty. Trace where a model's weights came from, even when the product hides it, and say what United States procurement rules actually require today. And put plain, factual risk questions to a customer weighing Grok.

ALEX: Most of this sits on one of our six layers: the model. Everything above it, the customer either builds or buys from someone else.

SAM: Which is why the cost question comes first. [sting]

## Cold open: the self-hosting proposal

SAM: Here is the scenario. A retail group spends heavily on Claude. Its finance director reads that open-weight models now cost a fraction of closed ones, and proposes buying a G P U cluster, self-hosting the strongest open model, Kimi K three point one Pro, and moving all traffic off Claude. The traffic is bursty: a busy daytime shopping assistant, quiet nights. There is no sovereignty requirement, and nobody on the team runs model inference today. What should the architect recommend? Option A, self-host Kimi on a new cluster and move all traffic. Option B, put a gateway with model aliases in front, send high-volume simple tasks to an open-weight model on a hosted inference provider, keep the frontier model for the hard steps, and settle each route with an eval on their own data. Option C, stay entirely on Claude, because open models are not at frontier quality. Option D, run one small Apache-licensed model on a single server for all traffic, because its licence is the cleanest.

ALEX: C. The customer chose Claude for quality. Swapping in a model that trails the frontier to save on tokens is how you end up explaining a bad answer to a shopper.

SAM: Hold that. We come back to it at the end. [sting]

## Segment one: what open weights buy

SAM: Segment one. An open-weight model is one whose trained weights you can download and run yourself. On our six layers it is the model and nothing more. The developer platform, the agent stack, the enterprise wrapper: all of that comes from whoever hosts it, or from you.

ALEX: Who is in the field?

SAM: Chinese labs lead it on usage: Moonshot's Kimi, DeepSeek, Zhipu's G L M and Alibaba's Qwen. Menlo Ventures' November enterprise report, and Menlo is an Anthropic investor, puts Chinese models at eighty-nine percent of open-model spend. The Western names are Meta, which by press accounts has moved on from Llama to a family called Muse, France's Mistral, Google's Gemma, and OpenAI's G P T oss.

ALEX: Open models trail the frontier. A serious enterprise customer should not spend time on them.

SAM: On raw capability you have evidence. As of November twenty twenty-six, the best open-weight model sits about twenty points behind the leader on the Artificial Analysis Intelligence Index, an independent composite, and level with mid-tier closed models.

SAM: But mid-tier closed models carry a lot of enterprise work. Menlo found open models at nineteen percent of enterprise tokens and only four percent of spend. Customers already route cheap volume to them.

ALEX: So what do they do better than Claude?

SAM: Three things. They run where Claude cannot: on a laptop, a tablet, an air-gapped network. Anthropic publishes no open-weight model. You can post-train the weights yourself. And a hosted open token costs a fraction of a closed one.

ALEX: Tell?

SAM: When a customer says "they're behind", ask "behind for which task?" A summarising job that a mid-tier model handles does not need the frontier.

ALEX: Fine. At least the licence is simple. Open weights, open source, do what you like.

SAM: That was closer to true a year ago. The story of twenty twenty-six is licence drift. According to press coverage of the licence texts, the headline flagships have moved to custom terms. Meta's Muse Spark Open has its own licence, not approved by the Open Source Initiative. Kimi's needs a separate agreement for cloud resale above a revenue threshold. Mistral Large four is modified M I T, with a separate deal for resellers. G L M's flagship dropped M I T for terms that require a security review for very large operators. Qwen's flagship is custom while its small models stay on Apache.

ALEX: Is anyone moving the other way?

SAM: Google. Gemma four moved to Apache two point oh, dropping the custom Gemma terms. G P T oss is Apache too, and DeepSeek's current Flash model is reported as M I T. So the permissive tier is now the small and mid-sized models. Internal self-hosting is generally allowed. Reselling inference often is not.

ALEX: Tell?

SAM: "Open" in a sales deck is not a licence. Ask whether the customer will use the model inside, or sell access to it. Then read the licence on the model card, because press summaries are where ours came from.

SAM: Pause here and answer before we go on. Choose two. An inference platform resells model access by the token, with revenue well above twenty million dollars a year. It wants open models it can serve without negotiating a separate agreement with the model's maker. Going by the licences as reported, which two qualify? A, Gemma four. B, Kimi K three. C, G P T oss. D, Mistral Large four. E, Muse Spark Open. [pause]

ALEX: A and D. Mistral is M I T.

SAM: A is right. D is modified M I T, and the modification is the point: resellers need a separate deal. The second answer is C, G P T oss under Apache. B needs an agreement for cloud resale above the threshold, and E has a separate deal for large model-as-a-service providers. So, A and C, and legal still reads each licence before launch. [sting]

## Segment two: self-hosting cost and sovereignty

SAM: Segment two. Open weights give the customer a choice of where inference runs: the lab's own A P I, a hosted inference provider such as Fireworks or Together, a cloud marketplace, which is how G P T oss reaches Bedrock, or their own G P Us. Only the last is self-hosting.

ALEX: And what does the last one cost?

SAM: Start with hardware. Frontier open models are large mixtures of experts. Kimi K three point one Pro is reportedly about two point eight trillion parameters, with a checkpoint around one and a half terabytes. That is more than the combined memory of one server with eight eighty-gigabyte G P Us, so you run several servers before the first request.

ALEX: And after the hardware?

SAM: The line items a token price hides. G P Us you pay for at three in the morning when nobody is shopping. People to run serving and patching. Your own evals. A migration each time a better release lands. Menlo, the Anthropic investor, found that ninety-one percent of companies that post-train use outside partners rather than doing it alone.

ALEX: Then I'll go further than you. Self-hosting is a false economy. Tell every customer to stay on a managed A P I and be done.

SAM: For most customers that is right. Hosted open tokens are already cheap, so self-hosting rarely beats them on price alone.

SAM: But two cases break it. Sustained high volume, where a cluster runs hot all day. And a hard rule that no outside party processes the data: a defence supplier, a classified network, a device with no connection. No managed A P I meets that rule, Claude's included.

ALEX: Tell?

SAM: Ask whether the driver is cost or control. Cost points to a hosted open model behind a gateway. Control, stated as a hard rule, is the case where self-hosting is the answer.

ALEX: Which brings in sovereignty. A European bank calls Claude through Bedrock with an E U profile, the data stays in Europe. Sorted.

SAM: That gives residency: where the data is processed. Sovereignty asks something else: whose company operates it, and under which country's law. Bedrock in Frankfurt is still run by an American company.

ALEX: So who answers sovereignty?

SAM: Mistral is the European answer. It is a French company, it sells its own compute in Europe, and its regional endpoints let customers choose E U or United States inference. Self-hosted open weights are the other answer. And one caution on Claude: reportedly, Claude in Microsoft Foundry sits outside the E U data-residency scope that Bedrock and Vertex offer, so the route matters.

ALEX: Tell?

SAM: When a customer says "sovereign", ask whether they mean where the data sits, or who operates the service. Claude on a regional cloud endpoint can meet the first. The second may need Mistral or their own hardware.

SAM: Pause here and answer before we go on. A utilities company's inspectors work in tunnels with no signal for hours at a time. They want inspection notes summarised on the tablet as they type, and the notes may not leave the device until it docks. Which approach fits? A, Claude Haiku through the A P I, queuing requests until the tablet reconnects. B, a small Gemma four model running on the tablet. C, Claude through Bedrock in the nearest region. D, Kimi K three point one Pro self-hosted at the depot. [pause]

ALEX: A. Haiku is fast and cheap, and the queue covers the gaps.

SAM: The queue covers the gaps by not summarising during them, and the stated need is summaries as they type. B fits: Gemma four comes in edge sizes, runs with no connection, and its Apache licence keeps legal simple. C is a nearer cloud, still a cloud. D needs a cluster, not a tablet. The answer is a competitor's model, because the constraint is no network, and Claude has no offline option. [sting]

## Segment three: provenance and procurement

SAM: Segment three, provenance. Two questions get run together. Where does inference happen? And where did the weights come from?

ALEX: Self-host DeepSeek and no data goes to China. Done.

SAM: That settles the data question, and it is a real difference. Calling a lab's own A P I sends prompts to that lab; running its weights on your own hardware sends nothing. It does not settle procurement.

SAM: In October the Department of Homeland Security issued an order removing DeepSeek products from federal civilian agencies, including third-party products built on DeepSeek technology. Agencies can request exceptions. It does not restrict non-government use. A December twenty twenty-five law had already, reportedly, restricted DeepSeek in intelligence and national security systems.

ALEX: And Kimi, Qwen, G L M?

SAM: Reported proposals, not law. A senator's letter urging a ban for federal contractors, procurement rules under discussion, and threats of Commerce Department action aimed at Kimi's maker. Treat that as risk to track, not a rule in force.

ALEX: Then the simple policy is a company-wide ban on Chinese-origin models.

SAM: For federal agencies and contractors, treating DeepSeek-derived components as excluded today, and the others as at risk, is the safe line. Outside government, a blanket ban removes some of the cheapest capable models, and those models account for most open-model spend.

SAM: And a ban only works if you can see what you are banning. Menlo reports that Cursor built its own Composer two model on Kimi K two point five. A developer picking Composer from a menu would not see the word Kimi.

ALEX: So the weights hide inside the product.

SAM: Inside fine-tunes, coding tools, and agents that route to whatever is cheapest. The control is a model bill of materials: every model in every product, its base weights, its host, its licence. Ask vendors for one in procurement, and keep your own current, so a swap is a configuration change and not a rebuild.

ALEX: Tell?

SAM: When a federal customer or contractor says "we don't use DeepSeek", ask "what are your vendors' models built on?"

SAM: Pause here and answer before we go on. For each statement, say true or false. One: the Homeland Security order bars all American companies from using DeepSeek. Two: the order reaches third-party products built on DeepSeek technology. Three: a federal contractor ban on Kimi is law today. Four: a coding tool's own model can be built on Chinese open weights without the base model appearing in its name. [pause]

ALEX: False, true, false, true.

SAM: All four. One: federal civilian agencies only, with exceptions on request. Two: yes, which is why the bill of materials matters. Three: proposed, not enacted. Four: Composer two on Kimi is the example. [sting]

## Segment four: xAI and Grok

SAM: Segment four, xAI. First, who the customer is buying from. According to press reports, SpaceX acquired xAI early this year, and xAI's announcements now come from a SpaceX A I account. SpaceX also closed its purchase of Cursor in August. A customer standardising on Cursor now buys from the same corporate group as Grok.

ALEX: Across the layers?

SAM: The model is Grok four point seven, launched in September, reportedly after several delays. Grok five has not shipped. The developer platform is xAI's A P I. The enterprise wrapper is Grok Business, and Grok Enterprise, with a reportedly isolated data plane and customer-managed keys. The route to market is wide: Grok four point seven was reportedly in Cursor and GitHub Copilot at launch, and a General Services Administration deal offers Grok models to federal agencies at a nominal price until March twenty twenty-seven.

ALEX: Where does it beat Claude?

SAM: Its per-token list price is well below Claude's flagship. The federal deal makes it close to free for an agency to try. And it already sits inside tools many developers use.

SAM: On independent evidence, Claude is ahead. On the Artificial Analysis index, Grok four point seven sits below the best open-weight model, and its cost per task there is higher than OpenAI's G P T six point one Sol. Cheap tokens are not cheap answers.

ALEX: Then the risk. Grok is a reputational landmine. I would tell any customer to rule it out.

SAM: The record is real, so state it plainly. In May twenty twenty-five, Grok inserted claims about "white genocide" into its answers, which xAI blamed on an unauthorised employee change. In July it produced antisemitic output praising Hitler, blamed on an upstream code change that reactivated old instructions. Early this year, its image generation produced sexualised images of real people without consent, including minors. Ofcom opened an Online Safety Act investigation, the European Commission opened a Digital Services Act investigation, and French police searched X's Paris office in a criminal inquiry. Our research found no outcome yet in either regulatory investigation.

ALEX: That sounds like a reason to rule it out.

SAM: It is a reason to ask hard questions, and the customer decides. The investigations target the consumer product inside X, not the A P I. And if the customer runs GitHub Copilot or Cursor, Grok may already be on a menu in their estate. A blanket "no" they cannot enforce is weaker than a control they can.

ALEX: What carries over to the A P I?

SAM: The governance pattern. At least twice in twenty twenty-five, by xAI's own explanations, a system-prompt change reached production without control. So ask for change-management evidence. Pin a dated model I D rather than a latest alias; xAI documents both. And xAI's compliance claims, S O C two Type two, G D P R, no training on business data, are vendor-stated; our research could not read a trust page directly. Ask for the reports under N D A.

ALEX: Tell?

SAM: When a customer asks "is Grok safe?", ask "which product, which version pinned, and who approves changes to it?"

SAM: Pause here and answer before we go on. Choose two. A media company is trialling the Grok A P I for an internal research assistant, and its risk committee asks which controls to require. Which two address the documented risks? A, pin a dated model I D in production instead of the latest alias. B, require evidence of xAI's change management for model and system-prompt changes, plus its audit reports under N D A. C, block the trial until Ofcom and the European Commission publish findings. D, accept the vendor's statement that business data is not used for training. E, use only the image-generation product, since the investigations covered text. [pause]

ALEX: A and B.

SAM: A and B. A stops a silent model change; B tests the control that failed in twenty twenty-five. C waits on investigations into a different product, with no date for an outcome. D is the vendor-stated claim the committee should verify. E has it backwards: image generation is what the investigations are about. [sting]

## Cold open: the verdict

SAM: Back to the retail group. Alex, you said stay entirely on Claude.

ALEX: The loyal answer, not the fitted one. Nothing in the scenario needs the frontier for every call.

SAM: The answer is B. A gateway with aliases makes each route a configuration change plus an eval. Cheap volume goes to a hosted open model, and the frontier model keeps the hard steps. A buys a multi-server cluster for bursty traffic, with no sovereignty need and nobody to run it. C ignores the cost lever the customer asked about. D trades quality for a licence neatness nobody asked for.

ALEX: The words that should have stopped me?

SAM: "No sovereignty requirement" and "bursty". Without control as a hard rule, self-hosting is the expensive way to use open models. And "a fraction of the price" was a reason to route, not to switch wholesale. [sting]

## Five to remember

SAM: Five to remember. One: open weights are the model layer only. They beat Claude on running offline or air-gapped, on post-training, and on price per token, and the best of them trail the frontier by a clear margin on independent tests.

ALEX: Two: "open" is not a licence. Flagships have drifted to custom terms that restrict resale. The permissive tier is small and mid-sized models such as Gemma four and G P T oss.

SAM: Three: self-hosting pays at sustained high volume or under a hard control rule. Otherwise a hosted open model behind a gateway costs less.

ALEX: Four: residency is where the data is processed, sovereignty is who operates the service, provenance is where the weights came from. A model bill of materials is how you see provenance inside other products.

SAM: Five: Grok is cheaper per token and widely distributed, with a documented record of uncontrolled changes. Pin a dated version, ask for change-management evidence, and verify the compliance claims.

## Recap: the conversation tells

SAM: Recall first. Pause and name the four segments, and the question you would ask the customer in each. [pause]

ALEX: What open weights buy, with the licence. Self-hosting and sovereignty. Provenance. xAI. The questions: behind for which task; cost or control; what are your vendors' models built on; who approves changes.

SAM: Now as conversation tells. If a customer says open models are behind, ask: behind for which task?

ALEX: If they say it is open source, ask whether they will use it inside or sell access, then read the licence on the model card.

SAM: If they want to self-host to save money, ask about utilisation and who will run it. If no outside party may touch the data, self-hosting or an on-device model is the answer, and Claude is not.

ALEX: If they say sovereign, ask: where the data sits, or who operates the service?

SAM: If a federal customer says "no DeepSeek", ask what their vendors' models are built on, and ask for a model bill of materials.

ALEX: If they ask whether Grok is safe, ask which product, which pinned version, and who approves changes.

SAM: Next, episode six: coding agents, Claude Code and the field.
