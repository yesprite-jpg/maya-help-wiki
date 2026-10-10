# maya-help-wiki

面向 Agent 的 Maya 2022 帮助手册（Layout／动画核心层） 离线 Wiki Skill，来源为 <https://help.autodesk.com/view/MAYAUL/2022/CHS>。

**先读 [版权与使用声明](COPYRIGHT-NOTICE.md)**：文档正文与截图版权归 Autodesk，本仓库是个人离线检索快照，不代表取得再分发许可。

文档按原 Wiki 导航层级保存为 Markdown，并配有完整索引、本地全文检索和逐文档 SHA-256 清单。手动或自动同步会先比较内容哈希；没有变化时不会重写正文、索引或清单。

## 使用

调用 `$maya-help-wiki` 后直接询问 Maya 2022 帮助手册（Layout／动画核心层） 的概念、使用、配置或排障问题。Agent 会先检索少量相关文档，再给出带本地文档路径的回答。

## 更新与边界

- 更新规则见 `references/UPDATE.md`，来源和许可边界见 `references/SOURCE.md`。
- 这是离线快照；版本敏感问题需要核对规范来源。
- 不包含真实凭据，不绕过登录、付费墙或访问控制。
