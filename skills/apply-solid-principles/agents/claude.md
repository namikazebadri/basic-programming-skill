# Apply SOLID Principles

Use these instructions when the task involves SRP, OCP, LSP, ISP, DIP, dependency direction, or focused design refactoring.

## Working Style

- Start from the design pain before naming a principle.
- Prefer the smallest change that improves cohesion, substitution safety, or dependency direction.
- Compare the recommendation against a simpler local refactor.
- Reject abstraction that mainly adds ceremony.
- Preserve readability and behavior while refactoring incrementally.

## What To Optimize For

- Clear responsibilities
- Safer extension points
- Narrow and relevant interfaces
- Explicit dependencies
- Maintainability without abstraction theater

## Load These References As Needed

- `skills/apply-solid-principles/SKILL.md` for the core workflow and guardrails
- `skills/apply-solid-principles/references/benchmark-harness.md` for a fair comparison workflow across agents
- `skills/apply-solid-principles/references/benchmark-starter-pack.md` for the fast comparison workflow across agents
- `skills/apply-solid-principles/references/benchmark-starter-prompts.md` for the first-pass SOLID benchmark set
- `skills/apply-solid-principles/references/principles.md` for practical SOLID heuristics
- `skills/apply-solid-principles/references/misuse-signals.md` for overengineering warnings
- `skills/apply-solid-principles/references/review-checklist.md` for review questions
- `skills/apply-solid-principles/references/before-after-examples.md` for concrete refactor examples
- `skills/apply-solid-principles/references/eval-prompts.md` for evaluation prompts
- `skills/apply-solid-principles/references/evaluation-rubric.md` for output quality checks
- `skills/apply-solid-principles/references/go-guidance.md` for Go-oriented guidance
- `skills/apply-solid-principles/references/kotlin-guidance.md` for Kotlin-oriented guidance

## Stop Signals

- Do not add interfaces for speculative flexibility.
- Do not fragment cohesive code just to name a principle.
- Do not let SOLID language hide the actual problem.
