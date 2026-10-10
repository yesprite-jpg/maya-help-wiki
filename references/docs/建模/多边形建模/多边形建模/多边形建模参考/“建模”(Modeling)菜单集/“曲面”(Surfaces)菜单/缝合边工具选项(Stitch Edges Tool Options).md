# 缝合边工具选项(Stitch Edges Tool Options)

使用以下选项可设置在选择“曲面 > 缝合 > 缝合边工具”(Surfaces > Stitch > Stitch Edges Tool)时发生的情况。

#### 融合(Blending)

“位置”(Position)可缝合位置连续性的曲面。

“切线”(Tangent)可缝合切线连续性的曲面。

**注**

“缝合工具”(Stitch Tool)不会更改 CV 或 UV 参数化的数量。它可以修改 CV 位置，使其尽可能拥有更多的位置，且尽可能保持切线连续性。

#### 设置边的权重(Weighting on Edge)

在缝合边之前，两个选定等参线将在加权模式中平均化。两个曲面均会修改，以便沿该平均化的等参线与切线连续性会合。可以将权重指定给选定等参线。

默认情况下，权重 1.0 和 0.0 已指定给第一个和第二个选定等参线。从效果上来说，这会修改第二个曲面上的 CV，使该曲面具有第一个曲面的切线连续性。如果将非零权重指定给两个选定等参线，则两个曲面上的 CV 均会修改，以实现切线连续性。

![图：在缝合边之前，两个选定等参线将在加权模式中平均化。两个曲面均会修改，以便沿该平均化的等参线与切线连续性会合。可以将权重指…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-46E6BAB3-2016-4751-9586-E6D466400B95.png) <!-- baize:img-hook downloaded=false reason="正文 1075 字 ≥300，非承重" -->

在构建历史启用的情况下，可以在创建缝合之后修改权重。选择在缝合期间创建的“avgCurve”节点，然后显示“属性编辑器”(Attribute Editor)。

可以拖动操纵器选择性地沿等参线改变要一起加权的部分。这些部分是两个曲面中要在缝合在一起的部分。

**注**

提示：

若要查看根据平均节点计算的曲线，请在平均节点上选择“显示操纵器工具”(Show Manipulator Tool)。该操纵器仅提供视觉线索，且无法进行编辑。

#### 沿边采样数(Samples Along Edge)

缝合曲面的 CV 是通过沿曲面对边进行采样来确定的，其中，曲面是指需要针对切线连续性进行修改的曲面。可以明确地设定“沿边采样数”(Samples Along Edge)，以闭合缝合曲面上的任何位置间隙。采样数越高，性能越慢。这与“通道盒”(Channel Box)和“属性编辑器”(Attribute Editor)中的“stitchSrf”节点的“步长计数”(Step Count)相同。

#### 层叠缝合节点(Cascade Stitch Node)

如果“层叠缝合节点”(Cascade Stitch Node)已启用，则缝合操作会忽略之前在曲面中进行的任何缝合操作。如果禁用，且曲面中已执行缝合操作，则将使用上一个操作中的缝合节点。默认设置为启用。

#### 保持原始(Keep Original)

如果“保持原始”(Keep Original)已启用，则将在原始输入曲面上创建缝合曲面。通过这种方式，如果对结果不满意，则可以移动结果曲面，并使用不同选项设置重新缝合新曲面。

如果禁用，则缝合操作将替换正在缝合的曲面。

## 相关主题

- [手动缝合曲面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-1E19646E-F32D-4E6F-A080-34770663BED6.htm)
