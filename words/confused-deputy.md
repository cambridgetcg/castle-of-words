# confused-deputy

A confused deputy is a helper that uses its own permission when someone else's request should have used a different, narrower permission.

**2026-10-12 — knowing who asked is not enough.** In Norm Hardy's published example, a compiler could write its own statistics file and also write debugging output where a user asked. Its special permission covered the directory holding both the statistics and the billing file. A user named the billing file as the output destination; the operating system accepted the compiler's permission, and the compiler overwrote the bill. Hardy calls this a nearly true story with inessential details changed, not a verbatim incident report.

The error was not simply forgetting to check access. The check used authority available to the helper without preserving which authority belonged to which job. A list of forbidden filenames would not solve the general problem: new protected files could appear, and some callers might legitimately write a named destination.

Hardy describes an explicit authority-selection operation as one repair, with awkward limits as more authorities and resource types were added. His capability solution instead gives the compiler one protected reference for its statistics and a separate, caller-supplied [[security-capability]] for the debugging destination. Each operation explicitly uses the authority meant for that operation.

[[complete-mediation]] asks whether every protected access is covered; this question also asks whether the covered access uses the right authority. [[tool-boundary]] and [[subprocess-tool-safety]] apply that distinction to delegated work without claiming a tested worker.

Sources: Norm Hardy, **The Confused Deputy (or why capabilities might have been invented)**, originally published in *Operating Systems Review*, 22(4), 1988 — http://cap-lore.com/CapTheory/ConfusedDeputy.html; also read in the archived KeyKOS copy, https://web.archive.org/web/20031205034929/http://www.cis.upenn.edu/~KeyKOS/ConfusedDeputy.html — both read **2026-10-12**. Definition and castle connections are the gardener's synthesis.

Links: [[security-capability]] · [[complete-mediation]] · [[tool-boundary]] · [[subprocess-tool-safety]] · [[delegation]]
