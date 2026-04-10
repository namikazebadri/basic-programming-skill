# Evaluation Rubric

Use this file to assess whether the clean-code skill output is strong enough before returning it.

Score each category from 0 to 2.

## 1. Problem Diagnosis

- 0: Jumps into cleanup advice without identifying what makes the code hard to read or maintain.
- 1: Identifies a readability problem, but only partially explains why it matters.
- 2: States the main reader-facing problem clearly and connects it to maintenance or comprehension cost.

## 2. Simplicity Bias

- 0: Recommends a broad refactor or abstraction without testing smaller options first.
- 1: Mentions a smaller option but does not evaluate it seriously.
- 2: Clearly prefers the smallest effective cleanup and explains why it is enough.

## 3. Readability Impact

- 0: Does not explain how the code becomes easier to read.
- 1: Mentions readability loosely.
- 2: Explains how names, flow, structure, or responsibility boundaries become clearer.

## 4. Trade-Off Awareness

- 0: Presents the cleanup as purely good.
- 1: Mentions one downside or risk.
- 2: Names the real costs, churn risk, or cases where the cleanup could make things worse.

## 5. Incremental Actionability

- 0: Suggests a vague cleanup or a large rewrite.
- 1: Gives action steps, but they are broad or hard to review safely.
- 2: Proposes a narrow, reviewable next step that preserves behavior.

## 6. Test Awareness

- 0: Ignores test impact.
- 1: Mentions tests in passing.
- 2: Explains what behavior should be protected or what tests should be added or updated.

## Interpreting The Score

- 10-12: Strong output. Safe to use as-is.
- 7-9: Acceptable, but likely missing clarity or refactor restraint.
- 4-6: Weak. Rework the cleanup reasoning before answering.
- 0-3: Cleanup theater risk. Start over from the reader pain.
