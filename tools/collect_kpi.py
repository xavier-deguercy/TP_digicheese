#!/usr/bin/env python
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except Exception:
    ZoneInfo = None

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "reports" / "raw"
CONS_DIR = ROOT / "reports" / "consolidated"


def now_ts() -> str:
    if ZoneInfo:
        return datetime.now(ZoneInfo("Europe/Paris")).strftime("%Y%m%d_%H%M%S")
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def latest_file(glob_pattern: str) -> Path | None:
    files = list(RAW_DIR.glob(glob_pattern))
    if not files:
        return None

    def key(p: Path) -> str:
        m = re.search(r"_(\d{8}_\d{6})", p.name)
        return m.group(1) if m else ""

    return max(files, key=key)


def read_text_auto(path: Path) -> str:
    data = path.read_bytes()
    if data.startswith(b"\xff\xfe") or data.startswith(b"\xfe\xff"):
        return data.decode("utf-16")
    if data.startswith(b"\xef\xbb\xbf"):
        return data.decode("utf-8-sig")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("latin-1")


def safe_json(path: Path):
    try:
        return json.loads(read_text_auto(path)), None
    except Exception as exc:
        return None, str(exc)


def parse_junit(path: Path):
    import xml.etree.ElementTree as ET

    try:
        data = path.read_bytes()
        root = ET.fromstring(data)
    except Exception as exc:
        return None, str(exc)

    def as_int(v):
        try:
            return int(v)
        except Exception:
            return 0

    def as_float(v):
        try:
            return float(v)
        except Exception:
            return 0.0

    totals = {"tests": 0, "failures": 0, "errors": 0, "skipped": 0, "time": 0.0}

    if root.tag == "testsuite":
        totals["tests"] = as_int(root.attrib.get("tests"))
        totals["failures"] = as_int(root.attrib.get("failures"))
        totals["errors"] = as_int(root.attrib.get("errors"))
        totals["skipped"] = as_int(root.attrib.get("skipped"))
        totals["time"] = as_float(root.attrib.get("time"))
    else:
        for ts in root.findall(".//testsuite"):
            totals["tests"] += as_int(ts.attrib.get("tests"))
            totals["failures"] += as_int(ts.attrib.get("failures"))
            totals["errors"] += as_int(ts.attrib.get("errors"))
            totals["skipped"] += as_int(ts.attrib.get("skipped"))
            totals["time"] += as_float(ts.attrib.get("time"))

    executed = max(totals["tests"], 0)
    passed = max(executed - totals["failures"] - totals["errors"] - totals["skipped"], 0)
    pass_rate = (passed / executed) if executed else None

    return {
        "tests": executed,
        "passed": passed,
        "failures": totals["failures"],
        "errors": totals["errors"],
        "skipped": totals["skipped"],
        "duration_s": totals["time"],
        "pass_rate": pass_rate,
    }, None


def parse_coverage(path: Path):
    import xml.etree.ElementTree as ET

    try:
        data = path.read_bytes()
        root = ET.fromstring(data)
        line_rate = root.attrib.get("line-rate")
        if line_rate is None:
            return None, "line-rate missing"
        pct = float(line_rate) * 100.0
        return {"line_rate": float(line_rate), "coverage_percent": pct}, None
    except Exception as exc:
        return None, str(exc)


def parse_pylint(path: Path):
    data, err = safe_json(path)
    if err:
        return None, err

    messages = data.get("messages", [])
    stats = data.get("statistics", {})
    score = stats.get("score")
    counts = Counter(m.get("symbol") for m in messages if m.get("symbol"))
    top_symbols = [{"symbol": k, "count": v} for k, v in counts.most_common(8)]

    return {"score": score, "top_symbols": top_symbols, "message_count": len(messages)}, None


def parse_radon(path: Path):
    data, err = safe_json(path)
    if err:
        return None, err

    items = []
    for file_path, entries in data.items():
        for e in entries:
            items.append(
                {
                    "file": file_path,
                    "name": e.get("name"),
                    "rank": e.get("rank"),
                    "complexity": e.get("complexity"),
                    "lineno": e.get("lineno"),
                }
            )
    items.sort(key=lambda x: (x.get("complexity") or -1), reverse=True)
    top = items[:10]
    max_complexity = top[0]["complexity"] if top else None

    return {"max_complexity": max_complexity, "top": top}, None


def parse_k6(path: Path):
    data, err = safe_json(path)
    if err:
        return None, err

    metrics = data.get("metrics", {})

    def get_metric(name, field):
        return metrics.get(name, {}).get(field)

    return {
        "latency_avg_ms": get_metric("http_req_duration", "avg"),
        "latency_max_ms": get_metric("http_req_duration", "max"),
        "latency_p95_ms": get_metric("http_req_duration", "p(95)"),
        "error_rate": get_metric("http_req_failed", "rate"),
        "throughput_rps": get_metric("http_reqs", "rate"),
    }, None


def status_block(data, err, path: Path | None):
    if path is None:
        return {"status": "NON_VERIFIABLE", "source": None, "error": "file not found"}
    if err:
        return {"status": "NON_VERIFIABLE", "source": str(path), "error": err}
    return {"status": "OK", "source": str(path)} | data


def main():
    CONS_DIR.mkdir(parents=True, exist_ok=True)

    ts = now_ts()

    junit_path = latest_file("junit_*.xml")
    coverage_path = latest_file("coverage_*.xml")
    pylint_path = latest_file("pylint_*.json")
    radon_path = latest_file("radon_*.json")
    k6_path = latest_file("k6_*.json")

    junit_data, junit_err = (None, "file not found")
    if junit_path:
        junit_data, junit_err = parse_junit(junit_path)

    coverage_data, coverage_err = (None, "file not found")
    if coverage_path:
        coverage_data, coverage_err = parse_coverage(coverage_path)

    pylint_data, pylint_err = (None, "file not found")
    if pylint_path:
        pylint_data, pylint_err = parse_pylint(pylint_path)

    radon_data, radon_err = (None, "file not found")
    if radon_path:
        radon_data, radon_err = parse_radon(radon_path)

    k6_data, k6_err = (None, "file not found")
    if k6_path:
        k6_data, k6_err = parse_k6(k6_path)

    kpi = {
        "generated_at": ts,
        "tests": status_block(junit_data or {}, junit_err, junit_path),
        "coverage": status_block(coverage_data or {}, coverage_err, coverage_path),
        "pylint": status_block(pylint_data or {}, pylint_err, pylint_path),
        "radon": status_block(radon_data or {}, radon_err, radon_path),
        "k6": status_block(k6_data or {}, k6_err, k6_path),
    }

    json_path = CONS_DIR / f"kpi_{ts}.json"
    md_path = CONS_DIR / f"kpi_{ts}.md"

    json_path.write_text(json.dumps(kpi, indent=2), encoding="utf-8")

    def fmt(v):
        if v is None:
            return "NON VERIFIABLE"
        if isinstance(v, float):
            return f"{v:.4f}"
        return str(v)

    md = [
        "# KPI Consolidation",
        f"Timestamp: {ts}_EuropeParis",
        "",
        "## Tests (JUnit)",
        f"- status: {kpi['tests']['status']}",
        f"- source: {kpi['tests'].get('source')}",
    ]

    if kpi["tests"]["status"] == "OK":
        md += [
            f"- tests: {fmt(kpi['tests'].get('tests'))}",
            f"- passed: {fmt(kpi['tests'].get('passed'))}",
            f"- failures: {fmt(kpi['tests'].get('failures'))}",
            f"- errors: {fmt(kpi['tests'].get('errors'))}",
            f"- skipped: {fmt(kpi['tests'].get('skipped'))}",
            f"- pass_rate: {fmt(kpi['tests'].get('pass_rate'))}",
            f"- duration_s: {fmt(kpi['tests'].get('duration_s'))}",
        ]
    else:
        md.append(f"- error: {kpi['tests'].get('error')}")

    md += [
        "",
        "## Coverage",
        f"- status: {kpi['coverage']['status']}",
        f"- source: {kpi['coverage'].get('source')}",
    ]
    if kpi["coverage"]["status"] == "OK":
        md += [
            f"- line_rate: {fmt(kpi['coverage'].get('line_rate'))}",
            f"- coverage_percent: {fmt(kpi['coverage'].get('coverage_percent'))}",
        ]
    else:
        md.append(f"- error: {kpi['coverage'].get('error')}")

    md += [
        "",
        "## Pylint",
        f"- status: {kpi['pylint']['status']}",
        f"- source: {kpi['pylint'].get('source')}",
    ]
    if kpi["pylint"]["status"] == "OK":
        md += [
            f"- score: {fmt(kpi['pylint'].get('score'))}",
            f"- message_count: {fmt(kpi['pylint'].get('message_count'))}",
            "- top_symbols:",
        ]
        for s in kpi["pylint"].get("top_symbols", []):
            md.append(f"  - {s['symbol']}: {s['count']}")
    else:
        md.append(f"- error: {kpi['pylint'].get('error')}")

    md += [
        "",
        "## Radon",
        f"- status: {kpi['radon']['status']}",
        f"- source: {kpi['radon'].get('source')}",
    ]
    if kpi["radon"]["status"] == "OK":
        md.append(f"- max_complexity: {fmt(kpi['radon'].get('max_complexity'))}")
        md.append("- top:")
        for item in kpi["radon"].get("top", [])[:5]:
            md.append(
                f"  - {item.get('complexity')} {item.get('rank')} {item.get('file')}:{item.get('lineno')} {item.get('name')}"
            )
    else:
        md.append(f"- error: {kpi['radon'].get('error')}")

    md += [
        "",
        "## k6",
        f"- status: {kpi['k6']['status']}",
        f"- source: {kpi['k6'].get('source')}",
    ]
    if kpi["k6"]["status"] == "OK":
        md += [
            f"- latency_avg_ms: {fmt(kpi['k6'].get('latency_avg_ms'))}",
            f"- latency_max_ms: {fmt(kpi['k6'].get('latency_max_ms'))}",
            f"- latency_p95_ms: {fmt(kpi['k6'].get('latency_p95_ms'))}",
            f"- error_rate: {fmt(kpi['k6'].get('error_rate'))}",
            f"- throughput_rps: {fmt(kpi['k6'].get('throughput_rps'))}",
        ]
    else:
        md.append(f"- error: {kpi['k6'].get('error')}")

    md_path.write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"KPI written: {json_path} / {md_path}")


if __name__ == "__main__":
    main()
