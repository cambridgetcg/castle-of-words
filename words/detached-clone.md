# detached-clone

A Git clone checked out at a specific commit, not attached to any branch. It is disposable — you can test against it, throw it away, and the real working tree is untouched. The ordinary test gate can exercise a fail-closed command against a detached clone of HEAD without weakening the production boundary.

Links: [[dirty-checkout]] [[fail-closed]] [[receipt]]
