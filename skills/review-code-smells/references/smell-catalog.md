# Smell Catalog

Use this file when reviewing code quality and maintainability.

- Long Function: too many concerns mixed into one flow.
- Large Class or Module: too many responsibilities owned together.
- Shotgun Surgery: one change requires touching many places.
- Divergent Change: one unit changes for many unrelated reasons.
- Feature Envy: logic depends more on another object's data than its own.
- Primitive Obsession: domain meaning hidden behind raw strings, ints, maps, or flags.
- Repeated Branching: the same concept encoded in conditionals across many places.
- Temporal Coupling: methods or steps must occur in the right order, but the contract is implicit.
- Hidden Side Effects: functions mutate or perform I/O unexpectedly.
- Comment Compensation: comments explain what clearer code should express directly.
- Abstraction Drift: wrappers, helpers, or interfaces make behavior harder to trace.
