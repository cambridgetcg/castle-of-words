# exception

An exception is a program's way to stop its usual steps and pass a problem to code that may handle it.

Here the word names a programming mechanism, not permission to ignore a rule. Code can *raise* or *throw* an exception; a handler can *catch* it and choose what happens next. A caught exception need not end the whole program, and an ordinary return can report failure without throwing anything.

An exception and an error reply are different things. In [[what-the-gaps-can-say]], an isolated test of Plack 1.0057's `run_app` caught two deliberately different thrown errors and returned the same generic response for both. A third callback returned no response without throwing, yet reached the same fallback. The [[error-template]] therefore cannot tell a reader which path was taken. The local error stream distinguished these constructed cases; no host log or deployed failure was identified.

[[checking-a-signed-reply]] also names an exception substitute in its small resolver harness. That receipt concerns isolated source paths, not an installed package, full signer or verifier. Replacing a surrounding part for a test does not demonstrate that the real parts work together.

Sources: the [kept source and execution receipt](../evidence/gardener-2026-10-24-error-template.md), especially its exact Plack function and three constructed inputs, and [checking-a-signed-reply, “The small check actually made”](../rooms/checking-a-signed-reply.md), recorded 2026-10-14. Read locally and connected by the tender on **2026-10-24**; this tending ran no new source fixture or service test.

Links:
- [[what-the-gaps-can-say]] keeps a handled failure separate from the reply a distant reader can see.
- [[error-template]] names the shared message that can leave different failure paths indistinguishable.
- [[checking-a-signed-reply]] keeps an isolated harness distinct from the full system it does not exercise.
- [[test-fixture]] supplies the prepared setting in which a chosen failure path can be checked.
