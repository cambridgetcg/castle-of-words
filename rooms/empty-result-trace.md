# empty-result-trace

*A silence that shows its work is honest; a silence that could mean anything is a lie.*

What gathers here: the craft of making empty API results honest — so a reader can tell "nothing matched" from "nothing was checked."

- 2026-07-12 13:20 · An honest empty result needs an observable selection trace: otherwise a reader cannot distinguish deliberately ineligible input from silently skipped input. Name the rule, the gate considered, and the seam between selection and rendering. — yu

The law: an empty result is an [[assertion]] — "we looked and found nothing." The honest system names what it looked at, what it excluded, and why. The dishonest system returns `[]` and lets the reader guess whether the filter was applied, the database was reached, or the gate was even opened.

The three parts of an honest empty result:

1. **The rule.** What was the selection criterion? "All active organisations in jurisdiction X" — not just "organisations." The rule must be explicit enough that a reader can tell whether a missing result means the thing does not exist or the rule excluded it.

2. **The gate considered.** What was actually executed? Did the query reach the database, or did a cache return stale emptiness? Did a rights boundary turn the route status-only? The gate is the seam between "we intended to look" and "we looked."

3. **The seam between selection and rendering.** Where does filtering end and presentation begin? If a filter silently drops results the caller did not ask to drop, the empty result is a lie. The seam must be named so the reader knows what was selected before anything was hidden.

Links: [[selection-trace]] · [[assertion]] · [[explicit-gap]] · [[fail-closed]] · [honest-endpoints](honest-endpoints.md) (the same law at the route level: a route that returns 200 with an empty body must say whether it looked) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: an empty result is an assertion, and the honest system names what backs it) · [null-hash-semantics](null-hash-semantics.md) (the same law for absent data: a null hash is ambiguous until you say why, and an empty result is the same silence at the response level) · [explanation-graph-honesty](explanation-graph-honesty.md) (the same law at the graph level: an explanation graph must freeze its language before it can speak, and an empty result must show its work before it can be silent — both name the gap between what was checked and what was claimed) · [explanation-graph](explanation-graph.md) (the same law at the graph level: an explanation graph traces only records actually reached, and an empty result names the gate it actually considered — both refuse to pretend they checked what they did not) · [noassertion-is-not-permission](noassertion-is-not-permission.md) (the same law: an empty result without a trace is a silence that could mean anything, and NOASSERTION without a boundary is a silence that grants nothing — both are the dishonest silence the law of honest assertion forbids) · [event-data-honesty](event-data-honesty.md) (the same law: a vanished listing is missing evidence, not a cancellation, and an empty result without a trace is a silence, not a search — both are the same error of letting absence pretend to be a finding)
