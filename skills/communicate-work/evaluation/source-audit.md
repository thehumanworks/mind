# Source-fidelity and self-consistency audit

**Finding:** Four of the six before/after pairs add substantive information that their input sentences do not establish. The general instructions are substantially faithful to the cited writing guidance.

Scope: the lean and operational `communicate-work/SKILL.md` files and their linked public source pages. No evaluation cases, generated responses, source-map file, or neighboring artifacts were read. This is a source and internal-consistency audit, not a performance assessment.

## Concrete findings

1. **Lean, first example: an invented verification state.** The input says that the requested fix was implemented after investigating files. The rewrite adds “the release check is still pending.” Nothing in the input establishes that a release check exists or remains pending. This contradicts the skill's requirement to preserve facts and limits. Remove the added clause, or establish the pending check in the example's input facts.

2. **Operational, migration example: an invented blocker and cause.** “I would like to provide an update regarding the migration” becomes “The migration is blocked by the missing export.” The original supplies neither a blocked status nor a missing export. This demonstrates replacing an empty introduction with a substantive update, but does not demonstrate editing without changing facts. Supply those scenario facts before the pair, or choose a before sentence that already contains them.

3. **Both versions, cache examples: unsupported operational detail.** The lean input states that invalidation follows a write; its rewrite specifies clearing a saved copy and promises fresh data on the next read. The operational input says only that cache invalidation ensures consistency; its rewrite adds an actor, update timing, a clearing mechanism, and next-read behavior. These are stronger, more specific claims than the respective inputs establish. Retain the original level of specificity, or explicitly supply the mechanism and outcome as scenario facts. This conflicts directly with both versions' warnings against turning a scoped result into a broader guarantee.

These findings follow from comparing each pair, without assuming anything about a real release process, migration, or cache. They also conflict with the cited principles of preserving meaning when simplifying ([Wes Kao](https://newsletter.weskao.com/p/how-to-be-concise)), keeping documentation factually correct ([INNOQ](https://www.innoq.com/en/blog/2022/01/principles-of-technical-documentation/)), and making coverage limits clear ([Write the Docs](https://www.writethedocs.org/guide/writing/docs-principles/)).

## Source fidelity

No additional material overgeneralization was identified in the instructions. The answer-first guidance matches [Umbrex](https://umbrex.com/resources/front-line-manager-training-program/lead-with-the-answer/); the conclusion/reasons/evidence hierarchy matches [StrategyU](https://strategyu.co/pyramid-principle-partone/); and prioritizing information for partial reading matches [NN/G](https://www.nngroup.com/articles/inverted-pyramids-in-cyberspace/). Neither skill repeats that article's outdated claim that users do not scroll.

The distinction among learning, doing, reference, and explanation accurately applies [Diátaxis](https://diataxis.fr/start-here/). Conditions before instructions, numbered sequences, code formatting, and descriptive links agree with [Google's highlights](https://developers.google.com/style/highlights). Both files identify the examples as original applications, so the problematic examples are internal inconsistencies rather than falsely attributed source quotations.

## Concision and self-application

Both files use direct instructions and functional sections. The operational version repeats ordering and depth guidance across its core rules, task table, framework section, and checklist, but those sections provide distinct applications or checking functions; repetition alone does not establish a material defect. Neither source supports grading concision by length alone: [Purdue OWL](https://owl.purdue.edu/owl/general_writing/academic_writing/conciseness/index.html) and [Wes Kao](https://newsletter.weskao.com/p/how-to-be-concise) emphasize useful meaning rather than minimum word count. The example fact changes are the substantive self-consistency issue.
