# “UV 固定”(UV Pin)选项

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 1225 字 ≥300，非承重" -->

- 在“动画”(Animation)或“绑定”(Rigging)菜单集中：“约束 > UV 固定”(Constrain > UV Pin)> ![图：在“动画”(Animation)或“绑定”(Rigging)菜单集中：“约束 UV 固定”(Constrain UV P…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1225 字 ≥300，非承重" -->

“UV 固定”(UV Pin)从简单的 UV 坐标派生其位置，而[接近度固定(Proximity Pin)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-8A5E153C-8D06-408D-9D72-D82AC39D1288.htm)使用变换中的输入矩阵派生其位置。

本主题介绍了“UV 固定”(UV Pin)窗口中的选项。若要创建 UV 固定节点，请参见[创建 UV 固定](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-AADA4417-39D1-4EE0-84DB-2DCEE2F72B1F.htm)。

**注**

在

属性编辑器(Attribute Editor)

的“UV 固定”(UV Pin)

选项卡中，还提供了适用于

“UV 固定”(UV Pin)

约束的其他控件。在本主题中的

“连接”(Connections)

和

“坐标系”(Coordinate System)

部分之后介绍了这些控件。

## 连接(Connections)

“连接”(Connections)区域可用于指定目标几何体上固定位置的确定方式以及输出矩阵的连接方式。

#### 固定位置(Pin locations)

选择固定位置的派生位置：

- **组件(Components)**：从选定组件的位置派生

- **变换(Transforms)**：从曲面上距选定变换最近的点派生。

#### 输出(Output)

指定输出矩阵的连接方式。可以在[节点编辑器(Node Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-23277302-6665-465F-8579-9BC734228F69)中查看连接。

| 现有变换(Existing Transform) | 使用选定变换并将其连接到 uvPin 的输出。（这是默认设置。） |
|---|---|
| 新变换(New Transform) | 在指定的 UV 坐标处创建新变换，并将其连接到节点输出。 |
| 新定位器(New Locator) | 在指定的 UV 坐标处创建新定位器，并将其连接到节点输出。 |
| 矩阵(Matrix) | 创建（但不连接）节点上的任何输出栓，保持连接可用。 |

## 坐标系(Coordinate System)

此区域确定从曲面法线和 UV 坐标派生时输出如何与曲面坐标系对齐。由于“UV 固定”(UV Pin)是程序节点，因此创建后可以继续在[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)中编辑这些设置，包括可以创建额外的输入和输出。

#### 法线轴(Normal Axis)

指定输出的坐标系中的哪个轴应与曲面法线对齐。不能与“切线轴”(Tangent axis)相同。

#### 切线轴(Tangent Axis)

指定输出的坐标系中的哪个轴与曲面切线对齐。不能与“法线轴”(Normal axis)相同。

#### UV 集(UV Set)

如果场景中包含多个 UV 集，请选择要使用的集。

#### 归一化等参线(Normalize Isoparms)

**注**

此选项仅适用于 NURBS。

由于 NURBS 的坐标值可能以不同方式进行参数化，因此请激活此设置以使用绝对值。

## 属性编辑器选项

[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED) 的“UV 固定”(UV Pin)选项卡包含了“连接”(Connections)和“坐标系”(Coordinate System)部分中未涵盖的其他设置。

#### 法线覆盖(Normal Override)

![图：将“法线覆盖”(Normal Override)设置为“轨道”(Rail)，可以将“UV 固定”(UV Pin)约束连接…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1225 字 ≥300，非承重" -->

将“法线覆盖”(Normal Override)设置为**“轨道”(Rail)**，可以将“UV 固定”(UV Pin)约束连接到轨道曲线几何体。
