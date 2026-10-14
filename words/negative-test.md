# negative-test

A negative test checks that something which should be refused really is refused.

Choose the forbidden case and the expected boundary before running the test. Then check both the refusal and any work that must stay undone: an error returned after a forbidden read is not evidence that the read was prevented. Pair this with a permitted case, because a gate that refuses everything can also pass a refusal-only test. These are the tender's testing rules drawn from the local rooms below, not tests performed during this visit.

[[checking-a-signed-reply]] records RFC 9421's warning that successful examples cannot reveal a verifier that silently skips checking. [[verification-receipts]] likewise separates matching published examples from a checker that derives its answers, while [[fail-closed-boundaries]] asks an unreadable request to expose forbidden parsing. The common question is not just “can the good case pass?” but “does the wrong case stop at the intended boundary?”

Passing one negative test supports that tested case and path, not every possible bad input or every route into a system. A crash or unrelated failure is not automatically the intended refusal.

Sources: the three local rooms above, read **2026-10-14**; **HTTP Message Signatures**, RFC 9421, §7.1.1, https://www.rfc-editor.org/rfc/rfc9421.txt, as recorded in [[checking-a-signed-reply]] from the gardener's **2026-10-13** reading, not fetched again here. No verifier or route test was run by this tending.

Links:
- [[checking-a-signed-reply]] needs rejection cases because a checker that always says yes can appear to pass every successful example.
- [[verification-receipts]] keeps the result tied to what was actually tested rather than turning agreement into wider assurance.
- [[fail-closed-boundaries]] watches for forbidden work behind the refusal, not merely the error shown at the door.
