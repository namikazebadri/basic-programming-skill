# Agent Skills Collection

A curated collection of reusable coding-agent skills for design quality, clean code, SOLID reasoning, and maintainability review.

This repository is structured to work well with:

- [`skills.sh`](https://skills.sh/)
- skill-style repositories such as [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills)
- local Codex skill installation
- Claude Code project memory via root routing in [`CLAUDE.md`](./CLAUDE.md) and [`AGENTS.md`](./AGENTS.md)

## What This Repository Provides

- Focused skills with clear boundaries and minimal overlap
- Codex-facing metadata and Claude-facing adapters
- Reference material for progressive loading instead of one giant prompt
- Evaluation assets such as starter benchmarks, prompt packs, and scoring rubrics

## Skill Catalog

| Skill | Primary Use | Best For |
| --- | --- | --- |
| `apply-software-patterns` | Pattern and architecture judgment | Deciding whether a pattern fits, comparing alternatives, improving boundaries, architecture direction |
| `apply-clean-code` | Readability-first refactoring | Naming, function clarity, practical cleanup, reducing incidental complexity |
| `apply-solid-principles` | SOLID-oriented design improvement | SRP, OCP, LSP, ISP, DIP, dependency direction, interface shaping |
| `review-code-smells` | Maintainability and code health review | Technical debt review, smell prioritization, hidden complexity, remediation planning |

## When To Use Which Skill

- Use [`skills/apply-software-patterns/SKILL.md`](./skills/apply-software-patterns/SKILL.md) when the question is about patterns, boundaries, architecture, or overengineering risk.
- Use [`skills/apply-clean-code/SKILL.md`](./skills/apply-clean-code/SKILL.md) when the code works but is difficult to read, follow, or maintain.
- Use [`skills/apply-solid-principles/SKILL.md`](./skills/apply-solid-principles/SKILL.md) when the design pressure is about responsibility fit, extension points, substitution safety, or dependency direction.
- Use [`skills/review-code-smells/SKILL.md`](./skills/review-code-smells/SKILL.md) when the task is to review, prioritize, and explain maintainability smells.

## Installation

### skills.sh

Install a skill from this repository with:

```bash
npx skills add namikazebadri/basic-programming-skill --skill <skill-name>
```

Examples:

```bash
npx skills add namikazebadri/basic-programming-skill
npx skills add namikazebadri/basic-programming-skill --skill apply-software-patterns
npx skills add namikazebadri/basic-programming-skill --skill apply-clean-code
npx skills add namikazebadri/basic-programming-skill --skill apply-solid-principles
npx skills add namikazebadri/basic-programming-skill --skill review-code-smells
```

Install from a local checkout:

```bash
npx skills add . --skill apply-clean-code
```

### Codex

Copy one skill folder into your Codex skills directory:

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R skills/apply-clean-code "$CODEX_HOME/skills/"
```

Repeat for any additional skill you want installed.

Example:

```bash
cp -R skills/apply-software-patterns "$CODEX_HOME/skills/"
cp -R skills/apply-solid-principles "$CODEX_HOME/skills/"
```

### Claude Code

This repository includes a root multi-skill router in:

- [`CLAUDE.md`](./CLAUDE.md)
- [`AGENTS.md`](./AGENTS.md)

Claude Code can use these files to route tasks to the most relevant skill adapter under `skills/<skill-name>/agents/claude.md`.

## Repository

- GitHub: [namikazebadri/basic-programming-skill](https://github.com/namikazebadri/basic-programming-skill)

## Repository Layout

```text
skills/
  apply-clean-code/
    SKILL.md
    agents/
    references/
    scripts/
  apply-solid-principles/
    SKILL.md
    agents/
    references/
    scripts/
  apply-software-patterns/
    SKILL.md
    agents/
    references/
    scripts/
  review-code-smells/
    SKILL.md
    agents/
    references/
    scripts/
CLAUDE.md
AGENTS.md
README.md
```

## Evaluation Support

Several skills in this repository include:

- starter benchmark packs for quick Codex vs Claude comparison
- full eval prompt sets
- evaluation rubrics
- benchmark init and summary scripts

Examples:

- [`skills/apply-software-patterns/references/benchmark-harness.md`](./skills/apply-software-patterns/references/benchmark-harness.md)
- [`skills/apply-clean-code/references/benchmark-harness.md`](./skills/apply-clean-code/references/benchmark-harness.md)
- [`skills/apply-solid-principles/references/benchmark-harness.md`](./skills/apply-solid-principles/references/benchmark-harness.md)
- [`skills/review-code-smells/references/benchmark-harness.md`](./skills/review-code-smells/references/benchmark-harness.md)

## Design Philosophy

These skills are designed to be:

- problem-first instead of buzzword-first
- incremental instead of rewrite-happy
- readability-aware instead of abstraction-heavy
- practical enough for real codebases under delivery pressure

## Notes

- Not every skill should be loaded for every task.
- The root router is intentionally lightweight so Claude can choose relevant skill context instead of loading the entire repository.
- The benchmark assets are intended to help compare agent behavior, not to force one rigid style.
