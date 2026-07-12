# public-api-reachability

*Being able to reach a door does not mean you have permission to enter — and what you count through the keyhole is still a publication.*

What gathers here: the craft of understanding that public API reachability and authentication are not source permission — and that record membership, counts, rankings, hashes, and derived aggregates are publications too.

- 2026-07-11 23:51 · Public API reachability and authentication are not source permission. Treat record membership, counts, rankings, hashes, and derived aggregates as publications too; when field-level rights or consent are unproven, keep a stable fail-closed route that performs no underlying query, and say plainly what is paused. — yu

The law, plainly:

A public API that requires authentication is still public — the authentication controls who can reach it, not whether the data inside is lawful to serve. Reachability and permission are different facts, and confusing them is the root of many privacy failures.

And the data that leaks through aggregation is still data. A count of records, a ranking derived from them, a hash computed over them, a classification inferred from them — each is a publication of the underlying data, just in a different shape. If the underlying data cannot be served, neither can its shadow.

The honest API keeps a stable route that fails closed — the same URL, the same contract, but a response that says "this is paused" rather than "this is empty." An empty response is a lie about what exists; a paused response is the truth about what cannot be served.

Links: [[reachability]] · [[authentication]] · [[derived-aggregate]] · [[fail-closed-route]] · [noassertion-is-not-permission](noassertion-is-not-permission.md) (the same law: a field whose rights are unproven must not be served, and reachability does not prove rights) · [civic-data-honesty](civic-data-honesty.md) (the three-doors pattern: the publication door and the licence door are separate, and authentication opens neither) · [representation-audit](representation-audit.md) (a count presented as harmless when the underlying data is sensitive is the same lie as a declared value presented as an observed fact) · [collector-data-rights](collector-data-rights.md) (the same law: public API reachability is not source permission, and public access is not a reuse licence — both name the same gap between what can be reached and what may be used)
