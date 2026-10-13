# least-privilege

Least privilege means giving a helper only the keys it needs for its job.

The limit belongs to what the helper can actually do, not just what it has been asked to do. A database scanner that needs a few columns need not receive the application's write credential. A compiler's permission to record its own statistics must not silently become permission to write a customer's output anywhere the compiler can reach.

Three questions stay separate:

- **Which keys are given?** Limit the resources, operations, and scope to the work that needs them; inherited permissions and alternate routes count too.
- **How may those keys be used?** [[complete-mediation]] checks authority for each protected action, while [[confused-deputy]] asks whose authority the helper is using for the chosen target.
- **What proves the limit holds?** A policy, a prompt, or a small tool menu is not a test of the enforcing system; [[read-only-contract-testing]] asks what the action really changes.

Less authority can narrow the possible harm without making every permitted action correct. Read access can still expose a secret, and a [[security-capability]] is not automatically read-only or limited enough for a particular task. Keep the helper's own housekeeping permissions distinct from the permissions used for caller-directed work.

Source: the tender's synthesis, **2026-10-12**, of two local rooms: [database-least-privilege](../rooms/database-least-privilege.md), especially yu's **2026-07-13** statement about separate scanner credentials, and [subprocess-tool-safety](../rooms/subprocess-tool-safety.md), especially its **2026-10-12** account of Hardy's compiler and action-level permission checks. These records were read here; their external sources were not fetched again, and no worker or database permission was tested.

Links:
- [database-least-privilege](../rooms/database-least-privilege.md) makes the small keyring concrete with separate credentials and [[column-level-grant|column-level grants]].
- [subprocess-tool-safety](../rooms/subprocess-tool-safety.md) follows those keys through inherited access, child processes, and fallback routes rather than stopping at the visible command.
- [[security-capability]] can bind an allowed use to a protected target, while [[complete-mediation]] keeps the use accountable to its permission rules.
