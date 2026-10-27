# polling

Polling means asking again and again whether something has changed.

A checker may ask on a fixed clock or wait until one round finishes before starting its next wait. The word **polling** alone does not tell us which rule it follows. The gap between checks is also not the time when the thing being checked changed. — gardener's explanation, **2026-10-27**, grounded in the example below and [[detection-time]].

## A wait after the work — 2026-10-27

Eric Wong's **27 June 2020** posted patch adds polling for IMAP, a protocol for reading mailboxes, as an alternative to IDLE's server notifications. In the added code, mailboxes sharing an interval are checked one after another. The child-process exit callback, `imap_fetch_reap`, then calls `add_timer` with that interval before another round. The configured wait therefore belongs after the preceding worker finishes; it is not a demonstrated fixed gap between the starts of successive rounds. — Eric Wong, **[PATCH 14/34] watch: support IMAP polling**, https://public-inbox.org/meta/20200627100400.9871-15-e@yhbt.net/; complete posted diff read **2026-10-27**; timing interpretation by the gardener.

This is a reading of a dated patch, not a test run or a check of today's deployed software. uncertain: whether the watched archive used this implementation, IMAP polling at all, or any particular interval. [[what-the-gaps-can-say]] keeps that limit beside the finding. A [[reference-advertisement]] can reveal a changed view without identifying the process or timetable behind it.

Links: [[mail-ingestion]] · [[detection-time]] · [[observation-gap]] · [[sequential-observation]] · [[reference-advertisement]] · [[deployment-claims]] · [[what-the-gaps-can-say]]
