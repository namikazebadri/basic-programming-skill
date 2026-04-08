# Java Guidance

Use this file when the codebase is in Java or JVM-style enterprise applications.

## General Notes

- Prefer explicit package boundaries and constructor injection over service locators or static access.
- Keep framework annotations from dominating domain code where business logic longevity matters.
- Use interfaces intentionally, not automatically for every class.
- Favor module or package clarity over deep inheritance trees.

## Pattern Notes

- Builder fits immutable objects with many optional fields, especially where validation matters.
- Strategy, Command, and Template Method are natural in Java, but still should not replace small readable control flow without need.
- Adapter and Facade are useful around external systems and noisy frameworks.
- Repository is appropriate when persistence concerns leak upward, but should not become generic abstraction theater.
- Domain-driven and layered architectures often map well to explicit packages, application services, and aggregate boundaries.

## Review Reminders

- Check whether Spring or similar frameworks are encouraging accidental over-abstraction.
- Check whether interfaces improve tests and substitutions, or merely duplicate implementation names.
- Check whether transaction boundaries and side effects remain visible.
