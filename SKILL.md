---
name: get-more-perspectives-skill
description: >-
  Assemble a virtual advisory board of diverse expert personas (Operator,
  Skeptic, Visionary, Customer Advocate, Quant) to stress-test decisions,
  uncover hidden blindspots, and synthesize actionable next steps. Triggers
  when users face tough choices, ask "what would experts think", hesitate
  between options, seek pre-mortem risk audits, or need multi-angle trade-off
  analysis across career, tech architecture, pricing, and startup decisions.
license: MIT
activation: /get-more-perspectives
metadata:
  author: 文森策
  version: 1.1.0
  created: 2026-08-16
  last_reviewed: 2026-08-26
  review_interval_days: 90
provenance:
  maintainer: 文森策
  version: 1.1.0
  created: 2026-08-16
  source_references:
    - https://github.com/FrancyJGLisboa/agent-skill-creator
    - https://agentskills.io
compatibility: >-
  Works on all platforms supporting the Agent Skills Open Standard (SKILL.md):
  Claude Code, Codex CLI, Antigravity, Gemini CLI, Cursor, Windsurf, Cline,
  Roo Code, Goose, and Copilot CLI.
---

# /get-more-perspectives-skill — 虚拟顾问团多视角决策洞察

人在做重大决定时，最容易犯两个错误：要么是一个人闷头想，陷入单一维度的思维盲区；要么是身边朋友一团和气，谁都不好意思泼冷水。

这个技能的作用，就是在你做出关键决策前，**拉起一个由 3-5 位虚拟专家组成的专属顾问团**。从执行落地、风险挑刺、长期远见、用户感知和财务算账 5 个角度独立审视方案，帮你提前把坑排完、把潜在机会找全，最终交付一份带有可验证实验与止损红线的综合行动方案。

---

## 🎯 触发机制与常见场景

当用户输入 `/get-more-perspectives` 或在对话中表达以下决策困境时激活：

- **二选一或多选一纠结**：“在选项 A 和 B 之间犹豫不决”、“收到两份 Offer 不知道怎么选”
- **重大方向审视**：“该不该把现有单体架构拆成微服务”、“这个 SaaS 产品的免费版要不要取消”
- **寻求多角度挑刺**：“从不同专业角度帮我看看这个方案”、“如果专家来看会挑出什么毛病”、“做个事前失败推演 (Pre-Mortem)”
- **商业与转型评估**：“这个新业务靠不靠谱”、“产品该怎么定价”、“这个创业方向有没有坑”

```bash
# 常见调用示例
/get-more-perspectives 收到两份 Offer：外企架构师 vs AI 初创团队早期成员
/get-more-perspectives 是否应该将现有 SaaS 产品的免费版全面取消？
/get-more-perspectives --domain tech 是否应该将单体后端架构拆分为微服务？
/get-more-perspectives --advisors operator,skeptic,visionary,quant 评估新季度商业化方案
```

---

## 🏛️ 顾问团核心阵容 (Core Advisory Board)

默认由 5 位立场鲜明的专家组成，覆盖决策最核心的五个维度：

| 顾问角色 | 核心视角与代表声音 | 经典口头禅 / 必问问题 |
| :--- | :--- | :--- |
| ⚙️ **执行者 (The Operator)** | 聚焦落地可行性、团队带宽、排期摩擦与第一步动作 | *“想法很美好，但到底谁来干？第一周干什么？最容易卡在哪里？”* |
| 🛡️ **质疑者 (The Skeptic)** | 专职挑刺与事前排雷，死磕隐性假设与最坏情况 | *“假设 6 个月后项目在落地中彻底搞砸了，复盘报告上写的最主要踩坑原因会是什么？”* |
| 🔭 **远见者 (The Visionary)** | 关注 3-5 年长期复利、非对称上行机会与技术趋势 | *“这步棋是在通往长远壁垒的必经之路上吗？不做会不会错失更大浪潮？”* |
| 👤 **客户代言人 (The Customer Voice)** | 捍卫真实用户体验，区分是用户真痛点还是自己脑补 | *“用户真的愿意为这个掏钱或改变习惯吗？还是我们在自嗨？”* |
| 📊 **财务专家 (The Quant)** | 算细账，死磕投入产出比 (ROI)、现金流与机会成本 | *“把隐性人力全算进去到底赚不赚钱？同样的资源投在别处会不会收益更高？”* |

> 💡 **针对特定领域的扩展席位**：
> 如需更垂直的审视，可按需替换或引入：**技术架构师 (`tech_architect`)**、**合规与法务顾问 (`legal_ethicist`)**、**极简主义者 (`simplifier`)**、**组织文化顾问 (`talent_culture`)**。
> 详细角色定义与思维模型见 `references/advisor-personas.md`。

---

## 🔄 标准执行 5 步流程 (Standard 5-Step Workflow)

### 步骤 1：拆解议题与判断决策属性
- 提炼核心问题与硬性约束（时间、预算、团队能力）。
- 判断决策属性：
  - **单向门决策 (Type 1 不可逆)**：代价极大，一旦做出很难回头 ➡️ 必须由【质疑者】和【财务专家】深度排雷。
  - **双向门决策 (Type 2 可逆)**：试错成本低，随时可撤回 ➡️ 重点看【执行者】与【远见者】，推动快速小步实验。
- 决策分流与方法论详见 `references/synthesis-frameworks.md`。

### 步骤 2：组建定制化顾问团
- 根据决策主题，自动从角色库挑选 3-5 位最对口的专家（可调用职场、技术、定价、创业等预设配方）。
- 场景配方详见 `references/domain-recipes.md`。

### 步骤 3：各顾问独立发表意见 (Round 1)
- 顾问之间保持**完全独立**，严禁在第一轮互相妥协或说场面话。
- 每位顾问必须给出：
  1. 明确的立场倾向（赞成 / 反对 / 有条件支持）；
  2. 2-3 条扎实的判断依据；
  3. 1 个最担心的致命风险或潜在机会；
  4. 1 个必须反问决策者的犀利问题。

### 步骤 4：梳理分歧与提炼张力矩阵 (Round 2)
- 找出顾问团的**高度共识点**（大家都认可的事实与基础前提）。
- 绘制**观点张力矩阵**：将表面争论提炼为本质权衡（如“快速见效 vs 长期架构”、“极致体验 vs 商业变现”）。
- 照亮被决策者忽略的**隐形盲区**。

### 步骤 5：综合行动建议与止损红线
- 给出明确的综合决策倾向建议（拒绝模棱两可的和稀泥）。
- 制定 **72 小时内即可启动的低成本验证实验**（用最小代价获取真实反馈）。
- 设立不可逾越的**止损红线与回滚条件 (Kill Criteria)**（写清楚“出现什么情况就坚决撤退”）。

---

## 🛠️ CLI 辅助工具与命令行

本技能内置零依赖的 Python CLI 脚本，可快速生成分析报告或跑自动化测试：

```bash
# 1. 查看所有可用顾问角色
python3 scripts/consult_perspectives.py --list-advisors

# 2. 针对特定主题生成多视角分析报告
python3 scripts/consult_perspectives.py --topic "是否应该辞职全职做独立开发？"

# 3. 指定领域配方与输出文件
python3 scripts/consult_perspectives.py --domain tech --topic "将单体应用重构为微服务" --output report.md

# 4. 执行自动化回归测试
python3 scripts/run_evals.py
```

---

## 💡 实战避坑指南 (Gotchas)

1. **拒绝一团和气的和稀泥**：第一轮发言必须保持各专家的犀利本色。质疑者就要敢于泼冷水，远见者就要敢于想大的，千万不要一上来就搞中庸折中。
2. **单向门与双向门区别对待**：
   - 遇到双向门（可逆）决策，不要在会议室里反复纠结，直接推进 72 小时小步实验，让真实结果说话；
   - 遇到单向门（不可逆）决策，必须强制做事前失败推演 (Pre-Mortem 逆向排雷)，把最坏情况想透。
3. **必须提前写好止损红线 (Kill Criteria)**：决策当天必须定好“什么情况下果断放弃”。一旦真正陷入泥潭，人就会被沉没成本绑架，再也做不出理性的撤退决定。
4. **警惕自嗨型虚荣指标**：财务与用户顾问必须死磕真实留存与现金流，剔除表面光鲜但对业务没有实质帮助的虚荣数据。
5. **Python 3.8+ 标准库零依赖**：所有配套脚本均基于 Python 标准库编写，无需额外 `pip install`，可在任何环境即开即用。

---

## 📚 延伸参考文档 (References)

- `references/advisor-personas.md`：10+ 位专家的详细人设画像、思考视角与提问清单。
- `references/synthesis-frameworks.md`：单向门/双向门分类、张力权衡矩阵、事前失败推演 (Pre-Mortem) 与止损红线设计指南。
- `references/domain-recipes.md`：职场跃迁、技术重构、产品定价、创业转型等实战决策配方。
