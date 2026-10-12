# 烘焙变形器工具(Bake Deformer Tool)

- 从“装备”(Rigging)菜单集中访问：“蒙皮 > 烘焙变形到蒙皮权重”(Skin > Bake Deformation to Skin Weights)

- 在 Maya [命令行](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4981A0A5-9418-4274-918C-561E33B0102D)中输入 BakeDeformerTool

可使用烘焙变形器工具来近似计算任意变形器产生的变形，以便您可以将复杂的装备导出到具有有限变形器支持的应用程序。此方法使用权重值的“智能”计算将网格绑定到骨架。

**注**

“烘焙变形到蒙皮权重”(Bake Deformation to Skin Weights)

不会创建新类型的变形器，也不会修改源角色上现有变形器的结果。

**注**

这非常适用于

刚性绑定

和

Delta Mush

等变形。还可以使用它来快速确定默认角色绑定权重

有关使用此工具的信息，请参见[在角色上烘焙变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-8B68FF4A-E9BC-44E9-B0D9-53CFE0C008FC.htm)。

#### 源(Source)

指定要简化的角色。

#### 网格(Mesh)

要烘焙的网格。

#### 骨架(Skeleton)

要烘焙的骨架。

#### 目标(Destination)

指定接收变换的对象。

#### 网格(Mesh)

应用变形的网格。

#### 骨架(Skeleton)

![图：网格(Mesh) 应用变形的网格。 骨架(Skeleton) 应用变形的骨架。 在 Maya 2018 Update 4…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 633 字 ≥300，非承重" -->

应用变形的骨架。

在 Maya 2018 Update 4 之后，使用“烘焙变形器”(Bake Deformer)工具时，骨架上色不再自动进行，且在创建新蒙皮簇时，不为骨架指定颜色。

现在，骨骼上色是可选的。如果要对骨架上色，可以使用 bakeDeformer 命令上的以下标志，在[脚本编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7C861047-C7E0-4780-ACB5-752CD22AB02E)中用脚本激活它。

```text
colorizeSkeleton = true
```

#### 影响数量(Number of influences)

用于增加或减少每个顶点使用的最大影响数量。
