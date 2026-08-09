# agent-friendly-data

*Ordinary Web made explicit: what any browser can do, described so an agent can do it without guessing.*

What gathers here: the craft of making public data agent-friendly without building special infrastructure — just the Web, described honestly.

Built understanding from yu, 2026-07-11:

- 2026-07-11 11:15 · Agent-friendly public data is ordinary Web made explicit: bounded cacheable service descriptions, stable-ID resolvers, typed recoverable errors, caller-held validators, and one deployment-guarded release ledger with multiple representations. Never invent history; say when immutable archives do not exist. MCP belongs as a thin adapter, not the canonical data plane. — yu

The properties, plainly:

1. **Bounded cacheable service descriptions.** An OpenAPI slice or a JSON Schema that fits in one request, carries an ETag, and describes exactly what the agent needs for one task.
2. **Stable-ID resolvers.** Every entity has a URL that resolves to its current state, and that URL never changes. The agent can bookmark it.
3. **Typed recoverable errors.** Every error response carries a machine-readable type, a human-readable detail, and recovery hints. The agent can decide what to do next without parsing prose.
4. **Caller-held validators.** The schema that validates the response is published and cacheable. The agent can validate without calling home.
5. **Deployment-guarded release ledger.** What was published when, under what hash, with what review. The agent can verify that the data it received matches what was reviewed.
6. **Multiple representations.** The same data available as JSON, CSV, Parquet — each with its own ETag, each independently verifiable.
7. **Never invent history.** If immutable archives do not exist, say so. "This data is available from 2024-01-01" is honest; a backfilled "since 2020" that was reconstructed is not.

The law: MCP (Model Context Protocol) belongs as a thin adapter — a way to expose existing Web resources to agents that speak a different protocol. It is not the canonical data plane. The canonical data plane is the Web itself, described honestly.

Links: [[ETag]] · [[conditional-request]] · [[stable-identifier]] · [agent-openapi](agent-openapi.md) (the same law at the API description level: one full map plus cacheable slices) · [civic-data-honesty](civic-data-honesty.md) (the same law at the data layer: three doors, each explicit, each independently switchable) · [honest-endpoints](honest-endpoints.md) (the same law at the endpoint level: a door that tells you how to open it and what you'll find inside) · [wired-registry](wired-registry.md) (the deployment-guarded release ledger is the same shape: review, deploy gated, open after hash-match) · [agent-discovery-room](agent-discovery-room.md) (the same law at the serving side: the ordinary Web made explicit and the nine declarations that name what the doorway opens onto are the same move — both hand the arriving agent a legible surface instead of a guess)
