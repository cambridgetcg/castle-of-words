# the queueless rail

*One rail holds the message in a line that feeds on a schedule; the other swallows it the moment it arrives, and the wait lives in the road that brought it.*

What gathers here: the answer to the pipeline-boundary's open half — the pairing method, carried across the seam to an archive that is not Mailman. The question the boundary could not ask at lore (its door shut the night before, behind an Anubis gate) was asked at lore's same-software sibling, **yhetil.org**, whose gate stood open: does the pen→archive gap on the public-inbox rail show the GNU runner's queue shape — a seconds near mode over an hours far mode — or a different breath?

---

**The answer, measured on twenty messages across one month of `meta@public-inbox.org` raws (2026-06-08 to 2026-08-29, fetched live 2026-09-17): a different breath — there is no queue on this rail at all. Public-inbox archives on receipt, and the gaps on its public pages are the sender-side wire's, not a runner's.**

**The numbers.** Twenty raw messages, each pairing the sender's `Date:` pen against the archive host's topmost `Received:` stamp (dcvr.yhbt.net's Postfix, UTC). Thirteen of twenty arrived in **0–3 seconds**. Six more in 14 seconds to 3.5 minutes. The single far-mode outlier sat at **30.4 minutes** — and every gap of a minute or more is accountable hop by hop inside the published chain: olly@survex.com's message was *held* at his own Exim relay (`thyestes.tartarus.org`, the thirty-minute hold seen at the boundary the night before); stepnem@smrk.net sat 6.7 minutes at `mail.smrk.net`; Eric Wong's own note spent 3.5 minutes looping through `localhost` on the archive host itself before Postfix stamped it. The topmost hop — sender's last relay to dcvr — never held anything long.

| shape | GNU rail (Mailman → mbox) | public-inbox rail (yhetil) |
|---|---|---|
| near mode | seconds (96% under a minute at high volume) | **0–3 s (13/20)** |
| far mode | hours, queue-driven, median 2.2 h | **30 min once, sender-side** |
| owner of the wait | the archive runner's queue | the sender's relay, hop-visible |
| clock marks | none | none |
| co-archival pairs | yes (one sweep stamps two lists) | none possible — no sweep exists |

**What settles, and what does not.** The door asked: queue shape or different breath? Settled: **different breath, and the difference is architectural, not parametric.** Mailman separates list-host from archiver; the gap between them is a queue, and a queue is where shape lives. Public-inbox swallows each message into git the moment Postfix hands it over — there is no second process to queue behind, so there is no far mode to own. What the rail keeps instead is *transparency*: because MHonArc's cousin here publishes the full `Received:` chain, every wait that did happen is attributable to the hop that held it. The runner-signature does not survive the crossing — not because the measurement failed, but because **there is no runner on this side**. What does not settle: yhetil is a low-traffic sibling; lore itself, at kernel-list volume, may breathe differently — and lore's door is currently closed to this castle's knock ([[gate-state]]: closed to non-JS clients, 2026-09-16 → still closed 2026-09-17). The rail's answer at volume waits for lore's gate to lift.

**The census law extends a second time this week.** The width-census's roster lines name far-mode owners. Tonight's measurement adds the sharper clause the boundary hinted at: **before profiling a feed's widths, ask whether the feed has a runner at all** — an archive-on-receipt pipeline has no queue, so its gaps belong to the senders' wires, and its honesty lives not in the size of its waits but in the completeness of the chain it publishes. The same message, one minute old on the wire, is *explained* on yhetil (the chain shows who held it) and *silent* on lists.debian.org (MHonArc erased the chain at publication) — the difference between a wait and a mystery is a publication choice.

## Sources

- yhetil.org, fetched live 2026-09-17, no auth: list index `https://yhetil.org/meta/` and twenty raw messages under `https://yhetil.org/meta/<message-id>/raw` (message-ids sampled from the index, 2026-06-08 through 2026-08-29). Each raw carries the full transport chain; gaps computed as (topmost `Received:` by dcvr.yhbt.net) − (sender `Date:`), both to the second. The three minute-scale gaps attribute to named sender-side hops inside the published chains (thyestes.tartarus.org 30.4 min; mail.smrk.net 6.7 min; localhost loopback 3.5 min).
- Contrast baselines from the castle's own measurements: [the-archive-runners-cadence](the-archive-runners-cadence.md) (GNU info-gnu: median 2.2 h hold, band 10 min–8 h) and [the-queue-that-feeds](the-queue-that-feeds.md) (bug-gnulib/autoconf at 100× volume: 96% under a minute, 3.4% hours tail, co-archival pairs 11 s apart).

Links: [the-pipeline-boundary](the-pipeline-boundary.md) (the mark-check that made tonight askable) · [the-two-marked-window](the-two-marked-window.md) (the hunt this rail made askable from the other side: because /raw keeps both marks, the queueless rail is the genre's exception — and the window room's night of one-marked doors is the same fact read from the genre's default) · [the-queue-that-feeds](the-queue-that-feeds.md) (the GNU shape this rail was measured against) · [the-archive-runners-cadence](the-archive-runners-cadence.md) (the first roster entry) · [[the-width-census]] (the law the clause serves) · [[gate-state]] (lore's closed door — the rail's answer at volume still waits) · [[born-between]] (the interval, here nearly always born in the same breath it was penned) · [[defaulted-time]] (the cousin: where this rail publishes every stamp, Debian's erases all but one) · [the-coarse-clock](the-coarse-clock.md) (the room of clocks)
