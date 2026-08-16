# 🏛️ 虚拟顾问团决策洞察报告 (Advisory Board Perspectives)

## 📌 决策背景与核心议题
- **核心议题**：{{DECISION_TOPIC}}
- **决策属性**：{{DECISION_TYPE}} (单向门不可逆决策 / 双向门可逆实验)
- **顾问团席位**：{{ADVISOR_NAMES}}

---

## 🎙️ 顾问团独立见解 (Independent Perspectives)

{{#EACH_ADVISOR}}
### 🔹 {{ADVISOR_NAME}} — {{ADVISOR_FOCUS}}
- **立场倾向**：{{STANCE}}
- **核心论点与洞见**：
  1. {{INSIGHT_1}}
  2. {{INSIGHT_2}}
- **致命盲区与风险警示**：
  - {{RISK_1}}
- **必须反问决策者的关键问题**：
  - {{QUESTION_1}}
{{/EACH_ADVISOR}}

---

## ⚡ 观点交锋与张力矩阵 (Tension & Synthesis Matrix)

### 1. 🤝 顾问团高度共识区 (Consensus)
- {{CONSENSUS_ITEMS}}

### 2. 🔥 核心分歧与张力交锋 (Key Tensions)
| 争议焦点 | 视角 A 观点 | 视角 B 观点 | 本质权衡 (Tradeoff) |
| :--- | :--- | :--- | :--- |
| {{TENSION_ROW}} |

### 3. 🔍 被揭示的隐形盲点 (Hidden Blindspots)
- {{BLINDSPOTS}}

---

## 🧭 顾问团综合决策建议与行动框架

### 1. 最终建议方向 (Recommended Direction)
{{RECOMMENDED_DIRECTION}}

### 2. 72 小时低成本验证实验 (Low-Cost Probing Experiments)
- [ ] **实验 1**：{{EXPERIMENT_1}}
- [ ] **实验 2**：{{EXPERIMENT_2}}

### 3. 🛡️ 止损红线与回滚触发器 (Kill Criteria / Guardrails)
- ⚠️ **红线条件**：{{KILL_CRITERIA}}
