# 优化 UV 间距

优化 UV 以平均分配 UV 在网格上的间距并修复扭曲的区域（重叠 UV）。例如，您可以结合使用“映射 UV 边界”(Map UV Border)命令来解开内部 UV。首先可以通过将 UV 映射到边界（方形或圆形）来开始，然后松弛 UV 以平均分配 UV 的间距。

使用优化命令松弛 UV

1. （可选）在“UV 编辑器”(UV Editor)工具栏中，启用扭曲着色器 (![图：（可选）在“UV 编辑器”(UV Editor)工具栏中，启用扭曲着色器 ()。请参见识别 UV 扭曲。 这会着色 UV…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-6EF6E8DD-7A18-428C-BFF5-7091B93B2C74.png) <!-- baize:img-hook downloaded=false reason="正文 533 字 ≥300，非承重" -->)。请参见[识别 UV 扭曲](../显示和选择%20UV/显示%20UV%20扭曲.md)。

  这会着色 UV 网格中挤压或拉伸的区域，从而便于识别需要优化的区域。

2. 选择要优化的 UV。

3. 在“UV 工具包”(UV Toolkit)中，选择“展开 > 优化”(Unfold > Optimize)（或者，从菜单栏中选择“修改 > 优化”(Modify > Optimize) > ![图：在“UV 工具包”(UV Toolkit)中，选择“展开 优化”(Unfold Optimize)（或者，从菜单栏中选择…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 533 字 ≥300，非承重" -->以调整选项）。

  **注**

  提示：

  您可以多次应用

  “优化”(Optimize)

  命令以反复松弛选定 UV。

  ![图：在“UV 工具包”(UV Toolkit)中，选择“展开 优化”(Unfold Optimize)（或者，从菜单栏中选择…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F643C686-AB74-4E83-92F7-51E793347B34.png) <!-- baize:img-hook downloaded=false reason="正文 533 字 ≥300，非承重" -->

4. 也可以选择“展开 > 优化工具”(Unfold > Optimize Tool)（或者，从菜单栏中选择“工具 > 优化”(Tools > Optimize)），然后使用笔刷以交互方式在要优化的特定区域上绘制。

  ![图：也可以选择“展开 优化工具”(Unfold Optimize Tool)（或者，从菜单栏中选择“工具 优化”(Tools…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-71DABCA5-FB35-4318-9B47-1EF4D3250F78.gif) <!-- baize:img-hook downloaded=false reason="正文 533 字 ≥300，非承重" -->

  **注**

  在

  “工具设置”(Tool Settings)

  中，可以快速在

  “展开”(Unfold)

  与

  “优化工具”(Optimize Tool)

  之间切换。

## 相关主题

- [优化 UV 选项(Optimize UVs options)](../UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/优化%20UV%20选项%28Optimize%20UVs%20options%29.md)
