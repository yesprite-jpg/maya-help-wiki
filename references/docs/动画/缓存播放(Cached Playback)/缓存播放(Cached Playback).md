# 缓存播放(Cached Playback)

缓存播放已更新，包括对动力学节点和“时间编辑器”(Time Editor)的支持。

**“缓存播放”(Cached Playback)**可用于查看对动画所做的更改，而无需创建播放预览。 它显示为沿着[时间滑块(Time Slider)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-827ED8CD-C6AA-4495-8B5E-2FC98C8D49EE.htm)底部的蓝色条带。

以前，每次修改场景时，Maya 都需要更新和重画。若要查看您所做的编辑，通常必须播放预览。这些更新非常耗时，具体取决于场景的大小和所做的更改。现在，您的场景会在您工作时自动缓存，而 Maya 仅重新计算已更改的动画部分，而不是重画整个场景。

**注**

在 Maya 中，

“缓存播放”(Cached Playback)

默认处于活动状态。以下说明用于手动激活或禁用

“缓存播放”(Cached Playback)

。

每当您编辑已缓存的场景时，时间滑块的一部分将变为灰色以显示已过期的动画片段，然后再次变为蓝色以表明这些值已更新。请参见[“缓存播放”(Cached Playback)状态行的状态](缓存播放%28Cached%20Playback%29/使用“缓存播放”%28Cached%20Playback%29以提高播放速度/“缓存播放”%28Cached%20Playback%29状态行的状态.md)主题。

#### 缓存模式

由于“缓存播放”(Cached Playback)将动画存储在内存中，因此您可以通过为设置选择最佳缓存模式来进一步优化播放，因为每种方法都有可根据您的当前硬件设置提供更好性能的属性。

尝试不同的模式，以确定哪种模式提供最佳性能增益。您可以通过右键单击“缓存播放”(Cached Playback)图标 ![图：尝试不同的模式，以确定哪种模式提供最佳性能增益。您可以通过右键单击“缓存播放”(Cached Playback)图标 或…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-EDBB8091-6F7E-4772-B1C6-6019FCB26E2F.png) <!-- baize:img-hook downloaded=false reason="正文 601 字 ≥300，非承重" --> 或[时间滑块(Time Slider)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-827ED8CD-C6AA-4495-8B5E-2FC98C8D49EE.htm)来更改缓存播放模式。 有关不同模式的详细信息，请参见[选择缓存播放模式](缓存播放%28Cached%20Playback%29/使用“缓存播放”%28Cached%20Playback%29以提高播放速度/选择缓存播放模式.md)。

![图：尝试不同的模式，以确定哪种模式提供最佳性能增益。您可以通过右键单击“缓存播放”(Cached Playback)图标 或…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-704E5AA1-A6E1-4596-8073-A7505B7319D2.gif) <!-- baize:img-hook downloaded=false reason="正文 601 字 ≥300，非承重" -->
