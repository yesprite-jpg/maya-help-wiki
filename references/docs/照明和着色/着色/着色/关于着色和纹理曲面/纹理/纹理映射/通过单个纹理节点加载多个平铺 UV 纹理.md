# 通过单个纹理节点加载多个平铺 UV 纹理

UV 平铺功能允许您使用单个“文件”(File)纹理节点加载、预览和渲染包含对应于 UV 布局中栅格平铺的多个图像的纹理。 这意味着您可以打开和显示通过 3D 绘制应用程序（如 Mudbox）制作的超高分辨率纹理，以及提供使用 UV 集的更有效替代方法。

使用 UV 平铺时，纹理将作为平铺显示在 UV 空间中。在 UV 空间中，每个平铺的宽度和高度为单位宽，即 (1x1)。但是，它并非仅限于 0 到 1 的 UV 值。相反，平铺在 U 向维度和 V 向维度中的跨度可以为 0 到 1、3 到 4 或者 10 到 11。

请参见 [UV 平铺](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F7699459-D36A-4443-BA7E-883C241DE5E9)。

**注**

提示：

您可以在

Viewport 2.0

中可视化 UV 平铺。

加载和显示多平铺 UV 纹理

1. 将[文件纹理节点](../../../着色引用/着色节点/纹理节点概述/2D%20纹理/文件%28File%29纹理节点.md)连接到着色网络。

2. 在“文件”(File)节点的“图像名称”(Image Name)属性中加载第一个 UV 平铺。

  可以使用属性编辑器或者使用 Hypershade 中的特性编辑器执行此操作。（另请参见[在 Hypershade 特性编辑器中查看属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-51DFC2E3-7D78-41C7-BE9A-489C181D8DF5.htm)）。

3. 选择下列“UV 平铺模式”(UV Tiling)之一：

  - “0 型 (Zbrush)”(0-based (Zbrush)) - 如果 UV 坐标起点为 0，请选择此选项

    某些应用程序（例如，Zbrush）使用左下角 UV 坐标对 UV 平铺进行编号。即，UV 平铺 [0,0]x(1,1) 将在其文件名中使用 u0_v0。

  - “1 型 (Mudbox)”(1-based (Mudbox)) - 如果 UV 坐标起点为 1，请选择此选项

    某些应用程序（例如，Mudbox）使用右上角 UV 坐标对 UV 平铺进行编号。即，UV 平铺 [0,0]x(1,1) 将在其文件名中使用 u1_v1。

  - UDIM (Mari) - 如果 UV 坐标使用公式 1000+(u+1+v*10) 表示为四位数，请选择此选项

  - “显式平铺”(Explicit Tiles) - 选择此选项可分别加载每个平铺并显式输入 U 值和 V 值。对于每个平铺，输入与纹理相对应的左下角 UV 坐标的值。

  **注**

  上面列出的命名约定为每个应用程序的默认设置。可以使用其他约定。

  Maya 在文件路径中使用标记来解析每个纹理的 UV 坐标。

  在选择“UV 平铺模式”(UV Tiling Mode)后，“图像名称”(Image Name)字段将使用标记进行更新，这些标记指示 Maya 如何解析文件名：

  - “0 型 (Zbrush)”(0-based (Zbrush)) - u<u>_v<v>

  - “1 型(Mudbox)”(1-based (Mudbox)) - u<U>_v<V>

  - “UDIM (Mari)” - <UDIM>

  解析 UV 坐标后，Maya 指示在指定路径中找到的 UV 平铺数量。

  **注**

  提示：

  如果将鼠标悬停在指示发现的 UV 平铺数量的文本上，则显示工具提示，指示涉及的 UV 范围。

  如果您当前位于纹理模式，或此时切换到纹理模式，则 Maya 不会在 Viewport 2.0 中自动预览 UV 平铺纹理。若要执行此操作，您必须手动生成纹理预览。

4. 从下拉列表中选择一种“预览质量”(Preview Quality)。

  如果您有一个较大的纹理集，则您可能想要选择较低质量预览以减少纹理内存的使用。如果您使用的是非常大的纹理集，或者，如果出于任何其他原因，您不希望预览纹理，则可以选择“禁用预览”(Disable Preview)。

  **注**

  在

  “Viewport 2.0”

  中，UV 平铺纹理将烘焙到单个纹理以用于预览。此纹理的分辨率取决于您选择的

  “预览质量”(Preview Quality)

  ：

  - 高质量(High Quality)：4K

  - 中等质量(Medium Quality)：2K

  - 低质量(Low Quality)：1K

5. 单击“生成预览”(Generate Preview)并按 6 以使用纹理模式可视化平铺（如果尚未处于纹理模式）。

  如果在场景中有多个 UV 平铺集，可以通过选择“渲染器 > Viewport 2.0”(Renderer > Viewport 2.0) > ![图：如果在场景中有多个 UV 平铺集，可以通过选择“渲染器 Viewport 2.0”(Renderer Viewport …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3009 字 ≥300，非承重" -->，然后单击“重新生成所有 UV 平铺预览纹理”(Regenerate All UV Tile Preview Textures)生成所有 UV 平铺集的预览。此全局设置将遵循为每个文件节点保存的“预览质量”(Preview Quality)设置。

  如果自上次您单击“生成预览”(Generate Preview)后您的纹理已更改（例如，已重新加载纹理），则按钮将指示“生成预览*”(Generate Preview*)（红色）提示您重新生成预览。此功能使您在等待新纹理预览前，可以多次更改纹理设置。

默认情况下，第一次打开场景时，Maya 不会在 Viewport 2.0 中加载 UV 平铺纹理。您可以选择在场景加载时在“Viewport 2.0”中预览 UV 平铺，方法是：选择“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)打开“首选项”(Preferences)窗口，并在“显示”(Display)部分中启用“场景加载时生成 UV 平铺预览”(Generate UV tile previews on scene load)。如果不修改 UV 平铺，您可以始终在场景加载时自动预览纹理。但是，如果修改 UV 平铺，您必须通过单击“生成预览*”(Generate Preview*)再次手动重新生成预览。

您在“不支持的纹理类型的烘焙分辨率”(Bake Resolution for Unsupported Texture Types)（位于“渲染设置”(Render Settings)窗口）中的设置不会对显示分辨率有任何影响。

在选择“预览质量”(Preview Quality)设置后，基于“最大纹理分辨率”(Max Texture Resolution)设置（位于“Viewport 2.0 选项”(Viewport 2.0 Options)中）应用硬钳制。但是，如果平铺数据不是方形（即，分块线的行列比率小于 0.5 或大于 2），将忽略钳制。

## 自定义图像文件格式

如果图像文件名的自定义格式与可用的“UV 平铺模式”(UV Tiling Mode)不匹配，则您可以手动编辑标记，这样 Maya 就可以正确识别 UV 平铺序列。

1. 使用“图像名称”(Image Name)属性旁边的“浏览”(Browse)按钮加载第一个 UV 平铺。

2. 选择“0 型 (Zbrush)”(0-based (Zbrush))或“1 型 (Mudbox)”(1-based (Mudbox)) UV 平铺模式，然后编辑标记（如有需要）。

## 将单独的图像加载为 UV 平铺

您可以分别加载图像，并分别指定每个图像的 U 坐标和 V 坐标。

1. 选择“文件”(File)节点。

2. 在“属性编辑器”(Attribute Editor)中，使用“图像名称”(Image Name)属性加载第一个 UV 平铺。

3. 将“UV 平铺模式”(UV Tiling Mode)设置为“显式平铺”(Explicit Tiles)。

4. 输入加载的第一个纹理的 U 坐标和 V 坐标。

  输入与纹理相对应的左下角 UV 坐标的值。

5. 单击“添加显式分片”(Add Explicit Tile)添加下一个纹理并输入其对应的 UV 坐标。

6. 根据需要为剩余的纹理重复上述步骤。

## 将图像序列与 UV 平铺结合使用

当您选择“使用图像序列”(Use Image Sequence)选项时，Maya 会在“图像名称”(Image Name)下通过标记指明将文件名的哪一部分解释为帧编号。例如：

文件名.u<u>_v<v>_<f>.tif

在此示例中，第一个标记代表 U 值，第二个标记代表 V 值，第三个标记 <f> 代表*帧编号*。

对于每个帧，Maya 都会指明其在指定路径找到的 UV 平铺数量。
