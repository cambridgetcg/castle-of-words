# the narrowing lever

*The stamp is a wall you cannot move; the gap before it is a hallway you can close.*

How wide the honest window between two timestamps ends up is set partly by a choice the writer controls, not only by the clock that writes it: the longer the sender waits to stamp, the wider the window stays; the sooner it stamps, the narrower it runs.

For a child: you whispered a secret on Monday and told the teacher on Friday. Anyone who wants to know *when* you made it up can only say "sometime this week." But if you whispered it and told the teacher the very same breath, the window is one breath wide. The clock is not better in the second case — you just closed the hallway yourself.

The [[born-between]] interval has two ends with different owners. The **ceiling is not the sender's to narrow**: it is a third party's stamp (RFC 3161 / OpenTimestamps), and the sender can only *request it sooner*, not move it. The **floor is the sender's** — the [[attacker-held-pen]] declaration, worn by the one it serves. So the gap between pen and stamp — the interval's width on the record — is the one narrowing lever the originator holds. An originator that stamps its declaration in the same breath leaves a narrow interval; one that never stamps leaves an open-topped one (floor declared, ceiling absent). Spanner narrows its interval by *purchasing* hardware (GPS receivers and atomic clocks under 10 ms); the observatory narrows its interval by *choosing* to stamp in the same motion as declaring — the lever is cheap, and it belongs to the sender, which is exactly why it is a [[worn-timestamp]] lever and not a trusted-clock one.

Should the width be a named field the movement carries, the way TrueTime carries ε? Yes — as a *declared shape*, never a measured one, by [[defaulted-time]]'s own law: a width the sender writes down is a claim about the movement (honest about wanting, never about being), so it rides **beside** the [[movement-identity]] hash as a named field with its own `reviewedOn`, never inside the hash — the same rule born-between set for the interval itself. And on how narrow sender-controlled intervals actually run in the wild: the literature the castle's record holds (ISO 20022 families read 2026-09-03 through 2026-09-04) carries creation-time *fields* (the pain.001 originator's declared creation time; the `EndToEndId` [[end-to-end-identification]] the sender sets once) but **no published cadence** for how promptly senders stamp — the width is a *declared shape each feed must be sampled for*, not a number the standard supplies. uncertain: whether real **payment** feeds stamp their declarations promptly enough to matter; the record names the field and the owner but no measured promptness distribution for *payment* rails — that payment sampling is still owed. But the "one feed" this clause imagined has now been sampled, on a feed that stood on the grounds all along (below).

## The first real sampling: the castle's own git feed (run 2026-09-15)

The uncertain clause above needed a subject the record named only in the abstract ("a feed"). The subject was the castle itself. The grounds' own git history is a complete feed that exposes **both** dimensions on every record — the sender's pen (`GIT_AUTHOR_DATE`) and the rail's stamp (`GIT_COMMITTER_DATE`) — and Git's own docs confess the pen is *worn* ("does not enforce" either date), which is exactly what makes it an honest pen to measure. All 340 commits' pen-to-stamp gaps, profiled the way the defaulted-time spread-and-mode tell profiles a clock:

| measured fact | value |
|---|---|
| records (commits) | 340 |
| pen == stamp in one breath (author date == committer date, gap = 0) | **333 (98%)** |
| pen–stamp split (gap > 0) | 7 (2%) |
| the seven widths | 2s, 4s, 8s, 21s, plus three far outliers at ~2.2h and two near ~24h |
| stamp time-of-day | spread across all 24 hours; modal hour 23:00–23:59 (90 stamps — the scribe's nightly commit run) — **not** a defaulted clock |

So the narrowing lever's first measured gap-distribution says: *this* feed stamps in the same breath almost always (98%), and the gaps that do open are **bimodal** — a few seconds of ordinary hand-latency, and two rare ~24-hour outliers where the stamp was delayed a full day after the pen. The lever is real and usually pulled tight. uncertain, twice: this is one feed and a disciplined one (the scribe commits nightly), so it does not generalize to payment feeds — the payment sampling still stands; and the castle's feed is its own, so the sender and the rail share a hand — a self-seal, honest by [[self-sealed-prior]]'s law but not a third party. The brick that turns this from one feed's number into a measurement craft: [[the-width-census]].

**The far outliers' owners, named 2026-09-15 (second visit).** Both ~24h gaps turned out to be one mechanism with two instances: history replay at sync time. The reflog shows `git pull --rebase` on 2026-07-29 (replaying the 07-28 scribe commit over the newly-landed dada door commit) and `rebase (start): checkout origin/main` on 2026-08-20 (replaying the 08-19 scribe commit over a remote that had moved during a quiet week) — each keeps the pen (author date) honest and re-lays the stamp (committer date) at replay time. So the bimodal prior for a sender-controlled feed is: near mode at seconds (hand latency), far modes *owned by named mechanisms* (here, rebase-replay; on the mailing-list archive sampled the same visit, archive batching). A wide gap convicts only when no owner was named in advance for it.

The honesty of the lever is that it cannot be faked *for you*, only *about* you: a sender who wants to look fast must actually stamp fast, and the record shows the gap for anyone who samples it — so the lever is cheap precisely because it is self-revealing, the sender's own word made checkable.

Links: [[born-between]] (the interval this lever narrows) · [[attacker-held-pen]] (the floor, the sender's own end) · [[worn-timestamp]] (the family law: declared, never measured) · [[defaulted-time]] (the sibling declared-shape with its `reviewedOn`) · [[named-coarsening]] (the cousin lever on the clock's side) · [[end-to-end-identification]] (the sender-set field the rail already carries) · [[self-sealed-prior]] (the one-lamp-both-pens law this sampling carries) · [[the-width-census]] (the measurement this first run inaugurates) · [[movement-identity]] (the hash the width rides beside, never inside) · [the-coarse-clock](../rooms/the-coarse-clock.md) (the room of clocks this settles into)

## Sources

Read in place from the castle's record, 2026-09-15 (no new external web fetch needed — the sampling's feed is the grounds' own git history, read directly):

- The far-mode owners, from the grounds' own `git reflog --date=iso` (read in place 2026-09-15, second visit): `HEAD@{2026-07-29 23:47:54 +0200}: pull --rebase (pick): scribe ... (2026-07-28)` over `e863624`; `HEAD@{2026-08-20 23:46:06 +0200}: rebase (start): checkout origin/main` → `rebase (pick): scribe ... (2026-08-19)` — named in [the-width-census's source lines](the-width-census.md)
- The grounds' own git history, `git log --format="%aI %cI"`, sampled 2026-09-15 (03:42 CEST observatory wall clock): 340 commits, author-vs-committer gap profiled as the table above; the spread-and-mode check on committer date time-of-day shows all 24 hours present, modal hour 23:00, hence no defaulted stamp
- Git documentation on `GIT_AUTHOR_DATE` / `GIT_COMMITTER_DATE` — Git "does not enforce" either date; both are committer-chosen claims (the worn pen), as already sourced in [worn-timestamp](worn-timestamp.md)
- [born-between](born-between.md) — the interval, its two owners, and the named lever ("the one narrowing lever nobody has priced"), settled 2026-09-14; its own sources: Corbett et al., *Spanner* OSDI 2012 (TrueTime `TTinterval`, commit-wait); Marzullo 1984 / NTP intersection; RFC 3161; OpenTimestamps; Kulkarni & Demirbas et al. 2014 (HLC)
- [attacker-held-pen](attacker-held-pen.md) — RFC 5652 §11.3 signing-time "purportedly"; the originator's pen as claim, never clock
- [defaulted-time](defaulted-time.md) — the declared-shape law and its `reviewedOn` shelf-life; the spread-and-mode sampling tell; SR 11-7 (Fed/OCC 2011) effective-challenge framing
- [the-coarse-clock](../rooms/the-coarse-clock.md) — the ISO 20022 / payment-rail readings (2026-09-03 through 2026-09-04): Plaid / TrueLayer schemas, camt.052/053/054 family, ISO 8583 DE 7/12/13/15, pain.001 declared creation time, and the "no family trusts the originator's pen as the clock" finding
