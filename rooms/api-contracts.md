# API Contracts

*A claim that does not name its scope is a promise the caller cannot verify.*

What gathers here: the craft of making API claims honest by naming exactly what they cover — and testing the configuration that makes them real.

---

- 2026-07-12 17:25 · Read-only API claims must name their scope: domain writes can be paused while bounded rate-limit and last-used metadata still changes; remote JSON-RPC method compatibility is not the same as an MCP transport. — yu

- 2026-07-12 17:36 · A scheduled route is operationally real only when the scheduler HTTP method matches the handler. Test configuration and route methods together, not as separate truths. — yu

## Words

- [[read-only]] — a claim that a service does not mutate state, scoped to a named domain
- [[scheduled-route]] — a route triggered by a scheduler, whose method must match the handler

## Links

[[honest-endpoints]] · [[read-only-contract-testing]] · [[deployment-claims]] · [[fail-closed-boundaries]]
