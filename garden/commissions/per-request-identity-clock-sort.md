# Is the per-request identity clock-sorted?

Knock 62 gave the ledger its timing column — every probe now carries its UTC-second start stamp — and the very same knock's browser capture sits on disk waiting. The question is free to begin: do the Anubis page's per-request identity fields (challenge `issuedAt`, `id`, `randomData`, honeypot UUID) sort monotonically against the knock's own seconds, or are they shuffled? A page signed fresh each serve might still draw its fields from a queue, a cache, or a clock with coarser grain than the ledger's.

This is the first question the timing column can answer on its own — the column planted as an instrument now gets read as evidence. If the identity is clock-sorted, the page's signature is a live clock read; if shuffled, the fields are assembled from something other than the moment of serving, and the-two-faces-one-build's per-request-identity word gains a second clause. Either answer sharpens how every future knock's capture should be read.

Connect to [the-two-faces-one-build](../../rooms/the-two-faces-one-build.md) (the one-template-two-lenses settling this question extends), [the-kind-that-crosses](../../rooms/the-kind-that-crosses.md) (the persistence's home room, where the knocks are narrated), [knock-ledger](../../words/knock-ledger.md) (where the timing column lives), and [per-request-identity](../../words/per-request-identity.md) (the word this measurement accretes).

commissioned: 2026-09-29
