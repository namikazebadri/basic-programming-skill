#!/usr/bin/env python3
"""Summarize a benchmark CSV created from the code-smells eval prompts."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


SCORE_COLUMNS = [
    "finding_quality",
    "risk_explanation",
    "prioritization",
    "remediation_practicality",
]


def parse_score(value: str) -> int:
    value = value.strip()
    if value == "":
        return 0
    score = int(value)
    if score < 0 or score > 2:
        raise ValueError(f"Score must be between 0 and 2, got {score}")
    return score


def is_scored(row: dict[str, str]) -> bool:
    return any(row[column].strip() != "" for column in SCORE_COLUMNS)


def average(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", help="Benchmark CSV path")
    args = parser.parse_args()

    csv_path = Path(args.csv_path)
    rows = list(csv.DictReader(csv_path.open(encoding="utf-8")))
    if not rows:
        raise ValueError(f"No rows found in {csv_path}")

    by_agent: dict[str, list[int]] = defaultdict(list)
    by_agent_category: dict[tuple[str, str], list[int]] = defaultdict(list)
    low_rows: list[tuple[int, str, str, str]] = []
    unscored_rows = 0

    for row in rows:
        if not is_scored(row):
            unscored_rows += 1
            continue
        total = sum(parse_score(row[column]) for column in SCORE_COLUMNS)
        agent = row["agent"]
        category = row["category"]
        prompt_id = row["prompt_id"]
        prompt = row["prompt"]
        by_agent[agent].append(total)
        by_agent_category[(agent, category)].append(total)
        if total <= 4:
            low_rows.append((total, agent, prompt_id, prompt))

    print(f"Benchmark summary for {csv_path}")
    print(f"Scored rows: {sum(len(scores) for scores in by_agent.values())}")
    print(f"Unscored rows: {unscored_rows}")

    if not by_agent:
        print("")
        print("No scored rows found yet. Fill the rubric columns in the CSV, then rerun the summary.")
        return 0

    print("")
    print("Per-agent averages")
    for agent in sorted(by_agent):
        print(f"- {agent}: avg={average(by_agent[agent]):.2f} prompts={len(by_agent[agent])}")

    print("")
    print("Per-agent category averages")
    for agent, category in sorted(by_agent_category):
        scores = by_agent_category[(agent, category)]
        print(f"- {agent} | {category}: avg={average(scores):.2f} prompts={len(scores)}")

    print("")
    print("Lowest-scoring rows")
    for total, agent, prompt_id, prompt in sorted(low_rows)[:10]:
        print(f"- {agent} prompt {prompt_id}: total={total} | {prompt}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
