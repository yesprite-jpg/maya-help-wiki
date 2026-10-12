# 融合变形 > 将拓扑烘焙到目标(Blend Shape > Bake Topology To Targets)

- 在“动画”(Animation)、“绑定”(Rigging)和“建模”(Modeling)菜单集中：“变形 > (编辑)融合变形 > 将拓扑烘焙到目标”(Deform > (Edit) Blend Shape > Bake Topology To Targets)

使用“将拓扑烘焙到目标”(Bake Topology to Targets)，可以重新生成或更新融合形变变形，以使对基础对象所做的任何拓扑更改也会应用到其目标对象。有关详细信息，请参见[将拓扑更改从基础对象传播到目标对象](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-FD9D539B-BEC0-4F2F-B4E1-E96AFC88756B.htm)。

**注**

- “将拓扑烘焙到目标”(Bake Topology to Targets)会产生包含多边形几何体的最佳结果。

- “绘制融合变形权重工具”(Paint Blend Shape Weights Tool)支持自定义法线和 UV。

## 拓扑传播限制

- 在许多顶点相互比较靠近的密集拓扑数据实例中，“将拓扑烘焙到目标”(Bake Topology to Targets)可能导致顶点交换。例如，顶点交换可能会出现在模型的闭合口处。若要防止在此实例中进行顶点交换，请在使用“将拓扑烘焙到目标”(Bake Topology to Targets)之前打开模型口。

- “将拓扑烘焙到目标”(Bake Topology to Targets)在选定子集上执行时可能会产生不需要的结果。

- “将拓扑烘焙到目标”(Bake Topology to Targets)用于 NURBS 几何体，但生成的目标对象变形看上去可能与基础对象的变形并不完全一致。
