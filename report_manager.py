#!/usr/bin/env python3
"""
全球冲突报告管理系统
统一管理所有页面的报告列表更新，确保一致性
"""

from pathlib import Path
from datetime import datetime
import json

class ReportManager:
    """报告管理器 - 统一管理所有页面"""
    
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path
        self.reports_dir = repo_path / "reports"
        self.index_file = repo_path / "index.html"
        self.reports_md_file = repo_path / "REPORTS.md"
        self.config_file = repo_path / ".report_config.json"
    
    def scan_reports(self):
        """扫描所有报告文件"""
        if not self.reports_dir.exists():
            return []
        reports = sorted(
            [f.name for f in self.reports_dir.glob("*.html")],
            reverse=True
        )
        return reports
    
    def get_report_info(self, report_name):
        """解析报告文件名获取信息"""
        # global-conflict-20260304_0626.html
        name = report_name.replace('.html', '').replace('global-conflict-', '')
        date_str = f"{name[:4]}-{name[4:6]}-{name[6:8]} {name[9:11]}:{name[11:13]}"
        return {
            'filename': report_name,
            'date_str': date_str,
            'link': f"reports/{report_name}",
        }
    
    def update_all_pages(self, new_report=None):
        """更新所有页面（系统思考：确保一致性）"""
        reports = self.scan_reports()
        
        if not reports:
            print("⚠️ 没有找到报告文件")
            return False
        
        # 更新配置（记录状态）
        self._update_config(reports, new_report)
        
        # 更新 REPORTS.md
        self._update_reports_md(reports)
        
        # 更新 index.html
        self._update_index_html(reports)
        
        print(f"✓ 已更新所有页面（共{len(reports)}份报告）")
        return True
    
    def _update_config(self, reports, new_report=None):
        """更新配置文件（用于追踪状态）"""
        config = {
            'total_reports': len(reports),
            'latest_report': new_report,
            'last_updated': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'),
            'reports': reports[:20]  # 保存最近 20 个
        }
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
    
    def _update_reports_md(self, reports):
        """更新 REPORTS.md"""
        rows = []
        for i, report in enumerate(reports[:20]):
            info = self.get_report_info(report)
            status = "🟢 最新" if i == 0 else "✅ 已发布"
            rows.append(f"| {info['date_str']} | [{info['filename'].replace('.html', '')}]({info['link']}) | {status} |")
        
        content = f"""# 📊 全球冲突报告列表

**Global Conflict Reports Archive**

---

## 📋 报告列表

| 日期时间 | 报告 | 状态 |
|----------|------|------|
{chr(10).join(rows)}

---

## 📈 统计信息

- **总报告数:** {len(reports)}
- **今日报告:** {len(reports)}
- **最新更新时间:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}

---

## 🔗 快速链接

- [🏠 首页](index.html)
- [📖 能力说明](README.md)
- [🌍 GitHub Repo](https://github.com/mckayhou/global-conflict-monitor)

---

## ⏰ 更新频率

**北京时间：**
- **08:00-23:00:** 每 3 小时（08:00, 11:00, 14:00, 17:00, 20:00, 23:00）
- **01:00-08:00:** 仅 01:00 一次

**每日 7 次自动更新**

---

*最后更新：{datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}*
"""
        
        self.reports_md_file.write_text(content, encoding='utf-8')
    
    def _update_index_html(self, reports):
        """更新 index.html（首页）"""
        report_items = []
        for i, report in enumerate(reports[:10]):
            info = self.get_report_info(report)
            latest_class = "latest" if i == 0 else ""
            latest_badge = " | 最新" if i == 0 else ""
            report_items.append(f"""<li class="report-item {latest_class}">
<a href="{info['link']}">🌍 全球冲突情报简报 {info['date_str']}</a>
<div class="report-meta">📅 {info['date_str']}{latest_badge}</div>
</li>""")
        
        content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🌍 全球冲突情报监控</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; line-height: 1.6; color: #333; }}
header {{ border-bottom: 2px solid #eee; padding-bottom: 20px; margin-bottom: 30px; }}
h1 {{ margin: 0; font-size: 1.8em; color: #2c3e50; }}
.subtitle {{ color: #666; font-size: 0.9em; margin-top: 10px; }}
.report-list {{ list-style: none; padding: 0; }}
.report-item {{ background: #f8f9fa; padding: 15px; margin: 10px 0; border-radius: 8px; border-left: 4px solid #0066cc; }}
.report-item a {{ color: #0066cc; text-decoration: none; font-weight: 600; }}
.report-item a:hover {{ text-decoration: underline; }}
.report-meta {{ color: #888; font-size: 0.85em; margin-top: 5px; }}
.latest {{ border-left-color: #28a745; background: #e8f5e9; }}
footer {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #eee; text-align: center; color: #888; font-size: 0.85em; }}
</style>
</head>
<body>
<header>
<h1>🌍 全球冲突情报监控</h1>
<p class="subtitle">Global Conflict Intelligence Monitor | 自动更新四大战场风险报告</p>
</header>

<main>
<h2>📊 最新报告</h2>
<ul class="report-list">
{chr(10).join(report_items)}
</ul>

<h2>ℹ️ 关于</h2>
<p>这是一个全自动全球冲突监控系统，每 3 小时自动扫描四大战场（中东/欧洲/亚洲/美洲），生成专业情报报告。</p>
<p><a href="REPORTS.md">查看完整报告列表 →</a> | <a href="README.md">查看更多能力说明 →</a></p>
</main>

<footer>
<p>数据来源：Reuters/ISW/LiveUAMap/ACLED/Tavily | 自动生成</p>
<p>下次更新：北京时间 17:00 | <a href="https://github.com/mckayhou/global-conflict-monitor">GitHub Repo</a></p>
</footer>
</body>
</html>
"""
        
        self.index_file.write_text(content, encoding='utf-8')


# 主函数（供外部调用）
def update_all_pages(repo_path_str: str, new_report: str = None):
    """更新所有页面的统一入口"""
    repo_path = Path(repo_path_str)
    manager = ReportManager(repo_path)
    return manager.update_all_pages(new_report)


if __name__ == "__main__":
    # 测试
    repo_path = Path("/root/.openclaw/workspace/gcm-repo")
    update_all_pages(str(repo_path))
