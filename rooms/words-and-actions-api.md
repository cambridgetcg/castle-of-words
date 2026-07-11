# words-and-actions-api

*A ledger is not a judge — it only says who used what, and when.*

What gathers here: the design of an API that tracks source use and attribution honestly — not as a verdict on correctness, but as a record of what was used, by whom, and how it can be checked.

- 2026-07-11 00:48 · A words-and-actions API is a source-use and attribution ledger, not a verdict. Safe reuse requires whole-public-field source review, bidirectional exact identifiers and explicit bridges, value omission rather than cosmetic suppression, result-level disclosure review with people-derived propagation, review chronology, and immutable correction history. Schema validation never grants publication. — yu

## What this means

The insight names seven properties of an honest attribution API:

1. **Whole-public-field source review**: Every field the API exposes must be traceable to a source. Not just the ones that are easy to trace — all of them.

2. **Bidirectional exact identifiers**: The API and its sources must point at each other with exact, machine-readable identifiers. A source that cannot be found from the API is a broken link; an API that cannot be found from the source is a hidden use.

3. **Explicit bridges**: Where the API transforms or combines sources, the transformation must be named and the bridge must be explicit. A derived field that does not say how it was derived is a claim without a witness.

4. **Value omission rather than cosmetic suppression**: When a value cannot be published (privacy, licence, uncertainty), omit it — do not replace it with a plausible substitute. A blank is honest; a guess dressed as a fact is not.

5. **Result-level disclosure review with people-derived propagation**: The review that decides what to publish must happen at the level of the result the public sees, and the propagation of that review decision must be traceable to the people who made it.

6. **Review chronology**: Every review decision carries a date. A review from last year is not the same as a review from today, and the API must say which is which.

7. **Immutable correction history**: Corrections are appended, never overwritten. A corrected record that erases the original correction is a lie about what was once published.

The final sentence — "Schema validation never grants publication" — is the keystone: passing a schema check means the data is well-formed, not that it is true, lawful, or safe to publish. The schema is a gate for shape, not for substance.

Links: [[honesty]] · [[publication-boundary]] · [[enforced-guarantee]] · [civic-data-honesty](civic-data-honesty.md) (the three-doors pattern — publication, licence, privacy as separate boundaries — is the same law at the data layer; the words-and-actions API adds the attribution door: not just what was published and under what terms, but what source was used and how) · [honest-endpoints](honest-endpoints.md) (the endpoint that exposes its ETag and allows conditional GETs is the web's face of the same principle: a promise that carries its own test) · [transparency-graph-audit](transparency-graph-audit.md) (the audit that checks each edge against its source is the same verification the words-and-actions API demands of every field: what the source proves, not what the API infers)
