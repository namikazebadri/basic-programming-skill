# Apply Software Patterns

Use these instructions when the task involves design patterns, architecture decisions, refactoring for better boundaries, or reviewing whether code is becoming hard to read and maintain.

## Working Style

- Start from the concrete design pressure before naming a pattern.
- Prefer the smallest change that improves readability, maintainability, testability, and explicit dependency flow.
- Compare the recommendation against a simpler alternative before committing to a named pattern.
- Reject patterns that mainly add ceremony, indirection, or architectural theater.
- Prefer incremental refactors over broad rewrites.
- Keep code understandable to engineers who do not know pattern vocabulary.

## What To Optimize For

- Clear dependency direction
- Human-readable flow from entry point to business logic
- Explicit ownership of state, resources, and cleanup
- Boundaries that improve testing and maintenance
- Architecture choices that match team size, project lifetime, and operational reality

## Review And Implementation Expectations

- Explain the problem before the pattern name.
- Name at least one trade-off or misuse risk.
- Say how readability or architectural clarity improves.
- Keep simple code simple.
- When implementing, preserve behavior first and refactor in small steps.

## Pattern And Architecture Scope

This package is intended to cover:

- Creational, structural, and behavioral patterns
- Concurrency patterns
- Data access and messaging patterns
- Resource and lifetime management patterns
- Functional and modern code patterns
- Architecture patterns including layered, clean, hexagonal, onion, DDD, modular monolith, microservices, service-based, event-driven, CQRS, serverless, MVC, MVP, and MVVM

## Load These References As Needed

- `skills/apply-software-patterns/SKILL.md` for the core workflow and guardrails
- `skills/apply-software-patterns/references/benchmark-harness.md` for a fair comparison workflow across agents
- `skills/apply-software-patterns/references/eval-prompts.md` to evaluate whether responses stay problem-first and simplicity-aware
- `skills/apply-software-patterns/references/before-after-examples.md` for concrete transformations that improve readability or boundaries
- `skills/apply-software-patterns/references/decision-matrix.md` for pattern-selection heuristics
- `skills/apply-software-patterns/references/design-patterns.md` for creational, structural, and behavioral patterns
- `skills/apply-software-patterns/references/concurrency-patterns.md` for async and synchronization trade-offs
- `skills/apply-software-patterns/references/data-and-lifecycle-patterns.md` for repository, messaging, pooling, lifecycle, and cleanup choices
- `skills/apply-software-patterns/references/modern-code-patterns.md` for fluent APIs, function composition, monadic style, and CQS
- `skills/apply-software-patterns/references/architecture-patterns.md` for architecture choices and escalation rules
- `skills/apply-software-patterns/references/kotlin-guidance.md` for Kotlin-oriented implementation guidance
- `skills/apply-software-patterns/references/typescript-guidance.md` for TypeScript-oriented implementation guidance
- `skills/apply-software-patterns/references/python-guidance.md` for Python-oriented implementation guidance
- `skills/apply-software-patterns/references/java-guidance.md` for Java-oriented implementation guidance
- `skills/apply-software-patterns/references/go-guidance.md` for Go-oriented implementation guidance
- `skills/apply-software-patterns/references/anti-patterns.md` for overengineering checks
- `skills/apply-software-patterns/references/review-checklist.md` for review questions
- `skills/apply-software-patterns/references/evaluation-rubric.md` for output quality checks
- `skills/apply-software-patterns/references/catalog-coverage.md` to confirm the supported catalog

## Stop Signals

- Do not recommend a pattern only because it is famous.
- Do not introduce interfaces or layers for speculative future flexibility.
- Do not recommend distributed architecture before module boundaries are healthy.
- Do not sacrifice local readability for conceptual purity.
