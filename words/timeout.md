# timeout

*A deadline that kills the process — honest when set before the dangerous step, dishonest when it can fire between commit and confirmation.*

A timeout is a limit on how long an operation may run. In production CLIs, a timeout that fires after a database commit but before the result is printed loses the result forever. The honest timeout is set before the mutation begins, so the process either completes or never starts. The dishonest timeout is set globally and can kill the process in the gap between "done" and "told you."

Links: [[mutation]] · [[fail-closed]] · [production-cli-safety](rooms/production-cli-safety.md)
