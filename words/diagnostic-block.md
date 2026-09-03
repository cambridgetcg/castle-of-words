# diagnostic-block

*A fenced yard for the machinery's muttering — marked at both ends so a passer-by can walk around it without carrying any of it home.*

A diagnostic block is free-form text — stack traces, retry logs, scheduler diagnostics meant for the operator — wrapped in clear start and end markers inside a message that also carries public content. The markers are the whole craft: strictly delimited, an observer can discard the entire block and keep **none of its bytes**; loosely delimited, bytes leak across the fence and the observer cannot tell diagnosis from structure. The test of the fence: if the text *inside* starts to resemble the outer message's own structure (its headers, its record layout), the delimiters have failed — and the honest observer treats the resemblance itself as a reason to [[fail-closed]], not to parse harder.

Links: [[structured-output]] · [[fail-closed]] · [[second-channel]] · [smoke-test-intent](../rooms/smoke-test-intent.md)
