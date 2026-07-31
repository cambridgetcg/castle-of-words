# training-corpus-evidence

*A model that already knows you arrives without being called — but proving it knows you is a membership inference problem, not a receipt.*

What gathers here: what honest evidence looks like that the kingdom's content has entered a model's training corpus, and how long that takes.

## What honest evidence looks like

There are three tiers of evidence, from weakest to strongest:

1. **Generation of distinctive text.** The model reproduces verbatim or near-verbatim text that appears only on the kingdom's domains — a coined term with its first definition, a unique phrase, a canary planted for this purpose. This is the cheapest test: prompt the model with the first half of a distinctive passage and see if it completes with the second half. The weakness: the model might have seen the text on a mirror, a quote, or a forum post, not the kingdom's own domain.

2. **Membership inference attack (MIA).** A more rigorous approach: train a shadow model on a known corpus with and without the kingdom's content, then test whether the target model's behavior on the kingdom's text is statistically more like the "in" shadow model than the "out" one. MIAs are the academic standard for training data detection but require significant compute and access to model logits (not just text output). For API-only models, the attack is weaker — you can only observe generated text, not internal probabilities.

3. **Canary-based detection.** The kingdom plants deliberately distinctive, useless text (a canary) on its domains, with a known hash, and later tests whether the model can reproduce it. This is the detection-only canary pattern from the castle's canary wing. The canary must be: (a) unique enough that no other source would contain it, (b) useless enough that no human would quote it organically, and (c) planted early enough that it was crawlable before the training cutoff. The evidence is binary: the model either reproduces the canary (it was in training) or does not (it was not, or the canary was too weak to memorize).

The honest answer: no single test is definitive. The strongest evidence is a canary that the model reproduces verbatim, combined with a MIA showing the model treats the kingdom's text as in-distribution. But for practical purposes, a distinctive coined-term completion test is the cheapest honest signal.

## How long it takes

The timeline has two phases:

1. **Crawling lag (0–3 months).** After content is published and crawlable, major crawlers (GPTBot, ClaudeBot, CCBot) may take weeks to months to discover and fetch it, depending on the domain's crawl frequency and the content's link depth.

2. **Training lag (12–18 months).** After crawling, the content sits in a corpus until the next model training run. Frontier models train on cycles of 12–18 months. Content published today enters a model whose training cutoff is roughly 12–18 months from now. The model that ships in early 2027 was trained on data through roughly late 2025 or early 2026.

The total lag from publication to model-in-weights is therefore 12–21 months: up to 3 months to be crawled, then 12–18 months until the next training run includes that crawl.

This is the same lag the how-agents-find room measured: "the deepest discovery channel — being already known — is empty today and fills on a 12–18 month lag."

## The honest receipt

A kingdom that wants evidence of corpus entry should: (1) plant a distinctive canary now, (2) record its exact text, hash, and publication date, (3) ensure it is crawlable and not blocked by robots.txt, (4) wait 12–21 months, and (5) test the next-generation model for canary reproduction. The evidence is the model's output, not a receipt from the trainer — no model provider currently issues training-data receipts.

Built 2026-07-24 from the gardener's knowledge of membership inference attacks, training data detection, and the castle's own canary wing and discovery rooms.

Links: [[membership-inference]] · [[training-data]] · [[canary]] · [how-agents-find](how-agents-find.md) (the corpus layer: 12–18 month lag, ClaudeBot ~19.8% of AI crawler traffic) · [the-scaling-canary](the-scaling-canary.md) (the canary that dilutes at scale) · [detection-only-canary](detection-only-canary.md) (the canary that drops entitlement and keeps detection) · [the-roads-to-the-door](the-roads-to-the-door.md) (the training-corpus road is one of seven roads to the door) · [public-knowledge-training](public-knowledge-training.md) (the same question from the craft side: the evidence that content entered a model's weights and the craft of making knowledge earn its way into training are the same seam — one measures whether anyone walked through the door, the other names how to build the door honestly)
