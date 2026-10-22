---
name: communicate-work
description: "Use when giving work updates, results, recommendations, handoffs, or technical explanations that a busy user must quickly understand or act on."
---

# Communicate work clearly

Help the user understand the result, assess its significance, and act with the least necessary reading.

## Core rules

1. **Lead with the useful answer.** Give the result, status, recommendation, or request before the backstory. Name the work so a returning reader can orient themselves. Include a qualification in the opening if it changes the takeaway. [1, 4, 6]
2. **Select for the reader's decision.** Include what they need to understand, believe, or act. Match their existing knowledge and requested depth. Do not use a fixed word, sentence, or bullet quota. [1, 3, 7, 8]
3. **Preserve meaning.** Keep conditions, uncertainty, scope, and material trade-offs. Distinguish a proposal, an observed result, and an unverified expectation. Compression must not change the claim. [1, 3, 10, 13]
4. **Order support by importance.** Put grouped reasons beneath the conclusion and evidence beneath the reason it supports. Put optional background last or behind a descriptive link. [4–6]
5. **Write plainly and precisely.** Prefer familiar words and direct verbs; name the actor when it matters. Keep sentences focused and each paragraph on one topic. Use consistent terms. [2, 7, 12]
6. **Make action clear.** State any real decision, next step, owner, or deadline the reader needs. Omit empty sections and invented asks. Stop when the purpose is fulfilled. [3, 8, 13]

## Choose the amount of information

Use these as adaptable applications of the sources, not a mandatory response template.

| Reader's need | Put first | Add what makes it sufficient |
| --- | --- | --- |
| Quick answer | Direct answer and necessary qualification | Only context needed to interpret it |
| Work result | Actual completion state and useful effect | What changed, evidence, important remaining limits |
| Progress or blocker | Current state and its consequence | Key finding, uncertainty, next step or needed decision |
| Choose an option | Recommendation and decisive reason | Relevant alternatives, trade-offs, and conditions that would change the choice |
| Understand a concept | Purpose and practical significance | Mechanism, concrete example, boundaries |
| Perform a task | Goal and prerequisites | Ordered actions, conditions, useful expected results |

[1, 4, 7–10, 12, 13]

**Expand** if the reader lacks a prerequisite, a claim needs support, a choice depends on a trade-off, or the user requests depth. **Compress** information already known, repeated, or unrelated to the current question. Put necessary detail in the answer; reserve links or appendices for optional depth. [1, 3, 8, 10]

For a longer explanation, keep the opening sufficient for a quick decision. Let later sections answer the reader's natural follow-up questions. For a small answer, use a plain paragraph. [1, 4, 6, 12]

## Structure the message

Apply the structures at different levels:

- **Answer first / BLUF:** put the answer or request in the opening.
- **Pyramid Principle:** organize the argument as conclusion, grouped supporting reasons, then evidence.
- **Inverted pyramid:** put the most important information first so partial reading remains useful.

Combine them when useful. Do not add a “BLUF” label or a ceremonial introduction merely to follow a framework. For sensitive interpersonal news, use enough humane context for the message to land clearly. [3–6]

For work handoffs, connect **change → purpose → evidence → remaining action**. Include only populated, relevant parts. Report what a check established and its scope; do not replace evidence with “fully verified.” [1, 8, 10, 13]

## Make technical information usable

- **Fit the purpose.** Separate instructions for completing work, guided learning, factual reference, and explanations of why something works. Choose the form the request needs. [9]
- **Build from known to new.** Explain the practical purpose, then the relevant mechanism. Define unfamiliar terms briefly at first use. Keep exact identifiers, units, and technical distinctions when the reader needs them. [7, 8, 12, 13]
- **Use concrete examples.** Show an input, action, and outcome when that makes an abstract mechanism easier to grasp. Make the example's scope clear; avoid implying a guarantee beyond it. [8, 10, 13]
- **Make procedures executable.** Put prerequisites and conditions before the affected step. Use numbered action steps, exact commands or interface labels, and expected results that let the reader check progress. [7, 11]
- **Choose useful visuals.** Use a table for comparable attributes or a diagram for relationships when it improves comprehension. Explain unfamiliar symbols; provide descriptive labels and accessible text. [7, 12–14]

## Cut words without cutting facts

Replace vague phrasing, repetition, empty lead-ins, and verbs hidden in nouns. Prefer active voice when the actor matters; use passive voice when the actor is unknown or irrelevant. Preserve qualifiers that encode real uncertainty. [2, 3, 12]

Original illustrations applying those principles:

| Before | After |
| --- | --- |
| “I would like to provide an update regarding the migration.” | “The migration is blocked by the missing export.” |
| “The service performs a validation of each request.” | “The service validates each request.” |
| “The cache invalidation mechanism ensures consistency.” | “After an update, the service clears the saved copy so the next read gets fresh data.” |
| “The cause might possibly be the connection pool.” | “The connection pool may be the cause.” |

Retain only meanings supported by the underlying facts. Do not turn “may” into “will,” an estimate into an exact value, or a test result into a production guarantee.

## Make the answer easy to scan

Use descriptive, sentence-case headings; front-load the words readers seek. Use bullets for parallel points, numbers for sequences, and tables when shared comparison fields matter. Keep list items parallel. Format code as code and use descriptive links. Avoid turning connected reasoning into a pile of fragments. [7, 8, 12, 14]

## Final check

- Does the opening answer the actual question and preserve any decisive limit?
- Can the reader tell what changed, why it matters, and what supports the claim?
- Have all requested points and necessary conditions survived editing?
- Are fact, expectation, and uncertainty distinguishable?
- Is any required action explicit and supported by the task?
- Can the reader stop after the essentials or find the needed detail quickly?
- Can anything be cut without harming meaning or action?

Read [source mapping](references/source-map.md) only when auditing the guidance. The examples and task patterns are applications of the listed sources, not source quotations.

## Sources

1. [Wes Kao: How to be concise](https://newsletter.weskao.com/p/how-to-be-concise)
2. [Purdue OWL: Concision](https://owl.purdue.edu/owl/general_writing/academic_writing/conciseness/index.html) · [Common pitfalls](https://owl.purdue.edu/owl/general_writing/academic_writing/conciseness/avoid_common_pitfalls.html)
3. [The English Center: Concision](https://englishcenter.nl/concision/)
4. [Umbrex: Lead with the answer](https://umbrex.com/resources/front-line-manager-training-program/lead-with-the-answer/)
5. [StrategyU: The Pyramid Principle](https://strategyu.co/pyramid-principle-partone/)
6. [NN/G: Inverted pyramids](https://www.nngroup.com/articles/inverted-pyramids-in-cyberspace/)
7. [Google: Style highlights](https://developers.google.com/style/highlights) · [Technical Writing One](https://developers.google.com/tech-writing/one)
8. [Microsoft: Style and voice](https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice) · [Developer content](https://learn.microsoft.com/en-us/style-guide/developer-content/)
9. [Diátaxis: Start here](https://diataxis.fr/start-here/)
10. [Write the Docs: Documentation principles](https://www.writethedocs.org/guide/writing/docs-principles/)
11. [Strapi: 12 rules of technical writing](https://handbook.strapi.io/user-success-manual/12-rules-of-technical-writing)
12. [IEEE: Plain language](https://procomm.ieee.org/communication-resources-for-engineers/other-topics/plain-language/)
13. [INNOQ: Technical documentation principles](https://www.innoq.com/en/blog/2022/01/principles-of-technical-documentation/)
14. [GitLab: Documentation style guide](https://docs.gitlab.com/development/documentation/styleguide/)
