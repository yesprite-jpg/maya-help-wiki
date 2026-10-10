# “Hypergraph”提示

使用“Hypergraph”时，按下列提示可定义更轻松、更快速的工作流。

## 上游和下游连接

若要显示一个形状的上游和下游连接，请在转到 DG 视图之前选择该形状。选择变换父对象是远远不够的。

## 选择多个节点

如果在 DAG 视图中选择多个节点，当您转到 DG 视图时，将显示包含所有选定节点的 DG 图。

## DG 节点显示

给定 DG 节点的节点类型仅在鼠标悬停在反馈上时显示在弹出窗口中。

## DAG 视图中的连接线

当您将一个节点滚动出视图时，可能会剪裁 DAG 视图中的连接线。（这包括 DG 连接和 IK 控制柄关节跨度线。）

## 在查看大型图表时提高性能

若要在查看大型图表时提高性能，则不会在视图更改时绘制 DAG 连接。

## 书签

书签将记住您的节点排列和背景图像。

## 资产节点

使用“创建资产”(Create Asset)节点功能在依存关系图内创建逻辑分组。资产节点通过允许您将节点组织到对制作流程有意义的分组中来简化依存关系图的显示。有关详细信息，请参见[创建资产](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A59BDB0A-0CB8-4485-A325-EA928AE59D3B)。

## 合并连接

您可以使用选项 > 合并连接(Options > Merge Connections)将多个连接从一个节点压缩到另一个节点。这会将所有平行连接显示为单个粗体连接。如果将鼠标放在粗体连接线上，“Hypergraph”将显示线表示的所有连接的名称。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-B8AEEE80-FDCF-4D89-BD73-949EF09B0CCF.png) <!-- baize:img-hook downloaded=false reason="正文 1370 字 ≥300，非承重" -->

**注**

该选项不会更改连接。仅更改“Hypergraph”显示。

绘制源自资产节点的已合并连接时将附加一个小框。实心框指示所有已合并连接都来自已发布的属性。空心框指示一个或多个已合并连接来自未发布的内部属性。有关资产的详细信息，请参见[资产](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1826F831-E3D1-4045-B6B9-F7D34360C331)。

## 使用热量贴图显示监视性能

您可以使用“Hypergraph”中的“热量贴图显示”(Heat Map Display)选项直观地查看场景中各个节点的性能影响。

“热量贴图显示”(Heat Map Display)处于启用状态时，Maya 根据节点的时间性能为“Hypergraph”中的节点上色。您可以使用“热量贴图显示”(Heat Map Display)监视许多不同的度量标准，包括回调数、计算次数、脏更新数或绘制次数。以指定的度量标准执行的时间较长的节点将由蓝色变为红色，因为它们传递各个阈值。这样，您可以快速识别耗费大量资源或不太耗费资源的节点。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-78068AA7-B01C-49CF-AACF-464904A11905.png) <!-- baize:img-hook downloaded=false reason="正文 1370 字 ≥300，非承重" -->

默认情况下，“热量贴图显示”(Heat Map Display)的颜色方案如下所示：

- 灰色表示计时值为 0。

- 蓝色表示低计时值。

- 红色表示高计时值。

颜色按百分比测量。默认情况下，网络中具有最高计时值的节点为红色，而网络中具有最低非零计时值的节点为蓝色。低计时值和高计时值之间的值以蓝色到红色之间的一种色谱显示。您可以在“热量贴图显示”(Heat Map Display)选项中自定义阈值上限或下限，或者移除高于或低于某一性能阈值的节点。

热量贴图在每次播放结束时或在您单击“热量贴图显示”(Heat Map Display)选项中的“重画 Hypergraph”(Redraw HyperGraph(s))时重新计算。

您可以通过选择“窗口 > 设置/首选项 > 颜色设置”(Windows > Settings/Preferences > Color Settings)，然后选择“Hypergraph”设置并调整各个“热量贴图”(Heat Map)颜色，来自定义“热量贴图显示”(Heat Map Display)中使用的颜色。

### 相关主题

- [Hypergraph“选项”(Options)菜单](Hypergraph%20菜单/Hypergraph%20“选项”%28Options%29菜单.md#GUID-80135B8E-0F59-4C7B-A969-73FE766F4FF5__WS1A9193826455F5FF-4F542F6211C79DEA861-1C76)
