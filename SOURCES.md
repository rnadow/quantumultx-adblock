# 规则来源与验证范围

整理日期：2026-10-21（UTC）。规则经人工挑选，仓库不会自动拉取上游。

| 文件 | 参考来源 | 上游文件标注更新时间 | 选取范围 |
| --- | --- | --- | --- |
| `QuantumultX/MyAdBlock.conf` | [AdBlock-Splash.conf](https://github.com/hwind2021/QuantumultX-AdBlock-CN/blob/main/quantumultx/rewrite/AdBlock-Splash.conf)、[AdBlock-Feed.conf](https://github.com/hwind2021/QuantumultX-AdBlock-CN/blob/main/quantumultx/rewrite/AdBlock-Feed.conf) | 2026-10-20 | 仅选有明确 App 域名与广告路径的请求拦截规则 |
| `QuantumultX/MyAdBlock.list` | [Splash-Killer.list](https://github.com/hwind2021/QuantumultX-AdBlock-CN/blob/main/quantumultx/filter/Splash-Killer.list) | 2026-10-20 | 仅选广告专用域名 |
| `QuantumultX/MyAdBlock.list` | [anti-AD Surge DOMAIN-SET](https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt)；用其 [Quantumult X 版本](https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-quanx.txt)核对格式与域名 | Surge：2026-10-20；Quantumult X：2026-10-17 | 人工挑选穿山甲和腾讯广告域名；未导入约 10 万条完整列表 |

上游项目的[授权和来源说明](https://github.com/hwind2021/QuantumultX-AdBlock-CN/blob/main/LICENSE)、[anti-AD 项目说明](https://github.com/privacy-protection-tools/anti-AD)适用于其内容。这里没有复制大规模规则表或执行第三方脚本。

本次校验包括：来源文件可读取、规则格式与正则可解析、规则主机名与 MITM 列表对应。**尚未在实际 App 中抓包验证拦截效果**；App 改版后接口可能变化。若出现功能异常，先在 Quantumult X 中停用对应 App 的规则，再根据请求日志调整。
