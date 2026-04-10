# Code Smells

Use this file when reviewing code or deciding what to clean up first.

## Common Smells

- Vague names like `data`, `process`, `handle`, or `doStuff`
- Long functions that mix setup, validation, business rules, and I/O
- Deep nesting that hides the happy path
- Repeated conditionals spread across multiple call sites
- Mixed abstraction levels in one function
- Comments that explain what obvious code is doing
- Boolean flags that dramatically change behavior
- Hidden mutation or side effects
- Large parameter lists that suggest weak boundaries
- Error handling duplicated in many branches

## Cleanup Priorities

Prefer fixing these first:

1. Names that block understanding
2. Mixed responsibilities in a hot path
3. Control flow that is hard to trace
4. Repetition that creates bug risk
5. Comments masking unclear code

## Misuse Signals

- The refactor creates more files than understanding
- Every helper has only one call site and hides the main logic
- Cleanup changes style but not comprehension
- A "clean" result becomes harder to debug
