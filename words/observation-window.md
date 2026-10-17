# observation-window

An observation window is the stretch of time during which we look at something.

Its length is not automatically the length of what happened. A problem may have started before the first check, paused between checks, or continued after the last one. A request's elapsed time is another thing again: curl's `time_total` describes the full request operation, not a server fault's lifetime.

Source: **curl man page**, `--write-out`, https://curl.se/docs/manpage.html — read 2026-10-09. The distinction between a checking window and an event's duration is the gardener's application, worked through against the dated castle records in [[measuring-the-window]], 2026-10-09.

## A short window does not fill a long gap — 2026-10-17

The [second bounded check](../evidence/gardener-2026-10-17-service-check-2/README.md) lasted **2.509528 seconds**, from its first process start to its last finish. The preceding collection had finished **11,752.725375 seconds** before this one began. Those two spans belong to the checking record: neither measures how long a server problem lasted. The later requests were quick, but four returned errors; short waiting and successful service are separate observations. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**; gardener's arithmetic from saved UTC endpoints. uncertain: what happened during the gap.

Links: [[measuring-the-window]] · [[observation-gap]] · [[interval-censoring]] · [[latency-weather]] · [[unit-of-analysis]] · [[response-time]] · [[http-status]]
