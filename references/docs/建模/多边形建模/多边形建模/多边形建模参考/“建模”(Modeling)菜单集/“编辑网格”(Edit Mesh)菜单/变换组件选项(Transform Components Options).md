# 变换组件选项(Transform Components Options)

使用这些选项可设置在选择“编辑网格 > 变换”(Edit Mesh > Transform)时发生的情况。有关可以编辑的其他“变换组件”(Transform Components)属性的描述，请参见 [polyMoveComponentType](../../多边形节点/polyMoveComponentType.md) 属性。

**注**

在“变换组件”(Transform Components)选项窗口中显示的选项取决于当前的多边形组件选择。即，选择边时，会显示边选项，而选择顶点、面或 UV 时，会显示顶点选项。如果未作出任何有效选择，默认情况下会显示顶点选项。

#### “随机”(Random)（顶点、边、面和 UV）

输入值以在从 0 到 1 的值范围内随机变换组件。

#### “局部中心”(Local center)（边）

从“局部中心”(Local center)下拉菜单中选择项目会沿选定边重新定位操纵器。根据所选择的项目，所有后续的变换都将源于该位置。默认为“中间”。

![图：从“局部中心”(Local center)下拉菜单中选择项目会沿选定边重新定位操纵器。根据所选择的项目，所有后续的变换都…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-8D242038-2DE5-4A4F-AEC8-E7111EB99386.png) <!-- baize:img-hook downloaded=false reason="正文 493 字 ≥300，非承重" -->

![图：从“局部中心”(Local center)下拉菜单中选择项目会沿选定边重新定位操纵器。根据所选择的项目，所有后续的变换都…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-79F48FFF-C796-401A-89C3-326823D288C4.png) <!-- baize:img-hook downloaded=false reason="正文 493 字 ≥300，非承重" -->

请参见

通过使用[“属性编辑器”(Attribute Editor)](../../多边形节点/polyMoveComponentType.md)或“通道盒”(Channel Box)在“polyMoveComponentType”节点上编辑属性，可以对变换的组件进行其他修改。

## 相关主题

- [沿法线移动多边形顶点](../../../编辑多边形/变换多边形组件/沿法线移动多边形组件.md)

- [移动、旋转或缩放多边形组件](../../../编辑多边形/变换多边形组件/独立变换多个组件.md)
