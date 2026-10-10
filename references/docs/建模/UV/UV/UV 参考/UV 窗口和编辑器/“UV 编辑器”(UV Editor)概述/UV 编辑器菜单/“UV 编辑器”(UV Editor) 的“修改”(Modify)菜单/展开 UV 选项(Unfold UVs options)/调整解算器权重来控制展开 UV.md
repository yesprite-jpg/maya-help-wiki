# 调整解算器权重来控制展开 UV

以下示例演示更改“展开 UV 选项”(Unfold UVs options)中的[“权重解算器朝向”(Weight solver towards)](../展开%20UV%20选项%28Unfold%20UVs%20options%29.md#GUID-039FFDA5-3AC5-4CCF-A53E-546CCA6439FC__WS1A9193826455F5FF-4F542F6211C79DEA861-2999)选项以及固定和对齐 UV 如何帮助控制产生的展开 UV 布局和纹理映射。

**注**

此示例使用

“旧版”(Legacy)

展开算法。请参见

“展开 UV”(Unfold UVs)选项

。

- 桶状的多边形对象已使用棋盘格纹理进行纹理映射。将“权重解算器朝向”(Weight solver towards)选项设定为 0（默认值）的情况下执行初始展开操作，最初会在“UV 纹理编辑器”(UV Texture Editor)中产生锥化的 UV 布局。生成的纹理贴图在对象上是歪曲和扭曲的。

  ![图：桶状的多边形对象已使用棋盘格纹理进行纹理映射。将“权重解算器朝向”(Weight solver towards)选项设定…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-76341834-B0D4-4F8E-AB70-BAB39CDFBC58.png) <!-- baize:img-hook downloaded=false reason="正文 553 字 ≥300，非承重" -->

- 另一个展开操作在“权重解算器朝向”(Weight solver towards)选项设定为 0.6 时执行。这会以更全局化的方式展开 UV 并减弱之前出现的锥化效果。UV 布局的可预测性更强，但是 UV 网格的左下角会出现一些 UV 重叠，从而导致纹理上出现重叠。

  ![图：另一个展开操作在“权重解算器朝向”(Weight solver towards)选项设定为 0.6 时执行。这会以更全局…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D6DD3B32-4DFD-45D9-84BD-F06009E3018A.png) <!-- baize:img-hook downloaded=false reason="正文 553 字 ≥300，非承重" -->

- 通过重新定位和固定 UV 网格的角点并在“权重解算器朝向”(Weight solver towards)设置为 0 时执行另一展开操作，可进一步松弛 UV 并移除重叠区域。

  ![图：通过重新定位和固定 UV 网格的角点并在“权重解算器朝向”(Weight solver towards)设置为 0 时执…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F667F69E-6D23-4E3F-8351-5F16D809F3A7.png) <!-- baize:img-hook downloaded=false reason="正文 553 字 ≥300，非承重" -->

- UV 的顶部和底部行将会对齐，并在“权重解算器朝向”(Weight solver towards)选项设置为 0 且固定边界的情况下执行最终的展开操作。

  ![图：UV 的顶部和底部行将会对齐，并在“权重解算器朝向”(Weight solver towards)选项设置为 0 且固定…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-89B8FC1A-22B3-46B2-A9A5-0124671C91E0.png) <!-- baize:img-hook downloaded=false reason="正文 553 字 ≥300，非承重" -->
