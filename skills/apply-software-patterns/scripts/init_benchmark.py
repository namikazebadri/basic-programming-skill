#!/usr/bin/env python3
"""Create a benchmark score sheet from a prompt-pack markdown file."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


PROMPT_LINE_RE = re.compile(r"^(\d+)\.\s+(.*)$")


def parse_eval_prompts(path: Path) -> list[dict[str, str]]:
    prompts: list[dict[str, str]] = []
    category = ""

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            category = line[3:].strip()
            continue

        match = PROMPT_LINE_RE.match(line)
        if match:
            prompts.append(
                {
                    "prompt_id": match.group(1),
                    "category": category or "Uncategorized",
                    "prompt": match.group(2).strip(),
                }
            )

    if not prompts:
        raise ValueError(f"No prompts found in {path}")

    return prompts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--eval-prompts",
        default="skills/apply-software-patterns/references/eval-prompts.md",
        help="Deprecated alias for --prompt-file",
    )
    parser.add_argument(
        "--prompt-file",
        default="",
        help="Path to the benchmark prompt markdown file",
    )
    parser.add_argument(
        "--agents",
        nargs="+",
        required=True,
        help="Agent labels to include, for example: codex claude",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output CSV path",
    )
    parser.add_argument(
        "--run-label",
        default="baseline",
        help="Label for this benchmark run",
    )
    args = parser.parse_args()

    prompt_file = args.prompt_file or args.eval_prompts
    prompts = parse_eval_prompts(Path(prompt_file))
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "run_label",
        "agent",
        "prompt_id",
        "category",
        "prompt",
        "problem_diagnosis",
        "simplicity_bias",
        "readability_impact",
        "architectural_reasoning",
        "tradeoff_awareness",
        "incremental_actionability",
        "total",
        "verdict",
        "notes",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()

        for agent in args.agents:
            for prompt in prompts:
                writer.writerow(
                    {
                        "run_label": args.run_label,
                        "agent": agent,
                        "prompt_id": prompt["prompt_id"],
                        "category": prompt["category"],
                        "prompt": prompt["prompt"],
                        "problem_diagnosis": "",
                        "simplicity_bias": "",
                        "readability_impact": "",
                        "architectural_reasoning": "",
                        "tradeoff_awareness": "",
                        "incremental_actionability": "",
                        "total": "",
                        "verdict": "",
                        "notes": "",
                    }
                )

    print(
        f"Wrote {len(prompts) * len(args.agents)} rows to {output_path} "
        f"from {prompt_file}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
