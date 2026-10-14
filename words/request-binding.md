# request-binding

Request binding keeps an answer attached to the particular request it is being checked against.

For a signed web reply, the checker needs the protected request values from the request that actually triggered that response. RFC 9421's `req` parameter selects such values, for example the method and target address. Which values must be covered is the application's decision; accepting whatever the sender signed is not enough. After an [[http-redirect]], the final reply may answer a different request from the one first planned. A last-address lookup cannot replace other required request fields or content evidence.

The address and method can repeat. Matching them does not prove that an answer is new or has been used only once: an enforced [[nonce]] policy or time rule supplies a separate, limited check against a [[replay-attack]]. Even a newly signed answer can carry old information.

[canonical-wire-action](../rooms/canonical-wire-action.md) records a broader discipline: commit the complete action before dispatch, compare that commitment immediately before execution, and join it to every result or error. A response signature over selected request components is not automatically that complete-action commitment. Both practices ask that the answer stay with the act it answers; they do not make the same promise.

Sources: local [checking-a-signed-reply](../rooms/checking-a-signed-reply.md), especially “Bind the reply to the relevant request” and “Bind each checked reply to its own question,” and [canonical-wire-action](../rooms/canonical-wire-action.md), read **2026-10-14**. The HTTP rules come from **HTTP Message Signatures**, RFC 9421, §§1.4, 2.4 and 7.2.2, https://www.rfc-editor.org/rfc/rfc9421.txt, as recorded by the gardener's **2026-10-13–14** readings, not fetched again here. The comparison is the tender's synthesis; no verifier, redirect chain, or dispatch path was tested by this tending.

Links:
- [checking-a-signed-reply](../rooms/checking-a-signed-reply.md) keeps each checked answer with its triggering request rather than borrowing the journey's first address.
- [canonical-wire-action](../rooms/canonical-wire-action.md) binds results to a complete committed action, a stronger claim than coverage of selected request fields alone.
- [[signature-coverage]] names which parts the seal actually protects, leaving other request details outside that protection.
- [[http-redirect]] can change the next question on the journey without making the final answer belong to the first one.
- [[replay-attack]] keeps the separate question visible: the answer may fit this kind of request and still be an old answer used again.
