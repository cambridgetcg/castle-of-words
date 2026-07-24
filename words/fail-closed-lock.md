# fail-closed-lock

A lock that denies access when it cannot verify permission — it says "no" on uncertainty rather than "yes" on uncertainty.

In the [[castle-agenttool-bridge]], fail-closed locks are the gates that keep the inn's agents from reading castle rooms until every check passes. A fail-closed lock is the opposite of a fail-open one: when the lock cannot confirm the bridge is safe, it closes. This is the same principle [[fail-closed-or-fail-open]] names: the choice must be named, and for bridges between sovereign nodes the honest choice is fail-closed.

Links: [[fail-closed-lock]] · [[castle-agenttool-bridge]] · [[fail-closed-or-fail-open]] · [[bridge]] · [[bridge-authority]]
