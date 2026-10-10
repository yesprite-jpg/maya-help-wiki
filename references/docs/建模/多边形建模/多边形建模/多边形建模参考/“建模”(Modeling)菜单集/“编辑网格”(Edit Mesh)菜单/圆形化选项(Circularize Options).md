# 圆形化选项(Circularize Options)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-2308C5CA-12A1-428C-862D-412A4FBF12E1.png) <!-- baize:img-hook downloaded=false reason="正文 655 字 ≥300，非承重" -->

使用“圆形化”(Circularize)命令可以将选定组件（顶点、边和面）重新组织为完美的几何圆形。有关如何使用该命令的信息，请参见[圆形化组件](../../../编辑多边形/修改多边形网格/圆形圆角组件.md)。

使用这些选项可设置在选择“编辑网格 > 圆形化”(Edit Mesh > Circularize)时发生的情况。

#### 径向偏移(Radial Offset)

调整圆的初始半径。 如果还选择了内部组件，则这些组件也会根据偏移进行缩放。

#### 法线方向(Normal Orientation)

（在视图中编辑器内可用）确定对哪一组组件法线(面或循环边）进行平均以确定圆的方向。

#### 法线偏移(Normal Offset)

根据所有选定组件的平均法线调整初始挤出量。

#### 扭曲(Twist)

确定组件绕圆心旋转的程度。

#### 松弛内部(Relax Interior)

调整组件之间的间距，使它们保持在圆内，同时保持均匀分布。较低的值将强制采用组件的原始间距。

#### 对齐(Alignment)

确定将如何相对于所选组件确定生成的圆的方向。选项包括：

- 自动(Automatic)：根据选定组件的平均法线方向旋转圆形化的组件。

  ![图：自动(Automatic)：根据选定组件的平均法线方向旋转圆形化的组件。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-EAA20EB0-922B-4D8E-8887-D50DCD68E9D5.png) <!-- baize:img-hook downloaded=false reason="正文 655 字 ≥300，非承重" -->

- 曲面(Surface)：圆形化的组件符合原始形状的曲面。

  ![图：曲面(Surface)：圆形化的组件符合原始形状的曲面。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-941A4947-28C0-4CC4-ADD3-BEB0AF855182.png) <!-- baize:img-hook downloaded=false reason="正文 655 字 ≥300，非承重" -->

#### 平滑角度(Smoothing Angle)

指定操作完成后，是否自动软化或硬化圆上的插入边。

#### 均匀分布(Evenly Distribute)

指定是否沿圆的圆周均匀分布圆形化的顶点。

#### 添加分段(Add Divisions)

向当前选择添加额外的顶点，从而产生更平滑的圆。

#### 支撑边(Supporting Edges)

沿圆的圆周向顶点添加边。这可以用于帮助避免从圆的外部、内部或两侧产生 N 边形。
