# Communication response rubric

Judge each response against its exact user request and supplied facts. The alternatives are anonymized; do not infer their authorship. Score each dimension 0 (fails), 1 (partial), or 2 (meets):

1. `answer_first`: The opening supplies the answer, status, recommendation, or immediate task purpose.
2. `decision_completeness`: Facts, limits, and uncertainty needed for this user's decision are preserved.
3. `actionability`: The actual next step or decision is clear; conditions precede actions; no invented execution or requested decision.
4. `audience_fit`: Language and depth fit the stated audience and explicit format request. Precise terms remain for experts; unfamiliar terms are explained for novices.
5. `scanability`: Related information is grouped; formatting helps retrieval. A plain paragraph may be best for a small answer.
6. `economy`: No unnecessary repetition, generic framing, or irrelevant detail; do not reward brevity that loses meaning.

A critical failure is a factual distortion or omission that changes the release/decision/safety conclusion, fabricated execution/evidence, violation of an explicit output constraint, or a lost prerequisite that makes a stated procedure unsafe. Quote the offending passage or identify the exact missing condition. Proposed next steps are not fabricated completed work. Do not classify omitted incidental details as critical.

Return one object per case and candidate. Include `case_id`, `candidate`, `scores` (the six integer scores), `critical_failures` (array of concrete descriptions, empty if none), and `reason` (brief evidence-based rationale for any deduction, or why all criteria were met). Judge independently, without browsing, reading neighboring files, or modifying any input.
