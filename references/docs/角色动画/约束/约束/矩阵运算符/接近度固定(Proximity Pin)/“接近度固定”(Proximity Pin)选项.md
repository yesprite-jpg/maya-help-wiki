# “接近度固定”(Proximity Pin)选项

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 1877 字 ≥300，非承重" -->

  在“动画”(Animation)或“绑定”(Rigging)菜单集中：“约束 > 接近度固定”(Constrain > Proximity Pin)> ![图：在“动画”(Animation)或“绑定”(Rigging)菜单集中：“约束 接近度固定”(Constrain Prox…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1877 字 ≥300，非承重" -->

  本主题介绍了“接近度固定”(Proximity Pin)窗口中的选项。若要创建 proximityPin 节点，请参见[创建接近度固定](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-92DA0E89-26BB-4F1A-A74B-541FE2359BDC.htm)。

**注**

在

属性编辑器(Attribute Editor)

的“接近度固定”(Proximity Pin)选项卡中，还提供了适用于“接近度固定”(Proximity Pin)约束的其他控件。在本主题中的

“连接”(Connections)

和

“坐标系”(Coordinate System)

部分之后介绍了这些控件。

## 连接(Connections)

“连接”(Connections)区域包含将连接到节点输入和输出的变换。

**注**

连接选项不能同时设置为

“现有变换”(Existing Transform)

，否则将创建循环。一个节点上可以有多个输入或输出。

#### 输入(Input)

在[节点编辑器(Node Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-23277302-6665-465F-8579-9BC734228F69)中设置“接近度固定”(Proximity Pin)节点上的输入矩阵连接。

| 新定位器(New Locator) | 将选定变换作为定位器（称为 pinInput）进行复制，并将其连接到 proximityPin 节点的输入。（这是默认设置。） |
|---|---|
| 现有变换(Existing Transform) | 使用选定变换并将其连接到 proximityPin 节点的输入。 |
| 新变换(New Transform) | 将选定变换作为变换（称为 pinInput）进行复制，并将其连接到 proximityPin 节点的输入。 |
| 矩阵(Matrix) | 将输入栓添加到节点，而不连接定位器或变换。 注： 也可以在[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)中添加新的输入矩阵。 |

#### 输出(Output)

设置输出矩阵连接。

| 现有变换(Existing Transform) | 使用选定变换并将其连接到 proximityPin 节点的输出。（这是默认设置。） |
|---|---|
| 新定位器(New Locator) | 在曲面上的最近点处创建新定位器，并将其连接到节点的输出。 |
| 新变换(New Transform) | 在曲面上的最近点处创建新变换，并将其连接到节点的输出。 |
| 矩阵(Matrix) | 创建（但不连接）节点上的任何输入栓，保持连接可用。 |

## 坐标系(Coordinate System)

“坐标系”(Coordinate System)区域可用于设置从几何体曲面派生固定坐标的方式。由于“接近度固定”(Proximity Pin)是程序节点，因此创建后可以继续在[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)中编辑这些设置。

#### 模式(Mode)

指定从曲面派生坐标系的方式。

#### UV 集(UV Set)

指定在模式设置为“UV”时用于坐标系的 UV 集。

#### 法线轴(Normal axis)

指定输出的坐标系中的哪个轴与曲面法线对齐。不能与“切线轴”(Tangent axis)相同。

#### 切线轴(Tangent axis)

指定输出的坐标系中的哪个轴与曲面切线对齐。不能与“法线轴”(Normal axis)相同。

#### 保持偏移(Maintain Offset)

保留输入矩阵和[原始几何体](../../../../变形效果/变形效果/变形器成员身份/使用组件标记编辑变形器成员身份/原始几何体.md)之间的初始偏移。创建后，[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)允许您单独控制偏移的平移和方向，并支持小数。如果在“接近度固定”(Proximity Pin)窗口中激活“保持偏移”(Maintain Offset)，则它们最初均设置为 1。如果禁用“保持偏移”(Maintain Offset)，则平移和方向偏移最初均设置为 0。

## 属性编辑器选项

[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED) 的“接近度固定”(Proximity Pin)选项卡包含了“连接”(Connections)和“坐标系”(Coordinate System)部分中未涵盖的其他设置。

#### 封套(Envelope)

要应用的变换量。1.0 表示完全变换，0.0 表示不变换。

#### 坐标模式(Coordinate Mode)

与上述**“坐标系”(Coordinate System)**区域中的**“模式”(Mode)**设置相同。

#### 偏移平移(Offset Translation)

控制要使用的原始曲面偏移量。1.0 将保持完全绑定平移偏移，0.0 将强制对象保留在曲面上。

#### 偏移方向(Offset Orientation)

控制要使用的原始曲面偏移量。值为 1.0 将保持完全绑定方向偏移，值为 0.0 将使用从曲面派生的方向。

#### 法线覆盖(Normal Override)

![图：将“法线覆盖”(Normal Override)设置为“轨道”(Rail)，可以将“接近度固定”(Proximity P…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1877 字 ≥300，非承重" -->

将“法线覆盖”(Normal Override)设置为**“轨道”(Rail)**，可以将“接近度固定”(Proximity Pin)约束连接到轨道曲线几何体。
