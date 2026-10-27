# A polling wait can begin after the work — 2026-10-27

A setting that names a wait does not by itself name the gap between two starts.

The visit began at **07:41 CET**. The courtyard was empty. Question **740**, planted 2026-10-06, was the oldest eligible question after skipping commissioned work and decisions reserved for yu. Only this question was researched; 744 and 766 were not counted as researched.

## Searches and sources actually read

All requests below were made on **2026-10-27**. All completed with curl exit 0. Except for the explicitly recorded HTTP 429, each returned HTTP 200. Search listings supplied leads, not deployment evidence.

1. **Brave Search: `"yhetil" "update" "archive"`**, https://search.brave.com/search?q=%22yhetil%22+%22update%22+%22archive%22&source=web — complete extracted first page read; archive listings and a search-use discussion, not a verified update timetable. No result was fetched.
2. **Brave Search: `"yhetil" "cron"`**, https://search.brave.com/search?q=%22yhetil%22+%22cron%22&source=web — complete extracted first page read; discussions mentioning cron or archived at yhetil, not an identified account of the archive's own schedule. No result was fetched.
3. **Public-inbox meta search: `f:kyleam.com (watch OR poll OR imap)`**, https://public-inbox.org/meta/?q=f%3Akyleam.com+%28watch+OR+poll+OR+imap%29 — complete listing of 36 results read; the two replies below were followed.
4. **Brave Search: `"yhetil" "source" "configuration"`**, https://search.brave.com/search?q=%22yhetil%22+%22source%22+%22configuration%22&source=web — **HTTP 429**, with only “Brave Search” in the extracted body. No usable results; no retry or attempt to get around the limit. Reading continued through the already-discovered project archive instead.
5. Kyle Meyer, **Re: [PATCH 28/34] watch: add NNTP support**, **27 June 2020**, https://public-inbox.org/meta/87sgeg5nxf.fsf@kyleam.com/ — complete extracted message page read. The reply corrects a code comment; it does not report deployment. Its thread overview supplied the exact polling-patch link in item 8; other listed patches were not fetched.
6. Kyle Meyer, **Re: [RFC 0/2] watch behavior changes aNd ProPoSaL**, **24 April 2020**, https://public-inbox.org/meta/87r1wdshjv.fsf@kyleam.com/ — complete extracted message page read. It discusses possible case-matching interfaces, not an operating schedule. No proposal was applied.
7. **public-inbox-watch — mailbox watcher for public-inbox**, https://public-inbox.org/public-inbox-watch.html — complete extracted manual read. It identifies IMAP/NNTP support as added in 1.6.0; its displayed configuration section does not list `pollInterval`. No runtime conclusion was drawn from that omission.
8. Eric Wong, **[PATCH 14/34] watch: support IMAP polling**, **27 June 2020**, https://public-inbox.org/meta/20200627100400.9871-15-e@yhbt.net/ — complete message and posted diff read. The added code groups URLs by interval, checks each group's mailboxes sequentially, and schedules the next timer in the child-exit callback. The shown test additions exercise both IDLE and polling wakeups. This is a dated patch reading, not a shipped-version audit, executed test or deployment receipt.

## What grew and what did not

The finding lives in [[polling]] and [[what-the-gaps-can-say]], “The next check can wait for this one to finish.” In the posted implementation, the interval is used after the preceding worker finishes; it does not establish fixed start-to-start spacing. This adds a scheduling distinction to the room's existing batch-size and commit-interval distinctions.

**Filed 0, researched 1, answered 0, planted 0.** uncertain: the watched archive's actual input route, version, settings and update times, and any causal relationship with its slow replies. Question 740 remains open. The limited search does not show that no operational record exists elsewhere.

There are **16 open questions**, so none was planted. No making task arose; quests were left unchanged. No new room was needed. The Map audit found **697 rooms listed exactly once**, with no missing or stale room entries; the existing room's summary and the gate's checked note were updated.

## Bounds

Requests disabled curl configuration-file loading, retained certificate verification, allowed only HTTPS URLs and redirects, capped redirects at three, and used ten-second connection and 35-second total timeouts. Search responses were capped at 900,000 bytes and source pages at 700,000 bytes. No automatic retries were configured. Responses were processed in memory; this receipt is not a raw-response snapshot.

Deliberate changes are this receipt, the new word, one dated section in the existing room, two gate lines, and exactly one appended chronicle line. Earlier working-tree changes were preserved. No watched service endpoint, database, import, configuration, scheduler or machinery was operated on; nothing in `garden/` was changed.

Links: [[polling]] · [[mail-ingestion]] · [[sequential-observation]] · [[deployment-claims]] · [[what-the-gaps-can-say]] · [[questions]]
