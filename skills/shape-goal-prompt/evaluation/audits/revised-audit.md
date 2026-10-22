# Source and consistency audit: revised `shape-goal-prompt`

Audit date: 2026-10-21.

## Scope and conclusion

Reviewed the frozen revised skill's `SKILL.md`, both reference files, and `agents/openai.yaml` against the permitted research summaries: `requirements.md`, `long-horizon.md`, `clarification.md`, and `openai.md`. No other variant, evaluation material, conversation output, or package was inspected. No skill files were changed.

**No high- or medium-severity findings. One low-severity wording issue.** No material misrepresentation of the summarized sources, internal contradiction in the operating instructions, or loss of user requirements in the examples was identified. This is a source/consistency audit, not evidence of behavioral effectiveness.

## Finding

### Low — display copy presents agreement as the expected finished state without the core's qualification

**Evidence:** `agents/openai.yaml:3` describes the skill as turning requests into “agreed, testable agent prompts.” The actual workflow correctly allows provisional outputs when consequential uncertainty remains (`SKILL.md:32,52,96`), restricts agreement to the scope supported (`SKILL.md:50`), and explicitly rejects guarantees of agreement (`references/evidence.md:34`).

**Implication:** The brief catalog description can suggest that agreement is always obtained, although the substantive instructions correctly distinguish agreement, delegation, and an unresolved draft. This is a minor presentation mismatch, not an operational authorization defect.

**Suggested correction for a future revision:** Replace “agreed” with “clear,” or qualify the description to cover provisional prompts. The frozen files were left intact.

## Checks without material findings

- **Source fidelity and evidence strength:** `references/evidence.md:3,7–30,34` consistently distinguishes motivating evidence from proof of this particular skill. Its accounts of IN3, selective clarification, and multi-turn failures match `clarification.md` §§1, 2, and 4. Its NASA, van Lamsweerde, Horvitz, Clark/Brennan, and Amershi mappings match `requirements.md` R1–R7. It does not transplant numerical study results or universal question quotas into the workflow.
- **Long-work claims and capabilities:** `SKILL.md:84–86` and `references/evidence.md:25–30` preserve the research summaries' limits: prompts do not create access, persistence, runtime mechanisms, or authority; experimental harness designs do not make fixed sprints or agent teams mandatory. The field order is presented as a design choice with task-specific exceptions (`SKILL.md:56`), not a scientifically optimal template.
- **Acceptance and agreement:** `SKILL.md:38–44,50–52,88–96` retains the distinction between an inspectable deliverable, hoped-for external effects, prompt readiness, and completed downstream work. It preserves required methods and exclusions while allowing choices within those boundaries. The research summaries support these distinctions as engineering synthesis.
- **Example fidelity:** The support-backlog revision retains the export and contact prohibition while changing audience; the local assent example limits the scope of agreement; the transcript example preserves adoption status, the corrected source, and quoted speech. The clear-request prompt retains the supplied audience, topic, length, required content, and browsing/product-change prohibitions. The handbook, grant-research, and byte-preservation examples consistently illustrate the core's rules about proposed criteria, resource limits, actual capabilities, and the agreed verification reference (`references/examples.md:5–95`).

## Audit limit

Claims were checked against the supplied primary-source summaries. No specific factual uncertainty required reopening a primary source, so no additional browsing was performed. This audit does not independently authenticate every bibliography entry or establish that following the skill improves clarification or execution outcomes.
