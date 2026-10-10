# 切割 UV 工具(Cut UV Tool)

使用“切割 UV 工具”(Cut UV Tool)，可以借助沿边拖动来分割 UV。按住 Ctrl 键暂时激活“缝合 UV 工具”(Sew UV Tool)并将 UV 焊接在一起。 切割时，UV 将根据其各自的固定值移动（即，固定的 UV 将保持不动，而未固定的 UV 将按其“切开比”(Cut Open Ratio)值移动）。有关切割边的详细信息，请参见[分离和附加 UV](../../编辑%20UV/分离和附加%20UV.md)。

若要打开“切割 UV 工具”(Cut UV Tool)，请从“UV 工具包”(UV Toolkit)的“切割和缝合”(Cut & Sew)部分中选择它，或从“UV 编辑器”(UV Editor)菜单中选择“工具 > 切割”(Tools > Cut)。

**注**

在

“视口”(Viewport)

和

“UV 编辑器”(UV Editor)

之间移动时，

“切割工具”(Cut Tool)

将自动更改为

3D 切割和缝合工具(3D Cut and Sew Tool)。

选择“工具 > 切割”(Tools > Cut) > ![图：选择“工具 切割”(Tools Cut) 时，在“工具设置”(Tool Settings)窗口中将显示以下选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 870 字 ≥300，非承重" --> 时，在“工具设置”(Tool Settings)窗口中将显示以下选项。

## 笔刷选项(Brush Options)

#### 边选择敏感(Edge Select Sensitive)

指定工具的半径。较高的“边选择敏感”(Edge Select Sensitive)值会增大半径。在壳上拖动光标时处于半径内的任何边都将被切割。

#### 稳定笔划(Steady Stroke)

通过过滤鼠标运动，有助于产生更平滑的笔划。启用时，向量显示在工具光标上，但在拖动距离等于向量长度之前不显示切割。向量长度由“距离”(Distance)设置设定。

#### 距离(Distance)

在工具光标上设置“稳定笔划”(Steady Stroke)向量的长度。

#### 切开比(Cut Open Ratio)

指定分割 UV 之间间隙的大小。较高的值会生成较宽的间隙。

#### 显示所有壳边界(Display All Shell Borders)

启用时，亮显壳边界。各组连接的边将以不同的颜色显示，以便于识别共有的边。默认情况下，“显示所有壳边界”(Display All Shell Borders)处于禁用状态。

## 相关主题

- [分离和附加 UV](../../编辑%20UV/分离和附加%20UV.md)

- [3D 切割和缝合工具(3D Cut and Sew Tool)](../../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/“3D%20切割和缝合%20UV%20工具”%283D%20Cut%20and%20Sew%20UV%20Tool%29选项.md)
