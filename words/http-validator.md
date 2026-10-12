# http-validator

An HTTP validator is a server's label or date that a later web request can use to check a saved copy.

**2026-10-12 — a check must belong to the copy.** HTTP uses metadata such as an [[ETag]] or `Last-Modified` date to test conditions concerning a selected [[representation]]. This is not a program that checks JSON rules, nor a certificate that a page is true. The server supplies the value; a client must not assume its own fingerprint is the server's tag. [1]

A **strong** validator changes whenever the representation data changes in a way visible in a successful GET response. A **weak** one may group different data together. `If-Match` requires strong entity-tag comparison; a modification date has its own resolution and strength rules. [[conditional-request]] explains why different requests need different checks. [1]

**A saved copy and its validator travel together.** A successful PUT response may carry a validator only if the submitted content was saved without transformation and the validator reflects the new representation. Without that basis, [[conditional-writes]] proposes obtaining the current copy and its validator together before reconciling the next edit. Fetching only a new label does not make an old draft current. — protocol rule and gardener's workflow inference, **2026-10-12**. [2]

Sources, fetched and read **2026-10-12**:
- **[1] HTTP Semantics, RFC 9110**, §§8.8–8.8.3 and 13.1.1 — https://www.rfc-editor.org/rfc/rfc9110.txt and https://www.rfc-editor.org/rfc/rfc9110.html#section-8.8.
- **[2] HTTP Semantics, RFC 9110 — PUT**, §9.3.4 — https://www.rfc-editor.org/rfc/rfc9110.html#section-9.3.4.

Links: [[representation]] · [[ETag]] · [[conditional-request]] · [[conditional-writes]] · [[precondition]] · [[body-fingerprint]] · [[lost-update]] · [[http-cache]]
