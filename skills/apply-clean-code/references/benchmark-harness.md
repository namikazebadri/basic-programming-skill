# Benchmark Harness

Use this file when you want to compare how different agents behave with `apply-clean-code`, especially Codex versus Claude Code.

## Goal

Measure whether the agent:

- identifies reader pain before suggesting cleanup
- prefers the smallest effective refactor
- improves naming, flow, and responsibility boundaries
- avoids over-refactoring and style theater
- proposes incremental and test-aware cleanup

## Inputs

- Prompt set: `references/eval-prompts.md`
- Starter prompt set: `references/benchmark-starter-prompts.md`
- Review rubric:
  `problem_diagnosis`, `simplicity_bias`, `readability_impact`, `tradeoff_awareness`, `incremental_actionability`, `test_awareness`
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

## Suggested Output Storage

- Raw responses:
  `tmp/benchmark-outputs/<agent>/prompt-<id>.md`
- Score sheet:
  `tmp/clean-code-benchmark-results.csv`

## Script Workflow

Starter run:

```bash
python3 skills/apply-clean-code/scripts/init_benchmark.py \
  --prompt-file skills/apply-clean-code/references/benchmark-starter-prompts.md \
  --agents codex claude \
  --output /tmp/clean-code-benchmark-starter.csv \
  --run-label clean-code-starter
```

Full run:

```bash
python3 skills/apply-clean-code/scripts/init_benchmark.py \
  --agents codex claude \
  --output /tmp/clean-code-benchmark-results.csv
```

Then score the CSV manually by filling these columns:

- `problem_diagnosis`
- `simplicity_bias`
- `readability_impact`
- `tradeoff_awareness`
- `incremental_actionability`
- `test_awareness`
- `notes`

Summarize the results:

```bash
python3 skills/apply-clean-code/scripts/summarize_benchmark.py \
  /tmp/clean-code-benchmark-results.csv
```

## Interpreting Results

- Compare per-agent average score.
- Compare category averages to find where one agent is weaker.
- Review low-scoring prompts to see whether the failure is:
  weak naming judgment,
  over-splitting,
  comment dependence,
  weak refactor restraint,
  or missing test awareness.

## Suggested Rollout

1. Run `benchmark-starter-prompts.md` first.
2. Fix obvious weaknesses in the skill.
3. Run the full `eval-prompts.md` pack for broader confidence.
