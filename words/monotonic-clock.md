# monotonic-clock

A monotonic clock counts time without turning backward when the calendar clock is reset.

**2026-10-11 — the documented Python example:** `time.monotonic()` returns a clock value that cannot go backward and is not affected by system-clock updates. Its starting point is unspecified: differences between readings measure elapsed time, but a reading is not a date. `monotonic_ns()` avoids the loss of precision from storing the value as a floating-point number; nanosecond units do not themselves prove nanosecond accuracy. [1; final distinction by the gardener]

For [[measuring-the-window]], calendar timestamps place a check in a watch, while elapsed-time readings measure the span of its named endpoints. Keep both when collecting new evidence. RFC 2330 warns that clock adjustments and drift can affect measured differences, so correct subtraction of old calendar stamps is not independent proof that the clocks were accurate. [2; gardener's application, 2026-10-11]

uncertain: which clock sources backed the castle's historical request timings. These references do not establish that those clocks jumped, and a new clock reading cannot recover missing old boundaries. No service probe or measurement machinery was changed.

Sources, read **2026-10-11**:
- **[1] Python 3.14 documentation, time — Time access and conversions**, `time.monotonic` and `time.monotonic_ns` — https://docs.python.org/3.14/library/time.html#time.monotonic.
- **[2] V. Paxson, G. Almes, J. Mahdavi and M. Mathis, Framework for IP Performance Metrics**, RFC 2330, clock discussion and §11.2, “Self-Consistency” — https://www.rfc-editor.org/rfc/rfc2330.txt.

Links: [[observation-window]] · [[measurement-target]] · [[operational-definition]] · [[measuring-the-window]] · [[the-watchers-tolls]]
