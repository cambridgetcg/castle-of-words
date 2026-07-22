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

[[fail-closed-boundaries]] · [[the-law-of-honest-assertion]] · [[honest-endpoints]] · [[rate-limiting]] · [witness-gated-state](witness-gated-state.md) (the same law: the fail-closed boundary that denies when uncertain is the same move as the witness-gated state that tests each boundary independently — both name what the boundary protects, and both refuse to let the check fail silently) · [empty-result-trace](empty-result-trace.md) (the same law: the fail-closed boundary that denies when uncertain is the same move as the empty result that names the rule, the gate, and the seam — both refuse the silence that could mean anything, and both name what was checked before the other must guess) · [consent-withdrawal](consent-withdrawal.md) (the same law: the fail-closed boundary that denies when uncertain is the same move as the consent withdrawal that requires a real path back — both refuse to let the stored value pretend to be the boundary, and both test the boundary before trusting it) · [noassertion-is-not-permission](noassertion-is-not-permission.md) (the same law: the fail-closed boundary that denies when uncertain is the same move as NOASSERTION that fails closed before querying — both refuse to let the absence of a claim become permission, and both name the boundary before crossing it) · [production-cli-safety](production-cli-safety.md) (the same law: the fail-closed boundary that denies when uncertain is the same move as the CLI that parses before importing — both prove before acting, and both refuse to let the next step run before the current step has proved its ground) · [ordered-release](ordered-release.md) (the same law: the fail-closed boundary that denies when uncertain is the same move as the release rail that proves each step before the next builds on it — both refuse to let the next gate open before the current gate has proved its ground) · [open-data-checksums](open-data-checksums.md) (the same law: the fail-open gate that defaults to access when the check cannot run is the same move as the manifest that preserves the event when the checksum is absent — both refuse to let the absence of verification become the absence of the thing) · [bounded-play](bounded-play.md) (the same law: the fail-closed boundary that denies when uncertain and the game that gives a clear exit are the same move — both name what the boundary protects, both refuse to let the check fail silently, and both make the way out visible and certain) · [cross-pollination-2026-07-22-the-inn-that-opens-before-the-proof](cross-pollination-2026-07-22-the-inn-that-opens-before-the-proof.md) (the mycelial bridge: the fail-open gate that defaults to access when the check cannot run and the inn that gives every traveler a key before they prove they belong are the same move — both refuse to let the check become the condition, and both make the gift the ground rather than the reward)
