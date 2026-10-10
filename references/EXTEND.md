# EXTEND · 本包缺页时怎么办（三步 + 红线）

## 什么时候用

`scripts/search_docs.py` 命中 0 条，并且你在 `references/SOURCE.md` 里确认该主题属于
「Maya 手册有此页、只是本包没装」时，才走本流程。手册命中不了本包的问题不是缺页，别抓。

事实源是 `references/missing_pages.json`： Autodesk Maya 2022 帮助站带链接页面共 6,532 页
（`_meta.roster_pages_total`），核心层 2,724 页已入库；2026-10-10 又从 excluded 名册补装 67 页疑难解答／许可类
（包内正文 2,724＋67＝2,791 篇，核心层仍为 2,724，补装页不计入核心层），其余 3,741 页（`_meta.entries`）
列在这里，每条四个字段：`t` 标题 / `p` 入库后在 `references/docs` 下的落点 / `u` 原文 URL / `b` 书目 ID。

## 三步

```
python scripts/add_pages.py --keywords "崩溃 许可"          # 1 提议：只报告，不联网不写盘
python scripts/add_pages.py --keywords "崩溃 许可" --apply   # 2 人确认后才会真的抓并写盘
python scripts/selfcheck.py                                 # 3 体检，末行必须是 EVIDENCE_ALL_OK
```

选择页面也可用 `--paths <文件>`（每行一个 `p`）或 `--url <文件>`（每行一个 `u`）。
`--apply` 会先把 `wiki-manifest.json`、`references/INDEX.md`、`references/missing_pages.json`
备份到**包外** `<包同级>/.maya-help-wiki-backup/<时刻>/`（默认 `../.maya-help-wiki-backup/`，
可用 `--backup-dir <目录>` 改到别处；最多留 3 份，超了删最旧的，删前把待删清单与逐件 sha16 写进
本次 `references/.extension/report-<时刻>.json`），再把每页记进
`references/.extension/CHANGELOG.local.md` 并写出最新那份报告。**包内只留日志**
（`CHANGELOG.local.md` ＋最近一份 `report-*.json`，共约 1 KB）；备份不留在包里，因为它一份就 ≈7 MB。
要撤销这一批：

```
python scripts/add_pages.py --keywords x --rollback <时刻>
```

（回滚用的是包外那枚 `<时刻>` 备份，所以别手删它；`--backup-dir` 改过位置的话，回滚要带同一个参数。）

退出码：`0` 成功（含 `--suggest`）；`3` 被安全规则拒绝（未发请求、未写盘）；`2` 抓取中途失败已回滚，
或输入文件读不到。自动化调用方**按退出码判成败**，别只看有没有打印提示。

体检表可加 `--baseline <快照 json>`（形如 `{"docs": {"references/docs/...md": "<sha256 hex>"}}`），
它会把快照里的每一篇与磁盘现算哈希对拍，用来证明老页没被改动。**发布或分享本包之前先看第 10 格**
（包内 `references/.extension` 总体积 ≤256 KB）——那格是专门拦住"备份又偷偷长回包里"的闸；
它判红就说明有人把备份写进了包内，先挪出去再发布。

## 红线

- 只允许 `help.autodesk.com`，其他域名一律拒绝（页面 URL 和图片 URL 都查），拒绝时退出码 3。
- 单次 `--apply` ≤ 30 页，超了直接拒（rc=3），请分批。
- 备份只写包外目录，**不要**把它挪进 `references/`；包内 `.extension` 只放日志（selfcheck 第 10 格会管）。
- 只增不删：已有正文（核心层 2,724 ＋ 补装 67 ＝ 包内 2,791 篇）、251 张图、`wiki-manifest.json` 里的老条目一律不动。
- 不要 `--prune`、不要删文件、不要装第三方包、不要建定时任务或常驻服务、不要花钱。
- **补装过的包别再直接跑增量同步（`sync_wiki_docs.py`）**：它对 `wiki-manifest.json`（现含 2,791 篇）与「重采的核心层」（2,724 篇）做差集判 stale，差集正好是这 67 页补装件。
  1. 不给 `--prune` 时会抛 `StaleFilesError`（STALE_REQUIRES_APPROVAL，不会静默删）——**撞到它是保护、不是故障**，别当成抓取出错去重试。
  2. 给了 `--prune` 就会按核心层名册收口、**把这 67 页补装件全删掉**；绝不允许随手 `--prune`。
  3. 真要同步上游新版：先把包外备份留在手（`add_pages.py --rollback <stamp>` 与 `.maya-help-wiki-backup/<stamp>/`），并把这 67 页的 `CHANGELOG.local.md` 行交给人核对，再动同步。
- 图按 ADR 0001 处理：只有「正文 < 300 字且带 `/images/` 图」的承重页才下载图片，
  且下载到 `references/.extension/assets/`，**不进 `references/assets`、不进 assets 名册**；
  其余一律留绝对 URL + `<!-- baize:img-hook -->`。
- 抓取失败的页写进报告，不许静默；`selfcheck.py` rc 非 0 就别用这一批结果，把读数报给人，
  不要改判据让它变绿。

## 许可提醒

正文与界面截图的版权归 Autodesk。补页等于扩大再分发面：本包 `wiki.license` 写的是
「再分发许可未确认，仅限本地使用，公开发布前必须核对」。公开发布或分享包含补页的包之前，
先核对 Autodesk 的再分发条款，见 `references/COPYRIGHT-NOTICE.md`（若有）与 `references/SOURCE.md`。

## 重新生成缺页清单

`scripts/gen_missing_pages.py` 需要抓取侧的名册 `roster.json`（不在包内，属构建面）。
拿不到名册时就用包里现有的 `missing_pages.json`，不要凭记忆手写条目。
