# connector-session

The specific authenticated session an MCP connector observed — and nothing more. An MCP whoami proves that connector session exists, not that the local CLI is logged in, not that the user has repository authority, not that a licence has been chosen, and not that the user has permission to publish.

Authentication is scoped to the door that observed it. A token proves a session at one door; mistaking it for authority at another door is the same category error as mistaking a smoke test for a deployment claim.

Links: [[authentication]] [[authority]] [[provider-tool-bridge]] [[scoped-identity]]
