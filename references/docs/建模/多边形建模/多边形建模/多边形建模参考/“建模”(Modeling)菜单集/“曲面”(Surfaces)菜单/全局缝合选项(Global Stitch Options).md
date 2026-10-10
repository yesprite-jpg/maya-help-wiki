# 全局缝合选项(Global Stitch Options)

使用以下选项可设置在选择“曲面 > 缝合 > 全局缝合”(Surfaces > Stitch > Global Stitch)时发生的情况。

### 缝合角点(Stitch Corners)

“缝合角点”(Stitch Corners)选项指定曲面角点缝合到相邻的角点或曲面边的位置。无论选择哪个选项，仅当这些点处于“最大间隔”(Max Separation)距离内时，才会进行缝合。

缝合发生在两个角点之间的某个点处，或者发生在一个角点与曲面边上的一个点之间的某个点处。角点缝合到边上的一个点而不是缝合到角点的情况下，下列选项会可用。

#### 最近点(Closest Point)

将角点缝合到边上的最近点。

#### 最近结(Closest Knot)

将角点缝合到边上的最近结。

#### 禁用(Off)

不执行显式角点缝合。

![图：不执行显式角点缝合。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-70902113-0584-4244-82A3-52F9FB72E45C.png) <!-- baize:img-hook downloaded=false reason="正文 2170 字 ≥300，非承重" -->

### 缝合边(Stitch Edges)

“缝合边”(Stitch Edges)选项指定相邻边缝合到一起的位置。无论选择哪个选项，仅当这些边处于“最大间隔”(Max Separation)距离内时，才会进行缝合。缝合会沿着边之间的中点进行。

#### 最近点(Closest Point)

缝合边上的最近点，同时忽略边之间的参数化差异。因为面片数可能不同，可能不会发生精确的接合。

#### 匹配参数(Match Params)

缝合曲面边上的点，这些点沿着每条边具有相等的 UV 增量。忽略跨度数。若要使用该类型的缝合获得尽可能最好的拟合，请确保两条边具有相同的 UV 值、相同的跨度数以及排成一行的结。

#### 禁用(Off)

不执行显式边缝合。如果启用其中一个“缝合角点”(Stitch Corners)选项（而不是“禁用”(Off)）并将“缝合边”(Stitch Edges)设定为“禁用”(Off)，那么会将角点缝合到一起，而不是将边缝合到一起。

![图：不执行显式边缝合。如果启用其中一个“缝合角点”(Stitch Corners)选项（而不是“禁用”(Off)）并将“缝合…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-A887FDE9-FD5F-4A8B-9C4E-941BC6CF8648.png) <!-- baize:img-hook downloaded=false reason="正文 2170 字 ≥300，非承重" -->

### 缝合平滑度(Stitch Smoothness)

选择接合的等参线显示的方式。

#### 切线(Tangents)

弯曲等参线，使它们在遇到缝合的边的位置垂直。这样可在曲面之间获得最佳的连续性。

#### 法线(Normals)

不要求等参线垂直，尽管曲面仍平滑地接合。

#### 禁用(Off)

禁用平滑，且不保证边区域相切。

![图：禁用平滑，且不保证边区域相切。 注： 可以按任意组合使用“缝合角点”(Stitch Corners)、“缝合边”(Sti…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-A5381323-FE68-4253-B414-55DB356BEEC1.png) <!-- baize:img-hook downloaded=false reason="正文 2170 字 ≥300，非承重" -->

**注**

可以按任意组合使用“缝合角点”(Stitch Corners)、“缝合边”(Stitch Edges)和“缝合平滑度”(Stitch Smoothness)来创建各种缝合效果。如果“缝合平滑度”(Stitch Smoothness)为“禁用”(Off)，但其中一个“缝合边”(Stitch Edges)选项已启用，那么这些边将接触，但这些边之间的缝合的区域可能不平滑。

#### 缝合部分边(Stitch Partial Edges)

如果启用该选项，Maya 会接合处于“最大间隔”(Max Separation)距离内的边对的任何部分。相同的一对边可能会因此而沿着其长度接合和分离许多次。如果禁用该选项，那么沿着这些边的任何点超出“最大间隔”(Max Separation)距离时，就不会缝合边对的任何部分。

![图：如果启用该选项，Maya 会接合处于“最大间隔”(Max Separation)距离内的边对的任何部分。相同的一对边可能…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-C0DECF32-E053-402C-A6AE-5A9C1E2CA439.png) <!-- baize:img-hook downloaded=false reason="正文 2170 字 ≥300，非承重" -->

不必要时，不要启用“缝合部分边”(Stitch Partial Edges)。该选项需要额外的处理时间。

#### 最大间隔(Max Separation)

指定要缝合曲面边和角点，它们必须离得有多近。值较大时，缝合的点数可能会超出需要缝合的点数。值较小时，可能会导致缝合操作失败。

#### 修改阻力(Modification Resistance)

指定缝合曲面时曲面 CV 保持其位置的程度。增大该值可以平滑缝合的曲面中的波状程度。不要将该值增大太多，否则曲面接合可能会不平滑。

#### 采样密度(Sampling Density)

设定 Maya 在缝合操作过程中沿着每条边采样的点数。增大“采样密度”(Sampling Density)可能会改进拟合，但会减慢缝合操作。从最小值 (1) 开始，且仅当拟合较差时增大该值。值超过 5 通常是不必要的。

#### 锁定曲面(Lock surfaces)

“属性编辑器”(Attribute Editor)的“锁定曲面”(Lock surface)区域显示两个或更多名为*“锁定曲面n”(Lock surface n)*的属性。其中 *n* 代表其中一个缝合的曲面。例如，“锁定曲面1”(Lock surface 1)、“锁定曲面2”(Lock surface 2)等等。

如果为任何曲面启用该选项，该曲面都不会更改在结果缝合曲面中的形状。而缝合到该曲面的曲面已改变。

如果为两个相邻的缝合曲面启用该选项，那么它们可能会显示为未缝合。它们仍属于 globalStitch 节点的一部分，这样可以为任一曲面禁用“锁定曲面”(Lock surface)，且会再次显示缝合。

#### 保持原始(Keep Originals)

如果“保持原始”(Keep Originals)已启用，则会在原始输入曲面上创建缝合曲面。这样，如果对结果不满意，可以移动结果曲面，并使用不同的选项设置来重新缝合新曲面。

如果已禁用，则缝合操作会替换被缝合的曲面。

**注**

缝合曲面之后，可以将原始曲面移动到

“最大间隔”(Max Separation)

范围之外，而不会断开缝合。如果将曲面分离得太远，则可能会出现连续性和扭曲方面的损失。

如果在原始曲面离得很远的情况下编辑 globalStitch*n* 节点上的属性，那么将基于曲面的新位置重新计算缝合。先前缝合的边可能无法产生结果。请将曲面返回到其原始位置，然后再编辑指定如何缝合曲面的属性。

## 相关主题

- [将多个曲面缝合到一起](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-5F19A8E1-E3D7-46AD-A39C-02E1F37678C7.htm)
