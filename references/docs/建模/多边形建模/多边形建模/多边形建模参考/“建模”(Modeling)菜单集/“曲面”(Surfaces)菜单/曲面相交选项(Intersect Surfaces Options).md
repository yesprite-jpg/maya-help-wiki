# 曲面相交选项(Intersect Surfaces Options)

使用以下选项可设置在选择“曲面 > 相交”(Surfaces > Intersect)时发生的情况。

#### 为以下项创建曲线(Create Curves for)

“第一曲面”(First Surface)仅会导致选择的第一个曲面（即：目标曲面）接收曲面上的曲线。

“两个面”(Both Surfaces)将导致目标曲面和选择为相交的曲面的曲面均接收曲面上的曲线。这是默认设置。

**注**

如果选择多个曲面，则最后选择的曲面将成为目标曲面。例如，如果选择 10 个曲面，则前九个曲面将和第十个曲面相交。

#### 曲线类型(Curve Type)

“曲面上的曲线”(Curve On Surface)可将曲面上的曲线创建为相交曲线。这是默认设置。

“3D 世界”(3D World)将在 3D 世界空间中创建 NURBS 曲线。该曲线不是曲面上的曲线，因此无法稍后用来修剪该曲面。

**注**

由于文本是曲线的集合，因此不能与目标曲面相交。不能使曲面与曲线相交。若要使文本相交，必须将文本创建为修剪曲面。

#### 使用容差(Use Tolerance)

“使用容差”(Use Tolerance)选项可支持在默认交集的指定容差内相交。可以全局或局部应用容差。

“全局”(Global)容差将导致 Maya 使用“首选项窗口”的“设置”区域中的“位置”值。

“局部”(Local)容差允许输入一个新值，以覆盖“首选项”(Preferences)窗口中的值。

## 相关主题

- [创建曲面上的曲线](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-F023FD2B-9EFC-429D-809E-6AF6B298548F.htm)
