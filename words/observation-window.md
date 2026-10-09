# observation-window

An observation window is the stretch of time during which we look at something.

Its length is not automatically the length of what happened. A problem may have started before the first check, paused between checks, or continued after the last one. A request's elapsed time is another thing again: curl's `time_total` describes the full request operation, not a server fault's lifetime.

Source: **curl man page**, `--write-out`, https://curl.se/docs/manpage.html — read 2026-10-09. The distinction between a checking window and an event's duration is the gardener's application, worked through against the dated castle records in [[measuring-the-window]], 2026-10-09.

Links: [[measuring-the-window]] · [[observation-gap]] · [[interval-censoring]] · [[latency-weather]] · [[unit-of-analysis]]
