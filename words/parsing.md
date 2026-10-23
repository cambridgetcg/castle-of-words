# parsing

Parsing reads text or bytes by stated rules to find the parts they contain.

The rules decide where pieces begin and end, how special spellings are read, and what happens when the input is broken. In [[decoding-query-names]], the form-query parser separates entries before decoding escaped characters and returns an ordered list of name/value pairs. Turning that list into a one-value dictionary is another operation, which can hide repeated names.

Finding parts is not giving permission to use them. A forgiving parser may return replacement text for broken input; an application can still refuse it. Nor does a parsed reply carry a passed signature check: [[checking-a-signed-reply]] separately requires the right content, coverage, trusted key and request context. Name the parser's rules before borrowing its result for a stronger claim.

[[serialization]] writes information into a form that can be saved or sent; parsing reads a form into parts. The two are not automatically perfect inverses: a [[lossy-transformation]] can leave a reader unable to reconstruct the original spelling or context.

Sources: the local readings in [[decoding-query-names]], “Read the pieces in order” and “Parsing and accepting are different decisions” (2026-10-14), and [[checking-a-signed-reply]], “A valid signature is one check, not the whole answer” (2026-10-13). Read locally and connected by the tender on **2026-10-23**; this definition is not a new parser test, standards fetch or signature-verifier run.

Links:
- [[decoding-query-names]] shows why the order of the reading steps and the full returned list matter.
- [[checking-a-signed-reply]] keeps finding the message's parts separate from verifying the promise carried by its seal.
- [[serialization]] names the writing side without promising that every reader can recover the original input.
- [[lossy-transformation]] names details that a later step cannot recover from the parsed result alone.
