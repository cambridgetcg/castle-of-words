# canonical-wire-action

The complete committed action bytes, bound before dispatch and joined to every result or error that follows.

A redacted or forecast version of an action cannot bind what actually runs. The honest system commits the complete canonical wire action separately, compares the same commitment immediately before dispatch, and joins that commitment to every result — so a later reader can verify that what was dispatched is what was committed, not a redacted summary of it.

Links: [[receipt]] [[digest]] [[commitment]] [[dispatch]]
