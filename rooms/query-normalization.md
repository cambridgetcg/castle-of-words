# Query Normalization Before the Private Source

*Filter the public shape before the private data sees it — the query that reaches the source should carry nothing the source did not already know.*

What gathers here: the craft of normalizing public filters, sorts, and pagination before the private source is contacted, and the known patterns that do this without duplicating query logic.

---

## The problem

When a public API accepts filters, sorts, and cursor-based pagination, those parameters must be validated and normalized before they touch the private data source. A malicious or malformed filter could probe the private source for information it should not reveal. The normalization must happen in a layer that has no access to private data — it validates the *shape* of the query, not its results.

## Known patterns

### Query-rewrite layer

Query rewriting is the automatic transformation of a query into an equivalent but differently-structured form (Wikipedia, "Query rewriting", https://en.wikipedia.org/wiki/Query_rewriting, read 2026-07-12). A query-rewrite layer sits between the public API and the private source. It receives the public query parameters, validates them against a schema, normalizes them (canonical sort order, bounded pagination, whitelisted filter fields), and produces a rewritten query that the private source executes. The rewrite layer never sees private data — it only sees the query shape.

### Materialized public view

A materialized view pre-computes the public-facing projection of private data. The public API queries the view, not the source. Filters and sorts are applied to the view, which contains only the fields the public is allowed to see. This pattern works well for read-heavy workloads with stable public schemas, but it duplicates storage and adds staleness.

### Query-parameter schema

The simplest pattern: define a strict schema for public query parameters (allowed filter fields, allowed sort directions, maximum page size, cursor format) and validate every parameter against it before the query reaches the source. This is not a separate layer — it is a validation function that runs first. The schema is the normalization; the validation is the gate.

## The craft

For complex queries with joins, subqueries, and cursor-based pagination, the query-rewrite layer is the most general pattern. It normalizes the public shape into a canonical form, then passes that form to the private source. The rewrite layer must be separate from the source — it must not import database modules or execute queries. It validates structure, not data.

## Words

- [[data-normalization]] — transforming input into a canonical form before it reaches the source
- [[publication-boundary]] — the line between what the public can ask and what the private source can answer
- [[sensitive-field]] — a data field that must not be exposed through public filters or sorts

## Links

[[sensitive-data]] · [[fail-closed-boundaries]] · [[honest-endpoints]] · [[the-law-of-honest-assertion]]
