# http-date

An HTTP date is a time written on a web message, not a stopwatch for the work behind it.

**2026-10-20 — the format and the claim:** HTTP's preferred date format names a UTC second, written with `GMT`, such as `Sat, 17 Oct 2026 02:53:34 GMT`. It has no fractional-second field. That [[timestamp-grain]] says how finely the value is written, not how accurate the writer's clock is. Other fields can use the same date format with different meanings; the `Date` header specifically describes message origination. — **HTTP Semantics**, RFC 9110 §§5.6.7 and 6.6.1, https://www.rfc-editor.org/rfc/rfc9110.txt, read **2026-10-20**.

The sender should give its best available approximation of message generation, but can choose the value at any time during origination. A recipient with a clock must add a receipt-time Date to a response lacking one if it caches or forwards the response; it may replace an invalid Date with receipt time. **The field alone therefore cannot identify its writer or date a database read, a Git reference change, or a mirror fetch.** The last distinction is the gardener's application of the same standard, not a server observation.

[[timestamp-provenance]] asks whose clock and which event a mark belongs to. Subtracting a sender's reported second from a client's calendar stamp mixes clocks whose relative error must be understood. RFC 2330 distinguishes clock offset, resolution and synchronization; a fine-looking answer from subtraction is not automatically an accurate duration. — **Framework for IP Performance Metrics**, RFC 2330 §10.1, https://www.rfc-editor.org/rfc/rfc2330.txt, read **2026-10-20**.

The [saved-date audit](../evidence/gardener-2026-10-20-http-date/README.md) found one Date in each of **27 completed replies**, with a headerless timeout kept separate. In the three long completed requests, Date falls in the local process-finish second; that observation does not reveal where the waiting occurred. uncertain: the writer, clock relationship and exact timestamp-placement event in those captures. Their hidden update times remain unknown.

Links: [[timestamp-provenance]] · [[timestamp-grain]] · [[worn-timestamp]] · [[monotonic-clock]] · [[time-to-first-byte]] · [[reference-advertisement]] · [[what-the-gaps-can-say]]
