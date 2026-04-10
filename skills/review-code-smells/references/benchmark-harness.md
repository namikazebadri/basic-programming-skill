# Benchmark Harness

Use this file when you want to compare how different agents behave with `review-code-smells`, especially Codex versus Claude Code.

## Goal

Measure whether the agent:

- surfaces the highest-value smells first
- explains why a smell matters
- prioritizes findings clearly
- avoids generic nitpicks
- recommends proportional remediation

## Inputs

- Prompt set: `references/eval-prompts.md`
- Starter prompt set: `references/benchmark-starter-prompts.md`
- Review rubric:
  `finding_quality`, `risk_explanation`, `prioritization`, `remediation_practicality`

## Fair-Run Rules

- Use the same prompt text for each agent.
- Use the same codebase context, if any.
- Keep model settings as close as possible.
- Do not give one agent hidden hints the other does not receive.

## Script Workflow

Starter run:

```bash
python3 skills/review-code-smells/scripts/init_benchmark.py \
  --prompt-file skills/review-code-smells/references/benchmark-starter-prompts.md \
  --agents codex claude \
  --output /tmp/smells-benchmark-starter.csv \
  --run-label smells-starter
```

Full run:

```bash
python3 skills/review-code-smells/scripts/init_benchmark.py \
  --agents codex claude \
  --output /tmp/smells-benchmark-results.csv
```

After scoring the CSV manually, summarize it with:

```bash
python3 skills/review-code-smells/scripts/summarize_benchmark.py \
  /tmp/smells-benchmark-results.csv
```
