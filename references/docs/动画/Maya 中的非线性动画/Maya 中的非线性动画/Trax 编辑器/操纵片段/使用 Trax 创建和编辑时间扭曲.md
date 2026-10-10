# 使用 Trax 创建和编辑时间扭曲

使用时间扭曲可以在不修改片段动画曲线的情况下更改片段的计时。通常，您将使用时间扭曲反转片段中的动画，或者缓入或缓出片段的动画。

创建或复制片段时可以自动创建时间扭曲，或者可以选择现有片段，然后为其创建时间扭曲。请参见[创建片段选项](../“Trax%20编辑器”%28Trax%20Editor%29菜单/Trax%20编辑器%28Trax%20Editor%29%20创建%28Create%29菜单/“创建片段”%28Create%20Clip%29选项.md)。默认情况下，创建片段时不创建时间扭曲。

为片段创建时间扭曲时，时间扭曲曲线将添加到片段层次中片段的上方，片段上将显示绿色条。请参见[时间扭曲](../Trax%20中的非线性动画组件/Trax%20中的片段/片段状态.md#GUID-968254A9-1044-4887-8197-63A41D0DE05A__WS17956D7ADBC6E736475032DC117AE308AAE-7F6D)。可以对该时间扭曲曲线进行操纵，调节时间扭曲对动画片段中动画的影响方式。

**注**

多个时间扭曲会降低性能，因此应少用时间扭曲。

为片段创建时间扭曲

1. 选择要为其创建时间扭曲的片段。

2. 执行下列操作之一：

  - 在 Trax 菜单栏中，选择“创建 > 时间扭曲”(Create > Time Warp)。

  - 在片段上单击鼠标右键，然后从显示的菜单中选择“创建时间扭曲”(Create Time Warp)。

    ![图：在片段上单击鼠标右键，然后从显示的菜单中选择“创建时间扭曲”(Create Time Warp)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-EAFDB166-5223-4C6A-8593-28432D10C049.png) <!-- baize:img-hook downloaded=false reason="正文 1146 字 ≥300，非承重" -->

  将为该片段节点启用“时间扭曲启用”(Time Warp Enable)属性，新时间扭曲曲线将显示在片段中。默认情况下，时间扭曲曲线范围在 0 到 100 之间，表示其动画片段的百分比。时间 0 是片段的开始，时间 100 是片段的结束。

  在轨迹视图区域中，片段上将显示绿色条，表示该片段现在受时间扭曲影响。

编辑时间扭曲

1. 选择有时间扭曲的片段。

2. 在 Trax 工具栏中，单击“图形动画曲线”![图：在 Trax 工具栏中，单击“图形动画曲线” 按钮。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-6E06A364-2544-4960-838B-7BD1EB5D014D.png) <!-- baize:img-hook downloaded=false reason="正文 1146 字 ≥300，非承重" --> 按钮。

3. 在“曲线图编辑器大纲视图”(Graph Editor outliner)中，选择时间扭曲并单击“框显全部”(Frame All)![图：在“曲线图编辑器大纲视图”(Graph Editor outliner)中，选择时间扭曲并单击“框显全部”(Frame …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-AC8F3337-DCAE-42E6-89BD-B5CC5E392A61.png) <!-- baize:img-hook downloaded=false reason="正文 1146 字 ≥300，非承重" -->按钮或按 f 框显时间扭曲曲线。

4. 在图表视图中，使用“插入关键帧工具”(Insert Keys Tool)插入关键帧并使用“移动工具”(Move Tool)调整曲线。

  在图表视图中借助这些工具进行工作时，请使用鼠标中键。

在创建片段时创建时间扭曲

1. 选择要将其动画置入片段的角色。

2. 在 Trax 菜单栏中，选择“动画 > 创建片段”(Animate > Create Clip) > ![图：在 Trax 菜单栏中，选择“动画 创建片段”(Animate Create Clip) 。 此时将显示“创建片段选项”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1146 字 ≥300，非承重" -->。

  此时将显示[“创建片段选项”(Create Clip Options)](../“Trax%20编辑器”%28Trax%20Editor%29菜单/Trax%20编辑器%28Trax%20Editor%29%20创建%28Create%29菜单/“创建片段”%28Create%20Clip%29选项.md)窗口。

3. 启用“创建时间扭曲曲线”(Create Time Warp Curve)。

  此时将显示片段，其中包含片段的角色动画曲线和活动的时间扭曲曲线。现在，每次创建片段时，将为每个片段创建活动时间扭曲曲线。

启用或禁用时间扭曲曲线

1. 选择包含要启用或禁用的时间扭曲曲线的片段。

2. 在“属性编辑器”(Attribute Editor)或“通道盒”(Channel Box)中，将“时间扭曲启用”(Time Warp Enable)属性设置为启用或禁用。

禁用创建片段时自动创建时间扭曲

1. 在 Trax 菜单栏中，选择“动画 > 创建片段”(Animate > Create Clip) > ![图：在 Trax 菜单栏中，选择“动画 创建片段”(Animate Create Clip) 。 此时将显示“创建片段选项”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1146 字 ≥300，非承重" -->。

  此时将显示[“创建片段选项”(Create Clip Options)](../“Trax%20编辑器”%28Trax%20Editor%29菜单/Trax%20编辑器%28Trax%20Editor%29%20创建%28Create%29菜单/“创建片段”%28Create%20Clip%29选项.md)窗口。

2. 禁用“创建时间扭曲曲线”(Create Time Warp Curve)。
