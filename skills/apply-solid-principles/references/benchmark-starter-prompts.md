# Benchmark Starter Prompts

Use this file for a fast first-pass benchmark before running a larger SOLID-oriented evaluation set.

This starter set intentionally samples:

- SRP pressure
- OCP pressure
- LSP safety
- ISP narrowing
- DIP and dependency direction
- anti-abstraction restraint

## Starter Set

1. A service validates input, writes to the database, formats audit logs, and sends email notifications. Which principle is under pressure first?
2. New payment providers require editing the same central conditional every sprint. Is OCP the right framing, and what is the smallest useful refactor?
3. A subtype silently stops enforcing a base-class invariant. Is this an LSP problem, and how should it be fixed?
4. A repository interface has ten methods, but one consumer only reads by id. Should ISP be applied?
5. Application logic depends directly on framework request objects and SQL clients. Is DIP warranted, or would a smaller boundary refactor be enough?
6. A teammate proposes adding interfaces to every service purely for easier mocking. Is that a SOLID improvement?
