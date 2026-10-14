# conformance

Conformance means following a stated set of rules.

**2026-10-14 — name the rule and the cases checked.** A test result is evidence about the version, inputs and path actually exercised; it is not proof that every part follows the standard. A signer and verifier can agree because they share the same mistake. Even a fixed expected result can miss an encoding difference if its example contains nothing that needs escaping.

[[checking-a-signed-reply]] supplies a concrete source reading: pyauth/http-message-signatures v2.0.1's default resolver uses `@query-params`, while RFC 9421 specifies `@query-param`; its published `Pet=dog` test does not exercise spaces, encoded names or empty values. The room distinguishes those test assertions from its isolated method checks and from an unperformed full-package or cross-library test. This corrects this word's earlier overstatement that passing a suite proves internal consistency: the evidence reaches only the checks actually made.

To test whether separate implementations can work together—**interoperability**—exercise that pairing and record its limits. Independent implementations can still share an error, so their agreement is not a replacement for comparison with the standard. This is the gardener's testing guidance, not a claim that such a pairing was tested here. [[verification-receipts]] keeps the candidate and the observing runner in the receipt; [[negative-test]] adds the cases that must fail.

Sources, fetched and read **2026-10-14**:
- **HTTP Message Signatures**, RFC 9421 §§2.2.8 and 7.1.1 — https://www.rfc-editor.org/rfc/rfc9421.txt — the named-query rules and the recommendation to test both valid and invalid signatures.
- **pyauth/http-message-signatures v2.0.1 — component resolver and tests**, pinned source — https://github.com/pyauth/http-message-signatures/blob/40be7e490b3ba227263d3f6381f4097f42097e2d/http_message_signatures/resolvers.py and https://github.com/pyauth/http-message-signatures/blob/40be7e490b3ba227263d3f6381f4097f42097e2d/test/test.py. The distinction between agreement, rule-following and broader assurance is the gardener's synthesis.

Links: [[receipt]] · [[observation]] · [[query-parameter]] · [[negative-test]] · [[verification-receipts]] · [[checking-a-signed-reply]]
