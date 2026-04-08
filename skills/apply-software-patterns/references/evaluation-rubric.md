# Evaluation Rubric

Use this file to assess whether the skill output is strong enough before returning it.

Score each category from 0 to 2.

## 1. Problem Diagnosis

- 0: Jumps straight to pattern names without defining the real problem.
- 1: Identifies the issue, but only partially connects it to codebase constraints.
- 2: States the concrete design pressure and why it matters in this codebase now.

## 2. Simplicity Bias

- 0: Recommends a pattern without considering a simpler alternative.
- 1: Mentions a simpler option but does not evaluate it seriously.
- 2: Explicitly compares the recommendation against a smaller refactor or staying simple.

## 3. Readability Impact

- 0: Ignores whether the result is easier for humans to read and trace.
- 1: Mentions readability loosely.
- 2: Explains how names, flow, boundaries, or dependency visibility become clearer.

## 4. Architectural Reasoning

- 0: Uses architecture labels as slogans.
- 1: Connects architecture to some constraints.
- 2: Grounds architecture advice in dependency direction, ownership, team reality, and rate of change.

## 5. Trade-Off Awareness

- 0: Presents the recommendation as purely good.
- 1: Mentions one downside.
- 2: Clearly states costs, misuse risks, and what would change the recommendation later.

## 6. Incremental Actionability

- 0: Suggests a large rewrite or vague future design.
- 1: Gives some action steps, but they are broad.
- 2: Proposes a narrow, verifiable next step with test impact.

## Interpreting The Score

- 10-12: Strong output. Safe to use as-is.
- 7-9: Acceptable, but likely missing clarity or a sharper simplicity check.
- 4-6: Weak. Rework the reasoning before answering.
- 0-3: Pattern cargo cult risk. Start over from the actual problem.
