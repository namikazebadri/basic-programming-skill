# Clean Code Principles

Use this file when the task is mainly about readability, maintainability, and human comprehension.

## Core Ideas

- Write code for the next reader, not only the current author.
- Prefer clear intent over cleverness.
- Keep one function or block focused on one meaningful job.
- Keep a consistent level of abstraction inside a function.
- Make dependencies and side effects visible.
- Remove duplication when it hides risk or change cost, not only when lines look similar.
- Use comments sparingly and make the code carry the explanation whenever possible.

## Practical Heuristics

- Good names usually beat extra comments.
- Early returns often improve readability when they flatten nesting.
- Smaller functions help only when the overall flow stays traceable.
- Parameters should make intent clearer, not push hidden dependencies around.
- Error handling should support the main flow instead of burying it.
- Tests are part of maintainability; unclear code with fragile tests is still not clean.

## Real-World Perspective

Use clean code as a tool for long-term maintainability, especially in systems that live beyond a small tutorial or toy example. In real systems, readability must survive deadlines, legacy constraints, onboarding, and repeated changes.
