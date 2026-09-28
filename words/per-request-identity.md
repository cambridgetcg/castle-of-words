# per-request-identity

*The same blank form, signed fresh every time it is handed out.*

For a child: imagine a library card that is always the same card, but every time you ask for it the librarian writes today's date and a new serial number on it. The card doesn't change — but no two cards are ever exactly alike, because each one carries the moment it was given.

A **per-request-identity** is the layer of a served page that is stamped fresh on every request — a timestamp, a one-time id, a random token, a honeypot UUID — on top of a template that never changes. The page's *structure* (its headings, its prose, its worker script) is one build served to everyone; the *identity* (who this copy was handed to, and when) is re-signed with each serve. A reader counting the page's markers will find the identity fields always differ, and may — if the reader is careless — mistake the identity for a second state of the page. The honest reading separates the two: the template is the gate's configuration; the identity is the gate's clock. First measured in the castle at the Anubis two-state door (2026-09-27): byte-for-byte diff of two cached challenge pages found the *only* differences were the per-request identity fields; the "two states" were one template, signed twice.

Links: [[knock]] (one serve, one signing) · [[flicker]] (the kind of change per-request-identity is *not*) · [[gate-state]] (the cadence word whose instrument-clause now names it) · [[knock-ledger]] (the table whose two-counts artifact it settled) · [the-two-faces-one-build](../rooms/the-two-faces-one-build.md) (the room where the word was earned)
