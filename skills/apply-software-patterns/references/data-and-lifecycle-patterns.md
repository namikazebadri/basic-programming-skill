# Data And Lifecycle Patterns

Use this file when the task involves persistence boundaries, messaging flow, expensive object reuse, cleanup rules, or ownership of resources.

## Data Access And Messaging

- Repository: keep domain-oriented data access separate from business logic.
- DAO: isolate storage details when persistence technology is expected to vary.
- Unit of Work: coordinate a set of related changes as one transaction boundary.
- Data Mapper: keep persistence mapping out of rich domain models.
- Publish-Subscribe: broadcast events to subscribers without direct dependencies.
- Pipeline: process data through modular, sequential stages.

## Resource And Lifetime Management

- Object Pool: reuse expensive-to-create objects when lifecycle cost is high and pooled state can be reset safely.
- Lazy Initialization: defer creation until the resource is actually needed.
- Reference Counting: track active references to decide when cleanup should happen, especially in runtimes or systems without automatic lifecycle handling.
- Scope-Based Management: bind resource lifetime to an execution scope so acquisition and cleanup stay paired.
- Dispose Pattern: release non-memory resources explicitly and safely when the runtime will not do it for you.

## Selection Notes

- Prefer plain constructors over `Object Pool` unless allocation cost or external setup cost is proven meaningful.
- Use `Lazy Initialization` when startup cost matters, but keep initialization failures visible.
- Prefer scope-bound cleanup over distant manual release calls whenever the language supports it naturally.
- Use `Publish-Subscribe` only when decoupling is worth the loss of direct traceability.
- Keep repositories and DAOs thin; they should clarify boundaries, not hide business rules.

## Readability Checks

- Is resource ownership obvious?
- Can a reader tell who is responsible for cleanup?
- Does the abstraction reduce persistence leakage, or only move SQL and ORM complexity elsewhere?
- If an event is published, is the flow still traceable in logs, tests, and code structure?
