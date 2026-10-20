"""Bounded public-document retrieval; never probes watched Git endpoints."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.links = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "div", "li", "br", "h1", "h2", "h3", "pre"):
            self.parts.append("\n")
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def fetch(pair):
    label, url = pair
    assert label.replace("-", "").isalnum()
    assert url.startswith("https://") and "info/refs" not in url
    body = ROOT / (label + ".html")
    assert not body.exists(), "Do not overwrite an earlier retrieval"
    command = ["curl", "--disable", "--silent", "--show-error", "--location",
               "--retry", "0", "--connect-timeout", "10", "--max-time", "40",
               "--max-filesize", "3000000", "--user-agent", "CastleResearch/1.0",
               "--output", str(body), "--write-out", "%{json}", url]
    started = datetime.now(timezone.utc).isoformat()
    result = subprocess.run(command, capture_output=True, text=True, timeout=45)
    finished = datetime.now(timezone.utc).isoformat()
    raw = body.read_bytes() if body.exists() else b""
    receipt = {"url": url, "started_utc": started, "finished_utc": finished,
               "command": command, "exit_code": result.returncode,
               "stderr": result.stderr, "sha256": sha256(raw).hexdigest(),
               "bytes": len(raw), "curl": json.loads(result.stdout) if result.stdout else None}
    (ROOT / (label + "-receipt.json")).write_text(json.dumps(receipt, indent=2) + "\n")
    text = Text()
    text.feed(raw.decode("utf-8", errors="replace"))
    cleaned = "\n".join(s.strip() for s in "".join(text.parts).splitlines() if s.strip())
    (ROOT / (label + "-text.txt")).write_text(cleaned + "\n")
    (ROOT / (label + "-links.json")).write_text(json.dumps(list(dict.fromkeys(text.links)), indent=2) + "\n")
    return {"label": label, "exit_code": result.returncode,
            "status": receipt["curl"].get("http_code") if receipt["curl"] else None,
            "bytes": len(raw), "stderr": result.stderr}


if __name__ == "__main__":
    args = sys.argv[1:]
    assert args and len(args) % 2 == 0
    pairs = list(zip(args[::2], args[1::2]))
    assert len(pairs) <= 3
    with ThreadPoolExecutor(max_workers=3) as pool:
        for outcome in pool.map(fetch, pairs):
            print(json.dumps(outcome))
