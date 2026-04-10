# Kotlin Guidance

Use this file when the codebase is in Kotlin.

- Favor constructor injection and clear package boundaries.
- Use interfaces where multiple meaningful implementations or consumer-shaped contracts exist.
- Prefer composition, sealed hierarchies, and focused services over inheritance-heavy models.
- Watch for framework annotations or Android layers leaking into core logic.
