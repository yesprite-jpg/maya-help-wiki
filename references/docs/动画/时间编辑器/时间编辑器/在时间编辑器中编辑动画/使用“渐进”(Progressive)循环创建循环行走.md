# 使用“渐进”(Progressive)循环创建循环行走

您可以使用时间编辑器中的“渐进”(Progressive)循环功能在单个片段中创建循环动画。将动画片段添加到时间编辑器后，时间编辑器会自动将有可能进行渐进动画循环的动画片段解释为默认使用此循环模式。但是，您始终可以在“属性编辑器”(Attribute Editor)的“之前的片段循环”(Clip Loop Before)/“之后的片段循环”(Clip Loop After)菜单中手动设置此选项。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-6879DFC2-6E72-4A6D-A98F-3FAC3609051C.gif) <!-- baize:img-hook downloaded=false reason="正文 562 字 ≥300，非承重" -->

从内容浏览器文件（RobotHumanoid.ma 和 walk1.ma）创建动画循环

从动画片段创建循环行走

1. 将动画片段导入时间编辑器。

  **注**

  提示：

  确保片段的开始帧和结束帧尽可能相似，以尽可能创建最平滑的过渡。

2. 选择轨迹上的片段。

3. 在[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)中，检查**“之前的片段循环模式”(Clip Loop Before Mode)**和**“之后的片段循环模式”(Clip Loop After Mode)**是否已设置为**“渐进”(Progressive)**。有关循环模式的说明，请参见[时间编辑器中的循环类型](../使用时间编辑器片段/时间编辑器中的循环类型.md)。

  **注**

  时间编辑器会自动检测有可能创建循环行走的片段，且应已设置此选项。

4. 单击[时间编辑器工具栏](../时间编辑器界面概述/时间编辑器工具栏.md)上的循环图标 ![图：单击时间编辑器工具栏上的循环图标 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-DDB0D45F-B462-4FC5-9D22-9B788329F8E7.png) <!-- baize:img-hook downloaded=false reason="正文 562 字 ≥300，非承重" -->。

5. 拖动动画片段的开始或结束位置。光标发生变化以显示当前处于循环模式。

  ![图：拖动动画片段的开始或结束位置。光标发生变化以显示当前处于循环模式。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-7030A3D1-D029-4E12-86D8-D2D768C41793.gif) <!-- baize:img-hook downloaded=false reason="正文 562 字 ≥300，非承重" -->

6. 播放或拖动动画。

**注**

在

曲线图编辑器(Graph Editor)

中调整循环行走。
