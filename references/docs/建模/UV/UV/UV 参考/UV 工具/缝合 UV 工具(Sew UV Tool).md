# 缝合 UV 工具(Sew UV Tool)

若要打开“缝合 UV 工具”(Sew UV Tool)，请在“UV 工具包”(UV Toolkit)的“切割和缝合”(Cut & Sew)部分中选择它，或从“UV 编辑器”(UV Editor)菜单中选择“工具 > 缝合”(Tools > Sew)。 有关缝合边的详细信息，请参见[分离和附加 UV](../../编辑%20UV/分离和附加%20UV.md)。

使用“缝合 UV 工具”(Sew UV Tool)，可以借助沿边拖动来焊接 UV。按 Ctrl 键可暂时激活“切割 UV 工具”(Cut UV Tool)。在缝合期间，Maya 将遵循 UV 的当前固定状态（即，对于固定的 UV，仅在可以不移动它们的情况下对其进行缝合时才进行缝合，而对于未固定的 UV，将一起移动它们以进行缝合）。

选择“工具 > 缝合”(Tools > Sew) > ![图：选择“工具 缝合”(Tools Sew) 时，在“工具设置”(Tool Settings)窗口中将显示以下选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 650 字 ≥300，非承重" --> 时，在“工具设置”(Tool Settings)窗口中将显示以下选项。

## 笔刷(Brush)

#### 大小(Size)

指定工具的半径。在壳上拖动光标时处于半径内的任何分割边都将合并在一起。

#### 稳定笔划(Steady Stroke)

通过过滤鼠标运动，有助于产生更平滑的笔划。启用时，向量显示在工具光标上，但在拖动距离等于向量长度之前各边不接合在一起。向量长度由“距离”(Distance)设置设定。

#### 距离(Distance)

在工具光标上设置“稳定笔划”(Steady Stroke)向量的长度。

#### 显示所有壳边界(Display All Shell Borders)

启用时，亮显壳边界。各组连接的边将以不同的颜色显示，以便于识别共有的边。默认情况下，“显示所有壳边界”(Display All Shell Borders)处于禁用状态。
