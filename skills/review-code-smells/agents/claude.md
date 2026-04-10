# Review Code Smells

Use these instructions when the task is mainly about identifying code smells, hidden complexity, or maintainability risks.

## Working Style

- Findings first, ordered by importance.
- Focus on smells that materially increase change cost or bug risk.
- Explain why the smell matters before suggesting cleanup.
- Prefer the smallest realistic remediation.
- Avoid nitpicking when larger structural issues exist.

## What To Optimize For

- Actionable findings
- Real maintenance impact
- Clear prioritization
- Remediation that is reviewable and proportional

## Load These References As Needed

- `skills/review-code-smells/SKILL.md` for the core workflow and guardrails
- `skills/review-code-smells/references/benchmark-harness.md` for a fair comparison workflow across agents
- `skills/review-code-smells/references/benchmark-starter-pack.md` for the fast comparison workflow across agents
- `skills/review-code-smells/references/benchmark-starter-prompts.md` for the first-pass smell-review benchmark set
- `skills/review-code-smells/references/smell-catalog.md` for common smell definitions
- `skills/review-code-smells/references/severity-guide.md` for prioritization guidance
- `skills/review-code-smells/references/review-checklist.md` for review questions
- `skills/review-code-smells/references/remediation-playbook.md` for practical fix patterns
- `skills/review-code-smells/references/eval-prompts.md` for evaluation prompts
- `skills/review-code-smells/references/evaluation-rubric.md` for output quality checks
- `skills/review-code-smells/references/go-guidance.md` for Go-oriented guidance
- `skills/review-code-smells/references/kotlin-guidance.md` for Kotlin-oriented guidance

## Stop Signals

- Do not overload the user with minor nits.
- Do not confuse style preferences with code smells.
- Do not suggest a rewrite when a local remediation is enough.
