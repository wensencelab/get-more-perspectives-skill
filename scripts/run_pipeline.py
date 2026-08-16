#!/usr/bin/env python3
"""
Pipeline Orchestrator for get-more-perspectives-skill.

Connects input dilemma specification to the multi-perspective consultation
engine and writes the synthesized Markdown/JSON advisory board report to the
specified output destination.

Usage:
    python3 scripts/run_pipeline.py --input evals/golden/case-1/input.json --output output.md
    python3 scripts/run_pipeline.py --topic "Should we raise our SaaS prices by 20%?" --output report.md
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Local import from scripts directory
sys.path.insert(0, str(Path(__file__).resolve().parent))
from consult_perspectives import (
    load_personas_data,
    select_advisors,
    generate_markdown_report,
    generate_json_output
)


def run_pipeline(
    input_path: str = "",
    output_path: str = "",
    topic_str: str = "",
    format_type: str = "markdown",
    domain: str = ""
) -> int:
    """Run the multi-perspective consultation pipeline end-to-end."""
    topic = topic_str.strip()

    if input_path:
        p = Path(input_path)
        if not p.exists():
            print(f"[Pipeline Error] Input path not found: {p}", file=sys.stderr)
            return 1
        raw_text = p.read_text(encoding="utf-8").strip()
        if raw_text.startswith("{") and raw_text.endswith("}"):
            import json
            try:
                data = json.loads(raw_text)
                topic = data.get("topic") or data.get("decision_topic") or raw_text
                if not domain and "domain" in data:
                    domain = data["domain"]
            except Exception:
                topic = raw_text
        else:
            topic = raw_text

    if not topic:
        topic = "重大决策方案评估与盲区多视角分析"

    personas_data = load_personas_data()
    selected_advisors = select_advisors(
        personas_data,
        domain=domain if domain else None,
        topic=topic
    )

    md_report = generate_markdown_report(topic, selected_advisors, eval_mode=True)

    if format_type == "json" or (output_path and output_path.endswith(".json")):
        import json
        json_data = generate_json_output(topic, selected_advisors, md_report)
        rendered = json.dumps(json_data, ensure_ascii=False, indent=2)
    else:
        rendered = md_report

    if output_path:
        out_p = Path(output_path)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(rendered, encoding="utf-8")
        print(f"[Pipeline OK] Perspective report written to: {out_p}")
    else:
        print(rendered)

    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Pipeline orchestrator for get-more-perspectives-skill")
    parser.add_argument("--input", "-i", type=str, default="", help="Path to input decision file")
    parser.add_argument("--output", "-o", type=str, default="", help="Path to output destination")
    parser.add_argument("--topic", "-t", type=str, default="", help="Inline topic string")
    parser.add_argument("--domain", "-d", type=str, default="", help="Domain preset")
    parser.add_argument("--format", type=str, choices=["markdown", "json"], default="markdown", help="Output format")

    args = parser.parse_args()

    exit_code = run_pipeline(
        input_path=args.input,
        output_path=args.output,
        topic_str=args.topic,
        format_type=args.format,
        domain=args.domain
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
