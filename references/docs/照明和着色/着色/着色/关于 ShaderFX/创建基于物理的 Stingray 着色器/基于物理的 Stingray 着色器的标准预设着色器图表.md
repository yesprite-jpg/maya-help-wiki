# 基于物理的 Stingray 着色器的标准预设着色器图表

为了避免重复创建相同的着色器图表以及降低游戏的速度，可以创建并保存预设着色器图表，然后在下次创建新的 Stingray PBS 时重用此预设。

Maya 随附了一组内置预设：

- Standard.sfx

- Standard_Mask.sfx

- Standard_Transparent.sfx

它们保存在以下位置：

- Maya 安装目录的 presets/ShaderFX/Scenes/StingrayPBS

创建时，Stingray PBS 节点使用内置的标准预设。这在其属性编辑器中得到反映，其中“预设材质”(Preset Material)设置为“预设/标准”(presets/Standard)。

标准预设接受六种不同类型的贴图的输入：放射性贴图、法线贴图、环境光遮挡等。有关详细信息，请参见[使用基于物理的 Stingray 着色器创建 ShaderFX 着色网络](../创建基于物理的%20Stingray%20着色器.md)。

您可以使用“预设材质”(Preset Material)下拉列表切换到 Standard_Mask 和 Standard_Transparent 预设。有关详细信息，请参见[将贴图连接到基于物理的 Stingray 着色器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-04F2FFA5-1797-4FEF-8A52-AEE00C47224E.htm)。

只要不更改着色器图表，着色器就可以继续使用此标准预设。可以在属性编辑器中更改任何属性；但是，如果单击“打开 ShaderFX”(Open ShaderFX)打开 ShaderFX 编辑器窗口，并添加、删除或重新连接节点，则必须创建“自定义”(Custom)预设。请参见[创建自定义预设](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-58228469-AF63-4D8D-B9B2-E014277F7A2B.htm)。

**注**

如果单击“打开 ShaderFX”(Open ShaderFX)打开 ShaderFX 编辑器窗口，则看到 ShaderFX 节点的网络。此图表反映在属性编辑器中看到的内容，即与各种贴图的连接和属性（如粗糙度和金属）的值。

ShaderFX 编辑器中的消息将通知您，该图表继承自预设；在本例中为内置预设。

可执行以下操作之一：

1. 编辑当前预设。

  编辑图表完成后，必须选择“文件 > 导出图表”(File > Export Graph)并在其现有的文件名之下保存预设以替换先前版本。

2. 基于预设图形创建新的着色器图表。

  在“ShaderFX 属性编辑器”(ShaderFX Attribute Editor)中单击“使唯一”(Make Unique)，“属性编辑器”(Attribute Editor)中的“预设材质”(Preset Material)下拉列表将设置为“自定义”(Custom)。

只要您尝试更改任何预设的图表，就会显示此消息，而不管它是自定义预设还是 Maya 随附的默认预设。

## 相关主题

- [使用基于物理的 Stingray 着色器创建着色网络](../创建基于物理的%20Stingray%20着色器.md)

- [使用 ShaderFX 编辑器构建基于物理的 Stingray 着色器](使用%20ShaderFX%20编辑器构建基于物理的%20Stingray%20着色器.md)
