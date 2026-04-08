# Agent Skills

This repository contains agent skills in a layout compatible with repositories such as [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills) and tools such as [`skills.sh`](https://skills.sh/).

## Available Skills

### apply-software-patterns

Choose, reject, explain, review, and incrementally apply software design patterns and architecture patterns with strong attention to readability, maintainability, testability, explicit dependencies, and overengineering risk.

Path:

- `skills/apply-software-patterns`

## Repository Layout

```text
skills/
  apply-software-patterns/
    SKILL.md
    agents/
    references/
    scripts/
CLAUDE.md
AGENTS.md
```

## Using With skills.sh

Install from the repository:

```bash
npx skills add https://github.com/<owner>/<repo> --skill apply-software-patterns
```

Or install from a local checkout:

```bash
npx skills add . --skill apply-software-patterns
```
