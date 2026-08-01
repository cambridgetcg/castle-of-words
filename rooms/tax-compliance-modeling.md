# tax-compliance-modeling

*The door opens not when you file, but when you are required to deliver — model the obligation, not the act.*

What gathers here: the craft of modeling tax compliance — how the shape of the obligation, not the filing date, determines when a taxpayer enters the system.

Built understanding from yu, 2026-07-11:

- 2026-07-11 18:32 · For MTD Income Tax, being required to deliver the relevant return — not actual filing — drives entry, so non-filing must never be modelled as an escape. UK-resident qualifying income includes foreign property, and cessation needs an exact date so the final notice and quarterly update remain visible. — yu
- 2026-07-13 12:32 · Provision-level tax data must follow the current amendment topology: an API should name exact current selectors, taxpayer class and effective-date knowledge, and keep missing law explicit. — yu
- 2026-07-13 12:32 · Official guidance often compresses conditional procedure into friendly absolutes; agent data should keep the trigger, notice facts, time limit, payment effect and challenge gap as separate fields. — yu
- 2026-07-13 13:12 · In legal procedure data, [[adjacency]] is not sequence: a possible next door must never be encoded as mandatory without an exact trigger, actor, document, date, tax branch and jurisdiction. Model challenge modes separately too — appeal, correction rejection and superseding return are not interchangeable. — yu
- 2026-07-15 15:12 · A tax ledger must choose the local business ledger before aggregation: cash direction, tax treatment, and external HMRC business identity are separate facts. Source type alone cannot safely scope a filing when one person has multiple trades. — yu
- 2026-07-28 19:43 · Tax identity is not a property of an entity. It is a scoped, effective-dated claim over a subject, jurisdiction, tax or regime, activity or context, and ruleset; overlapping classifications may both be true when their scopes differ. — yu

The three rules, plainly:

1. **Obligation drives entry, not action.** A taxpayer enters the system when they are *required* to deliver a return, not when they actually file. Modeling non-filing as an escape from the system is modeling a lie — the obligation exists whether or not the return is filed.
2. **Foreign property counts.** For UK-resident taxpayers, qualifying income includes foreign property. The border does not shield the asset; residence pulls it into scope.
3. **Cessation needs an exact date.** When a taxpayer leaves the system, the date of cessation must be precise. Without it, the final notice and quarterly update obligations become invisible — the system loses sight of its own boundary.

The law: a compliance model that treats non-filing as exit is a model that has already decided the case. The obligation is the door; the filing is only the knock.

Links: [[obligation]] [[cessation]] [[tax-identity]] · [commerce-kingdom](commerce-kingdom.md) (the same law at the platform level: the platform's value is in the standing offer, not the completed trade — obligation precedes action) · [civic-data-honesty](civic-data-honesty.md) (the same law at the data level: a field that fuses the obligation with the act is a field that lies) · [accounting-product-design](accounting-product-design.md) (the same law at the product level: the inspectable path from evidence to filing and the compliance model that separates obligation from filing are the same move — both refuse to let the act be mistaken for the duty, and both know that the honest system names the gap between what is owed and what is done)
