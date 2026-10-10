# polyBevel

## 多边形倒角历史

通过使用“通道盒”(Channel Box)或“属性编辑器”(Attribute Editor)编辑“polyBevel”节点上的下列属性，可以对倒角进行其他修改。

#### 作为分数偏移(Offset As Fraction)

选中时，倒角宽度将不会大于最短边。该选项会限制倒角的大小，以确保不会创建由内到外的倒角。

#### 世界空间(World Space)

为扩展对象应用了倒角并且启用了“世界空间”(World Space)时，偏移将忽略缩放并使用世界空间值。

#### Offset

指定倒角的大小：原始边与偏移面中心之间的距离。“偏移”(Offset)值范围限制在 0 和 5 之间。默认值为 0.20。“偏移”(Offset)仅在启用“世界空间”(World Space)时可用。

#### 分数(Fraction)

指定倒角的大小：原始边与偏移面中心之间的距离。“分数”(Fraction)值范围限制在 0 和 1 之间。默认值为 0.50。“分数”(Fraction)仅在启用“作为分数偏移”(Offset As Fraction)时可用。

**注**

如果使用

“分数”(Fraction)

属性，则在场景中更改工作单位时，倒角结果将不受影响。

#### 分段(Segments)

“分段”(Segments)值确定沿倒角多边形的边创建的分段数量。使用滑块或输入值可更改分段的数量。默认值为 1。

![图：“分段”(Segments)值确定沿倒角多边形的边创建的分段数量。使用滑块或输入值可更改分段的数量。默认值为 1。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-C73A540A-A91C-4253-B613-1233D815C30B.png) <!-- baize:img-hook downloaded=false reason="正文 1837 字 ≥300，非承重" -->

#### 平滑角度(Smoothing angle)

使用该选项可以指定进行着色时希望倒角边是硬边还是软边。

如果希望倒角边是软边，请将“平滑角度”(Smoothing Angle)设置为较大的值 (180)。如果希望倒角边是硬边，请将“平滑角度”(Smoothing Angle)设置为较小的值 (0)。

![图：使用该选项可以指定进行着色时希望倒角边是硬边还是软边。 如果希望倒角边是软边，请将“平滑角度”(Smoothing An…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F1359E4F-6DB2-4888-B7C8-925B7745E956.png) <!-- baize:img-hook downloaded=false reason="正文 1837 字 ≥300，非承重" -->

通常，如果在两个共享边之间的角度大于“平滑角度”(Smoothing Angle)属性所指定的值，那么将对倒角边进行着色以显示为硬边。默认的“平滑角度”(Smoothing Angle)值是 30 度。

#### 自动适配(Auto Fit)

启用该选项后，Maya 会自动确定倒角与对象的适应程度。

#### 圆度(Roundness)

默认情况下，Maya 会自动调整舍入来基于对象的几何体倒角对象。如果选择“自动适配倒角到对象”(Automatically fit bevel to object)，则会暗淡该选项。如果未选中“自动适配倒角到对象”(Automatically fit bevel to object)，请使用“圆度”(Roundness)滑块或输入值来圆化倒角边。可以将“圆度”(Roundness)设置为负数来创建向内的倒角。

#### 逐面做平面投影(Planar project per face)

会使用平面投影来投影每个原始面，以生成合并从倒角产生的新面的 UV。作为一个结果，可能会修改原始 UV 坐标的边界。

#### 保持原始边界(Preserve original boundaries)

系统会将 UV 合并到 UV 贴图中，该 UV 贴图会保持在倒角之前存在的 UV 边界。为获得最佳结果，请使用一个偶数值作为“分段”(Segments)的数量。

![图：系统会将 UV 合并到 UV 贴图中，该 UV 贴图会保持在倒角之前存在的 UV 边界。为获得最佳结果，请使用一个偶数值…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-0F296434-5449-4349-8EE1-2C9A4241C1EF.png) <!-- baize:img-hook downloaded=false reason="正文 1837 字 ≥300，非承重" -->

## 清理

#### 细分 N 边形(Subdivide Ngons)

作为使用多个分段执行倒角操作的结果，细分包含大量边的任何面。默认情况下会启用“细分 N 边形”(Subdivide Ngons)选项，且可以在“通道盒”(Channel Box)内交替地控制该选项。

![图：作为使用多个分段执行倒角操作的结果，细分包含大量边的任何面。默认情况下会启用“细分 N 边形”(Subdivide Ng…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-8D37292C-6775-4BA3-A5E1-5882600A19C3.png) <!-- baize:img-hook downloaded=false reason="正文 1837 字 ≥300，非承重" -->

#### 斜接角度(Mitering angle)

涉及某个相交的非倒角边时，控制如何将两个相交的倒角边接合到一起。通过在需要时设置“斜接角度”(Mitering Angle)值，可以指定是否要对最近倒角边进行斜接。

![图：涉及某个相交的非倒角边时，控制如何将两个相交的倒角边接合到一起。通过在需要时设置“斜接角度”(Mitering Angl…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D52AF9E7-4B14-48CE-9567-253D0F8DA137.png) <!-- baize:img-hook downloaded=false reason="正文 1837 字 ≥300，非承重" -->

如果两个倒角边之间的角度大于指定的斜接角度，那么倒角边将不会进行斜接。默认情况下会启用“斜接角度”(Mitering Angle)功能，并将其设定为 180 度。

#### 角度容差(Angle tolerance)

倒角使用该角度来决定它是否需要插入附加边。如果模型仍包含不需要的边，请尝试增大该值以将这些边移除。

![图：倒角使用该角度来决定它是否需要插入附加边。如果模型仍包含不需要的边，请尝试增大该值以将这些边移除。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-1AB06406-17A1-4614-A495-F3A99596725B.png) <!-- baize:img-hook downloaded=false reason="正文 1837 字 ≥300，非承重" -->

#### 合并顶点(Merge Vertices)

可用于在倒角边时自动合并顶点，而不必单独使用“合并顶点”(Merge Vertices)功能。重合边及其关联的 UV 也会自动进行合并（在指定阈值内）。默认情况下会启用“合并顶点”(Merge Vertices)属性，且可以在“通道盒”(Channel Box)内交替地编辑这些属性。

#### 合并容差(Merge Tolerance)

启用了“合并顶点”(Merge Vertices)时，“合并容差”(Merge Tolerance)值指定顶点必须相距多近才能合并。
