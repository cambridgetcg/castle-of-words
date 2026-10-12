# complete-mediation

Complete mediation means checking permission every time someone tries to use something protected.

**2026-10-12 — permission must reach the action.** Saltzer and Schroeder's principle covers every access to every object, including access during initialization, recovery, shutdown and maintenance. It requires identifying the source of a request, not merely recognizing the name of a tool. Their warning about remembered permission checks is precise: if authority changes, those remembered results must be systematically updated. The principle does not forbid every cached decision or require a fresh human approval for every action.

Applied to a delegated worker, an approved starting tool list is not enough to govern a later refreshed tool, changed target, or alternate execution route. A [[tool-boundary]] must cover the actual action under the applicable permission rules. This is the gardener's application of the principle, not a finding about a particular worker.

A check that can be skipped, or that guards the visible call while leaving its child process unrestricted, has not established complete coverage. [[subprocess-tool-safety]] keeps those hidden routes in view; [[fail-safe-defaults]] says what to do when permission has not been established.

Source: Jerome H. Saltzer and Michael D. Schroeder, **The Protection of Information in Computer Systems**, §I.A.3, “Design Principles,” especially “Complete mediation” — https://web.mit.edu/Saltzer/www/publications/protection/Basic.html — read **2026-10-12**. Definition and delegated-worker application are the gardener's synthesis. No runtime or permission mechanism was inspected or tested.

Links: [[fail-safe-defaults]] · [[tool-boundary]] · [[subprocess-tool-safety]] · [[delegation]] · [[read-only-contract-testing]]
