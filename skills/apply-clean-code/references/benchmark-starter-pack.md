# Benchmark Starter Pack

Use this file when you want the quickest meaningful comparison between Codex and Claude for clean-code judgment.

## Why These 10 Prompts

This starter set is intentionally balanced:

- Prompt 1 tests whether the agent starts with naming and intent.
- Prompt 2 tests function responsibility and local boundary cleanup.
- Prompt 3 tests whether the agent prefers better code over explanatory comments.
- Prompt 4 tests resistance to over-splitting and refactor theater.
- Prompt 5 tests flattening control flow while preserving readability.
- Prompt 6 tests practical cleanup in Go without unnecessary abstraction.
- Prompt 7 tests whether the agent can distinguish real duplication from merely similar code.
- Prompt 8 tests review quality on code that is correct but painful to maintain.
- Prompt 9 tests readability-first refactoring with restraint.
- Prompt 10 tests resistance to churn disguised as improvement.

## Recommended Use

Run this starter pack first when:

- you are validating a new installation of `apply-clean-code`
- you are comparing Codex and Claude for clean-code tasks for the first time
- you want a quick signal before running the full prompt set

Use the full set in `references/eval-prompts.md` when:

- results are close and you need more confidence
- you want to retest after revising the skill
- you want broader evidence that the agent is consistently readability-first

## Suggested Workflow

You can use the generic benchmark scripts already present in this repository:

```bash
python3 skills/apply-software-patterns/scripts/init_benchmark.py \
  --prompt-file skills/apply-clean-code/references/benchmark-starter-prompts.md \
  --agents codex claude \
  --output /tmp/clean-code-benchmark-starter.csv \
  --run-label clean-code-starter
```

After scoring the CSV manually, summarize it with:

```bash
python3 skills/apply-software-patterns/scripts/summarize_benchmark.py \
  /tmp/clean-code-benchmark-starter.csv
```
