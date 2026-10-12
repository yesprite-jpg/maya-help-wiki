# 使用 ShaderFX 编辑器构建 ShaderFX 或 Stingray 基于物理的着色器网络

构建 ShaderFX 或 Stingray 基于物理的着色器网络时，可以在 ShaderFX 编辑器中执行以下操作。

## 创建节点

| 目标 | 操作 |
|---|---|
| 创建节点。 | 执行下列操作之一： 在 ShaderFX 编辑器的工作区中单击鼠标右键，并从标记菜单中选择“硬件着色器节点”(Hw Shader Nodes)（对于“Shaderfx 着色器”(Shaderfx Shader)）或“添加”(Add)（对于“Stingray PBS”），然后从纹理、工具、数学节点等中进行选择。 从“节点浏览器”(Node Browser)中选择要创建的节点，然后将其拖放到工作区。使用搜索字段即可轻松地找到所需的节点。 创建节点后，可以将它连接到现有的 TraditionalGameSurfaceShader 和“材质”(Material)节点（对于“Shaderfx 着色器”(Shaderfx Shader)）或“标准基础”(Standard Base)节点（对于 Stingray PBS）。 |
| 创建高级数学和编码节点。 注： 仅适用于“Shaderfx 着色器”(Shaderfx Shader)网络。 | 从 ShaderFX 菜单栏中选择“设置 > 切换高级模式”(Settings > Toggle Advanced Mode)以启用高级模式。 高级模式可以提供其他节点（例如“Bool AND”和“If Else”等。 |

## 连接节点

| 目标 | 操作 |
|---|---|
| 连接节点。 | 拖动以在输出和输入属性之间创建连接线。 着色图表的结果将在“ShaderFX”编辑器和场景视图中自动更新。 |

## 选择节点

| 目标 | 操作 |
|---|---|
| 选择节点及其上游节点。 | 按住 Ctrl 键和 Shift 键并单击。 |
| 从选择中删除节点。 | 按住 Ctrl 键并单击。 |
| 将节点添加到选择项。 | 按住 Shift 键并单击。 |

## 删除节点

| 目标 | 操作 |
|---|---|
| 删除节点。 | 选择节点并按 Delete。 注： 在“Shaderfx 着色器”(Shaderfx Shader)网络中，无法删除“材质”(Material)节点和 TraditionalGameSurfaceShader 节点（默认情况下已创建），除非已启用高级模式（从 ShaderFX 菜单栏中选择“设置 > 切换高级模式”(Settings > Toggle Advanced Mode)）。 如果删除这些节点，则着色器在场景视图中不执行渲染操作，您必须先创建新材质或表面着色器并将其并连接到节点网络，然后才能执行渲染操作。 您可以通过转到组视图，选择组节点，然后选择“属性编辑器”(Attribute Editor)中的“仅可在高级模式下删除”(Deletable only in Advanced mode)，设定仅可在高级模式下删除的任何组节点。 |

## 覆盖节点

**注**

仅适用于

“Shaderfx 着色器”(Shaderfx Shader)

网络。

默认情况下，您不能覆盖 Maya 附带的节点。

若要执行此操作，必须选择“设置 > 覆盖系统节点”(Settings > Overwrite System Nodes)。

**注**

不建议覆盖 Maya 提供的系统节点。

## 调整节点特性

您可以通过“属性编辑器”(Attribute Editor)调整图表节点的属性。或者，您可以选择“ShaderFX”菜单栏中的“设置 > 显示特性面板”(Settings > Show Property Panel)，以在“ShaderFX”编辑器中显示特性，而无需打开“属性编辑器”(Attribute Editor)。

调整 Stingray PBS 节点的特性时，必须选择节点上的单个属性。与“Shaderfx 着色器”(Shaderfx Shader)节点不同，根据单击的节点属性，为 Stingray PBS 节点显示的特性可能发生变化。例如，选择“标准基础”(Standard Base)节点的“基础颜色”(Base Color)输入时，在属性编辑器中将显示与选择“不透明度阈值”(Opacity Threshold)时不同的一组设置。

## 将预览样例保存到纹理

选择一个节点，然后单击鼠标右键 (![图：选择一个节点，然后单击鼠标右键 () 并选择“工具 将选定样例保存到图像”(Tools Save Selected Sw…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-C0C1B9D8-C98F-4091-9802-1D60B6077FED.png) <!-- baize:img-hook downloaded=false reason="正文 1995 字 ≥300，非承重" -->) 并选择“工具 > 将选定样例保存到图像”(Tools > Save Selected Swatches to Images)，将预览样例烘焙为 2kx2k 纹理。“ShaderFX” 编辑器中会出现一个工具提示，指示您要将样例保存到的位置。您也可以同时选择多个节点，并同时保存它们的样例。

此外，您还可以将几何体的展开 UV 烘焙到纹理。要执行此操作，请选择节点，单击鼠标右键（![图：此外，您还可以将几何体的展开 UV 烘焙到纹理。要执行此操作，请选择节点，单击鼠标右键（），然后选择“工具 将选定样例保…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-C0C1B9D8-C98F-4091-9802-1D60B6077FED.png) <!-- baize:img-hook downloaded=false reason="正文 1995 字 ≥300，非承重" -->），然后选择“工具 > 将选定样例保存到 UV 展开图像”(Tools > Save Selected Swatches to UV-unwrapped Image)。

## 隐藏节点浏览器

“节点浏览器”(Node Browser)创建节点方便快捷。但是，如果您希望增加工作区中的可用空间来创建着色器图表，可以在“设置”(Settings)菜单中禁用“节点浏览器”(Node Browser)，以隐藏节点浏览器。然后，您就可以通过以下方式创建节点：在工作区中单击鼠标右键 (![图：“节点浏览器”(Node Browser)创建节点方便快捷。但是，如果您希望增加工作区中的可用空间来创建着色器图表，可以…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-339814BD-5F9D-4AF0-AD24-9C56C81EB765.png) <!-- baize:img-hook downloaded=false reason="正文 1995 字 ≥300，非承重" -->)，然后从标记菜单创建节点。
