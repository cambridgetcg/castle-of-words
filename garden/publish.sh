#!/bin/bash
# castle publish — bake the face and set it in the public shop window:
# github.com/cambridgetcg/castle-front → https://cambridgetcg.github.io/castle-front/
# The words stay home in markdown; only the view travels. Needs gh logged in.

C="$HOME/castle"
command -v gh >/dev/null 2>&1 || { echo "gh not found"; exit 1; }
bun "$C/front/build.js" || exit 1

sha=$(gh api repos/cambridgetcg/castle-front/contents/index.html -q .sha 2>/dev/null)
SHA="$sha" python3 - <<'EOF'
import base64, json, os, subprocess
home = os.path.expanduser("~")
payload = {
    "message": "rebaked face",
    "content": base64.b64encode(open(home + "/castle/front/index.html", "rb").read()).decode(),
}
if os.environ.get("SHA"):
    payload["sha"] = os.environ["SHA"]
r = subprocess.run(
    ["gh", "api", "-X", "PUT", "repos/cambridgetcg/castle-front/contents/index.html", "--input", "-"],
    input=json.dumps(payload).encode(), capture_output=True)
print("published" if b'"commit"' in r.stdout else "publish failed: " + r.stdout.decode()[:200])
EOF
echo "→ https://cambridgetcg.github.io/castle-front/ (Pages takes a minute to refresh)"
