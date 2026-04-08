# Benchmark Harness

Use this file when you want to compare how different agents behave with this skill package, especially Codex versus Claude Code.

## Goal

Measure whether the agent:

- starts from the problem before naming a pattern
- prefers the simplest sufficient design
- explains readability and architectural boundaries clearly
- names trade-offs instead of recommending patterns dogmatically
- proposes incremental next steps

## Inputs

- Prompt set: `references/eval-prompts.md`
- Scoring rubric: `references/evaluation-rubric.md`
- Optional examples for judge calibration: `references/before-after-examples.md`

## Fair-Run Rules

- Use the same prompt text for each agent.
- Use the same codebase context, if any.
- Keep model temperature and reasoning mode as close as possible.
- Do not give one agent extra hidden hints that the other does not receive.
- If comparing with project memory enabled, ensure both agents have their intended local configuration active.

## Recommended Workflow

1. Generate a blank score sheet from the prompt pack.
2. Run each prompt once per agent and save the raw response separately.
3. Score each response from 0 to 2 on all rubric dimensions.
4. Summarize the sheet to compare averages, category performance, and weak spots.

## Suggested Output Storage

- Raw responses:
  `tmp/benchmark-outputs/<agent>/prompt-<id>.md`
- Score sheet:
  `tmp/benchmark-results.csv`

## Script Workflow

Initialize a score sheet for Codex and Claude:

```bash
python3 skills/apply-software-patterns/scripts/init_benchmark.py \
  --agents codex claude \
  --output /tmp/benchmark-results.csv
```

For a faster first-pass run, use the starter pack:

```bash
python3 skills/apply-software-patterns/scripts/init_benchmark.py \
  --prompt-file skills/apply-software-patterns/references/benchmark-starter-prompts.md \
  --agents codex claude \
  --output /tmp/pattern-benchmark-starter.csv \
  --run-label starter
```

Then score the CSV manually by filling these columns:

- `problem_diagnosis`
- `simplicity_bias`
- `readability_impact`
- `architectural_reasoning`
- `tradeoff_awareness`
- `incremental_actionability`
- `notes`

Summarize the results:

```bash
python3 skills/apply-software-patterns/scripts/summarize_benchmark.py /tmp/benchmark-results.csv
```

## Interpreting Results

- Compare per-agent average score.
- Compare category averages to find where one agent is weaker.
- Review low-scoring prompts to see whether the failure is:
  pattern cargo cult,
  weak trade-off reasoning,
  poor readability guidance,
  or over-architecting.

## Good Benchmark Questions

- Does the agent reject patterns often enough when they are not justified?
- Does it suggest architecture escalation only when constraints warrant it?
- Does generated code remain readable to humans who do not know the pattern name?
- Does language-specific guidance improve implementation realism?

## Suggested Rollout

1. Run `benchmark-starter-prompts.md` first.
2. Fix obvious weaknesses in the skill.
3. Run the full `eval-prompts.md` pack for broader confidence.
