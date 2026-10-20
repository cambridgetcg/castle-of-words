# A bounded search without a new answer — 2026-10-20

A search can end honestly without adding another explanation.

This visit researched **question 740**, the oldest open question not reserved for yu or commissioned to another builder: whether changes in the Org archive's advertised Git view are associated with slow replies. It found no new evidence adequate to answer it. The earlier sourced distinctions remain in [[what-the-gaps-can-say]], [[mail-ingestion]] and [[freshness-target]]; those pages were left unchanged rather than enlarged with another account of the same uncertainty.

## Searches and their limits

All attempts were made **2026-10-20**. Exact UTC times, URLs, curl commands, response codes and file hashes are in the corresponding `*-receipt.json` files.

| Record | Public search and URL | Actual result |
|---|---|---|
| `search-schedule` | Brave Search, **“\"yhetil.org\" \"schedule\"”**, https://search.brave.com/search?q=%22yhetil.org%22%20%22schedule%22 | HTTP 200. The returned page was read; it listed archive pages and an unrelated meetup discussion, not a current operating schedule. No result snippet was adopted as deployment evidence. |
| `search-slow` | public-inbox, **yhetil slow — search results**, https://public-inbox.org/meta/?q=yhetil%20slow&x=t | HTTP 404 with a readable “No results found” page. This is a result of this query, not proof that no relevant public report exists. |
| `search-latency` | Alternative Brave query, https://search.brave.com/search?q=%22yhetil%22%20%22latency%22 | HTTP 429. Rate-limited; no usable search result claimed. curl's exit 0 does not make this an HTTP success. |
| `archive-broad` | Broader public-inbox query, https://public-inbox.org/meta/?q=yhetil&x=t | curl exit 7: connection failed. No HTTP response or body was received; this was not an empty search result. |

The broader query and alternative wording were finite follow-ups, not a continuing watch. Four attempts were made, with no retries. No watched Git endpoint was requested, no timing sample was added, and no command quoted in a search result was executed.

uncertain: the current ingestion schedule, hidden update times and relationship to delays. **Question 740 remains open.** Questions 744 and 766 were not researched in this visit; commissioned questions and decisions reserved for yu were left alone.

## The grounds

- Courtyard: empty, so **0 filed**; its header was retained.
- Research: **1 question researched, 0 answered**; no checkbox was changed.
- Planting: **0**, because **16 questions remain open**; no quest was added.
- Map: **697 rooms, 697 entries, one entry per room**, with no missing or extra target; no edit was needed.
- Chronicle: exactly one dated visit line appended.
- Rooms, words, questions, quests and gate were unchanged. Nothing in `garden/` was edited.

## Rechecking this receipt

The retrieval function was reused, without modifying it, from `../gardener-2026-10-20-operator-notes/fetch.py`, with its output directory set to this folder. Successful HTTP retrievals retain response bytes, extracted text and discovered links; an HTTP error page is kept as an error page. The failed connection has a receipt but no response-body file. The helper's empty convenience text file does not stand for a retrieved document.

`before.json` holds pre-edit hashes of the checked castle files. `verify.py` verifies the retained response hashes, the unchanged files, the room-to-Map correspondence, the open-question count, and the chronicle's unchanged prefix plus exactly one new line. Its executed result is `verification.json`. This checks the local record, not the mirror's behavior.
