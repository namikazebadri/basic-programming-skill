---
name: apply-solid-principles
description: Review, explain, and incrementally improve code using the SOLID principles with strong attention to readability, maintainability, explicit dependencies, testability, and overengineering risk. Use when Codex needs to judge whether code violates SRP, OCP, LSP, ISP, or DIP, refactor toward cleaner object and module boundaries, explain SOLID to a teammate, or improve design without blindly adding abstraction.
---

# Apply SOLID Principles

## Overview

Use this skill to apply SOLID as a practical decision tool, not as a slogan. Start from the design pain, then use the smallest refactor that improves cohesion, substitution safety, interface fit, or dependency direction.

Prefer local, readable changes over class explosion. SOLID should make code easier to change and understand, not merely more abstract.

## When To Use This Skill

Use this skill when the task involves any of the following:

- A class, module, or service is taking too many responsibilities
- The user asks whether a design violates SRP, OCP, LSP, ISP, or DIP
- A refactor is needed to improve dependency direction or testability
- Inheritance feels unsafe or surprising
- Interfaces are too broad or dependencies are too concrete
- The user wants a practical explanation of SOLID in a real codebase

Do not force SOLID language onto small cleanup tasks where naming, extraction, or simpler flow already solves the issue.

## Workflow

### 1. Diagnose The Design Pressure

Inspect the current code and identify what makes it hard to change safely.

Look for signals such as:

- One unit changing for many unrelated reasons
- New behaviors requiring edits in too many places
- Subclasses weakening invariants or surprising callers
- Interfaces that force consumers to depend on methods they do not need
- Core logic depending directly on framework, transport, or infrastructure details
- Abstract layers that exist only in theory and are rarely justified

State the problem before naming the principle.

### 2. Map The Problem To The Smallest Relevant Principle

Use the smallest principle that explains the pain:

- SRP: one unit changes for multiple unrelated reasons
- OCP: new behavior requires editing stable logic repeatedly
- LSP: subtype behavior violates expectations of the base contract
- ISP: consumers depend on wide interfaces they barely use
- DIP: high-level logic depends on low-level details instead of stable abstractions

If the problem is mostly readability or naming, prefer `apply-clean-code`.

### 3. Default To The Smallest Sufficient Refactor

Evaluate these options in order:

1. Keep current design and document the trade-off
2. Rename or extract a smaller responsibility locally
3. Narrow an interface or separate one dependency
4. Introduce one focused abstraction or boundary
5. Reshape a module only if local fixes are not enough

Reject SOLID-driven refactors when they mainly increase ceremony.

### 4. Compare Against A Simpler Alternative

When recommending a SOLID-oriented change, explain:

- Why this principle matches the actual pain
- Why a simpler local refactor is or is not enough
- What trade-off the change introduces
- How readability, substitution safety, or dependency direction improves

### 5. Refactor Incrementally

When implementing:

- Preserve behavior first
- Change one responsibility boundary at a time
- Prefer small interfaces and explicit dependencies
- Avoid inheritance-heavy redesign unless clearly justified
- Add or update tests around the changed seam

### 6. Keep SOLID Practical

Reject changes like:

- Introducing interfaces for speculation
- Splitting tiny services into many classes with no real ownership gain
- Using DIP to hide obvious dependencies unnecessarily
- Treating OCP as "never edit existing code"
- Using inheritance when composition is clearer and safer

## Output Contract

For analysis or review tasks, structure the response around:

1. Main design problem
2. Best fitting SOLID principle and simpler fallback
3. Why the recommendation improves changeability
4. Trade-offs or misuse risks
5. Incremental refactor plan
6. Test impact

For implementation tasks, keep the explanation short and focus on:

- What changed
- Which design pressure was addressed
- How the code became safer to extend or easier to maintain
- What stayed intentionally simple

## Quality Bar

The response or implementation should usually satisfy all of the following:

- Names the real design pressure before naming a principle
- Avoids abstraction that does not improve changeability or testability
- Compares against a simpler local refactor
- Improves cohesion, substitution safety, interface fit, or dependency direction
- Keeps refactoring incremental and readable

If these conditions cannot be met, scale the recommendation down.

## Reference Guide

Read only the files that match the current task:

- `agents/claude.md`: Claude Code adapter memory for using this package through `CLAUDE.md`
- `references/benchmark-harness.md`: workflow for benchmarking Codex versus Claude against this skill package
- `references/benchmark-starter-pack.md`: recommended first benchmark pack for quick SOLID comparisons
- `references/benchmark-starter-prompts.md`: small benchmark prompt pack for fast first-pass evaluation
- `references/principles.md`: practical interpretation of SRP, OCP, LSP, ISP, and DIP
- `references/misuse-signals.md`: common SOLID cargo-cult mistakes and overengineering warnings
- `references/review-checklist.md`: concise review checklist for SOLID-oriented design work
- `references/before-after-examples.md`: examples showing focused SOLID refactors
- `references/eval-prompts.md`: evaluation prompts to test whether the skill improves design judgment
- `references/evaluation-rubric.md`: scoring rubric for whether the SOLID output is actually good enough
- `references/go-guidance.md`: Go-oriented SOLID guidance
- `references/kotlin-guidance.md`: Kotlin-oriented SOLID guidance

Scripts are available for benchmark setup and summary:

- `scripts/init_benchmark.py`: generates a blank benchmark score sheet from the SOLID prompt packs
- `scripts/summarize_benchmark.py`: summarizes scored benchmark CSV files by agent and category

Do not read every reference file by default. Load only what the task needs.

## Guardrails

- Do not introduce interfaces solely for mocking
- Do not use SRP to justify splitting cohesive logic into fragments
- Do not use OCP to avoid reasonable edits to stable code
- Do not ignore readability while chasing abstract purity
- Do not treat SOLID as more important than correct behavior or clear ownership

The goal is code that changes more safely over time, not code that collects design buzzwords.
