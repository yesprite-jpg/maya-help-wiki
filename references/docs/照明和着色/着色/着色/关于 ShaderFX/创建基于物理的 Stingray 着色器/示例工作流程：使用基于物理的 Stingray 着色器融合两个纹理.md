# 示例工作流程：使用基于物理的 Stingray 着色器融合两个纹理

此示例演示如何使用 Stingray PBS 节点和 ShaderFX 节点创建着色器网络，以便可以通过绘制顶点融合两个纹理。

此工作流与 [ShaderFX 介绍性示例工作流](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-7C3BECD1-6E58-4963-9534-477314928E0F.htm)主题中的*“使用顶点颜色节点融合纹理”*示例类似；但是，此示例使用 Stingray PBS 节点及其关联的 ShaderFX 节点。

  在场景中创建一个平面，并将其细分增至 20x20。

  右键单击该平面并选择“指定新材质”(Assign New Material)，然后从“指定新材质”(Assign New Material)窗口中选择 Stingray PBS。

  按 6 键以选择带纹理模式。

  在 StingrayPBS“属性编辑器”(Attribute Editor)中，从“预设材质”(Preset Material)下拉列表中选择“自定义”(Custom)。

  单击属性编辑器中的“打开 ShaderFX”(Open ShaderFX)以打开 ShaderFX 编辑器窗口。

  将“采样纹理”(Sample Texture)节点从节点浏览器拖动到工作区。将它连接到第一个纹理；在此示例中为“混凝土”。

  创建第二个“采样纹理”(Sample Texture)节点，并将它连接到第二个纹理；在此示例中为“草地”。

  创建 TexCoord 0 节点。

  注意：必须将 UV 集节点连接到“采样纹理”(Sample Texture)的 UV 输入，才能设置对象的纹理坐标。UV 端口的红色边界也表示输入是强制的。

  将 Texturecoord0 的“RG”输出连接到每个“采样纹理”(Sample Texture)节点的“UV”输入。

  创建“顶点颜色 0”(Vertex Color 0)节点和“线性插值”(Linear Interpolate)节点。

  将第一个“采样纹理”(Sample Texture)节点的“RGBA”输出连接到“线性插值”(Linear Interpolate)节点的第一个“值”(Value)输入。

11. 将第二个“采样纹理”(Sample Texture)节点的“RGBA”输出连接到第二个“值”(Value)输入。

  将“顶点颜色 0”(Vertex Color 0)节点的“RGBA”输出连接到“线性插值”(Linear Interpolate)节点的“混合”(Mix)输入。

  顶点颜色用于融合两个纹理。

  单击“线性插值”(Linear Interpolate)节点上的“混合”(Mix)属性。在属性编辑器中，在“组件混合”(Component Swizzle)字段中输入 r。

  在“混合”(Mix)属性的旁边将添加 r 注释。红色通道现在用于融合两个纹理。

  将“线性插值”(Linear Interpolate)的“结果”(Result)输出连接到“标准基础”(Standard Base)的“基础颜色”(Base Color)输入。

  选择平面，然后选择“网格显示 > 应用颜色”(Mesh Display > Apply Color) > ![图：选择平面，然后选择“网格显示 应用颜色”(Mesh Display Apply Color) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1456 字 ≥300，非承重" -->。

  将“颜色”(Color)设置为黑色，然后单击“应用颜色”(Apply Color)以确保所有顶点都以顶点颜色 0, 0, 0 开始。

  选择“网格显示 > 绘制顶点颜色工具”(Mesh Display > Paint Vertex Color Tool) > ![图：选择“网格显示 绘制顶点颜色工具”(Mesh Display Paint Vertex Color Tool) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1456 字 ≥300，非承重" -->。

  将“颜色”(Color)值设置为红色，因为红色通道用于融合。

  在平面上绘制，您会看到用红色绘制的区域采用草地纹理的值。现在，已通过绘制顶点融合纹理。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-C9D22021-652D-4041-AE96-BDFB5D607DF6.png) <!-- baize:img-hook downloaded=false reason="正文 1456 字 ≥300，非承重" -->

纹理由 www.cgtextures.com 提供。

## 相关主题

- [使用 ShaderFX 编辑器构建 Stingray 基于物理的着色器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-DC9B7CAC-B949-4C37-99D0-A1B3D8FD1EC9.htm)

- [将顶点颜色添加到 Stingray 基于物理的 ShaderFX 网络](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-6D54F764-0105-40CC-910E-53EAF37BBF0A.htm)
