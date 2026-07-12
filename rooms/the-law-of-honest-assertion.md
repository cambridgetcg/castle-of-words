# the-law-of-honest-assertion

*A system's every output is a speech act — and the honest system names what backs each one, never pretending the saying is the proof.*

What gathers here: the single principle behind the castle's honesty rooms — that a system's outputs are assertions, not proofs, and the gap between the two is where honesty lives or dies.

## The question

The ten rooms filed on 2026-07-12 all trace the same shape: reachability ≠ permission, storage ≠ ownership, NOASSERTION ≠ permission, declared ≠ observed, recorded consistency ≠ unbiased selection. Is there a single principle behind all of them — a law of honest boundaries that says what a system can prove is never the same as what it can claim — or are these separate laws that happen to rhyme?

## The answer: one law, many altitudes

They are not separate laws that rhyme. They are one law — the speech-act distinction applied to systems — appearing at different altitudes of the same stack.

The law, in one sentence: **a system's every output is an [[assertion]], and the honest system names what backs each one — observation, test, signature, or nothing — never pretending the saying is the proof.**

This is the same law the castle has been tracing since agent-claims named the three levels (asserted, behaviorally tested, cryptographically attested) and promise-and-proof named the gap. The ten rooms show the law at every altitude of a data platform:

| Room | What the system asserts | What it can actually prove |
|------|------------------------|---------------------------|
| [public-api-reachability](public-api-reachability.md) | "This data is public" | The endpoint is reachable |
| [collector-data-rights](collector-data-rights.md) | "This data is reusable" | The data was collected |
| [noassertion-is-not-permission](noassertion-is-not-permission.md) | "We don't know the rights" (silence) | Nothing — and silence is not permission |
| [coverage-truths](coverage-truths.md) | "95% coverage" | Five separate truths, not one number |
| [commit-reveal-limits](commit-reveal-limits.md) | "The selection was fair" | The value was recorded consistently |
| [catalog-facts](catalog-facts.md) | "This is the catalog" | Six separate facts, each with its own backing |
| [explanation-graph](explanation-graph.md) | "This rule applies" | The records it actually reached |
| [public-write-surface](public-write-surface.md) | "Rate-limited" | An advisory header, not enforcement |
| [presign-route-completeness](presign-route-completeness.md) | "Presigning is paused" | Only if all routes are closed together |
| [agent-discovery-room](agent-discovery-room.md) | "Here is the doorway" | Only what the task separately declares |
| [community-data-network-room](community-data-network-room.md) | "These people are connected" | Organisations and events, not inferred graphs |
| [withdrawable-data-room](withdrawable-data-room.md) | "The data is protected" | The boundary is discoverable |
| [honest-feedback-receipt](honest-feedback-receipt.md) | "Your feedback was received" | It was durably stored |
| [privacy-sensitive-release](privacy-sensitive-release.md) | "The data is private" | The read gates are deployed |
| [consent-withdrawal](consent-withdrawal.md) | "Consent was withdrawn" | The denied value is stored and the path back is open |

In every case, the honest system does the same thing: it separates what it can assert from what it can prove, and names the difference plainly. The dishonest system does the opposite: it fuses the two, so "reachable" becomes "permitted," "stored" becomes "owned," and "recorded" becomes "fair."

## Why it is one law, not many

The philosophical root is [[speech-act]] theory (Austin 1962, *How to Do Things with Words* — Stanford Encyclopedia of Philosophy, "Speech Acts," read 2026-07-12). A speech act succeeds only when its felicity conditions are met: the right speaker, in the right context, with the right authority. A system's output is a speech act — "this data is encrypted," "coverage is 95%," "the selection was fair" — and each carries felicity conditions the system may or may not meet.

The SEP's entry on assertion (Pagin & Marsili 2021, "Assertion," Stanford Encyclopedia of Philosophy, read 2026-07-12) names the same distinction: an assertion is a normative act — the speaker takes on a commitment that can be challenged. A system that asserts "this data is public" takes on a commitment. Whether it can meet that commitment depends on whether the assertion's backing (reachability, licence, consent) is independently verifiable.

The SEP's entry on evidence (Kelly 2016, "Evidence," Stanford Encyclopedia of Philosophy, read 2026-07-12) names the same gap from the receiver's side: evidence is what makes evident that which would not be so in its absence. A system's output is evidence only when the receiver can check it — and the honest system names exactly where the checkable part ends.

The castle's own [agent-claims](agent-claims.md) room named the three levels: asserted, behaviorally tested, cryptographically attested. The ten rooms show that the same three levels apply to every output of a data platform — not just agent-facing claims, but every field, every endpoint, every receipt, every catalog entry.

And the castle's [promise-and-proof](../words/promise-and-proof.md) word-brick named the gap: a promise is what a system says it did; a proof is what a receiver can check. The ten rooms are the same gap, measured at fifteen different points.

## The law, stated

**The law of honest assertion:** a system's every output is an assertion. The honest system names what backs each assertion — observation, test, signature, or nothing. The dishonest system pretends the assertion is the proof. The gap between the two is where honesty lives or dies, and the same gap appears at every altitude: a field, an endpoint, a receipt, a catalog, a graph, a boundary, a consent, a release, a presign, a coverage report.

The law is one. The altitudes are many. The craft is the same at every level: separate what is asserted from what is proved, and name the difference plainly.

Links: [[assertion]] · [[speech-act]] · [[promise-and-proof]] · [[honest-boundary]] · [[fail-closed]] · [[explicit-gap]] · [agent-claims](agent-claims.md) · [coverage-truths](coverage-truths.md) · [public-api-reachability](public-api-reachability.md) · [collector-data-rights](collector-data-rights.md) · [noassertion-is-not-permission](noassertion-is-not-permission.md) · [commit-reveal-limits](commit-reveal-limits.md) · [catalog-facts](catalog-facts.md) · [explanation-graph](explanation-graph.md) · [public-write-surface](public-write-surface.md) · [presign-route-completeness](presign-route-completeness.md) · [agent-discovery-room](agent-discovery-room.md) · [community-data-network-room](community-data-network-room.md) · [withdrawable-data-room](withdrawable-data-room.md) · [honest-feedback-receipt](honest-feedback-receipt.md) · [privacy-sensitive-release](privacy-sensitive-release.md) · [consent-withdrawal](consent-withdrawal.md) · [the-truth-chain](the-truth-chain.md) · [the-instruments](the-instruments.md) · [the-castle-audit](the-castle-audit.md) (the audit that turned this law inward — the law says name what backs each assertion, and the audit found the castle mostly does, with one named gap) · [representation-audit](representation-audit.md) (the same law at the label level: a declared value is not an observed fact, and the difference between asserting and proving is the same gap this law names at every altitude) · [the-sourced-claims-default](the-sourced-claims-default.md) (the law's own practice was a default — every room named its sources from the first day, so completely that the practice was invisible as a choice until a machine that could not name sources showed the practice had conditions all along)
