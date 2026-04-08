# Decision Matrix

Use this file when the main task is selecting a pattern, rejecting one, or explaining why a design change is worth the cost.

## Quick Flow

1. Define the concrete problem in one sentence.
2. Name the pressure: creation, structure, behavior, concurrency, data access, or architecture.
3. Check whether a simpler refactor solves it first.
4. Compare one focused pattern against one simpler alternative.
5. Recommend the smallest change that improves maintainability or testability.

## Questions To Ask

- Is the pain local or spread across the codebase?
- Is the problem caused by unstable requirements, too many dependencies, or poor boundaries?
- Does the code need extensibility now, or is that speculative?
- Will this recommendation reduce coupling or only move it around?
- Will tests become easier to write and understand?
- Will a new teammate understand the abstraction quickly?
- Is the project a prototype, CRUD app, or long-lived product?

## Pattern Selection Heuristics

| Situation | Start With | Consider Instead When |
| --- | --- | --- |
| Object creation is duplicated or full of conditionals | Factory Method or Builder | Plain constructor or helper is enough |
| One boundary must fit an incompatible dependency | Adapter | A direct translation function is sufficient |
| Multiple algorithms change by rule or config | Strategy | A small conditional is still clearer |
| A complex subsystem needs a simpler entry point | Facade | Callers only need one helper function |
| Shared behavior depends on internal mode or status | State | Explicit conditionals remain small and readable |
| Data access leaks into business logic | Repository or DAO | A thin query function is enough for now |
| Framework details dominate core logic | Clean or Hexagonal boundaries | Layered structure with disciplined modules is sufficient |
| Concurrency causes shared-state issues | Immutable data, worker pool, producer-consumer | Single-threaded or serialized flow is acceptable |

## Escalation Signals

Move from simple refactor to named pattern when:

- The same design pressure appears in multiple places
- New feature requests repeatedly modify the same branching logic
- Construction, coordination, or persistence details are leaking everywhere
- Testing requires too much setup because dependencies are hidden or tangled

Move from pattern-level change to architecture-level change when:

- Business rules are consistently mixed with transport, database, and framework code
- Team size and deployment surface make loose boundaries materially valuable
- The system is expected to evolve across multiple integrations and clients

## Stop Signals

Reject or scale down the recommendation when:

- The project is small and not expected to grow much
- The abstraction introduces more files than real understanding
- The proposal mainly exists to match a known pattern name
- The refactor would interrupt delivery without reducing meaningful risk
