# Quantumult X 去广告规则

这是手动维护的规则仓库。仓库不会自动拉取或合并第三方规则。你可以直接编辑 `QuantumultX/MyAdBlock.conf`（重写）与 `QuantumultX/MyAdBlock.list`（分流），提交后再在 Quantumult X 中更新远程资源。

**目前两个文件仅含注释，没有启用任何拦截规则。** 添加并验证自己的规则后，再在现有 Quantumult X 配置的对应段落订阅：

```ini
[filter_remote]
https://raw.githubusercontent.com/rnadow/quantumultx-adblock/main/QuantumultX/MyAdBlock.list, tag=自用去广告分流, force-policy=reject, update-interval=86400, enabled=true

[rewrite_remote]
https://raw.githubusercontent.com/rnadow/quantumultx-adblock/main/QuantumultX/MyAdBlock.conf, tag=自用去广告重写, update-interval=86400, enabled=true
```

如果配置中已有 `[filter_remote]` 或 `[rewrite_remote]`，只添加相应 URL 行。使用 HTTPS 重写规则时，需要在 Quantumult X 中启用 MITM 并信任自己生成的证书；将规则涉及的主机名加入 `.conf` 的 `hostname` 行。

参考来源：[blackmatrix7 AdvertisingLite](https://github.com/blackmatrix7/ios_rule_script/tree/master/rewrite/QuantumultX/AdvertisingLite)、[NobyDa Rewrite_lhie1](https://github.com/NobyDa/Script/blob/master/QuantumultX/Rewrite_lhie1.conf)。从第三方项目复制规则时，请保留来源并遵守其授权条款。
