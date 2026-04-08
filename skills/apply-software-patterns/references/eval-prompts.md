# Eval Prompts

Use this file to evaluate whether the skill actually changes agent behavior in the intended way.

A good answer should:

- diagnose the concrete problem before naming a pattern
- compare against a simpler alternative
- explain readability and boundary impact
- name at least one trade-off
- propose an incremental next step when implementation is requested

## Creational

1. A service constructs three payment clients with repeated setup logic in multiple handlers. Should this use a factory, builder, or just a helper?
2. The app has one configuration loader used everywhere. Is Singleton justified, or should dependencies still be passed explicitly?
3. A request object has twelve optional fields and validation rules. Should we use Builder or keep plain constructors with option structs?

## Structural

4. An external SDK shape does not match the interface expected by your domain service. Should this be an Adapter or a direct translation function?
5. A UI package needs a simpler entry point to several low-level services. Is Facade warranted or would one helper module do?
6. The app creates thousands of nearly identical style objects. Is Flyweight appropriate, or is the added indirection not worth it?

## Behavioral

7. Shipping cost rules vary by country and provider, and new rules keep arriving. Should we use Strategy or better-organized conditionals?
8. You need undo support in a drawing editor. Is Memento the right fit, or would an explicit history object be clearer?
9. You have a stable AST with many operations added over time. Should you introduce Visitor, or would method-based behavior stay simpler?
10. A tiny domain-specific expression language is growing. Is Interpreter justified, or should parsing stay ad hoc for now?

## Concurrency

11. Image processing jobs spike under load and spawn too many workers. Should the design move to a worker pool?
12. A shared cache is lazily initialized under concurrency. Is double-checked locking safe here, or should initialization be simplified?
13. Event handling uses nested callbacks that are hard to follow. Keep async callbacks, or move to a clearer future/promise or queue-based flow?

## Data And Lifecycle

14. SQL queries are leaking into business logic. Should this become a Repository, DAO, or simply a thin query function?
15. A broker publishes many domain events, but debugging event flow is painful. Keep publish-subscribe, or reduce indirection?
16. Database connections are expensive to create. Should an object pool be introduced, or is the existing pool already enough?
17. A file handle must always be released on failure paths. Is a dispose-style abstraction needed, or does scope-based cleanup already solve it?

## Modern Code

18. A transformation pipeline chains many data-mapping steps. Is function composition improving clarity, or should the flow become named helper steps?
19. A query API wants chainable calls. Should it use a fluent interface or plain functions for clarity?
20. Several service methods both return data and mutate state. Should Command Query Separation be introduced?
21. Optional and error-prone workflows are modeled with nested null checks. Would a monadic style help, or would it confuse the team more?

## Architecture

22. A CRUD-heavy product is getting larger, but most issues are still local. Stay layered, or move to Clean Architecture?
23. The team wants microservices because the codebase feels messy. Is modular monolith or service-based architecture the better next step?
24. Business rules are complex and domain language matters a lot. Is Domain-Driven Architecture worth the added modeling effort?
25. Read and write paths have very different performance needs. Is CQRS justified, or can read models be split more simply?
26. The team wants serverless for a system with long-running workflows. Is serverless a good fit, or do platform constraints dominate?

## Review-Oriented Prompts

27. Review this module and identify where pattern vocabulary is being used to justify unnecessary indirection.
28. Review this architecture and tell me whether the code structure actually reflects the stated boundaries.
29. Refactor this service to be easier for a new teammate to follow, but avoid introducing patterns unless they truly reduce complexity.
30. Explain why the current design should stay simple even though a textbook pattern seems available.
