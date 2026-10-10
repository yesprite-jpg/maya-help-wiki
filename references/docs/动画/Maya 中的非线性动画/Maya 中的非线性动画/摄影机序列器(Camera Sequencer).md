# 摄影机序列器(Camera Sequencer)

打开摄影机序列器：

- 从主菜单栏中：“窗口 > 动画编辑器 > 摄影机序列器”(Windows > Animation Editors > Camera Sequencer)。

- 从视图菜单栏中：“面板 > 面板 > 摄影机序列器”(Panels > Panel > Camera Sequencer)。

**注**

注意：

(Mac OS X) 在 64 位系统上的

“摄影机序列器”(Camera Sequencer)

支持受限。为获得更好的性能和实时结果，请在 32 位模式下运行 Maya 以使用

“摄影机序列器”(Camera Sequencer)

。

利用“摄影机序列器”(Camera Sequencer)提供的工具，可以布置和管理摄影机快照，然后在场景中生成动画的一段渲染影片。您可以开始在 Maya 中布置快照，或先导入您自己的包含音频和视频片段信息的 FCP 格式编辑文件。即使对于大型场景，也可以生成影片片段，以实现实时播放。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-EE64E229-89E2-4EB3-8488-D0DD6A25D733.png) <!-- baize:img-hook downloaded=false reason="正文 1154 字 ≥300，非承重" -->

在“摄影机序列器”(Camera Sequencer)窗口中，快照表示为排列在轨迹上的一组矩形，您可以通过操纵摄影机快照来定义和操纵在任意时间点哪个摄影机处于活动状态。如果您对摄影机的布局和计时满意，则可以播放预览动画的影片片段。

**注**

注意：

(Mac OS X) 在 64 位系统上的

“摄影机序列器”(Camera Sequencer)

支持受限。为获得更好的性能和实时结果，请在 32 位模式下运行 Maya 以使用

“摄影机序列器”(Camera Sequencer)

。

该工具包括下列主要区域：

- [菜单栏](摄影机序列器%28Camera%20Sequencer%29/“摄影机序列器”%28Camera%20Sequencer%29菜单栏.md)

- [工具栏](摄影机序列器%28Camera%20Sequencer%29/“摄影机序列器”%28Camera%20Sequencer%29工具栏.md)

- [快照视图区域](摄影机序列器%28Camera%20Sequencer%29/“摄影机序列器”%28Camera%20Sequencer%29快照视图区域.md)

- [时间轴和播放控制](摄影机序列器%28Camera%20Sequencer%29/“摄影机序列器”%28Camera%20Sequencer%29时间轴和播放控件.md)

下表简要概述了使用“摄影机序列器”(Camera Sequencer)的任务。

| 目标 | 操作 |
|---|---|
| 创建快照。 | 单击 ![图：单击 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-BFFBFB17-1D29-4775-8437-E396B114DF84.png) <!-- baize:img-hook downloaded=false reason="正文 1154 字 ≥300，非承重" -->。 |
| 框显所有快照。 | 单击 ![图：单击 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-AC8F3337-DCAE-42E6-89BD-B5CC5E392A61.png) <!-- baize:img-hook downloaded=false reason="正文 1154 字 ≥300，非承重" -->。 |
| 创建单个摄影机来播放所有快照。 | 选择“创建 > Ubercam”(Create > Ubercam)。 |
| 滚动快照视图区域。 | 按住 Alt 键并使用鼠标中键拖动（Linux 和 Windows），或按住 Option 键并使用鼠标中键拖动 (Mac OS X)。 |
| 移动快照。 | 拖动单个快照来移动它们，或按住 Shift 键单击以选择多个快照，然后在白色矩形区域中拖动。 |
| 缩放快照。 | 拖动片段的底部角。（将显示缩放光标 ![图：拖动片段的底部角。（将显示缩放光标 。）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-410EF49B-8091-4A9E-AB18-6447F53429B7.png) <!-- baize:img-hook downloaded=false reason="正文 1154 字 ≥300，非承重" -->。） |
| 修剪快照。 | 拖动片段的顶部角。（将显示修剪光标 ![图：拖动片段的顶部角。（将显示修剪光标 。）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-73B9F6D2-F57E-4512-9E42-185C5D85BD12.png) <!-- baize:img-hook downloaded=false reason="正文 1154 字 ≥300，非承重" -->。） |
| 禁用快照。 | 在快照上单击鼠标右键，然后选择“禁用”(Mute)。 |
| 删除快照。 | 选择快照并按 Delete 键。 |
| 播放预览影片序列。 | 在所需快照上单击鼠标右键并从弹出菜单中选择“播放预览快照”(Playblast Shot)。 |
| 对快照分组。 | 选择要分组的快照，然后选择“分组 > 创建”(Group > Create)。 |
| 将音频添加到快照中。 | 选择该快照，然后从菜单栏中选择“文件 > 导入镜头音频”(File > Import Shot Audio)。 |
| 将图像平面添加到快照摄影机中。 | 在快照上单击鼠标右键并选择“附加图像平面”(Attach Image Plane)。 |
