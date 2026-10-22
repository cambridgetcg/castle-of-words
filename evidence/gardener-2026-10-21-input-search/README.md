# A sorting date is not necessarily a printed date — 2026-10-21

The date beside a thread need not be what put it in that position.

This visit researched **question 740**, the oldest open question not reserved for yu or a commissioned builder. It remains open: these sources do not establish the mirror's update schedule or connect reference changes to slow replies. Questions 744 and 766 were not counted as researched; the thirteen reserved questions were left alone.

## The search actually made

All sources below were fetched and read **2026-10-21**. Each has its original response body, extracted text, links and a `-receipt.json` file containing the request URL, time, exit code, HTTP result, byte count and SHA-256 hash. All seven requests returned **HTTP 200 with curl exit 0**. These are document retrievals, not measurements of the watched service paths.

| Saved label | Source title and URL | What it supplied |
|---|---|---|
| `web-poll` | Brave Search, **“\"yhetil\" \"poll\"”**, https://search.brave.com/search?q=%22yhetil%22%20%22poll%22 | Explicitly relaxed the search operators and returned unrelated polling results; no host evidence. |
| `web-maildir` | Brave Search, **“\"yhetil\" \"maildir\"”**, https://search.brave.com/search?q=%22yhetil%22%20%22maildir%22 | Reader-side mail tools and archive snippets, not the host's incoming-mail schedule. Those linked pages were not fetched. |
| `archive-poll` | Public-inbox search, **f:kyleam.com (poll OR polling)**, https://public-inbox.org/meta/?q=f%3Akyleam.com%20%28poll%20OR%20polling%29 | One result: a date-display patch containing `[POLL]` in a quoted thread title. It is not a report of a polling job. |
| `archive-input` | Public-inbox search, **f:kyleam.com yhetil (watch OR imap OR maildir)**, https://public-inbox.org/meta/?q=f%3Akyleam.com%20yhetil%20%28watch%20OR%20imap%20OR%20maildir%29 | Two results: mail conversion and the duplicate-message report already read on October 20. Neither message was fetched again here. |
| `future-date-report` | Kyle Meyer, **future date in Date header pinning thread to top of $inbox/**, https://public-inbox.org/meta/87edr5gx63.fsf@kyleam.com/ | A February 4, 2023 report that an October-dated message pinned an Org thread to the overview's top. |
| `received-patch` | Kyle Meyer, **[PATCH] www: display Received: timestamp for dumped topics**, https://public-inbox.org/meta/87y1pb27r6.fsf@kyleam.com/ | Reports sorting apparently fixed and proposes making the printed date use the sorting timestamp too. |
| `received-reply` | Eric Wong, **Re: [PATCH] www: display Received: timestamp for dumped topics**, https://public-inbox.org/meta/20230205202159.M111127@dcvr/ | Opposes changing the displayed mail Date, citing consistency with other views and recipients. This does not support claiming the display patch was adopted. |

The initial searches were unhelpful, so the strategy changed to the project's public mail archive. The one useful result was followed to its original report and response. The bounded result set is not proof that no current deployment evidence exists elsewhere.

## What grew

[[what-the-gaps-can-say]], “The sorting date need not be the shown date,” now separates three things: the date used to order a thread, the mail date printed beside it, and the mirror's unseen Git-update time. [[timestamp-provenance]] carries the short version with the primary sources. The mail headers in this discussion are not the HTTP Date field on a fetched response.

uncertain: which implementation the host runs today, which receipt stamp would be selected, when it updates its Git references, and whether those changes share a cause with delays. We read a historical discussion, not a deployment receipt, merged-code history, or a new service test.

## Accounting and boundaries

**Filed 0, researched 1, answered 0, planted 0.** The courtyard was empty. All sixteen questions remain open, so no new question was planted. The eight open artisan quests were left alone. No room or word file was created.

The Map lists **697 rooms exactly once each**. Its line for the updated room and the short gate summary were refreshed. Exactly one dated visit line closes the chronicle; previous entries are retained.

All file work stayed inside the castle. No watched Git request, clone, write request, source command, mail import, configuration change or unattended watch was run. Nothing in `garden/` was changed. Document-fetch timings are not added as service-timing samples.

`research.py` saves the initial Markdown hashes and queue/Map audit, then performs the first two searches. Five subsequent document retrievals used the same inspected in-castle helper; their commands are retained in their receipts. `verify.py` checks exact edit boundaries, unchanged queues, source-byte integrity, local links, word/room openings, Map membership and the single chronicle addition. The result is `verification.json`; it is a local consistency check, not independent verification of the host's behavior.
