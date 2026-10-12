# 使用“组件混合”(Component Swizzle)为 Stingray 基于物理的着色器输入提供不同的顶点颜色通道

通过 Stingray PBS 节点创建的 ShaderFX 网络使用混合，以允许 xyz 的单个组件采用任何 xyz 组件的值。

在 ShaderFX 中，默认情况下 RGB 值连接到 XYZ。默认情况下，X 对应于 R，Y 对应于 G，Z 对应于 B。但是，您可以提供 xxx 或 rrr 的 float3 输入，即红色通道用于 float3 的全部 3 个浮点值。也可以提供 rgg 或 xyy，其中红色通道用于第一个浮点，绿色用于第二个和第三个浮点。

通过自定义“标准基础”(Standard Base)节点的不同通道输入（如基础颜色和不透明度），创建不同的着色器效果。

## 设置“组件混合”(Component Swizzle)值

1. 在 Stingray PBS 节点的 ShaderFX 编辑器中，单击要在“标准基础”(Standard Base)节点上调整的属性；例如“基础颜色”(Base Color)。

  此时将显示其属性编辑器。

2. 在“组件混合”(Component Swizzle)字段中，输入要输入到此属性的通道。

如果“组件混合”(Component Swizzle)字段为空，则使用默认值（例如，对 xyz 使用 rgb）。

以下示例演示了“基础颜色”(Base Color)输入为 xyz (rgb) 与“基础颜色”(Base Color)输入为 rrr 时的不同效果。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-18AE63AD-CA7A-46A0-8BFB-695E75E8C0E0.png) <!-- baize:img-hook downloaded=false reason="正文 1001 字 ≥300，非承重" -->

## 示例：将顶点颜色绿色通道连接到“环境光遮挡”(Ambient Occlusion)

1. 将“颜色贴图”(Color Map)的“RGBA”输出连接到“标准基础”(Standard Base)的“基础颜色”(Base Color)输入。

  颜色贴图将为模型提供基础颜色。

2. 将顶点颜色的“RGBA”输出连接到“标准基础”(Standard Base)的“环境光遮挡”(Ambient Occlusion)输入。

  float3 输出将自动转化为浮点，且默认情况下使用 r 通道。

3. 在“标准基础”(Standard Base)节点中选择“环境光阻挡”(Ambient Occlusion)通道，然后在属性编辑器的“组件混合”(Component Swizzle)属性中输入 g。

在此示例中，在恐龙尾巴的各部分（绘制为绿色）上可看到环境光遮挡。

顶点颜色的 r 和 b 通道现在可以连接到其他输入；例如，r 表示金属，b 表示粗糙度。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-CEA60350-6CC4-42CB-BFAA-CF5C22FFC018.png) <!-- baize:img-hook downloaded=false reason="正文 1001 字 ≥300，非承重" -->

## 相关主题

- [创建 Stingray 基于物理的着色器](../../创建基于物理的%20Stingray%20着色器.md)

- [使用 ShaderFX 编辑器构建 Stingray 基于物理的着色器](../使用%20ShaderFX%20编辑器构建基于物理的%20Stingray%20着色器.md)

- [示例工作流程：使用 Stingray 基于物理的着色器融合两个纹理](../示例工作流程：使用基于物理的%20Stingray%20着色器融合两个纹理.md)
