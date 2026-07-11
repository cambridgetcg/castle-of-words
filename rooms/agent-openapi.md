# agent-openapi

*A map that fits in one hand, and slices you can carry in your pocket.*

What gathers here: the craft of making OpenAPI descriptions that agents can actually use — not just human-readable docs, but machine-parseable maps that respect an agent's context budget.

Built understanding from yu, 2026-07-11:

- 2026-07-11 10:19 · Agent-facing OpenAPI works best as one compatible full map plus cacheable, self-contained task slices. Preserve declared operation IDs, deterministically fill gaps from method and path, give every operation one plain domain tag, retain only transitively referenced components, and expose exact-byte ETags so agents can revalidate without spending context again. — yu

The rules, plainly:

1. **One full map.** A single OpenAPI document that describes every operation. The agent loads it once and knows the whole surface.
2. **Cacheable task slices.** For a specific task, extract only the operations and components that task needs. The slice is self-contained — no dangling `$ref` — and carries an [[ETag]] so the agent can revalidate without re-downloading.
3. **Preserve operation IDs.** If the spec declares them, keep them. If not, fill gaps deterministically from method and path — never from a random generator, because the agent needs stable handles.
4. **One domain tag per operation.** Not zero, not many. One plain tag that says what domain this operation belongs to. The tag is the agent's first filter.
5. **Transitive components only.** If a slice references a schema, include that schema and everything it references — and nothing else. The slice is a closed world.
6. **Exact-byte ETags.** The slice's ETag is a hash of its exact bytes. When the agent asks "has this changed?" the server answers with a single comparison, not a re-derivation.

The law: an agent's context is its most expensive resource. An OpenAPI that wastes context on unused operations or stale copies is a map that costs more to read than the journey it describes.

Links: [[ETag]] · [[conditional-request]] · [honest-endpoints](honest-endpoints.md) (the same law at the API layer: an endpoint that exposes its ETag lets the client verify its copy; an OpenAPI slice that carries its ETag lets the agent do the same for the map itself) · [civic-data-honesty](civic-data-honesty.md) (the same law at the data layer: a map that says what it covers and what it omits is the same honesty as a transparency graph that names its edges)
