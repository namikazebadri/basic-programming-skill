---
name: apply-clean-code
description: Review, explain, and incrementally improve code using practical clean code principles with strong attention to readability, naming, small responsibilities, explicit intent, testability, and long-term maintainability. Use when Codex needs to make code easier for humans to read, reduce incidental complexity, clean up messy functions, improve naming, separate responsibilities, review code quality, or refactor without unnecessary architecture or abstraction.
---

# Apply Clean Code

## Overview

Use this skill to improve code clarity without turning "clean code" into dogma. Start from the reader's confusion and the real maintenance pain, then make the smallest changes that improve intent, readability, and safety.

Prefer practical cleanup over style theater. The goal is code that a teammate can understand, modify, and test with less friction.

## When To Use This Skill

Use this skill when the task involves any of the following:

- Cleaning up messy or overly dense code
- Improving naming, function boundaries, or module clarity
- Reviewing whether a change is readable and maintainable
- Refactoring code that technically works but is difficult to understand
- Explaining clean code principles to a teammate
- Reducing comments, duplication, or control-flow confusion by improving the code itself

Do not force this skill onto purely architectural decisions when the main question is about patterns, service boundaries, or system structure. In those cases, prefer `apply-software-patterns` or combine the two carefully.

## Workflow

### 1. Diagnose Reader Pain First

Inspect the code and identify what makes it hard to read or change.

Look for signals such as:

- Names that hide intent
- Functions doing multiple jobs
- Deep nesting or branching that obscures the happy path
- Repeated logic with small but risky variations
- Comments compensating for unclear code
- Temporal coupling or hidden side effects
- Mixed levels of abstraction in one function
- Error handling scattered through the core logic

State the problem in terms of reader pain before proposing cleanup.

### 2. Prefer The Smallest Helpful Refactor

Evaluate options in this order:

1. Keep the code and document the trade-off
2. Rename for clarity
3. Extract a small function or value
4. Separate responsibilities locally
5. Reshape module boundaries if local cleanup is not enough

Avoid broad rewrites unless clearly requested.

### 3. Optimize For Intent-Revealing Code

Prefer code that answers these questions quickly:

- What is this code trying to do?
- Where does the main flow start and end?
- Which part is business logic versus plumbing?
- Where would the next change likely go?

Favor:

- Clear names
- Small focused functions
- Consistent abstraction level inside a function
- Explicit dependencies and side effects
- Early returns when they simplify control flow

### 4. Let The Code Replace The Comment

Prefer making code clearer over adding explanatory comments.

Comments are still useful for:

- Non-obvious domain rules
- Important warnings or invariants
- Why a trade-off was chosen
- Public API contracts when behavior is subtle

Do not keep comments that merely narrate obvious code.

### 5. Keep Boundaries Honest

Improve maintainability by separating concerns that change for different reasons:

- Validation versus orchestration
- Business rules versus framework code
- Computation versus I/O
- Data transformation versus persistence

If a function or module mixes these heavily, refactor toward clearer boundaries.

### 6. Protect Behavior While Refactoring

When editing code:

- Preserve working behavior first
- Make one meaningful cleanup at a time
- Add or update tests around risky behavior
- Avoid mixing cleanup with unrelated feature changes
- Keep diffs readable enough for code review

### 7. Keep Clean Code Practical

Reject cleanup that mainly adds churn:

- Splitting tiny code into too many files
- Renaming everything without improving comprehension
- Replacing obvious logic with fashionable abstraction
- Obsessing over short functions while hiding the real flow
- Applying rules mechanically without regard to local context

## Output Contract

For review or analysis tasks, structure the response around:

1. Main readability problem
2. Best cleanup option and smaller fallback
3. Why the change improves comprehension
4. Trade-offs or risks
5. Incremental refactor plan
6. Test impact

For implementation tasks, keep the explanation short and focus on:

- What changed
- How readability or maintainability improved
- What stayed intentionally simple
- What to test next

## Quality Bar

The response or implementation should usually satisfy all of the following:

- Names the reader-facing problem before prescribing cleanup
- Improves intent without adding unnecessary indirection
- Uses naming, extraction, or structure before reaching for comments
- Preserves the main flow or makes it easier to follow
- Avoids cleanup churn that does not materially improve comprehension
- Keeps refactoring incremental and test-aware

If these conditions cannot be met, scale the cleanup down.

## Reference Guide

Read only the files that match the current task:

- `agents/claude.md`: Claude Code adapter memory for using this package through `CLAUDE.md`
- `references/benchmark-harness.md`: workflow for benchmarking Codex versus Claude against this skill package
- `references/benchmark-starter-pack.md`: recommended first 10-prompt benchmark pack for quick clean-code comparisons
- `references/benchmark-starter-prompts.md`: small benchmark prompt pack for fast first-pass evaluation
- `references/principles.md`: practical clean code principles and when they matter
- `references/smells.md`: common code smells, misuse signals, and cleanup cautions
- `references/review-checklist.md`: concise checklist for code review and refactoring quality
- `references/before-after-examples.md`: concrete examples of cleaner naming, functions, and flow
- `references/eval-prompts.md`: evaluation prompts to test whether the skill improves code quality decisions
- `references/evaluation-rubric.md`: scoring rubric for whether the clean-code output is actually good enough
- `references/go-guidance.md`: Go-oriented clean code guidance
- `references/kotlin-guidance.md`: Kotlin-oriented clean code guidance

Scripts are available for benchmark setup and summary:

- `scripts/init_benchmark.py`: generates a blank benchmark score sheet from the clean-code prompt packs
- `scripts/summarize_benchmark.py`: summarizes scored benchmark CSV files by agent and category

Do not read every reference file by default. Load only what the task needs.

## Guardrails

- Do not rewrite large areas just to satisfy aesthetic rules
- Do not replace readable code with abstraction for its own sake
- Do not add comments where better naming would solve the problem
- Do not split code so aggressively that the main flow becomes harder to follow
- Do not judge code quality only by function length or line count
- Do not treat "clean code" as more important than correct behavior

The goal is code that remains understandable in real projects with deadlines, legacy constraints, and future change pressure.
