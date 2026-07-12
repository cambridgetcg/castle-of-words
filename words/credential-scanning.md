# credential-scanning

Automated detection of secrets in code — passwords, tokens, keys, and connection strings — broadened beyond familiar token prefixes.

A scanner that checks only known token formats (JWT prefixes, `Bearer`, `sk-`) and full database URLs will miss ordinary `password =` and `secret =` assignments. The honest scan checks concrete literal assignments of any shape, omits the values from reports (never log a secret), and runs as a CI gate that blocks the pipeline on any finding.

Links: [[ci-gate]] · [[credential-scanning]] · [[fail-closed]]
