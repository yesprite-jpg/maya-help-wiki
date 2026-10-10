# 曲线图编辑器(Graph Editor)

您可修改的动画关键帧之间插值的图形表示。

若要打开曲线图编辑器(Graph Editor)，请执行以下操作：

- 从主菜单栏中，选择“窗口 > 动画编辑器 > 曲线图编辑器”(Windows > Animation Editors > Graph Editor)。

- 从视图菜单栏中，选择“面板 > 面板 > 曲线图编辑器”(Panels > Panel > Graph Editor)。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-83E0DFEE-8248-43A7-AE6D-B06098B5458D.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" -->

“曲线图编辑器”(Graph Editor)显示动画曲线（或函数曲线/FCurve）以表示场景中的动画。

在“曲线图编辑器”(Graph Editor)中查看动画

选择已设置动画的对象，例如模型。两个关键帧之间的任何插值在“曲线图编辑器”(Graph Editor)中表示为动画曲线。请参见[设置关键帧](../关键帧动画/关键帧动画/设定关键帧.md)与[关键帧动画和“曲线图编辑器”(Graph Editor)](../关键帧动画/关键帧动画/关键帧动画和“曲线图编辑器”%28Graph%20Editor%29.md)。

“曲线图编辑器”(Graph Editor)显示场景动画的图表视图，以便通过多种方式创建、查看和修改动画曲线。例如，通过使用切线控制柄改变动画曲线的形状，您可以控制关键帧之间的插值和曲线外插并更改动画曲线值和计时。

**注**

尽管

“曲线图编辑器”(Graph Editor)

的颜色方案专门设计用于提高可见性，但您可以在

颜色设置(Color Settings)

中自定义这些颜色。

其他改进包括：

- 不再需要移动工具即可移动关键帧

- 默认情况下，切线是非加权的

- 提供交互式关键帧且支持隔离曲线

- 时间标记可拖动，能够移动到您在时间标尺上单击的任意位置

- 可调整播放范围大小

- 已简化视图名称。（“堆叠的曲线”(Stacked Curves)现已简化为“堆叠视图”(Stacked View)，“显示已归一化”(Display Normalized)现已简化为“归一化视图”(Normalized View)。此外，现在还提供了一个“绝对视图”(Absolute View)。）

- 可自定义的关键帧和曲线颜色（请参见[颜色设置(Color Settings)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1FC6CC4E-6C21-44FA-A58B-AC31ED57B591)中的“曲线图编辑器”(Graph Editor)部分）

下表提供使用曲线图编辑器的各项任务的简要概述。

| 目标 | 操作 |
|---|---|
| 将“曲线图编辑器”(Graph Editor)放置在场景视图中 | 选择要在其中显示“曲线图编辑器”(Graph Editor)的场景视图，然后选择“面板 > 面板 > 曲线图编辑器”(Panels > Panel > Graph Editor)。 |
| 显示对象的动画曲线 | 在视口或大纲视图中选择对象，以显示其动画曲线。 ![图：在视口或大纲视图中选择对象，以显示其动画曲线。 在曲线图编辑器大纲视图(Graph Editor Outliner)中单…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-C3AE6EB6-E43A-4AFB-9A85-5C7B5E95213F.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 在[曲线图编辑器大纲视图(Graph Editor Outliner)](曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29界面概述/“曲线图编辑器大纲视图”%28Graph%20Editor%20outliner%29.md)中单击通道以显示相应的曲线。 |
| 选择关键帧 | 单击该关键帧或拖动选择它。 ![图：单击该关键帧或拖动选择它。 提示： 直接单击关键帧。放大（按住 Alt 并拖动）以提高精度。如果无法通过此方式选择关键帧…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F2A8A0E5-E5B4-4B37-A25F-D6851E4A188C.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 提示： 直接单击关键帧。放大（按住 **Alt** 并拖动）以提高精度。如果无法通过此方式选择关键帧，可能存在显卡问题；请确保您使用的是最新的驱动程序。 如果在拖动选择关键帧时无意中包含了额外的关键帧，请使用[“动画”(Animation)首选项（在“设置”(Settings)下）](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F)中的**“最小关键帧选择大小”(Min key selection size)**选项收缩可选区域。 |
| 插入关键帧 | **Alt** + **I** 插入一个与当前时间指示器的位置相对应的关键帧。 ![图：Alt + I 插入一个与当前时间指示器的位置相对应的关键帧。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-34118D36-22F3-413C-992E-B27EFC7077DD.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 在**“旋转”(Rotation)**、**“缩放”(Scaling)**或**“平移”(Translation)**通道上的当前时间指示器位置插入关键帧 | **Ctrl** + **Shift** + ****E** **（旋转）、** **R** **（缩放）或 **W**（平移）。 ![图：Ctrl + Shift + E （旋转）、 R （缩放）或 W（平移）。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-4F6A4A30-0714-4C2C-A981-BD8E63F05DC3.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 在选定曲线上插入关键帧，而不管当前时间指示器的位置如何 | 在选定曲线上单击鼠标中键 + **I**。 ![图：在选定曲线上单击鼠标中键 + I。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-C6313CB1-D429-4B52-9D29-38C2045C8280.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 将时间标记移动到选定关键帧。 | **Alt** + **/**（正斜线） ![图：Alt + /（正斜线）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-960FB59D-92EA-4218-9A11-7FC4FA454037.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 在“曲线图编辑器”(Graph Editor)中启用预先选择亮显 | 在“曲线图编辑器”(Graph Editor)菜单栏中，启用“选择 > 选择前亮显”(Select > Pre-select Highlight)。 ![图：在“曲线图编辑器”(Graph Editor)菜单栏中，启用“选择 选择前亮显”(Select Pre-select H…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-61BF0118-BFC2-4E94-ADC8-9ECD280927D9.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 提示： 使用“颜色”(Colors)窗口更改亮显颜色。选择“窗口 > 设置/首选项 > 颜色设置”(Windows > Settings/Preferences > Color Settings)，然后更改“动画编辑器”(Animation Editors)部分中的“预先选择亮显”(Pre-selection highlight)选项。 |
| 平移并放大“曲线图编辑器”(Graph Editor) | 与视口导航相同： 平移：按住 **Alt** 或 **Option** (Mac OS X) 键并使用鼠标中键拖动。 ![图：平移：按住 Alt 或 Option (Mac OS X) 键并使用鼠标中键拖动。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-2DD73939-AB47-4CD7-82C0-973D4C600E1D.png) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 缩放：按住 **Alt** 或 **Option** (Mac OS X) 键并拖动或使用鼠标右键拖动。将基于鼠标光标的位置使缩放居中。 ![图：缩放：按住 Alt 或 Option (Mac OS X) 键并拖动或使用鼠标右键拖动。将基于鼠标光标的位置使缩放居中。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-98DBE2A3-5296-4924-A8A5-9D34FB6B2933.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 水平缩放：按住 **Alt** 或 **Option** (Mac OS X) + **Shift** 键并使用鼠标右键拖动。 ![图：水平缩放：按住 Alt 或 Option (Mac OS X) + Shift 键并使用鼠标右键拖动。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-548E379B-12FA-44B4-B7FD-52D86067E97D.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 缩放曲线 | 选择动画曲线（请参见下文中的**“选择曲线”**），然后单击 **F** 键框显当前选择。 ![图：选择动画曲线（请参见下文中的“选择曲线”），然后单击 F 键框显当前选择。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-16B90ED7-3E03-4297-A666-DC8BC2205666.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 调整播放范围 | 在时间标尺上，单击暗区域的边并拖动以更改播放范围。通过拖动时间标尺上的标志，在时间视图中延伸播放范围。 ![图：在时间标尺上，单击暗区域的边并拖动以更改播放范围。通过拖动时间标尺上的标志，在时间视图中延伸播放范围。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-6A434892-BBBB-4C63-991B-BBA2F130CB11.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 拖动动画 | 拖动当前时间标记。 若要沿图表视图顶部的时间标尺拖动，请向左或向右拖动当前时间标记。 ![图：若要沿图表视图顶部的时间标尺拖动，请向左或向右拖动当前时间标记。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-FE1983F5-5528-49D6-9188-812CC7C5B481.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 若要在图表视图（位于时间标尺下方）中拖动，请按 **K** 键释放光标锁定。（光标将在时间视图中锁定拖动，从而防止无意中移动关键帧/曲线。） ![图：若要在图表视图（位于时间标尺下方）中拖动，请按 K 键释放光标锁定。（光标将在时间视图中锁定拖动，从而防止无意中移动关键…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-AFDF4E8B-508D-4E6E-AAE8-BD5C71EA5340.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 锁定曲线 | 按 **H** 键锁定曲线，按 **J** 键解除锁定曲线。 ![图：按 H 键锁定曲线，按 J 键解除锁定曲线。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-B7DF92AE-929E-4B78-8BD1-187856467B3C.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 移动到上一个或下一个视图 | 使用方括号热键（**[** 和 **]**）。这些是相同的热键，用于在视口的摄影机视图之间移动。 ![图：使用方括号热键（[ 和 ]）。这些是相同的热键，用于在视口的摄影机视图之间移动。 若要使用这些热键导航到视图，请在“曲线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-CF2A579A-35DC-4AE1-BC09-42494DD11F30.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 若要使用这些热键导航到视图，请在“曲线图编辑器”(Graph Editor)中单击，然后按左方括号 (**[**) 移动到上一个视图，或按右方括号 (**]**) 移动到下一个视图。 |
| 过滤损坏的 Euler 角度 | 选择损坏的动画曲线（例如，“旋转 X”(Rotate X)、“旋转 Y”(Rotate Y)和“旋转 Z”(Rotate Z)），然后选择“曲线 > Euler 过滤器”(Curves > Euler Filter)。 请参见[“曲线图编辑器”(Graph Editor)的“曲线”(Curves)菜单](曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)。 |
| 更改现有曲线的旋转插值类型 | 使用“曲线图编辑器”(Graph Editor)和“摄影表”(Dope Sheet) “曲线”(Curves)中的“更改旋转插值”(Change Rotation Interp)选项。请参见[“曲线图编辑器”(Graph Editor)的“曲线”(Curves)菜单](曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)。 |
| 选择关键帧 | 单击[“曲线图编辑器”(Graph Editor)工具栏](曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29界面概述/“曲线图编辑器”%28Graph%20Editor%29工具栏.md)上的**“移动最近拾取的关键帧工具”(Move Nearest Picked Key Tool)** ![图：单击“曲线图编辑器”(Graph Editor)工具栏上的“移动最近拾取的关键帧工具”(Move Nearest Pic…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-9CB815BF-DD09-415F-8E4E-979CF5270544.png) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" -->。 单击关键帧。该关键帧会变为白色，表示已将其选中。 使用鼠标中键单击该关键帧，使光标变为十字光标 (![图：使用鼠标中键单击该关键帧，使光标变为十字光标 ()。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-6DDE9D1B-A204-4657-BDF4-984F9352BDEE.png) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" -->)。 放置关键帧。 ![图：单击“曲线图编辑器”(Graph Editor)工具栏上的“移动最近拾取的关键帧工具”(Move Nearest Pic…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-19FE15C1-6534-4D18-BE31-D35653057FB6.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 提示： 双击**“移动最近拾取的关键帧工具”(Move Nearest Picked Key Tool)** ![图：单击“曲线图编辑器”(Graph Editor)工具栏上的“移动最近拾取的关键帧工具”(Move Nearest Pic…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-9CB815BF-DD09-415F-8E4E-979CF5270544.png) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" -->打开选项窗口，可以在其中设置**“直接关键帧设置”(Direct Key Settings)**。请参见[“曲线图编辑器”(Graph Editor)工具栏](曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29界面概述/“曲线图编辑器”%28Graph%20Editor%29工具栏.md)主题中的**“移动最近拾取的关键帧工具”(Move Nearest Picked Key Tool)**条目。 |
| 选择并移动关键帧组。 | 拖动矩形选择框，然后按住 **Alt** 键并重新定位选择框。 ![图：拖动矩形选择框，然后按住 Alt 键并重新定位选择框。 另请参见区域关键帧工具(Region Keys Tool)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F8735810-4927-41C5-AB4E-D0DC427D66C0.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 另请参见[区域关键帧工具(Region Keys Tool)](../动画引用/动画引用/动画工具/区域关键帧工具%28Region%20Keys%20Tool%29.md)。 |
| 使关键帧变大 | 可以使用[“动画”(Animation)首选项（在“设置”(Settings)下）](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F)中的“关键帧大小”(Key Size)设置来增加或减小关键帧的大小。 ![图：可以使用“动画”(Animation)首选项（在“设置”(Settings)下）中的“关键帧大小”(Key Size)设…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-0E4E4251-E765-4EC9-AC5E-EF4AC37823DB.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 剪切、复制、粘贴和转化关键帧 | 使用[关键帧切线标记菜单](曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/关键帧切线标记菜单.md)访问常用操作（例如，转化、剪切、复制、粘贴关键帧以及切换切线类型）。 ![图：使用关键帧切线标记菜单访问常用操作（例如，转化、剪切、复制、粘贴关键帧以及切换切线类型）。 在图表视图中按 Shift …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-9ECD69D4-0ABE-42E2-A905-9E1AFA560EB3.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 在[图表视图](曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29界面概述/“曲线图编辑器”%28Graph%20Editor%29图表视图.md)中按 **Shift** + **s** 并向左轻扫，以访问此菜单中的关键帧选项。 |
| 设置 FK/IK 关键帧曲线 | 使用[“IK/FK 关键帧”(IK/FK Keys)菜单](../动画引用/动画引用/“动画”%28Animation%29菜单集/“关键帧”%28Key%29菜单/“IKFK%20关键帧”%28IKFK%20Keys%29菜单.md)中的“设置 IK/FK 关键帧”(Set IK/FK Key)选项（在“动画”(Animation)菜单集中，“关键帧 > FK/IK 关键帧 > 设置 IK/FK 关键帧”(Key > FK/IK Keys > Set IK/FK Key)）。 |
| 选择曲线 | 默认情况下，已启用曲线选择。 单击（或拖动选择）两个关键帧之间的曲线即可将其选中。 再次单击（或使用鼠标中键单击）该曲线即可移动。 ![图：默认情况下，已启用曲线选择。 单击（或拖动选择）两个关键帧之间的曲线即可将其选中。 再次单击（或使用鼠标中键单击）该曲线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-D1D285CF-F2EC-42B0-9084-C04014056FB2.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 关键帧类型 | ![图：菱形关键帧：非加权切线](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-39FED8C1-B131-42D5-8782-E8786D757C8A.png) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 菱形关键帧：非加权切线 ![图：方形关键帧：加权切线](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-C2B74128-6D47-4469-894E-961BB6FEA749.png) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 方形关键帧：加权切线 ![图：圆形关键帧：四元数曲线上的关键帧（无切线）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-EC985483-EFD0-4AE4-9143-A9A30FCD6FAD.png) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 圆形关键帧：四元数曲线上的关键帧（无切线） ![图：空心关键帧：带有“自动”切线的新关键帧。当您调整切线时会填充关键帧，以显示其已被编辑。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-CA12BA28-219D-44A3-B551-B17C0DDA477B.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 空心关键帧：带有“自动”切线的新关键帧。当您调整切线时会填充关键帧，以显示其已被编辑。 请参见[“曲线图编辑器”(Graph Editor)颜色](曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29界面概述/“曲线图编辑器”%28Graph%20Editor%29颜色.md)主题中的**“曲线图编辑器”(Graph Editor)关键帧颜色/形状**。 |
| 移动关键帧 | 选择并拖动关键帧。 ![图：选择并拖动关键帧。 若要打开“移动关键帧”(Move Key)工具，请选择“编辑 变换工具 移动关键帧工具 设置”(Ed…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-3B23D7CA-A06A-40F1-9F35-E6449683DBCE.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 若要打开“移动关键帧”(Move Key)工具，请选择“编辑 > 变换工具 > 移动关键帧工具 > ![图：若要打开“移动关键帧”(Move Key)工具，请选择“编辑 变换工具 移动关键帧工具 设置”(Edit Transfo…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" -->设置”(Edit > Transformation Tools > Move Keys Tool > Settings)。 还可以使用鼠标中键单击“曲线图编辑器”(Graph Editor)中的空白区域，然后拖动以重新定位选定关键帧。 ![图：选择并拖动关键帧。 若要打开“移动关键帧”(Move Key)工具，请选择“编辑 变换工具 移动关键帧工具 设置”(Ed…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-2295C176-EE5A-4B2B-8EFB-23D51FAE786B.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 偏移关键帧 | 选择关键帧，然后按 **Shift** + **9** 或 **Shift** + **0** 以将关键帧向右或向左稍微移动一帧。 ![图：选择关键帧，然后按 Shift + 9 或 Shift + 0 以将关键帧向右或向左稍微移动一帧。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-4D1C1EE0-8DB6-43A6-85C6-B18A353B00BF.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 选择上一个/下一个关键帧 | 选择一个关键帧，然后按 **Ctrl** + **Alt** + **,**（逗号）或 **Ctrl** + **Alt** + **.**（句点）以将当前选择移动到上一个或下一个关键帧。 ![图：选择一个关键帧，然后按 Ctrl + Alt + ,（逗号）或 Ctrl + Alt + .（句点）以将当前选择移动到上…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-1162A77C-52EF-4800-A269-0D4343F24009.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 在时间方向上移动多个关键帧而不更改属性值 | 拖动选择要移动的关键帧。按住 Shift 键并使用鼠标中键向左或向右拖动关键帧。 ![图：拖动选择要移动的关键帧。按住 Shift 键并使用鼠标中键向左或向右拖动关键帧。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F1C0D884-F2F3-440D-866D-AFABD560EDC9.gif) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> |
| 更改视图 | 绝对视图：按 **1** 键 这是默认视图。 ![图：绝对视图：按 1 键 这是默认视图。 堆叠视图：按 2 键 归一化视图：按 3 键 选择“视图 重新归一化”(View …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-BD06ED42-4532-46AD-95EF-342069005352.png) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 堆叠视图：按 **2** 键 ![图：绝对视图：按 1 键 这是默认视图。 堆叠视图：按 2 键 归一化视图：按 3 键 选择“视图 重新归一化”(View …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-CA9CCA2F-FF68-4F75-9E5D-C5C59F14A373.png) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 归一化视图：按 **3** 键 ![图：绝对视图：按 1 键 这是默认视图。 堆叠视图：按 2 键 归一化视图：按 3 键 选择“视图 重新归一化”(View …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-B15E8721-519A-4274-8D17-9181721471C4.png) <!-- baize:img-hook downloaded=false reason="正文 3921 字 ≥300，非承重" --> 选择“视图 > 重新归一化”(View > Renormalize)可还原。 注： 当启用“显示已归一化”(Display Normalized)或者活动曲线列表更改时，曲线将自动重新归一化。 |

## 相关主题

- [关键帧动画和曲线图编辑器(Graph Editor)](../关键帧动画/关键帧动画/关键帧动画和“曲线图编辑器”%28Graph%20Editor%29.md)

- [使用“曲线图编辑器”(Graph Editor)和“摄影表”(Dope Sheet)](../关键帧动画/关键帧动画/编辑曲线/使用“曲线图编辑器”%28Graph%20Editor%29和“摄影表”%28Dope%20Sheet%29.md)

- [“曲线图编辑器”(Graph Editor)颜色](曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29界面概述/“曲线图编辑器”%28Graph%20Editor%29颜色.md)
