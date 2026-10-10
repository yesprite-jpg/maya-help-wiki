# 通道盒(Channel Box)

打开“通道盒”(Channel Box)

- 单击界面右上角的“通道盒”(Channel Box)图标。

  ![图：单击界面右上角的“通道盒”(Channel Box)图标。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-4851D584-0F1B-4011-8D86-46B1C9F8CFC1.png) <!-- baize:img-hook downloaded=false reason="正文 2077 字 ≥300，非承重" -->

- 选择“窗口 > 常规编辑器 > 通道盒/层编辑器”(Windows > General Editors > Channel Box/Layer Editor)。

- 按 Ctrl+A 打开[属性编辑器(Attribute Editor)](属性编辑器%28Attribute%20Editor%29.md)，然后打开“通道盒”(Channel Box)。

如果“在通道盒内显示层编辑器”(Show Layer Editor within Channel Box)选项在“UI 元素”(UI Elements)首选项（“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)）中处于禁用状态，则“通道盒”(Channel Box)和“层编辑器”(Layer Editor)按钮将分别显示。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-F4FA1F6A-8235-440F-AEDB-41AD14DC2B94.png) <!-- baize:img-hook downloaded=false reason="正文 2077 字 ≥300，非承重" -->

“通道盒”(Channel Box)是用于编辑对象属性的最快最高效的主要工具。它允许您快速更改属性值，在可设置关键帧的属性上设置关键帧，锁定或解除锁定属性以及创建属性的表达式。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-C1775953-291F-480F-87EB-9302A35FAEF0.png) <!-- baize:img-hook downloaded=false reason="正文 2077 字 ≥300，非承重" -->

可以从界面右侧的默认位置取消停靠“通道盒”(Channel Box)，并使其位于浮动窗口中或停靠到其他位置。有关详细信息，请参见[停靠和取消停靠窗口和面板](../../../界面概述/界面概述/工作区/停靠和取消停靠窗口和面板.md)。

与属性编辑器相似，您可以使用“通道盒”(Channel Box)修改对象的属性值。“通道盒”(Channel Box)在以下各方面不同于“属性编辑器”(Attribute Editor)：

- 它仅显示选定对象的*“可设置关键帧”*和*“显示的不可设置关键帧的项”*属性。这样，您便可以从“通道盒”(Channel Box)轻松访问不可设置关键帧的通道，不必担心会意外设置它们的关键帧。从“通道盒”(Channel Box)或[通道控制编辑器(Channel Control Editor)](通道盒%28Channel%20Box%29/“通道控制”%28Channel%20Control%29编辑器.md)中，可以将通道创建为可设置关键帧或不可设置关键帧。

- 您可以更改多个对象的多个属性值（请参见[查看和编辑多个节点上的多个属性](查看和编辑多个节点上的多个属性.md)）

- 其面板变窄，但可以在其边上拖动以调整其宽度。

- 您可以控制对象的构建历史。

“通道盒”(Channel Box)中显示的信息根据选定对象或组件的类型而变化。如果未选定对象，则“通道盒”(Channel Box)为空。

**注**

“通道盒”(Channel Box)有时会错误显示已枚举属性的下拉菜单。可能出现附加菜单项，它们表示在无序选项值之间的编号。若要修复该问题，请为将显示在“通道盒”(Channel Box)中的任何已枚举属性的选项指定连续值。例如：“solo=1:triplet=2:quintet=3”。

## 属性

当您选择几何对象时，“通道盒”(Channel Box)将显示以下区域：

| 区域 | 用法 |
|---|---|
| objectName | 列出可在世界空间中平移、缩放和旋转对象的绝对位置的可设置关键帧变换属性。还显示了对象的可见性属性。 |
| 形状 | 列出定义对象的几何体的节点的名称。其他节点，例如，可在此处找到的相关粒子发射器。 |
| 输入 | 列出影响该节点的其他节点的名称。通常，这些节点名称构成节点的构建历史。 |
| 输出 | 列出该节点的输出节点（接收数据的节点）的名称。 |

如果已选定两个或更多对象，则“通道盒”(Channel Box)将仅显示最后一个选定对象的属性。若要在“通道盒”(Channel Box)中显示另一个选定对象的属性，请选择“对象 > 对象名”。

在“通道盒”(Channel Box)中执行的编辑会影响与显示对象同类型的*所有选定对象*。

## 锁定“通道盒”(Channel Box)属性

若要锁定“通道盒”(Channel Box)属性以使其无法更改，请亮显属性，然后从“通道盒”(Channel Box) [“通道”(Channels)菜单](通道盒%28Channel%20Box%29/“通道盒”%28Channel%20Box%29菜单.md#GUID-19CD9DD8-0119-448F-A1B8-93C82A74B633__WS1A9193826455F5FF-6507591011913E8F4B8-7D85)中选择“通道 > 锁定选定项”(Channels > Lock Selected)。

若要锁定并隐藏属性，请亮显属性，然后从“通道盒”(Channel Box) [“通道”(Channels)菜单](通道盒%28Channel%20Box%29/“通道盒”%28Channel%20Box%29菜单.md#GUID-19CD9DD8-0119-448F-A1B8-93C82A74B633__WS1A9193826455F5FF-6507591011913E8F4B8-7D85)中选择“通道 > 锁定选定项”(Channels > Lock Selected)。

## 组件属性

如果显示对象组件的属性，则对于与该组件相关的图形属性，“通道盒”(Channel Box)将仅显示一个区域。

例如，假定您已使用下列 CV 创建一条 NURBS 曲线：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-D6F5BF87-95BE-4B87-97FC-A3B7787F61C4.png) <!-- baize:img-hook downloaded=false reason="正文 2077 字 ≥300，非承重" -->

如果启用组件选择模式（在主菜单栏中）并选择各 CV，则“通道盒”(Channel Box)将如下所示：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-F16AD000-D221-45B7-ABA9-03A80D255C29.png) <!-- baize:img-hook downloaded=false reason="正文 2077 字 ≥300，非承重" -->

可以在“通道盒”(Channel Box)中显示 CV 值并输入新值。若要显示这些值，请在“通道盒”(Channel Box)单击“CV”（单击以显示）。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-CD2B5AEF-2F5C-42FC-8297-40BC5CB440F4.png) <!-- baize:img-hook downloaded=false reason="正文 2077 字 ≥300，非承重" -->

## “通道盒”(Channel Box)颜色

以下颜色表示“通道盒”(Channel Box)中各通道的状态：

| 已锁定 | 灰度 |
|---|---|
| 不可设定关键帧 | 浅灰色 |
| 禁用 | 褐色 |
| 已融合 | 绿色 |
| 已设置关键帧的帧 | 红色 |
| 未设置关键帧的帧 | 深粉红色 |
| 已改变关键帧 | 淡粉红色 |
| 表达式 | 紫色 |
| 受约束 | 蓝色 |
| 已连接 | 黄色 |

## 输入

使用“通道盒”(Channel Box)的输入组件修改对象的构建历史。

## 相关主题

- [层编辑器](../../../界面概述/界面概述/层编辑器%28Layer%20Editor%29.md)

- [节点和属性概述](../../节点和属性.md)

- [关键帧(Keys)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-68F66F69-1F76-4F58-A88A-0A58FBDE5350)

- [受控关键点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5B605DBF-63DC-44A3-83AE-33EAE2B025F5)

- [在属性编辑器(Attribute Editor)或通道盒(Channel Box)中更改属性值](在“属性编辑器”%28Attribute%20Editor%29或“通道盒”%28Channel%20Box%29中更改属性值.md)

- [锁定属性值](锁定属性值.md)

- [创建、编辑或删除自定义属性](创建、编辑或删除自定义属性.md)

- [使用表达式连接属性](../查看和更改节点之间的输入和输出关系/使用表达式连接属性.md)
