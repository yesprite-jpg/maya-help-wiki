# 使用 ShaderFX 编辑器构建基于物理的 Stingray 着色器

使用 ShaderFX 编辑器窗口和可用的 ShaderFX 节点构建 Stingray 基于物理的着色器。

有关可用的 ShaderFX 节点属性的参考信息，请参见 [Stingray 着色器节点参考](http://www.autodesk.com/stingray-help?contextId=shaders_ref_list_globals_cat)。

若要开始，请先从 Hypershade 或“指定新材质”(Assign New Material)窗口创建 Stingray PBS 节点。

## 创建预设着色器图表

创建着色网络时，可以将图表另存为预设，并在下次创建新的 Stingray PBS 节点时重用它。这样，就可以避免重复创建相同的着色器图表（可能会降低游戏的性能）。

若要创建新的自定义预设，请在 Stingray PBS属性编辑器的“预设材质”(Preset Material)下拉列表中选择 “自定义”(Custom)。请参见[为 Stingray 基于物理的着色器创建自定义预设](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-58228469-AF63-4D8D-B9B2-E014277F7A2B.htm)。

## 打开 ShaderFx 编辑着色器图表

单击“打开 ShaderFX”(Open ShaderFX)打开 ShaderFX 编辑器窗口。

像任何 ShaderFX 网络那样，创建和连接节点。在 ShaderFX 编辑器的工作区中单击鼠标右键，并从标记菜单中选择“添加”(Add)，然后从可用的节点中进行选择。或者，可以从“节点浏览器”(Node Browser)进行拖放。

**注**

虽然可以通过 ShaderFX 编辑器以与创建 ShaderFX 着色器网络类似的方式，创建 Stingray PBS 着色器网络，但是无法从前者保存 .sfx 文件，并在后者中使用它，反之亦然。虽然 ShaderFX 编辑器界面是类似的，但是可用节点集是不同的，因此不可互换。

## 在着色网络中创建浮点或颜色值

若要创建浮点，请创建“材质变量”(Material Variable)节点，然后从属性编辑器的“类型”(Type)下拉列表中选择“标量”(Scalar)、“向量 3”(Vector 3)或“向量 4”(Vector 4)，以分别创建浮点、浮点 3 或浮点 4。

若要创建颜色，请创建“材质变量”(Material Variable)节点，然后从属性编辑器的“类型”(Type)下拉列表中选择“向量 3”(Vector 3)，并从“向量”(Vector)属性颜色缸中选择一种颜色。

可以连接浮点 1-4 的任意组合；即，例如可以将浮点 3 端口连接到浮点 4 端口。

## 创建纹理贴图

若要创建纹理贴图，请创建“采样纹理”(Sample Texture)节点，并将它连接到文件纹理。

必须将“UV 集”(UV set)节点（例如 Texcoord 0）连接到“采样纹理”(Sample Texture)的“UV”属性，才能设置对象的纹理坐标。

以下简单网络演示如何使用“线性插值混合”(Linear Interpolate Mix)节点将两个纹理组合在一起，以及如何使用“标量”(Scalar)值控制每个纹理的贡献。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-D837C530-BB4E-44B5-B13E-E30FD72D2076.png) <!-- baize:img-hook downloaded=false reason="正文 2122 字 ≥300，非承重" -->

纹理由 www.cgtextures.com 提供

## 在属性编辑器中显示 ShaderFX 节点

可以将节点添加到图表，以便在关闭 ShaderFX 编辑器时，这些节点显示为 Stingray PBS 属性编辑器中的属性。这样，您就可以在重用同一自定义预设的同时调整这些属性，而无须打开 ShaderFX 编辑器。

这些节点包括：

- 采样立方体：接受立方体贴图纹理

- 采样纹理：接受 2D 纹理

- 材质变量

属性的名称取自节点的名称。因此，您可能希望更改节点的默认名称。在上面的示例中，默认名称 *texture map 5881422* 已更改为 *Grass*，以便在关闭 ShaderFX 编辑器时 *Grass*（而不是 *texture map 5881422*）显示为属性编辑器中的属性。若要重命名节点，请选择它，然后在属性编辑器的“名称”(Name)字段中输入新名称。

## 在着色器中调整照明

您可以限制影响着色器中阴影效果的灯光数量。着色器计算中包含大量灯光可能会降低着色器的性能，因此您可能需要设置一个合理的数量。在 ShaderFX 编辑器中选择“标准基础”(Standard Base)节点以显示其“属性编辑器”(Attribute Editor)，然后从“阴影光线数”(Num Shadow Lights)下拉列表选择从 1 到 3 之间的任意数字、不选择任何数字或全部选择。

此外，Stingray PBS 节点中的灯光强度以灯光停止数进行测量。如果您发现灯光强度太亮，可以在“标准基础”(Standard Base)节点的“属性编辑器”(Attribute Editor)中禁用“灯光强度(以停止数为单位)”(Light Intensity in Stops)选项。

## IBL 颜色编码

从“标准基础”(Standard Base)节点“属性编辑器”(Attribute Editor)的“IBL 编码”(IBL Encoding)下拉列表中，选择 IBL 立方体贴图（着色器中的全局漫反射和全局镜面反射纹理）使用的编码类型。

## 粗糙度和反射

在“标准基础”(Standard Base)节点“属性编辑器”(Attribute Editor)中启用“重映射粗糙度热度”(Remap Roughness hotness)选项，可降低镜面反射的热度。

## 相关主题

- [使用 ShaderFX 节点](../使用%20ShaderFX%20编辑器构建%20ShaderFX%20或%20Stingray%20基于物理的着色器网络.md)

- [ShaderFX 介绍性的采样工作流](../创建%20ShaderFX%20着色器/ShaderFX%20介绍性的采样工作流.md)

- [Stingray 基于物理的着色器的标准预设着色器曲线图](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-3DB877CD-2BA7-4D5C-ABB6-5292955D4600.htm)

- [为 Stingray 基于物理的着色器创建自定义预设](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-58228469-AF63-4D8D-B9B2-E014277F7A2B.htm)
