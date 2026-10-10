# 版权与使用声明 / Copyright & Use Notice

本仓库里有两类东西，授权来源不同，请分开理解。

## 1. 文档正文与界面截图 — 版权归 Autodesk

`references/docs/**`（2,724 篇 Markdown）与 `references/assets/**`（251 张图片）的内容来自
**Autodesk 官方 Maya 2022 简体中文帮助手册**（规范来源：<https://help.autodesk.com/view/MAYAUL/2022/CHS>）。

我做这份快照的用途是：给自己和一个 Agent 做**离线检索与问答**，解决"手册内容埋得太深、每次要靠截图问答"的问题。
上传到这里是个人备份与学习分享性质，**不代表我取得了 Autodesk 文档的再分发许可**，也不构成对任何人使用 Autodesk 内容的授权。

- 文档正文与截图的版权归 **Autodesk** 所有。
- 若 Autodesk 认为本仓库中的任何文件不妥，请开 Issue 或直接联系我，我会**立即删除相应文件或整个仓库**。
- 请不要再把 `references/docs/**` 与 `references/assets/**` 二次分发或用作训练/商业用途前先自行核对 Autodesk 条款。

## 2. 检索与同步脚本 — 由第三方 Skill「白泽」产出

`scripts/search_docs.py`、`scripts/sync_wiki_docs.py` 及包结构（`SKILL.md`、`references/INDEX.md`、
`references/wiki-manifest.json`、`references/SOURCE.md`、`references/UPDATE.md`）由公开 Skill
**白泽（baize）**的生成器产出，遵循其原始许可声明（CC BY-NC-SA），本仓库仅收录其运行产物副本，不另行授权。

`wiki-manifest.json` 为每篇文档记录了 SHA-256，任何人 clone 后可逐篇校验内容是否被我或他人改动过。

## 3. 时效声明

抓取时间：**2026-10-09**（Maya 2022 CHS 版本快照）。离线快照不天然代表最新内容；版本敏感问题请核对上方规范来源。
