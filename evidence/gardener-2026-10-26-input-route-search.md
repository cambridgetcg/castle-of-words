# An input-route search returned a known report — 2026-10-26

The search found no newly verified account of the watched archive's update times.

The visit began at **22:22 CET**. The courtyard was empty. Question **740** was the oldest eligible open question after skipping commissioned work and decisions reserved for yu. It was the only question researched; questions 744 and 766 were not counted as researched.

## Searches and reading

All requests below were made on **2026-10-26**. Search listings were leads, not evidence that a host runs a particular program.

1. **Brave Search: `"yhetil.org" ("cron" OR "systemd" OR "mbsync" OR "offlineimap")`**, https://search.brave.com/search?q=%22yhetil.org%22+%28%22cron%22+OR+%22systemd%22+OR+%22mbsync%22+OR+%22offlineimap%22%29&source=web — HTTP 200, curl exit 0. The complete extracted first page was read. It largely returned other people's mail-sync arrangements and an archived Guix discussion, not a verified description of the watched host's input route. No result link was fetched.
2. **Public-inbox meta search: `f:kyleam.com ("imap" OR "poll" OR "fetchmail" OR "mbsync" OR "offlineimap")`**, https://public-inbox.org/meta/?q=f%3Akyleam.com+%28%22imap%22+OR+%22poll%22+OR+%22fetchmail%22+OR+%22mbsync%22+OR+%22offlineimap%22%29 — HTTP 200, curl exit 0. The complete listing contained 19 results. Only the message in items 4–5 was followed this visit.
3. **Brave Search: `"yhetil.org" "config"`**, https://search.brave.com/search?q=%22yhetil.org%22+%22config%22&source=web — HTTP 200, curl exit 0. The complete extracted first page was read. It returned mirror instructions, an ownership discussion, archive listings and client configuration, not a newly verified operating timetable. No result link was fetched.
4. Kyle Meyer, **news.public-inbox.org misbehaving?**, raw-message URL https://public-inbox.org/meta/87r1unyjj0.fsf@kyleam.com/raw — **curl exit 7**, connection failure, HTTP code reported as **000**. No message was obtained from this request; 000 is not a received HTTP status.
5. The same message's **HTML page**, https://public-inbox.org/meta/87r1unyjj0.fsf@kyleam.com/ — HTTP 200, curl exit 0. The complete extracted page was read as an alternative to the failed raw request. Dated **9 June 2020**, it reports messages absent from a news-reading interface but visible on the website. Its subject, host and report match the source already kept in [[what-the-gaps-can-say]], “A new index can leave an old reader behind,” and the [October 24 receipt](gardener-2026-10-24-reader-replacement.md). The replies linked by its thread overview were not fetched again.

## Outcome

The fetched message adds no new update-schedule evidence to the existing reading. It concerns **news.public-inbox.org's news-reading interface**, not the watched yhetil Git service. No duplicate explanation was added to rooms or words.

**Filed 0, researched 1, answered 0, planted 0.** uncertain: the watched archive's input route, update times and any relationship between reference changes and delayed replies remain unknown. Question 740 stays open. This bounded search does not prove that no public operational record exists.

There are **16 open questions**, so none was planted. No making task arose; the eight open quests were left unchanged.

## Bounds and checks

- The Map audit found **697 room files and 697 unique room entries**, with no missing, stale or duplicate targets. Its room entries needed no edit. The gate's checked note was refreshed to this visit and receipt.
- Requests disabled curl configuration-file loading, retained certificate verification, allowed only HTTPS URLs and redirects, capped redirects at three, and used ten-second connection and 35-second total timeouts. Search responses were capped at 900,000 bytes; message responses at 700,000 bytes. No automatic retries were configured; the failed raw request was followed once through the ordinary HTML page.
- Responses were processed in memory. This is a reading receipt, not a raw-response snapshot. No posted command or patch was executed.
- Deliberate writes are this receipt, the gate's checked note and exactly one appended chronicle line. Courtyard, questions, quests, rooms and words were left unchanged; earlier working-tree changes were preserved.
- No watched Git endpoint, database, mail import, service or scheduler was operated on. Nothing in `garden/` was changed. No new service-timing sample was collected.

Links: [[what-the-gaps-can-say]] · [[file-identity]] · [[mail-ingestion]] · [[mirror-fetch]] · [[questions]]
