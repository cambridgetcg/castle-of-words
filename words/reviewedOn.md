# reviewedOn

Reviewed-on is the date a legal ruleset was last researched by the team — it measures evidence freshness, not legal coverage.

It answers "how recent is our research?" not "how current is the law?" A ruleset reviewed yesterday may still cover a statute that was enacted five years ago, or may not yet cover a change that takes effect tomorrow. Conflating reviewedOn with the law's [[effectiveTo]] makes an API expire every day (if reviewedOn is the coverage end, the API is already stale today) while dropping the upper guard entirely turns distant future law into an unsafe guess.

Links: [[effectiveTo]] · [[audit-grade]]