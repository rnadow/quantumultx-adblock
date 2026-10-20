# Quantumult X 去广告规则

这是手动维护的规则仓库。仓库不会自动拉取或合并第三方规则。当前收录高德地图、淘宝、京东、拼多多、小红书、百度贴吧、微博、叮咚买菜、Keep 和墨迹天气的部分广告接口，以及少量广告专用域名。来源和验证范围见 [SOURCES.md](SOURCES.md)。

在现有 Quantumult X 配置的对应段落订阅：

```ini
[filter_remote]
https://raw.githubusercontent.com/rnadow/quantumultx-adblock/main/QuantumultX/MyAdBlock.list, tag=自用去广告分流, force-policy=reject, update-interval=86400, enabled=true

[rewrite_remote]
https://raw.githubusercontent.com/rnadow/quantumultx-adblock/main/QuantumultX/MyAdBlock.conf, tag=自用去广告重写, update-interval=86400, enabled=true
```

如果配置中已有 `[filter_remote]` 或 `[rewrite_remote]`，只添加相应 URL 行。使用 HTTPS 重写规则时，需要在 Quantumult X 中启用 MITM 并信任自己生成的证书；将规则涉及的主机名加入 `.conf` 的 `hostname` 行。

这些规则只经过静态检查，尚未在上述 App 中逐一抓包验证。若某个 App 出现异常，可先停用其对应规则。与 [blackmatrix7 AdvertisingLite](https://github.com/blackmatrix7/ios_rule_script/tree/master/rewrite/QuantumultX/AdvertisingLite) 等大合集同时使用时，可能出现重复拦截。
