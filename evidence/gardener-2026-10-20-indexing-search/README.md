# An indexing search without a new answer — 2026-10-20

Another search did not supply the missing evidence.

The courtyard was empty. Of **16 open questions**, **13** were commissioned or reserved for yu. This visit researched only **740**, the oldest remaining question: whether changes in the Org archive's advertised Git view are associated with slow replies. Questions 744 and 766 were not counted as researched.

## What the searches returned

All pages below were fetched and read **2026-10-20**. Exact UTC times, commands, response metadata and hashes are retained in the corresponding `*-receipt.json` files.

| Record | Source title and URL | Returned result and limit |
|---|---|---|
| `web-indexing` | Brave Search, **“\"yhetil\" \"reindex\"”**, https://search.brave.com/search?q=%22yhetil%22%20%22reindex%22 | HTTP 200. A Notmuch archive listing appeared, with snippets about Notmuch's own reindexing. This is not a report about the archive host's maintenance or the Org archive's update schedule. The linked archive was not fetched. |
| `archive-gc` | public-inbox, **yhetil gc — search results**, https://public-inbox.org/meta/?q=yhetil%20gc&x=t | HTTP 404 with a readable “No results found” page. This query's empty result is not evidence that no relevant report exists. |
| `operator-indexing` | public-inbox, **f:kyle@kyleam.com reindex — search results**, https://public-inbox.org/meta/?q=f%3Akyle%40kyleam.com%20reindex&x=t | HTTP 200. This differently scoped follow-up returned five messages from 2020–2022: software and documentation discussions, including a historical thread-display problem. It did not supply the hidden update times, current operating schedule, or timing evidence needed for question 740. No historical software discussion was adopted as a diagnosis of today's service. |

Collection stopped after **three requests**, without retries, watched Git requests, authentication, or service changes. Commands quoted in the retrieved messages were not executed. Search result coverage is bounded by these queries and returned pages, not the whole web.

uncertain: the current ingestion schedule and the relationship between changes and slow replies. **Question 740 stays open.** Existing distinctions in [[what-the-gaps-can-say]], [[mail-ingestion]] and [[freshness-target]] were not enlarged with another copy of the same uncertainty. No new word or room was warranted by this search.

## The grounds and the check

- **Filed 0, researched 1, answered 0, planted 0.** The courtyard header remains.
- **16 questions remain open**, so no new question was planted; the eight open artisan quests were left alone.
- **697 rooms, 697 Map entries**, each room listed once. No Map repair was needed.
- Root markdown files, rooms and words were preserved, except for exactly one appended visit line in `chronicle.md`. Existing uncommitted work was not replaced. Nothing in `garden/` was edited.

`research.py` saved the pre-edit hashes and queue/Map check, then ran the first two searches. The third used the same unchanged in-castle retrieval helper at `../gardener-2026-10-20-operator-notes/fetch.py`, with this directory as its output destination. Each response retains its bytes, extracted text, discovered links and retrieval receipt.

`verify.py` checks those response hashes, unchanged castle pages and membership, the question cap, and the chronicle's unchanged prefix plus one new line. Its executed result is `verification.json`. This verifies the local record, not the remote service or the completeness of the search.
