# Eval Spec: get-more-perspectives-skill

## Overview
Evaluates the multi-perspective advisory board synthesis capabilities of the `get-more-perspectives-skill`.

## Binary Criteria
- `has-perspectives`: Checks that the output includes independent advisor perspectives.
- `has-tension-matrix`: Checks that the output includes the tension and synthesis matrix.
- `has-kill-criteria`: Checks that the output includes risk guardrails and kill criteria.
- `has-sufficient-depth`: Checks that the output is detailed and non-trivial (>20 lines).

```json
{
  "skill": "get-more-perspectives-skill",
  "run": "python3 scripts/run_pipeline.py --input {input} --output {output}",
  "criteria": [
    {
      "id": "has-perspectives",
      "text": "Output contains independent advisor perspectives",
      "type": "command",
      "cmd": "grep -q '顾问团独立见解' {output}"
    },
    {
      "id": "has-tension-matrix",
      "text": "Output contains tension and synthesis matrix",
      "type": "command",
      "cmd": "grep -q '观点交锋与张力矩阵' {output}"
    },
    {
      "id": "has-kill-criteria",
      "text": "Output defines clear guardrails and kill criteria",
      "type": "command",
      "cmd": "grep -q '止损红线' {output}"
    },
    {
      "id": "has-sufficient-depth",
      "text": "Output contains comprehensive depth with at least 25 lines",
      "type": "command",
      "cmd": "test $(wc -l < {output}) -ge 25"
    }
  ],
  "golden": [
    {
      "id": "case-1",
      "input": "golden/case-1/input.json",
      "expected": "golden/case-1/expected.md",
      "split": "val"
    },
    {
      "id": "case-2",
      "input": "golden/case-2/input.json",
      "expected": null,
      "split": "test",
      "expected_status": "pending-first-green"
    },
    {
      "id": "case-3",
      "input": "golden/case-3/input.json",
      "expected": null,
      "split": "val",
      "expected_status": "pending-first-green"
    }
  ]
}
```
