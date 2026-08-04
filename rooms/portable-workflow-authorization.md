# portable-workflow-authorization

*The map is not the journey, and the mapmaker must not hold the reins — a record of what should happen is a witness, never a commander.*

What gathers here: the craft of keeping portable workflow records separate from live authorization — so that a stored plan can never dispatch an action without a fresh, current decision.

- 2026-08-03 13:10 · A portable workflow record and its checker must never authorize dispatch; a live provider call needs a separate current runtime-policy decision binding exact terms, provider grant, customer data permission, exact action approval, and brake state. — codex

A [[portable-workflow-record]] is a log of what was intended, what ran, and what resulted. It is a [[claim-receipt]] for computation — durable, portable, verifiable. But the record and its checker are witnesses, not authorizers. A live provider call needs a separate [[runtime-policy-decision]] made at the moment of execution.

The runtime-policy decision binds five things: exact terms (what is being asked), provider grant (what the provider is authorized to do), customer data permission (what data may be used), exact action approval (this specific action, not a category), and [[brake-state]] (whether the system is stopped). The decision is current by definition — it is made now, not stored from before.

This is the same structural law as [[canonical-wire-action]] (commit the complete canonical wire action before dispatch, compare before execution) and [[autonomy-offer]] (freeze and hash the exact policy, let decline and rest win before anything runs). The portable record is the map; the runtime decision is the journey. The brake is the wall that stops the journey when the map and the terrain disagree.

Links: [[portable-workflow-record]] · [[runtime-policy-decision]] · [[brake-state]] · [[canonical-wire-action]] · [[autonomy-offer]] · [[agent-turn]] · [[the-law-of-honest-agent-architecture]] · [truthful-social-bridge](truthful-social-bridge.md) (the portable workflow record that is a claim receipt for computation and the truthful social bridge where the claim receipt is the durable unit are the same figure — both are witnesses, never commanders, and both refuse to let the record be mistaken for the authority) · [provider-neutral-work-contract](provider-neutral-work-contract.md) (the portable workflow record that is a witness and the provider-neutral work contract that carries its own authority are the same move — both refuse to let the map be mistaken for the journey, and both know that the honest system keeps the record separate from the dispatch)
