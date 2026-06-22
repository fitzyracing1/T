#!/usr/bin/env python3
"""Run the Female Transformer Unit agent in local text-reporting mode."""

from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "agents" / "female-transformer-unit.agent.json"


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as manifest_file:
        return json.load(manifest_file)


def select_move(manifest: dict[str, Any], cycle_index: int, requested_move: str | None) -> str:
    commands = manifest["commands"]
    if requested_move:
        if requested_move not in commands:
            available = ", ".join(sorted(commands))
            raise ValueError(f"Unknown move '{requested_move}'. Available moves: {available}")
        return requested_move

    autonomy = manifest.get("autonomy", {})
    sequence = autonomy.get("moveSequence") or [autonomy.get("defaultMove", "dance")]
    move = sequence[cycle_index % len(sequence)]
    if move not in commands:
        return autonomy.get("defaultMove", "dance")
    return move


def format_report(manifest: dict[str, Any], move: str, cycle_number: int) -> str:
    dosing = manifest["dosing"]
    helium = dosing["helium"]
    argon = dosing["argon"]
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    command_meaning = manifest["commands"][move]
    cascade = manifest["communicationCascade"]

    return "\n".join(
        [
            f"[{manifest['id']}] autonomous report",
            f"timestamp: {timestamp}",
            f"cycle: {cycle_number}",
            "status: spawned",
            "acceptance: accepted by autonomous mode",
            f"move: {move}",
            f"move_meaning: {command_meaning}",
            (
                "dosing: "
                f"helium={helium['units']} ({helium['binary']}), "
                f"argon={argon['units']} ({argon['binary']}), "
                f"ratio={dosing['ratio']}"
            ),
            (
                "cascade: visual_text report emitted; "
                f"auditory/physical adapters available in contract={cascade['modalities']}"
            ),
            "report_destination: stdout",
        ]
    )


def run_agent(manifest_path: Path, cycles: int, interval: float, requested_move: str | None) -> None:
    manifest = load_manifest(manifest_path)
    autonomy = manifest.get("autonomy", {})
    if not autonomy.get("enabled", False):
        raise RuntimeError("Autonomous mode is not enabled for this agent.")

    for cycle_index in range(cycles):
        move = select_move(manifest, cycle_index, requested_move)
        print(format_report(manifest, move, cycle_index + 1), flush=True)
        if cycle_index < cycles - 1:
            print("", flush=True)
            time.sleep(interval)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Spawn the Female Transformer Unit agent in autonomous text-reporting mode."
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help="Path to the agent manifest.",
    )
    parser.add_argument(
        "--cycles",
        type=int,
        default=1,
        help="Number of autonomous report cycles to emit.",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=0.0,
        help="Seconds to wait between cycles.",
    )
    parser.add_argument(
        "--move",
        choices=["live", "laugh", "dance"],
        help="Optional move override for this run.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.cycles < 1:
        raise ValueError("--cycles must be at least 1")
    if args.interval < 0:
        raise ValueError("--interval cannot be negative")

    run_agent(args.manifest, args.cycles, args.interval, args.move)


if __name__ == "__main__":
    main()
