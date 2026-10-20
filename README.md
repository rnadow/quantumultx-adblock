# Quantumult X 去广告规则

此仓库镜像 [blackmatrix7/ios_rule_script 的 AdvertisingLite](https://github.com/blackmatrix7/ios_rule_script/tree/master/rewrite/QuantumultX/AdvertisingLite)。自动更新任务每天检查上游；只有规则与授权文件都下载并通过基本校验时才提交。规则文件保持上游原样，便于核对来源。

## 在 Quantumult X 中订阅

仓库首次运行更新任务后，在现有配置的相应段落中加入：

```ini
[filter_remote]
https://raw.githubusercontent.com/rnadow/quantumultx-adblock/main/QuantumultX/AdvertisingLite.list, tag=广告分流, force-policy=reject, update-interval=86400, enabled=true

[rewrite_remote]
https://raw.githubusercontent.com/rnadow/quantumultx-adblock/main/QuantumultX/AdvertisingLite.conf, tag=广告重写, update-interval=86400, enabled=true
```

如果已有 `[filter_remote]` 或 `[rewrite_remote]`，只加入对应 URL 行，不要重复添加段落标题。HTTPS 重写需要在 Quantumult X 中启用 MITM 并信任自己生成的证书。建议先关闭与这套规则重复的去广告订阅，再观察常用 App 是否正常。

## 来源与范围

- 上游规则：[AdvertisingLite.list](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rewrite/QuantumultX/AdvertisingLite/AdvertisingLite.list) 和 [AdvertisingLite.conf](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rewrite/QuantumultX/AdvertisingLite/AdvertisingLite.conf)。
- 旧版 [NobyDa/Rewrite_lhie1.conf](https://raw.githubusercontent.com/NobyDa/Script/master/QuantumultX/Rewrite_lhie1.conf) 标注更新于 2021 年，且包含去广告以外的跳转、请求头改写。此仓库不合并该文件。
- 镜像内容版权归原作者，按上游 [GPL-2.0 授权](https://github.com/blackmatrix7/ios_rule_script/blob/master/LICENSE) 分发；`LICENSE` 随规则同步。

更新任务位于 `.github/workflows/update-rules.yml`。也可以运行 `python scripts/update_rules.py` 手动更新。网络失败或内容校验失败时，不会替换已有规则。
