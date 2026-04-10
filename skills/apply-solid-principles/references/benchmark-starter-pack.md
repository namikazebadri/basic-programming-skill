# Benchmark Starter Pack

Use this file when you want the quickest meaningful comparison between Codex and Claude for SOLID-oriented reasoning.

## Why These 6 Prompts

This starter set is intentionally balanced:

- Prompt 1 tests whether the agent finds the first responsibility boundary that truly matters.
- Prompt 2 tests whether the agent applies OCP without jumping to heavy abstraction.
- Prompt 3 tests substitution safety and contract reasoning.
- Prompt 4 tests whether the agent can narrow interfaces practically.
- Prompt 5 tests dependency direction and boundary restraint.
- Prompt 6 tests resistance to interface cargo cult.

## Recommended Use

Run this starter pack first when:

- you are validating a new installation of `apply-solid-principles`
- you are comparing Codex and Claude for design-principle tasks for the first time
- you want a quick signal before building a larger SOLID eval set

## Suggested Workflow

You can reuse the generic benchmark scripts from `apply-software-patterns`:

```bash
python3 skills/apply-software-patterns/scripts/init_benchmark.py \
  --prompt-file skills/apply-solid-principles/references/benchmark-starter-prompts.md \
  --agents codex claude \
  --output /tmp/solid-benchmark-starter.csv \
  --run-label solid-starter
```

After scoring the CSV manually, summarize it with:

```bash
python3 skills/apply-software-patterns/scripts/summarize_benchmark.py \
  /tmp/solid-benchmark-starter.csv
```
