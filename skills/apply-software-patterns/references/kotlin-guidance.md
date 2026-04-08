# Kotlin Guidance

Use this file when the codebase is in Kotlin, especially for backend services, Android apps, or multiplatform modules.

## General Notes

- Prefer explicit constructor injection and clear package boundaries over hidden service lookup.
- Use data classes, sealed hierarchies, and extension functions where they improve clarity, but avoid scattering core business flow across too many extension files.
- Keep framework and platform concerns out of domain logic where business rules need to stay testable.
- Favor small focused abstractions over deep inheritance chains.

## Pattern Notes

- Strategy often maps cleanly to interfaces, lambdas, or sealed-dispatch depending on how many behaviors really vary.
- Builder is useful when Java interop, many optional parameters, or staged construction make named arguments insufficient.
- Adapter works well around Android APIs, third-party SDKs, persistence libraries, or transport clients.
- Repository can help when database or API details leak into use-case logic, but avoid turning it into generic abstraction boilerplate.
- State and Command often fit UI state flows, reducers, or action handling, but keep them local unless the complexity is real.

## Review Reminders

- Check whether coroutines make concurrency flow clearer or whether async boundaries are becoming too implicit.
- Check whether sealed classes or result wrappers are clarifying domain states instead of adding ceremony.
- Check whether extension functions improve discoverability or hide important logic away from the main flow.
