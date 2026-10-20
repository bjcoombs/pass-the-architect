---
episode: "D05"
series: "CCDV-F"
slug: models
title: "LLM fundamentals and choosing a model"
description: "Tokens, context windows, sampling and why the same prompt can answer differently; extended and adaptive thinking, effort levels and fast mode; zero, single and multi-shot prompting; and choosing between Opus, Sonnet and Haiku when a release changes behaviour."
domain: "Model Selection and Optimization"
weight: "5.2% and 2.7%"
target_minutes: 18
---

## In this episode

SAM: Welcome to Pass the Architect, Developer Foundations. This is episode five: L L M fundamentals and choosing a model.

ALEX: And by the end?

SAM: You'll explain what a token is and why a test that compares exact strings fails at random. You'll choose between thinking, effort and fast mode by what each one actually changes. You'll decide when one example is too few. And you'll pick Opus, Sonnet or Haiku against a quality bar, a latency target and a budget, and know what to check when a new release breaks your code.

ALEX: Eight percent of the paper, about four items. The trap is answering "which model" by instinct instead of by the constraint in the stem.

SAM: So here is a stem. [sting]

## Cold open: two million emails

SAM: Here is your opening item. A retailer routes about two million customer emails a day into one of twelve queues. Each decision must come back in under a second, the budget is tight, and an eval set defines the accuracy the business accepts. The prototype runs the largest model at high effort and is too slow and too expensive. What is the best approach? Option A: keep the largest model and turn on fast mode. Option B: test the smallest, fastest tier against the eval set, and adopt it if it meets the accuracy bar. Option C: keep the largest model at maximum effort so accuracy has headroom. Option D: move to the middle tier and lengthen the prompt with every edge case the team can think of.

ALEX: A. Fast mode exists for exactly this: same model, faster.

SAM: Hold that. We come back to it at the end.

ALEX: Two skills, then.

SAM: L L M fundamentals: tokens, context windows, sampling, non-determinism and next-token generation; fast mode, extended thinking, adaptive thinking and effort levels; and zero, single and multi-shot prompting. Then model selection: Opus, Sonnet and Haiku use cases, the quality, latency and cost trade-off, and breaking behaviour changes across releases. [sting]

## How a model writes

SAM: A large language model is pretrained to predict the next token given everything before it. It writes one token, appends it, and predicts again. Everything it produces is that loop.

ALEX: So it doesn't plan the whole answer first?

SAM: Each token is chosen from what came before it. That is why reasoning written before the answer improves the answer, and why thinking exists. It is also why output can sound confident and still be wrong: fluency comes from the loop, correctness has to be checked.

ALEX: And a token is a word?

SAM: Sometimes. A token can be a word, part of a word, a character or a byte. On earlier Claude models a token is about three and a half English characters. A newer tokenizer produces roughly thirty percent more tokens for the same text, so the documentation's advice is to count tokens with the token counting endpoint, for the model you plan to use, rather than estimate.

ALEX: Context window?

SAM: The model's working memory: everything it can look at while generating. The system prompt, the conversation history, tool results and the reply being written all share it. It is not the training data, and it does not persist between requests unless you send it again. A bigger window lets you send more, but every token in it is paid for on each request, and a long, noisy context dilutes what matters.

SAM: Sampling is how the next token is picked from the probabilities. Temperature controls the randomness: higher gives more varied wording, lower sticks to the most probable. And the glossary says it outright: even at temperature zero, results are not fully deterministic, and identical inputs can produce different outputs.

SAM: Pause here and answer before we go on. A team's regression test sends a fixed prompt and asserts the reply equals a stored string exactly. Temperature is zero. The test fails on roughly one run in ten with no code change. What is the best fix? A, also set top k to one so only the most likely token is ever chosen. B, assert on the properties that matter, such as schema validity and the required fields, and score over several runs. C, switch to a larger model, which is more consistent. D, retry the call until the output matches the stored string. [pause]

ALEX: A. Temperature zero plus top k one is greedy decoding. Pin the decoding and the output pins with it.

SAM: That is a sound instinct from classical software, and narrowing sampling does reduce variation.

SAM: But the documentation does not promise determinism at any setting, and some newer models reject sampling parameters altogether. B. Design for variation: check structure and meaning, not bytes, and measure over several trials. C is "bigger" aimed at a test design fault. D hides the failure and burns calls.

ALEX: Tell?

SAM: "Exact match", "byte for byte", "same output every time". The fix is in how you assert, not in a knob. [sting]

## Thinking, effort and speed

SAM: Three controls that people blur. Extended thinking is the older manual mode: you turn thinking on and give it a token budget. Adaptive thinking is the newer mode: the model decides, request by request, whether to think and how much. A simple question may get no thinking at all.

ALEX: Do I still need the manual budget anywhere?

SAM: On older models that only take it, yes. On newer ones it is deprecated or rejected outright, and you steer with effort instead.

ALEX: And effort steers that.

SAM: Effort runs low, medium, high, extra high and max. It is a behavioural signal, not a strict budget, and it affects every output token: thinking, the text and the tool calls. Lower effort means fewer, more consolidated tool calls and terser replies. Max tokens stays the hard cap, and it covers thinking and the answer together. Thinking tokens bill as output tokens.

ALEX: So for anything important I'd set max effort. Why risk shallow reasoning?

SAM: On a genuinely hard problem, that can pay.

SAM: But the documentation warns that max can bring diminishing returns and overthinking, and it costs more on every request. And changing effort between requests invalidates the prompt cache, as episode one said of thinking settings. The exam wants the level that meets the stated quality bar, chosen by measurement.

ALEX: Tell?

SAM: "Simple", "high volume", "latency-sensitive" point to lower effort. "Hardest", "long-horizon agentic work" point to higher. "Just in case" is the distractor.

SAM: Then fast mode. It runs the same model with a faster inference configuration: up to two and a half times the output tokens per second, at premium pricing, on supported Opus models. No change to intelligence. The gain is in output speed, not in time to first token, and it is not available on the batch A P I.

SAM: Pause here and answer before we go on. Choose two. A chat assistant runs a large model at high effort with adaptive thinking. Users complain about a long wait before the first word appears on simple questions. Which two changes most directly shorten the time to the first visible text? A, lower the effort for this route so simple questions skip most of the thinking. B, stream the response so text appears as it is generated. C, turn on fast mode. D, raise max tokens. E, add five worked examples to the system prompt. [pause]

ALEX: B and C. Streaming, and fast mode for speed.

SAM: B is right. C is the trap the stem was built around. Fast mode speeds output tokens per second, not time to first token, and the complaint is the wait before the first word. A: less thinking before the answer on simple questions. D gives more room and changes nothing about the wait. E lengthens the prompt.

ALEX: So A and B. "Before the first word" was the phrase I skipped.

SAM: Pause here and answer before we go on. For each statement, say true or false. One: effort affects only thinking, not the text or tool calls. Two: max tokens caps thinking and the response together. Three: thinking tokens are billed as output tokens. Four: fast mode runs a smaller model to go faster. [pause]

ALEX: False, true, true, false. Effort touches every output token, and fast mode is the same model.

SAM: All four. [sting]

## Zero, one and many shots

SAM: Zero-shot is instructions with no example. Single-shot adds one. Multi-shot adds several. Zero-shot is the right start when the task is clear and the format is loose. Examples earn their tokens when a format or tone must hold. The documentation calls examples one of the most reliable ways to steer format, tone and structure, and recommends three to five that are relevant, diverse, and wrapped in example tags so Claude can tell them from instructions.

ALEX: I usually give one good example. Every example is tokens on every call.

SAM: True, and with caching those tokens get cheap. One example also beats none for format.

SAM: But one example is a template. The model copies its surface: its currency, its length, its layout. Diversity is what tells the model which features vary. When the stem says outputs copy a detail of the example, the fix is more varied examples, not a louder instruction.

ALEX: Tell?

SAM: "Copies the example", "always produces the same layout", "inconsistent format". Multi-shot, diverse, in tags.

SAM: Pause here and answer before we go on. An invoice extraction prompt includes one worked example, an invoice in euros. On invoices in other currencies, the output sometimes reports euros anyway. What is the best fix? A, add three to five diverse examples in example tags, covering several currencies and layouts. B, add "IMPORTANT: use the invoice's own currency" in capitals. C, remove the example and go zero-shot. D, raise the temperature so the model explores other currencies. [pause]

ALEX: A. B is louder guidance, C throws away the format control, D adds randomness to an extraction job.

SAM: A. [sting]

## Choosing a model, and when it changes

SAM: The tiers. Opus is the most capable of the three, for complex reasoning and long-running agentic coding, and the slowest and most expensive. Sonnet is the documented best combination of speed and intelligence, the everyday workhorse. Haiku is the fastest and cheapest, for high-volume, latency-sensitive work such as classification, extraction and routing, and for sub-agents. A bank's agent that reasons across a forty-page credit agreement: Opus. A summariser for a support desk: Sonnet. Tagging every incoming ticket by product: Haiku.

ALEX: In real projects I'd put Opus everywhere. Quality is what users notice, and I don't want to debug a cheaper model's mistakes.

SAM: For the hard, open-ended work, Opus is often the right call.

SAM: But the guide frames this as a trade-off across quality, latency and cost, and the exam's answer meets the stated constraint. If the eval says the smaller tier clears the bar, the larger one buys nothing but cost and wait. Also check what each model supports: not every model offered adaptive thinking, and older ones take the manual thinking budget. The Models A P I reports each model's capabilities.

ALEX: Then whenever a stem mentions cost, I go Haiku.

SAM: Now that rule outran its evidence. Cost in the stem does not cancel a quality bar in the same stem. If Haiku misses the accuracy the business set, it is the wrong answer however cheap. Read for the bar first, then pick the cheapest tier that clears it. And try a lower effort on the current model before switching tiers.

ALEX: The tell?

SAM: "Meets the accuracy bar on the eval", "under a second", "two million a day": smallest tier that passes. "Hardest reasoning", "long-horizon agent": Opus. No bar stated: measure before you choose.

SAM: Last, breaking changes across releases. A newer model can reject what an older one accepted. Prefilling the assistant's turn returns an error on newer models. The manual thinking budget is not accepted on later ones. Sampling parameters are restricted. A new tokenizer shifts token counts, and with them cost and limits. Defaults such as effort can change.

ALEX: So read the migration guide and re-run the evals.

SAM: And pin the model I D until they pass, which the last episode covered. A pinned model also retires in time; the deprecations page publishes the dates, so the move is planned, not avoided.

SAM: Pause here and answer before we go on. A team moves its service to a newer model I D. Every request that starts the assistant's reply with an opening brace, to force JSON, now returns a four hundred error. What is the best fix? A, return to the old model permanently. B, retry the failing requests with backoff. C, remove the prefill and request the JSON shape through structured outputs. D, raise max tokens. [pause]

ALEX: C. A four hundred is a request the model will not accept; retrying it changes nothing.

SAM: C. A is a freeze, not a fix, and the old model will retire. B treats a breaking change as a transient error. D is unrelated. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Alex, you chose A, fast mode.

ALEX: Which keeps the most expensive model and charges a premium on top.

SAM: The answer is B: test the smallest, fastest tier on the eval set and adopt it if it clears the bar. Classification at high volume with a one-second budget is the documented Haiku use case. A raises cost per token on a cost-constrained job. C adds latency and cost for headroom nobody asked for. D pays for a bigger prompt on every one of two million calls.

ALEX: The words?

SAM: "Two million a day", "under a second", "budget is tight", "accuracy the business accepts". Smallest tier that passes the eval. [sting]

## Five to remember

SAM: Five to remember. One: the model predicts the next token, again and again. Tokens are not words; count them with the token counting endpoint for your model. The context window holds prompt, history, tool results and reply.

ALEX: Two: temperature changes variety, but even at zero output is not fully deterministic. Assert on structure and meaning, over several runs.

SAM: Three: adaptive thinking lets the model decide whether to think; effort steers every output token; max tokens caps thinking and answer together; thinking bills as output.

ALEX: Four: fast mode is the same model with faster output tokens per second at premium price. It does not cut time to first token. Multi-shot means three to five diverse examples in tags.

SAM: Five: Opus for the hardest work, Sonnet for balance, Haiku for high-volume, latency-sensitive tasks. Pick the cheapest tier that clears the stated bar, and on a new release check prefill, thinking settings, sampling, tokenizer and defaults before moving the pin.

## Recap: the exam tells

SAM: Recall first. Pause and name the four segments, and the giveaway for each. [pause]

ALEX: How a model writes: exact-match tests fail. Thinking, effort and speed: which wait the user means. Shots: outputs copying the example. Choosing a model: the bar, the latency and the volume.

SAM: As exam tells. If the stem shows an exact-match assertion failing at random, think non-determinism, and assert on properties.

ALEX: If users wait before the first word, think less thinking and streaming. If the output is slow once it starts, fast mode.

SAM: If the task is simple or high volume, lower effort. If someone wants max "just in case", it is the distractor.

ALEX: If outputs copy one example's details, think three to five diverse examples in tags.

SAM: If the stem gives a quality bar, latency and volume, think the smallest tier that clears the bar. If a new model returns four hundreds on old requests, think breaking change: prefill, thinking budget or sampling parameters.

ALEX: Next, episode six: agents and workflows.
