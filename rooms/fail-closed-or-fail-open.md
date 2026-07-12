# Fail-Closed or Fail-Open

*A gate that stays shut when uncertain is stronger — unless the door it guards is the only way out.*

What gathers here: the principle for choosing between fail-closed and fail-open boundaries, and why the choice must be named.

---

## The principle

The choice between fail-closed (deny on uncertainty) and fail-open (allow on uncertainty) is domain-specific, but the principle is not: **fail-closed for security boundaries, fail-open for safety boundaries.** A security boundary protects what should not be accessed — authentication, authorization, data access. When the check fails, the safe default is denial. A safety boundary protects what must remain available — emergency exits, life-support systems, fire alarms. When the check fails, the safe default is access.

In engineering, a fail-safe system is one that, on failure, responds in a way that causes minimal or no harm (Wikipedia, "Fail-safe", https://en.wikipedia.org/wiki/Fail-safe, read 2026-07-12). The direction of "safe" depends on what is being protected: for a nuclear reactor, safe means shutdown (fail-closed); for an airplane's flight controls, safe means continued operation (fail-open, with redundancy).

## The castle's boundaries

The castle's fail-closed rooms — rate-limiting, credential scanning, route guards, login limiters — all protect security boundaries. The principle holds: when the check cannot confirm permission, deny. The principle does not say *all* boundaries must be fail-closed. It says the choice must be named, and the name must match what the boundary protects.

## The one rule

**Name what the boundary protects, then choose the direction that protects it when the check fails.** A security boundary that fails open is a door that unlocks when the guard falls asleep. A safety boundary that fails closed is a fire exit that locks when the alarm sounds. The principle is not "always fail-closed" — it is "the direction must match the thing being protected, and the choice must be named."

## Words

- [[fail-closed]] — deny when uncertain; the default for security boundaries
- [[fail-open]] — allow when uncertain; the default for safety boundaries
- [[honest-boundary]] — a boundary that names which direction it fails and why

## Links

[[fail-closed-boundaries]] · [[the-law-of-honest-assertion]] · [[honest-endpoints]] · [[rate-limiting]]
