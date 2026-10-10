# 将传统渲染层渲染为 PSD 格式

可以将所有层渲染为 Adobe Photoshop (PSD) 格式。

**注**

提供的

新渲染设置系统

现已取代传统渲染层，是 Maya 中的

默认系统

。这种新方法可简化复杂场景的管理以便进行渲染，如今已成为建议的工作流。有关详细信息，请参见

Maya 渲染设置

。

PSD 文件将在渲染过程中创建，场景中的每个层将作为该 PSD 文件中的单独层，所有融合模式的指定方式与这些模式在 Maya 文件中的指定方式相同。在 Adobe Photoshop 中打开该文件时，Maya 场景中的每个渲染层将在 PSD 中有相应的层和融合模式。

PSD 文件直接渲染到项目的图像目录中，不在子目录中。

渲染为 PSD 层文件格式

1. 在“渲染设置”(Render Settings)的“公用”(Common)选项卡中，从“图像格式”(Image Format)列表选择“分层 PSD(psd)”(PSD layered (psd))。

  ![图：在“渲染设置”(Render Settings)的“公用”(Common)选项卡中，从“图像格式”(Image Form…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-6C9E4133-CDF0-4413-9E83-930A67223C05.png) <!-- baize:img-hook downloaded=false reason="正文 401 字 ≥300，非承重" -->

  可以在 Adobe Photoshop 中打开创建的 PSD 文件。

  ![图：在“渲染设置”(Render Settings)的“公用”(Common)选项卡中，从“图像格式”(Image Form…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-741F26D1-738F-4FB2-A41B-8C71F53F1026.png) <!-- baize:img-hook downloaded=false reason="正文 401 字 ≥300，非承重" -->
