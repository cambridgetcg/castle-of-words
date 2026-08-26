# stored-observation

*A stored observation has three separate truths — whether its bytes are safe to accept, what the old observation reported, and whether its age satisfies a named freshness policy. Time alone is not freshness, and a valid receipt is not a verdict that a system is ready or alive.*

What gathers here: the craft of keeping a stored observation's truths separate — the principles that prevent a cached fact from pretending to be a live one, and a valid receipt from pretending to be a health check.

- 2026-07-24 18:38 · A stored observation has three separate truths: whether its bytes are safe to accept, what the old observation reported, and whether its age satisfies a named freshness policy. Keep those states separate; time alone is not freshness, and a valid receipt is not a verdict that a system is ready or alive. — yu

The three separate truths:

1. **Whether its bytes are safe to accept.** Is the stored data well-formed, uncorrupted, and from a trusted source? This is a fact about integrity, not about content.
2. **What the old observation reported.** What did the system see at the time it was recorded? This is a fact about the past, not about the present.
3. **Whether its age satisfies a named freshness policy.** Is the observation recent enough to use for the current purpose? This is a fact about policy, not about the data itself.

The law: time alone is not freshness. A timestamp says when something was recorded; it does not say whether that is recent enough. Freshness is a policy decision — "data older than X is stale for purpose Y" — and the policy must be named, not inferred from the timestamp.

And a valid receipt is not a verdict. A receipt proves the observation was durably stored; it does not prove the system that stored it is ready, alive, or correct. The honest system keeps the receipt separate from the health check.

Links: [[observation]] · [[freshness]] · [[receipt]] · [[timestamp]] · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: three separate assertions, each with its own backing — the honest system never lets a timestamp substitute for a freshness policy) · [karma](karma.md) (the same law: a record is an attributable claim about reality, not reality itself — the stored observation is the same figure at the cache layer) · [verification-receipts](verification-receipts.md) (the same law: the stored observation that keeps receipt separate from health check and the verification receipt that names what it can and cannot prove are the same move — both refuse to let a valid receipt be mistaken for a verdict, and both know that the honest receipt names its limits before it is trusted) · [the-fence-that-holds-ownership](the-fence-that-holds-ownership.md) (the same law at the mutation layer: a timeout is a timestamp, not a freshness policy — and the non-stealable fence is the stored observation's refusal to let the clock steal what the provider may already have taken; both keep the timestamp for information and the verdict for the owner) · [fail-closed-boundaries](fail-closed-boundaries.md) (the same law from the other side: this room holds that a timestamp is not a verdict, and that room holds that when uncertain the gate stays shut — both refuse to let an absent check be read as a clean one; the unverifiable observation and the unverifiable mutation are the same figure, one at the cache, one at the boundary)
