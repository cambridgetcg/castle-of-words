# Put the clock on the count — 2026-10-19

The courtyard was empty. This visit researched questions **740 and 744**, oldest eligible first, without claiming either answered. The other eligible question, 766, was not researched. Sixteen open questions leave no room for planting; commissioned work and decisions reserved for yu were left alone.

## Fixed scope and actual result

[before.json](before.json) records the scope before calculation: use the same fourteen October 17–18 visit directories as the request-order audit; sort each orgmode request by its own start into **[00:00,06:00), [06:00,12:00), [12:00,18:00), [18:00,24:00) UTC**. These are chosen clock bins, not host working hours. Keep the first-view comparison, first wait, completed recheck and timed-out recheck separate. No new service probes, statistical tests or inferred event kinds.

`python3 -B evidence/gardener-2026-10-19-clock-bins/analyze.py` executed successfully. [analysis.json](analysis.json) keeps each row and **58 input-file hashes**. It checks source-record body hashes and parses the complete two-reference Git v0 advertisements in this slice; it is not a general Git parser.

| UTC bin | First views | Changed / no detected change | First waits ≥ 1 s | Completed rechecks ≥ 1 s | Timed-out rechecks |
|---|---:|---:|---:|---:|---:|
| 00:00–06:00 | 3 | 0 / 3 | 0 | 2 | 0 |
| 06:00–12:00 | 4 | 3 / 1 | 0 | 0 | 0 |
| 12:00–18:00 | 4 | 4 / 0 | 0 | 0 | 0 |
| 18:00–24:00 | 3 | 3 / 0 | 1 | 0 | 1 |

There were fourteen recheck attempts, one per visit. The cutoff is an inherited descriptive convention. **Five of ten changed first views followed completed-view gaps crossing a bin boundary; eight of all fourteen gaps crossed one.** The bin of discovery is not the bin of a known underlying update. Even a gap within one bin does not establish update timing: the endpoint request durations, cache behavior and hidden history remain separate limits.

Original public source: **yhetil.org orgmode Git discovery responses and client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**, with the preceding baseline on **2026-10-16 UTC**; reanalysed **2026-10-19**. Hash checks establish consistency of local saved records, not independent authentication of their history. No old capture was edited or collector executed.

## Web reading

All three retrievals returned HTTP 200 with curl exit 0. [sources.json](sources.json) retains URLs, commands, retrieval times, sizes and hashes.

- **Brave Search: “NIST contingency table counts categories sampling”**, https://search.brave.com/search?q=NIST%20contingency%20table%20counts%20categories%20sampling — searched **2026-10-19**; found the NIST page, discovery only.
- Klyne and Newman, **Date and Time on the Internet: Timestamps**, RFC 3339 §§4.2–4.4, https://www.rfc-editor.org/rfc/rfc3339.txt — read **2026-10-19** for UTC offsets and unqualified local time, not the choice of bins or any host schedule.
- NIST/SEMATECH, **7.4.5. How can we compare the results of classifying according to several categories?**, https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm — classification and row totals read **2026-10-19**. Its wafer-defect example does not validate a service-observation model.

The understanding lives in [[what-the-gaps-can-say]], “Put the clock on the count,” and [[time-bin]]. The gate's Map summary was updated. **Filed 0, researched 2, planted 0; both questions remain open.** uncertain: hidden change times, update–delay association, local work hours and fault kinds. No question was closed merely to free a planting slot.

## Reusable checking path

Fix the observation unit and bins before counting; read each timestamp with its offset; keep request order and missing outcomes; count observations as well as detected differences; distinguish a discovery bin from event timing; recheck the table against raw records; verify the Map and unchanged machinery; append exactly one closing chronicle line. This recipe stays in the castle, not in an installed skill or a changed monitoring policy.

`verify.py` recomputes the table from raw records with a separate classification path, checks body comparisons and input/source hashes, and validates the document edits and complete Map membership. Run without arguments before closing, then with `--closed` after the chronicle entry. It is a same-session check, not an independent reviewer or proof of the unobserved service history.
