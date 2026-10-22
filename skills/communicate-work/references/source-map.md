# Source mapping

Read this file when checking the basis of a communication rule. Source numbers refer to the linked list at the end of [SKILL.md](../SKILL.md#sources).

## What supports the skill

| Instruction family | Source support | Application to agent communication |
| --- | --- | --- |
| Lead with the answer | 4: conclusion first, brief support, more detail as needed. 6: conclusion, important support, background. | Put status or recommendation before the work history. |
| Build a coherent argument | 5: a higher-level conclusion summarizes logically ordered supporting ideas. | Group reasons by the point they support; do not recite tool calls. |
| Select sufficient detail | 1: necessary complexity and context must survive shortening. 3: include details needed to understand, believe, or act. 8: enough information for decisions. | Keep decision-changing caveats and requested reasoning; do not prescribe response-length quotas. |
| Preserve meaning and uncertainty | 3: hedges can express real uncertainty. 10: make coverage limits visible. 13: correctness is a basic requirement. | Distinguish observed, proposed, expected, and unchecked results. Do not add facts while editing. |
| Adapt to expertise | 7: identify prior knowledge and learning needs. 8: developer content can assume programming fundamentals. 12: define necessary unfamiliar terms. | Explain concepts for novices while keeping useful precision for experts. |
| Cut unnecessary wording | 2: precise words, direct verbs, removal of dead weight; recommendations allow context-sensitive exceptions. | Remove padding and duplication while preserving facts and tone. |
| Organize technical content | 9: tutorials, how-to guides, reference, and explanation serve different needs. | Choose the form the user needs; do not force all four into a reply. |
| Make instructions usable | 7: conditions before instructions. 11: prerequisites, locations, action steps, and useful results. | Put required checks before commands and retain exact values. |
| Use examples selectively | 8: code examples show how to apply reference material. 10: examples should serve common needs without overwhelming the page. | Use a concrete example when it makes the explanation actionable. |
| Format for retrieval | 7 and 14: semantic lists, code formatting, descriptive links. 12: informative headings and grouped information. | Use paragraphs for connected reasoning, lists for parallel points, numbers for order, tables for comparison. |
| Show rather than overexplain | 12: figures need labels and nearby explanation. 13: explain unfamiliar diagram symbols. | Add a visual only when it makes a relationship easier to understand. |
| Review the reader's outcome | 12: evaluate whether the audience understands and can use the message. | Check that the reader can identify the answer, its limits, and any action. |

## Synthesis boundaries

- Treat work-update patterns and checklists as applications of the cited principles. The sources do not prescribe this exact AI-agent template.
- Treat all before/after examples as original illustrations, not quotations or real completed work. Both versions must preserve the same stated facts.
- Use short sentences as an editing preference, not a numerical limit. The supplied sources differ in their length heuristics.
- Prefer active voice when it clarifies responsibility. Do not ban passive voice when the actor is unknown or irrelevant.
- Resolve the apparent conflict between documenting prerequisites and skipping fundamentals through audience knowledge.
- Keep human context for sensitive messages. Answer-first ordering is a practical default, not permission to be abrupt.
- Do not turn a house style into a universal requirement. The skill does not mandate American spelling, a fixed tone, a number of options, SCQA, or branded headings.
- Do not infer current reading-speed statistics or a universal brain-capacity limit from older articles or consulting summaries.

Only user-supplied communication sources informed these rules. Packaging instructions and the evaluation protocol are workflow scaffolding, not additional communication authorities. The separate evaluation records document access limitations and the evidence actually inspected.
