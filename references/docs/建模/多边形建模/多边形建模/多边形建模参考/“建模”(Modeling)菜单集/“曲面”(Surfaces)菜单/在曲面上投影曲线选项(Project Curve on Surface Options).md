# 在曲面上投影曲线选项(Project Curve on Surface Options)

使用以下选项可设置在选择“曲面 > 在曲面上投影曲线”(Surfaces > Project Curve on Surface)时发生的情况。

#### 沿以下项投影(Project Along)

指定曲面上曲线的投影方向。

“活动视图”(Active View)是默认选项，表示在活动视图的法线方向进行投影。例如，如果前视图处于活动状态，曲线沿 Z 轴（前视图的轴法线）投影。

## 确保投影在活动视图中正常

如果使用“活动视图”(Active View)选项投影曲线，则在使用“在曲面上投影曲线”(Project Curve On Surface)之前必须确定希望处于活动状态的视图。请务必确保选定的曲线（或曲线集）沿着当前视图的垂直（法线）轴投影。

在下图中，在透视视图处于活动状态时尝试进行了投影。您可以看到，曲线没有正确地投影。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-FA9A863D-D1C1-4F0F-812F-89123B4C2377.png) <!-- baize:img-hook downloaded=false reason="正文 1367 字 ≥300，非承重" -->

前视图处于活动状态时投影正常，因为投影的垂直方向相对于前视图的曲面法线。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-440C32A2-491C-4F7B-BEAF-7C8C698D8339.png) <!-- baize:img-hook downloaded=false reason="正文 1367 字 ≥300，非承重" -->

使用“曲面法线”(Surface Normal)，您可以在一个视图中将一条曲线投影到选定的曲面上，然后在任何其他视图中将同一条曲线投影到其他曲面。如果投影时选定了该选项，则活动视图并不重要。

如果选择“曲面法线”(Surface Normal)，请确保将曲线移动到曲面外部。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-E15BB5B8-16E1-4D88-8245-649CCC7D4EA9.png) <!-- baize:img-hook downloaded=false reason="正文 1367 字 ≥300，非承重" -->

曲线位于曲面内部的旋转轴上。如果曲线在曲面内部，投影将花费较长时间才能完成，或将失败。

#### 使用容差(Use Tolerance)

通过“使用容差”(Use Tolerance)选项，您可以在原始曲线的指定容差内投影曲线。您可以全局或局部应用容差。

“全局”(Global)容差会使 Maya 使用“首选项”(Preferences)窗口的“设置”(Settings)部分中的“位置”(Positional)值。

“局部”(Local)容差允许您输入新值以覆盖“首选项”(Preferences)窗口中的值。

#### 曲线范围(Curve Range)

“完成”(Complete)选项用于将整个曲线投影到曲面上。

“部分”(Partial)选项用于仅将部分曲线投影到曲面上。这将创建一个细分曲线（最初是整个曲线），然后可以使用“显示操纵器工具”(Show Manipulator Tool)编辑它。

## 在“通道盒”(Channel Box)中编辑投影的曲线

单击“通道盒”(Channel Box)的“输入”(INPUTS)区域中的“projectCurve”标题以显示投影曲线的属性。

在框中输入值以更改投影的 X、Y 和 Z 方向，或调整局部容差值。您可以键入 on 以设定投影沿曲面法线（而不是在活动视图中）进行。这些选项在选项窗口和“属性编辑器”(Attribute Editor)中也可用。

**注**

如果“沿以下项投影”(Project Along)模式设定为“曲面法线”(Surface Normal)，则“通道盒”(Channel Box)中的“方向”(Direction)值无效。

#### 输入曲面和输入曲线(Input Surface & Input Curve)

“输入曲面和输入曲线”(Input Surface and Input Curve)信息是只读的。通过它您可以访问用于投影曲线的曲面和曲线的历史。单击箭头按钮以选择曲面或曲线，然后单击选项卡以打开其编辑器部分。

#### 使用法线(Use Normal)

如果选择沿曲面法线投影曲线，请启用“使用法线”(Use Normal)。

## 相关主题

- [创建曲面上的曲线](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-F023FD2B-9EFC-429D-809E-6AF6B298548F.htm)
