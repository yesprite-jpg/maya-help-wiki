# 圆形圆角选项(Circular Fillet Options)

使用以下选项可设置在选择“曲面 > 曲面圆角 > 圆形圆角”(Surfaces > Surface Fillet > Circular Fillet)时发生的情况。

#### 在曲面上创建曲线(Create Curve On Surface)

启用“在曲面上创建曲线”(Create Curve On Surface)，以便在构建圆角时在曲面上创建曲线。曲线被放置在与圆角相交点的曲面上。

当禁用“在曲面上创建曲线”(Create Curve On Surface)时，将不会在原始曲面上构建曲面上的曲线。默认设置为禁用。

#### 反转表面法线(Reverse Surface Normals)

在构建圆角期间，曲面将沿法线方向以指定的“半径”(Radius)值偏移。通过反转曲面法线，可构建所需的圆角。单击“显示操纵器”(Show Manipulator)图标查看曲面法线。

在创建圆角之前，选择要反转主曲面法线（第一个选定的曲面），还是反转次曲面法线（第二个选定的曲面）。下例显示了半径值为 0.75 的主/次反转方法。

![图：在构建圆角期间，曲面将沿法线方向以指定的“半径”(Radius)值偏移。通过反转曲面法线，可构建所需的圆角。单击“显示操…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-E6F88CB4-35DE-4470-AE7C-1CD1933F739F.png) <!-- baize:img-hook downloaded=false reason="正文 977 字 ≥300，非承重" -->

还可以在曲面上选择点并构建圆角来反转曲面法线。例如，如果主曲面上选定的点不在其曲面法线的同一侧，那么将反转次曲面上的法线。

通过选择曲面点来反转曲面法线：

1. 选择一个点，然后按住 Shift 键并选择另一个点。

  ![图：选择一个点，然后按住 Shift 键并选择另一个点。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F47D9091-52CB-481D-9B3F-063EFA6F152A.png) <!-- baize:img-hook downloaded=false reason="正文 977 字 ≥300，非承重" -->

2. 选择“反转主曲面法线”(Reverse Primary Surface Normal)或“反转次曲面法线”(Reverse Secondary Surface Normal)，然后单击“圆角”(Fillet)按钮。单击“显示操纵器”(Show Manipulator)图标以查看曲面法线。

## 使用操纵器编辑圆形圆角法线

1. 若要在创建完圆角后显示曲面法线和半径操纵器，选择圆角曲面并显示“显示操纵器工具”(Show Manipulator Tool)。

2. 拖动半径操纵器控制柄。

  ![图：拖动半径操纵器控制柄。 使用容差(Use Tolerance) “使用容差”(Use Tolerance)选项允许在指定…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-E13A2A6D-D7AB-4E61-A0CF-588EC2C4B237.png) <!-- baize:img-hook downloaded=false reason="正文 977 字 ≥300，非承重" -->

  #### 使用容差(Use Tolerance)

  “使用容差”(Use Tolerance)选项允许在指定容差值内应用圆形圆角。可以在全局或局部应用容差。

  “全局”(Global)容差可以让 Maya 使用“首选项”(Preferences)窗口设置部分的“位置”(Positional)和“切向”(Tangential)值。

  “局部”(Local)容差允许输入新值来覆盖“首选项”(Preferences)窗口中的值。

## 相关主题

- [在两个曲面之间创建圆角](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-229FEB19-8A78-4A6D-AAF1-D880B39B5F70.htm)

- [自由形式圆角工具选项](自由形式圆角选项%28Freeform%20Fillet%20Options%29.md)

- [圆角融合工具选项](圆角融合工具选项.md)
