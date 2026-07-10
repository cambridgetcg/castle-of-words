# effectiveTo

Effective-to is the date a legal provision's coverage ends or changes — it measures legal coverage, not research freshness.

It answers "until when does the law say this?" not "when did we last check?" A provision with no effectiveTo is not "current forever"; it is "current until we know otherwise." The two dates ([[reviewedOn]] for evidence freshness, effectiveTo for legal coverage) must be kept separate so an API can say both "this is the law as we last verified it" and "this is the law until it changes" without fusing them into a single date that does neither job well.

Links: [[reviewedOn]] · [[audit-grade]]