# read-only

A claim that a service or endpoint does not mutate state — but only within a named scope.

"Read-only" is not one property. Domain writes can be paused while rate-limit counters and last-used timestamps still change. A read-only claim must name its scope: which domain's writes are paused, which metadata may still change, and which transport (REST, JSON-RPC, MCP) the claim covers. Remote JSON-RPC method compatibility is not the same as an MCP transport — the scope includes the protocol.

Links: [[api-contracts]] · [[read-only-contract-testing]] · [[honest-endpoints]]
