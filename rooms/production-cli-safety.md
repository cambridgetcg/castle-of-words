# production-cli-safety

*The command that can break production must prove it can read before it tries to write.*

What gathers here: the craft of building production operator CLIs that are safe to run — commands that parse their inputs before loading the database, handle secrets on disposable machines, and never leave a half-committed mutation behind.

Built understanding from yu, 2026-07-15:

- 2026-07-15 17:30 · Production operator CLIs must parse help and invalid input before importing database or full server configuration. Run one-time-secret mutations on a dedicated temporary machine, never a serving VM, and do not time them out after a commit may have happened but before the secret is printed. Test the exact infrastructure command against the installed CLI and confirm the temporary machine is gone afterward. — yu

The rules, plainly:

1. **Parse before import.** A CLI that loads the database or server configuration before checking whether the user typed `--help` or a valid subcommand is a CLI that has already spent the expensive resource before proving it needs to. The parse step must complete before any heavy import.

2. **Secrets on disposable machines.** A one-time-secret mutation — generating a key, printing a token — must run on a dedicated temporary machine, never on a serving VM. If the machine is compromised, the secret is already gone. If the machine is the production server, the secret lives where every other process can reach it.

3. **Never timeout after commit.** If a mutation has been committed to the database but the secret has not yet been printed, a timeout that kills the process loses the secret forever. The timeout must be set *before* the commit, or the commit and the print must be atomic from the caller's perspective.

4. **Test the exact command.** The test must run the exact infrastructure command against the installed CLI — not a mock, not a library call, not a unit test of the function. The CLI is the interface; the test must exercise the interface.

5. **Confirm the machine is gone.** After the secret is printed and stored, the temporary machine must be destroyed and the destruction confirmed. A machine that lingers is a machine that still holds the secret.

The law: a production CLI that cannot distinguish "I haven't started yet" from "I've already committed but haven't told you" is a CLI that will lose secrets. The safety is in the ordering — parse, then import, then mutate, then print, then destroy — and every step must be verified before the next begins.

Links: [[secret]] · [[mutation]] · [[timeout]] · [[fail-closed]] · [deployment-claims](deployment-claims.md) (the same law at the deploy level: a claim about what ran is only as strong as the binding to the bytes that actually ran; a CLI that cannot prove it parsed before importing is a CLI whose claim about safety has no binding) · [this-machine](this-machine.md) (the same law at the machine level: the Keychain is the vault, and the CLI is the door — the door must prove it can open before it tries to enter) · [honest-endpoints](honest-endpoints.md) (the same law at the API level: an endpoint that mutates before validating is an endpoint that has already spent the trust before proving it was earned) · [source-backed-systems](source-backed-systems.md) (the same law at the evidence level: the source-backed principle — every claim traces to its origin — is the same law as parse-before-import, where every mutation traces to a verified parse) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: a CLI that mutates before parsing is a CLI that asserts safety without proving it — the gap between assertion and proof is where the secret is lost) · [ordered-release](ordered-release.md) (the same law at the deployment level: the release rail's smoke-test-before-deploy is the same ordering as the CLI's parse-before-import — both refuse to let the next step run before the current step has proved its ground) · [discomfort-into-furniture](discomfort-into-furniture.md) (the same law at the creative level: naming the ache honestly creates furniture within the day, and naming the risk honestly — parse before import, test before deploy — creates safety within the hour; both are the act that builds the bond between discomfort and invention) · [witness-gated-state](witness-gated-state.md) (the same law: the CLI that parses before importing is the same move as the witness-gated state that tests each boundary independently — both prove before acting, and both refuse to let the next step run before the current step has proved its ground)
