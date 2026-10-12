# ShaderFX 的“UV 集”(UV Set)和“顶点颜色”(Vertex Color)节点

以下是两种公用的且非常有用的节点。

## UV 集(UV Set)

通过以下方法创建该节点：在“ShaderFX”编辑器中选择“硬件着色器节点 > 公共输入 > UV 集”(Hw Shader Nodes > Inputs Common > UVSet)。

“UV 集”(UV Set)节点控制 UV 纹理坐标的排列。

一些节点是包含“UV 集(UV Set)”节点的组。示例包括“纹理贴图”(Texture Map)节点（“硬件着色器节点 > 纹理 > 纹理贴图”(Hw Shader Nodes > Textures > Texture Map)）或“棋盘格 2D”(Checker 2D)节点（“硬件着色器节点 > 图案 > 棋盘格 2D”(Hw Shader Nodes > Patterns > Checker 2D)）。

例如，“棋盘格 2D”(Checker 2D)节点使用 “UV 集”(UV Set)节点来确定如何分割棋盘格图案。棋盘格图案将连接到此对象的 UV 布局，并且当更改对象的 UV 时，棋盘格图案也会随之更改。

有关如何使用“UV 集”(UV Set)节点改变纹理图案的示例，请参阅[乘以纹理以在平铺图案中重复它来创建更密集的不同效果](../ShaderFX%20介绍性的采样工作流.md#GUID-7C3BECD1-6E58-4963-9534-477314928E0F__GUID-19AAE387-4BCF-46D2-BD83-A3C50829A8C8)。

有关如何使用默认或自定义 UV 集名称的信息，请参阅[使用 UV 集](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-05D66C65-0B08-4EED-AD13-E40A6A3C74B4.htm)。

## 顶点颜色(Vertex Color)

通过以下方法创建该节点：在“ShaderFX”编辑器中选择“硬件着色器节点 > 纹理 > 顶点颜色”(Hw Shader Nodes > Textures > Vertex Color)。

“顶点颜色”(Vertex Color)节点控制顶点颜色。

有关如何使用“顶点颜色”(Vertex Color)节点改变纹理图案的示例，请参阅[使用顶点颜色节点融合纹理](../ShaderFX%20介绍性的采样工作流.md#GUID-7C3BECD1-6E58-4963-9534-477314928E0F__GUID-5D2A088F-0505-4041-BA7B-C298E9530F56)。

有关如何使用默认或自定义颜色集名称的信息，请参阅[使用 UV 集](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-05D66C65-0B08-4EED-AD13-E40A6A3C74B4.htm)。此过程的准则与 UV 集的准则等效。
