# “编辑接近度包裹变形器”(Edit Proximity Wrap Deformer)窗口

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1418 字 ≥300，非承重" -->

在“属性编辑器”(Attribute Editor)的**“接近度包裹”(Proximity Wrap)**选项卡中单击“编辑节点”(Edit Node)时，将打开“编辑接近度包裹变形器”(Edit Proximity Wrap Deformer)窗口。

#### 节点(Node)

标识活动的“接近度包裹”(Proximity Wrap)节点。

展开“选择”(Select)下拉菜单，以选择场景中的任何“接近度包裹”(Proximity Wrap)驱动者。

#### “驱动者”(Drivers)区域

使用“驱动者”(Drivers)区域可更改或添加几何体以推动变换。

#### “选择”(Select)菜单

选择现有“接近度包裹”(Proximity Wrap)节点。

#### 添加选定对象(Add Selected)

从选定几何体创建新的驱动者。

#### 移除选定对象(Remove Selected)

从选定几何体中删除驱动者。

#### 新驱动者默认值(New Drivers Defaults)

#### 包裹模式(Wrap Mode)

选择驱动者影响几何体的方法。如果设置为**“全局”(Global)**，各个驱动者都将使用此模式。

| 模式 | 行为 |
|---|---|
| 表面(Surface) | 在考虑曲面法线的同时移动所有内容。当“偏移”(Offset)模式失败时，请使用此模式。这种模式需要更多的时间来处理，因为它必须计算曲面法线。该设置为默认设置。 |
| 偏移(Offset) | 根据加权影响，将驱动者移动的顶点数应用于目标顶点。它将忽略曲面方向，因此涉及严重旋转时，它可能会产生瑕疵。但如果不是这种情况，“偏移”(Offset)是将驱动者变形应用于目标的有效方式。 |
| 捕捉(Snap) | 将几何体捕捉到驱动者，因此它的行为在某些方面与收缩包裹变形器类似。它也可用于调试，因为它清楚地说明了驱动者的哪些部分被目标绑定。 |
| 刚性(Rigid) | 使用驱动者几何体来计算影响，且仅使用驱动者的变换来使目标变形。通过这种方式，其行为与 skinCluster 变形器十分类似。 |
| **簇(Cluster)** 注： “簇”(Cluster)包裹选项仅在这些选项的“属性编辑器”(Attribute Editor)版本中可用。若要使用“簇”(Cluster)，请单击“属性编辑器”(Attribute Editor)的**“ProxWrap”**选项卡，然后使用其中的“包裹模式”(Wrap Mode)菜单。 | 使用驱动者矩阵输入来变换顶点。 |

#### 强度(Strength)

调整驱动者的相对影响。此倍增用于增加或减少某一驱动者相对于其他驱动者对相同顶点造成的影响。

#### 衰减开始(Falloff Start)

距影响开始下降的驱动者的距离。

#### 衰减结束(Falloff End)

距影响完全消失的驱动者的距离。

#### 平滑法线(Smooth Normals)

仅当使用曲面包裹模式时才会处于活动状态。

此设置预先运行一个过滤器（而不是使用直接曲面法线）来平滑生硬更改。使用此设置可生成更柔和的外观结果。

#### 覆盖平滑法线(Override Smooth Normals)

如果希望驱动者覆盖“平滑法线”(Smooth Normals)值，请激活此选项。

#### 覆盖衰减渐变(Override Falloff Ramp)

如果希望驱动者覆盖衰减渐变值，请激活此选项。

#### 几何体(Geometry)区域

#### “选择”(Select)菜单

从此下拉菜单中选择场景中要受驱动者几何体影响的几何体。

#### 添加选定对象(Add Selected)

添加要受变形几何体（驱动者）影响的新几何体。

#### 移除选定对象(Remove Selected)

从变形影响物中移除几何体。
