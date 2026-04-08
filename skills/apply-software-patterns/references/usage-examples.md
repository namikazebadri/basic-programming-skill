# Usage Examples

Use this file to calibrate tone and output shape.

## Example Requests That Should Trigger This Skill

- "Review this service layer and tell me whether Strategy or plain conditionals are better."
- "Refactor this Go module so database code does not leak into business logic."
- "Is Singleton appropriate for this config loader?"
- "We are growing fast. Should this app move to Clean Architecture or stay layered?"
- "Compare modular monolith and microservices for this team and codebase."
- "Explain when Repository is useful and when it is just extra boilerplate."
- "Refactor this code so the flow is easier for humans to follow without overengineering it."
- "Review whether this architecture makes dependency direction obvious."
- "Would `Flyweight` or an object cache be a better fit here?"
- "Should this API use a fluent interface or plain functions?"
- "Do we need `Object Pool`, or is normal allocation fine?"
- "Is `Service-Based Architecture` enough here, or are microservices justified?"
- "Would `DDD` improve this codebase or just add ceremony?"

## Expected Response Style

- Start from the current problem, not the pattern catalog.
- Include a simpler fallback option.
- Name the trade-off clearly.
- Point out misuse risk when relevant.
- If implementation is requested, recommend a narrow first step that can be tested.
- Explain whether the code becomes easier or harder to read after the change.
- Keep architecture language grounded in code boundaries, not folder theater.
- When a specialized pattern is considered, explain why the simpler nearby option is not enough.

## Example Decision Framing

Problem:
The handler contains branching logic for multiple payment providers and keeps growing.

Recommendation:
Extract provider behavior behind a Strategy-like boundary, but keep the first refactor small by moving only provider-specific charge logic behind an interface or function table.

Why:
Behavior varies by provider, the branching is growing, and tests can target each policy separately.

Why not bigger:
Do not introduce a full architecture rewrite unless provider workflows start affecting many modules.

## Example Review Framing

Problem:
The service layer technically works, but database queries, HTTP concerns, and validation rules are mixed together. A new engineer would need to read three files just to understand one use case.

Recommendation:
Keep the existing layered structure, but move validation and business rules into a use-case-oriented service function. Leave the database package in place and introduce a repository boundary only around the query path that is leaking into domain logic.

Why:
This improves readability and dependency direction without paying the cost of a full Clean Architecture rollout.

Why not bigger:
The codebase is not yet showing enough complexity to justify ports-and-adapters everywhere.

## Example "Reject The Pattern" Framing

Problem:
There are two small conditionals selecting a formatter implementation.

Recommendation:
Do not introduce Strategy yet. Keep the explicit conditional and extract a helper with better names.

Why:
The variation is still local, and Strategy would add indirection without improving testability much.

What to watch:
Revisit only if new formatting rules keep arriving and the branching starts spreading.

## Example Implementation Bias

When code changes are requested, prefer transformations like:

- Extract one dependency-construction hotspot instead of creating an application-wide factory layer
- Move one use case out of a controller instead of redesigning every module
- Introduce one adapter around an unstable dependency instead of wrapping every dependency preemptively
- Improve naming and flow first when that solves most of the comprehension problem

## Example Specialized Pattern Framing

Problem:
Thousands of tiny value objects are being allocated repeatedly, and most of their state is identical.

Recommendation:
Consider `Flyweight` only if profiling shows memory pressure is real. Otherwise keep normal objects and focus on simpler data-shape cleanup first.

Why:
`Flyweight` can help when intrinsic shared state is large and stable, but it also makes object construction and reasoning less direct.

## Example Architecture Escalation Framing

Problem:
The monolith is growing, but most pain comes from unclear module boundaries rather than independent deployment needs.

Recommendation:
Move toward a modular monolith or coarse service-based split before discussing microservices.

Why:
This keeps operational complexity lower while still clarifying ownership and architecture boundaries.
