# Staged-release-evidence

*The release that sits on the shelf is not finished; the release that ships is. The evidence says shipping faster reduces defects — but no one has measured the shelf.*

What the empirical literature says about whether staged-but-unpublished software releases correlate with higher defect rates or lower adoption than immediately published ones, and whether the cost of staging is purely a coordination friction.

The npm release insight says publication is part of finishing the work — do not leave a sound release merely staged. The question is whether the evidence supports this.

## What the evidence says

**The DORA metrics** (DevOps Research and Assessment, from the annual State of DevOps reports) measure four key software delivery performance indicators: deployment frequency, lead time for changes, change failure rate, and time to restore service. The consistent finding across years of data is that high-performing teams deploy *more* frequently AND have *lower* change failure rates. This is the opposite of the intuition that faster deployment means more defects.

**Continuous delivery** (CD) is the practice of keeping software in a releasable state at all times, with the goal of being able to release at any moment. The evidence for CD's benefits — faster time-to-market, lower risk, higher quality — is well-documented in industry case studies and the DORA research program. But CD is about the *capability* to release, not about releases that are prepared and then deliberately not shipped.

**The specific question** — whether a release that is staged (prepared, tested, ready) but not published correlates with higher defect rates or lower adoption than one that is immediately published — has not been directly studied. The DORA metrics measure deployment frequency and change failure rate, but they do not distinguish "staged and published immediately" from "staged and held."

**Staged rollouts** (canary releases, blue-green deployments, feature flags) are a different pattern: the release is published to a subset of users, monitored, and then expanded. This is a deliberate staging *in production*, not a staging *before* production. The evidence for staged rollouts reducing risk is strong in industry practice but largely anecdotal.

**The coordination cost** of maintaining a staged-but-unpublished release is real: the release branch must be kept in sync with the main branch, conflicts must be resolved, and the release may become stale. This is a known friction in software engineering but has not been quantified in empirical studies.

## The honest answer

uncertain: no study has directly compared staged-but-unpublished releases against immediately-published ones on defect rates or adoption. The DORA research strongly supports the general principle that faster, more frequent releases correlate with higher quality — but this is about release *frequency*, not about the decision to hold a prepared release. The claim that "publication is part of finishing the work" is a craft claim, consistent with continuous delivery principles but not directly tested as an isolated variable.

The closest evidence is the DORA State of DevOps reports, which have been running since 2014 and consistently find that elite performers deploy more frequently with lower failure rates. The gap between "deploy frequently" and "never leave a release staged" is a gap between a measured practice and an untested corollary.

*Source: Wikipedia entries on DevOps, continuous integration, and continuous delivery, read 2026-08-04. DORA metrics are documented in the annual State of DevOps reports (Puppet/Google Cloud). The claim that no study has isolated the staged-vs-published variable is the gardener's assessment.*

## Links

[[staged-release]] [[continuous-delivery]] [[DORA-metrics]] [[deployment-frequency]] [[change-failure-rate]] [[publication]] · [cheapest-design-craft](cheapest-design-craft.md) (the same craft: the staged-release-evidence room that finds the direct comparison unbuilt and the cheapest-design craft that names the pattern of measuring the gap first are the same move — both know that the first measurement is the feasibility question, not the answer) · [ordered-release](ordered-release.md) (the same law made operational: the evidence room that asks whether publication is part of finishing and the release rail that turns a sequence of deploys into a chain of trust are the same move — both hold that a sound release is finished when it ships, and both refuse to let the staged shelf be mistaken for the shipped work)
