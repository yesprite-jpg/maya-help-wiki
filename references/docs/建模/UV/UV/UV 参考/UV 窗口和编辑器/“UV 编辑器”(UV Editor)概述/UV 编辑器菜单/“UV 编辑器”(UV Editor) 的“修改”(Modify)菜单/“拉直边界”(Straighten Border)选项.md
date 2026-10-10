# “拉直边界”(Straighten Border)选项

使用这些选项可设置在选择“UV > 拉直 UV 边界”(UV > Straighten UV Border)时发生的情况。

## 设置

#### 曲率(Curvature)

将选定边界区域向外或向内推动指定量。如果值为零，则可将边强制为直线。在 UV 坐标标度上，每个“曲率”(Curvature)单位都为 0.01。

根据值为正数还是负数，Maya 将向外或向内弯曲边界。但是，您无法提前判断使用正数还是负数。如果在通道盒或属性编辑器中打开 polyStraightenUVBorder 节点，请尝试正值和负值，然后在 UV 编辑器中检查结果。

#### 保持长度比(Preserve length ratio)

在拉直时控制 UV 纹理边的尺寸。设置为 1 时，Maya 保留原始边长度。设置为 0 时，Maya 对长度求平均值。0 和 1 之间的值可按比例更改长度。

#### 填充当前选择中的间隙(Fill gaps in selection)

“填充当前选择中的间隙”(Fill gaps in selection)选项可帮助您拉直选择中缺失的 UV，因为它们很难选择。

#### UV 间隙容差(UV gap tolerance)

“UV 间隙容差”(UV Gap Tolerance)设置是 Maya 选择的时间阈值，可用于拉直未选定的 UV。例如，如果两个选定的 UV 中间有三个未选定的 UV，则“UV 间隙容差”必须为 3 或更高，Maya 才能选择并拉直中间的 UV。下图显示了一个示例。

![图：“UV 间隙容差”(UV Gap Tolerance)设置是 Maya 选择的时间阈值，可用于拉直未选定的 UV。例如，…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-79627A08-49BF-4C63-A2F3-DE67277929D9.png) <!-- baize:img-hook downloaded=false reason="正文 769 字 ≥300，非承重" -->

#### 保持原始形状(Preserve original shape)

通过将拉直边界的形状与原始边界形状融合，来影响拉直边界的形状。您可以使用此设置来约束以上两个设置的效果。设置为 1 时，Maya 保留原始形状并覆盖其他设置。设置为 0 时，Maya 在拉直时不考虑原始形状。0 和 1 之间的值按比例将原始形状与其他设置创建的曲率融合。

## 相关主题

- [将边界 UV 映射到方形或圆形](../../../../../编辑%20UV/将边界%20UV%20映射到方形或圆形.md)

- [映射 UV 边界选项(Map UV Border options)](“映射边界”%28Map%20Border%29选项.md)
