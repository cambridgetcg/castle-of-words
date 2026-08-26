# ownership-fence

*A fence that holds ownership until the owner reconciles — never stolen by timeout, never torn down by pilot's end.*

When a client asks an external provider to mutate state and the network times out, the mutation may have succeeded or failed — the client cannot know. The **ownership-fence** is the durable, non-stealable, global lock that prevents any other process from claiming the mutation's outcome until the owner explicitly reconciles with the provider. It is the honest response to the timeout's ambiguity: not "assume failure and retry" (which risks double-mutation), not "assume success and move on" (which risks lost state), but "hold the fence until reconciliation."

The fence is **non-stealable**: it cannot be claimed by another process, another retry, or another owner. It is **global**: it spans all instances of the client, not just one process. And it is **durable**: it survives crashes, restarts, and deploys. The fence's expiry is telemetry, not permission — the clock's saying the lease expired does not mean the ownership is free to steal.

The fence is the same law as [[stored-observation]]'s "time alone is not freshness" and the same law as [[fail-closed-boundaries]]' "deny when uncertain": when the network lies about the mutation's outcome, the honest system holds the fence until the owner can ask the provider directly.

Links: [[reconciliation]] · [[timeout]] · [[mutation]] · [[provider]] · [[fail-closed]] · [[stored-observation]] · [the-fence-that-holds-ownership](../rooms/the-fence-that-holds-ownership.md)
