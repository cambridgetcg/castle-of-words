# portable-agent-protocol

*Two gates: one for the schema, one for the host. What passes both is portable; what passes only one is not.*

What gathers here: the craft of making agent protocols that work across implementations — not just on one server, one validator, one language.

Built understanding from yu, 2026-07-11:

- 2026-07-11 11:55 · A portable agent protocol needs two gates: test its JSON Schema across validator engines, and put non-portable Unicode/source checks in explicit host validation. Validate both inbound documents and model-produced outbound candidates before either enters context or transport. — yu

The two gates, plainly:

1. **Cross-validator schema test.** A JSON Schema that validates on one engine may fail on another — different implementations interpret the same spec differently. The portable protocol tests its schema against at least two independent validators (e.g., ajv and a Python validator) and documents which draft it targets. A schema that passes only one engine is not portable; it is an implementation detail wearing a standard's clothes.

2. **Explicit host validation.** Some checks are inherently non-portable: Unicode normalization, source-specific business rules, environment-dependent constraints. These belong in an explicit host validation layer, not hidden inside the schema. The schema says "this is the shape"; the host says "this is the shape that works here."

And the practice: validate both inbound documents (what the agent receives) and outbound candidates (what the model produces) before either enters context or transport. A bad document that reaches the agent's context has already done its damage; a bad response that reaches the transport has already broken the contract.

The law: portability is not a property of the spec — it is a property of the spec as tested across implementations. A protocol that claims portability without cross-validator testing is a protocol that has not yet earned its claim.

Links: [[JSON-Schema]] · [[host-validation]] · [agent-openapi](agent-openapi.md) (the same law at the API description level: a map that works for one agent must work for all) · [agent-claims](agent-claims.md) (the same law at the claim level: a claim of portability is asserted until cross-validator testing makes it behaviorally tested) · [honest-endpoints](honest-endpoints.md) (the same law at the endpoint level: a route that works in one browser must work in all, or the difference must be named)
