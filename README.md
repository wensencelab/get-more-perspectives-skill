# 🏛️ get-more-perspectives-skill

> 在做出重大决定之前，召集由 3-5 位虚拟专家组成的顾问团，收集多元视角，揭示隐形盲区，交付高置信度的决策综合行动方案。

---

## 🌟 核心价值

在面临重大决策（跳槽转型、技术架构选型、商业定价、战略重组等）时，个人思考极易陷入单一维度的认知盲区或过度乐观/悲观偏误。

`get-more-perspectives-skill` 模拟由资深专家组成的**虚拟顾问团 (Advisory Board)**：
- **执行者 (The Operator)**：评估落地可行性与操作摩擦
- **质疑者 (The Skeptic)**：进行事前验尸 (Pre-Mortem) 并深挖潜在漏洞
- **远见者 (The Visionary)**：评估长期战略复利与非对称上行机会
- **客户代言人 (The Customer Advocate)**：捍卫最终用户真实感知与信任账户
- **财务专家 (The Quant)**：计算投入产出比、单位经济与机会成本

各顾问独立发表见解，随后通过**张力矩阵 (Tension Matrix)** 提炼本质权衡，输出带有 72 小时探针实验与止损红线的综合行动方案。

---

## 🚀 快速开始与调用方式

### 1. Slash 快捷指令
```bash
# 通用调用
/get-more-perspectives 是否应该将单体后端架构拆分为微服务？

# 指定领域配方 (career, tech, pricing, startup)
/get-more-perspectives --domain career 收到外企架构师与初创团队合伙人两份 Offer 怎么选？

# 指定顾问席位
/get-more-perspectives --advisors operator,skeptic,visionary,quant 评估新产品定价策略
```

### 2. 自然语言触发
- *"在选项 A 与选项 B 之间犹豫不决，帮我多角度分析一下"*
- *"如果由不同维度的专家来评估这个决定，他们会怎么想？"*
- *"帮我找出这个方案的致命盲点并做个事前验尸 (Pre-Mortem)"*

---

## 📦 跨平台安装指南 (Cross-Platform Installation)

### 自动安装 (推荐)
进入技能目录并运行安装脚本：
```bash
./install.sh
```

### 各平台安装路径：
- **Claude Code**:
  ```bash
  /plugin marketplace add path/to/get-more-perspectives-skill
  ```
- **OpenAI Codex CLI / Antigravity / Gemini CLI**:
  已自动安装至 `~/.codex/skills/get-more-perspectives-skill` 或 `~/.agents/skills/get-more-perspectives-skill`
- **Cursor / Windsurf**:
  运行 `./install.sh` 自动生成对应的 `.cursor/rules` / `.windsurfrules` 配置

---

## 🛠️ CLI 命令行工具

本技能内置开箱即用的 Python CLI 工具（Python 3.8+ 零依赖）：

```bash
# 1. 查看所有可用顾问角色库
python3 scripts/consult_perspectives.py --list-advisors

# 2. 对特定决策议题生成多视角分析报告
python3 scripts/consult_perspectives.py --topic "是否应该辞职全职做独立开发？"

# 3. 输出为标准结构化 JSON 格式
python3 scripts/consult_perspectives.py --topic "技术重构方案评估" --format json

# 4. 执行自动化流水线与批处理
python3 scripts/run_pipeline.py --input evals/golden/case-1/input.json --output report.md

# 5. 运行评测基准与回归测试
python3 scripts/run_evals.py --rollout
```

---

## 📂 目录结构

```
get-more-perspectives-skill/
├── SKILL.md                          # 核心技能定义与触发规范 (<500行)
├── AGENTS.md                         # 多工具跨平台通用指令文件
├── README.md                         # 项目使用与安装说明
├── install.sh                        # 跨平台自动检测安装脚本
├── .claude-plugin/                   # Claude 插件元数据 (plugin.json, marketplace.json)
├── scripts/
│   ├── consult_perspectives.py       # 顾问团多视角编排核心引擎
│   ├── run_pipeline.py               # 单入口流水线执行器
│   ├── run_evals.py                  # 自动化评测与黄金测试用例校验器
│   ├── evolve.py                     # 技能自我迭代与反馈捕获工具
│   └── check_pipeline.py             # 流水线完整性校验工具
├── references/
│   ├── advisor-personas.md           # 15+ 专业顾问人设、思维模型与提问库
│   ├── synthesis-frameworks.md       # 单向门/双向门、张力矩阵与事前验尸方法论
│   └── domain-recipes.md             # 职场、技术、定价、创业等领域决策配方
├── assets/
│   ├── advisor-personas.json         # 机器可读的顾问角色数据库
│   ├── perspectives-template.md      # 标准多视角输出 Markdown 模板
│   └── decision-matrix-schema.json   # 决策综合 JSON Schema
└── evals/
    ├── get-more-perspectives-skill.eval.md  # 评测规范文件
    └── golden/                             # 黄金测试用例集
        ├── case-1/
        ├── case-2/
        └── case-3/
```

---

## 🔄 技能进化与学习闭环

如果技能在实际使用中有任何需要修正的视角偏误，可以通过以下命令快速沉淀经验：

```bash
# 记录真实用户修正意见至 EVOLUTION.md 并更新 Gotchas
python3 scripts/evolve.py --correct "在评估早期技术选型时，必须优先考虑核心团队对底层源码的排错能力"
```

---

## 📄 License
MIT
