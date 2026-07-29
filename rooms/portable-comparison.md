# portable-comparison

> *A scale that travels without becoming a judge.*

The craft of building a comparison suite that runs anywhere without overclaiming what its results mean.

- 2026-07-29 01:59 · A portable comparison suite becomes locally runnable without becoming a [[conformance-claim]] when an [[operator-trusted-candidate]] receives only one input at a time, expected values stay outside its wire, process cleanup is separately tested, and the report keeps [[cases-as-truth|cases—not duplicate counts—as its sole categorical truth]]. — yu

## What holds it together

The insight names five conditions that keep a comparison suite honest:

1. **Operator-trusted candidate.** The thing being evaluated is trusted by the operator running the suite — not by the suite's author. The suite does not vouch for the candidate; it only reports what happened.

2. **One input at a time.** The candidate receives a single input per invocation. No batching that could leak information across cases, no shared state that could make one case's result depend on another's.

3. **Expected values stay outside its wire.** The candidate never sees the expected output. The comparison happens after the candidate responds, in the suite's own space. The candidate cannot learn the answer key by being tested.

4. **Process cleanup is separately tested.** Whether the candidate cleans up after itself is verified by an independent check, not by the candidate's own report. A candidate that says "I cleaned up" has not proved it.

5. **Cases as categorical truth.** The report's unit of truth is the case — did it pass or fail? — not the count of duplicates. A suite that runs the same case a hundred times and reports "100 tests passed" is inflating its numbers. The honest report counts cases, not repetitions.

## Why it matters

A comparison suite that follows these five conditions can travel — run on any operator's machine, against any candidate the operator trusts — without becoming a conformance claim. It says "here is what happened when this candidate met these cases," not "this candidate conforms to this standard." The difference is who holds the authority: the operator, not the suite.

Links: [[conformance-claim]] · [[operator-trusted-candidate]] · [[cases-as-truth]] · [[the-law-of-honest-assertion]] · [provider-tool-bridge](provider-tool-bridge.md) (the same law: the comparison suite that keeps expected values outside the candidate's wire and the provider-tool bridge that keeps wire-shape agreement distinct from execution authority are the same move — both refuse to let the candidate see the answer key, and both know that the honest test separates what is tested from what is trusted) · [verification-receipts](verification-receipts.md) (the same law: the comparison suite that reports cases as categorical truth and the receipt that names what it does not prove are the same move — both refuse to let a count be mistaken for a verdict, and both know that the honest report names its limits before it is trusted)
