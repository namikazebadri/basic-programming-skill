# Benchmark Harness

Use this file when you want to compare how different agents behave with `apply-solid-principles`, especially Codex versus Claude Code.

## Goal

Measure whether the agent:

- identifies the real design pressure before naming a principle
- chooses the right SOLID principle, if any
- compares against a simpler refactor
- avoids abstraction theater
- proposes a narrow, reviewable next step

## Inputs

- Prompt set: `references/eval-prompts.md`
- Starter prompt set: `references/benchmark-starter-prompts.md`
- Review rubric:
  `problem_diagnosis`, `simplicity_bias`, `solid_fit`, `tradeoff_awareness`, `incremental_actionability`
- Optional calibration examples: `references/before-after-examples.md`

## Fair-Run Rules

- Use the same prompt text for each agent.
- Use the same codebase context, if any.
- Keep model settings as close as possible.
- Do not give one agent hidden hints the other does not receive.
- If project memory is enabled, ensure both agents have their intended local configuration active.

## Recommended Workflow

1. Generate a blank score sheet from the prompt pack.
2. Run each prompt once per agent and save the raw response separately.
3. Score each response from 0 to 2 on all rubric dimensions.
4. Summarize the sheet to compare averages, category performance, and weak spots.

## Script Workflow

Starter run:

```bash
python3 skills/apply-solid-principles/scripts/init_benchmark.py \
  --prompt-file skills/apply-solid-principles/references/benchmark-starter-prompts.md \
  --agents codex claude \
  --output /tmp/solid-benchmark-starter.csv \
  --run-label solid-starter
```

Full run:

```bash
python3 skills/apply-solid-principles/scripts/init_benchmark.py \
  --agents codex claude \
  --output /tmp/solid-benchmark-results.csv
```

After scoring the CSV manually, summarize it with:

```bash
python3 skills/apply-solid-principles/scripts/summarize_benchmark.py \
  /tmp/solid-benchmark-results.csv
```

## Suggested Rollout

1. Run `benchmark-starter-prompts.md` first.
2. Fix obvious weaknesses in the skill.
3. Run the full `eval-prompts.md` pack for broader confidence.
