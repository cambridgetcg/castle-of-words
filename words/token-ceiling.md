# token-ceiling

A cap on how many outstanding tokens (links, invitations, sessions) may exist at once, distinct from a time-window rate limit.

A token ceiling bounds storage and fan-out — it says "no more than N unclaimed links may exist." But a caller who controls and consumes the links can cycle beneath the ceiling: claim one, request another, repeat. A true attempt limit needs a separate bucket that counts every attempt and retains the count even after the token is consumed.

Links: [[rate-limiting]] · [[fail-closed]] · [[rate-limiting]]
