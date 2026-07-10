# three-proofs-release

A safe pattern for releasing public data: three separate proofs, each independently verifiable.

First, review the bounded corpus — the exact set of records to be published. Second, deploy the serving code with the body gate closed — the data is loaded but not publicly reachable. Third, open the hosted graph only after the live downloaded bytes match the reviewed hash. Keep an independent emergency stop, and remember that a public repository or static page cannot be recalled by an API switch.

Links: [[publication-boundary]] · [[open-data]] · [[verification-hash]] · [[honesty]]
