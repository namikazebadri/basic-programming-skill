# Benchmark Starter Pack

Use this file when you want the quickest meaningful comparison between Codex and Claude for code-smell review quality.

## Why These 6 Prompts

This starter set is intentionally balanced:

- Prompt 1 tests whether the agent surfaces the highest-value smells first.
- Prompt 2 tests whether the agent recognizes recurring change pain.
- Prompt 3 tests whether it can detect abstraction drift instead of praising indirection.
- Prompt 4 tests whether it identifies divergent change and mixed responsibilities.
- Prompt 5 tests whether it catches hidden side effects despite small function size.
- Prompt 6 tests whether it can distinguish between multiple likely smell classes and prioritize correctly.

## Recommended Use

Run this starter pack first when:

- you are validating a new installation of `review-code-smells`
- you are comparing Codex and Claude for review tasks for the first time
- you want a quick signal before expanding the smell-review benchmark

## Suggested Workflow

You can reuse the generic benchmark scripts from `apply-software-patterns`:

```bash
python3 skills/apply-software-patterns/scripts/init_benchmark.py \
  --prompt-file skills/review-code-smells/references/benchmark-starter-prompts.md \
  --agents codex claude \
  --output /tmp/code-smells-benchmark-starter.csv \
  --run-label smells-starter
```

After scoring the CSV manually, summarize it with:

```bash
python3 skills/apply-software-patterns/scripts/summarize_benchmark.py \
  /tmp/code-smells-benchmark-starter.csv
```
