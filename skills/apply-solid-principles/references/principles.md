# SOLID Principles

Use this file when the task is about object, module, or dependency design.

## SRP

Use SRP when one unit changes for multiple unrelated reasons. Look for validation, orchestration, persistence, and formatting all mixed together.

## OCP

Use OCP when new behaviors repeatedly require edits to stable decision logic. Prefer local extension seams, not blanket indirection.

## LSP

Use LSP when subtype behavior surprises callers, weakens invariants, or changes semantics hidden behind the same contract.

## ISP

Use ISP when consumers depend on wide interfaces they barely use. Prefer smaller consumer-shaped contracts.

## DIP

Use DIP when high-level logic depends directly on low-level infrastructure details. Prefer stable abstractions at the boundary, not everywhere.

## Practical Reminder

SOLID is useful only if it makes code easier to change, reason about, and test.
