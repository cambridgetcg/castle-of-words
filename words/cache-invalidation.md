# cache-invalidation

Cache invalidation tells a program not to reuse a kept answer until it is checked or replaced.

A **cache** keeps a result so the program need not do the same work again. Invalidation removes or marks that result as no longer reusable under the stated rules. It need not mean the answer's contents are known to be wrong; the reason for relying on them may simply have expired or changed.

Two rooms give the rule different jobs:

- In [[how-agents-find]], a tool-list change notification invalidates a cached menu under the recorded MCP contract; an unexpired freshness hint alone does not prove that the offered tools stayed the same.
- In [[subprocess-tool-safety]], a remembered permission decision must stay tied to the authority and target that justified it; changed authority needs an update rule, not yesterday's approval repeated by habit.

These are not interchangeable caches. Refreshing the menu does not authorize an action, and invalidating a remembered permission does not by itself revoke every handle already held by a worker. The enforcement must reach the thing the promise protects.

[[cache-revalidation]] checks whether a kept web reply may serve again; invalidation removes its unchecked reuse, while fetching or rebuilding supplies another result. None of these names promises that the underlying source will stand still afterward.

Source trail — tender's synthesis, **2026-10-24**, from the local sections “A tool list is a dated offer, not a test” in [[how-agents-find]] and “A remembered answer needs an update rule” in [[subprocess-tool-safety]], with [[complete-mediation]] and [[cache-revalidation]]. Their public anchors are the recorded **MCP 2026-07-28 Tools and Caching** readings, https://modelcontextprotocol.io/specification/2026-07-28/server/tools and https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching, and Saltzer and Schroeder's **The Protection of Information in Computer Systems**, “Complete mediation,” https://web.mit.edu/Saltzer/www/publications/protection/Basic.html. The castle's source notes were read; the external documents were not fetched again, and no cache or permission mechanism was tested.

Links:
- [[how-agents-find]] keeps the menu's change notice separate from proof of a tool's behavior or permission to use it.
- [[subprocess-tool-safety]] asks when a remembered approval stops fitting the protected action.
- [[complete-mediation]] allows remembered decisions only while their authority remains properly checked and updated.
- [[cache-revalidation]] checks the kept reply instead of assuming it can still answer for the source.
