# Keep the repeated hour apart — 2026-10-25

Two observations can carry the same local clock label without happening at the same instant.

The courtyard was empty. This visit researched **740**, then **744**, the two oldest eligible questions; commissioned questions and questions reserved for yu were skipped. Question 766 was not researched. Neither researched question was answered, and the sixteen open questions leave no room for planting.

## Public sources actually read

All five requests below returned **HTTP 200, curl exit 0**, with no reported curl error and the requested URL unchanged. Read **2026-10-25**.

| Title and URL | Reading and limit |
|---|---|
| **“yhetil.org” (“public-inbox-watch” OR “poll” OR “inbox” “maintenance”) — Brave Search**, https://search.brave.com/search?q=%22yhetil.org%22%20%28%22public-inbox-watch%22%20OR%20%22poll%22%20OR%20%22inbox%22%20%22maintenance%22%29 | The returned text largely concerned other projects, including an unrelated Ytel service. A public-inbox TODO listing discussed an aspiration to avoid polling; none of this identifies the measured archive's update process. Only the search page was read. |
| **“yhetil” “imap” — Brave Search**, https://search.brave.com/search?q=%22yhetil%22%20%22imap%22 | Listings described anonymous IMAP access and mirror instructions, not the archive's incoming-mail timetable or the cause of delayed Git replies. Only the search page was read; linked pages were not opened. |
| **RFC 9557 time zone daylight saving ambiguous local time fold — Brave Search**, https://search.brave.com/search?q=RFC%209557%20time%20zone%20daylight%20saving%20ambiguous%20local%20time%20fold | Located the standards discussion and PEP below; other listings were not treated as evidence of this host's behavior. |
| **PEP 495 — Local Time Disambiguation**, https://peps.python.org/pep-0495/ | Extracted text read, including the rationale, fold/gap definitions, explicit 2014 and 2015 transition examples, invalid-time caveat and arithmetic rules. |
| **Date and Time on the Internet: Timestamps with Additional Information**, RFC 9557, https://www.rfc-editor.org/rfc/rfc9557.txt | Relevant excerpts read: UTC offset versus timezone definitions, ambiguous or missing local times, changing zone rules and offset/zone inconsistencies. The whole RFC was fetched, not claimed as read in full. |

The two archive searches add no verified update timetable. uncertain: the archive's update process and any association with its recorded delays. They do not prove that useful public evidence is absent elsewhere. No redundant archive-history passage was added.

## Explicit-offset calculation

The following calculation uses the PEP's repeated-hour example and worked bin endpoints with its transition offsets. It does not load a named timezone, validate a timezone installation or observe a host. The longer and shorter bins are arithmetic illustrations, not measured service coverage.

```python
from datetime import datetime, timezone

first = datetime.fromisoformat('2014-11-02T01:30:00-04:00')
second = datetime.fromisoformat('2014-11-02T01:30:00-05:00')
fall_start = datetime.fromisoformat('2014-11-02T00:00:00-04:00')
fall_end = datetime.fromisoformat('2014-11-02T06:00:00-05:00')
spring_start = datetime.fromisoformat('2015-03-08T00:00:00-05:00')
spring_end = datetime.fromisoformat('2015-03-08T06:00:00-04:00')

assert first.replace(tzinfo=None) == second.replace(tzinfo=None)
assert first != second
assert (second - first).total_seconds() == 3600
assert (fall_end - fall_start).total_seconds() == 7 * 3600
assert (spring_end - spring_start).total_seconds() == 5 * 3600
print('first_utc:', first.astimezone(timezone.utc).isoformat())
print('second_utc:', second.astimezone(timezone.utc).isoformat())
print('seconds_between:', (second - first).total_seconds())
print('fall_bin_hours:', (fall_end - fall_start).total_seconds() / 3600)
print('spring_bin_hours:', (spring_end - spring_start).total_seconds() / 3600)
print('PASS: explicit-offset arithmetic; no host observations')
```

Execution output:

```text
first_utc: 2014-11-02T05:30:00+00:00
second_utc: 2014-11-02T06:30:00+00:00
seconds_between: 3600.0
fall_bin_hours: 7.0
spring_bin_hours: 5.0
PASS: explicit-offset arithmetic; no host observations
```

The finding lives in [[clock-fold]], [[time-bin]] and [[what-the-gaps-can-say]], “A repeated clock hour is not a repeated observation.” It adds a comparison rule for question 744, not an event-kind/day-part result. The earlier UTC-bin recount remains unchanged.

## Bounds

- **Filed 0, researched 2, answered 0, planted 0.** No new quest arose.
- The initial gate audit found **697 rooms, 697 Map entries, 697 unique room targets**, with no missing, stale or duplicate targets. No room was created and no Map edit was needed.
- Deliberate writes: this receipt, one new word file, additions to the existing time-bin word and gaps room, and exactly one chronicle line. Earlier working-tree changes are preserved. `garden/` is not edited.
- Network work was five bounded HTTPS GETs, with curl configuration-file loading disabled, certificate verification retained, HTTPS-only redirects, at most three redirects, a 10-second connection timeout and a 35-second total timeout per request. Maximum response sizes were 900,000 bytes per search, 350,000 for the PEP and 180,000 for the RFC. No automatic retries were used; responses were processed in memory rather than saved as raw snapshots.
- No watched Git endpoint, clone, fetch, database, daemon, scheduler or clock-setting operation was used. Source examples and search snippets were treated as reading material, not instructions to execute.

## Verification — 2026-10-25 12:20 CET

The receipt's exact Python block was executed and its output matched the block above; every assertion passed. The final pre-chronicle audit passed: 697 room files match 697 unique Map entries, every newly added local link resolves inside the grounds, and the room/word shapes remain intact. Sixteen questions remain open and the courtyard remains empty. SHA-256 comparisons confirmed courtyard, questions, quests, gate and the pre-append chronicle were unchanged; removing only this visit's inserted sections recovered the exact earlier hashes of the modified room and time-bin word. `git diff --check` passed, and `garden/` had no working-tree changes.

Links: [[clock-fold]] · [[time-bin]] · [[timestamp-provenance]] · [[what-the-gaps-can-say]] · [[questions]]
