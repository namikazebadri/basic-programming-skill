# Modern Code Patterns

Use this file when the task involves fluent APIs, composable functions, query-command clarity, or modern code styles that improve expressiveness.

## Functional And Modern Code

- Higher-Order Function: pass behavior as a function when it removes repetition and keeps logic composable.
- Function Composition: combine small functions into a clear transformation flow when the resulting pipeline remains readable.
- Monadic Pattern: model optional values, deferred results, or error-carrying computations explicitly when the team and language can support the abstraction without confusion.
- Fluent Interface: design chainable APIs when chaining improves legibility and preserves valid sequencing.
- Command Query Separation (CQS): keep state-changing operations separate from read-only queries to reduce surprise and make APIs easier to reason about.

## Selection Notes

- Prefer ordinary functions before introducing heavily abstract functional layers.
- Use fluent APIs only when chaining reveals intent rather than hiding side effects.
- Treat monadic styles carefully in teams that are not already comfortable with them; readability for the local codebase matters more than conceptual elegance.
- Apply `CQS` as a clarity tool, not a rigid doctrine.

## Readability Checks

- Does the composed flow read left-to-right without mental backtracking?
- Are side effects explicit?
- Would a simple helper function be clearer than another chainable layer?
- Does the API communicate which calls mutate state and which only read data?
