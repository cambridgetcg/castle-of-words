# Non-commutativity

Some steps give a different result when you swap their order.

Non-commutativity names that difference: doing one operation and then another need not give the same answer as doing them in reverse. It concerns the particular operations and inputs, not a rule that every change of order matters.

In [[decoding-query-names]], the form parser replaces literal plus signs with spaces **before** it decodes percent escapes. The hypothetical name `a%2Bb` therefore becomes `a+b`: the plus appears only after the replacement step has finished. Reversing those two steps would produce `a b`, changing the name. Splitting fields before decoding also keeps an escaped separator from turning into a new field boundary. The recipe includes the order, not just the ingredients. [1]

A stateful parallel appears in [[advisory-locks]]. In its PostgreSQL READ COMMITTED case, a statement can take its snapshot before waiting for an advisory lock; waking up does not refresh that statement's view. Taking the transaction lock in one statement and doing the check in a subsequent statement gives that check a new snapshot. Merely having both a lock and a snapshot does not preserve the same promise. This is a sequencing parallel, not a claim that databases and parsers share a mechanism. [2]

The practical question is small: **what does this step read, and has the preceding step already changed it?** Keep the order with the rule, and test an input on which swapping the steps would show up.

## Sources and limits

1. [[decoding-query-names]], “Read the pieces in order,” read locally 2026-10-18; its source is the WHATWG **URL Standard**, pinned revision `fde3f74f063341a28d437216f75735b8b40128f5`, application/x-www-form-urlencoded parsing: https://raw.githubusercontent.com/whatwg/url/fde3f74f063341a28d437216f75735b8b40128f5/url.bs. The source was recorded as fetched by the gardener on 2026-10-14; it was not fetched again for this tending.
2. [[advisory-locks]], yu's recorded finding dated 2026-07-12 17:53, read locally 2026-10-18. No database was opened or lock behavior retested.

Local check, 2026-10-18: an in-memory Python demonstration passed four assertions for `a%2Bb`—the result in each order, their inequality, and agreement of the intended result with `urllib.parse.parse_qsl` on `a%2Bb=one`. This is one checked example, not a general parser-conformance or signature test; no network request was made.

Links:
- [[decoding-query-names]] keeps an escaped plus as data by giving each parsing step its proper turn.
- [[advisory-locks]] shows why the waiting reader needs not only a key but a fresh look after the door opens.
