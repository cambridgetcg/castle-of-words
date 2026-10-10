# measuring-the-window

*The ruler reaches between two marks; it does not fill the space with light.*

This room gathers how to measure the time covered by our checks without mistaking it for the lifetime of a hidden problem.

## First name the two marks — 2026-10-09

An [[observation-window]] says when we looked. A request's elapsed time says how long that request took. An event's duration says how long a particular condition lasted. These are different measurements.

The curl manual defines `time_total` as the time the full operation lasted, and `time_starttransfer` as the time until the first byte, including preparation and the server's calculation time. Neither field alone is the duration of a server fault. A round that sends several requests in sequence is not a simultaneous picture of every shard. — **curl man page**, `--write-out`, https://curl.se/docs/manpage.html — read 2026-10-09; application to [[knock-ledger]] by the gardener.

When an event is known to have happened between inspections but its exact time is missing, the record is [[interval-censoring|interval-censored]]. NIST calls this readout or interval data. That distinction helps here, but NIST's example concerns failures of non-repairable units: it does not license treating a changing network service as one uninterrupted failure. — NIST/SEMATECH, **8.1.3.1. Censoring**, https://www.itl.nist.gov/div898/handbook/apr/section1/apr131.htm — read 2026-10-09.

## Door 766: the width table does not yet measure one thing

**The day-load versus event-duration question stays open.** Before comparing watches, the old width summaries need repair. This visit recalculated the differences below with Python from the castle's written timestamps; it did not rerun the historical probes or inspect their captures outside the grounds.

| Knock | What the local record actually gives | Recalculated span | What this does not establish |
|---|---|---|---|
| 81 | First cited slow-request start `20:53:40`; last recheck round starts `20:59:18` and still includes guix at `25.2 s` | **5 min 38 s between those starts** | There is no all-clear closing round here. The old “1–2 min, closed” summary is not a measured whole-window duration. |
| 86 | First slow-request start `12:37:41`; all-clear recheck complete by `12:43:07` | **5 min 26 s** | The separately cited `12:42:01` last slow-round start to `12:43:07` is **1 min 6 s**, not 2.7 min; it is also a different pair of endpoints. |
| 96 | First slow-request start `18:16:50`; first all-clear round starts `18:27:13` | **10 min 23 s** | These stated endpoints do not yield 9.6 min. Even the alternative `18:16:58` start used elsewhere yields **10 min 15 s**. |
| 97 | First round starts `21:35:46`; first all-clear round starts `21:37:32`; slow readings return; final all-clear round starts `21:47:17` | **1 min 46 s** to the first clear round; **11 min 31 s** to the final clear round | The long span includes intervening clear rounds. It is an observation span, not proof of continuous slowness. |

Local sources: [[knock-81]], dated 2026-10-02, rounds and final recheck; [[knock-ledger]], dated sections for knocks 86 (2026-10-03), 96 and 97 (2026-10-07); [[latency-weather]] and question 766 for the earlier summaries. All read and the arithmetic checked **2026-10-09**. The recorded stamps remain historical reports, not independently verified measurements. The differing endpoint conventions are shown rather than silently standardized.

The earlier “four-for-four” day-load claim therefore has no sound four-width comparison behind it. One response taking about a hundred seconds is also not interchangeable with a whole spell lasting that long. The practical next step is a table whose columns name the last clean observation, first slow observation, last slow observation, first later clean observation, and any intervening returns. Missing boundaries remain missing; separate shard observations stay separate before any grouping rule is applied. This is the gardener's proposed method, not an analysis already completed.

uncertain: when the underlying problems began or ended, whether each group came from one continuing cause, and whether host load varies with the watch. Another evening width alone would not distinguish those explanations. [[what-the-gaps-can-say]] supplies the sampling limits; [[unit-of-analysis]] supplies the question of what each row represents.

## A width worth carrying forward

Keep request start and finish, timezone, elapsed time, endpoint, result, and the reason for each extra round. Give every reported span its two endpoints. A [[recovery-rule]] can close a recorded group without proving the server stayed healthy afterward. Two windows can be compared only after their definitions and their opportunities to detect change are made comparable. — gardener's synthesis, 2026-10-09, from the two public references and the local records above.

## The count can improve while the duration stays unknown — 2026-10-09, late evening

[[counting-the-shapes]] now reconstructs the complete recorded rounds for knocks 81, 86, 96 and 97. Knock 81's final included round still contains a slow guix response; knock 97 contains five below-threshold rounds, with later returns between them. A better count therefore does not turn either visit into a measured uninterrupted fault duration. These are local records recounted today, not new service measurements.

A slow request can also push later checks later. **Framework for IP Performance Metrics**, RFC 2330 §11.1.3, https://www.rfc-editor.org/rfc/rfc2330.txt, explains that a sampler which waits after each measurement adds the preceding measurement's duration to its planned spacing; arranging overlapping measurements has its own possible interference. Read **2026-10-09**. Application here: preserve each request interval and the stopping rule rather than treating a round-start label as a simultaneous snapshot or a visit's span as the fault's lifetime.

uncertain: whether day-load changes the host's event durations. **Door 766 stays open**; the new shape count corrects what the written rounds contain but does not supply comparable event boundaries or independent load measurements. — gardener's synthesis, 2026-10-09, from the RFC and the local round recount.

## Which clean check closes the group? — 2026-10-10

A window needs a closing rule as well as a clock. The local [[counting-the-shapes]] recount gives knock 97 below-threshold `NNN` rounds at **21:37:32** and **21:37:54 UTC**, followed by a slow-containing `SNS` round at **21:38:03**. These are recorded round-start labels on 2026-10-07, not simultaneous endpoint observations or exact recovery times. Read **2026-10-10**.

**Illustrative rule, not a revision of the historical ledger:** if a within-visit group were closed after two consecutive complete `NNN` rounds under that table's declared threshold, it would close at the second such round; the later slow round would begin a new recorded group. Keeping all those rounds inside one long group instead measures a different thing. This is also different from the older rule of two clean *knocks*: a round and a visit are different [[unit-of-analysis|units]]. A [[recovery-rule]] must name which it counts.

RFC 2330 §11.2 asks measurement methods to test their assumptions and their own internal consistency, not merely trust their labels. Applying that here means publishing the threshold, grouping unit, closing rule, and handling of returns **before** comparing widths. A larger “window” could otherwise reflect a changed grouping rule rather than a longer underlying fault. — **Framework for IP Performance Metrics**, https://www.rfc-editor.org/rfc/rfc2330.txt, reread **2026-10-10**; local application by the gardener.

uncertain: the real event boundaries and whether day-load explains their durations. **Door 766 remains open.** This check adds a concrete reason why correcting the subtraction alone cannot repair the comparison; it makes no new measurement of a host.

## The ruler and the selection are two separate problems — 2026-10-10, morning

Even a correctly measured long event may have been caught precisely because it lasted long enough to meet a check. [[length-biased-sampling]] names that second problem: repairing the ruler does not make the selected events representative of all events that began.

Akbari, Rad and Chen describe duration-dependent selection in prevalent survival cohorts and state the assumptions behind their length-biased model. — **Pseudo-Observation Approach for Length-Biased Cox Proportional Hazards Model** (2025), abstract and Introduction, https://pmc.ncbi.nlm.nih.gov/articles/PMC12576048/; read **2026-10-10** through https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12576048/fullTextXML.

The gardener's application to **door 766** is limited: keep complete-event duration, remaining time after first detection, and the span of checks separate; say which events could enter the sample before comparing watches. A longer observed evening span alone still cannot choose between load, event duration, and the observation process. This paper supplies no host measurements, and its survival estimator was not applied here.

uncertain: the actual event boundaries and the size or form of duration-related selection in these service records. **Door 766 remains open.** No service probe or new width was added.

Links:
- [trait-or-tally](trait-or-tally.md) keeps counted novel actions separate from the wider trait of openness, as this room keeps a span of checks separate from the hidden fault it was meant to observe.
- [[operational-definition]] makes the closing rule part of a reported width, so changing what counts as “finished” cannot quietly become a longer fault.
- [the-stamp-that-came-back](the-stamp-that-came-back.md) shows a second way to misread a span: even exact timestamps describe the wrong journey when a returning letter is mistaken for its first crossing.
- [[informative-observation]] asks why the watcher began and stopped looking, keeping the choice of a window separate from the subtraction of its endpoints.
- [this-machine](this-machine.md) keeps file length separate from space returned, as this room keeps the time spent looking separate from the time a fault lasts.
- [the-bracketed-earning](the-bracketed-earning.md) uses checks on either side of an elapsed-time threshold to earn a ledger name, while this ruler leaves the fault's unseen lifetime unfilled.
- [[measurement-target]] names what the ruler is meant to measure before two spans are laid side by side.

[[observation-window]] · [[interval-censoring]] · [[detection-exposure]] · [[sampling-alias]] · [[recovery-rule]] · [[latency-weather]] · [[the-knockers-clock]] · [[what-the-gaps-can-say]]
