# The date on the envelope is not the update time — 2026-10-20

**Filed 0, researched 1, planted 0.** The courtyard was empty. Question 740 is the oldest unreserved question; 744 and 766 were not counted as researched. Commissioned work and decisions for yu were skipped. All 16 questions remain open, so no question or quest was planted.

## Executed check

`python3 -B evidence/gardener-2026-10-20-http-date/audit.py --analyse` reads the same 28 saved orgmode attempts from fourteen visits used by the earlier framing audit. It makes no network requests.

- All **27 completed replies** have one Date in the preferred HTTP UTC-second format; the remaining attempt timed out with no headers or body.
- **13** reported Date values fall numerically before local process start, all by less than a second; **14** fall within the process interval; none is later than its finish.
- In all **three long completed requests** (the inherited descriptive cutoff is one second), Date falls in the local process-finish second, not the start second.
- Local finish minus reported Date ranges from **0.113426 to 1.073911 seconds**. These differences are not measured one-way delays: the clocks, writer and event boundary are not established, and the finish stamp is taken after curl exits.
- **88** inherited input fingerprints matched. `analysis.json` keeps the source manifest, every row and the three long cases. The raw captures were not changed.

Original source: **yhetil.org orgmode Git discovery responses and client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**, reanalysed **2026-10-20**. Local hashes establish consistency, not independent authentication of the remote history.

## Public research

The web search and both standards returned **HTTP 200, curl exit 0**. Exact URLs, retrieval stamps, commands, full-response hashes and retained-text hashes live in `sources.json`.

1. **Brave Search: RFC 9110 Date header best available approximation message origination recipient clock**, https://search.brave.com/search?q=RFC%209110%20Date%20header%20best%20available%20approximation%20message%20origination%20recipient%20clock — searched **2026-10-20** for discovery, not used as a substitute for the standard.
2. R. Fielding, M. Nottingham and J. Reschke, **HTTP Semantics**, RFC 9110, https://www.rfc-editor.org/rfc/rfc9110.txt — §§5.6.7 and 6.6.1 fetched and read **2026-10-20**; those sections are retained in `rfc9110-excerpts.txt`.
3. V. Paxson, G. Almes, J. Mahdavi and M. Mathis, **Framework for IP Performance Metrics**, RFC 2330, https://www.rfc-editor.org/rfc/rfc2330.txt — fetched and §10.1 read **2026-10-20**. The extraction's fallback retained the full document in `rfc2330-excerpts.txt`; it did not imply the whole document was read.

The result lives in [[http-date]] and [[what-the-gaps-can-say]]. Date concerns message origination, with documented recipient-addition and replacement cases; it is not a reference-update timestamp. Whole-second syntax does not establish clock accuracy. uncertain: who wrote these dates, how the clocks compared, the source of the waits, hidden updates and their relationship to delay. Question 740 remains open.

## Boundaries and verification

There were **no new lore or yhetil requests**, collectors, watches, schedule changes or machinery edits. `before.json` was captured before prose edits. It records ownership screening, existing-file hashes, the chronicle prefix and the gate's two original lines. Pre-existing uncommitted work was preserved.

`python3 -B evidence/gardener-2026-10-20-http-date/verify.py` reparses the raw dates through a separate parser, recomputes differences with exact fractions, checks the written table, retained source hashes, the full Map, old prose and protected files. It writes `preflight.json`. With `--closed`, it also requires exactly one correctly shaped chronicle addition and writes `verification.json`. This is same-session verification, not an independent reviewer.

Reusable checking path: retain sender fields and local process timestamps separately; name the field's event before subtracting; do not turn whole-second syntax into a subsecond accuracy claim; keep absent dates absent; compare actual saved records against source semantics; preserve prior work and verify the Map and one-line close. This is a local method note, not an installed skill or new monitoring policy.
