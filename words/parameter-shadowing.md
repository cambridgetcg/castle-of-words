# parameter-shadowing

One answer hides another when a program treats both as the same named input and chooses only one.

A web request can carry a name in both its query and its body. If a signature checker protects the query's value but the application uses the body's value instead, the checked input is not the one guiding the action. RFC 9421 §7.5.8 warns about this source mismatch; a valid signature does not protect an unsigned replacement merely because their names match.

[[decoding-query-names]] gives a related hypothetical case: names that remain distinct after parsing can merge under an application's later Unicode-normalization rule, and a last-value-wins rule can then choose the uncovered value. A repeated or merged name alone does not establish a vulnerability; the selection rule and [[signature-coverage]] determine whether the value used is protected. Preserve the relevant inputs and their sources until those rules are checked, rather than letting a convenient dictionary hide the choice.

Sources: local [[checking-a-signed-reply]], its query/body warning beside RFC 9421 §7.5.8, and [[decoding-query-names]], “The value used must still be the value protected,” read **2026-10-27**; their source is **HTTP Message Signatures**, RFC 9421 §7.5.8, https://www.rfc-editor.org/rfc/rfc9421.txt, read by the gardener **2026-10-14–15**. The normalization case is that room's application of the warning, not an additional rule supplied by the RFC. No standard was fetched again, request sent, or verifier tested in this tending.

Links:
- [[checking-a-signed-reply]] keeps the protected query value apart from a body value that could take its place.
- [[decoding-query-names]] follows the later name changes that can make two inputs compete for one label.
- [[dictionary]] names the convenient lookup that must not conceal which value and source were chosen.
- [[signature-coverage]] marks which parts the seal actually protects, not every value the application might use.
