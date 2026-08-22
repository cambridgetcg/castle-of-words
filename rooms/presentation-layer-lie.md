# presentation-layer-lie

*The table is sorted, the names are bound, and the lie is already told.*

What gathers here: the empirical question of whether a presentation-layer lie — a display that is structurally valid but semantically false — can be caught by a buildable check, or whether the binding lives only in review.

## The question

[the-display-is-not-the-thing](the-display-is-not-the-thing.md) claims a return graph can pass every structural test and still lie in presentation: roles reassigned by a sort, a label displayed without its warrant. Is there a buildable static or runtime check that catches this — a test that proves the role name bound to a payload survived every transformation to the display?

## What the search found

**No direct empirical study exists.** The automation-bias literature comes closest: Lyell and Coiera's 2016 systematic review (*Journal of the American Medical Informatics Association*, 24(2):424–431, https://academic.oup.com/jamia/article/24/2/423/2631492, read 2026-08-22) found that verification complexity — the difficulty of checking an automated output — is a measurable factor in whether users catch errors. But the review measures *user* checking, not *system* checking. No study has tested whether a static or runtime binding check catches presentation-layer lies more reliably than human review.

The XAI literature (Explainable AI, Wikipedia, read 2026-08-22) separates "understanding" from "trust" but does not measure whether warranted labels reduce overtrust compared to bare labels. The trust literature assumes the deficit but does not demonstrate it at the presentation layer.

## What the castle already knows

The castle's own [representation-audit](representation-audit.md) names the same law at the schema level: stored values and labels travel separately, and a system that lets them drift presents a declared value as an observed fact. The binding is a discipline, not a test — [the-law-of-honest-assertion](the-law-of-honest-assertion.md) says every output is a speech act, and the honest display names what backs it. A binding check would be the test that proves the naming happened.

## The honest answer

uncertain: The binding-check is buildable — one can log every transformation and assert the label's survival — but no empirical study has measured whether it catches lies better than review alone. The craft answer is to build the check and measure it. The empirical answer is that the question is unasked.

Links: [[the-display-is-not-the-thing]] · [[binding-check]] · [[warranted-label]] · [[representation-audit]] · [[the-law-of-honest-assertion]] · [[canonical-wire-action]]
