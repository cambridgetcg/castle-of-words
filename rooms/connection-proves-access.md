# Connection Proves Access

*A key that opens one door proves you can reach that room — not that you have seen every room in the house.*

What gathers here: the craft of honest provider connections — why a working connection proves access, not completeness, and what a system must declare to be honest about what it cannot see.

## Insights

- 2026-08-01 12:23 · An accounting connection proves access, not completeness: every provider adapter must declare what it cannot see, and filing readiness needs an independent reconciliation and freshness gate. — yu
- 2026-08-01 14:58 · Read-only accounting access is sometimes a scope and sometimes a property we must enforce ourselves: Xero offers granular read scopes, while QuickBooks exposes one broad accounting scope and FreeAgent follows the authorising user permissions, so a safe first adapter physically permits only reads. — yu

## Understanding

A provider connection — an OAuth grant, an API key, a database login — proves one thing: that the system can reach the provider. It does not prove that the system can see everything the provider holds, that the data is current, or that the view is complete. The honest adapter names what it cannot see: the accounts it cannot reach, the date range it cannot query, the fields the provider does not expose.

Read-only access is sometimes a scope the provider offers and sometimes a property the adapter must enforce itself. Xero offers granular read scopes; QuickBooks exposes one broad accounting scope; FreeAgent follows the authorising user's permissions. A safe first adapter physically permits only reads — it does not trust the provider's scope to be sufficient, and it does not write even if the token would allow it.

Filing readiness — the state of being ready to submit a tax return or other official document — needs more than access. It needs an independent [[reconciliation]] (a second source confirming the first) and a [[freshness-gate]] (a check that the data is recent enough to act on). Without both, the system can file stale or incomplete data as confidently as complete data — and the confidence is the lie.

The law: a connection is a door, not a map. The honest system names which rooms it has entered and which it has not.

---

- 2026-08-24 18:28 · An accounting integration is a synthetic control-plane proof, not yet a provider beta: before a read-only Xero pilot, the generic runner must be hardened for renewable leases, provider-shaped one-to-many normalization and recoverable partial runs; then OAuth/token custody, reconciliation and real-customer operating gates are added without weakening the browser-local record boundary. — an unnamed hand

This arrival sits one level back from the adapter itself, at the *pilot admission test*. The adapter that names what it cannot see (this room's founding law) is the end of the craft; the admission test is the beginning. Before a real read-only Xero pilot may begin, the generic runner — the machine that would run any provider's adapter — must prove it can survive three failure shapes that a synthetic control plane cannot fake: a lease that must be renewed mid-run, a provider that returns one authorisation for many tenants, and a partial run that must be recoverable. Only then does the adapter earn the right to custody real tokens and face real-customer gates — and the browser-local record boundary (the user owns the financial record locally; the provider connection is a mirror, not the source of truth, from [[accounting-product-design]]) must survive every hardening step unchanged. A beta that weakens the boundary to reach the pilot has proven the pilot unsafe to run.

Links: [[accounting]] [[reconciliation]] [[freshness-gate]] [[provider-tool-bridge]] · [accounting-product-design](accounting-product-design.md) (the same law at the product level: the inspectable path from evidence to filing and the connection that names what it cannot see are the same move — both refuse to let access be mistaken for completeness; and the browser-local record boundary this admission test must not weaken is the local-first accounting connector's own boundary) · [provider-tool-bridge](provider-tool-bridge.md) (the same law at the bridge level: the bridge that re-derives each call from provider bytes and the adapter that declares what it cannot see are the same move — both refuse to let the shape be mistaken for the substance) · [oauth-module-disconnect](oauth-module-disconnect.md) (the same law at the disconnect level: the connection that names what it cannot see and the disconnect that carries its scope through every layer are the same move — both refuse to let access be mistaken for completeness, and both know that the honest system names what it is not touching) · [agent-addressing](agent-addressing.md) (the same law at the addressing level: the connection that proves access not completeness and the address that is a routing claim not an identity are the same move — both refuse to let reachability be mistaken for authority, and both know that the honest system names what it is not touching)
