# proxy-preservation

When a proxy continues serving the old version during a failed deploy — doing its job, but also hiding the failure.

A deployment claim must distinguish "the proxy is serving the intended version" from "the proxy is serving the fallback." The smoke test must check both.

Links: [[deployment-claim]] · [[mixed-traffic]]
