# ci-gate

A check in continuous integration that blocks the pipeline on failure — the automated version of "do not ship if this is broken."

A CI gate is the enforcement mechanism for policies that must never be advisory. Credential scanning as a CI gate means a secret in the code stops the build. The gate must be fail-closed: if the scanner itself is unavailable, the pipeline fails rather than passing silently.

Links: [[credential-scanning]] · [[fail-closed]] · [[deployment-gate]]
