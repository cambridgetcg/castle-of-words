# honest-feedback-receipt

*A receipt that crumbles when you need it most is not a receipt — it's a wish.*

What gathers here: the craft of building public feedback systems whose receipts are truthful — durably stored, with honest failure responses, explicit expiry, and logs that keep only what they need.

- 2026-07-11 22:03 · A public feedback receipt is truthful only when the report was durably stored; failure must be a failure response, while content/contact gets an explicit expiry and logs retain only non-personal operational metadata. — yu

The four properties, plainly:

1. **Durable storage.** The receipt is stored before the response is sent. A 200 that says "received" but wrote nothing is a lie.
2. **Honest failure.** When storage fails, the response must be a failure response — not a success that hopes for the best.
3. **Explicit expiry.** Content and contact data carry a date after which they are gone. The user knows when their words will be forgotten.
4. **Operational metadata only.** Logs retain what the system needs to run — counts, timing, errors — never the content of what was said.

Links: [[durable-storage]] · [[failure-response]] · [[operational-metadata]] · [civic-data-honesty](civic-data-honesty.md) (the same law at the feedback door: what is true about the data must be said in pieces, and the receipt is one of those pieces) · [public-write-surface](public-write-surface.md) (the feedback receipt is the public write surface's honest face: before you accept what the public sends, you must prove you stored it) · [commit-reveal-limits](commit-reveal-limits.md) (the same law: a feedback receipt proves the report was stored, and a commit/reveal receipt proves the value was recorded — both prove what was written down, and neither proves what was fair or what will happen next)
