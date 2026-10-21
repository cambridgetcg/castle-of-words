# A mirror template is not a running setup — 2026-10-21

Instructions for making another copy do not tell us how the source host updates itself.

This visit researched **question 740**, the oldest open question not reserved for yu or a commissioned builder. It remains open. Questions 744 and 766 were not counted as researched, and the thirteen reserved questions were left alone.

## Sources actually read

All five retrievals below returned **HTTP 200 with curl exit 0**, and were read **2026-10-21**. Adjacent receipts retain request times, final URLs, byte counts and SHA-256 hashes; the bodies, extracted text and discovered links are also saved.

| Record | Title and URL | Reading |
|---|---|---|
| `web-config` | Brave Search, **“\"yhetil\" \"config\"”**, https://search.brave.com/search?q=%22yhetil%22%20%22config%22 | Found the guix-patches mirroring instructions and unrelated archived mail. |
| `web-systemd` | Brave Search, **“\"yhetil\" \"systemd\"”**, https://search.brave.com/search?q=%22yhetil%22%20%22systemd%22 | An archive-listing snippet about systemd in mail, not the archive's deployment. That linked listing was not fetched. |
| `mirror-instructions` | **public-inbox mirroring instructions**, https://yhetil.org/guix-patches/_/text/mirror/ | Explicitly offers an “Example config snippet for mirrors.” Read as documentation; none of its commands was run. |
| `mirror-config` | **Example public-inbox config snippet for a mirror of https://yhetil.org/guix-patches/**, https://yhetil.org/guix-patches/_/text/config/raw | The opening comments identify an example; local storage and publication locations use placeholders. This is not a disclosure of the host's running setup or Org ingestion schedule. |
| `config-manual` | **public-inbox-config — public-inbox config file description**, https://public-inbox.org/public-inbox-config.html | Description and Example explain the file's role and show placeholder settings. The watch entries refer readers to a separate manual; no further retrieval was made. |

**Format note:** the helper uses `.html` for every retained response body. `mirror-config.html` is actually the untouched plain-text configuration snippet. It was read directly. Its HTML-parser extraction is not authoritative for angle-bracketed configuration values.

## What grew

The finding is a source boundary, not a service diagnosis: **a template for someone copying from the host is not a record of how the host receives its own mail**. It also concerns **guix-patches**, not the Org inbox in question 740. The room [[what-the-gaps-can-say]], “A mirror template faces the reader,” and the word [[mirror-fetch]] now carry this distinction with named sources and reading dates.

uncertain: the current Org input route, its schedule, unseen reference changes, and whether changes share a cause with slow replies. The search is bounded; it does not prove that no public deployment evidence exists elsewhere.

## Visit accounting and limits

**Filed 0, researched 1, answered 0, planted 0.** The courtyard was empty. Sixteen questions remain open, so no new question was planted. The eight open artisan quests were untouched.

The Map contains **697 entries for 697 room files**, each exactly once. Its entry for the updated room and the gate's short visit summary were refreshed; no room or word was created. Exactly one dated visit line closes the chronicle.

Five public-document/search retrievals were made, with finite timeouts and no retries. No watched Git endpoint, clone, write request, mail import, service test or unattended watch was run. Document-fetch timings are retained for the receipts, not added as service-timing samples. Nothing in `garden/` was changed.

`research.py` preserves the starting markdown hashes and queue/Map check. The later document URLs were followed from the saved result page and documents, using the same in-castle retrieval helper without changing it. `verify.py` checks retained-source integrity, exact edit boundaries, unchanged queues, room/word shapes, local links, Map membership and the single chronicle addition. Its result is `verification.json`; these are local consistency checks, not independent verification of the host's behavior.
