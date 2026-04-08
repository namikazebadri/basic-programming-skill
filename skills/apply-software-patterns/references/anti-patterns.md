# Anti-Patterns And Misuse Signals

Use this file to pressure-test a recommendation before proposing or implementing it.

## Common Misuse Signals

- The recommendation exists because the pattern is famous, not because the pressure is real.
- The abstraction hides dependencies instead of clarifying them.
- The number of concepts grows faster than the number of solved problems.
- The design adds ceremony to avoid a small explicit conditional or helper.
- Interfaces are added without multiple meaningful implementations.

## Specific Warnings

- Singleton as a service locator in disguise
- Clean Architecture implemented as folder theater with business logic still stuck in handlers
- Strategy added for two tiny branches that will likely never grow
- Repository added on top of a simple query path without domain value
- Microservices introduced before module boundaries are healthy inside the monolith
- Event-driven flows added without tracing, idempotency, or ownership clarity

## Smells To Call Out In Reviews

- Business rules coupled directly to HTTP, ORM, or framework types
- Construction logic repeated in many call sites
- Deep branching around mode, status, or provider behavior
- Mutable shared state across goroutines or workers
- Database models reused as domain models and transport models at the same time
- Controllers, handlers, or routers making domain decisions

## Healthy Countermoves

- Pass dependencies explicitly
- Extract one boundary at a time
- Move one use case inward before introducing a larger architecture frame
- Keep DTOs, persistence models, and domain models distinct when their responsibilities differ
- Choose readability over pattern purity
