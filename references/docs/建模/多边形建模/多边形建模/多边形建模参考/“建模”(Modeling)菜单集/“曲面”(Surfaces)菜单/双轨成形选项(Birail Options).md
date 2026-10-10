# 双轨成形选项(Birail Options)

使用以下选项可设置在选择“曲面 > 双轨成形 > 双轨成形 1 工具/双轨成形 2 工具/双轨成形 3+ 工具”(Surfaces > Birail > Birail 1 Tool/Birail 2 Tool/Birail 3+ Tool)时发生的情况。

#### 变换控制(Transform Control)

选择“成比例”(Proportional)或“不成比例”(Non Proportional)以选择如何沿轨道缩放剖面曲线扫描。

## 使用“变换控制”(Transform Control)的示例

在 XZ 平面上构造轨道曲线。构造剖面曲线，使内部 CV 的 Y 坐标为某个常量。通过不成比例的缩放，双轨成形曲面内部 CV 的 Y 坐标也会如剖面曲线的 Y 坐标一样保持常量。

1. 在顶视图中，创建两条轨道曲线。选择“显示 > NURBS > 编辑点”(Display > NURBS > Edit Points)以显示曲线上的编辑点。

  ![图：在顶视图中，创建两条轨道曲线。选择“显示 NURBS 编辑点”(Display NURBS Edit Points)以显…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-2904D832-8ECB-412B-A700-45ADE9ECD465.png) <!-- baize:img-hook downloaded=false reason="正文 1795 字 ≥300，非承重" -->

2. 单击“状态行”(Status Line)上的“捕捉到点”(Snap to points)图标，放置剖面曲线的第一个点，然后再次单击“捕捉到点”(Snap to points)以禁用捕捉功能。

  ![图：单击“状态行”(Status Line)上的“捕捉到点”(Snap to points)图标，放置剖面曲线的第一个点，然…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-54EEFEBF-982D-45A6-8AEC-88194FDF2DD6.png) <!-- baize:img-hook downloaded=false reason="正文 1795 字 ≥300，非承重" -->

3. 在前视图中，继续放置点来创建剖面曲线。选择“捕捉到点”(Snap to points)图标以将最后一个点捕捉到最后一条轨道曲线（请记住，之后要禁用捕捉功能）。

  ![图：在前视图中，继续放置点来创建剖面曲线。选择“捕捉到点”(Snap to points)图标以将最后一个点捕捉到最后一条轨…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4DA9BC77-8DF7-40F9-B1B1-4C424E5CCD05.png) <!-- baize:img-hook downloaded=false reason="正文 1795 字 ≥300，非承重" -->

4. 构建双轨成形曲面。当双轨成形曲面处于活动状态时，单击“通道盒”(Channel Box)的“变换模式”(Transform Mode)框，并选择“不成比例”(Non Proportional)，然后再选择“成比例”(Proportional)。下图显示的是每个变换模式下的双轨成形曲面。

  ![图：构建双轨成形曲面。当双轨成形曲面处于活动状态时，单击“通道盒”(Channel Box)的“变换模式”(Transfor…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-9BAB63E4-F064-4CA0-9FE3-552D9A43BEB9.png) <!-- baize:img-hook downloaded=false reason="正文 1795 字 ≥300，非承重" -->

  #### “剖面融合值”(Profile Blend Value)（仅双轨成形 2）

  通过该选项可设定剖面曲线对已创建曲面的中间剖面的影响。值为 1.0 时表示第一条选定的剖面曲线所具有的影响比第二条剖面曲线的大。值为 0 时表示相反效果。默认情况下，这两条选定的剖面曲线具有相等的影响值，即 0.5。该选项仅适用于使用“双轨成形 2 工具”(Birail 2 Tool)创建的曲面。

  #### 连续性(Continuity)

  这使生成的曲面切线与剖面曲线下的曲面保持连续性。

  由于将多条剖面曲线用于双轨成形 2 工具和双轨成形 3+ 工具，因此“连续性”(Continuity)选项会对使用的每条曲线提供“剖面”(Profile)和“轨道”(Rail)选项。

  #### 重建(Rebuild)

  启用其中一个“重建”(Rebuild)选项以先重建剖面曲线或轨道曲线，然后再将这些曲线用于创建曲面。由于将多条剖面曲线用于双轨成形 2 工具和双轨成形 3+ 工具，因此“重建”(Rebuild)选项会对使用的每条曲线提供“剖面”(Profile)和“轨道”(Rail)选项。

  “剖面”(Profile)可重建剖面曲线。

  “第一轨道”(First Rail)可重建构建曲面时所选的第一条轨道曲线。“第二条轨道”可重建所选的第二条轨道曲线。

  启用任何“重建”(Rebuild)选项时，Maya 都会显示“重建曲线”(Rebuild Curve)选项，在“曲线 > 重建”(Curves > Rebuild)中对其进行了说明。

  #### 输出几何体(Output Geometry)

  指定创建的几何体类型。（Subdiv 表示细分曲面。）

  #### 工具行为(Tool Behavior)

  “完成时退出”(Exit On Completion)会在创建双轨成形曲面后结束工具的使用。如果禁用此选项，则可以执行其他双轨成形操作，而不必再次选择该工具。

  “自动完成”(Auto Completion)在使用双轨成形工具的每步中均会显示提示。如果禁用该选项，则必须按正确的顺序拾取曲线，然后选择双轨成形工具以完成操作。首先拾取剖面曲线，然后拾取两条轨道曲线。

  #### 输入剖面和输入轨道(Input Profile & Input Rail)

  “输入剖面”(Input Profile)和“输入轨道”(Input Rail)信息框会列出用作剖面曲线和轨道曲线的曲线。如果要编辑曲线，请单击曲线名称旁边的箭头按钮。

  #### 切线连续性剖面(Tangent Continuity Profile)

  通过“切线连续性剖面”(Tangent Continuity Profile)选项可以启用或禁用输入剖面曲线的切线连续性功能。当剖面曲线是曲面曲线（等参线、已修剪的边、曲面上的曲线）时，该选项才有效。

## 相关主题

- [沿两条路径曲线扫描一条或多条剖面曲线（双轨成形）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-E9C6BCFF-261A-4E8E-8139-468A57E0E0D4.htm)
