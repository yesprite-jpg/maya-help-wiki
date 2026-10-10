# 偏移曲线和偏移曲面上的曲线选项(Offset Curve and Offset Curve on Surface Options)

使用以下选项可设置在选择“曲线 > 偏移 > 偏移曲线”(Curves > Offset > Offset Curve)或“曲线 > 偏移 > 曲面上的曲线”(Curves > Offset > Curve on Surface)时发生的情况。

#### 法线方向(Normal Direction)

“几何体平均值”(Geometry Average)和“活动视图”(Active View)选项可选择 Maya 用于定位偏移的方法。最简单的方式是通过“显示操纵器工具”(Show Manipulator Tool)只创建偏移并调整其位置来了解每种方法的工作方式。

“几何体平均值”(Geometry Average)是更直观的方法。对于平面曲线，假设您站在曲线起点，朝向初始曲线方向。“几何体平均值”(Geometry Average)使偏移曲线处于曲线的左边。它按比例缩小向左形成圆弧的曲线，并按比例放大向右形成圆弧的曲线。

对于 3D 曲线，“几何体平均值”(Geometry Average)将曲线点所在的平均平面的法线考虑在内。

对于平面曲线和 3D 曲线，“活动视图”(Active View)将摄影机的视点方向考虑在内。

#### 偏移距离(Offset Distance)

指定原始曲线与偏移曲线之间的距离。

#### 连接断开(Connect Breaks)

如果您创建偏移曲线所基于的曲线包含多点结或 CV，且多重性大于 1，则 Maya 可能会创建具有尖锐棱角的偏移曲线或者将曲线断开为多个不连续的曲线。

“圆形”(Circular)通过在断点处插入圆弧创建连续的曲线。

“线性”(Linear)通过用直线连接断点创建连续的曲线。

“禁用”(Off)保留断开为多个不连续曲线的偏移曲线。

如果选择“圆形”(Circular)或“线性”(Linear)，则 Maya 在曲线中插入多点结以保留曲线形状。如果调整多结位置附近的曲线，则曲线可能会发生切线断开。

#### 循环剪切(Loop Cutting)

设置是否对平面曲线中的任何循环进行修剪。如果与原始曲线的距离超出所偏移曲线的最小弯曲半径（曲率），则发生循环。例如，如果曲线的半径为 20 cm 并且您尝试向内偏移超过 20 cm，则偏移曲线横贯自身并创建一个循环。使用“圆形”(Circular)在修剪的循环处插入圆弧。

![图：设置是否对平面曲线中的任何循环进行修剪。如果与原始曲线的距离超出所偏移曲线的最小弯曲半径（曲率），则发生循环。例如，如果…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-AAE4A42C-4A13-4F24-B0FC-BEE1A5E67F3F.png) <!-- baize:img-hook downloaded=false reason="正文 1595 字 ≥300，非承重" -->

#### 切割半径(Cutting Radius)

如果启用“循环剪切”(Loop Cutting)，则使用“切割半径”(Cutting Radius)值。如果“切割半径”(Cutting Radius)值大于 0，则可以获取指定半径的圆弧，而不是获取已剪切循环位置的尖锐棱角。

![图：如果启用“循环剪切”(Loop Cutting)，则使用“切割半径”(Cutting Radius)值。如果“切割半径”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-84EB511F-D5ED-49C3-BA28-6A15E746A5EA.png) <!-- baize:img-hook downloaded=false reason="正文 1595 字 ≥300，非承重" -->

#### 最大细分密度(Max Subdivision Density)

指定在当前容差范围内偏移几何体可以细分的最大次数。默认值为 5，这意味着曲线上的任何一个跨度最多可以细分 5 次。

#### 使用容差(Use Tolerance)

如果选择“全局”(Global)容差，则 Maya 使用您在“首选项”(Preferences)窗口的“设置”(Settings)部分中设置的“位置”(Positional)值。

如果选择“局部”(Local)容差，则您可以直接输入一个新值以替代“首选项”(Preferences)窗口的“位置”(Positional)容差值。

#### 容差(Tolerance)

指定将偏移曲线放置在指定距离的精确度。默认值精确到 0.05 个单位内。默认单位为厘米。偏移是一个迭代过程，在当前偏移达到容差值或最大细分限制内之前连续执行该过程。

#### 曲线范围(Curve Range)

“完成”(Complete)可创建整个原始曲线的偏移曲线。

“部分”(Partial)仅允许您创建部分原始曲线的偏移曲线。它创建一个细分曲线节点，您可以编辑该节点以在创建之后更改偏移距离。

#### 输入曲线(Input Curve)

列出偏移曲线或等参线的历史节点。单击“输入曲线”(Input Curve)名称旁边的箭头按钮以编辑曲线的长度。

## 相关主题

- [创建曲线或曲面的偏移副本](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-A61D32E0-335C-41F1-92F7-7A14352AD672.htm)
