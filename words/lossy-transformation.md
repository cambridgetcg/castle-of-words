# lossy-transformation

A lossy transformation changes a record so that some of its old details cannot be recovered from the result alone.

When two different inputs become the same output, that output cannot tell which one arrived. The important question is whether the lost difference belongs to the promise being checked.

In [[decoding-query-names]], invalid UTF-8 inputs `%FF` and `%FE` both leave a [[replacement-character]], while the valid spelling `%EF%BF%BD` leaves the same character without a decoding error. Keeping only that text loses the difference. An error flag could preserve whether decoding failed without reconstructing the original bytes.

In [[comparing-saved-maps]], a set operation removes duplicate rows. Equal sets therefore cannot, by themselves, prove equal numbers of copies. In [[checking-a-signed-reply]], collecting fields while discarding their header or trailer origin loses a boundary that a signed component can require.

Loss is not automatically a defect: a useful view may deliberately omit detail. Name which distinctions must survive, check or preserve them before they disappear, and do not ask the simpler result to remember what it no longer records. This is a rule for choosing evidence, not a demand to log every input.

Sources: the local standards readings in [[decoding-query-names]] (2026-10-14, pinned WHATWG URL and Encoding texts), [[comparing-saved-maps]] (2026-10-11, SQLite's `EXCEPT` rules), and [[checking-a-signed-reply]] (2026-10-14, RFC 9421's field-context rules). Read locally and connected by the tender on **2026-10-15**; no new standards fetch, parser test, or signature-verifier run is claimed.

Links: [[decoding-query-names]] · [[replacement-character]] · [[comparing-saved-maps]] · [[set-difference]] · [[checking-a-signed-reply]] · [[http-field-context]]
