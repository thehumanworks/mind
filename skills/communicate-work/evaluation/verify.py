#!/usr/bin/env python3
"""Verify packaged evaluation integrity and recompute reported scores (standard library only)."""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
EVAL = ROOT / "evaluation"
SKILL = ROOT / "communicate-work"

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def original_path(name):
    if name.startswith("eval/"):
        return EVAL / name[5:]
    if name.startswith("variants/"):
        return EVAL / name
    return EVAL / name

def verify_freezes():
    for name in ("protocol-freeze.json", "variant-freeze.json", "revision-freeze.json"):
        frozen = read_json(EVAL / name)
        for path, value in frozen.items():
            expected = value["sha256"] if isinstance(value, dict) else value
            require(digest(original_path(path)) == expected, f"Frozen artifact changed: {path}")

def verify_skill():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    require(text.startswith("---\n"), "Missing YAML frontmatter")
    front, body = text.split("---\n", 2)[1:]
    require(re.search(r"^name: communicate-work$", front, re.M), "Incorrect skill name")
    require(re.search(r'^description: ".+"$', front, re.M), "Missing trigger description")
    require(set(re.findall(r"^(\w+):", front, re.M)) == {"name", "description"}, "Unexpected frontmatter")
    require(len(text.splitlines()) < 500, "Skill exceeds creator guideline")
    require("[TODO" not in text, "Unfilled template")
    require(text == (EVAL / "variants/revised/communicate-work/SKILL.md").read_text(encoding="utf-8"), "Delivered skill differs from evaluated revision")
    allowed = {row["url"] for row in read_json(EVAL / "source-retrieval.json")["sources"]}
    external = re.findall(r"\]\((https?://[^)]+)\)", text)
    require(external and set(external).issubset(allowed), "Communication source outside allowlist")
    for source in SKILL.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
            if not target.startswith(("http://", "https://", "#")):
                require((source.parent / target.split("#")[0]).exists(), f"Broken local link: {target}")
    require("$communicate-work" in (SKILL / "agents/openai.yaml").read_text(), "UI prompt does not invoke the skill")
    return {"words_including_sources": len(text.split()), "lines": len(text.splitlines()), "source_urls": len(set(external))}

def verify_stage(stage, conditions, grade_paths):
    cases = read_json(EVAL / stage / "requests.json")
    ids = {c["id"] for c in cases}
    require(len(ids) == len(cases), "Duplicate case IDs")
    originals = {}
    for condition in conditions:
        responses = read_json(EVAL / stage / f"responses-{condition}.json")
        require({r["id"] for r in responses} == ids and len(responses) == len(ids), f"Incomplete output: {stage}/{condition}")
        require(all(isinstance(r["response"], str) and r["response"].strip() for r in responses), "Empty reply")
        originals[condition] = {r["id"]: r["response"] for r in responses}
    blind = read_json(EVAL / "grading" / f"{stage}-blind.json")
    key = read_json(EVAL / "grading" / f"{stage}-key.json")
    expected = set()
    require({c["id"] for c in blind} == ids, "Blinded cases differ")
    for case in blind:
        source = next(c for c in cases if c["id"] == case["id"])
        require(case["request"] == source["request"] and case["facts"] == source["facts"], "Blinding changed case facts")
        for label, response in case["candidates"].items():
            require(response == originals[key[case["id"]][label]][case["id"]], "Blinding changed a response")
            expected.add((case["id"], label))
    dimensions = {"answer_first", "decision_completeness", "actionability", "audience_fit", "scanability", "economy"}
    result = {}
    for index, grade_path in enumerate(grade_paths, 1):
        ratings = [r for r in read_json(EVAL / "grading" / grade_path) if r["case_id"] in ids]
        require(len(ratings) == len(expected), f"Missing ratings in {grade_path}")
        require({(r["case_id"], r["candidate"]) for r in ratings} == expected, "Incorrect rating identities")
        totals = {c: {"score": 0, "max_score": 12 * len(cases), "critical_failures": 0} for c in conditions}
        for rating in ratings:
            require(set(rating["scores"]) == dimensions, "Incorrect rubric dimensions")
            require(all(type(v) is int and 0 <= v <= 2 for v in rating["scores"].values()), "Score out of range")
            require(isinstance(rating["critical_failures"], list), "Critical failures must be a list")
            condition = key[rating["case_id"]][rating["candidate"]]
            totals[condition]["score"] += sum(rating["scores"].values())
            totals[condition]["critical_failures"] += len(rating["critical_failures"])
        result[f"grader_{index}"] = totals
    result["response_words"] = {c: sum(len(s.split()) for s in replies.values()) for c, replies in originals.items()}
    return result

def main():
    manifest = EVAL / "SHA256SUMS.json"
    if manifest.exists():
        for relative, expected in read_json(manifest).items():
            require(digest(ROOT / relative) == expected, f"Integrity failure: {relative}")
    else:
        raise AssertionError("Missing package checksum manifest")
    verify_freezes()
    summary = {"skill": verify_skill()}
    summary["development"] = verify_stage("development", ["q", "r", "s"], ["development-grades-1.json", "development-grades-2.json"])
    summary["holdout"] = verify_stage("holdout", ["t", "u", "v"], ["validation-grades-1.json", "validation-grades-2.json"])
    summary["regression"] = verify_stage("regression", ["w", "x"], ["validation-grades-1.json", "validation-grades-2.json"])
    print(json.dumps({"integrity": "passed", "summary": summary}, indent=2))

if __name__ == "__main__":
    try:
        main()
    except (AssertionError, KeyError, ValueError, OSError) as exc:
        print(f"Verification failed: {exc}", file=sys.stderr)
        sys.exit(1)
