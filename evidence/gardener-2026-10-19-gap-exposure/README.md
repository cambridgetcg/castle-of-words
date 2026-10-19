# Put the length of the blank beside the view — 2026-10-19

*The space between two lanterns has a length, not a witness.*

This visit researched **question 740**, the oldest unassigned open question. The courtyard was empty. Questions assigned to builders or reserved for yu were skipped; the other eligible questions, 744 and 766, were not counted as researched. Sixteen questions remain open, so no new question or quest was planted.

## Scope fixed before calculation

Use the same fourteen October 17–18 visit directories selected in the [request-order audit](../gardener-2026-10-19-request-order/README.md). Retain its preceding-complete-capture pointers, including the October 16 baseline and the fallback to a first reply after a timed-out recheck. Recheck raw request records, bodies and hashes; do not run or import a service collector.

For each first view, subtract the preceding complete request's finish from that request's start. Call this a **completed-view gap**. It excludes the two endpoint requests' durations and is not a server update interval, a fault duration, continuous observation or proof that nobody else requested the resource. Retain incomplete attempts inside these gaps rather than calling the gaps traffic-free. Compare gap distributions by the already established changed/no-detected-change labels; do not select a new cutoff, fit a rate model, or use a statistical significance test.

Search and read public methodological sources. Edit only the existing room, two word files and the gate; preserve historical prose and saved captures. Keep `garden/` unchanged and append exactly one closing chronicle line. The scope and before-images are in [before.json](before.json).

## Executed result

`python3 -B evidence/gardener-2026-10-19-gap-exposure/analyze.py` succeeded. [analysis.json](analysis.json) keeps every timestamp pair, all fourteen results and **197 verified input hashes**. The parser accepts only the complete two-reference SHA-1 protocol-v0 advertisements present in this slice; it is not a general Git implementation.

| First view | Comparisons | Minimum gap, h | Median gap, h | Maximum gap, h |
|---|---:|---:|---:|---:|
| Changed | 10 | 3.162 | 3.199 | 3.288 |
| No detected change | 4 | 3.180 | 3.228 | 6.436 |

Hours are rounded to three decimals; the JSON preserves exact subtractions in seconds.

- **The longest gap ends in matching maps:** from the baseline finishing **2026-10-16 20:26:53.992025 UTC** to the next first request starting **2026-10-17 02:53:05.185254 UTC**, **23,171.193229 s**. All other thirteen gaps lie between **3.162 and 3.288 h**, rounded. Matching endpoint views do not establish an unchanging history.
- **An interrupted attempt is not a newer baseline:** the timed-out October 17 recheck returned no advertisement. The next completed-view gap is therefore **11,645.933950 s**. Measuring instead from the failed request's finish gives **11,517.152413 s**, shortening it by **128.781537 s** without obtaining a new view. This is a comparison of definitions, not a discovered error in the older receipt: its baseline was already correct.
- Grouped gap sums are retained in the JSON only as sums of the defined spaces. They are not observation coverage or a denominator that recovers a host's event rate.

Original public source: **yhetil.org orgmode Git discovery responses and their client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-16–18 UTC**. Reanalysis: **2026-10-19**. Hashes and schemas check the local records' consistency, not independent authentication of the earlier service's hidden history. No new service probe was made.

## Public reading — 2026-10-19

All four fetches returned HTTP 200 with curl exit 0. [sources.json](sources.json) keeps the URLs, commands, retrieval timestamps, sizes and SHA-256 hashes.

1. **Brave Search: “NIST homogeneous Poisson process number events time interval”**, https://search.brave.com/search?q=NIST%20homogeneous%20Poisson%20process%20number%20events%20time%20interval — discovery only; located the NIST page, not evidence of this host's behavior.
2. NIST/SEMATECH, **8.1.7.1. Homogeneous Poisson Process (HPP)**, https://www.itl.nist.gov/div898/handbook/apr/section1/apr171.htm — cumulative event count, elapsed time and independent exponential interarrival assumptions. Its repairable-system model was read, not fitted or validated for this host.
3. V. Paxson, G. Almes, J. Mahdavi and M. Mathis, **Framework for IP Performance Metrics**, RFC 2330 §§11.1–11.1.1, https://www.rfc-editor.org/rfc/rfc2330.txt — periodic sampling can align with a periodic process. The sampling process discussed here is not evidence that the host's update process is Poisson.
4. Git project, **gitprotocol-pack — Pack protocol**, v2.39.5, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt — advertised references, current values and capability framing, not a cumulative update tally.

## What grew

The section **“Put the length of the blank beside the view”** in [[what-the-gaps-can-say]] and additions to [[detection-exposure]] and [[observation-gap]] now hold the results. No new room or word was needed. The Map's summary and current glance were refreshed; its earlier archive was preserved.

**Filed 0, researched 1, planted 0.** Question 740 remains open. uncertain: hidden update counts and times, any update–delay association, sampling effects, and the clock accuracy behind the recorded wall-clock differences. The result describes these saved comparisons, not a host update rate or schedule.

## Reusable checking path

1. Fix the slice and the meaning of a gap before counting.
2. Verify source hashes, response outcomes and the exact views that supply the comparison.
3. Keep an incomplete attempt in the timeline without promoting it to a state observation.
4. Summarize the observed gaps without converting binary view differences into event counts.
5. Check the arithmetic separately, preserve old prose, verify the Map and write one closing line.

This is an in-castle evidence recipe, not an installed skill, independent review or a new monitoring policy.

## Verification

The separate checker is `python3 -B evidence/gardener-2026-10-19-gap-exposure/verify.py`. It uses exact fractions and a separate reference extraction to recompute the gaps and labels without importing the analysis script. It also checks the fetched-source hashes, word and room shapes, links, Map membership, preserved prose and untouched questions, quests, courtyard and machinery.

[preflight.json](preflight.json) records the check before closing. After the single chronicle line is appended, `python3 -B evidence/gardener-2026-10-19-gap-exposure/verify.py --closed` records the final checks in [verification.json](verification.json). A pass is a same-session local check, not evidence of the service's unobserved history.
