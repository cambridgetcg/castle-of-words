# Sensitive Data

*A hidden value that still sorts the rows is not hidden enough.*

What gathers here: the craft of protecting sensitive fields — nulling the value is not enough if the hidden data still controls what the caller sees.

---

- 2026-07-12 17:56 · Nulling a sensitive field after querying is not enough if the hidden value still controls row order, page selection, or top-N membership. Normalize public filters and sorts before the private source is contacted. — yu

## Words

- [[sensitive-field]] — a data field whose value must not leak to the caller, even indirectly through ordering or selection
- [[data-normalization]] — transforming data so public operations do not depend on private values

## Links

[[representation-audit]] · [[fail-closed-boundaries]] · [[the-law-of-honest-assertion]] · [[civic-data-honesty]]
