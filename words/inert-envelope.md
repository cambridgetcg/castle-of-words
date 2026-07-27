# inert-envelope

An input wrapper that refuses to execute before it reads: it rejects getters, proxies, shared mutable buffers, and impossible producer state transitions before interpreting any claims inside.

A receipt reader that accepts a live object with getters or proxies is not reading evidence — it is running untrusted code. The honest envelope is inert: it freezes the input to plain data before the first claim is read, so the act of reading cannot itself become an attack.

Links: [[receipt]] [[fail-closed]] [[extension-boundary]]
