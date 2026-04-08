# Architecture Patterns

Use this file when the task is about system structure, dependency direction, or long-term maintainability.

## Layered Architecture

Use for conventional applications that benefit from clear responsibility boundaries without heavy abstraction. It is a strong baseline for many business systems.

## Monolithic Architecture

Use when one deployable unit keeps development simple and operational overhead low. A monolith is not inherently bad; an unstructured monolith is.

## Clean Architecture

Use when business rules are important, the project is expected to live for a long time, and framework or database independence will improve testing and maintainability.

Watch for:

- Over-abstraction in small systems
- Framework details leaking into use cases
- Controllers or handlers containing business logic

## Hexagonal Architecture

Use when external systems, transports, or adapters change frequently and the domain should stay insulated behind ports and adapters.

## Onion Architecture

Use when dependency direction toward the domain is the main concern and the team is comfortable with layered inward dependencies.

## Domain-Driven Architecture

Use when the domain is complex enough that ubiquitous language, aggregate boundaries, and explicit domain modeling materially improve correctness and team understanding.

## Modular Monolith

Use when a system is large enough to need strong module boundaries but not yet complex enough to justify distributed services. This is often a better default than microservices.

## Microservices

Use only when independent deployment, team autonomy, scaling differences, or organizational boundaries justify the operational cost.

Do not recommend for:

- Early products still discovering their domain
- Teams without strong observability and deployment maturity
- Systems whose complexity is mostly internal rather than organizational

## Service-Based Architecture

Use when a system benefits from a few coarse-grained services with clearer ownership, but full microservice decomposition would add too much operational burden.

## Event-Driven Architecture

Use when asynchronous collaboration, decoupled reactions, or integration-heavy workflows are central. Be explicit about eventual consistency and debugging cost.

## CQRS

Use when read and write models have materially different scaling or complexity needs. Avoid for ordinary CRUD systems.

## Serverless Architecture

Use when elastic scaling, event-triggered execution, and reduced infrastructure management are meaningful advantages, and cold starts, platform limits, and operational observability are acceptable trade-offs.

## UI-Oriented Patterns

- MVC: useful when separating input handling, view rendering, and model logic in classic UI flows.
- MVP: useful when a presenter should coordinate view behavior explicitly and UI frameworks make passive views desirable.
- MVVM: useful when UI state binding and testable view models improve separation in reactive or binding-friendly frameworks.

## Architecture Recommendation Rules

- Start from monolithic, layered, or modular monolith by default.
- Escalate to Clean, Onion, Hexagonal, or Domain-Driven approaches when business rules need real protection from technical details and domain language matters.
- Prefer service-based architecture before microservices when the system needs some deployment separation but not full distributed complexity.
- Escalate to microservices, event-driven architecture, CQRS, or serverless only when there is concrete operational, scaling, or domain evidence.
- Keep architecture advice tied to team size, change rate, testing needs, and deployment reality.
- A clean modular monolith is usually a better stepping stone than an early distributed system.
