# 放样选项(Loft Options)

使用以下选项可设置在选择“曲面 > 放样”(Surfaces > Loft)时发生的情况。

#### 参数化(Parameterization)

这将修改放样曲面的“参数化”(parameterization)（请参见 [NURBS 曲线和曲面参数化](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-275E0E44-2E4B-4A53-B329-B9F5688730A3.htm)）。

“一致”(Uniform)结间距使剖面曲线与 V 方向平行。在 U 方向生成曲面的参数值的间距均匀。第一条剖面曲线对应于曲面 U[0] 的等参线，第二条对应于 U[1]，依此类推。

“弦长”(Chord Length)间距导致 U 方向生成曲面上的参数值要基于剖面曲线开始点之间的距离。

**注**

提示：

如果曲线具有相同的曲线次数和编辑点数，放样曲面将在 U 方向具有相同数量的跨度数。曲面将更容易操纵和纹理。一个完成该操作的简便方式是复制单个曲线，并在必要时变换复制上的 CV，以便获得所需的剖面曲线。

如果曲线的参数化不同，已放样曲面可能比任何剖面曲线都有更多的跨度数。如果创建曲线为带“弦长”(Chord Length)的“编辑点曲线”(Edit Point curves)，曲面将更加复杂，同时更难处理。

#### 自动反转(Auto Reverse)

如果“自动反转”(Auto Reverse)处于禁用状态，将使用曲线的当前状态，这可能会产生扭曲的曲面。启用后，曲线将自动反转。

在以下示例中，两个顶部曲线和两个底部曲线将进入不同的方向。

![图：如果“自动反转”(Auto Reverse)处于禁用状态，将使用曲线的当前状态，这可能会产生扭曲的曲面。启用后，曲线将自…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-1BB20861-04EB-4714-A648-BCC4BF7A7258.png) <!-- baize:img-hook downloaded=false reason="正文 1599 字 ≥300，非承重" -->

如果“自动反转”(Auto Reverse)处于禁用状态，结果是扭曲的已放样曲面。启用后，曲线将自动反转。

![图：如果“自动反转”(Auto Reverse)处于禁用状态，将使用曲线的当前状态，这可能会产生扭曲的曲面。启用后，曲线将自…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D97508D8-A64D-4516-B71C-240CFA076C2C.png) <!-- baize:img-hook downloaded=false reason="正文 1599 字 ≥300，非承重" -->

如果“自动反转”(Auto Reverse)处于禁用状态，可以在必要时使用“显示操纵器工具”(Show Manipulator Tool)反转原始剖面曲线的曲线方向。只要单击操纵器控制柄就可反转曲线方向。

![图：如果“自动反转”(Auto Reverse)处于禁用状态，将使用曲线的当前状态，这可能会产生扭曲的曲面。启用后，曲线将自…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-9505EE29-1E95-442F-842E-C22ECE00E7E4.png) <!-- baize:img-hook downloaded=false reason="正文 1599 字 ≥300，非承重" -->

#### 关闭(Close)

“关闭”(Close)选项设定已创建曲面是否是周期性在一个维度中（U 或 V）。默认情况下，“关闭”(Close)被禁用。请参见[周期几何体、闭合几何体和开放几何体](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-0BC955AF-3024-437E-838D-CA8328B1D99D.htm)。

#### 曲面次数(Surface Degree)

可以设定“曲面次数”(Surface Degree)为“线性”(Linear)或“立方”(Cubic)。这将设定 U 方向的放样曲面为线性或立方。“线性”(Linear)将创建看起来为面的曲面。“立方”(Cubic)创建平滑曲面。

![图：可以设定“曲面次数”(Surface Degree)为“线性”(Linear)或“立方”(Cubic)。这将设定 U 方…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-5FA3F257-DAAA-48E5-8590-B485D9D8D0BA.png) <!-- baize:img-hook downloaded=false reason="正文 1599 字 ≥300，非承重" -->

#### 截面跨度数(Section Spans)

该选项将设定放样曲线之间的跨度数。较大的数值会生成更精细的曲面变形控制，代价是额外的处理时间。

#### 曲线范围(Curve Range)

如果选择“部分”(Partial)，可以在放样操作后使用“显示操纵器工具”(Show Manipulator Tool)，以更改用于创建曲面的 subCurve 的长度。这将更改曲面的长度。

![图：如果选择“部分”(Partial)，可以在放样操作后使用“显示操纵器工具”(Show Manipulator Tool)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-ECEE9631-83C6-4F0E-8635-F1D1B0B2564C.png) <!-- baize:img-hook downloaded=false reason="正文 1599 字 ≥300，非承重" -->

#### 输出几何体(Output Geometry)

指定创建的几何体类型。（Subdiv 表示细分曲面。）

#### 输入曲线(Input Curves)

“属性编辑器”(Attribute Editor)的“放样历史”(Loft History)区域中的选项允许您访问已构建放样曲面的历史。此信息是只读的。单击箭头按钮以选择曲面、等参线或曲线，然后打开其编辑器区域。

#### 反转曲线(Reverse Curve)

如果在放样曲面时启用“自动反转”(Auto Reverse)，将为用于创建放样曲面的每个曲线、基本体或曲面等参线显示“反转曲线”(Reverse Curve)选项。选择“显示操纵器工具”(Show Manipulator Tool)以显示反转操纵器。单击该选项以反转输入曲线的方向，或单击操纵器。

在以下示例中，选择第一条用于创建放样曲面的曲线来反转。

![图：如果在放样曲面时启用“自动反转”(Auto Reverse)，将为用于创建放样曲面的每个曲线、基本体或曲面等参线显示“反…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-1954B5FE-C64C-4727-9F73-1F090A4D1BBA.png) <!-- baize:img-hook downloaded=false reason="正文 1599 字 ≥300，非承重" -->

### 在“属性编辑器”(Attribute Editor)中编辑 subCurve

如果在创建好放样后在选项窗口中设定“曲线范围”(Curve Range)为“部分”(Partial)，可以使用“属性编辑器”(Attribute Editor)用于由此生成的 subCurve。

## 相关主题

- [蒙皮跨剖面曲线的曲面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-BC91797F-6C42-4B92-9F1E-12518F3BFE8A.htm)
