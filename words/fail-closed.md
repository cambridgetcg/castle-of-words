# fail-closed

*A door that locks when it cannot see who is knocking.*

Fail-closed means: when the system cannot be certain, it denies. An API that fails closed refuses to widen a query when the filter is empty, refuses to serve data when the caller's scope is unknown, and refuses to cache free text when the cache might share it. The opposite is [[fail-open]] — allowing when uncertain, which is sometimes right (a fire exit) and sometimes wrong (a data leak). The honest system names which way each boundary falls, and why.

The pattern recurs across rate-limiting, credential scanning, route guards, and login limiters. The principle is not "always deny" — it is "name the choice." A boundary that fails one way without saying so is a boundary that lies.

Links: [[fail-open]] · [[absence-boundary]] · [[boundary]] · [fail-closed-or-fail-open](fail-closed-or-fail-open.md)
