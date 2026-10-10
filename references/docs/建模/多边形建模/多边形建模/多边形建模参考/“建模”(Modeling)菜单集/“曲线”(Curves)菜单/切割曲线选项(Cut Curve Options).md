# 切割曲线选项(Cut Curve Options)

使用以下选项可设置在选择“曲线 > 切割”(Curves > Cut)时发生的情况。

#### 查找相交处(Find Intersections)

选择 Maya 考虑相交处的方式。

- “在 2D 和 3D 空间”(In 2D and 3D)考虑在 3D 视口或任何 2D 视图（前视图、侧视图或顶视图）中相交的曲线。

- “仅在 3D 空间”(In 3D only)考虑在 3D 视口中相交的曲线（即有一个每个选定曲线公用的点）。

- “使用方向”(Use direction)仅考虑仅在所选方向上相交的曲线。

#### 方向(Direction)

“查找相交处”(Find intersection)设定为“使用方向”(Use direction)时，该选项可以指定方向。

“X”、“Y”和“Z”仅各自考虑沿这些轴相交的曲线。

“活动视图”(Active view)仅考虑在当前摄影机视图中相交的曲线。

“自由”(Free)仅考虑沿下方“方向”(Direction)字段中所定义的自定义轴相交的曲线。

#### 切割(Cut)

选择曲线的切割方式。

- “在所有相交处”(At All Intersections)将在选定曲线的所有相交点处切割曲线。

- “使用最后一条曲线”(Using Last Curve)仅切割选定的最后一条曲线。

#### 保持(Keep)

选择要保留的曲线部分：

- “最长分段”(Longest Segments)将删除每个切割曲线最长部分之外的所有曲线部分。

- “所有曲线分段”(All Curve Segments)将在切割后保持所有曲线。

- “具有曲线点的分段”(Segments with Curve Points)将保持具有选定曲线点的所有曲线分段。如果曲线上没有选定的曲线点，则不会丢弃任何分段。

#### 使用容差(Use Tolerance)

可以使用此选项来提高基本体图形的精度。

“全局容差”(Global tolerance)使用“首选项”(Preferences)窗口（“窗口 > 设置/首选项 > 首选项”(Window > Settings/Preferences > Preferences)）中“设置”(Settings)部分的“位置容差”(Positional tolerance)值。

“局部”(Local)允许您在“容差”(Tolerance)字段中输入值，覆盖“首选项”(Preferences)窗口中的“位置容差”(Positional tolerance)值。

#### 保持原始(Keep Original)

保持原始曲线并从切割处创建新的曲线。

## 相关主题

- [分割曲线或曲面（分离）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-D42B5077-4D64-4942-875D-F39F69506087.htm)
