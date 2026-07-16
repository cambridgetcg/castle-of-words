# API Contracts

*A claim that does not name its scope is a promise the caller cannot verify.*

What gathers here: the craft of making API claims honest by naming exactly what they cover — and testing the configuration that makes them real.

---

- 2026-07-12 17:25 · Read-only API claims must name their scope: domain writes can be paused while bounded rate-limit and last-used metadata still changes; remote JSON-RPC method compatibility is not the same as an MCP transport. — yu

- 2026-07-12 17:36 · A scheduled route is operationally real only when the scheduler HTTP method matches the handler. Test configuration and route methods together, not as separate truths. — yu
- 2026-07-16 19:25 · When an OpenAPI slice selects routes by prefix, deployment smoke tests that assert an exact path list must be changed in the same commit as any new child route; unit tests alone can pass while the production release gate fails on the stale list. — yu
- 2026-07-16 19:48 · For production JSON Schema APIs, commit a self-contained generated snapshot, check it for drift before tests, compile the served bytes with an independent Draft 2020-12 validator, restore generator-lost constraints such as exact tuples and uniqueItems, and keep cross-field rules in explicit runtime invariants. Release smoke tests must assert the current contract, not an earlier representation. — yu

## Words

- [[read-only]] — a claim that a service does not mutate state, scoped to a named domain
- [[scheduled-route]] — a route triggered by a scheduler, whose method must match the handler

## Links

[[honest-endpoints]] · [[read-only-contract-testing]] · [[deployment-claims]] · [[fail-closed-boundaries]]
