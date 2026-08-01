# freshness-gate

A check that data is recent enough to act on. Old data is not wrong data — but acting on stale data as if it were fresh is the lie.

A connection proves access; reconciliation proves the data is real; the freshness gate proves the data is current. Without it, a system can file stale data as confidently as complete data — and the confidence is the lie.

The freshness gate is a time-bound claim: "this data was observed at time T, and T is within the acceptable window for the action being taken." The window is named, not assumed. The gate is checked, not trusted.

Links: [[reconciliation]] [[connection-proves-access]] [[stored-observation]] [[timeout]]
