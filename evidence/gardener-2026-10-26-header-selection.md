# Arrival is not selection — 2026-10-26

A mailbox can receive a letter that an archive's selection rule leaves out; this does not tell us which rule the watched host actually used.

The visit began at **16:11 CET**. The courtyard was empty. **Question 740** was the oldest eligible open question after skipping commissioned work and decisions reserved for yu; it was the only question researched. Questions 744 and 766 were not counted as researched.

## Searches and sources actually read

Every request listed below returned **HTTP 200 with curl exit 0** on **2026-10-26**. Search results supplied leads, not evidence of a deployed configuration.

1. **Public-inbox meta search: `f:kyleam.com (watch OR mda OR maildir)`**, https://public-inbox.org/meta/?q=f%3Akyleam.com+%28watch+OR+mda+OR+maildir%29 — the complete extracted listing contained 40 results. Three messages were selected below; the other messages were not fetched this visit.
2. **Brave Search: `"yhetil.org" "public-inbox-watch"`**, https://search.brave.com/search?q=%22yhetil.org%22+%22public-inbox-watch%22&source=web — the complete extracted first page was read. It explicitly said search operators were not applied because too few matches were found. Archive pages and manuals in this relaxed result set do not establish that the named host runs the watcher. No archive result from this page was fetched.
3. Kyle Meyer, **[RFC PATCH] watchmaildir: support multiple watchheader values**, dated **12 April 2020**, https://public-inbox.org/meta/20200412044452.7524-1-kyle@kyleam.com/raw — decoded email and posted patch read in full. It proposes accepting a match to either of several configured headers for project archives sharing a mailbox; its scenario is not presented as a report of yhetil's operation.
4. Kyle Meyer, **Re: [RFC 0/2] watch behavior changes aNd ProPoSaL**, dated **24 April 2020**, https://public-inbox.org/meta/87r1wdshjv.fsf@kyleam.com/raw — decoded email read in full. It discusses proposed case-sensitivity choices, not an update schedule or deployed configuration. No present behavior was inferred from these alternatives.
5. Kyle Meyer, **[PATCH v2] watchmaildir: support multiple watchheader values**, dated **19 April 2020 −0400 / 20 April UTC**, https://public-inbox.org/meta/20200420001332.14769-1-kyle@kyleam.com/raw — decoded email, patch and test read in full. The example test expects an article number for a message matching `To`, another for a message matching `Cc`, and no number for a message matching neither. The posted test was not executed, and its presence was not reported as a passing result or proof of deployment.
6. **public-inbox-config — public-inbox configuration**, https://public-inbox.org/public-inbox-config.html — the `watchheader` and `listid` entries and their surrounding extracted text were read, not the whole manual. `watchheader` points to the watcher manual; `listid` documents accepting one matching List-Id among repeated configured values.
7. **public-inbox-watch — mailbox watcher for public-inbox**, https://public-inbox.org/public-inbox-watch.html — complete extracted manual read. Its Configuration section documents repeated `watchheader` values as accepting any match in **1.5 and later**, versus using only the last value in **1.4 and earlier**. This is a maintained manual's account of versioned behavior, not a source audit of those releases or an inspection of a host.

## What grew

[[what-the-gaps-can-say]], “Mail can arrive without entering this archive,” keeps the documented selection step separate from mailbox arrival and a changed [[reference-advertisement]]. [[mail-ingestion]], “Arrival is not selection,” now carries the version distinction beside its definition. The Map's existing room line now mentions mail-selection rules. No new room or word file was needed.

**Filed 0, researched 1, answered 0, planted 0.** uncertain: the watched archive's input path, selection settings, software version, update times, and any relationship to delayed replies. **740 remains open.** Neither the proposal nor the manual supplies a current configuration or the missing historical update record.

There are **16 open questions**, so none was planted. No making task arose; the eight open quests were left unchanged.

## Bounds and checks

- The Map audit found **697 room files and 697 unique room entries**, with no missing, stale or duplicate room targets. One description was updated; no entry was added or removed.
- Requests disabled curl configuration-file loading, retained certificate verification, allowed only HTTPS redirects, limited redirects to three, and used a ten-second connection timeout and a 35-second total timeout. Response-size caps were 800,000 bytes for the archive search, 900,000 for Brave, and 700,000 for each email or manual. No automatic retries were configured.
- Responses were processed in memory. HTML was text-extracted; raw emails were decoded with Python's standard-library email parser. This is a reading receipt, not a saved raw-response snapshot.
- Deliberate writes are this receipt, one addition to the existing room, one addition to the existing word, one Map description, and exactly one appended chronicle line. Courtyard, questions and quests remain unchanged; earlier working-tree changes are preserved.
- No watched Git endpoint, source command, patch, regression test, mail import, database, configuration, scheduler or service was operated on. Nothing in `garden/` was changed.

Links: [[what-the-gaps-can-say]] · [[mail-ingestion]] · [[reference-advertisement]] · [[deployment-claims]] · [[questions]]
