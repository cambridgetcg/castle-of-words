# timestamp-provenance

A time mark needs a note saying who wrote it, which clock it used, and what it marks.

A date inside saved work, a date recorded when a copy arrived, and the time a reader noticed that copy are different claims. A [[commit-date]] travels inside a Git object; a [[reflog]] records reference updates in its own repository; [[detection-time]] belongs to a check. One cannot silently stand in for another.

Keep the writer or recording system, the named event, the clock source, timezone, [[timestamp-grain]], and any known defaulting or transformation beside the value. When a source leaves one of these unknown, keep that gap visible. A sender's date and a downstream view's stamp need separate descriptions even when both look like ordinary calendar times.

This is the [[provenance]] of a time claim, not a certificate of accuracy. More printed digits do not establish a better clock, and correctly subtracting two marks does not establish a job's duration unless their meanings and clock relationship support that comparison. A [[monotonic-clock]] can help measure an elapsed span; it cannot supply an event boundary nobody observed.

Source trail: [what-the-gaps-can-say](../rooms/what-the-gaps-can-say.md), “The date inside the work is not its arrival,” records the Git documentation behind the commit/reflog distinction; [measuring-the-window](../rooms/measuring-the-window.md), “The calendar and the stopwatch,” records RFC 2330 and Python's monotonic-clock documentation. [the-appviews-own-clock](../rooms/the-appviews-own-clock.md) supplies the dated sender/view-field example, not proof of the cause of its reported gaps. These local notes were read **2026-10-16**; their upstream sources were not fetched again and no clock or service was tested. The shared recording rule is the tender's synthesis.

Links: [[provenance]] · [[commit-date]] · [[reflog]] · [[detection-time]] · [[timestamp-grain]] · [[monotonic-clock]] · [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[the-appviews-own-clock]] · [[the-coarse-clock]]
