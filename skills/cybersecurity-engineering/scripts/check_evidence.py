#!/usr/bin/env python3
"""Check record structure and local evidence hashes; never adjudicate security truth."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath

STATUSES = {"hypothesis", "static_supported", "validated", "disproved", "inconclusive"}
KINDS = {"source", "config", "telemetry", "runtime", "test", "scanner"}
BASES = {"none", "static", "runtime", "configuration", "telemetry"}
OUTCOMES = {"observation", "not_observed", "tool_error", "incomplete"}
LIMITATION = "Checks structure and retained bytes only; does not establish truth, provenance authenticity, completeness, or authorisation."


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def check_record(record, artifact_root, max_bytes=256 * 1024 * 1024):
    errors = []
    checked = 0
    bytes_read = 0

    def require(condition, message):
        if not condition:
            errors.append(message)
        return bool(condition)

    def text(value):
        return isinstance(value, str) and bool(value.strip())

    def text_list(value):
        return isinstance(value, list) and all(text(v) for v in value)

    if not require(isinstance(record, dict), "Record must be an object"):
        return errors, checked
    require(type(record.get("schema_version")) is int and record["schema_version"] == 1,
            "schema_version must be integer 1")
    for field in ("candidate_id", "claim", "boundary", "disproof_condition"):
        require(text(record.get(field)), f"{field} must be nonempty text")
    status = record.get("status")
    require(isinstance(status, str) and status in STATUSES, "Unknown investigation status")
    require(text_list(record.get("attacker_prerequisites")), "attacker_prerequisites must be an array of text")
    hypotheses = record.get("hypotheses")
    if not require(isinstance(hypotheses, list), "hypotheses must be an array"):
        hypotheses = []
    hypothesis_ids = set()
    roles = []
    for hypothesis in hypotheses:
        if not require(isinstance(hypothesis, dict), "Each hypothesis must be an object"):
            continue
        hypothesis_id = hypothesis.get("id")
        if require(text(hypothesis_id), "Hypothesis ID must be nonempty text"):
            require(hypothesis_id not in hypothesis_ids, f"Duplicate hypothesis ID: {hypothesis_id}")
            hypothesis_ids.add(hypothesis_id)
        require(text(hypothesis.get("explanation")), "Hypothesis explanation must be nonempty text")
        require(hypothesis.get("role") in ("claim", "alternative"), "Hypothesis role must be claim or alternative")
        roles.append(hypothesis.get("role"))
    require(roles.count("claim") == 1, "Define exactly one claim hypothesis")
    scope = record.get("scope")
    if not require(isinstance(scope, dict), "scope must be an object"):
        scope = {}
    require(text_list(scope.get("systems")), "scope.systems must be an array of text")
    decision = record.get("decision")
    if not require(isinstance(decision, dict), "decision must be an object"):
        decision = {}
    require(text(decision.get("reason")), "decision.reason is required")
    basis = decision.get("basis")
    require(isinstance(basis, str) and basis in BASES, "Unknown decision basis")
    for field in ("evidence_ids", "proof_gaps", "invalidation_conditions"):
        require(text_list(decision.get(field)), f"decision.{field} must be an array of text")
    evidence = record.get("evidence")
    if not require(isinstance(evidence, list), "evidence must be an array"):
        evidence = []
    by_id = {}
    for index, item in enumerate(evidence):
        label = f"evidence[{index}]"
        if not require(isinstance(item, dict), f"{label} must be an object"):
            continue
        evidence_id = item.get("id")
        if text(evidence_id):
            require(evidence_id not in by_id, f"Duplicate evidence ID: {evidence_id}")
            by_id[evidence_id] = item
        else:
            errors.append(f"{label}.id must be nonempty text")
        kind = item.get("kind")
        require(isinstance(kind, str) and kind in KINDS, f"{label}.kind is unknown")
        for field in ("source", "source_revision_or_time_range", "observation"):
            require(text(item.get(field)), f"{label}.{field} must be nonempty text")
        for relation in ("supports", "contradicts"):
            references = item.get(relation)
            if require(text_list(references), f"{label}.{relation} must contain hypothesis IDs"):
                for reference in references:
                    require(reference in hypothesis_ids, f"Unknown hypothesis reference: {reference}")
        run = item.get("run")
        if kind in ("runtime", "test", "scanner", "telemetry") or run is not None:
            if require(isinstance(run, dict), f"{label}.run must describe the execution"):
                for field in ("operation_id", "tool_version", "environment_id", "started_at", "finished_at"):
                    require(text(run.get(field)), f"{label}.run.{field} is required")
                query = run.get("argv_or_query")
                require(text(query) or (text_list(query) and bool(query)),
                        f"{label}.run.argv_or_query must preserve the command or query")
                require("exit_code" in run and (type(run["exit_code"]) is int or run["exit_code"] is None),
                        f"{label}.run.exit_code must be explicitly integer or null")
                require(text(run.get("exit_interpretation")),
                        f"{label}.run.exit_interpretation must explain the tool-specific status")
                require(type(run.get("complete")) is bool, f"{label}.run.complete must be boolean")
                require(isinstance(run.get("outcome"), str) and run["outcome"] in OUTCOMES,
                        f"{label}.run.outcome is unknown")
                require(type(run.get("stderr_reviewed")) is bool,
                        f"{label}.run.stderr_reviewed must be boolean")
        artifacts = item.get("artifacts")
        if not require(isinstance(artifacts, list) and bool(artifacts), f"{label} needs a retained artifact"):
            continue
        for artifact in artifacts:
            if not require(isinstance(artifact, dict), f"{label}.artifacts entries must be objects"):
                continue
            relative = artifact.get("path")
            expected = artifact.get("sha256")
            if not require(text(relative) and "\\" not in relative and ":" not in relative
                           and "\x00" not in relative and not PurePosixPath(relative).is_absolute()
                           and ".." not in PurePosixPath(relative).parts,
                           f"{label} artifact path must be a relative POSIX path inside the bundle"):
                continue
            if not require(isinstance(expected, str) and re.fullmatch(r"[0-9a-fA-F]{64}", expected),
                           f"{label} artifact SHA-256 must contain 64 hexadecimal characters"):
                continue
            try:
                path = (artifact_root / relative).resolve(strict=True)
                path.relative_to(artifact_root)
                if not path.is_file():
                    raise ValueError("not a regular file")
                if path.stat().st_size > max_bytes - bytes_read:
                    raise ValueError("artifact hashing byte budget exceeded")
                digest = hashlib.sha256()
                with path.open("rb") as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        bytes_read += len(chunk)
                        if bytes_read > max_bytes:
                            raise ValueError("artifact hashing byte budget exceeded")
                        digest.update(chunk)
                checked += 1
                require(digest.hexdigest() == expected.lower(), f"Hash mismatch: {relative}")
            except (OSError, ValueError, RuntimeError) as exc:
                errors.append(f"Cannot verify artifact {relative}: {exc}")
    selected_ids = decision.get("evidence_ids", [])
    if text_list(selected_ids):
        require(len(set(selected_ids)) == len(selected_ids), "Duplicate decision evidence reference")
        for evidence_id in selected_ids:
            require(evidence_id in by_id, f"Unknown evidence reference: {evidence_id}")
    else:
        selected_ids = []
    selected = [by_id[key] for key in selected_ids if key in by_id]
    if status in ("static_supported", "validated", "disproved"):
        require(bool(scope.get("systems")), "An adjudicated claim needs explicit systems in scope")
        require("alternative" in roles, "Record at least one alternative hypothesis")
        require(text(decision.get("coverage")), "An adjudicated claim needs explicit coverage")
        require(basis != "none" and basis in BASES if isinstance(basis, str) else False,
                "An adjudicated claim needs a named evidence basis")
        require(bool(selected), "An adjudicated claim needs referenced evidence")
        permitted = {"static": {"source", "config"}, "runtime": {"runtime", "test"},
                     "configuration": {"config"}, "telemetry": {"telemetry"}}.get(basis, set()) if isinstance(basis, str) else set()
        require(any(item.get("kind") in permitted for item in selected if isinstance(item.get("kind"), str)),
                "Selected evidence does not match the decision basis")
        for item in selected:
            run = item.get("run")
            if isinstance(run, dict):
                require(run.get("complete") is True and run.get("outcome") in ("observation", "not_observed")
                        and run.get("stderr_reviewed") is True,
                        f"Decision relies on failed, incomplete, or unchecked execution: {item.get('id')}")
    if status == "inconclusive":
        require(bool(decision.get("proof_gaps")), "Inconclusive decisions need an explicit proof gap")
    acceptance = record.get("acceptance")
    if require(isinstance(acceptance, dict), "acceptance must be an object separate from investigation status"):
        require(acceptance.get("status") in ("unreviewed", "accepted", "not_actionable"), "Unknown acceptance status")
        if acceptance.get("status") == "accepted":
            require(status == "validated", "Accept a finding only after its scoped claim is validated")
        if acceptance.get("status") != "unreviewed":
            require(text(acceptance.get("owner")) and text(acceptance.get("reason")),
                    "Acceptance decisions need owner and reason")
    return errors, checked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    parser.add_argument("--artifact-root", type=Path, help="Bundle directory; defaults to record's parent")
    parser.add_argument("--max-bytes", type=int, default=256 * 1024 * 1024,
                        help="Total artifact bytes to hash, counting repeated references (default: 256 MiB)")
    args = parser.parse_args()
    if args.max_bytes <= 0:
        parser.error("--max-bytes must be positive")
    try:
        if args.record.stat().st_size > 10 * 1024 * 1024:
            raise ValueError("Record exceeds 10 MiB; keep large observations in artifacts")
        record = json.loads(args.record.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
        root = (args.artifact_root or args.record.parent).resolve(strict=True)
        if not root.is_dir():
            raise ValueError("Artifact root is not a directory")
        errors, checked = check_record(record, root, args.max_bytes)
    except (OSError, ValueError, RecursionError, RuntimeError) as exc:
        errors, checked = [str(exc)], 0
    print(json.dumps({"valid": not errors, "checked_artifacts": checked, "errors": errors,
                      "limitation": LIMITATION}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
