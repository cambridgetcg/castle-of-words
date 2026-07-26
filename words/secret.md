# secret

*A piece of information whose value lives in being known by few — and whose safety lives in being held by one.*

A secret is data that must not be shared: a key, a token, a password. The craft of handling secrets is not about hiding them — it is about controlling the boundary between "held" and "shared." A secret printed to a terminal is a secret that now lives in the scrollback buffer. A secret stored in an environment variable is a secret that every child process can read. A secret committed to git is a secret that will outlive the machine.

Links: [[mutation]] · [[fail-closed]] · [[trust]] · [production-cli-safety](../rooms/production-cli-safety.md) (the room that gathers the craft of handling secrets in production CLIs)
