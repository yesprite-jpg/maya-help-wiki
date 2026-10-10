# 在进行 UV 修改后更新纹理图像

“扭曲图像”(Warp Image)通过比较单个多边形网格上的两个 UV 集来修改纹理图像，并生成新的位图图像。若要使用该功能，必须指定一个源图像，以及模型的源和目标 UV 集，将从该模型引用 UV 以进行图像操纵。“扭曲图像”(Warp Image)生成新的目标图像作为结果。

通过在“建模”(Modeling)菜单集中或从“UV 编辑器”(UV Editor)中的“修改”(Modify)菜单中选择“UV > 扭曲图像”(UV > Warp Image)，可选择“扭曲图像”(Warp Image)。有关详细信息，请参见 [“扭曲图像”(Warp Image UV 选项](../UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/扭曲图像%20UV%20选项%28Warp%20Image%20UVs%20Options%29.md)。

在下列情况下，扭曲图像很有用：

- 纹理的 UV 已更改时，如果不希望手动为现有纹理贴图重新生成图像。“扭曲图像”(Warp Image)将计算应在何处重新定位像素，并更新纹理。已通过某种方式细化多边形网格上的 UV 时，“扭曲图像”很有帮助。例如，如果出于某种原因有必要切割、合并或优化 UV，那么在多边形对象上显示关联的纹理贴图的方式会作为一结果受到影响。

- 为纹理贴图中的关键区域创建更多纹理空间。例如，当对面进行纹理映射时，眼睛和嘴周围的 UV 可以缩放得更大，以便在最终的纹理贴图中将更多像素指定给这些区域。如果已在 UV 编辑器中缩放 UV 来优化纹理空间，那么可以扭曲关联图像以说明修改的 UV。

  **注**

  “扭曲图像”(Warp Image)

  可能不会生成像预期一样的高质量图像。可能有必要在图像上执行其他后期处理工作。

“扭曲图像”(Warp Image)需要两个 UV 集才能生成新图像（除了原始图像之外）。除非先前已经为多边形网格创建了一个 UV 集，否则强烈建议在“UV 编辑器”(UV Editor)中执行任何 UV 编辑之前，通过选择“UV 集 > 将 UV 复制到 UV 集 > 复制到新 UV 集”(UV Sets > Copy UVs to UV Set > Copy into New UV Set)，显式将纹理多边形网格的原始 UV 的一个副本另存为一个 UV 集。这样，在需要原始 UV 集时可以还原回去。

扭曲图像之前，多边形网格必须存在两个 UV 集：从其指定原始纹理的现有 UV 集，以及将被引用以修改或扭曲图像的第二个 UV 集。这两个 UV 集将被引用为“源 UV 集”(Source UV sets)和“目标 UV 集”(Destination UV sets)。

基于更新的 UV 扭曲图像

1. 执行下列操作之一：

  - 从“建模”(Modeling)菜单集中，选择“UV > 扭曲图像”(UV > Warp Image)。

  - 在“UV 编辑器”(UV Editor)中，选择“修改 > 扭曲图像”(Modify > Warp Image) > ![图：在“UV 编辑器”(UV Editor)中，选择“修改 扭曲图像”(Modify Warp Image) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1505 字 ≥300，非承重" -->。

  将显示“扭曲图像选项”(Warp Image Options)窗口。

2. 在“源图像名称”(Source Image Name)字段中为要扭曲的源图像键入文件名，或者浏览到相应位置并选择该文件名。

3. 在“新图像名称”(New Image Name)字段中为希望由“扭曲图像”(Warp Image)创建的新图像键入文件名，或者通过浏览来选择某个位置和图像名称。

4. 键入希望“扭曲图像”(Warp Image)功能引用的“源 UV 集”(Source UV sets)和“目标 UV 集”(Destination UV sets)的名称。如果忘记了 UV 集的名称，则可以通过选择“UV 集”(UV Sets)菜单并在下拉列表中查看 UV 集名称，在 UV 编辑器中查看这些名称。

5. 设定需要的所有剩余选项，然后单击“扭曲图像”(Warp Image)。

6. “扭曲图像”(Warp Image)会为新图像计算新像素位置，并将图像输出到指定的位置。

  若要查看曲面网格上的新纹理，必须编辑当前指定的着色器才能使用新图像。确保已将正确的 UV 集应用到网格，以便看到预期的结果。
