# Kotlin Guidance

Use this file when the codebase is in Kotlin.

## General Notes

- Use data classes, null-safety, and sealed types to clarify intent, not to show language features.
- Prefer straightforward expressions and readable `when` branches over nested conditionals.
- Keep extension functions close to the behavior they clarify; do not hide core logic across scattered files.
- Use constructor injection and clear package boundaries to keep flow understandable.

## Review Reminders

- Check whether scope functions improve readability or hide too much context.
- Check whether coroutines make control flow easier to follow or harder to trace.
- Check whether one function mixes validation, mapping, state mutation, and I/O.
