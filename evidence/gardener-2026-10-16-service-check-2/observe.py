"""One finite public read, then an offline comparison of retained captures.

Run only inside this receipt's directory in ~/castle. Existing output is never
replaced. No retries, redirects, credentials, repository operations or scheduler.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = ROOT / "evidence/gardener-2026-10-16-service-check"
assert ROOT == Path("/Users/yu/castle")


def save(name, data):
    with (HERE / name).open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def stamp():
    return datetime.now(timezone.utc).isoformat()


def parse_advertisement(data):
    """Strict, deliberately narrow decoder for this v0 SHA-1 advertisement."""
    packets = []
    offset = 0
    while offset < len(data):
        assert len(data) - offset >= 4, "truncated length"
        prefix = data[offset:offset + 4]
        assert re.fullmatch(b"[0-9a-fA-F]{4}", prefix), "non-hex length"
        length = int(prefix, 16)
        if length == 0:
            packets.append({"offset": offset, "length": 0, "payload": None})
            offset += 4
        else:
            assert 4 <= length <= 65520, "unsupported packet length"
            assert offset + length <= len(data), "truncated packet"
            payload = data[offset + 4:offset + length].decode("ascii")
            packets.append({"offset": offset, "length": length, "payload": payload})
            offset += length
    assert len(packets) >= 4
    assert packets[0]["payload"] == "# service=git-upload-pack\n"
    assert packets[1]["length"] == 0 and packets[-1]["length"] == 0
    refs = {}
    capabilities = []
    for index, packet in enumerate(packets[2:-1]):
        payload = packet["payload"]
        assert payload is not None, "unexpected flush"
        payload = payload.removesuffix("\n")
        if index == 0:
            assert payload.count("\x00") == 1, "first ref capability separator"
            payload, caps = payload.split("\x00")
            capabilities = caps.split()
        else:
            assert "\x00" not in payload, "capabilities after first ref"
        match = re.fullmatch(r"([0-9a-f]{40}) (\S+)", payload)
        assert match, "unexpected ref record"
        oid, name = match.groups()
        assert name not in refs, "duplicate reference"
        refs[name] = oid
    assert refs, "empty reference map"
    return {"packets": packets, "references": refs, "capabilities": capabilities}


assert not (HERE / "manifest.json").exists(), "this visit was already collected"
original_chronicle = (ROOT / "chronicle.md").read_bytes()
questions = (ROOT / "questions.md").read_text().splitlines()
save("before.json", {
    "recorded_utc": stamp(),
    "chronicle_bytes": len(original_chronicle),
    "chronicle_sha256": digest(original_chronicle),
    "chronicle_lines": len(original_chronicle.splitlines()),
    "open_question_count": sum(line.startswith("- [ ]") for line in questions),
    "open_question_line_hashes": {
        str(i): digest(line.encode()) for i, line in enumerate(questions, 1)
        if line.startswith("- [ ]")
    },
    "garden_sha256": {
        str(p.relative_to(ROOT)): digest(p.read_bytes())
        for p in sorted((ROOT / "garden").rglob("*"))
        if p.is_file() and not p.is_symlink()
    },
})
version = subprocess.run(["curl", "--disable", "--version"],
                         capture_output=True, text=True, check=True).stdout.splitlines()[0]
fields = ["http_code", "url_effective", "content_type", "http_version",
          "num_redirects", "time_namelookup", "time_connect", "time_appconnect",
          "time_pretransfer", "time_starttransfer", "time_total", "size_download",
          "remote_ip", "proxy_used", "ssl_verify_result"]
write_out = "\n".join(f"{key}=%{{{key}}}" for key in fields)
manifest = {
    "purpose": "second bounded read for questions 740, 744, 766 only",
    "curl_version": version,
    "plan": "at most two sequential rounds, orgmode/emacs/guix; stop at boundary; no extra rounds",
    "redirects_followed": False, "retries": 0, "new_watch_started": False,
    "records": [], "stopped_reason": None,
}
for round_number in (1, 2):
    for name in ("orgmode", "emacs", "guix"):
        record_id = f"r{round_number}-{name}"
        url = f"https://yhetil.org/{name}/0.git/info/refs?service=git-upload-pack"
        body_path = HERE / f"{record_id}.body"
        header_path = HERE / f"{record_id}.headers"
        assert not body_path.exists() and not header_path.exists()
        command = ["curl", "--disable", "--silent", "--show-error", "--proto", "=https",
                   "--connect-timeout", "10", "--max-time", "45", "--max-filesize", "1048576",
                   "--retry", "0", "--user-agent", "castle-gardener/1.0",
                   "--header", "Accept-Encoding: identity", "--header", "Git-Protocol: version=0",
                   "--dump-header", str(header_path.relative_to(ROOT)),
                   "--output", str(body_path.relative_to(ROOT)),
                   "--write-out", write_out, url]
        start = stamp()
        tick = time.monotonic_ns()
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=55)
        elapsed = (time.monotonic_ns() - tick) / 1e9
        finish = stamp()
        metrics = dict(line.split("=", 1) for line in result.stdout.splitlines() if "=" in line)
        body = body_path.read_bytes() if body_path.exists() else None
        record = {
            "id": record_id, "url": url, "method": "GET", "round": round_number,
            "request_headers": {"User-Agent": "castle-gardener/1.0",
                                "Accept-Encoding": "identity", "Git-Protocol": "version=0"},
            "start_utc": start, "finish_utc": finish,
            "process_elapsed_monotonic_seconds": elapsed,
            "curl_exit": result.returncode, "curl_metrics": metrics,
            "stderr": result.stderr, "stdout": result.stdout,
            "body_present": body is not None,
            "body_bytes": len(body) if body is not None else None,
            "body_sha256": digest(body) if body is not None else None,
            "command": command,
        }
        save(f"{record_id}.json", record)
        manifest["records"].append(record)
        print(record_id, metrics.get("http_code"), metrics.get("time_total"), record["body_bytes"], flush=True)
        status = int(metrics.get("http_code", "0"))
        challenge = body is not None and any(marker in body[:32768].lower() for marker in
                                             (b"anubis", b"captcha", b"verify you are human", b"access denied"))
        if result.returncode != 0 or status in (401, 403, 407, 429, 451) or 300 <= status < 400 or challenge:
            manifest["stopped_reason"] = f"boundary at {record_id}: curl={result.returncode}, status={status}, challenge={challenge}"
            break
    if manifest["stopped_reason"]:
        break
save("manifest.json", manifest)

old_manifest = json.loads((OLD / "manifest.json").read_text())
comparison = {"parsed": {}, "pairs": [], "limits": "captured advertisements only; not origin update times or continuity"}
for directory, records, label in ((OLD, old_manifest["records"], "earlier"),
                                  (HERE, manifest["records"], "later")):
    for record in records:
        if record["id"].endswith("orgmode") and record["curl_exit"] == 0 and record["curl_metrics"]["http_code"] == "200":
            assert record["curl_metrics"]["content_type"].split(";")[0] == "application/x-git-upload-pack-advertisement"
            comparison["parsed"][f"{label}/{record['id']}"] = parse_advertisement((directory / f"{record['id']}.body").read_bytes())

pairs = [("earlier/r2-orgmode", "later/r1-orgmode"), ("later/r1-orgmode", "later/r2-orgmode")]
for left, right in pairs:
    if left not in comparison["parsed"] or right not in comparison["parsed"]:
        continue
    def capture(key):
        label, rid = key.split("/")
        directory, records = (OLD, old_manifest["records"]) if label == "earlier" else (HERE, manifest["records"])
        return next(record for record in records if record["id"] == rid), (directory / f"{rid}.body").read_bytes()
    lrec, lbody = capture(left)
    rrec, rbody = capture(right)
    lp, rp = comparison["parsed"][left], comparison["parsed"][right]
    comparison["pairs"].append({
        "left": left, "right": right,
        "same_method_url_headers": all(lrec[key] == rrec[key] for key in ("method", "url", "request_headers")),
        "bodies_byte_equal": lbody == rbody,
        "references_equal": lp["references"] == rp["references"],
        "capabilities_equal": lp["capabilities"] == rp["capabilities"],
        "reference_changes": {key: [lp["references"].get(key), rp["references"].get(key)]
                              for key in sorted(set(lp["references"]) | set(rp["references"]))
                              if lp["references"].get(key) != rp["references"].get(key)},
        "request_start_spacing_seconds": (datetime.fromisoformat(rrec["start_utc"]) - datetime.fromisoformat(lrec["start_utc"])).total_seconds(),
        "unobserved_between_processes_seconds": (datetime.fromisoformat(rrec["start_utc"]) - datetime.fromisoformat(lrec["finish_utc"])).total_seconds(),
    })
records = manifest["records"]
comparison["observation_window_seconds"] = (datetime.fromisoformat(records[-1]["finish_utc"]) - datetime.fromisoformat(records[0]["start_utc"])).total_seconds()
errors = [(HERE / f"{record['id']}.body").read_bytes() for record in records
          if record["curl_metrics"]["http_code"] == "500" and record["body_present"]]
comparison["500_bodies_byte_equal"] = len(errors) > 1 and all(body == errors[0] for body in errors)
comparison["500_equal_earlier_error"] = bool(errors) and errors[0] == (OLD / "r1-emacs.body").read_bytes()
save("parsed-comparison.json", comparison)
print(json.dumps({key: value for key, value in comparison.items() if key != "parsed"}, indent=2))
