# Benchmark Starter Prompts

Use this file for a fast first-pass benchmark before running the full 30-prompt suite.

A good first benchmark should sample:

- one case where a pattern is likely justified
- one case where the pattern should probably be rejected
- one case involving architecture escalation
- one case involving readability-focused refactoring
- one case involving concurrency or lifecycle trade-offs

## Starter Set

1. A service constructs three payment clients with repeated setup logic in multiple handlers. Should this use a factory, builder, or just a helper?
2. The app has one configuration loader used everywhere. Is Singleton justified, or should dependencies still be passed explicitly?
3. An external SDK shape does not match the interface expected by your domain service. Should this be an Adapter or a direct translation function?
4. Shipping cost rules vary by country and provider, and new rules keep arriving. Should we use Strategy or better-organized conditionals?
5. Image processing jobs spike under load and spawn too many workers. Should the design move to a worker pool?
6. SQL queries are leaking into business logic. Should this become a Repository, DAO, or simply a thin query function?
7. A query API wants chainable calls. Should it use a fluent interface or plain functions for clarity?
8. A CRUD-heavy product is getting larger, but most issues are still local. Stay layered, or move to Clean Architecture?
9. The team wants microservices because the codebase feels messy. Is modular monolith or service-based architecture the better next step?
10. Refactor this service to be easier for a new teammate to follow, but avoid introducing patterns unless they truly reduce complexity.
