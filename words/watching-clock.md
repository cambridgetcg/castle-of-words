# watching clock

*Every rail keeps two clocks: one that watches the bell ring, one that books it at closing time.*

A watching clock is the timestamp a system writes at the movement's own instant — the match made, the card swiped, the transaction first seen. Its sibling, the accounting clock, is the timestamp the system writes for the books — the settlement date, the end-of-day statement, the balance snapshot. The watching clock is fine-grained and immediate; the accounting clock is coarse-grained and authoritative.

For a child: imagine a school with two people who note when the bell rings. One stands in the hall and writes the second it rings. The other writes in the logbook at the end of the day: "Monday — bell rang." Both are honest. But if you wanted to know whether two bells rang at the same moment, only the hall-watcher can tell you.

The split is universal across the message families the castle measured (settled 2026-09-04): banks keep camt.052 intraday reports (second-grain booking datetime) beside camt.053 end-of-day statements (day-grain); card rails keep ISO 8583's mandatory DE 12 local transaction time (hhmmss at authorization) beside DE 15 settlement date (day); the chain keeps the mempool's first-seen instant beside the block stamp (which Bitcoin's own wiki confesses is "accurate only to within an hour or two"); exchanges keep microsecond WebSocket ticks and trades exports beside day-scoped balance snapshots and account statements.

The law: the finest grain lives in the message built for watching, not the one built for accounting. For [[movement-identity]] the watching clock is the one to trust — but the watching clock's *owner* differs per family (the bank's booking engine, the terminal's clock, your own node's first sight of the transaction, the venue's match engine), so the universality of the split does not remove the per-feed sampling pass: the shape of the answer is general, whose hand holds the pen is not.

uncertain: whether any family exists where the accounting clock is *finer* than the watching clock — none of the four measured families shows it, but four is not all.

One more honest boundary, settled 2026-09-04: a watching clock's observer proves *seeing*, not *birth* — but no message family fixes that by letting the movement's originator sign the instant instead. The originator's signed time is an [[attacker-held-pen]]: a claim to log, never a clock to trust; and the third-party stamps (RFC 3161, OpenTimestamps) prove only that the datum existed *at or before* their mark — a ceiling, never a birth-certificate.

Links: [[timestamp-grain]] (the parent law: the grain is a property of the feed) · [[defaulted-time]] (the painted-on mark — the dishonest version of coarse) · [[attacker-held-pen]] (the originator-signed instant — the dishonest direction of fine: written by the one it serves) · [[movement-identity]] (the hash that should read the watching clock) · [the-coarse-clock](../rooms/the-coarse-clock.md) (the room where the split was first measured, and settled across families 2026-09-04)

## Sources

- Bitcoin Wiki, "Block timestamp" — https://en.bitcoin.it/wiki/Block_timestamp — read 2026-09-04: "A timestamp is accepted as valid if it is greater than the median timestamp of previous 11 blocks, and less than the network-adjusted time + 2 hours… block times are accurate only to within an hour or two"
- Kraken support, "How to export your account history" — https://support.kraken.com/articles/208267878-how-to-export-your-account-history — read 2026-09-04: export family splits into Trades ("detailed execution information"), Ledgers ("balance changes over time"), and Balances ("a snapshot of your balances at a specific date")
- Worldpay / FIS, "ISO 8583 Reference Guide V2.46" — https://docs.worldpay.com/assets/pdf/Worldpay_ISO_8583_Reference_Guide_V2.46.pdf — read 2026-09-04: DE 12 mandatory hhmmss beside DE 15 day-grained settlement (first read for [the-coarse-clock](../rooms/the-coarse-clock.md))
- Huntington developer portal, "CAMT.052" — https://developer.huntington.com/enterprisepayments/docs/camt052 — read 2026-09-04: entry-level second-grain booking datetime beside day-grain value date (first read for the-coarse-clock)
