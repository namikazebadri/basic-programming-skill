# Design Patterns

Use this file when the task is about code-level design choices rather than whole-system architecture.
This file intentionally covers the classic creational, structural, and behavioral families so the skill can reason across the standard catalog instead of only a small subset.

## Creational

- Singleton: reserve for shared infrastructure resources with a true single lifecycle. Avoid for normal business services because it hides dependencies and hurts testability.
- Factory Method: use when callers should not know the concrete type they receive.
- Abstract Factory: use when families of related objects must vary together.
- Builder: use when construction is multi-step, optional-heavy, or needs validation before build.
- Prototype: use when cloning an existing configured object is simpler than reconstructing it.

## Structural

- Adapter: wrap incompatible interfaces without changing stable code on either side.
- Bridge: separate abstraction from implementation when both vary independently.
- Composite: treat leaf and grouped objects through a consistent interface.
- Decorator: add responsibilities dynamically without changing the wrapped type.
- Facade: expose a simpler entry point to a complicated subsystem.
- Flyweight: share immutable intrinsic state when huge numbers of similar objects would otherwise waste memory.
- Proxy: control access for caching, security, lazy loading, or remote boundaries.

## Behavioral

- Strategy: switch algorithms or policies without changing the caller.
- Observer: publish state changes to multiple listeners with loose coupling.
- Command: represent actions as objects for queuing, undo, logging, or delayed execution.
- Chain of Responsibility: pass a request through handlers until one accepts it.
- State: model behavior that changes by internal state without large conditional trees.
- Template Method: fix the algorithm skeleton while varying selected steps.
- Mediator: centralize collaboration when object-to-object communication becomes tangled.
- Memento: capture and restore state snapshots when undo or rollback behavior matters and encapsulation should remain intact.
- Iterator: traverse collections without exposing their underlying representation.
- Visitor: separate operations from object structures when many stable node types need multiple distinct operations.
- Interpreter: model a small grammar or rule language when expressions themselves are first-class inputs.

## Selection Notes

- Prefer an ordinary function or small refactor over a named pattern when the pressure is isolated.
- Prefer explicit dependencies over hidden globals.
- Prefer boundaries that improve testing or comprehension, not just extensibility in theory.
- Prefer `Flyweight`, `Visitor`, and `Interpreter` only when the problem structure truly matches them; these are easy to over-apply.
- If a pattern increases the number of concepts faster than it improves traceability, scale back.
