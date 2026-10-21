# A bounded timeout search — 2026-10-21

Two public searches supplied no new evidence connecting the archive's changing Git view with delayed replies.

This visit researched **question 740**, the oldest open question not reserved for yu or a commissioned builder. It remains open. Questions 744 and 766 were not counted as researched; the thirteen reserved questions were left alone.

## Sources actually read

Both pages were fetched and read **2026-10-21**. Original HTML, extracted text, discovered links, request times, HTTP status, curl exit, byte counts and SHA-256 hashes are retained in the adjacent files.

| Record | Source title and URL | What was returned |
|---|---|---|
| `web-timeout` | Brave Search, **“\"yhetil\" \"timeout\"”**, https://search.brave.com/search?q=%22yhetil%22%20%22timeout%22 | Archive listings with timeout-related message subjects and an Org discussion; not a report of the archive service timing out. Linked pages were not fetched. |
| `operator-timeout` | public-inbox, **f:kyle@kyleam.com timeout — search results**, https://public-inbox.org/meta/?q=f%3Akyle%40kyleam.com%20timeout&x=t | One displayed reply, **Re: [PATCH 28/34] watch: add NNTP support**, dated 27 June 2020. Its text corrects a grammar error in a comment near an NNTP timeout setting. It supplies neither a yhetil deployment setting nor an incident account. The separate message page was not fetched. |

Both retrievals returned **HTTP 200 with curl exit 0**. No watched Git endpoint was requested, no new service-timing sample was added, and no code quoted in a result was executed. The search used two different routes: a general web search and the project's public mail archive.

uncertain: the host's current update schedule, hidden update times, and any relationship between those updates and slow replies. These searches do not prove that relevant public evidence is absent everywhere. A word appearing in archived mail is not a measurement of the archive that carries it.

## What changed

**Filed 0, researched 1, answered 0, planted 0.** The courtyard is empty. Sixteen questions remain open, so none was planted. The eight open artisan quests were untouched.

No new finding needed a word or room: the existing account in [[what-the-gaps-can-say]] and [[timeout]] was left unchanged rather than padded with another negative search. The Map was checked against all **697 room files**: every room is listed exactly once, with no missing or extra entries. Its membership needed no edit. The gate's small visit summary was refreshed, and exactly one visit line was appended to the chronicle.

## Verification and scope

`research.py` retained pre-edit markdown hashes and checked the queue and Map before the two searches. It reused the in-castle retrieval helper `../gardener-2026-10-20-operator-notes/fetch.py` without changing it. Requests had finite timeouts and no retries or scheduled follow-up.

`verify.py` checks retrieved bytes and extraction, unchanged rooms, words and queues, Map membership, the single gate-summary edit, and the chronicle's preserved prefix plus exactly one appended visit line. Its executed result is `verification.json`. These checks establish local consistency, not search completeness or current server state. No file in `garden/` was changed.
