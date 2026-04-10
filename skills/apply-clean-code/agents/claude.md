# Apply Clean Code

Use these instructions when the task involves making code easier to read, understand, review, or maintain.

## Working Style

- Start from the reader's confusion before proposing cleanup.
- Prefer the smallest refactor that makes intent clearer.
- Improve naming, flow, and responsibility boundaries before adding abstraction.
- Keep code understandable to engineers reading it under real project pressure.
- Preserve behavior first and refactor incrementally.

## What To Optimize For

- Intent-revealing names
- Clear top-to-bottom control flow
- Small focused responsibilities
- Honest separation of business logic and plumbing
- Testable changes with minimal churn

## Review And Implementation Expectations

- Explain the main readability problem first.
- Suggest a smaller fallback if the cleanup feels too broad.
- Say how the refactor improves comprehension.
- Name at least one risk or trade-off.
- Keep simple code simple.

## Load These References As Needed

- `skills/apply-clean-code/SKILL.md` for the core workflow and guardrails
- `skills/apply-clean-code/references/benchmark-harness.md` for a fair comparison workflow across agents
- `skills/apply-clean-code/references/benchmark-starter-pack.md` for the fast comparison workflow across agents
- `skills/apply-clean-code/references/benchmark-starter-prompts.md` for the first-pass clean-code benchmark set
- `skills/apply-clean-code/references/principles.md` for clean code heuristics
- `skills/apply-clean-code/references/smells.md` for common readability and maintainability problems
- `skills/apply-clean-code/references/review-checklist.md` for review questions
- `skills/apply-clean-code/references/before-after-examples.md` for concrete refactor examples
- `skills/apply-clean-code/references/eval-prompts.md` for evaluation prompts
- `skills/apply-clean-code/references/evaluation-rubric.md` for output quality checks
- `skills/apply-clean-code/references/go-guidance.md` for Go-oriented guidance
- `skills/apply-clean-code/references/kotlin-guidance.md` for Kotlin-oriented guidance

## Stop Signals

- Do not rewrite broadly when a rename or small extraction would do.
- Do not add layers or classes just to look cleaner.
- Do not keep comments that only explain obvious code.
- Do not optimize style at the expense of behavior or reviewability.
