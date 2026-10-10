# 边界选项(Boundary Options)

使用以下选项可设置在选择“曲面 > 边界”(Surfaces > Boundary)时发生的情况。

#### 曲线顺序(Curve Ordering)

“自动”(Automatic)创建带内部决定过程的边界。“作为选定项”(As Selected)会导致曲线选择顺序确定生成的曲面。

在下图中，在选定“自动”(Automatic)的情况下通过选择曲线来创建第一个曲面。当选项设置为“作为选定项”(As Selected)，同时以不同顺序选择曲线时，创建第二个曲面。

![图：“自动”(Automatic)创建带内部决定过程的边界。“作为选定项”(As Selected)会导致曲线选择顺序确定生…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-48ED5C6C-A054-4AC9-AD59-6D8FD1196379.png) <!-- baize:img-hook downloaded=false reason="正文 777 字 ≥300，非承重" -->

#### 公用端点(Common End Points)

“公用端点”(Common End Points)选项用于决定是否应在创建边界曲面前匹配结束点。

如果选择“可选”(Optional)，将创建该曲面，即使曲线结束点不匹配。这是默认设置。

如果选择“必需”(Required)，将仅在曲线结束点完全匹配的情况下构建边界曲面。

![图：“公用端点”(Common End Points)选项用于决定是否应在创建边界曲面前匹配结束点。 如果选择“可选”(Op…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4C188CDF-FB16-4A6D-85A4-DED9FF92333D.png) <!-- baize:img-hook downloaded=false reason="正文 777 字 ≥300，非承重" -->

若要确保结束点匹配，请记住在绘制曲线时从“状态行”(Status Line)选择捕捉模式。

若要在绘制曲线后匹配结束点：

1. 启用捕捉模式，例如，“捕捉到栅格”(Snap to grids)。

2. 选择要移动的编辑点或 CV。

3. 选择“移动工具”(Move Tool)并拖动以捕捉到同一位置。

  ![图：选择“移动工具”(Move Tool)并拖动以捕捉到同一位置。 结束点容差(End Point Tolerance) 如…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-9B50F3CF-CE3F-4881-ACF7-332D7F6754CC.png) <!-- baize:img-hook downloaded=false reason="正文 777 字 ≥300，非承重" -->

  #### 结束点容差(End Point Tolerance)

  如果选择“必需”(Required)作为“公用端点”(Common End Point)选项，可以更改结束点的“结束点容差”(End Point Tolerance)值以设定其被视为重合时的接近程度。

  “全局”(Global)容差可以使 Maya 使用“首选项”(Preferences)窗口的“设置”(Settings)区域中的“位置”(Positional)值。

  “局部”(Local)容差用于输入新值覆盖“首选项”(Preferences)窗口中的“位置”(Positional)值。

## 相关主题

- [在边界曲线内创建曲面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-5D83A8B9-3CA8-40CE-AC53-A6B8440F1C34.htm)
