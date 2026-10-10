# 使用“缓存播放”(Cached Playback)以提高播放速度

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 1828 字 ≥300，非承重" -->

“缓存播放”(Cached Playback)可用于立即查看对动画所做的更改，而无需创建播放预览。

以前，每当您修改场景时，Maya 都需要更新和重画。若要查看更改，您需要创建播放预览。更新场景非常耗时，具体取决于场景的大小和所做的更改。现在，您可以构建场景的缓存，使 Maya 仅重新计算已更改的动画部分，而不必在整个时间范围内更新整个场景。

“缓存播放”(Cached Playback)在 Maya 中显示为蓝色和粉色条带，称为沿时间滑块移动的**“缓存播放”(Cached Playback)状态行**。

动画和动力学在场景中分别缓存：蓝色的缓存播放状态行显示动画缓存的进度，而粉色状态行表示动力学节点的缓存。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F102497F-2064-4BF5-B534-638198843F8A.gif) <!-- baize:img-hook downloaded=false reason="正文 1828 字 ≥300，非承重" -->

为场景激活或禁用缓存

**注**

在 Maya 中，

“缓存播放”(Cached Playback)

默认处于活动状态。以下说明用于手动激活或禁用

“缓存播放”(Cached Playback)

。

单击[播放选项(Playback Options)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-9853B7B5-8AD5-46F6-A921-A3771A505AD1.htm)中的“缓存播放”(Cached Playback)图标 ![图：单击播放选项(Playback Options)中的“缓存播放”(Cached Playback)图标 。（也可以右键单…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-EDBB8091-6F7E-4772-B1C6-6019FCB26E2F.png) <!-- baize:img-hook downloaded=false reason="正文 1828 字 ≥300，非承重" -->。（也可以右键单击[时间滑块(Time Slider)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-827ED8CD-C6AA-4495-8B5E-2FC98C8D49EE.htm)，并从菜单中选择“缓存播放”(Cached Playback)。）

右键单击“缓存播放”(Cached Playback)图标 ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-EDBB8091-6F7E-4772-B1C6-6019FCB26E2F.png) <!-- baize:img-hook downloaded=false reason="正文 1828 字 ≥300，非承重" --> 以执行以下操作：

- 选择其他缓存模式（有关不同模式的列表及各模式执行的操作，请参见[选择缓存播放模式](使用“缓存播放”%28Cached%20Playback%29以提高播放速度/选择缓存播放模式.md)）。

- 打开[缓存播放首选项(Cached Playback Preferences)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3CB35662-DB1D-4CF3-9135-E09B973635DE)窗口。

- 在[颜色设置(Color Settings)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1FC6CC4E-6C21-44FA-A58B-AC31ED57B591)窗口中更改“缓存播放”(Cached Playback)状态行的颜色。

- 清除缓存以清空缓存的内容，以便进行重建。（有关清除缓存的信息，请参见[“缓存播放”(Cached Playback)状态行的状态](使用“缓存播放”%28Cached%20Playback%29以提高播放速度/“缓存播放”%28Cached%20Playback%29状态行的状态.md)。）

每当您编辑已缓存的场景时，“时间滑块”(Time Slider)中的已修改区域就会变为灰色以显示已过期的动画片段，然后再次变为蓝色以表明这些值已更新。这称为**缓存失效**。有关此过程的详细信息，请参见[“缓存播放”(Cached Playback)状态行的状态](使用“缓存播放”%28Cached%20Playback%29以提高播放速度/“缓存播放”%28Cached%20Playback%29状态行的状态.md)。

**注**

有关

“缓存播放”(Cached Playback)

的技术详细信息，请参见

Maya 缓存播放白皮书

。

#### 自定义缓存播放

在[缓存播放首选项(Cached Playback Preferences)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3CB35662-DB1D-4CF3-9135-E09B973635DE)中，您可以指定以下设置：

- “缓存播放”(Cached Playback)状态行的显示方式和位置

- 填充缓存的时间和方向

- 要为“缓存播放”(Cached Playback)分配的内存量

**注**

对“缓存播放”(Cache Playback)状态行的外观所做的更改会影响“动画”(Animation)和“动力学”(Dynamics)缓存条带。

您可以更改“时间滑块”(Time Slider)上“缓存播放”(Cached Playback)的每个部分的默认颜色。您可以为缓存帧、未缓存帧和无效帧以及子帧拾取颜色。您甚至可以使用不透明度设置来设置“缓存播放”(Cached Playback)状态行的透明度。请参见[颜色设置(Color Settings)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1FC6CC4E-6C21-44FA-A58B-AC31ED57B591)窗口的“缓存播放”(Cached Playback)部分。

## 我何时需要使用播放预览？

“缓存播放”(Cached Playback)意味着您不再需要仅为查看工作结果而创建播放预览。但是，有时仍建议使用播放预览：

- 您的场景具有禁用缓存的设置（有关缓存限制的列表，请参见[“缓存播放”(Cached Playback)限制](使用“缓存播放”%28Cached%20Playback%29以提高播放速度/“缓存播放”%28Cached%20Playback%29限制.md)。）

- 播放时，即使已启用“缓存播放”(Cached Playback)，播放速度仍然不够快

- 您想要创建视频以发送供审阅

但是，如果使用缓存播放的速度会更快，播放预览性能也将从这一改进中受益。

## “缓存播放”(Cached Playback)限制

虽然“缓存播放”(Cached Playback)适用于 Maya 中的大多数动画，但一些方面仍然不受支持，例如 Trax 和 XGen 等非线性动画。

如果“缓存播放”(Cached Playback)在将数据发送到缓存时遇到错误，状态行和“缓存播放”(Cached Playback)图标会变为黄色，以表明缓存已禁用，并且处于安全模式。有关您可以执行哪些操作以修复这种情况的详细信息，请参见[“缓存播放”(Cached Playback)状态行的状态](使用“缓存播放”%28Cached%20Playback%29以提高播放速度/“缓存播放”%28Cached%20Playback%29状态行的状态.md)主题中的**“安全模式”**。

有关禁用“缓存播放”(Cached Playback)的时间的列表，请参见[“缓存播放”(Cached Playback)限制](使用“缓存播放”%28Cached%20Playback%29以提高播放速度/“缓存播放”%28Cached%20Playback%29限制.md)和[“缓存播放”(Cached Playback)不支持的节点](使用“缓存播放”%28Cached%20Playback%29以提高播放速度/“缓存播放”%28Cached%20Playback%29限制/“缓存播放”%28Cached%20Playback%29不支持的节点.md)。
