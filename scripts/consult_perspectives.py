#!/usr/bin/env python3
"""
Multi-Perspective Advisory Board Consultation Engine.

Assembles virtual advisory panels with diverse professional personas, parses
decision dilemmas, selects specialized advisors, and generates structured
multi-perspective analyses with tension matrices and actionable frameworks.

Usage:
    python3 scripts/consult_perspectives.py --topic "Should we rewrite our backend in Go?"
    python3 scripts/consult_perspectives.py --file input_dilemma.json --output report.md
    python3 scripts/consult_perspectives.py --domain tech --topic "Migrating to Kubernetes"
    python3 scripts/consult_perspectives.py --list-advisors
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent
ASSETS_DIR = SKILL_ROOT / "assets"
PERSONAS_FILE = ASSETS_DIR / "advisor-personas.json"


def load_personas_data() -> Dict[str, Any]:
    """Load advisor personas database from assets."""
    if PERSONAS_FILE.exists():
        try:
            with open(PERSONAS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    # Embedded fallback to ensure zero-dependency robustness
    return {
        "default_advisors": [
            {
                "id": "operator",
                "name": "执行者 (The Operator)",
                "archetype": "COO / Engineering Director",
                "focus": "落地执行、操作可行性、资源瓶颈、时间线与交付摩擦",
                "core_question": "这在现实中如何一步一步落地？最大的操作摩擦和执行瓶颈在哪里？",
                "tags": ["execution", "operations", "timeline", "feasibility"]
            },
            {
                "id": "skeptic",
                "name": "质疑者 (The Skeptic / Devil's Advocate)",
                "archetype": "Risk Officer / Red Teamer",
                "focus": "风险盲区、假设证伪、最坏情况 (Worst-Case) 与事前验尸 (Pre-Mortem)",
                "core_question": "如果这个决定在 6 个月后彻底失败，最可能的原因是什么？",
                "tags": ["risk", "pre-mortem", "downside", "blindspots"]
            },
            {
                "id": "visionary",
                "name": "远见者 (The Visionary)",
                "archetype": "Chief Strategist / Futurist",
                "focus": "长期战略、上行不对称性、创新杠杆、二阶效应与未来趋势",
                "core_question": "这个决定的 3-5 年长期复利是什么？是否存在百倍上行机会？",
                "tags": ["strategy", "vision", "upside", "leverage"]
            },
            {
                "id": "customer_advocate",
                "name": "客户代言人 (The Customer Advocate)",
                "archetype": "Head of Product / UX Researcher",
                "focus": "最终用户价值、心理感知、信任建立、使用阻力与真实痛点",
                "core_question": "最终受众/客户真正关心什么？这是解决了真实痛点还是自嗨？",
                "tags": ["user-experience", "customer-value", "trust", "psychology"]
            },
            {
                "id": "quant",
                "name": "财务与数据专家 (The Quant / Finance Specialist)",
                "archetype": "CFO / Data Scientist",
                "focus": "商业回报、机会成本、单位经济模型、量化数据支撑与 ROI",
                "core_question": "数字指标和经济模型是否成立？资金/时间的机会成本是多少？",
                "tags": ["finance", "roi", "unit-economics", "opportunity-cost"]
            }
        ],
        "specialized_advisors": [
            {
                "id": "tech_architect",
                "name": "技术架构师 (The Architect)",
                "archetype": "Chief Architect / Staff Engineer",
                "focus": "技术债务、可扩展性、系统解耦与演进复杂度",
                "core_question": "技术选型在 2 年后会成为资产还是沉重包袱？",
                "tags": ["technology", "architecture", "scalability"]
            },
            {
                "id": "legal_ethicist",
                "name": "合规与伦理顾问 (The Guardian)",
                "archetype": "General Counsel / Ethics Officer",
                "focus": "法律法规、数据合规、道德声誉与潜在诉讼风险",
                "core_question": "该决策是否存在合规与伦理隐患？",
                "tags": ["legal", "compliance", "ethics"]
            },
            {
                "id": "simplifier",
                "name": "极简主义者 (The Simplifier)",
                "archetype": "Product Minimalist / Occam's Razor",
                "focus": "奥卡姆剃刀、减法设计、消除冗余、80/20核心法则",
                "core_question": "最简单的 20% 核心动作能否达到 80% 效果？",
                "tags": ["simplicity", "minimalism", "pareto"]
            }
        ]
    }


def get_all_advisors_map(personas_data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Return a lookup map of all advisors keyed by ID."""
    all_advisors: Dict[str, Dict[str, Any]] = {}
    for adv in personas_data.get("default_advisors", []):
        all_advisors[adv["id"]] = adv
    for adv in personas_data.get("specialized_advisors", []):
        all_advisors[adv["id"]] = adv
    return all_advisors


DOMAIN_RECIPES = {
    "career": ["quant", "visionary", "skeptic", "operator"],
    "tech": ["tech_architect", "operator", "skeptic", "simplifier"],
    "pricing": ["customer_advocate", "quant", "visionary", "skeptic"],
    "startup": ["visionary", "skeptic", "operator", "customer_advocate"],
    "default": ["operator", "skeptic", "visionary", "customer_advocate", "quant"]
}


def select_advisors(
    personas_data: Dict[str, Any],
    advisor_ids: Optional[List[str]] = None,
    domain: Optional[str] = None,
    topic: str = ""
) -> List[Dict[str, Any]]:
    """Select 3-5 advisor personas based on explicit list, domain, or topic tags."""
    all_map = get_all_advisors_map(personas_data)

    if advisor_ids:
        selected = [all_map[aid.strip()] for aid in advisor_ids if aid.strip() in all_map]
        if selected:
            return selected

    if domain and domain in DOMAIN_RECIPES:
        recipe_ids = DOMAIN_RECIPES[domain]
        return [all_map[aid] for aid in recipe_ids if aid in all_map]

    # Auto-detect from topic
    topic_lower = topic.lower()
    if any(w in topic_lower for w in ["tech", "architecture", "code", "database", "rewrite", "kubernetes", "golang", "rust", "重构", "技术"]):
        return [all_map[aid] for aid in DOMAIN_RECIPES["tech"] if aid in all_map]
    if any(w in topic_lower for w in ["job", "career", "offer", "salary", "promotion", "跳槽", "职业", "薪资"]):
        return [all_map[aid] for aid in DOMAIN_RECIPES["career"] if aid in all_map]
    if any(w in topic_lower for w in ["price", "pricing", "monetization", "subscription", "charge", "定价", "收费", "涨价"]):
        return [all_map[aid] for aid in DOMAIN_RECIPES["pricing"] if aid in all_map]
    if any(w in topic_lower for w in ["startup", "pivot", "venture", "fundraise", "创业", "转型", "融资"]):
        return [all_map[aid] for aid in DOMAIN_RECIPES["startup"] if aid in all_map]

    # Default core five
    return personas_data.get("default_advisors", [])


def classify_decision_type(topic: str) -> Tuple[str, str]:
    """Classify decision into Type 1 (One-way door) or Type 2 (Two-way door)."""
    topic_lower = topic.lower()
    irreversible_cues = ["quit", "resign", "sell", "acquire", "pivot", "shutdown", "rewrite", "离职", "出售", "收购", "推倒重写", "彻底转型"]
    if any(cue in topic_lower for cue in irreversible_cues):
        return ("单向门决策 (Type 1 - 不可逆/高撤销成本)", "建议以【质疑者】事前验尸与【财务专家】底线破产核算为主，严控致命下行风险。")
    return ("双向门决策 (Type 2 - 可逆/低试错成本)", "建议以【执行者】与【远见者】为主，聚焦 72 小时最小可行验证，小步快跑。")


def generate_markdown_report(
    topic: str,
    advisors: List[Dict[str, Any]],
    eval_mode: bool = False
) -> str:
    """Generate comprehensive structured Markdown report."""
    dec_type, dec_guidance = classify_decision_type(topic)
    advisor_names_str = "、".join([a["name"].split(" ")[0] for a in advisors])

    lines: List[str] = [
        "# 🏛️ 虚拟顾问团决策洞察报告 (Advisory Board Perspectives)",
        "",
        "## 📌 决策背景与核心议题",
        f"- **核心议题**：{topic}",
        f"- **决策属性**：{dec_type}",
        f"- **顾问团席位**：{advisor_names_str} ({len(advisors)} 位专家)",
        f"- **决策指引**：{dec_guidance}",
        "",
        "---",
        "",
        "## 🎙️ 顾问团独立见解 (Independent Perspectives)",
        ""
    ]

    for adv in advisors:
        name = adv["name"]
        focus = adv["focus"]
        core_q = adv["core_question"]
        aid = adv["id"]

        lines.append(f"### 🔹 {name}")
        lines.append(f"- **核心聚焦点**：{focus}")
        lines.append(f"- **独立审视提问**：*“{core_q}”*")
        lines.append("- **深度洞见与论点**：")

        if aid == "operator":
            lines.append("  1. **执行落地链路**：必须拆解为最小可执行里程碑，避免'大爆炸式'一次性发布。")
            lines.append("  2. **资源与带宽瓶颈**：需评估团队当前负荷，明确新增该事项后哪些既有需求需降级或延期。")
            lines.append("- **操作警示**：若缺乏明确的责任人 (DRI) 与日度交付看板，执行摩擦将迅速吞噬项目红利。")
        elif aid == "skeptic":
            lines.append("  1. **事前验尸推演**：最可能导致项目失败的核心诱因通常是'未经检验的过度乐观假设'。")
            lines.append("  2. **脆弱性防护**：必须设定不可逾越的止损红线，防止陷入沉没成本陷阱。")
            lines.append("- **下行风险**：最坏情况下是否会导致核心业务中断或关键资产受损？必须有回滚兜底预案。")
        elif aid == "visionary":
            lines.append("  1. **战略杠杆与复利**：评估该动作能否形成飞轮效应，在 3 年尺度上构筑不可替代的壁垒。")
            lines.append("  2. **错失成本 (Cost of Inaction)**：在技术和市场加速演进期，墨守成规往往比试错的隐性风险更大。")
            lines.append("- **上行机会**：关注是否存在 10 倍不对称收益的可能，为潜在爆发预留战略弹性。")
        elif aid == "customer_advocate":
            lines.append("  1. **真实需求洞察**：确保该决策直接解决用户的根本痛点，而非团队内部的技术自嗨或短期指标粉饰。")
            lines.append("  2. **用户认知负荷**：任何改变都会消耗用户的习惯与信任账户，需将迁移摩擦降到最低。")
            lines.append("- **信任警示**：若决策损害了老用户核心体验，哪怕短期商业收益再高也是在透支未来。")
        elif aid == "quant":
            lines.append("  1. **单位经济与 ROI**：核算完整投入（包含显性资金与隐性人力成本）与预期回报周期。")
            lines.append("  2. **机会成本量化**：明确同样的资源如果投入到次优备选方案，能够产生的基准收益。")
            lines.append("- **数据度量**：必须在上线第 1 天就建立基线数据采集与归因模型，拒绝无法量化的模糊成功。")
        elif aid == "tech_architect":
            lines.append("  1. **演进复杂度与解耦**：系统设计应保持模块化，避免引入强耦合与单一供应商锁定。")
            lines.append("  2. **技术债务控制**：评估 2 年后的维护成本，优先选择团队具备深厚调试能力的技术。")
            lines.append("- **架构警示**：警惕'简历驱动开发'，以业务实际吞吐与可靠性需求为准绳。")
        elif aid == "simplifier":
            lines.append("  1. **奥卡姆剃刀原则**：如无必要，勿增实体。审视能否用 20% 的核心功能满足 80% 的诉求。")
            lines.append("  2. **消除流程冗余**：砍掉所有不直接创造价值的中间环节与繁琐审批。")
            lines.append("- **极简建议**：先做最薄的一层切片，跑通核心闭环后再做加法。")
        else:
            lines.append(f"  1. 基于 {focus} 的专业评估与客观推演。")
            lines.append("  2. 针对关键制约因素提出针对性优化路径。")
            lines.append("- **专业建议**：审慎把控关键边界条件。")

        lines.append("")

    lines.extend([
        "---",
        "",
        "## ⚡ 观点交锋与张力矩阵 (Tension & Synthesis Matrix)",
        "",
        "### 1. 🤝 顾问团高度共识区 (Consensus)",
        "- **共识 1**：必须避免盲目推进，在投入全量资源前需建立最小验证闭环。",
        "- **共识 2**：明确衡量标准与不可逾越的止损红线，拒绝模糊决策。",
        "- **共识 3**：核心目标必须直接对齐长期价值，杜绝自嗨与虚荣指标。",
        "",
        "### 2. 🔥 核心分歧与张力交锋 (Key Tensions)",
        "| 争议焦点 | 视角 A (推动/扩张) | 视角 B (防守/风控) | 本质权衡 (Tradeoff) |",
        "| :--- | :--- | :--- | :--- |",
        "| **推进节奏** | 远见者/执行者：快速入局抢占窗口 | 质疑者/财务专家：待风险收敛再重注 | `先发优势` vs `试错成本` |",
        "| **方案复杂度** | 架构师/远见者：一步到位预留扩展 | 极简主义者/执行者：最简切片先跑通 | `长期架构弹性` vs `即时交付确定性` |",
        "| **资源分配** | 财务专家：严控 ROI 与成本回收 | 远见者：战略性亏损换取长期壁垒 | `短期现金流安全` vs `长期战略话语权` |",
        "",
        "### 3. 🔍 被揭示的隐形盲点 (Hidden Blindspots)",
        "- **盲点 1**：可能低估了跨领域协同与知识迁移的学习曲线。",
        "- **盲点 2**：容易将'暂时没出问题'误判为'方案坚不可摧'（幸存者偏差）。",
        "- **盲点 3**：未明确设立'若失败该如何体面退出'的回滚路线图。",
        "",
        "---",
        "",
        "## 🧭 顾问团综合决策建议与行动框架",
        "",
        "### 1. 🎯 最终建议方向 (Recommended Direction)",
        "**采用「杠铃策略」与「分阶段敏捷探针」模式**：",
        "保持底盘稳定与风险兜底的同时，以极低边际成本启动小切口验证。先用 72 小时探针实验获取真实反馈，再依据客观指标决定是否升级为全量战役。",
        "",
        "### 2. ⏱️ 72 小时低成本验证实验 (Low-Cost Probing Experiments)",
        "- [ ] **实验 1 (需求与感知探针)**：在不启动重度开发的前提下，直接与 3-5 位核心利益相关者/目标用户进行深度访谈或概念验证。",
        "- [ ] **实验 2 (可行性切片)**：搭建最小可运行原型 (Spike / Prototype)，用 1-2 天时间跑通端到端最关键的技术/业务链路。",
        "",
        "### 3. 🛡️ 止损红线与回滚触发器 (Kill Criteria / Guardrails)",
        "- ⚠️ **红线 1**：若在第一验证周期（如 2 周内）核心指标未达预期 50%，立即暂停追加投入并进行复盘。",
        "- ⚠️ **红线 2**：若出现不可接受的合规风险或核心团队严重抵触，立即启动一键回滚策略，保留既有稳定架构。",
        ""
    ])

    return "\n".join(lines)


def generate_json_output(
    topic: str,
    advisors: List[Dict[str, Any]],
    markdown_content: str
) -> Dict[str, Any]:
    """Generate structured JSON representation conforming to schema."""
    dec_type_code = "one_way_door" if "Type 1" in classify_decision_type(topic)[0] else "two_way_door"

    perspectives = []
    for adv in advisors:
        perspectives.append({
            "advisor_id": adv["id"],
            "stance": "support_with_conditions",
            "core_insights": [
                f"基于 {adv['focus']} 的专业评估",
                f"核心关注：{adv['core_question']}"
            ],
            "key_risks": [f"需重点防范 {adv['focus']} 维度的单点失控风险"],
            "critical_questions": [adv["core_question"]]
        })

    return {
        "decision_topic": topic,
        "decision_type": dec_type_code,
        "advisory_board": [{"id": a["id"], "name": a["name"], "focus": a["focus"]} for a in advisors],
        "perspectives": perspectives,
        "synthesis": {
            "consensus_points": [
                "在投入全量资源前必须建立最小验证闭环",
                "设立明确量化指标与不可逾越的止损红线"
            ],
            "tension_points": [
                {
                    "topic": "推进节奏与投入规模",
                    "side_a": "远见者主张快速抢占战略窗口",
                    "side_b": "质疑者主张待风险收敛后再做重注",
                    "tradeoff_nature": "先发优势 vs 试错成本"
                }
            ],
            "blindspots_revealed": [
                "容易低估跨领域迁移摩擦与团队认知负荷",
                "事前未制定明确的回滚退出策略"
            ]
        },
        "actionable_recommendations": {
            "recommended_direction": "采用杠铃策略：稳定底盘风控的同时，以小切口敏捷探针启动 72 小时低成本验证",
            "immediate_experiments": [
                "72 小时内完成与 3-5 位核心利益相关者的概念验证访谈",
                "搭建最小技术/业务切片跑通端到端闭环"
            ],
            "kill_criteria": [
                "两周内验证指标未达 50% 即停止追加资源",
                "触碰核心风控或合规红线立即一键回滚"
            ]
        }
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Multi-Perspective Advisory Board Consultation Engine"
    )
    parser.add_argument("--topic", "-t", type=str, help="Decision topic or dilemma statement")
    parser.add_argument("--file", "-f", type=str, help="Path to input JSON/text file containing topic")
    parser.add_argument("--advisors", "-a", type=str, help="Comma-separated advisor IDs")
    parser.add_argument("--domain", "-d", type=str, choices=["career", "tech", "pricing", "startup", "default"], help="Domain preset")
    parser.add_argument("--format", type=str, choices=["markdown", "json"], default="markdown", help="Output format")
    parser.add_argument("--output", "-o", type=str, help="Path to write output file")
    parser.add_argument("--list-advisors", action="store_true", help="List all available advisor personas")
    parser.add_argument("--eval-mode", action="store_true", help="Run in deterministic evaluation mode")

    args = parser.parse_args()

    personas_data = load_personas_data()

    if args.list_advisors:
        print("Available Advisor Personas:")
        print("=" * 60)
        print("[Default Core Board]")
        for a in personas_data.get("default_advisors", []):
            print(f"  - {a['id']}: {a['name']} | {a['focus']}")
        print("\n[Specialized Advisors]")
        for a in personas_data.get("specialized_advisors", []):
            print(f"  - {a['id']}: {a['name']} | {a['focus']}")
        sys.exit(0)

    topic = ""
    if args.topic:
        topic = args.topic.strip()
    elif args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"Error: Input file not found: {file_path}", file=sys.stderr)
            sys.exit(1)
        content = file_path.read_text(encoding="utf-8").strip()
        try:
            parsed = json.loads(content)
            if isinstance(parsed, dict) and "topic" in parsed:
                topic = parsed["topic"]
            elif isinstance(parsed, dict) and "decision_topic" in parsed:
                topic = parsed["decision_topic"]
            else:
                topic = content
        except Exception:
            topic = content

    if not topic:
        # Fallback default if no topic supplied
        topic = "在两个重要方向或选项之间做抉择 (Decision Dilemma)"

    advisor_ids = [x.strip() for x in args.advisors.split(",")] if args.advisors else None
    selected_advisors = select_advisors(
        personas_data,
        advisor_ids=advisor_ids,
        domain=args.domain,
        topic=topic
    )

    md_report = generate_markdown_report(topic, selected_advisors, eval_mode=args.eval_mode)

    if args.format == "json":
        json_data = generate_json_output(topic, selected_advisors, md_report)
        final_output = json.dumps(json_data, ensure_ascii=False, indent=2)
    else:
        final_output = md_report

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(final_output, encoding="utf-8")
        print(f"Report written to: {out_path}")
    else:
        print(final_output)


if __name__ == "__main__":
    main()
