# “细节级别”(Level of Detail)属性

当您选择 LOD_group 节点时，您可以使用“通道盒”(Channel Box)或“属性编辑器”(Attribute Editor)编辑以下属性。

“通道盒”(Channel Box)中可用的属性将会更改，具体取决于您是根据“距离”(Distance)还是“屏幕高度百分比”(Screen Height Percentage)设定 LOD 组及其阈值设置。（请参见[创建 LOD 组](创建%20LOD%20组.md)。）

#### 阈值类型

显示 LOD 是设置为使用“距离”(Distance)还是“屏幕高度百分比”(Screen Height Percentage)以触发级别切换。

默认情况下，“阈值类型”(Threshold Type)设置为“百分比”(Percentage)（“屏幕高度百分比”(Screen Height Percentage)），这将根据整个 LOD 组在当前摄像机帧中所占的屏幕高度百分比拾取要显示的组级别。

设置为“距离”(Distance)时，级别切换取决于它们距离摄影机的距离。

**注**

提示：

如果基于正交摄影机创建 LOD 组，将

“阈值类型”(Threshold Type)

设置为

“距离”(Distance)

，此选项将显示为只读，您无法更改

“阈值类型”(Threshold Type)

。

但是，如果基于正交摄影机创建 LOD 组，将“阈值类型”(Threshold Type)设置为“百分比”(Percentage)，则可以通过临时切换到透视摄影机，并将“阈值类型”(Threshold Type)设置为“距离”(Distance)，启用“阈值类型”(Threshold Type)切换，然后切换回“百分比”(Percentage)和原始正交摄影机。这将创建使阈值类型切换对正交摄影机起作用所需的“距离”(Distance)阈值。请参见 [LOD 和正交摄影机](基于距离的%20LOD%20和正交摄影机.md)了解更多详细信息。

#### LOD_ *n* 显示(LOD_n Display)

（其中 *n* 是组中每个 LOD 的名称。）

控制级别几何体是根据 LOD 组阈值规则（“使用细节级别”(uselod)）显示，还是始终显示（“显示”(show)），或者从不显示（“隐藏”(hide)）。这对测试十分有用，使您能够独立于组的阈值设置强制显示不同的级别，以便您能够比较几何体。另请参见[测试或预览 LOD](测试或预览%20LOD.md)。

#### “LOD_*n* 开始百分比”(LOD_n Start Percentage)或“LOD_*n* 开始距离”(LOD_n Start Distance)

（其中 *n* 是组中每个 LOD 的名称。）

此属性标签将发生更改，具体取决于组“阈值类型”(Threshold Type)是设置为“距离”(Distance)还是“屏幕高度百分比”(Screen Height Percentage)。更改这些值以修改何时启用级别，然后缩放以测试结果。另请参见[编辑 LOD 阈值](编辑%20LOD%20阈值的值.md)。

#### 摄影机

（仅在“阈值类型”(Threshold Type)设置为“百分比”(Percentage)时才可用。）选择要用于确定 LOD 级别切换时间的摄影机。

#### 世界空间(World Space)

仅当“阈值类型”(Threshold Type)设置为“距离”(Distance)时适用。启用时，根据世界原点在各 LOD 之间进行切换。否则，根据 LOD 组的原点进行切换。

#### 最小最大距离(Min Max Distance)

仅当“阈值类型”(Threshold Type)设置为“距离”(Distance)时适用。禁用时（默认），行为不会发生更改。启用时，“最小距离”(Min Distance)和“最大距离”(Max Distance)属性将定义对象的可见性范围。

## 相关主题

- [创建 LOD 组](创建%20LOD%20组.md)

- [测试或预览 LOD](测试或预览%20LOD.md)
