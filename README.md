# 🌍 全球冲突情报监控

**Global Conflict Intelligence Monitor**

---

## 🌐 访问报告（重要）

> **⚠️ 请访问 GitHub Pages 查看报告，而非此代码仓库！**

| 页面 | 链接 |
|------|------|
| **📊 报告首页** | 👉 https://mckayhou.github.io/global-conflict-monitor/ |
| 📋 完整报告列表 | https://mckayhou.github.io/global-conflict-monitor/REPORTS.md |
| 📖 能力说明 | https://mckayhou.github.io/global-conflict-monitor/README.md |

---

## 📋 项目简介

这是一个**全自动全球冲突监控系统**，每 3 小时自动扫描四大战场，生成专业情报报告。

**监控范围：**
- ⚔️ 中东战场（以色列 - 哈马斯 - 伊朗）
- 🇪🇺 欧洲战场（俄乌战争）
- 🌏 亚洲战场（台海/南海 + 缅甸内战）
- 🌎 美洲战场（墨西哥卡特尔 + 厄瓜多尔 + 海地帮派）

**核心能力：**
- ✅ 自动搜索 + 置信度过滤（≥80 分）
- ✅ 风险量化引擎（1-10 分指数）
- ✅ 金融市场影响分析（含 BTC/ETH）
- ✅ 四情景风险展望（基准/温和/中度/极端）
- ✅ 卫星地图动态链接
- ✅ GitHub Pages 自动部署

---

## ⏰ 更新频率

**北京时间：**
- **08:00-23:00:** 每 3 小时（08:00, 11:00, 14:00, 17:00, 20:00, 23:00）
- **01:00-08:00:** 仅 01:00 一次

**每日 7 次自动更新**

---

## 🛠️ 技术架构

| 组件 | 技术 |
|------|------|
| **搜索** | Tavily API |
| **脚本** | Python 3.10+ |
| **部署** | GitHub Pages |
| **自动化** | Cron + Git 推送 |
| **报告管理** | report_manager.py |

---

## 📊 报告结构

每份报告包含：
1. **总体评估** - 全局风险指数（1-10 分）
2. **四大战场** - 各战区风险指数 + 关键事件
3. **金融市场** - 油价/黄金/股市/加密货币
4. **风险展望** - 四情景分析（概率 + 量化）
5. **卫星地图** - 实时链接 + 动态截图

---

## 🚀 快速开始

### 安装依赖
```bash
pip install requests python-dateutil
```

### 配置 API Key
```bash
export TAVILY_API_KEY="your_api_key"
```

### 运行监控
```bash
python3 scripts/mideast-monitor-v21.py
```

### 配置 Cron（北京时间）
```bash
0 1,8,11,14,17,20,23 * * * cd /path/to/repo && python3 scripts/mideast-monitor-v21.py
```

---

## 📁 目录结构

```
global-conflict-monitor/
├── index.html              # GitHub Pages 首页
├── README.md               # 本文件
├── REPORTS.md              # 报告列表
├── .report_config.json     # 报告配置
├── report_manager.py       # 报告管理器
├── reports/                # 报告文件
│   └── global-conflict-YYYYMMDD_HHMM.html
└── scripts/
    └── mideast-monitor-v21.py  # 主脚本
```

---

## 📈 历史报告

查看完整报告列表：https://mckayhou.github.io/global-conflict-monitor/REPORTS.md

---

## ⚠️ 免责声明

- 本报告由 AI 自动生成，仅供参考
- 数据来源：Reuters/ISW/LiveUAMap/ACLED/Tavily
- 不构成投资建议，市场有风险，决策需谨慎

---

## 📞 联系

- **GitHub:** https://github.com/mckayhou/global-conflict-monitor
- **Pages:** https://mckayhou.github.io/global-conflict-monitor/

---

**🦞 最后更新：** 2026-03-04 | **版本：** v23
