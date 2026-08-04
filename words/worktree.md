# worktree

A worktree is a separate working copy of a git repository, attached to the same object store — a temporary room for a feature that can be built, committed, and cleaned away without disturbing the main workspace.

A temporary feature worktree should end with one verified commit fast-forwarded into its clean owning branch, then the temporary worktree and short-lived branch should be removed. Prune only metadata whose paths are confirmed absent, and never use a dirty canonical worktree as a merge hub.

Links: [[git]] [[branch]] [[this-machine]]
