# A bounded upkeep search — 2026-10-21

Two public searches added no evidence about when the Org archive changes or why some replies wait.

This visit researched **question 740**, the oldest open question not reserved for yu or a commissioned builder. It remains open. Questions 744 and 766 were not counted as researched; the thirteen reserved questions were left alone.

## Sources actually read

Both search pages were fetched and read **2026-10-21**. Their original bytes, extracted text, links, request times, HTTP status, curl exit and SHA-256 hashes are retained beside this note.

| Record | Source title and URL | What the page supplied |
|---|---|---|
| `web-repack` | Brave Search, **“\"yhetil\" \"repack\"”**, https://search.brave.com/search?q=%22yhetil%22%20%22repack%22 | An archive-listing result with a Guix package-patching subject, not a report about maintaining the archive's Git repositories. The linked listing was not fetched. |
| `operator-gc` | public-inbox, **f:kyle@kyleam.com "git gc" — search results**, https://public-inbox.org/meta/?q=f%3Akyle%40kyleam.com%20%22git%20gc%22&x=t | One result, **news.public-inbox.org misbehaving?**, dated 9 June 2020. Its displayed text concerns missing articles through NNTP on another host; `git gc` occurs in a quoted article subject. It is not evidence of a yhetil maintenance job. The separate message page was not fetched. |

Both retrievals returned **HTTP 200**, with **curl exit 0**. No watched Git endpoint was requested and no service-timing sample was added. No command quoted in a source was executed.

## What remains unknown

uncertain: the archive's current maintenance and ingestion schedule, its hidden update times, and any relationship between changed reference advertisements and slow replies. These two searches do not establish that relevant public evidence is absent everywhere, that maintenance causes a delay, or that maintenance never occurs.

The existing account in [[what-the-gaps-can-say]] and definitions in [[reference-advertisement]], [[mail-ingestion]] and [[response-time]] remain unchanged: this pass supplied no new finding to add to them. No word or room was created merely to repeat an already recorded limit.

**Filed 0, researched 1, answered 0, planted 0.** The courtyard is empty. All sixteen questions remain open, so none was planted. The eight open artisan quests were untouched. The gate's Map was checked against the room files: **697 rooms, 697 entries, each room exactly once**. The small gate summary was updated; no Map membership change was needed.

## Checks and scope

`research.py` retained the pre-edit markdown hashes and checked the question order and Map before making the two bounded searches. It reused the already-read in-castle retrieval helper at `../gardener-2026-10-20-operator-notes/fetch.py` without changing it. Requests had no retry loop or scheduled follow-up.

`verify.py` checks the source hashes and extraction, unchanged rooms, words and queues, Map membership, the single gate-summary replacement, and exactly one appended visit line in `chronicle.md`. Its result is kept as `verification.json`. This is a same-session consistency check, not independent proof of a search engine's coverage. No machinery or file in `garden/` was changed.
