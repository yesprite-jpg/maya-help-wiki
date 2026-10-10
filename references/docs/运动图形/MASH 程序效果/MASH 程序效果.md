# MASH 程序效果

使用 MASH 可以创建包含程序节点网络的多用途运动设计动画。从属性编辑器和节点编辑器中自定义所有效果，并将效果链接在一起实现更大的变化。

您可以从场景中的一个或多个对象创建 MASH 网络，必要时，您可以通过“实例化器”(Instancer)或“重新投影”(Repro)节点在 MASH 网络中添加和移除对象。

创建 MASH 网络

1. 如果尚未加载 MASH 插件，请转到“窗口 > 设置/首选项 > 插件管理器”(Windows > Settings/Preferences > Plug-in Manager)，然后加载 MASH 插件。

2. 转到“动画”(Animation)或“FX”菜单集。

3. （可选）在场景中选择要用作输入对象的对象。

4. 选择“MASH > 创建 MASH 网络”(MASH > Create MASH Network)，或者单击“MASH”或“运动图形”(Motion Graphics)工具架中的“创建 MASH 网络”(Create MASH Network)图标 (![图：选择“MASH 创建 MASH 网络”(MASH Create MASH Network)，或者单击“MASH”或“运动…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-MotionGraphics/images/GUID-718E37DB-8D71-4F32-A5F1-0D8CA2356244.png) <!-- baize:img-hook downloaded=false reason="正文 848 字 ≥300，非承重" -->)。

Maya 会自动隐藏任何选定的输入对象，改为显示这些对象的多个实例（沿一系列不可见的点排列）。它还会使用以下三个起始节点填充新的 MASH 网络：

- “Waiter”节点，充当整个网络的中心。可以使用此节点向网络添加其他节点或更改其显示和处理方式。

- “分布”(Distribute)节点，用于处理原始对象副本的初始数量和排列。

- 取决于当前“几何体类型”(Geometry Type)（通过 [MASH 菜单](MASH%20程序效果/MASH%20参考/MASH%20菜单.md)设置）的其他节点。 默认情况下，Maya 会为源对象创建功能全面的[复制对象](MASH%20程序效果/MASH%20参考/MASH%20节点概述/重新投影.md)，但您可以手动将其更改为速度更快（但限制更多）的[实例](MASH%20程序效果/MASH%20参考/MASH%20节点概述/实例化器.md)。

创建初始 MASH 网络后，可以通过使用 MASH 过滤器（禁用“仅 DAG 对象”(DAG objects only)时，“显示 > 对象 > MASH”(Show > Objects > MASH)），在“MASH 编辑器”(MASH Editor)或“大纲视图”(Outliner)中查看新节点。

**注**

您可以在

Creative Market

找到一些免费的 MASH 示例项目。

## 相关主题

- [MASH 节点](MASH%20程序效果/MASH%20参考/MASH%20节点概述.md)

- [MASH 编辑器](MASH%20程序效果/MASH%20参考/MASH%20窗口和编辑器/MASH%20编辑器.md)
