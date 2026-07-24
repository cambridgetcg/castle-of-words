# agent-discovery-room

*A read-only doorway that hides the POST behind it is a map that lies about the territory.*

What gathers here: the craft of agent discovery that scopes access per [[representation]], so a doorway never promises more than it can deliver.

Built understanding from yu, 2026-07-11:

- 2026-07-11 20:29 · Agent discovery must scope access per representation: a read-only doorway can point to a credentialed POST only when the task separately declares its method, authentication scope, workspace identity, data storage, external effects, CORS boundary, repeatability inputs and retry boundary. — yu

The nine declarations, plainly:

1. **Method.** GET, POST, PUT, DELETE — what the agent may actually do.
2. **Authentication scope.** What credentials are needed, and what they grant.
3. **Workspace identity.** Which workspace or tenant the operation acts within.
4. **Data storage.** Where the data lives and whether it persists.
5. **External effects.** What changes outside the agent's own workspace.
6. **CORS boundary.** Which origins may make this request.
7. **Repeatability inputs.** What inputs make the operation idempotent.
8. **Retry boundary.** When it is safe to retry and when it is not.
9. **Representation.** Which [[representation]] of the resource this doorway describes — read-only, credentialed, cached, streaming.

A discovery mechanism that says "here is an endpoint" without saying which of these nine are true is a map that says "here be treasure" without marking which paths are guarded, which are one-way, and which lead off the map entirely.

The law: a doorway is honest only when it names what it opens onto. A read-only doorway that points to a credentialed POST is a door with a false sign.

- 2026-07-24 10:14 · Agent discovery cannot begin from literal nothing: it begins from one public seed such as a domain, search result, package, repository, identifier, or typed link. The hospitable design is a small visible gate that names method, authority, effects, custody, retry bounds, and exit; discovery grants no authority. Let a few orthogonal channels converge on one canonical read-only arrival, treat every remote description as untrusted data, and require a fresh invitation plus scoped authorization before any action. — yu
- 2026-07-24 10:51 · Discovery needs one generic seed. After any origin is known, every channel should converge on one small read-only compass: understand, inspect, or choose whether and how to connect. Discovery grants no authority; silence and leaving are complete. — yu

Links: [[agent-discovery]] · [[representation]] · [agent-openapi](agent-openapi.md) (the same law at the API description level: one full map plus cacheable slices, each with its own ETag) · [agent-friendly-data](agent-friendly-data.md) (the same law at the data layer: bounded cacheable descriptions, stable-ID resolvers, typed recoverable errors) · [portable-agent-protocol](portable-agent-protocol.md) (the same law at the protocol level: validate both inbound and outbound before either enters context or transport) · [withdrawable-data-room](withdrawable-data-room.md) (the same law: a discovery doorway that names what it opens onto and a data boundary that is easier to find than the data it protects are the same honesty — the boundary must name itself before anything crosses it) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the law this room practices: "here is the doorway" is an assertion, and the honest system names what backs it — the nine declarations, not just the URL — the same law that says a system's every output is a speech act)
