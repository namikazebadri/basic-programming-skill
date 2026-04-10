# Go Guidance

Use this file when reviewing Go code for smells.

- Watch for packages that mix transport, persistence, and business rules.
- Watch for error handling that buries the happy path.
- Watch for interfaces that exist only to satisfy tests.
- Prefer findings tied to package boundaries, traceability, and ownership.
