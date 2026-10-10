# 使用“重影编辑器”(Ghosting Editor)修改场景重影

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1184 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-5F673921-2ADB-44AC-93B4-8D8EA936A1A8.gif) <!-- baize:img-hook downloaded=false reason="正文 1184 字 ≥300，非承重" -->

使用[重影编辑器(Ghosting Editor)](../重影编辑器%28Ghosting%20Editor%29.md)，可以将更改应用于场景中的所有重影。使用“重影编辑器”(Ghosting Editor)，可以一个一个或一组一组地编辑每个重影属性。

对场景中的元素应用重影

1. 在“动画”(Animation)[菜单集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D90A2BDB-FD05-4528-8A95-C33A02D15129) (**F4**) 中选择“可视化 > 打开重影编辑器”(Visualize > Open Ghosting Editor)。此时将打开“重影编辑器”(Ghosting Editor)。

2. 在“重影设置”(Ghosting Settings)区域中，选择要应用重影的对象类型：**“几何体”(Geometry)** ![图：在“重影设置”(Ghosting Settings)区域中，选择要应用重影的对象类型：“几何体”(Geometry) 、…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-EC45E90C-C488-47DE-B706-EA95CA024DFE.png) <!-- baize:img-hook downloaded=false reason="正文 1184 字 ≥300，非承重" -->、**“关节”(Joints)** ![图：在“重影设置”(Ghosting Settings)区域中，选择要应用重影的对象类型：“几何体”(Geometry) 、…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-6D663821-A99B-4CC3-A247-38894D0A8699.png) <!-- baize:img-hook downloaded=false reason="正文 1184 字 ≥300，非承重" -->或**“定位器”(Locators)** ![图：在“重影设置”(Ghosting Settings)区域中，选择要应用重影的对象类型：“几何体”(Geometry) 、…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-D89C59C5-9EB1-4F5A-BA9E-FEAE735D62E6.png) <!-- baize:img-hook downloaded=false reason="正文 1184 字 ≥300，非承重" -->。如果要在重影预览中包括整个绑定层级，请激活**“包括层级”(Include Hierarchy)**。

3. 单击“从当前选择创建重影”(Create Ghost from Selection)，之后将填充“重影对象”(Ghosted Objects)列表。

4. 使用“重影”(Ghost)选项可以选择重影显示方式，如在动画前显示、在动画后显示或在动画前后显示；在“帧步长”(Frame Step)区域中可以选择在每一帧、每两帧、每五帧等之后显示重影。

使用其他对象驱动重影

1. 使用以下 MEL 脚本，在[节点编辑器(Node Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-23277302-6665-465F-8579-9BC734228F69)中将对象设置为重影驱动者：

  ```text
connectAttr <driver>.msg <ghost>.ghostDriver
```

1. （其中 <driver> 是要驱动重影的对象。）

2. 在[重影编辑器(Ghosting Editor)](../重影编辑器%28Ghosting%20Editor%29.md)中，选择“为关键帧生成重影”(Ghost Key Frames) ![图：在重影编辑器(Ghosting Editor)中，选择“为关键帧生成重影”(Ghost Key Frames) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-9ADECEDA-CC77-4FB0-8EDF-8F60D421C668.gif) <!-- baize:img-hook downloaded=false reason="正文 1184 字 ≥300，非承重" -->。

3. 单击“为关键帧生成重影”(Ghost Key Frames)下方显示的“使用重影驱动者”(Use Ghost Driver)选项，在“节点编辑器”(Node Editor)中将重影关键帧替换为选定对象中的关键帧。

更改场景重影的颜色

在[重影编辑器(Ghosting Editor)](../重影编辑器%28Ghosting%20Editor%29.md)底部的“显示选项”(Display Options)中，双击颜色平铺以打开颜色窗口，您可以在其中设置颜色。在 UI 中单击颜色窗口以外的位置以将其关闭。

更改场景重影的透明度

在[重影编辑器(Ghosting Editor)](../重影编辑器%28Ghosting%20Editor%29.md)底部的“显示选项”(Display Options)中，移动“近不透明度”(Near Opacity)或“远不透明度”(Far Opacity)设置的滑块。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-B362AFEB-FB7C-41FF-AC96-005F658CF757.png) <!-- baize:img-hook downloaded=false reason="正文 1184 字 ≥300，非承重" -->

重影编辑器不透明度设置：**A**)“近不透明度”(Near Opacity)设置为 100，“远不透明度”(Far Opacity)设置为 5，**B**)“近不透明度”(Near Opacity)设置为 5，“远不透明度”(Far Opacity)设置为 100

“近不透明度”(Near Opacity)百分比用于设置重影靠近已生成重影的对象时的可见程度，“远不透明度”(Far Opacity)设置用于增加或减少重影远离已生成重影的对象时的可见程度。
