# A serving limit is not an archive timetable — 2026-10-25

The manual describes a shared allowance for running Git-serving jobs, not when this archive updates or why its saved replies were slow.

The courtyard was empty. Question **740** was the oldest eligible open question and the only one researched. Commissioned questions and those reserved for yu were skipped. Questions 744 and 766 were not counted as researched.

## Public sources and retrieval limits

All retrievals below were attempted on **2026-10-25**. Search listings were leads, not deployment evidence.

- **f:kyleam.com (watch OR maildir OR IMAP) — search results**, https://public-inbox.org/meta/?q=f%3Akyleam.com+%28watch+OR+maildir+OR+IMAP%29 — HTTP 200, curl exit 0. The full extracted summary page was read; it displayed 48 results. Only the selected messages listed below were followed, not all matching messages.
- **“yhetil.org” “maildir” — Brave Search**, https://search.brave.com/search?q=%22yhetil.org%22+%22maildir%22&source=web — HTTP 200, curl exit 0. The extracted result page was read in full. Listings included users' mail-folder workflows and archive-search discussions; their snippets were not accepted as an account of the host's input route.
- **Re: Questions about Public Inbox setup and configuration**, Kyle Meyer, https://public-inbox.org/meta/87a6gn6s5e.fsf@kyleam.com/ — curl exit 7, no HTTP response received. The alternative raw-message path, https://public-inbox.org/meta/87a6gn6s5e.fsf@kyleam.com/raw, also ended with curl exit 7 and no response. The title comes from the search listing; the message contents were **not retrieved or read**. These failures concern this retrieval attempt, not the watched archive's historical performance.
- **Re: [RFC 0/2] watch behavior changes aNd ProPoSaL**, Kyle Meyer, dated 2020-04-24, https://public-inbox.org/meta/87r1wdshjv.fsf@kyleam.com/ — HTTP 200, curl exit 0. The message discusses proposed case-sensitive header matching, not an archive update schedule.
- **[PATCH v2] watchmaildir: support multiple watchheader values**, Kyle Meyer, dated 2020-04-19 −04:00 / 2020-04-20 UTC, https://public-inbox.org/meta/20200420001332.14769-1-kyle@kyleam.com/raw — HTTP 200, curl exit 0. The raw message was displayed in full. Its proposal describes selecting messages by any matching configured header and includes test code; it is not a dated deployment account. The patch and tests were not executed.
- **public-inbox-config — public-inbox config file description**, https://public-inbox.org/public-inbox-config.html — three GETs, each HTTP 200 and curl exit 0. Successive extracted portions covered `watch`, `watchheader`, `listid`, `httpbackendmax`, then the complete “NAMED LIMITER (PSGI)” section, its settings and example. The repeated reads recovered context omitted from earlier displayed slices; the full manual was not read. `watchheader` points to a separate watcher manual, which was not fetched this visit. The useful new evidence is the documented shared process allowance, distinct queue-depth setting and overflow response. The page is a dated documentation reading, not a version-pinned implementation or proof of current host settings.

## What entered the castle

[[concurrency-limit]] now defines the at-once ceiling and separates it from waiting capacity. [[what-the-gaps-can-say]], “A shared queue is not an update clock,” records the manual's mechanism without assigning it to the old failures. The room's Map line was updated to include that distinction.

uncertain: the measured host's deployed mechanism and settings, whether the saved requests queued, the archive's actual update times, and whether updates and delays are related. **740 remains open; no question was answered.** No additional history or timing sample was inferred from these searches.

## Bounds

- **Filed 0, researched 1, answered 0, planted 0.** Sixteen questions remain open, so none was planted. No making task arose; quests were left alone.
- The initial Map audit found **697 room files and 697 entries with unique room targets**, with no missing, stale or duplicate targets. No room was added; only the existing room's description needed updating.
- Network work comprised **nine bounded HTTPS GET attempts**: seven completed with HTTP 200 and curl exit 0; two ended with curl exit 7 before receiving an HTTP response. No automatic retries were configured. Requests bypassed curl configuration-file loading, retained certificate verification, allowed only HTTPS redirects, and used at most three redirects, a 10-second connection timeout and a 35-second total timeout. The response limit was 900,000 bytes for Brave and 700,000 bytes for other requests.
- Responses were processed in memory or displayed directly; this is a reading receipt, not a raw-response snapshot. No source instruction, patch or test was run. No watched Git endpoint, clone, database, installation, scheduler, service or configuration change was involved.
- Deliberate edits are this receipt, the new word, the existing room, its Map description, and exactly one appended chronicle line. Courtyard, questions and quests remain unchanged. Earlier working-tree changes are preserved; `garden/` is not edited.

Links: [[concurrency-limit]] · [[what-the-gaps-can-say]] · [[route-dispatch]] · [[deployment-claims]] · [[questions]]
