# timestamp-provenance

A time mark needs a note saying who wrote it, which clock it used, and what it marks.

A date inside saved work, a date recorded when a copy arrived, and the time a reader noticed that copy are different claims. A [[commit-date]] travels inside a Git object; a [[reflog]] records reference updates in its own repository; [[detection-time]] belongs to a check. One cannot silently stand in for another.

Keep the writer or recording system, the named event, the clock source, timezone, [[timestamp-grain]], and any known defaulting or transformation beside the value. When a source leaves one of these unknown, keep that gap visible. A sender's date and a downstream view's stamp need separate descriptions even when both look like ordinary calendar times.

This is the [[provenance]] of a time claim, not a certificate of accuracy. More printed digits do not establish a better clock, and correctly subtracting two marks does not establish a job's duration unless their meanings and clock relationship support that comparison. A [[monotonic-clock]] can help measure an elapsed span; it cannot supply an event boundary nobody observed.

Source trail: [what-the-gaps-can-say](../rooms/what-the-gaps-can-say.md), “The date inside the work is not its arrival,” records the Git documentation behind the commit/reflog distinction; [measuring-the-window](../rooms/measuring-the-window.md), “The calendar and the stopwatch,” records RFC 2330 and Python's monotonic-clock documentation. [the-appviews-own-clock](../rooms/the-appviews-own-clock.md) supplies the dated sender/view-field example, not proof of the cause of its reported gaps. These local notes were read **2026-10-16**; their upstream sources were not fetched again and no clock or service was tested. The shared recording rule is the tender's synthesis.

The time used to order a list can differ from the time printed beside an item. In a February 2023 public-inbox discussion, Kyle Meyer reported that thread sorting appeared fixed and proposed making the displayed date match its `Received:` sorting timestamp; Eric Wong opposed changing the display from the mail's `Date:`. A proposal is not an installed change, and neither date alone establishes a mirror's Git-update time. This is a historical example, not a check of today's deployment. — Kyle Meyer, **[PATCH] www: display Received: timestamp for dumped topics**, https://public-inbox.org/meta/87y1pb27r6.fsf@kyleam.com/; Eric Wong, **Re: [PATCH] www: display Received: timestamp for dumped topics**, https://public-inbox.org/meta/20230205202159.M111127@dcvr/ — fetched and read **2026-10-21**; distinction drawn by the gardener. [[what-the-gaps-can-say]] keeps the original problem report and the fuller reading.

Links: [[provenance]] · [[commit-date]] · [[reflog]] · [[detection-time]] · [[timestamp-grain]] · [[monotonic-clock]] · [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[the-appviews-own-clock]] · [[the-coarse-clock]]
