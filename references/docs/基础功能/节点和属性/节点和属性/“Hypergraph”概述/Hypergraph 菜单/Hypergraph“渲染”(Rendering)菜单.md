# Hypergraph“渲染”(Rendering)菜单

#### 显示着色组/显示材质/显示纹理/显示灯光(Show ShadingGroups/ Show Materials/ Show Textures/ Show Lights)

可以显示到着色组、材质、纹理和灯光的连接。

**示例：**

假定您创建了一个 NURBS 球体，然后使用“Hypershade”为其创建并指定一个 Phong 着色组。接下来，使用“Hypershade”创建 2D 棋盘格纹理，然后将其指定到 Phong 节点。

“Hypershade”将显示以下内容：

![图：可以显示到着色组、材质、纹理和灯光的连接。 示例： 假定您创建了一个 NURBS 球体，然后使用“Hypershade”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-555C59A2-BA2E-4A68-8516-3CFBA854321B.png) <!-- baize:img-hook downloaded=false reason="正文 724 字 ≥300，非承重" -->

在“Hypergraph”中选择“渲染 > 显示着色组”(Rendering > Show Shading Groups)时，将显示以下依存关系图。

![图：可以显示到着色组、材质、纹理和灯光的连接。 示例： 假定您创建了一个 NURBS 球体，然后使用“Hypershade”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-B727A441-411F-4003-A785-BDA410DD6EA2.png) <!-- baize:img-hook downloaded=false reason="正文 724 字 ≥300，非承重" -->

节点之间的连接线显示了连接方向。连接线源自输出数据的节点，且该线指向接收数据作为输入的节点。上例中显示，输出的流从 phong1SG 着色组到 renderPartition。

尽管可以看到的大多数节点与“Hypershade”中的节点相同，但依存关系图以流程图的形式显示节点。这样很容易看到构成着色组的节点之间的连接。

如下图所示，如果将鼠标指针移至连接线上，则会出现一个工具提示，用于标识输出节点名称、提供输出的属性、输入节点名称以及接收输入的属性。

![图：可以显示到着色组、材质、纹理和灯光的连接。 示例： 假定您创建了一个 NURBS 球体，然后使用“Hypershade”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-93B5193F-CA2A-46D8-A804-DBB3E34F8BEE.png) <!-- baize:img-hook downloaded=false reason="正文 724 字 ≥300，非承重" -->

节点名称和属性使用句点分隔，例如，initialShadingGroup.partition。在图中，initialShadingGroup 的划分属性将输出到 renderPartition 的集属性。

在许多情况下，必须熟悉 Maya 的内部操作细节才能了解白框中看到的节点和属性名称。

#### 创建渲染节点(Create Render Node)

在“Hypergraph”中使用纹理贴图创建渲染节点。

## 相关主题

- [“Hypergraph”概述](../../“Hypergraph”概述.md)

- [Hypergraph 菜单](../Hypergraph%20菜单.md)
