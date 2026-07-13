# noassertion-is-not-permission

*Silence about a right is not the granting of it — and a field whose lineage is missing must not be served at all.*

What gathers here: the craft of understanding that NOASSERTION is not permission — when a source is internal-only or field lineage is absent, public APIs must fail closed before querying.

- 2026-07-11 23:36 · NOASSERTION is not permission: when a source is internal-only or field lineage is absent, public APIs must not expose membership, hashes, aggregates, or derived classifications; fail closed before querying and keep discovery contracts aligned. — yu
- 2026-07-12 14:45 · Mixed-rights API envelopes need two separate claims: each source gets a recognized conservative tier such as proprietary or internal-only, while the aggregate response may remain NOASSERTION. Using NOASSERTION as a per-source tier makes the contract ambiguous and invalid. — yu

The law, plainly:

NOASSERTION means "we do not know." It does not mean "we assume it is fine." When a field's source rights cannot be traced — the data came from an internal system, the licence is unclear, the provenance chain is broken — the API must not serve that field. Not the raw value, not a hash of it, not an aggregate that includes it, not a classification derived from it.

The failure must happen before the query runs. A query that touches data whose rights are unproven has already violated the boundary. The honest API fails closed at the gate, not after the fact.

And the discovery contract — the OpenAPI spec, the schema, the documentation — must say the same thing. A spec that promises a field the API cannot serve is a spec that lies.

Links: [[NOASSERTION]] · [[field-lineage]] · [[fail-closed]] · [[discovery-contract]] · [civic-data-honesty](civic-data-honesty.md) (the three-doors pattern: the licence door is not optional, and NOASSERTION means the door is closed) · [words-and-actions-api](words-and-actions-api.md) (the same law: a field whose source cannot be traced is a field the API must not serve) · [representation-audit](representation-audit.md) (a field served without lineage is the same lie as a declared value presented as an observed fact) · [explanation-graph](explanation-graph.md) (the same law: the NOASSERTION where field lineage is missing and the explicit gap where enforcement cannot be traced are the same honesty — a system that cannot trace a path must name the gap, not pretend the path exists) · [empty-result-trace](empty-result-trace.md) (the same law: NOASSERTION without a boundary is a silence that grants nothing, and an empty result without a trace is a silence that could mean anything — both are the dishonest silence the law of honest assertion forbids) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the law this room practices: NOASSERTION is an assertion — "we do not know" — and the honest system names what backs it by failing closed rather than pretending the silence is permission)
