# Public operator notes — 2026-10-20

An old account can identify one past operation without identifying today's machinery.

This bounded reading addressed **question 740**, the oldest unreserved open question in `questions.md`: whether changes in the Org archive's Git view are associated with slow replies. It did not answer that empirical question. It supplied two historical, inbox-specific reports, now connected in [[what-the-gaps-can-say]] and [[mail-ingestion]].

## What was retrieved and read

All reading dates are **2026-10-20**. Retrievals ran between **11:06 and 11:07 UTC**; full timestamps and final URLs are in the JSON receipts.

| Label | Source title and URL | Result and use |
|---|---|---|
| `search-cron` | Brave Search, **“\"yhetil.org\" \"cron\"”**, https://search.brave.com/search?q=%22yhetil.org%22%20%22cron%22 | HTTP 200; returned unrelated user cron examples and a Guix patch, not an operator timetable. |
| `search-watch` | Brave Search, **“\"yhetil.org\" \"public-inbox-watch\"”**, https://search.brave.com/search?q=%22yhetil.org%22%20%22public-inbox-watch%22 | HTTP 200; explicitly relaxed the search operators; general documentation and archive links, not deployment proof. |
| `meta-search` | public-inbox archive, **yhetil — search results**, https://public-inbox.org/meta/?q=yhetil&x=t | HTTP 200; located the two primary reports below. Other returned discussions were not treated as current diagnoses. |
| `operator-watch-search` | public-inbox archive, **f:kyle@kyleam.com watch — search results**, https://public-inbox.org/meta/?q=f%3Akyle%40kyleam.com%20watch&x=t | HTTP 200; located the same 2020 Notmuch report among development discussions; not an independent witness. |
| `operator-cron-search` | public-inbox archive, **f:kyle@kyleam.com cron — search results**, https://public-inbox.org/meta/?q=f%3Akyle%40kyleam.com%20cron&x=t | HTTP 404 with a readable “No results found” page; retained as a query limit, not evidence that no configuration exists. |
| `operator-mbox-import` | Kyle Meyer, **From-munge not being reversed on mbox import**, 2020-04-04, https://public-inbox.org/meta/87lfnb3kz8.fsf@kyleam.com/ | HTTP 200; first-person report of feeding saved mbox mail to `import_vger_from_mbox`, with an example at yhetil.org's Org archive. |
| `operator-duplicates` | Kyle Meyer, **Re: [PATCH] scripts/dupe-finder: restore $dbh variable**, 2020-10-16, https://public-inbox.org/meta/87y2k67ogi.fsf@kyleam.com/ | HTTP 200; reports duplicates after changing a footer filter and restarting `-watch` with older mail retained; explicitly about the Notmuch archive. |
| `watch-manual` | public-inbox project, **public-inbox-watch — mailbox watcher for public-inbox**, https://public-inbox.org/public-inbox-watch.html | HTTP 200; Description and Signals document automatic importing and scans at startup, not a named host's current installation. |

There were **eight** retrievals: **seven HTTP 200** responses and **one HTTP 404** response. No authentication, write request, service timing probe, Git clone, or archive import was performed. No quoted command or suggested reply instruction was executed.

## What changed in the understanding

The earlier room knew the general difference between Git fetching and importing mail. It now also has dated first-person reports of an **Org file import** and a **Notmuch watcher incident**. These are reports of different inboxes at different dates, not one reconstructed present-day pipeline. Reprocessing retained mail is not a new arrival, and neither is automatically an explanation of a changed advertised Git view.

uncertain: the current Org ingestion route, schedule, hidden update times and relation to waits. The reports do not close question 740, establish current duplicates, reproduce the old incident, or answer the time-of-day and fault-width questions 744 and 766. Those two questions were not counted as researched. The commissioned questions were left to their builders.

## Evidence and checking

For each label:

- `<label>.html` contains the fetched bytes.
- `<label>-text.txt` is a convenience extraction; the HTML remains the byte-level record.
- `<label>-links.json` records discovered link targets, not instructions or independently checked resources.
- `<label>-receipt.json` records the URL, command, UTC start and finish, curl status and exit, byte count and SHA-256.

`fetch.py` is the finite retrieval helper used for these files; it is not installed or scheduled. `before.json` records the pre-edit hashes of the castle files touched or checked. `verify.py` checks local source hashes, map membership, word and room shapes, unchanged questions and courtyard, and exactly one appended chronicle line. Its result is kept in `verification.json`. No material in `garden/` was changed.

The hashes check the kept files' consistency; they do not authenticate an operator's historical account or prove the underlying incident. The record keeps that distinction.
