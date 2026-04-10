---
name: review-code-smells
description: Review code for maintainability smells, readability risks, hidden complexity, and design drift, then explain the most important findings with practical remediation guidance. Use when Codex needs to identify code smells, review technical debt, prioritize cleanup, explain why code feels hard to change, or suggest targeted refactors without unnecessary rewrites.
---

# Review Code Smells

## Overview

Use this skill to review code with a maintainability-first lens. The goal is to identify the smells that matter, explain why they matter, and recommend the smallest effective remediation.

Prefer concrete findings over generic advice. A good smell review helps a teammate understand what is wrong, why it is risky, and what to change first.

## When To Use This Skill

Use this skill when the task involves any of the following:

- Reviewing code quality or technical debt
- Explaining why code feels hard to change
- Prioritizing cleanup opportunities
- Identifying maintainability, readability, or design smells
- Reviewing a PR for hidden complexity or code health regressions

Do not use this skill as a substitute for architecture design or detailed pattern selection. It is a review and prioritization skill first.

## Workflow

### 1. Find The Most Expensive Smells

Look for issues that create real maintenance cost, such as:

- Long functions with mixed responsibilities
- Repeated branching around the same concept
- Primitive obsession and vague data shaping
- Feature envy or logic living far from the data it depends on
- Shotgun surgery risk when one change touches many files
- Divergent change where one unit changes for many unrelated reasons
- Hidden side effects or temporal coupling
- Comments compensating for unclear code
- Over-abstraction that makes tracing behavior harder

Prioritize smells by likely maintenance pain, not by textbook neatness.

### 2. Explain The Risk Clearly

For each important smell, explain:

- what it is
- where it appears
- why it increases change cost, bug risk, or confusion
- what smaller change would reduce the risk

### 3. Prefer Reviewable Remediation

Recommend fixes in this order:

1. naming and structure cleanup
2. local extraction or simplification
3. responsibility separation
4. boundary refactor only if local fixes are not enough

Avoid broad rewrites unless the user explicitly wants one.

### 4. Keep Findings Actionable

Strong findings are:

- specific
- tied to actual code behavior
- ordered by severity or change cost
- paired with a realistic next step

Weak findings are:

- generic style complaints
- rules without context
- cleanup advice that costs more than the smell

## Output Contract

For review tasks, present:

1. Findings first, ordered by severity
2. Why each finding matters
3. Suggested remediation direction
4. Open questions or assumptions
5. Residual risks or testing gaps

If no significant smells are present, say so explicitly and mention any smaller risks that remain.

## Quality Bar

The response should usually satisfy all of the following:

- focuses on the highest-value smells first
- explains real maintenance or readability risk
- avoids generic rule recitation
- recommends the smallest helpful remediation
- keeps findings concrete enough to act on

## Reference Guide

Read only the files that match the current task:

- `agents/claude.md`: Claude Code adapter memory for using this package through `CLAUDE.md`
- `references/benchmark-harness.md`: workflow for benchmarking Codex versus Claude against this skill package
- `references/benchmark-starter-pack.md`: recommended first benchmark pack for quick smell-review comparisons
- `references/benchmark-starter-prompts.md`: small benchmark prompt pack for fast first-pass evaluation
- `references/smell-catalog.md`: common code smells and why they matter
- `references/severity-guide.md`: how to prioritize findings by likely cost and risk
- `references/review-checklist.md`: concise smell-review checklist
- `references/remediation-playbook.md`: practical fix patterns and when to stop
- `references/eval-prompts.md`: evaluation prompts to test smell-review quality
- `references/evaluation-rubric.md`: scoring rubric for whether the smell review is actually useful
- `references/go-guidance.md`: Go-oriented smell review notes
- `references/kotlin-guidance.md`: Kotlin-oriented smell review notes

Scripts are available for benchmark setup and summary:

- `scripts/init_benchmark.py`: generates a blank benchmark score sheet from the smell-review prompt packs
- `scripts/summarize_benchmark.py`: summarizes scored benchmark CSV files by agent and category

Do not read every reference file by default. Load only what the task needs.

## Guardrails

- Do not flood the user with low-value nits when bigger smells exist
- Do not call something a smell without explaining the maintenance cost
- Do not recommend rewrites when local cleanup would do
- Do not confuse style preferences with meaningful findings
- Do not ignore readability and traceability when code is technically correct

The goal is to help teams see and fix the smells that actually slow them down.
