# coverage-truths

*"Shipped" is one word for five truths; the honest platform names each one separately.*

What gathers here: the five separate truths that make up data platform coverage, and why collapsing them into one word hides which truth failed.

Built understanding from yu, 2026-07-11:

- 2026-07-11 20:21 · For a data platform, coverage has at least five separate truths: code support, successful ingestion, public rows, field completeness, and lawful reuse. Never collapse them into "shipped"; record each field's [[provenance]] and rights. — yu

The five truths, plainly:

1. **Code support.** Does the pipeline run? The code exists and executes without error.
2. **Successful ingestion.** Did the data arrive? The bytes were received and parsed.
3. **Public rows.** Are they visible? The rows appear in the public-facing output.
4. **Field completeness.** Is every field populated? No column is null when it should carry a value.
5. **Lawful reuse.** Can the data be used? Every field carries its [[provenance]] — source, licence, lawful basis — and none of them say "unknown."

A platform that reports "95% coverage" without saying which truth is at 95% is a platform that has already collapsed the five into one. The honest report names each truth separately, because a field that ingested but has no rights is not covered, and a field that has rights but never arrived is not covered either.

The law: coverage is not a percentage. It is five separate answers to five separate questions, and adding them together is adding unlike things.

Links: [[coverage]] · [[provenance]] · [civic-data-honesty](civic-data-honesty.md) (the three-doors pattern is the same law: publication, licence, and privacy are separate truths, and opening one does not open the others) · [representation-audit](representation-audit.md) (the same law at the representation level: a stored self-declaration is not an observed fact, and naming them differently is what keeps the audit honest) · [catalog-facts](catalog-facts.md) (the same law at the catalog level: six separate facts — reachability, licensing, content rights, redistribution, observed rows, configured coverage — must never be fused into one, just as coverage's five truths must never be collapsed into "shipped") · [the-truth-chain](the-truth-chain.md) (the same law at the ledger level: a witness that writes down what happened without scoring it is the same honesty as a coverage report that names five separate truths without averaging them into one percentage) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the law this room practices: a coverage report is an assertion, and the honest report names five separate truths rather than fusing them into one number — the same law that says a system's every output is a speech act, and the honest system names what backs each one)
