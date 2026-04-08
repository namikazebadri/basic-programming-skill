---
name: apply-software-patterns
description: Choose, reject, explain, review, and incrementally apply software design patterns and architecture patterns with strong attention to readability, maintainability, testability, explicit dependencies, and overengineering risk. Use when Codex needs to decide whether a pattern fits a codebase, compare alternatives, review code for human-readable structure, refactor toward clearer boundaries, explain patterns to a teammate, or recommend architecture direction for a growing system.
---

# Apply Software Patterns

## Overview

Use this skill to make design decisions practical, not dogmatic. Start from the real problem and codebase constraints, then recommend the smallest design move that improves readability, maintainability, testability, and room to grow.

Prefer incremental refactors over big rewrites. When a pattern is not justified, say so clearly and keep the design simpler.

Treat pattern names as tools, not goals. The target is code that another engineer can read, trace, modify, and test without needing a pattern catalog open beside them.

## When To Use This Skill

Use this skill when the task involves any of the following:

- Choosing between a named pattern and a simpler refactor
- Reviewing whether a code path is becoming too coupled, too abstract, or too hard to read
- Refactoring code toward clearer boundaries, dependency direction, or architectural layers
- Explaining why a pattern should or should not be introduced
- Checking whether code structure reflects the domain cleanly
- Advising on architecture growth from simple layering toward stronger boundaries

Do not force this skill onto ordinary cleanup tasks that only need naming, extraction, or smaller functions. In those cases, prefer straightforward refactoring language over pattern vocabulary.

## Workflow

### 1. Understand the Real Design Problem

Inspect the request, codebase, and failure mode before naming a pattern. Identify both the technical pressure and the human-readability problem.

Look for signals such as:

- Object creation is duplicated, conditional, or coupled to callers
- Interfaces are incompatible or dependencies are too tightly connected
- Behavior varies by runtime rules, state, or workflow stage
- Concurrency and shared state are causing race conditions or contention
- Business rules are mixed with framework, transport, or persistence details
- The code is difficult to trace because responsibilities are blurred
- Architectural intent is unclear from package, module, or folder boundaries
- The user mainly needs explanation, review, or architecture guidance rather than code changes

Identify the true constraint set:

- Team size and code ownership
- Expected project lifetime
- Complexity of business rules
- Testability requirements
- Runtime performance or concurrency needs
- Frequency of change
- Whether the code is a prototype, CRUD app, or long-lived system
- Whether the current code is hard for a new teammate to read safely

Do not jump to a famous pattern just because the symptoms sound familiar.

### 2. Classify the Problem Before Choosing a Solution

Use the smallest category that explains the issue:

- Creational problem: object creation, lifecycle, configuration, dependency construction
- Structural problem: composition, abstraction boundaries, incompatible interfaces, facade needs
- Behavioral problem: interchangeable algorithms, event propagation, request routing, stateful behavior
- Concurrency problem: worker coordination, async flow, shared mutable state, throughput control
- Resource or lifetime problem: expensive objects, cleanup, ownership, lazy setup, lifecycle safety
- Functional or modern API problem: composability, fluent APIs, command-query split, pipeline clarity
- Architecture problem: dependency direction, bounded layers, service boundaries, domain isolation
- Readability problem: implicit flow, hidden dependencies, vague naming, or structure that obscures intent

If the issue is mostly readability, naming, duplication, or missing tests, prefer ordinary refactoring over introducing a pattern.

### 3. Default to the Simplest Sufficient Design

Always evaluate these options in order:

1. Keep current design and document the trade-off
2. Apply a small refactor without adding a named pattern
3. Apply one focused pattern
4. Introduce broader architectural restructuring only if the codebase context justifies it

Reject patterns when they add more ceremony than value.

Anti-signals include:

- The project is tiny, short-lived, or mostly CRUD
- The proposed abstraction exists only to satisfy theory
- The pattern hides dependencies and makes testing harder
- The team will struggle to maintain the added indirection
- The same goal can be met with a smaller, explicit change
- The code becomes harder to read top-to-bottom after the refactor

### 4. Compare Candidate Options Explicitly

When recommending a pattern, compare it against at least one alternative. Include:

- Why this option matches the current problem
- What trade-off it introduces
- Why a simpler option is insufficient or sufficient
- How the recommendation affects readability for a new maintainer
- How the recommendation clarifies or complicates dependency direction
- What would make the recommendation change later

For architecture choices, always compare the recommended target against a simpler baseline such as layered architecture or a modular monolith before suggesting microservices, CQRS, or event-driven designs.

### 5. Implement or Refactor Incrementally

When the user wants code changes:

- Preserve working behavior first
- Refactor toward boundaries in small steps
- Avoid mass renames or whole-project rewrites unless clearly requested
- Add or update tests around the changed behavior
- Keep dependencies explicit
- Keep framework details out of core business rules when recommending cleaner architecture
- Preserve or improve the ability to follow a request path from entry point to core logic
- Prefer changes that make intent visible in names, module boundaries, and constructor signatures

If introducing a pattern, make the change local and verifiable:

- Strategy: extract one varying behavior first
- Adapter: wrap one incompatible boundary first
- Factory or Builder: isolate one construction hotspot first
- Repository or DAO: move one data access concern behind an interface first
- Clean or Hexagonal architecture: move one use case inward and one adapter outward first

### 6. Teach With Context

When the user asks for explanation or mentoring:

- Explain the problem before the pattern name
- Emphasize when not to use the pattern
- Use concrete trade-offs instead of slogans
- Relate the recommendation to maintainability, testability, and team comprehension
- Distinguish design pattern, architecture pattern, framework feature, and simple refactor

### 7. Optimize For Human Readability

Prefer designs that make the code easier for humans to navigate:

- Keep dependencies visible through constructors, parameters, or clearly owned modules
- Favor explicit names over abstract pattern terminology in code identifiers
- Use small interfaces only when multiple meaningful behaviors or test seams exist
- Keep pattern-specific machinery close to the problem it solves
- Align files, packages, and folders with architectural intent when possible
- Avoid turning simple control flow into a maze of indirection
- If a pattern is used, the code should still read well to someone who does not know the pattern name

### 8. Validate The Recommendation

Before finalizing, pressure-test the result:

- Does this change reduce coupling instead of only moving it elsewhere?
- Will a new teammate understand where to add the next feature?
- Are boundaries clearer in code, not just in explanation?
- Is the pattern earning its keep through simpler tests, cleaner flow, or safer change points?
- Would a smaller refactor have delivered nearly the same value?

## Output Contract

For analysis or review tasks, structure the response around:

1. Design diagnosis
2. Best option and runner-up
3. Why the recommendation fits this codebase
4. Readability and architectural boundary impact
5. Risks, anti-patterns, and overengineering checks
6. Incremental implementation or refactor plan
7. Test impact

For implementation tasks, keep the explanation short and focus on:

- What changed
- Why this pattern or refactor was chosen
- How the change improved readability or boundaries
- What stayed intentionally simple
- What to test next

When reviewing or generating code, ensure the result can answer these questions clearly:

- Where does business logic live?
- Where do external dependencies enter?
- Where would the next variation or feature likely go?
- Which part is intentionally simple and should stay that way?

## Quality Bar

The response or implementation should usually satisfy all of the following:

- Names the concrete problem before naming a pattern
- Compares the recommendation against a simpler fallback
- Calls out at least one downside or trade-off
- Explains how readability, traceability, or boundary clarity changes
- Avoids speculative interfaces or architecture layers
- Preserves incremental delivery and testability

If these conditions cannot be met, scale the recommendation down.

## Reference Guide

Read only the files that match the current task:

- `agents/claude.md`: Claude Code adapter memory for using this package through `CLAUDE.md`
- `references/benchmark-harness.md`: workflow for benchmarking Codex versus Claude against this skill package
- `references/benchmark-starter-pack.md`: recommended first 10-prompt comparison pack for quick Codex versus Claude checks
- `references/benchmark-starter-prompts.md`: small benchmark prompt pack for fast first-pass evaluation
- `references/eval-prompts.md`: evaluation prompt set to test whether the skill improves agent behavior in realistic cases
- `references/before-after-examples.md`: concrete code and structure transformations showing when a pattern helps and when simplicity wins
- `references/decision-matrix.md`: decision heuristics, selection workflow, and escalation signals
- `references/design-patterns.md`: creational, structural, and behavioral pattern guidance, including classic GoF coverage and selection notes
- `references/concurrency-patterns.md`: concurrency coordination patterns, async trade-offs, and synchronization cautions
- `references/data-and-lifecycle-patterns.md`: data access, messaging, resource lifecycle, pooling, disposal, and ownership guidance
- `references/modern-code-patterns.md`: functional composition, fluent APIs, CQS, and modern readability-oriented code patterns
- `references/architecture-patterns.md`: layered, clean, hexagonal, onion, domain-driven, monolithic, modular monolith, microservices, service-based, event-driven, CQRS, serverless, and UI-oriented architecture guidance
- `references/anti-patterns.md`: overengineering checks, misuse signals, and common design smells
- `references/go-guidance.md`: Go-oriented implementation notes and trade-offs for common pattern choices
- `references/kotlin-guidance.md`: Kotlin-oriented implementation notes and trade-offs for common pattern choices
- `references/typescript-guidance.md`: TypeScript-oriented implementation notes and trade-offs for common pattern choices
- `references/python-guidance.md`: Python-oriented implementation notes and trade-offs for common pattern choices
- `references/java-guidance.md`: Java-oriented implementation notes and trade-offs for common pattern choices
- `references/usage-examples.md`: example prompts, response framing, and concrete before-or-after style guidance
- `references/catalog-coverage.md`: explicit coverage map of the supported pattern and architecture catalog
- `references/review-checklist.md`: concise review checklist for readability, boundaries, and safe pattern use
- `references/evaluation-rubric.md`: scoring rubric for whether the skill output is actually good enough

Scripts are available for benchmark setup and summary:

- `scripts/init_benchmark.py`: generates a blank benchmark score sheet from `eval-prompts.md`
- `scripts/summarize_benchmark.py`: summarizes scored benchmark CSV files by agent and category

Do not read every reference file by default. Load only what the task needs.

## Guardrails

- Do not recommend Singleton for ordinary business services just to simplify access
- Do not recommend Clean Architecture, Hexagonal Architecture, or microservices for very small systems without a clear justification
- Do not turn every conditional into Strategy or every wrapper into Facade
- Do not introduce interfaces solely for future speculation
- Do not add layers whose only purpose is to look architecturally mature
- Do not hide core behavior behind factories, registries, or dependency injection indirection unless the pressure is real
- Do not sacrifice local readability for pattern purity
- Do not let the pattern name replace direct reasoning about coupling, lifecycle, and change cost

The goal is software that stays understandable and adaptable over time, with code structure that humans can read and trust, not software that collects pattern vocabulary.
