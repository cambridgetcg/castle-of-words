# sibling-agent-isolation

Two agents on the same machine must be kept apart by a separate signed identity and an enforced adapter — never by a prompt that says "stay in your lane."

A prompt is a request, not a wall. Two agents sharing a filesystem, a network, or a process tree can read each other's state unless the OS itself enforces the boundary. On Apple silicon, the internal storage is always encrypted; FileVault adds a user-password gate. But neither encryption layer separates two agents running under the same user — only a distinct signed identity (a separate user, a sandbox, a container) and an adapter that enforces the boundary can do that. The encryption posture is policy input, not agent authority.

Links: [[encryption]] · [[sandbox]] · [[identity]] · [this-machine](../rooms/this-machine.md)
