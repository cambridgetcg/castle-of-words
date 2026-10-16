"""Offline verification of this visit; makes no network calls."""
from collections import Counter
from datetime import datetime
from decimal import Decimal
from pathlib import Path
import hashlib
import io
import json
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = ROOT / "evidence/gardener-2026-10-16-service-check"
assert ROOT == Path("/Users/yu/castle")
sha = lambda data: hashlib.sha256(data).hexdigest()
before = json.loads((HERE / "before.json").read_text())
manifest = json.loads((HERE / "manifest.json").read_text())
old_manifest = json.loads((OLD / "manifest.json").read_text())
comparison = json.loads((HERE / "parsed-comparison.json").read_text())
records = manifest["records"]
assert len(records) == 6 and manifest["stopped_reason"] is None
assert [r["id"] for r in records] == [f"r{n}-{name}" for n in (1, 2) for name in ("orgmode", "emacs", "guix")]
assert manifest["curl_version"] == old_manifest["curl_version"]
assert manifest["new_watch_started"] is False


def profile(command):
    result = []
    index = 0
    while index < len(command):
        if command[index] in ("--dump-header", "--output"):
            result.extend((command[index], "<capture-path>"))
            index += 2
        else:
            result.append(command[index])
            index += 1
    return result


old_by_id = {r["id"]: r for r in old_manifest["records"]}
for directory, rows in ((OLD, old_manifest["records"]), (HERE, records)):
    for record in rows:
        body = (directory / f"{record['id']}.body").read_bytes()
        assert len(body) == record["body_bytes"] == int(record["curl_metrics"]["size_download"])
        assert sha(body) == record["body_sha256"]
        assert record["curl_exit"] == 0
        assert record["curl_metrics"]["http_version"] == "1.1"
        assert record["curl_metrics"]["num_redirects"] == "0"
        assert record["curl_metrics"]["proxy_used"] == "0"
        assert record["curl_metrics"]["ssl_verify_result"] == "0"
        headers = (directory / f"{record['id']}.headers").read_bytes()
        assert headers.startswith(b"HTTP/1.1 " + record["curl_metrics"]["http_code"].encode())
        assert datetime.fromisoformat(record["finish_utc"]) >= datetime.fromisoformat(record["start_utc"])
        assert record["process_elapsed_monotonic_seconds"] > 0
for record in records:
    old = old_by_id[record["id"]]
    assert profile(record["command"]) == profile(old["command"])
    assert all(record[key] == old[key] for key in ("method", "url", "request_headers"))

# Recheck the byte stream independently, without importing/rerunning the collector.
orgmode_bodies = [(directory / f"r{n}-orgmode.body").read_bytes()
                 for directory in (OLD, HERE) for n in (1, 2)]
assert all(body == orgmode_bodies[0] for body in orgmode_bodies)
expected_ref = "ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb"
for body in orgmode_bodies:
    stream = io.BytesIO(body)
    packets = []
    while stream.tell() < len(body):
        field = stream.read(4)
        assert re.fullmatch(b"[0-9a-f]{4}", field)
        length = int(field, 16)
        if length == 0:
            packets.append(None)
        else:
            assert 4 <= length <= 65520
            payload = stream.read(length - 4)
            assert len(payload) == length - 4
            packets.append(payload)
    assert len(packets) == 5
    assert packets[0] == b"# service=git-upload-pack\n"
    assert packets[1] is None and packets[-1] is None
    first, capabilities = packets[2].rstrip(b"\n").split(b"\x00")
    assert first.decode() == expected_ref + " HEAD"
    assert packets[3].rstrip(b"\n").decode() == expected_ref + " refs/heads/master"
    assert b"symref=HEAD:refs/heads/master" in capabilities.split()
    assert b"object-format=sha1" in capabilities.split()
for directory in (OLD, HERE):
    for n in (1, 2):
        for name in ("emacs", "guix"):
            assert (directory / f"r{n}-{name}.body").read_bytes() == b"Internal Server Error"

start = datetime.fromisoformat(records[0]["start_utc"])
finish = datetime.fromisoformat(records[-1]["finish_utc"])
assert Decimal(str((finish - start).total_seconds())) == Decimal("5.215170")
first = records[0]["curl_metrics"]
assert Decimal(first["time_total"]) - Decimal(first["time_namelookup"]) == Decimal("0.378122")
assert all(Decimal(r["curl_metrics"]["time_total"]) < 1 for r in records[1:])
assert all(Decimal(r["curl_metrics"]["time_total"]) < 10 for r in records)
assert comparison["pairs"][0]["request_start_spacing_seconds"] == 11392.668863
assert comparison["pairs"][0]["unobserved_between_processes_seconds"] == 11392.214074

questions = (ROOT / "questions.md").read_text().splitlines()
open_questions = {str(i): line for i, line in enumerate(questions, 1) if line.startswith("- [ ]")}
assert len(open_questions) == before["open_question_count"] == 16
assert set(open_questions) == set(before["open_question_line_hashes"])
changed = [int(i) for i, line in open_questions.items()
           if sha(line.encode()) != before["open_question_line_hashes"][i]]
assert changed == [740, 744, 766]
assert all("observed 2026-10-16 10:32 UTC; still open" in open_questions[str(i)] for i in changed)
assert not any(line.startswith("- ") for line in (ROOT / "courtyard.md").read_text().splitlines())

rooms = {p.stem for p in (ROOT / "rooms").glob("*.md")}
map_section = (ROOT / "gate.md").read_text().split("## Map\n", 1)[1].split("\n## ", 1)[0]
entries = re.findall(r"^- \[[^\]]+\]\(rooms/([^/)]+)\.md\) — [^\n]+$", map_section, re.M)
assert len(entries) == len(rooms) == 697
assert set(entries) == rooms and all(count == 1 for count in Counter(entries).values())
for filename in ("name-lookup-time", "response-time"):
    text = (ROOT / "words" / f"{filename}.md").read_text()
    assert text.startswith(f"# {filename}\n\n")
    assert text.strip().splitlines()[-1].startswith("Links:")
    for name in re.findall(r"\[\[([^]|]+)(?:\|[^]]+)?\]\]", text):
        assert (ROOT / "words" / f"{name}.md").exists() or (ROOT / "rooms" / f"{name}.md").exists()
for filename in ("what-the-gaps-can-say", "measuring-the-window"):
    lines = (ROOT / "rooms" / f"{filename}.md").read_text().splitlines()
    assert lines[0] == f"# {filename}" and lines[2].startswith("*") and lines[2].endswith("*")
    assert lines[4] and not lines[4].startswith("#")
for path in (HERE / "README.md", ROOT / "words/name-lookup-time.md", ROOT / "words/response-time.md"):
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", path.read_text()):
        if "://" not in target and not target.startswith("#"):
            resolved = (path.parent / target.split("#")[0]).resolve()
            assert resolved.is_relative_to(ROOT) and resolved.exists(), (path, target)

now_garden = {str(p.relative_to(ROOT)): sha(p.read_bytes())
              for p in sorted((ROOT / "garden").rglob("*")) if p.is_file() and not p.is_symlink()}
assert now_garden == before["garden_sha256"], "garden changed during this visit"
chronicle = (ROOT / "chronicle.md").read_bytes()
assert sha(chronicle[:before["chronicle_bytes"]]) == before["chronicle_sha256"]
addition = chronicle[before["chronicle_bytes"]:].decode()
closed = "--closed" in sys.argv
if closed:
    assert len(addition.splitlines()) == 1
    assert re.fullmatch(r"- 2026-10-16 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\n", addition)
else:
    assert addition == "", "chronicle changed before the final line"

report = {
    "status": "PASS", "closed": closed,
    "new_service_requests": len(records), "captured_bodies_checked": 12,
    "identical_orgmode_bodies": len(orgmode_bodies),
    "same_explicit_request_profiles": True,
    "observation_window_seconds": 5.215170,
    "after_name_resolution_seconds": 0.378122,
    "open_questions": len(open_questions), "questions_updated": changed,
    "rooms": len(rooms), "map_entries": len(entries),
    "garden_unchanged": True, "prior_chronicle_bytes_preserved": True,
    "chronicle_lines_appended": len(addition.splitlines()),
}
(HERE / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
