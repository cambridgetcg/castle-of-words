# recovery-rule

A recovery rule says what checks must pass before we stop marking a problem as active.

The rule is a choice about the record, not proof that nothing went wrong between checks. The castle's two-clean-knock rule can close a recorded spell without promising that slowness will never return. Missing readings are not passing checks.

Source: Prometheus, **Alerting rules**, https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/ — read 2026-10-09. Its configurable `for` and `keep_firing_for` clauses illustrate the distinction between observations and alert state; they do not validate the castle's chosen count. Local application: [[what-the-gaps-can-say]], §707, 2026-10-09.

Links: [[what-the-gaps-can-say]] · [[latency-weather]] · [[observation-gap]]