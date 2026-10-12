# 在 ShaderFX 中使用图形节点添加开关

当“切换高级模式”(Toggle Advanced Mode)处于启用状态时，还可以创建“图形节点”(Graph Nodes)。

“图形节点”(Graph Nodes)可让您在图形中执行自定义决策。实际上，您可以创建一个开关，如下所示：

```text
if true
    do A
else
    do B
```

“布尔 AND”(Bool AND)和“路径方向”(Path Direction)都属于图形节点。

“布尔”(Bool)“图形节点(Graph Nodes)（“图形节点 > 代码控件 > 布尔 AND”(Graph Nodes > Code Control > Bool AND)、“图形节点 > 值 > 布尔值”(Graph Nodes > Values > Bool Value)等等）不应与“布尔”(Bool)值节点（“硬件着色器节点 > 值 > 布尔”(Hw Shader Nodes > Values > Bool)）混淆。

“布尔”(Bool)节点为着色器提供了 True 或 False 值，而布尔图形节点是一个开关，不为着色器提供值。

在本示例中，BoolValue 图形节点是用来控制 PathDir 采用输入 A 还是输入 B 的开关。如果布尔连接到 PathDir，则使用输入 A。如果非布尔连接到 PathDir，则使用输入 B。BoolValue 不直接为漫反射颜色提供任何值。

套接字中的 V 符号 ![图：套接字中的 V 符号 表示期望采用图形节点的输入（或图形节点的输出）。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-CA8AAF32-BF75-4393-89EA-747717F6649D.png) <!-- baize:img-hook downloaded=false reason="正文 826 字 ≥300，非承重" --> 表示期望采用图形节点的输入（或图形节点的输出）。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-D3F2E53D-F335-4350-8AC6-3352D7E65DCF.png) <!-- baize:img-hook downloaded=false reason="正文 826 字 ≥300，非承重" -->

在本示例中，颜色值乘以 1 或 0，具体取决于“布尔”(Bool)。当“布尔”(Bool)设置为 True 时，颜色将乘以 1，“漫反射颜色”(Diffuse Color)为黄色。当“布尔”(Bool)设置为 False 时，颜色将乘以 0，“漫反射颜色”(Diffuse Color)为黑色。因此，“布尔”(Bool)直接为着色器提供值。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-1395C3C0-4A08-4853-85A0-AE75D51813C1.png) <!-- baize:img-hook downloaded=false reason="正文 826 字 ≥300，非承重" -->

使用“图形节点”(Graph Nodes)的一个示例应用是启用或禁用不透明度。相对于不使用不透明度渲染着色器而言，使用不透明度渲染着色器较为昂贵，因此艺术工作者可以添加一个开关来轻松启用或禁用此设置，以加快预览渲染速度。
