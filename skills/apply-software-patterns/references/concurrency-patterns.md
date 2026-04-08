# Concurrency Patterns

Use this file when the task involves parallel work, async coordination, shared mutable state, scheduling, or throughput bottlenecks.

## Coordination Patterns

- Thread Pool: manage a reusable pool of worker threads when raw thread creation would be wasteful or unstable.
- Worker Pool: distribute independent jobs to bounded workers when throughput matters and work items are uniform enough to queue.
- Producer-Consumer: separate production and processing rates through a queue or channel.
- Future or Promise: represent work whose result arrives later while keeping composition explicit.
- Async Callback: use for event-style async completion where callback flow stays readable and the platform idiom expects it.
- Fork-Join: split a large task into independent subproblems and merge results when the work is naturally parallelizable.
- Guarded Suspension: delay execution until a required condition becomes true, usually around coordination or readiness.

## Synchronization And Safety Patterns

- Read-Write Lock: optimize concurrent reads while protecting writes when read contention dominates and invariants are clear.
- Double-Checked Locking: lazily initialize shared state with minimal locking only when the language memory model makes it safe and well understood.
- Immutable Object: eliminate race conditions by removing mutation from shared data.

## Selection Notes

- Prefer ownership transfer, message passing, or immutability before adding locks.
- Prefer worker pools over ad hoc goroutine or thread explosions when backpressure matters.
- Use callbacks only when they match the platform style and do not create nested control-flow confusion.
- Use `Fork-Join` only when the split, scheduling, and merge overhead is justified by real parallel work.
- Treat `Double-Checked Locking` as a specialized optimization, not a default pattern.

## Readability Checks

- Can a maintainer explain when work starts, where it runs, and when it completes?
- Are cancellation, timeout, and error paths visible?
- Is ownership of shared state obvious?
- Would a serialized design be simpler and fast enough?
