# 导出 Stingray 基于物理的着色器

可以使用 FBX 导入和导出 Stingray 基于物理的着色器 (PBS)。着色器和已导入的图表的外观是相同的，包括所有的输入连接和节点。

**注**

如果着色器使用自定义预设，则还导出预设着色器图表。（请参见

为 Stingray PBS 着色器创建自定义预设

。）

导出对象及其着色器

1. 选择对象，然后选择“文件 > 导出当前选择”(File > Export Selection)。

2. 从“文件类型”(Files of type)下拉列表中选择“FBX 导出”(FBX export)，然后输入文件的名称并导出对象。

仅导出自定义预设着色器曲线图

1. 在“ShaderFX”编辑器中，选择“文件 > 导出图表”(File > Export Graph)。

2. 在“文件类型”下拉列表中选择“.sfx”。

3. 将文件保存到所需的项目目录中（您计划稍后导入着色器的位置）。

  现在，您可以直接在 Maya、Maya LT 或 3ds Max 中加载该着色器。

## 相关主题

- [创建 Stingray 基于物理的着色器](../创建基于物理的%20Stingray%20着色器.md)

- [使用 ShaderFX 编辑器构建 Stingray 基于物理的着色器](使用%20ShaderFX%20编辑器构建基于物理的%20Stingray%20着色器.md)
