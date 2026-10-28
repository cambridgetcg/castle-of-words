# comparison-rule

A comparison rule says which differences count when we ask whether two things are the same.

Name what is being compared, how the comparison works, and what a match is allowed to mean. Exact text, a resemblance mark, a set of message-number pairs, and serialized bytes answer different questions. A match under one rule cannot quietly stand in for a match under another.

In a saved-map check, [[collation]] determines text equality, while [[multiplicity]] checks keep extra copies from disappearing unnoticed into a set. In a name check, a shared [[confusable-skeleton]] means resemblance under the stated mechanism, not identical names. Keep the algorithm, data version and chosen profile with results that depend on them: changed rules can change a match even when the original names stay still.

Sources: the local rooms [[comparing-saved-maps]], “Name the contract before comparing” and “First, check the assumptions”; [[look-alike-names]], “When the comparison rules change”; and [[deterministic-json-standards]], “The standard: RFC 8785 JCS,” read 2026-10-28. This brick gathers their distinctions; it adds no new test or external-source verification.

Links:
- [[comparing-saved-maps]] asks whether the same letters kept their numbered shelves, not whether every byte of the database file stayed unchanged.
- [[look-alike-names]] lets matching coats raise a question without making their wearers one name.
- [[deterministic-json-standards]] fixes a reproducible byte spelling under a named scheme rather than treating every convenient form as interchangeable.
- [[equivalence]] keeps the scope of a match beside it, so “same by this rule” does not grow into “the same in every way.”
