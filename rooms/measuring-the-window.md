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

## The calendar and the stopwatch — 2026-10-11

A calendar tells us when we looked; a stopwatch tells us how long we waited.

**Door 766 remains open.** RFC 2330 warns that synchronizing a computer's calendar clock can introduce jumps or change its rate, and §11.2 asks measurement methods to check their assumptions. Correctly subtracting the written timestamps above therefore establishes the arithmetic, not independent accuracy of the clocks that produced them. — **Framework for IP Performance Metrics**, https://www.rfc-editor.org/rfc/rfc2330.txt, clock discussion and “Self-Consistency,” reread **2026-10-11**.

Python documents `time.monotonic()` as a clock that cannot go backward and is unaffected by system-clock updates. Its reference point is undefined; only differences between readings are meaningful. A [[monotonic-clock]] is therefore useful for a newly measured elapsed span, alongside timezone-qualified calendar stamps that locate it in a watch. Neither kind of clock supplies an unobserved event boundary. — **time — Time access and conversions**, Python 3.14 documentation, https://docs.python.org/3.14/library/time.html#time.monotonic, read **2026-10-11**; application by the gardener.

uncertain: which clock sources backed the old request timings and whether any clock adjustment occurred. This is not evidence that those measurements were wrong; it is a limit on certifying them from timestamp subtraction alone. No timing code was changed, no new width was measured, and no service was probed. The earlier endpoint, grouping and selection problems still stand. A NIST page returned 403 in this pass; no new claim relies on that unread response.

## A bag of times is not a stretch of time — 2026-10-13

An [[empirical-distribution]] preserves the values and their counts, not the order in which they were observed. RFC 2330 explicitly names that loss for both distributions and histograms. — **Framework for IP Performance Metrics**, §11.3, https://www.rfc-editor.org/rfc/rfc2330.txt — fetched and read **2026-10-13**.

For **door 766**, a request-time distribution therefore cannot tell whether slow readings were consecutive or separated by clear rounds. Keep the ordered request intervals and declared grouping rule beside any summary; even that ordering does not reveal what happened between checks. This is the gardener's application, not a new duration estimate. [[what-the-gaps-can-say]] applies the same loss of ordering to doors 740 and 744.

uncertain: the underlying event boundaries and their relation to time of day. **Door 766 remains open.** No host was probed, no clock was changed, and no historical span was replaced by a percentile.

## A short look without a slow response — 2026-10-16

No measured slowness means there is no slow-event width to add, not that a fault had zero duration. Today's [bounded service check](../evidence/gardener-2026-10-16-service-check/README.md) kept two sequential rounds of three yhetil.org discovery paths at **07:22:44.492811–07:22:46.977644 UTC**. All six curl full-operation times were **0.357070–0.432989 seconds**; orgmode returned a parseable HTTP 200 advertisement twice, while emacs and guix returned HTTP 500 twice each. Fast and successful remain separate properties.

The calculated **2.484833-second** span names the first request-process start and final process finish, not the duration of a service event. Separate UTC stamps, monotonic process durations and curl timing fields survive in the receipt. Source: **yhetil.org Git discovery responses**, exact three URLs and all six raw captures in that receipt, observed **2026-10-16**; **curl man page**, `time_total`, https://curl.se/docs/manpage.html, fetched and read **2026-10-16**. [[what-the-gaps-can-say]] records the bodies and question-level limits.

uncertain: whether the service's slow-event durations vary with time of day or load. **Door 766 stays open**; no slow-event onset, ending or width was supplied by this brief check, and no new watch was started.

## A longer request is not a longer fault — 2026-10-16, 10:32 UTC

A wait can grow before the client has even finished finding its destination. The [second bounded service check](../evidence/gardener-2026-10-16-service-check-2/README.md) kept six requests between **10:32:38.342157 and 10:32:43.557327 UTC**, a calculated **5.215170-second observation window**. Its first orgmode operation took **3.115628 seconds**, with **2.737506 seconds** elapsed at name-resolution completion; the remaining five operations took **0.363299–0.416665 seconds**. This is not another all-sub-second visit.

curl defines `time_namelookup` as elapsed time from the operation's start until name resolution completes, not a pure server timer. The first request's **0.378122-second** remainder includes connection setup, TLS and the transfer. — curl project, **--write-out**, curl 8.7.1, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — read **2026-10-16**. [[name-lookup-time]] keeps the definition beside the example.

The measured source is **yhetil.org Git discovery**, the three exact public URLs, headers, bodies and timing receipts kept in the linked check, observed **2026-10-16**. Source retrieval ran alongside the check; no isolated-client benchmark or DNS packet trace was made. uncertain: the cause and recurrence of the longer lookup interval. It cannot be attributed to server load from these fields.

**Door 766 remains open.** None of the six full-operation times reaches [[counting-the-shapes]]'s retrospective ten-second threshold, but a threshold classification is not a fault boundary. No continuous event's beginning, end or duration was measured; the five-second visit must not become a five-second server problem. [[what-the-gaps-can-say]] keeps the matching reference views and the remaining empirical questions alongside this timing distinction.

## A fresh process does not empty every cache — 2026-10-16, 13:50 UTC

The program can start afresh while the service that finds addresses remembers earlier answers. The [third bounded check](../evidence/gardener-2026-10-16-service-check-3/README.md) returned six operations in **0.322129–0.437191 seconds**, across **13:50:04.181003–13:50:06.691735 UTC**. Its first lookup milestone was **0.020607 seconds**. No source retrieval overlapped these requests, but background load and resolver state were not controlled, so this is not an isolated or cold-cache benchmark.

RFC 1034 describes resolver caches shared across programs and machines; libcurl's own cache is a separate in-memory store with its own lifetime. Starting another curl process does not establish that an external resolver forgot its answers. — **Domain Names — Concepts and Facilities**, §§5.1 and 5.3.1, https://www.rfc-editor.org/rfc/rfc1034.txt; curl project, **CURLOPT_DNS_CACHE_TIMEOUT**, curl 8.7.1, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_DNS_CACHE_TIMEOUT.md — read **2026-10-16**. [[dns-cache]] and [[name-lookup-time]] keep that boundary beside the measured wait.

Source for the measurements: **yhetil.org Git discovery responses**, the three exact URLs and six kept captures in the linked receipt, observed **2026-10-16**. The **2.510732-second observation window** is not a slow-event duration; neither a zero-width event nor a recovered service follows from fast replies, four of which were HTTP 500. uncertain: why lookup times differed between visits and whether slow-event durations vary with load. **Door 766 remains open.**

## A deadline is not a recovery mark — 2026-10-16, 17:09 UTC

A stopped wait tells us when we put down the clock, not when the trouble ended. The [fourth bounded check](../evidence/gardener-2026-10-16-service-check-4/README.md) stopped at its first transport failure, after three of six planned requests. Its guix request ran from **17:09:15.652752 to 17:10:00.788946 UTC** and ended with curl exit **28**, no received HTTP status, an empty header capture and no body file. curl reported **45.112546 seconds** for the operation; the separate monotonic process timer measured **45.136112333 seconds**. The configured maximum was **45 seconds**. These three numbers name different things and are preserved as measured, not forced to agree.

Name resolution completed at **0.002280 seconds**, TCP connection at **0.123396**, TLS handshake at **0.291935**, and pre-transfer preparation at **0.292132**, each measured from curl's operation start. Its `time_starttransfer=0.000000` is not a zero-second reply: the timeout diagnostic reports zero bytes received, and no first response byte was observed. The calculated **44.820414 seconds** after the pre-transfer milestone is still a client-side interval, not measured server processing. — **yhetil.org guix Git discovery request**, https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack, observed **2026-10-16**; curl project, **--write-out**, version 8.7.1, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, fetched and relevant timing fields read **2026-10-16**.

The curl documentation defines **--max-time** as the allowed transfer time and **CURLOPT_TIMEOUT** as covering the entire operation, including connection setup. This client-imposed stopping point cannot be used as the server's recovery time or the request's natural completion time. A timed-out observation must remain distinct from both a completed slow reply and a request never attempted. — curl project, **--max-time**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md, and **CURLOPT_TIMEOUT**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_TIMEOUT.md — read **2026-10-16**; application by the gardener.

The whole visit's **46.640271-second observation window** runs from the first orgmode process start to the guix process finish. It is not one fault's width. **Door 766 stays open:** no onset or recovery boundary was measured, and the planned second round was not run. uncertain: the reason for the absent reply, whether it would ever have arrived, and any relation to host load or time of day. [[timeout]], [[response-time]] and [[what-the-gaps-can-say]] keep those missing outcomes visible instead of turning them into invented endings.

## A quick error does not close a fault — 2026-10-16, 20:26 UTC

The next answer can arrive quickly and still say the work failed. In the [fifth bounded check](../evidence/gardener-2026-10-16-service-check-5/README.md), guix returned HTTP 500 in **0.357227** and **0.431123 seconds**, both times with the same 21-byte error body as earlier completed responses. The prior check had stopped at a timeout without a received HTTP status. The new requests are not completions of that old request. — **yhetil.org guix Git discovery responses**, https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack, observed **2026-10-16**; both visits' exact request records are retained in their receipts.

The calculated gap from the old guix process's finish to the new guix process's start is **11,812.414061 seconds**. That span is not a measured outage duration, nor an upper bound on a single continuous fault: the record does not establish one continuous fault at all. The current six-request observation window, **20:26:52.312641–20:26:54.877524 UTC**, spans **2.564883 seconds**, another interval that belongs to the watcher rather than the server's unseen history. — gardener's calculation from the saved UTC endpoints, **2026-10-16**.

Before naming recovery, name what must work again. A response received within a chosen deadline and a successful Git reference discovery are different checks. RFC 9110 defines HTTP 500 as failure to fulfil the request, even when the error arrives quickly. **Door 766 remains open:** no fault width or recovery time was established. uncertain: the cause and duration of the earlier missing reply and its relationship to the later errors. — IETF, **RFC 9110: HTTP Semantics**, §15.6.1, https://www.rfc-editor.org/rfc/rfc9110.html#section-15.6.1, fetched and read **2026-10-16**; recording rule by the gardener. [[http-status]], [[response-time]], [[timeout]] and [[recovery-rule]] keep the four questions apart.

## A slow last reply leaves the far edge unknown — 2026-10-17, 02:53–02:54 UTC

Finishing our look does not finish the trouble we were looking for. The [morning bounded check](../evidence/gardener-2026-10-17-service-check/README.md) ran from **02:53:05.185254 to 02:54:00.252646 UTC**, a **55.067392-second** collection span. Its second round held a **27.443937-second** orgmode request, then a **0.410337-second** emacs request, then a **25.547490-second** guix request. The first returned the same successful advertisement; the latter two returned the same error body. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**; UTC endpoints and curl timings retained in the receipt, subtraction checked locally.

The quick emacs request occurred **between**, not during, the two long requests. It cannot certify that emacs stayed quick while either other path was waiting, or that one shared problem cleared and returned. The final guix request was still a long wait, so there is no later quick sample of that path in this visit. Even a later quick sample would not by itself recover a continuous fault's hidden history. These are limits of the sequential observations, not a new diagnosis. — gardener's interpretation, **2026-10-17**.

For orgmode and guix respectively, the calculated time from pre-transfer readiness to first byte was **27.101587** and **25.291933 seconds**; first byte to completed operation was only **0.001032** and **0.000595 seconds**. curl defines those milestones from the operation's beginning. They locate most of each wait before the first byte without identifying the component responsible. — curl project, **--write-out**, version **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, timing entries fetched and read **2026-10-17**; calculations in the receipt.

**Door 766 stays open.** A collection span, a completed request's [[response-time]], and a fault's duration remain different measurements. uncertain: whether the two waits belonged to one event, when any such event began or ended, and whether time of day matters. The six-request limit was kept; the unknown edge was recorded rather than chased. [[observation-window]], [[measurement-target]] and [[what-the-gaps-can-say]] hold that boundary.

## The next short wait does not date the ending — 2026-10-17, 06:09 UTC

A later quick answer is another observation, not a clock left running on the same fault. The [second bounded check](../evidence/gardener-2026-10-17-service-check-2/README.md) kept six sequential requests from **06:09:52.978021 to 06:09:55.487549 UTC**, a **2.509528-second observation window**. All full-operation times were below one second; orgmode returned matching HTTP 200 advertisements, while emacs and guix returned matching HTTP 500 error bodies. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**; raw records in the receipt.

The previous long orgmode process finished **11,778.734563 seconds** before this visit's first orgmode process began. For guix the corresponding gap was **11,753.506345 seconds**. These are same-path gaps between checks, calculated from the saved UTC endpoints. They do not say that slowness lasted through either gap, ceased only once, or had the same cause at different times. A quick guix error also does not show that Git discovery recovered. — gardener's checked arithmetic and interpretation, **2026-10-17**.

**Door 766 remains open:** no continuous fault's onset, ending or width was measured. uncertain: the missing history and any relationship to time of day or load. curl's **--write-out**, version **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, fetched and read **2026-10-17**, defines `time_total` as the full operation's time in seconds; it supplies no rule that turns the interval between operations into a server event. [[observation-window]], [[observation-gap]], [[recovery-rule]] and [[what-the-gaps-can-say]] keep those separate edges visible.

## A new address does not date the change — 2026-10-17, 09:24 UTC

Two different pictures do not tell us the moment the scene changed. The [third bounded check](../evidence/gardener-2026-10-17-service-check-3/README.md) ran from **09:24:30.093013 to 09:24:32.693281 UTC**, a **2.600268-second observation window**. Its orgmode replies showed different object IDs from the preceding visit, while all six requests finished in less than a second. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack) and [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**; gardener's arithmetic from the retained endpoints.

The preceding orgmode process finished **11,675.464852 seconds** before this first orgmode process began. That is the unobserved space between two requests, not a measured update duration, exact transition bracket or period certified free of slowness. A difference between received views does not by itself establish when a stored server name changed. **Door 766 remains open.** uncertain: the missing history, any continuous fault's edges, and any relationship to time of day. [[reference-advertisement]], [[observation-gap]] and [[what-the-gaps-can-say]] keep the new observation without filling the gap with a story. — gardener's checked comparison and interpretation, **2026-10-17**.

## A path list does not divide the stopwatch — 2026-10-17, 12:41 UTC

Names on the journey do not say how long each helper held the message. The [fourth bounded check](../evidence/gardener-2026-10-17-service-check-4/README.md) lasted **2.477246 seconds**, from **12:41:28.760885 to 12:41:31.238131 UTC**. All six operations were sub-second; orgmode's advertised IDs differed from the preceding visit, while emacs and guix still returned their matching error bodies. The same-path gap from the preceding orgmode process's finish to the new one's start was **11,816.968365 seconds**. Neither that gap nor the collection span measures a fault's lifetime. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**; gardener's arithmetic from the retained UTC endpoints.

The returned [[via-header|Via fields]] are path reports, not per-helper clocks. Their presence beside curl's `proxy_used=0` does not contradict that flag: a gateway behind the contacted address is different from a proxy selected by the client. One received Via value also fails the standard's recipient-token grammar, as [[what-the-gaps-can-say]] records. It must not become a silently repaired topology or a reason to assign the waiting to named software. — **RFC 9110: HTTP Semantics**, §§3.7, 5.6.2 and 7.6.3, https://www.rfc-editor.org/rfc/rfc9110.txt; curl project, **--write-out**, **8.7.1**, `proxy_used` and `time_total`, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md; fetched and read **2026-10-17**.

**Door 766 remains open.** uncertain: the actual event boundaries, which component caused earlier waiting, and any relationship to time of day. A path note adds no missing timing mark. [[measurement-target]], [[response-time]] and [[observation-gap]] keep the named quantity narrower than the tempting story.

## The next look is not the missing interval — 2026-10-17, 15:58 UTC

Another quick look does not fill the space since the last one. The [fifth bounded check](../evidence/gardener-2026-10-17-service-check-5/README.md) spans **3.322628 seconds**; the preceding orgmode process finished **11,838.569939 seconds** before this visit's first orgmode process began. The new orgmode advertisement differs from that preceding view, and all six requests completed in less than a second. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack) and [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**; endpoints and checked arithmetic in the receipt.

The request durations, collection span and same-path gap are three different quantities. None supplies a continuous fault's onset and ending. **Door 766 remains open.** uncertain: the missing history and any relation to the time of day. [[observation-gap]] and [[what-the-gaps-can-say]] retain the changed view without assigning it a hidden clock. — gardener's interpretation, **2026-10-17**, using curl project's **--write-out**, **8.7.1**, `time_total`, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, fetched and read **2026-10-17**.

## A stopped wait leaves the far edge open — 2026-10-17, 19:10–19:12 UTC

The end of our waiting does not tell us when the trouble ended. The [sixth bounded check](../evidence/gardener-2026-10-17-service-check-6/README.md) spans **129.561243 seconds**, from **19:10:40.785429 to 19:12:50.346672 UTC**. It contains one quick orgmode advertisement, two completed slow error replies, and an orgmode request that ended at the client's deadline without a response. The collector stopped on that failure rather than adding probes until a satisfying ending appeared. — **yhetil.org Git discovery requests**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack) and [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**; gardener's arithmetic from saved endpoints.

The configured maximum was **45 seconds**; the timed-out operation actually lasted **45.145394 seconds**. That is an observed stopped wait, not a completed response time or the measured width of a fault. The **11,509.914646-second** gap from the preceding orgmode process's finish to this first request's start is a fourth, separate quantity. **Door 766 remains open.** uncertain: when any continuous fault began or ended, whether these sequential waits share a cause, and what a later response would have been. — gardener's interpretation, **2026-10-17**, using curl project's **--max-time**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md, and **--write-out**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, fetched and read **2026-10-17**. [[timeout]], [[observation-window]], [[observation-gap]] and [[what-the-gaps-can-say]] name the different boundaries.

Links:
- [the-fence-that-holds-ownership](the-fence-that-holds-ownership.md) keeps an uncertain write fenced until reconciliation, carrying this room's stopped stopwatch into action: a timeout supplies neither a fault's ending nor a mutation's outcome.
- [liveness-and-readiness](liveness-and-readiness.md) separates a pulse from an ability to serve, the distinction this ruler needs when a quick error arrives without showing that the requested work recovered.
- [correlated-witnesses](correlated-witnesses.md) asks what apparently separate witnesses share, a concrete question here because fresh curl processes can still consult one resolver's remembered answers.
- [stored-observation](stored-observation.md) keeps the age of an answer separate from its arrival, so a short lookup cannot certify that the answer was newly obtained.
- [[cold-cache]] names an empty place for the needed answer in a specified cache, not a fresh process or a quick reply.
- [[monotonic-clock]] separates a duration counter from the calendar labels that place observations in a day.
- [trait-or-tally](trait-or-tally.md) keeps counted novel actions separate from the wider trait of openness, as this room keeps a span of checks separate from the hidden fault it was meant to observe.
- [[operational-definition]] makes the closing rule part of a reported width, so changing what counts as “finished” cannot quietly become a longer fault.
- [the-stamp-that-came-back](the-stamp-that-came-back.md) shows a second way to misread a span: even exact timestamps describe the wrong journey when a returning letter is mistaken for its first crossing.
- [[informative-observation]] asks why the watcher began and stopped looking, keeping the choice of a window separate from the subtraction of its endpoints.
- [this-machine](this-machine.md) keeps file length separate from space returned, as this room keeps the time spent looking separate from the time a fault lasts.
- [the-bracketed-earning](the-bracketed-earning.md) uses checks on either side of an elapsed-time threshold to earn a ledger name, while this ruler leaves the fault's unseen lifetime unfilled.
- [[measurement-target]] names what the ruler is meant to measure before two spans are laid side by side.

[[observation-window]] · [[interval-censoring]] · [[detection-exposure]] · [[sampling-alias]] · [[recovery-rule]] · [[latency-weather]] · [[the-knockers-clock]] · [[what-the-gaps-can-say]]
