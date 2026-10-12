# 为基于物理的 Stingray 着色器创建自定义预设

为了避免重复创建相同的着色器图表以及降低游戏的速度，可以创建并保存预设着色器图表，然后在下次创建新的 StingrayPBS 时重用此预设。

1. 创建 Stingray PBS 节点。

2. 在“属性编辑器”(Attribute Editor)中，从“预设材质”(Preset Material)下拉列表中选择“自定义”(Custom)。

  “父材质”(Parent Material)字段现在为空。

3. 在属性编辑器中单击“打开 ShaderFX”(Open ShaderFX)以打开 ShaderFX 编辑器窗口并构建 ShaderFX 图表。

  另请参见[使用 ShaderFX 编辑器构建基于物理的 Stingray 着色器](../使用%20ShaderFX%20编辑器构建基于物理的%20Stingray%20着色器.md)。

4. 从 ShaderFX 编辑器菜单中选择“文件 > 导出图表”(File > Export Graph)。

5. 将 .sfx 文件保存到以下位置之一：

  - 若要使预设仅对当前项目可用，则保存到项目目录，即 renderData\shaders 文件夹。

  - 若要使预设对所有项目全局可用，则保存到 \Documents\maya\ShaderFX\Scenes\StingrayPBS。

  （可选）重命名着色器节点，以便将 .fbx 文件导入到游戏引擎中时易于识别。

现在，当您重新启动 Maya 并创建新的 Stingray PBS 节点时，可以在“预设材质”(Preset Material)下拉列表中找到预设。

选择预设以重用相同的着色器图表。只要仅更改属性（在 Stingray PBS 属性编辑器中可见的属性）而不更改着色器图表，就可以继续使用该预设。

## 创使用现有着色器图表建自定义预设

  从“预设材质”(Preset Material)下拉列表中，选择所需预设以及要从中开始构建的着色器图表。

  单击“Stingray PBS 属性编辑器”(Stingray PBS > Attribute Editor)中的“使唯一”(Make Unique)。“Stingray PBS”节点不再指向以前选定的预设；但当您单击“打开 ShaderFX”(Open ShaderFX)时，仍保留该预设的着色器图表。

## 自定义预设的应用

### 父材质和子材质

包含着色器图表的材质称为父材质。

您可以基于父材质创建子材质。子材质从父材质继承着色器图表，因此也继承了其材质属性。

子材质可以修改父材质的属性；例如，其颜色值和纹理贴图。通常情况下，这些属性都将显示在 Stingray PBS “属性编辑器”(Attribute Editor)中。然而，子材质无法更改父材质的着色器图表。

如果在场景中具有一个由足球运动员组成的团队，则可以创建一个着色器图表以对其所有 T 恤着色。

创建一个具有预设着色器图表的父材质，然后基于该父材质创建 10 个子材质。每个子材质“属性编辑器”(Attribute Editor)都可以连接到表示运动员姓名和编号的不同纹理。由于 10 个子材质未连接着色器图表，因此计算它们要快得多，从而降低了对性能的瞬时干扰。

## 编辑现有的自定义预设

1. 在 StingrayPBS 着色器“属性编辑器”(Attribute Editor)中，从“预设材质”(Preset Material)下拉列表中选择要编辑的预设。

  单击“打开 ShaderFX”(Open ShaderFX)打开 ShaderFX 编辑器窗口。

  ShaderFX 编辑器中的消息将通知您，该图表继承自预设图表；在本例中为自定义预设。

3. 编辑图表，然后选择“文件 > 导出图表”(File > Export Graph)，并在其现有的文件名之下保存预设以替换先前版本。

## 相关主题

- [创建 Stingray 基于物理的着色器](../../创建基于物理的%20Stingray%20着色器.md)
