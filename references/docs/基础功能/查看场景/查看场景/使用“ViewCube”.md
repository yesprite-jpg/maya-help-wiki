# 使用“ViewCube”

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-8045690E-F012-4CC0-8B54-6FC73196DAF9.png) <!-- baize:img-hook downloaded=false reason="正文 1720 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-57E9DA6F-DB97-48FB-859F-5FA7A7471DF8.png) <!-- baize:img-hook downloaded=false reason="正文 1720 字 ≥300，非承重" -->

“ViewCube” ® 是屏幕上的一个 3D 导航元素，它可以：

- 提供有关与 3D 场景相关的当前摄影机视图的反馈。

- 让您快速而轻松地在场景视图之间切换。

“ViewCube”显示为场景视图右上角的一个立方体，并对其各个面进行标记以指示与 3D 场景相关的摄影机视图。

Maya 中的默认摄影机视图是“透视”(Perspective)视图，这是使用透视投影的标准四分之三视图。调整摄影机视图时，“ViewCube”将更新以反映摄影机相对于 3D 场景的当前方向。

单击立方体的特定面将自动调整摄影机的视图，以使其与该面匹配。在视图之间进行过渡的过程中，查看摄影机实时设置动画，以便您可以查看摄影机的方向如何相对于 3D 场景进行更改。单击“ViewCube”的边或角可将摄影机视图调整到面视图之间的位置。单击“主页”(Home)图标可将摄影机的位置重置为默认的透视视图。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-DC53E41B-CD52-443F-A019-372DD0E97455.png) <!-- baize:img-hook downloaded=false reason="正文 1720 字 ≥300，非承重" -->

通过单击各个立方体元素总共可获得 26 个标准视图（6 个面视图、8 个角视图和 12 个边视图）。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-1E7D7EA3-48B6-4DF0-899A-5D31EDDC78FC.png) <!-- baize:img-hook downloaded=false reason="正文 1720 字 ≥300，非承重" -->

也可拖动“ViewCube”并将其与不同位置对齐，而不是与提供许多其他查看选项的固定视图对齐。执行该操作时，将使用虚线样式绘制“ViewCube”轮廓。

在场景视图中，默认启用“ViewCube”。可以禁用“ViewCube”，也可以通过[“ViewCube”首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F8DD60C0-A955-4D51-9D3D-9FFE1E8D3D16)（在“ViewCube”上单击鼠标右键，然后选择“首选项”(Preferences)，或转到“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)，然后选择“ViewCube”类别）编辑其选项。

当将鼠标指针置于“ViewCube”上时，立方体区域将亮显。立方体的亮显区域（面、角和边）指示在您单击鼠标时将选择的视图。

使用“ViewCube”更改场景视图

1. 将鼠标指针置于“ViewCube”上，以便所需区域亮显。

2. 单击“ViewCube”的亮显区域。

  场景视图将更改，以匹配与您选择的“ViewCube”区域相对应的视点。

  ![图：单击“ViewCube”的亮显区域。 场景视图将更改，以匹配与您选择的“ViewCube”区域相对应的视点。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-673C4A39-653A-4B9B-9594-37A1075FD4A3.png) <!-- baize:img-hook downloaded=false reason="正文 1720 字 ≥300，非承重" -->

使用“ViewCube”重置场景视图

1. 单击“ViewCube”上方的“主页”(Home)按钮。

  摄影机将返回到其默认位置。也就是说，单击正交视图（前、顶和侧）中的“主页”(Home)按钮可将视图重置为其默认的摄影机位置。单击“透视”(Perspective)视图中的“主页”(Home)按钮可将摄影机的位置重置为使用透视投影的四分之三视图。

在正交视图中查看场景时，“ViewCube”周围的四个小箭头用于将摄影机旋转到相邻的正交视图。

例如，在前视图中查看场景时，单击“ViewCube”右侧的箭头可更改正交视图，以便从右侧查看场景。

使用“ViewCube”查看相邻正交视图

1. 在正交视图中，单击“ViewCube”周围显示的四个箭头之一。这些箭头表示当前正交视图的相邻视图。

  正交视图将更改以匹配您在“ViewCube”上选择的相邻正交视图。

  ![图：在正交视图中，单击“ViewCube”周围显示的四个箭头之一。这些箭头表示当前正交视图的相邻视图。 正交视图将更改以匹配…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-B4482B2A-5D6A-4738-827E-5DEF1EE4F064.png) <!-- baize:img-hook downloaded=false reason="正文 1720 字 ≥300，非承重" -->

在正交视图中查看场景时，两个弧形曲线箭头显示在“ViewCube”附近来控制场景视图的顺时针和逆时针旋转（侧滚）。

使用“ViewCube”侧滚正交视图

1. 在所需的正交视图中，单击曲线侧滚箭头可按顺时针或逆时针方向侧滚视图。

  ![图：在所需的正交视图中，单击曲线侧滚箭头可按顺时针或逆时针方向侧滚视图。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-A190077C-6015-4104-AAE0-50BB5AF7D17E.png) <!-- baize:img-hook downloaded=false reason="正文 1720 字 ≥300，非承重" -->

使用“ViewCube”翻滚场景视图

1. 单击“ViewCube”并向任意方向拖动它来翻滚视图。

在场景视图中隐藏“ViewCube”的显示

1. 在“ViewCube”上单击鼠标右键，然后选择“隐藏 ViewCube”(Hide ViewCube)，或选择“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)，然后在“ViewCube”类别中禁用“显示 ViewCube”(Show the ViewCube)。

修改“ViewCube”首选项

您可以通过[“ViewCube”首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F8DD60C0-A955-4D51-9D3D-9FFE1E8D3D16)编辑器控制相关特性，例如 ViewCube 的大小、位置、不透明度及其他行为。

1. 在“ViewCube”上单击鼠标右键，然后选择“首选项”(Preferences)，或选择“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)，然后转到“ViewCube”类别。
