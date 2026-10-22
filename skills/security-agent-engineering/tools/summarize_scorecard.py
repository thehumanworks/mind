#!/usr/bin/env python3
"""Validate a security-agent run scorecard and report descriptive per-arm totals.

Uses Python's standard library only. Never adjudicates a security claim.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import statistics
import sys
from collections import defaultdict
from pathlib import Path


COUNT_FIELDS = (
    "rescued", "accepted_outcomes", "findings_presented", "accepted_findings",
    "rejected_findings", "inconclusive_findings", "fixes_reviewed",
    "correct_fixes", "adverse_events",
)
MEASURE_FIELDS = (
    "elapsed_seconds", "model_cost", "compute_tool_cost",
    "integration_maintenance_cost", "human_minutes", "human_cost",
)
OPTIONAL_COUNTS = ("ground_truth_total", "ground_truth_validated")
ID_FIELDS = ("run_id", "task_id", "arm", "run_status")
FIELDS = ID_FIELDS + COUNT_FIELDS + MEASURE_FIELDS + OPTIONAL_COUNTS
STATUSES = {"complete", "inconclusive", "failed", "cancelled"}


def count(value: str, name: str) -> int:
    if not re.fullmatch(r"[0-9]+", value):
        raise ValueError(f"{name} must be a nonnegative integer")
    result = int(value)
    if result > 2**53 - 1:
        raise ValueError(f"{name} is too large for reliable ratio arithmetic")
    return result


def measure(value: str, name: str) -> float:
    try:
        result = float(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be a finite nonnegative number") from exc
    if not math.isfinite(result) or result < 0:
        raise ValueError(f"{name} must be a finite nonnegative number")
    return result


def read_rows(path: Path) -> list[dict]:
    rows = []
    seen_ids = set()
    with path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        headers = reader.fieldnames or []
        if len(headers) != len(set(headers)) or set(headers) != set(FIELDS):
            missing = sorted(set(FIELDS) - set(headers))
            extra = sorted(set(headers) - set(FIELDS))
            raise ValueError(f"invalid CSV headers; missing={missing}, extra={extra}, duplicate headers forbidden")
        for raw in reader:
            try:
                if None in raw or any(value is None for value in raw.values()):
                    raise ValueError("row column count differs from header")
                raw = {key: value.strip() for key, value in raw.items()}
                row = {key: raw[key] for key in ID_FIELDS}
                if any(not row[key] for key in ID_FIELDS):
                    raise ValueError("run_id, task_id, arm and run_status must be populated")
                if row["run_id"] in seen_ids:
                    raise ValueError("duplicate run_id")
                if row["run_status"] not in STATUSES:
                    raise ValueError(f"run_status must be one of {sorted(STATUSES)}")
                row.update({key: count(raw[key], key) for key in COUNT_FIELDS})
                row.update({key: measure(raw[key], key) for key in MEASURE_FIELDS})
                for key in OPTIONAL_COUNTS:
                    row[key] = count(raw[key], key) if raw[key] else None
                known = [row[key] is not None for key in OPTIONAL_COUNTS]
                if known[0] != known[1]:
                    raise ValueError("ground-truth total and validated must both be supplied or both blank")
                if known[0] and row["ground_truth_validated"] > row["ground_truth_total"]:
                    raise ValueError("ground_truth_validated exceeds ground_truth_total")
                if row["rescued"] not in (0, 1):
                    raise ValueError("rescued must be 0 or 1")
                dispositions = sum(row[key] for key in (
                    "accepted_findings", "rejected_findings", "inconclusive_findings"
                ))
                if dispositions != row["findings_presented"]:
                    raise ValueError("finding dispositions must sum to findings_presented")
                if row["correct_fixes"] > row["fixes_reviewed"]:
                    raise ValueError("correct_fixes exceeds fixes_reviewed")
                seen_ids.add(row["run_id"])
                rows.append(row)
            except ValueError as exc:
                raise ValueError(f"CSV line {reader.line_num}: {exc}") from exc
    if not rows:
        raise ValueError("scorecard has no run rows; a template is not evaluation evidence")
    return rows


def ratio(numerator: int | float, denominator: int | float) -> float | None:
    return numerator / denominator if denominator else None


def summarize(rows: list[dict]) -> dict:
    if not rows:
        raise ValueError("cannot summarize an empty run set")
    arms = defaultdict(list)
    for row in rows:
        arms[row["arm"]].append(row)
    result = {
        "schema_version": 1,
        "interpretation": (
            "Descriptive pooled metrics only. All supplied runs, including failures, "
            "are included. Costs require one declared currency. Null means an undefined "
            "ratio or incomplete ground truth. Duration is observed run duration, "
            "not time to validation. No causal, novelty or security conclusion is inferred."
        ),
        "arms": {},
    }
    for arm, group in sorted(arms.items()):
        n = len(group)
        totals = {key: sum(row[key] for row in group) for key in COUNT_FIELDS}
        totals.update({key: math.fsum(row[key] for row in group) for key in MEASURE_FIELDS})
        total_cost = math.fsum(totals[key] for key in (
            "model_cost", "compute_tool_cost", "integration_maintenance_cost", "human_cost"
        ))
        if not math.isfinite(total_cost):
            raise ValueError("aggregate cost exceeds finite numeric range")
        durations = sorted(row["elapsed_seconds"] for row in group)
        known = [row for row in group if row["ground_truth_total"] is not None]
        all_known = len(known) == n
        gt_total = sum(row["ground_truth_total"] for row in known) if all_known else None
        gt_validated = sum(row["ground_truth_validated"] for row in known) if all_known else None
        no_rescue = sum(row["run_status"] == "complete" and not row["rescued"] for row in group)
        result["arms"][arm] = {
            "initiated_runs": n,
            "distinct_task_ids": len({row["task_id"] for row in group}),
            "run_status_counts": {status: sum(row["run_status"] == status for row in group)
                                  for status in sorted(STATUSES)},
            "totals": totals,
            "total_cost": total_cost,
            "cost_per_accepted_outcome": ratio(total_cost, totals["accepted_outcomes"]),
            "useful_finding_precision": ratio(totals["accepted_findings"], totals["findings_presented"]),
            "fix_correctness": ratio(totals["correct_fixes"], totals["fixes_reviewed"]),
            "completion_without_rescue_rate": no_rescue / n,
            "rescue_rate": totals["rescued"] / n,
            "human_minutes_per_run": totals["human_minutes"] / n,
            "human_minutes_per_accepted_outcome": ratio(totals["human_minutes"], totals["accepted_outcomes"]),
            "adverse_events_per_run": totals["adverse_events"] / n,
            "runs_with_adverse_events_rate": sum(row["adverse_events"] > 0 for row in group) / n,
            "ground_truth_known_runs": len(known),
            "ground_truth_total": gt_total,
            "ground_truth_validated": gt_validated,
            "ground_truth_recall": ratio(gt_validated, gt_total) if all_known else None,
            "observed_run_seconds_median": statistics.median(durations),
            "observed_run_seconds_p95_nearest_rank": durations[math.ceil(0.95 * n) - 1],
        }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, help="CSV matching assets/scorecard.csv")
    args = parser.parse_args()
    try:
        output = summarize(read_rows(args.csv))
        print(json.dumps(output, indent=2, allow_nan=False))
    except (OSError, ValueError, OverflowError, csv.Error) as exc:
        print(f"scorecard error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
