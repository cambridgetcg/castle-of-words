# A batch size is not an update timetable — 2026-10-27

Grouping work by size and committing it after a time interval are different rules; neither identifies the watched archive's schedule.

The visit began at **04:33 CET**. The courtyard was empty. Question **740**, planted 2026-10-06, was the oldest eligible open question after skipping commissioned work and decisions reserved for yu. It was the only question researched; 744 and 766 were not counted as researched.

## Searches and sources actually read

All requests below were made on **2026-10-27**, and each returned **HTTP 200, curl exit 0**. Search results were treated as leads, not evidence of deployment.

1. **Brave Search: `"public-inbox-watch" "batch"`**, https://search.brave.com/search?q=%22public-inbox-watch%22+%22batch%22&source=web — the complete extracted first page was read. It led to the project's index manual and release notes; the Ubuntu result was not followed.
2. **Public-inbox meta search: `f:kyleam.com (batch OR commit OR transaction)`**, https://public-inbox.org/meta/?q=f%3Akyleam.com+%28batch+OR+commit+OR+transaction%29 — the complete displayed listing contained 56 results. A narrower search found the exact batch-size reply below; the other listed messages were not fetched in this visit.
3. **public-inbox-index — create and update search indices**, https://public-inbox.org/public-inbox-index.html — the complete extracted manual was read, particularly `--commit`, `publicinbox.indexBatchSize`, and the reindexing warnings.
4. **Public-inbox meta search: `f:kyleam.com s:"batch-size"`**, https://public-inbox.org/meta/?q=f%3Akyleam.com+s%3A%22batch-size%22 — the complete listing contained one result and supplied the URL in item 5.
5. Kyle Meyer, **Re: [PATCH] index: add --batch-size=SIZE option**, **17 May 2020**, https://public-inbox.org/meta/871rnit8vv.fsf@kyleam.com/ — the complete extracted message page was read. Meyer identifies a missing “to” in documentation prose. He does not report his archive's settings or a deployed change. The parent patch and replies were not fetched or executed.
6. **public-inbox releases**, https://public-inbox.org/NEWS.html — the displayed first 18,000 text characters included the complete **2.0.0** entry. That entry's search-improvement notes were read for the stated purpose of `--commit` and its checkpoint wording. Older entries beyond the displayed excerpt were not read; no upgrade instructions were run.

## What grew

- **Amount and time are separate controls.** The index manual describes a byte threshold for committing changes and releasing locks, and a time interval that can force commits before that threshold is reached. The release notes identify the latter's purpose as changing the rate at which SQLite and Xapian data is made available to read-only processes. These are indexing controls, not evidence of a mail-arrival or Git-fetch schedule.
- **The numerical prose needs care.** The manual's batch explanation still calls `1m` the default and gives an example based on it, while its explicit default line distinguishes `1m` on 32-bit from `8m` on 64-bit. The manual gives `--commit` a 15-second default, while the 2.0.0 release entry says long-running indexing operations auto-checkpoint every 5 seconds. These are observed differences in the fetched texts, not a version-pinned determination of runtime behavior. No one number was adopted as the watched host's setting or as an end-to-end delay bound.
- **A wording review is not an operating record.** The 2020 reply adds no deployment evidence. The useful new material comes from reading the manual and release notes together, not from treating the author's involvement as proof that the host used a setting.

The understanding lives in [[batch]] and [[what-the-gaps-can-say]], “A batch size and a commit interval are different rulers.” The existing October 10 distinction between fetching and indexing is preserved, not rediscovered as a new host finding.

**Filed 0, researched 1, answered 0, planted 0.** uncertain: which release, settings and jobs the watched archive used, when its references changed, and whether those changes shared a cause with slow replies. **740 stays open.** This bounded search does not establish that no operational record exists elsewhere.

There are **16 open questions**, so none was planted. No making task arose; the eight open quests were left unchanged.

## Bounds and checks

- Before editing, the Map audit found **697 room files and 697 unique room entries**, with no missing, stale or duplicate targets. No new room was needed. The existing room's one-line Map description and the gate's checked note were updated.
- Six HTTPS requests were made. They disabled curl configuration-file loading, retained certificate verification, allowed at most three HTTPS redirects, and used ten-second connection and 35-second total timeouts. Responses were capped at 900,000 bytes, except the individual message at 700,000 bytes. No automatic retries were configured.
- Responses were processed in memory. This receipt records the reading and its limits; it is not a raw-response snapshot or an independent source-code test.
- No watched Git endpoint, database, mail import, indexing process, service, scheduler or configuration was operated on. Nothing in `garden/` was changed. No service-timing sample was collected.
- Deliberate changes are this receipt, one new word, a dated addition to one existing room, the gate's checked note and Map entry, and exactly one appended chronicle line. Earlier working-tree changes were preserved; courtyard, questions, quests and the earlier `mail-ingestion` addition were left unchanged.

Links: [[batch]] · [[mail-ingestion]] · [[queue]] · [[reference-advertisement]] · [[what-the-gaps-can-say]] · [[questions]]
