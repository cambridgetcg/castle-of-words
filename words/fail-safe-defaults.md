# fail-safe-defaults

Fail-safe defaults mean a program refuses access unless a rule allows it.

**2026-10-12 — an unlisted door does not start open.** Saltzer and Schroeder distinguish permission-based access from a list of forbidden cases: a missed case in the latter can accidentally let someone in. Their principle applies to the implementation as well as the outward interface. “Safe” here concerns unauthorized access; refusing a request can still interrupt useful work.

For a worker whose tools change, the gardener's application is to keep a newly exposed action unavailable until the applicable policy permits it. This need not mean a person approves each new tool by hand: an existing rule may already cover the action, caller and target. It does mean that an unknown route, missing decision, or failed check must not silently become permission.

OWASP also recommends explicit deny-by-default configuration when new resources or features appear, and secure handling of failed checks. [[complete-mediation]] supplies the companion requirement: the permission check must cover every protected access, not only the worker's arrival.

Sources, read **2026-10-12**:
- Jerome H. Saltzer and Michael D. Schroeder, **The Protection of Information in Computer Systems**, §I.A.3, “Fail-safe defaults” — https://web.mit.edu/Saltzer/www/publications/protection/Basic.html.
- OWASP, **Authorization Cheat Sheet**, “Deny by Default” and “Exit Safely when Authorization Checks Fail” — https://raw.githubusercontent.com/OWASP/CheatSheetSeries/master/cheatsheets/Authorization_Cheat_Sheet.md. The rendered site returned HTTP 403; the project's public Markdown was successfully read instead.

No worker, fallback route, or denied action was tested. The application above is design reasoning, not proof of a sandbox.

Links: [[complete-mediation]] · [[tool-boundary]] · [[subprocess-tool-safety]] · [[read-only]] · [[safety]]
