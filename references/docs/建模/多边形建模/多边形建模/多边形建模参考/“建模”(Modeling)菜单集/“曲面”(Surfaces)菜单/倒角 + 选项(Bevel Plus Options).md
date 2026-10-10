# 倒角 + 选项(Bevel Plus Options)

使用以下选项可设置在选择“曲面 > 倒角 +”(Surfaces > Bevel)时发生的情况。

编辑“倒角 +”(Bevel Plus)选项时，请参考下图，图中展示了通过“倒角 +”(Bevel Plus)创建的一部分曲面：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-3EFA2829-8D5B-4BB8-82E2-7A65F21EE6BE.png) <!-- baize:img-hook downloaded=false reason="正文 2699 字 ≥300，非承重" -->

#### 附加曲面(Attach Surfaces)

将“输出几何体”(Output Geometry)选项设定为“NURBS”时，可启用该选项。若打开“附加曲面”(Attach Surfaces)，则 Maya 将结合倒角区域和挤出区域以形成一个 NURBS 曲面。若关闭该选项，则 Maya 将为各区域单独创建 NURBS 面片。

例如，您可以关闭“附加曲面”(Attach Surfaces)，以便使倒角区域内的面片所采用的材质不同于挤出区域内的面片所采用的材质。

#### 创建倒角(Create Bevel)：在开始处(At Start)、在结束处(At End)

在结果曲面的任意一端打开或关闭倒角。“在开始处”(At Start)控制距离曲线最近的部分，“在结束处”(At End)控制距离曲线最远的部分。

#### 倒角宽度(Bevel Width)

指定从结果曲面正面看到的倒角区域宽度。

#### 倒角深度(Bevel Depth)

指定从顶部或侧面看到的倒角区域深度。

#### 挤出距离(Extrude Distance)

指定几何体挤出部分的距离，不包括倒角区域。

#### 创建封口(Create Cap)：在开始处(At Start)、在结束处(At End)

打开或关闭倒角曲面任意一端中心区域封口曲面的创建。“在开始处”(At Start)控制距离曲线最近的部分，“在结束处”(At End)控制距离曲线最远的部分。

#### 倒角内部曲线(Bevel inside curves)

在曲线内部启用倒角，而非曲线外部。因为要确保结果曲面不大于原始曲线，启用此选项可以使您更好地控制倒角曲面的总体大小。

![图：在曲线内部启用倒角，而非曲线外部。因为要确保结果曲面不大于原始曲线，启用此选项可以使您更好地控制倒角曲面的总体大小。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F0C02A2B-8FA3-4FBB-88E8-5781BE5400C9.png) <!-- baize:img-hook downloaded=false reason="正文 2699 字 ≥300，非承重" -->

#### 外部倒角样式(Outer Bevel Style)、内部倒角样式(Inner Bevel Style)

倒角样式控制倒角曲面的整体外观。例如，“直出”(Straight Out)创建从原始曲线向外延伸的直倒角边。

可以通过访问“属性编辑器”(Attribute Editor)或“通道盒”(Channel Box)中的“outerStyleCurve”或“innerStyleCurve”来切换样式和比较结果。

下图说明了倒角样式名称中使用的一些术语：

![图：倒角样式控制倒角曲面的整体外观。例如，“直出”(Straight Out)创建从原始曲线向外延伸的直倒角边。 可以通过访…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-2F5427C4-573C-4E81-BEB9-AC0B13FCC5EA.png) <!-- baize:img-hook downloaded=false reason="正文 2699 字 ≥300，非承重" -->

#### 与外部样式相同(Same as Outer Style)

“外部”(Outer)和“内部”(Inner)样式用于拥有外部曲线和内部曲线的字母或艺术效果图，如字母 O。默认情况下，它们共享相同的倒角样式，但可以通过关闭“与外部样式相同”(Same As Outer Style)选项来使他们不同。

### 使用容差(Use Tolerance)

将“输出几何体”(Output Geometry)选项设定为“NURBS”后可启用该选项。容差确定了原始曲线和倒角曲面之间保持的精确度。从下列选项中选择：

#### 全局(Global)

Maya 采用了“首选项”(Preferences)窗口“设置”(Settings)部分的“位置”(Positional)值（“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)）。

#### 局部(Local)

可用于输入新值,以覆盖“首选项”(Preferences)窗口中设定的值。

#### 容差(Tolerance)

如果选择“局部”(Local)，请设定原始曲线和倒角曲面之间的精确度。较小值所创建的曲面严格遵循曲线。较大值所创建的曲面大体遵循曲线。

## 输出选项(Output Options)

单击“输出选项”(Output Options)选项卡，以指定结果几何体类型和拓扑。

#### 输出几何体(Output Geometry)

确定是否使用结果倒角曲面的“NURBS”或“多边形”(polygons)。

**注**

如果选择“NURBS”，Maya 将为倒角曲面封口区域创建已修剪的曲面。某些外部应用程序（如游戏导出器）可能无法处理已修剪的曲面。

#### 细分方法(Tessellation Method)

用两种不同的方法控制结果倒角曲面的平滑度。将方法设定为“计数”(Count)以指定多边形的数量；请参见[计数细分方法](倒角%20+%20选项%28Bevel%20Plus%20Options%29.md#WS17956D7ADBC6E736-61417A49117AE32C705-7FD1)。将方法设定为“采样”(Sampling)以指定倒角曲面不同区域内的不同细分程度；请参见[采样控制(Sampling Controls)](倒角%20+%20选项%28Bevel%20Plus%20Options%29.md#WS17956D7ADBC6E736-61417A49117AE32C705-7FD0)。

## 计数细分方法(Count tessellation method)

通过将“细分方法”(Tessellation Method)设定为“计数”(Count)，可以指定结果倒角曲面中创建的面数。

#### 面数(Face Count)

输入面数，然后由 Maya 细分曲面，以匹配或大致匹配此计数。为了获得最佳性能，设定的值应能给出足够的平滑度，同时保持较小的多边形数。

**注**

由于为倒角区域和封口创建的面的实际数量不包括在内，所以实际面数高于“面数”(Face Count)值。

## 采样控制(Sampling Controls)

如果将“细分方法”(Tessellation Method)设定为“采样”(Sampling)（默认），则可使用下列选项。“采样”(Sampling)可用于指定倒角曲面不同区域内的不同细分程度。

#### 沿挤出(Along Extrusion)

使用这些设置来控制挤出方向上的细分。

#### 截面(Section)

若想使倒角区域中的细分曲面间的空间与挤出区域中的细分曲面间的空间不同，则可使用此选项。启用“截面”(Section)后，可分别对倒角曲面各截面进行细分：前倒角区域、后倒角区域和未倒角挤出区域。各截面拥有的细分数与“采样数”(Samples)设置中规定的相同。

#### 完成(Complete)

若想在整个曲面上均匀间隔的细分曲面，则使用此选项。启用“完成”(Complete)后，可沿着整个倒角曲面（从一个曲面封口到另一个曲面封口）进行细分。

#### 采样数(Samples)

结果细分中的细分数。

#### 沿曲线(Along Curve)

使用这些设置来控制沿源曲线方向的细分。

#### 跨度(Span)

若想使长跨度数细分曲面间的空间与短跨度数细分曲面间的空间不同，则可使用此选项。（跨度数是指两编辑点之间某根曲线的一部分）。启用“跨度”(Span)后，可在源曲线的各跨度之间进行细分。各跨度拥有的细分数与“采样数”(Samples)设置中规定的相同。

#### 完成(Complete)

若想在整个曲面上均匀间隔经细分的细分曲面，则可使用此选项。启用“完成”(Complete)后，可沿着整个倒角曲面（从曲线的起点到终点）进行细分。

#### 采样数(Samples)

结果细分中的细分数。

## 相关主题

- [从曲线挤出曲面并对其进行倒角处理](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-347C23AB-D9D9-4AF2-B7E5-6F91C98936E6.htm)
