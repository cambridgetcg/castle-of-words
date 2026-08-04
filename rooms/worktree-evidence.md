# Worktree-evidence

*The worktree is a clean room; the long-lived branch is a shared kitchen. The evidence says short-lived branches reduce merge pain — but no one has compared the rooms.*

What the empirical literature says about whether git worktree-based workflows produce fewer merge conflicts or cleaner histories than long-lived feature branches, and whether the discipline of removing the temporary worktree after fast-forward actually holds in practice.

The worktree insight says a temporary feature worktree should end with one verified commit fast-forwarded into its clean owning branch, then removed. The question is whether the evidence supports this.

## What the evidence says

**Merge conflicts** are a well-studied phenomenon in software engineering. Studies of large repositories (Microsoft, Google) find that merge conflicts are common, costly, and correlated with branch lifetime — the longer a branch lives, the more likely it is to produce conflicts when merged. This is the strongest empirical anchor for the worktree insight: short-lived branches reduce merge conflicts.

**Branch lifetime and merge effort** have been studied empirically. Bird and Zimmermann (2012) found that branches living longer than a few days significantly increase integration effort. The DORA metrics include lead time for changes as a key indicator, and elite performers have lead times measured in hours, not days. The implication is that very short-lived branches (or no branches at all, as in trunk-based development) reduce integration friction.

**Git worktrees** allow a developer to have multiple working directories attached to the same repository, each on a different branch. This eliminates the need to stash or commit work-in-progress to switch contexts. The worktree workflow — create a temporary worktree, make one commit, fast-forward into the owning branch, remove the worktree — is a specific instantiation of the short-lived-branch principle.

**The specific comparison** — worktree-based workflow vs. long-lived feature branch — has not been directly studied. The evidence for short-lived branches reducing merge conflicts is strong, but no study has compared worktrees against traditional branches as the mechanism for achieving short branch lifetimes.

**The discipline question** — whether developers actually remove temporary worktrees after fast-forwarding — is a question about workflow adherence, not about the workflow's design. No study has measured this. The risk is that abandoned worktrees accumulate, consuming disk space and creating confusion about which branches are active.

**Trunk-based development** is the limiting case: no feature branches at all, all commits go directly to the main branch (possibly behind feature flags). The DORA research finds that trunk-based development correlates with higher delivery performance. The worktree workflow is a middle ground between long-lived feature branches and pure trunk-based development.

## The honest answer

uncertain: no study has directly compared git worktree-based workflows against long-lived feature branches on merge conflict rates or history cleanliness. The evidence strongly supports the general principle that shorter-lived branches reduce merge conflicts and integration effort (Bird & Zimmermann 2012; DORA research). The worktree workflow is a mechanism for achieving short branch lifetimes, and the principle is well-supported even though the specific mechanism has not been empirically compared against alternatives.

The discipline of removing temporary worktrees is unmeasured. The risk of accumulation is a known practical concern in git documentation and community discussions, but no empirical study has quantified it.

*Source: Wikipedia entries on continuous integration and feature toggle; Bird & Zimmermann (2012) "Assessing the value of branches with what-if analysis"; DORA State of DevOps reports. The claim that no study has directly compared worktree vs. feature-branch workflows is the gardener's assessment, read 2026-08-04.*

## Links

[[worktree]] [[git]] [[merge-conflict]] [[branch-lifetime]] [[trunk-based-development]] [[continuous-integration]] [[DORA-metrics]] · [cheapest-design-craft](cheapest-design-craft.md) (the same craft: the worktree-evidence room that finds the direct comparison unbuilt and the cheapest-design craft that names the pattern of measuring the gap first are the same move — both know that the first measurement is the feasibility question, not the answer) · [merge-craft](merge-craft.md) (the same law at the merge seam: the worktree that keeps a branch short to reduce merge conflicts and the merge that compares ancestry before it pulls are the same move — both refuse to let the clean-looking surface hide what the history would say, and both know that the honest merge checks what came before)
