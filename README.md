# 🌍 全球冲突情报监控

**Global Conflict Intelligence Monitor**

---

## 📊 能力说明

这是一个**全自动全球冲突监控系统**，每 3 小时自动扫描四大战场，生成专业情报报告。

---

## 🎯 核心功能

### 1. 四战场实时监控
| 战区 | 监控内容 |
|------|----------|
| **⚔️ 中东** | 伊朗 - 以色列冲突、真主党动态、美军基地 |
| **🇪🇺 欧洲** | 俄乌战争、前线变化、基础设施打击 |
| **🌏 亚洲** | 台海/南海局势、缅甸内战 |
| **🌎 美洲** | 墨西哥卡特尔、厄瓜多尔帮派、海地帮派 |

### 2. 风险量化评估
- **整体风险指数** (1-10 分)
- **各战区风险等级** (高/中/低)
- **置信度评分** (Admiralty Code 标准)

### 3. 金融市场影响
- 油价/黄金/股市波动预测
- 风险量化指标（波动率 + 突破概率）
- 投资建议（中国/新加坡视角）

### 4. 卫星与实时地图
- LiveUAMap 实时标注
- ISW 专业分析图
- ACLED 冲突数据库

---

## ⏰ 更新频率

**北京时间：**
- **08:00-23:00**：每 3 小时（08:00, 11:00, 14:00, 17:00, 20:00, 23:00）
- **01:00-08:00**：仅 01:00 一次

**每日 7 次自动更新**

---

## 🛠️ 技术架构

| 组件 | 技术 |
|------|------|
| **数据源** | Tavily API + OSINT 账号 + 专业仪表盘 |
| **验证** | 3 层交叉验证（Tier S/A/B 来源分级） |
| **置信度** | v3 公式评分（≥70 才推送） |
| **发布** | GitHub Pages 自动部署 |
| **自检** | 5 轮自动修复机制 |

---

## 📁 报告结构

```
reports/
├── global-conflict-YYYYMMDD_HHMM.html  # 各次报告
└── latest.html                          # 最新报告（始终指向最新）
```

---

## 🔗 访问地址

- **GitHub Repo:** https://github.com/mckayhou/global-conflict-monitor
- **GitHub Pages:** https://mckayhou.github.io/global-conflict-monitor/

---

## 📌 数据来源

- **新闻:** Reuters, BBC, Al Jazeera, Haaretz
- **OSINT:** @sentdefender, @OSINTWarfare, @WarMonitors
- **专业:** ISW (understandingwar.org), LiveUAMap, ACLED, InSight Crime

---

## ⚠️ 免责声明

- 所有数据来自公开来源（OSINT）
- 风险指数仅供参考，不构成投资建议
- 报告自动生成，可能存在延迟或误差

---

**最后更新:** 2026-03-04  
**维护者:** @mckayhou  
**版本:** v21
