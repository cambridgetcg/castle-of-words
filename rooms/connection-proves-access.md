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

Links: [[accounting]] [[reconciliation]] [[freshness-gate]] [[provider-tool-bridge]] · [accounting-product-design](accounting-product-design.md) (the same law at the product level: the inspectable path from evidence to filing and the connection that names what it cannot see are the same move — both refuse to let access be mistaken for completeness) · [provider-tool-bridge](provider-tool-bridge.md) (the same law at the bridge level: the bridge that re-derives each call from provider bytes and the adapter that declares what it cannot see are the same move — both refuse to let the shape be mistaken for the substance)
