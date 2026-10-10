# “曲线”(Curves)菜单

- 位于“建模”(Modeling)[菜单集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D90A2BDB-FD05-4528-8A95-C33A02D15129)中。

## 修改

#### 锁定长度(Lock Length)

选择“锁定长度”(Lock Length)时，选定的曲线（或选定的 CV）将保持恒定的壳线长度。然后，如果修改曲线（例如，通过移动 CV），曲线的形状将会调整，以便保持恒定的壳线长度（即，除了您移动的 CV 以外的其他 CV 也将发生移动）。第一次锁定曲线的长度时，“锁定长度”(Lock Length)属性会添加到 curveShape 节点中。可以使用 l（小写的 L）键作为临时热键。按住 l 键可以锁定选定曲线的长度。释放 l 键可以解除锁定曲线的长度。

**注**

如果在启用

“锁定长度”(Lock Length)

的情况下移动 CV 并选择

“撤消”(Undo)

，则仅有移动的 CV 返回到其原始位置。如果启用

“锁定长度”(Lock Length)

并修改曲线，则曲线的第一个 CV 不会移动（除非明确移动第一个 CV）。例如，如果移动曲线的第一个 CV，则曲线的响应将不同于移动曲线的最后一个 CV 时曲线的响应。

#### 解除锁定长度(Unlock Length)

选择“解除锁定长度”(Unlock Length)时，选定的曲线（或选定的 CV）将不再保持恒定的壳线长度。然后，如果修改曲线（例如，通过移动 CV），则曲线的壳线长度将不再保持恒定（且仅移动的 CV 发生实际移动）。选择“解除锁定长度”(Unlock Length) 时，curveShape 的“锁定长度”(Lock Length)属性处于禁用状态。

#### 弯曲(Bend)

使选定曲线（或选定 CV）朝一个方向弯曲。曲线的第一个 CV 将保持其原始位置。

选择“曲线 > 弯曲”(Curves > Bend) > ![图：选择“曲线 弯曲”(Curves Bend) 以设置弯曲曲线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[弯曲曲线选项](“曲线”%28Curves%29菜单/弯曲曲线选项%28Bend%20Curves%20Options%29.md)。

#### 卷曲(Curl)

卷曲选定曲线（或选定 CV）以使其类似螺旋。曲线的第一个 CV 将保持其原始位置。

**注**

提示：

不对一条曲线应用两次

“卷曲”(Curl)

。第二次

“卷曲”(Curl)

将会产生不理想的结果，因为它尝试卷曲已卷曲的曲线。

选择“曲线 > 卷曲”(Curves > Curl) > ![图：选择“曲线 卷曲”(Curves Curl) 以设置卷曲曲线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[卷曲曲线选项](“曲线”%28Curves%29菜单/卷曲曲线选项%28Curl%20Curves%20Options%29.md)。

#### 缩放曲率(Scale Curvature)

根据“比例因子”(Scale Factor)和“最大曲率”(Max Curvature)值，使选定曲线（或选定 CV）更直，或扩大其现有曲率。

选择“曲线 > 缩放曲率”(Curves > Scale Curvature) > ![图：选择“曲线 缩放曲率”(Curves Scale Curvature) 以设置缩放曲率选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[缩放曲率选项](“曲线”%28Curves%29菜单/缩放曲率选项%28Scale%20Curvature%20Options%29.md)。

#### 平滑(Smooth)

使选定曲线（或选定 CV）更平滑。曲线的第一个和最后一个 CV 将保留它们的原始位置。

选择“曲线 > (修改)平滑”(Curves > (Modify) Smooth) > ![图：选择“曲线 (修改)平滑”(Curves (Modify) Smooth) 以设置平滑曲线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[平滑曲线选项](“曲线”%28Curves%29菜单/平滑曲线选项%28修改%29%28Smooth%20Curves%20Options%20%28Modify%29%29.md)。

#### 拉直(Straighten)

使选定曲线（或选定 CV）更直（以曲线第一分段的方向）。曲线的第一个 CV 将保持其原始位置。

选择“曲线 > 拉直”(Curves > Straighten) > ![图：选择“曲线 拉直”(Curves Straighten) 以设置拉直曲线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[拉直曲线选项](“曲线”%28Curves%29菜单/拉直曲线选项%28Straighten%20Curves%20options%29.md)。

## 编辑

#### 复制曲面曲线(Duplicate Surface Curves)

基于选定的曲面边、等参线或曲面上的曲线创建新的 NURBS 曲线。

选择“曲线 > 复制曲面曲线”(Curves > Duplicate Surface Curves) > ![图：选择“曲线 复制曲面曲线”(Curves Duplicate Surface Curves) 以设置复制曲面曲线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[复制曲面曲线选项](“曲线”%28Curves%29菜单/复制曲面曲线选项%28Duplicate%20Surface%20Curves%20Options%29.md)。

#### 对齐(Align)

对齐曲线的端点。

选择“曲线 > 对齐”(Curves > Align) > ![图：选择“曲线 对齐”(Curves Align) 以设置对齐曲线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[对齐曲线选项](“曲线”%28Curves%29菜单/对齐曲线选项%28Align%20Curves%20Options%29.md)。

#### 添加点工具(Add Points Tool)

使用该工具可以将点添加到选定曲线的末端。

#### 附加(Attach)

将 NURBS 曲线在端点接合起来，以形成一条新曲线。可以选择两条或多条曲线进行附加。

#### 分离(Detach)

将一条曲线分割为两条新曲线。

#### 编辑曲线工具(Edit Curve Tool)

在单击的曲线上将显示一个操纵器，通过它可以更改曲线上任意点的位置和方向。调整“切线操纵器大小”(Tangent Manip. Size)以控制操纵器上切线方向控制柄的长度。

#### 移动接缝(Move Seam)

将闭合/周期曲线的接合点移动到选定的编辑点。

#### 开放/闭合(Open/Close)

在开放和闭合/周期之间转化曲线。

选择 “曲线 > 开放/闭合”(Curves > Open/Close) > ![图：选择 “曲线 开放/闭合”(Curves Open/Close) 以设置开放/闭合曲线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[开放/闭合曲线选项](“曲线”%28Curves%29菜单/开放闭合曲线选项%28OpenClose%20Curve%20Options%29.md)。

#### 圆角(Fillet)

在两条不相交的独立曲线之间创建一条曲线。

选择“曲线 > 圆角”(Curves > Fillet) > ![图：选择“曲线 圆角”(Curves Fillet) 以设置圆角曲线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[圆角曲线选项](“曲线”%28Curves%29菜单/圆角曲线选项%28Fillet%20Curve%20Options%29.md)。

#### 切割(Cut)

在视图中曲线穿过切割曲线的位置分割曲线。

选择“曲线 > 切割”(Curves > Cut) > ![图：选择“曲线 切割”(Curves Cut) 以设置切割曲线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[切割曲线选项](“曲线”%28Curves%29菜单/切割曲线选项%28Cut%20Curve%20Options%29.md)。

#### 相交(Intersect)

创建曲线点定位器，其中两条或更多条独立曲线按某个视图或方向彼此接触或交叉。“曲线相交”(Intersect Curves)通常与“曲线 > 切割”(Curves > Cut)、“曲线 > 分离”(Curves > Detach)和“捕捉到点”(Snap to Point)一起使用。

选择“曲线 > 相交”(Curves > Intersect) > ![图：选择“曲线 相交”(Curves Intersect) 以设置曲线相交选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[曲线相交选项](“曲线”%28Curves%29菜单/曲线相交选项%28Intersect%20Curve%20Options%29.md)。

#### 延伸(Extend)

延伸一条曲线，或者创建一条新曲线作为延伸。

选择“曲线 > 延伸 > 延伸曲线”(Curves > Extend > Extend Curve) > ![图：选择“曲线 延伸 延伸曲线”(Curves Extend Extend Curve) 以设置延伸曲线选项，或者选择“曲线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[延伸曲线选项](“曲线”%28Curves%29菜单/延伸曲线选项%28Extend%20Curve%20Options%29.md)，或者选择“曲线 > 延伸 > 延伸曲面上的曲线”(Curves > Extend > Extend Curve on Surface) > ![图：选择“曲线 延伸 延伸曲线”(Curves Extend Extend Curve) 以设置延伸曲线选项，或者选择“曲线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[延伸曲面上的曲线选项](“曲线”%28Curves%29菜单/延伸曲面上的曲线选项%28Extend%20Curve%20on%20Surface%20Options%29.md)。

#### 插入结(Insert Knot)

在选定曲线点处插入编辑点。

选择“曲线 > 插入结”(Curves > Insert Knot) > ![图：选择“曲线 插入结”(Curves Insert Knot) 以设置插入结选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[插入结选项](“曲线”%28Curves%29菜单/插入结选项%28Insert%20Knot%20Options%29.md)。

#### 偏移(Offset)

创建所选内容的副本，从原始位置偏移一定的距离。从“偏移曲线”(Offset Curve)和“偏移曲面上的曲线”(Offset Curve On Surface)中进行选择。

选择“曲线 > 偏移 > 偏移曲线”(Curves > Offset > Offset Curve) > ![图：选择“曲线 偏移 偏移曲线”(Curves Offset Offset Curve) 以设置偏移曲线选项，或者选择“曲线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[偏移曲线选项](“曲线”%28Curves%29菜单/偏移曲线和偏移曲面上的曲线选项%28Offset%20Curve%20and%20Offset%20Curve%20on%20Surface%20Options%29.md)，或者选择“曲线 > 偏移 > 偏移曲面上的曲线”(Curves > Offset > Offset Curve on Surface) > ![图：选择“曲线 偏移 偏移曲线”(Curves Offset Offset Curve) 以设置偏移曲线选项，或者选择“曲线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[偏移曲面上的曲线选项](“曲线”%28Curves%29菜单/偏移曲线和偏移曲面上的曲线选项%28Offset%20Curve%20and%20Offset%20Curve%20on%20Surface%20Options%29.md)。

#### CV 硬度(CV Hardness)

设定选定 CV 的多重性。

选择“曲线 > CV 硬度”(Curves > CV Hardness) > ![图：选择“曲线 CV 硬度”(Curves CV Hardness) 以设置 CV 硬度选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置 [CV 硬度选项](“曲线”%28Curves%29菜单/CV%20硬度选项%28CV%20Hardness%20Options%29.md)。

#### 拟合 B 样条线(Fit B-spline)

将一个三次（立方）线拟合到一次（线性）曲线中。在从其他产品（其中曲线次数为 1）导入曲线、表面和数字化数据后，通常会使用“拟合 B 样条线”(Fit B-spline)。

选择“曲线 > 拟合 B 样条线”(Curves > Fit B-spline) > ![图：选择“曲线 拟合 B 样条线”(Curves Fit B-spline) 以设置拟合 B 样条线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[拟合 B 样条线选项](“曲线”%28Curves%29菜单/拟合%20B%20样条线选项%28Fit%20B-spline%20Options%29.md)。

#### 投影切线(Project Tangent)

使曲线切线端点或曲率与另一个曲线或曲面连续。

选择“曲线 > 投影切线”(Curves > Project Tangent) > ![图：选择“曲线 投影切线”(Curves Project Tangent) 以设置投影切线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[投影切线选项](“曲线”%28Curves%29菜单/投影切线选项%28Project%20Tangent%20Options%29.md)。

#### 平滑(Smooth)

在选定曲线中平滑折点。再次选择该命令以提高平滑度。

选择“曲线 > (编辑)平滑”(Curves > (Edit) Smooth) > ![图：选择“曲线 (编辑)平滑”(Curves (Edit) Smooth) 以设置平滑曲线选项（编辑）。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[平滑曲线选项（编辑）](“曲线”%28Curves%29菜单/平滑曲线选项%28编辑%29%28Smooth%20Curve%20Options%20%28Edit%29%29.md)。

#### Bezier 曲线(Bezier Curves)

可用于更改 Bezier 曲线上的选定锚点（控制顶点）或选定切线。

选择“曲线 > Bezier 曲线 > 切线选项”(Curves > Bezier Curves > Tangent Options)，然后选择 [Bezier 曲线切线选项](“曲线”%28Curves%29菜单/Bezier%20曲线切线选项%28Bezier%20Curve%20Tangent%20Options%29.md)；或者选择“曲线 > Bezier 曲线 > 锚点预设”(Curves > Bezier Curves > Anchor Presets)，然后选择 [Bezier 曲线锚点预设](“曲线”%28Curves%29菜单/Bezier%20曲线锚点预设%28Bezier%20Curve%20Anchor%20Presets%29.md)之一。

#### 重建(Rebuild)

执行各种操作以修改选定曲线。

选择“曲线 > 重建”(Curves > Rebuild) > ![图：选择“曲线 重建”(Curves Rebuild) 以设置重建曲线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[重建曲线选项](“曲线”%28Curves%29菜单/重建曲线选项%28Rebuild%20Curve%20Options%29.md)。

#### 反转方向(Reverse Direction)

反转选定曲线的方向。

选择“曲线 > 反转方向”(Curves > Reverse Direction) > ![图：选择“曲线 反转方向”(Curves Reverse Direction) 以设置反转曲线选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3126 字 ≥300，非承重" --> 以设置[反转曲线选项](“曲线”%28Curves%29菜单/反转方向选项%28Reverse%20Direction%20Options%29.md)。
