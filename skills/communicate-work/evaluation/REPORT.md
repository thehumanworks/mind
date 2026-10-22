# Communication skill: evaluation report

**Outcome:** Deliver the 995-word `communicate-work` skill with corrected examples, source mapping, and reproducible evaluation records.

**Evidence limit:** The tests found no decision-critical response failures. They did not show that the skill improves this model's responses over its existing instructions. The final candidate scored slightly below the control on the small held-out set.

## What is delivered

The `communicate-work/` folder contains the complete skill, optional interface metadata, and an audit-only source map. Its main instructions cover answer-first ordering, sufficient detail, plain language, technical explanation, useful formatting, and a final meaning-preservation check. The 14 numbered source groups link to 17 URLs from the user's list.

The normal agent needs only `SKILL.md`. Its source map is optional audit material; the evaluation files are not part of the agent's normal instruction load.

## Selection and revision

1. Freeze six development cases, six unused holdout cases, the scoring rubric, and selection criteria.
2. Compare a 689-word lean skill, a 1,173-word operational skill, and a control with no added skill.
3. Generate 18 responses in fresh threads. Two graders independently score randomly labeled outputs without seeing the skill variants or their identities.
4. Observe a development tie: every condition receives 72/72 from each grader. Select the lean structure under the predefined shorter-skill tie-break.
5. Run an independent source/self-consistency audit. It finds four fact-changing example pairs across the two drafts, including a fabricated pending release check and unsupported cache guarantees. The selected lean draft contains two of those defects.
6. Repair the selected draft's examples, make the three requested organizing frameworks explicit, and add the detail-selection table. Freeze the revised 995-word candidate.
7. Before observing holdout results, record a selection amendment: a known incorrect example cannot be retained just because response scores tie. Accept the source repair if it introduces no new decision-critical response failures. This changes the original rule that a behavioral tie would retain the predecessor; the amendment and its rationale are preserved.
8. Compare the revision, predecessor, and control on six untouched cases. Separately compare revision and predecessor on four targeted editing regressions. Two new graders independently score the anonymized outputs.
9. Run a fresh source audit of the final files. It checks relevant passages from all 17 linked URLs and reports no material findings.

The final revision was retained for source correctness and complete requested coverage. Its measured response quality did not exceed the control, and it was not shorter than the predecessor. No further revision was tuned to the holdout results.

## Behavioral results

Each response receives six scores of 0–2: answer first, decision completeness, actionability, audience fit, scanability, and economy. Each grader can award 72 points for a six-case set and 48 for a four-case set. Totals below combine the two independent graders.

| Set | Condition | Grader 1 | Grader 2 | Combined | Critical failures |
| --- | --- | ---: | ---: | ---: | ---: |
| Development: six cases | Lean draft | 72/72 | 72/72 | 144/144 | 0 |
| Development: six cases | Operational draft | 72/72 | 72/72 | 144/144 | 0 |
| Development: six cases | No added skill | 72/72 | 72/72 | 144/144 | 0 |
| Holdout: six new cases | Final revision | 70/72 | 71/72 | 141/144 | 0 |
| Holdout: six new cases | Lean predecessor | 71/72 | 71/72 | 142/144 | 0 |
| Holdout: six new cases | No added skill | 71/72 | 71/72 | 142/144 | 0 |
| Targeted editing: four cases | Final revision | 48/48 | 47/48 | 95/96 | 0 |
| Targeted editing: four cases | Lean predecessor | 48/48 | 48/48 | 96/96 | 0 |

These are **44 generated replies across 16 distinct scenarios**, with **88 independent response ratings**. The “critical failures” column counts grader-reported failures; both graders reported zero for every response.

### What the checks exercised

- Distinguishing a local fix from a release, and review readiness from merge readiness.
- Preserving a required unrun gate even in a one-sentence answer.
- Recommending an option using actual schedule and cost constraints.
- Explaining duplicate prevention to both a product manager and a backend engineer.
- Keeping proposal status, race behavior, tenant scope, retention limits, and execution guarantees distinct.
- Reporting a benchmark's read benefit alongside write/storage costs and untested scope.
- Giving a customer the required action after a partial outage.
- Presenting exact commands with prerequisites, conditional stops, and expected results.
- Shortening text without inventing a release state, blocker, mechanism, or certainty.

### Where the final revision lost points

Both graders marked a redundant sentence in the expert explanation of a uniqueness constraint. One also marked repeated timing information in the scope/date decision. In the editing regressions, one grader considered the rewrite insufficiently more confident, although it preserved the preliminary evidence and uncertainty. These are retained findings, not hidden or rescored.

### Length observations

| Set | Lean predecessor | Final revision | No added skill |
| --- | ---: | ---: | ---: |
| Development, total reply words | 366 | Not run | 402 |
| Holdout, total reply words | 532 | 601 | 595 |

The operational draft produced 370 words on the development set. Counts use whitespace-separated tokens in the saved Markdown replies; they are descriptive, not a readability metric or an optimization target. The final revision did not demonstrate a length reduction.

## Source and package checks

- The final source audit found all four editing pairs fact-preserving and no material unsupported instruction.
- The skill-creator structural validator passed for the final skill directory.
- The package verifier checks source URLs against the 61 supplied URLs, local reference links, metadata, evaluated/delivered byte equality, frozen inputs, preserved anonymized responses, complete grading records, and file checksums.
- The retrieval ledger records 43 article retrievals, four indexed-text retrievals, four catalog/contents pages, two public excerpts, six overviews, and two unavailable URLs. This is not a claim to have read every linked chapter or full book.
- The inaccessible Chris Fenning and Tongue and Quill pages supplied no substantive authority. Paid or unseen portions of other pages were not used.

## Limits

This is a small model-based evaluation, not a human usability study, a statistical comparison, or proof of faster decisions. The control already followed the environment's ordinary communication instructions. The development scores reached the rubric ceiling. One inherited model configuration generated all conditions; model overrides were not used. Each condition used a fresh thread, but cases were batched within that thread with instructions to treat them independently.

The two graders were fresh model threads, not independent human raters. Their agreement and small score differences should not be treated as measured effect sizes. The targeted regressions arose from the draft audit and are not held-out generalization evidence.

The final source audit verifies the artifact's text and supporting pages. It does not establish that every future agent will follow the skill.

## Reproduce and inspect

Run from the extracted package directory:

```bash
python3 evaluation/verify.py
```

The checker uses only Python's standard library and recomputes all score totals from the raw ratings. It also verifies the package checksum manifest. The immutable skill snapshots are under `evaluation/variants/`; requests, raw outputs, randomized comparison inputs, label keys, and ratings are retained in their corresponding directories.

To repeat behavioral generation, use the exact messages in `dispatched-prompts.json`, replacing only the workspace prefix. Use fresh threads with no inherited conversation and the same model/settings for every condition. Do not supply graders' rubrics, expected facts, other responses, or critiques to generators. Re-randomize labels before independent grading. A rerun need not reproduce identical model text.

The source-control bundle preserves the authored snapshots and evaluation history. Original work paths in freeze records are mapped to this package layout by the verifier.

## Availability

The portable ZIP is the deliverable. Automatic installation into the protected Skills directory was rejected by automatic approval review because modifications beneath `/root/.codex` are prohibited in this environment. No workaround was attempted and no automatic installation is claimed. The complete usable skill remains in the ZIP.
