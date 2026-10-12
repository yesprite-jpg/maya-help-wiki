# 使用 StingrayPBS 创建透明材质

在将 StingrayPBS 材质应用到对象后，您可以采用以下两种方式之一将其设置为透明：

- 从 StingrayPBS“属性编辑器”(Attribute Editor)的“预设材质”(Preset Material)下拉列表中，选择“预设/Standard_Transparent”(presets/Standard_Transparent)预设。调整“不透明度”(Opacity)滑块以调整对象的透明度。

- 从 StingrayPBS“属性编辑器”(Attribute Editor)的“预设材质”(Preset Material)下拉列表中选择“自定义”(Custom)预设，以创建您自己的自定义图表，然后执行以下操作：

  1. 单击“打开 ShaderFX”(Open ShaderFX)打开 ShaderFX 编辑器，然后选择“标准基础”(Standard Base)节点。

  2. 从“融合模式”(Blend Mode)下拉列表中选择“透明”(Transparent)。

    **注**

    “透明褪色”(Transparent Fade)

    选项类似于

    “透明”(Transparent)

    选项，只是在透明度增加时，反射高光也会褪色。

  3. 在 ShaderFX 编辑器中创建“材质变量”(Material Variable)节点。

    选择“材质变量”(Material Variable)节点，然后在其“属性编辑器”(Attribute Editor)中，将“类型”(Type)设置为“标量”(Scalar)。为清楚起见，您可能还希望将该节点重命名为“透明度”。

  4. 将“透明度”(Transparency)节点的“结果”(Result)输出连接到“标准基础”(Standard Base)节点的“不透明度”(Opacity)输入。

    在 StingrayPBS“属性编辑器”(Attribute Editor)中调整“透明度”(Transparency)值。

  **注**

  提示：

  您也可以向透明 StingrayPBS 添加折射。请参见

  向基于物理的着色器添加折射
