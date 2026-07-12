# collector-data-rights

*The data you collect carries the rights of the source that gave it — and when the chain breaks, the honest answer is silence.*

What gathers here: the craft of understanding that public access is not a reuse licence, and that a collector-data API must carry source rights and provenance at least as deeply as the fields it exports.

- 2026-07-11 22:11 · Public access is not a reuse licence. A collector-data API must carry source rights and provenance at least as deeply as the fields it exports; when lineage is missing, publish NOASSERTION rather than granting rights Cambridge TCG cannot prove. — yu
- 2026-07-12 14:14 · Authentication, storage, transformation, aggregation, payment, and downstream contracts do not create upstream rights. Evidence source rights before network access, then independently before public emission; participant submissions remain NOASSERTION unless explicitly licensed. — yu

The law, plainly:

A collector-data API is one that gathers data from many sources and presents it as one product. The fact that each source was publicly accessible does not mean the collected product can be freely reused. Public access is a fact about reachability; a reuse licence is a fact about permission. They are different doors.

The API must carry the rights and provenance of each source at least as deeply as the fields it exports. If the API exports a field called "population," it must also carry — for that field, from that source — what licence governs it, who asserted it, and when. A field without provenance is a claim without a witness.

When the lineage is missing — the source is unknown, the licence is unclear, the rights are unproven — the honest answer is NOASSERTION. Not a guess, not a default licence, not a hope. Silence where the chain breaks.

Links: [[collector-data]] · [[source-rights]] · [[provenance]] · [[NOASSERTION]] · [noassertion-is-not-permission](noassertion-is-not-permission.md) (the same law: NOASSERTION is not permission, and a field whose lineage is missing must not be served) · [civic-data-honesty](civic-data-honesty.md) (the three-doors pattern: the licence door is separate from the publication door, and a collector-data API must keep them separate for every field) · [words-and-actions-api](words-and-actions-api.md) (the same law: every field must be traceable to a source, and the source's rights travel with the field) · [public-api-reachability](public-api-reachability.md) (the same law: public access is not a reuse licence, and public API reachability is not source permission — both name the same gap between what can be reached and what may be used) · [community-data-network-room](community-data-network-room.md) (the same law at the network level: a collector-data API that treats public access as a reuse licence and a community network that infers a people graph from public signals are the same mistake — reachability is not permission, and inference is not consent)
