# cases-as-truth

The principle that a comparison report's unit of truth is the case, not the count — one case run once is one data point, and running it a hundred times does not make it a hundred truths.

A suite that reports "100 tests passed" when it ran the same 10 cases 10 times each is inflating its numbers. The honest report counts distinct cases, not repetitions. Duplicate runs may be useful for catching flakiness, but they are not independent evidence. The categorical truth is: did this case pass or fail?

Links: [[portable-comparison-suite]] · [[conformance-claim]]
