# Go Guidance

Use this file when the codebase is in Go or when examples should stay close to Go idioms.

## General Notes

- Prefer small interfaces defined near the consumer.
- Prefer package-level composition and explicit constructors over inheritance-style abstractions.
- Keep struct fields and package APIs explicit; avoid hiding too much behind globals.
- Let simple packages stay simple. Not every package needs its own interface layer.

## Pattern Notes

- Singleton: if a single shared resource is truly needed, use `sync.Once` or a similarly safe initialization path. Avoid for ordinary services or business rules.
- Factory or Builder: map well to constructors, option structs, and explicit build functions.
- Strategy: often fits function values or small interfaces.
- Adapter: often fits thin wrapper types around external clients.
- Repository: useful when domain logic should not depend on SQL, ORM, or external persistence details.

## Concurrency Notes

- Prefer ownership and message passing before reaching for locks.
- Use worker pools when throughput matters and task boundaries are clear.
- Use immutable or copy-on-write data where sharing state would create subtle races.
- Introduce locks only around clearly owned data with documented invariants.

## Review Reminders

- Check whether package boundaries already provide enough separation.
- Check whether an interface improves tests or only makes tracing behavior harder.
- Check whether the proposed abstraction feels natural in Go rather than imported from class-heavy OOP habits.
