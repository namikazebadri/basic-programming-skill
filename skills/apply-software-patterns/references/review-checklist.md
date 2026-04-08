# Review Checklist

Use this file when reviewing code, planning a refactor, or validating whether a pattern recommendation is actually helping.

## Problem Fit

- Is there a real design pressure, not just an abstract pattern opportunity?
- Is the pain recurring, growing, or affecting multiple change points?
- Would a simpler refactor solve most of the issue?

## Readability

- Can a new maintainer follow the main request or workflow path without jumping through many files?
- Are names concrete enough to reveal responsibility?
- Are dependencies visible instead of hidden behind globals, registries, or vague helpers?
- Did the refactor reduce branching or only move it elsewhere?

## Boundaries

- Is business logic separated from transport, framework, or persistence details where it matters?
- Do package or module boundaries reflect architectural intent?
- Is dependency direction easier to explain after the change?
- Is the pattern applied locally before being spread broadly?

## Pattern Discipline

- Is a named pattern earning its keep through better tests, clearer extension points, or lower coupling?
- Were speculative interfaces or layers avoided?
- Would the code still make sense to someone who does not recognize the pattern name?
- Is the chosen abstraction smaller than the problem, or at least no larger than necessary?

## Delivery Safety

- Can the change be shipped incrementally?
- Are tests protecting the changed behavior?
- Did the refactor preserve existing behavior before expanding scope?
- Is there a clear next step if the design pressure continues to grow?
