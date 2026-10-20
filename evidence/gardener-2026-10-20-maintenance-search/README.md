# A maintenance search, not an incident report — 2026-10-20

This search did not add a new answer.

The courtyard was empty. Of **16 open questions**, **13** were commissioned or reserved for yu; the remaining questions, in age order, were 740, 744 and 766. This visit researched only **740**: whether changes in the Org archive's advertised Git view are associated with slow replies. It made a bounded search for public maintenance or performance reports rather than adding another probe to the watched service.

## Sources and retrieval limits

Read **2026-10-20**. Exact UTC times, commands and returned HTTP metadata are in the `*-receipt.json` files.

| Record | Title and URL | What actually returned |
|---|---|---|
| `web-maintenance` | Brave Search, **“\"yhetil.org\" \"maintenance\"”**, https://search.brave.com/search?q=%22yhetil.org%22%20%22maintenance%22 | HTTP 200. The returned search page was read. It listed archived mailing-list discussions and the ownership question already covered by the castle's 2026-10-17 research, not a new service-maintenance report. No search snippet was treated as evidence of current operations. |
| `operator-performance` | Attempted public-inbox search, **f:kyle@kyleam.com performance**, https://public-inbox.org/meta/?q=f%3Akyle%40kyleam.com%20performance&x=t | curl exit 7: connection failed before an HTTP response. No retrieved search result or empty result set is claimed. |
| `indexed-performance` | Alternative Brave Search query, **site:public-inbox.org/meta/ \"yhetil\" \"performance\"**, https://search.brave.com/search?q=site%3Apublic-inbox.org/meta/%20%22yhetil%22%20%22performance%22 | HTTP 429. Rate-limited; no usable search results claimed. |

The third request was a different search route after the archive connection failed. Collection stopped after these **three attempts**, without automatic retries, authentication, watched Git requests, or service changes. A failed connection and a rate limit are retrieval limits, not evidence that relevant reports do not exist.

uncertain: the current ingestion schedule, hidden update times and relation to slow replies. **Question 740 stays open.** The historical operator statement and its limits already live in [[what-the-gaps-can-say]], “A historical voice is not a current incident report.” [[mail-ingestion]] and [[freshness-target]] retain the other dated findings. These pages were not enlarged with another copy of the same uncertainty. No question was marked answered; questions 744 and 766 were not counted as researched.

## The grounds

- **Filed 0, researched 1, answered 0, planted 0.** The courtyard header remains. With **16 open questions**, planting would exceed the allowed threshold; no quest was added.
- **697 rooms and 697 Map entries**, with each room listed exactly once. The Map needed no edit.
- Rooms, words, questions, quests and gate were left unchanged. Existing uncommitted work was preserved. Nothing in `garden/` was edited.
- Exactly one visit line was appended to `chronicle.md`.

## Evidence and verification

`research.py` captured `before.json` and `preflight.json`, then made the first two requests. It reuses the reviewed retrieval function in `../gardener-2026-10-20-operator-notes/fetch.py` without changing that helper. The alternative query used the same function with label `indexed-performance` and the URL above. Each receipt records its actual command, result, body length and SHA-256. Returned bytes, text extraction and discovered links are kept separately. The failed connection has no body file; its empty convenience text file is not a retrieved document.

`verify.py` checks the saved retrievals, unchanged castle pages, room-to-Map correspondence, question count, and the chronicle's unchanged prefix plus exactly one appended line. Its executed output is `verification.json`. These checks validate this local record; they neither diagnose the remote service nor turn an incomplete search into proof of absence.
