# Go Guidance

Use this file when the codebase is in Go.

## General Notes

- Prefer explicit names and package-level clarity over clever compression.
- Small interfaces should live near the consumer, not everywhere by default.
- Keep the happy path visible; guard clauses and early returns often help.
- Avoid helper explosions that force the reader to jump across many files.

## Review Reminders

- Check whether function names communicate domain intent.
- Check whether error handling overwhelms the main logic.
- Check whether a package is mixing transport, persistence, and business logic.
- Check whether abstractions feel natural in Go rather than imported mechanically from heavier OOP styles.
