# Benchmark Starter Pack

Use this file when you want the quickest meaningful comparison between Codex and Claude.

## Why These 10 Prompts

This starter set is intentionally balanced:

- Prompt 1 tests creational judgment without over-abstracting.
- Prompt 2 tests whether the agent resists Singleton misuse.
- Prompt 3 tests boundary thinking around unstable dependencies.
- Prompt 4 tests whether growing variation is recognized without forcing heavy structure.
- Prompt 5 tests concurrency reasoning and throughput thinking.
- Prompt 6 tests persistence leakage and boundary design.
- Prompt 7 tests modern API style versus plain readability.
- Prompt 8 tests architecture restraint in a growing but still ordinary system.
- Prompt 9 tests whether the agent avoids jumping from messiness straight to microservices.
- Prompt 10 tests readability-first refactoring without pattern cargo cult behavior.

## Recommended Use

Run this starter pack first when:

- you are validating a new installation of the skill
- you are comparing Codex and Claude for the first time
- you want a quick signal before investing in the full 30-prompt benchmark

Use the full set in `references/eval-prompts.md` when:

- results are close and you need more confidence
- you want category-level comparisons across the full catalog
- you changed the skill and want a broader regression check
