# MASH 工作流

在典型的 MASH 工作流中，您可以使用 Maya 集成工具包生成各种效果，然后将这些元素导出到创意后期制作工具。在以下教程中，我们将介绍如何从头开始设置未来派的 UI 效果，然后将其分层导出到 Adobe® After Effects®。

有关涉及创建特定 MASH 效果的更多视频，请参见 [Maya 教学频道](http://www.youtube.com/mayahowtos)上的[运动图形](https://www.youtube.com/playlist?list=PL8hZ6hQCGHMUn5NdkAQpWBG7xxGFP480q)播放列表。

**注**

有关本教程中使用的场景文件，请访问

此处

。

**注**

其中的大多数视频已录制在 Maya 2016 Extension 2 中。在 Maya 2017 或更高版本中，您可能会发现细微的差异，例如：

- MASH 菜单现在位于“动画”(Animation)和“FX”菜单集中。

- 不再需要为特定的变换通道指定 MASH 节点（这些节点现在始终同时指定给“平移”、“旋转”和“缩放”）。

- 替换某些节点（将“噪波”(Noise)和“三角”(Trig)替换为[信号(Signal)](MASH%20参考/MASH%20节点概述/信号.md)，将“禁用”(Mute)替换为[强度(Strength)](MASH%20参考/MASH%20节点概述/强度.md)）。

- 对其他杂项的 UI 进行了细微的更改。

## MASH 工作流简介

## 创建像素球体

使用的节点：[分布(Distribute)](MASH%20参考/MASH%20节点概述/分布.md)、[重新投影(Repro)](MASH%20参考/MASH%20节点概述/重新投影.md)、[可见性(Visibility)](MASH%20参考/MASH%20节点概述/可见性.md)。

## 创建网状球体和周围元素

使用的节点：[分布(Distribute)](MASH%20参考/MASH%20节点概述/分布.md)、[重新投影(Repro)](MASH%20参考/MASH%20节点概述/重新投影.md)、[复制器(Replicator)](MASH%20参考/MASH%20节点概述/复制器.md)、[轨迹(Trails)](MASH%20参考/MASH%20节点概述/添加工具/轨迹.md)、[变换(Transform)](MASH%20参考/MASH%20节点概述/变换.md)。

## 设置场景元素的动画

使用的节点：[分布(Distribute)](MASH%20参考/MASH%20节点概述/分布.md)、[重新投影(Repro)](MASH%20参考/MASH%20节点概述/重新投影.md)、[变换(Transform)](MASH%20参考/MASH%20节点概述/变换.md)。

## 为摄影机创建和修复 HUD 元素

使用的节点：[分布(Distribute)](MASH%20参考/MASH%20节点概述/分布.md)、[变换(Transform)](MASH%20参考/MASH%20节点概述/变换.md)。

## 创建其他 HUD 元素

使用的节点：[音频(Audio)](MASH%20参考/MASH%20节点概述/音频.md)、[分布(Distribute)](MASH%20参考/MASH%20节点概述/分布.md)、[信号(Signal)](MASH%20参考/MASH%20节点概述/信号.md)、[对称(Symmetry)](MASH%20参考/MASH%20节点概述/对称.md)、[变换(Transform)](MASH%20参考/MASH%20节点概述/变换.md)。

**注**

如果使用的是

Maya

2016 Extension 2，请改为参考

Maya 教学频道

中的上一工作流。

## 将效果层导出到 After Effects

使用的功能：[渲染层(Render Layers)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-646154F9-E4D2-4A3E-A0D9-B2F062960A4E)。
