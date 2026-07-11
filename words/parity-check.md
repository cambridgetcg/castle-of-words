# parity-check

A comparison of two observations of the same thing that names what is expected to differ before comparing what should be the same.

A parity check first names the dynamic fields (timestamps, request IDs, cache headers) and normalizes them, then compares everything else. Raw byte equality without normalization confuses the observer's timing with a change in the observed system. The check is honest only when it declares what it will ignore and why.

Links: [[observation-parity]] · [[deployment-claim]]
