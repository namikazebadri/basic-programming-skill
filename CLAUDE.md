# Skill Router

This repository contains multiple skills. Do not load every skill by default.

Start by classifying the user's request, then load only the most relevant skill adapter from `skills/<skill-name>/agents/claude.md`.

## Skill Selection

- For design patterns, architecture choices, refactoring toward better boundaries, or deciding whether a pattern fits:
  `@skills/apply-software-patterns/agents/claude.md`
- For readability, naming, smaller responsibilities, clearer flow, or practical refactoring without architectural expansion:
  `@skills/apply-clean-code/agents/claude.md`
- For SRP, OCP, LSP, ISP, DIP, dependency direction, interface fit, or SOLID-oriented refactoring:
  `@skills/apply-solid-principles/agents/claude.md`
- For code review focused on maintainability smells, technical debt, hidden complexity, design drift, or remediation prioritization:
  `@skills/review-code-smells/agents/claude.md`

## Combination Rules

- Load more than one skill only when the task clearly spans multiple concerns.
- Prefer `apply-clean-code` plus `apply-software-patterns` when the user wants both readability and design-pattern judgment.
- Prefer `apply-solid-principles` plus `apply-software-patterns` when dependency direction and design seams are both central.
- Prefer `review-code-smells` first when the user asks for a review; add another skill only if the findings clearly require deeper design or cleanup guidance.

## Default Behavior

- Stay problem-first.
- Prefer the smallest effective change.
- Preserve readability and maintainability.
- Avoid loading unnecessary skill context.
