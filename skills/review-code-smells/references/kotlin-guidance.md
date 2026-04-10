# Kotlin Guidance

Use this file when reviewing Kotlin code for smells.

- Watch for scope-function overuse that hides context.
- Watch for nested `if` and `when` flows that obscure the happy path.
- Watch for Android or framework concerns leaking into domain logic.
- Watch for extension functions scattering core business behavior across files.
