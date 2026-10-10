# “缓存播放”(Cached Playback)限制

当“缓存播放”(Cached Playback)遇到不受支持的节点而无法将动画发送至内存时，将进入“安全模式”。“安全模式”通过变黄的“缓存播放”(Cached Playback)状态行和图标表示，缓存被禁用。有关“安全模式”的详细信息，请参见[“缓存播放”(Cached Playback)状态行的状态](“缓存播放”%28Cached%20Playback%29状态行的状态.md)。

**注**

有关

“缓存播放”(Cached Playback)

的技术详细信息，请参见

Maya 缓存播放白皮书

。

如果“缓存播放”(Cached Playback)的内存即将用完，将在[帮助行](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-AD137576-F1CF-4A62-A7DA-E0ECF6524D11)上显示警告消息。您可以使用[范围滑块(Range Slider)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E9E054A1-A5D0-412C-976A-F57C0F6960B1)缩小播放范围，或者在[缓存播放首选项(Cached Playback Preferences)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3CB35662-DB1D-4CF3-9135-E09B973635DE)中为缓存进程分配更多内存。如果已达到分配的内存限制，缓存将停止，但您可以继续工作。

您可以打开[脚本编辑器(Script Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7C861047-C7E0-4780-ACB5-752CD22AB02E)查看状态消息，或在[解算工具包](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E22B253D-914B-4056-93F5-755702A6C998) **“缓存播放”(Cached Playback)**部分运行安全模式测试以查找问题的根源。

**注**

缓存播放首选项(Cached Playback Preferences)

中有一个

“显示警告框”(Show Warning Frames)

设置，允许您禁用黄色的“安全模式”通知。

下面列出了“缓存播放”(Cached Playback)工作流的一些限制：

#### 图形

**注**

重要：

动力学模拟和非线性动画（例如 Trax）以及与 XGen 相关的功能等许多情况均不支持“缓存播放”(Cached Playback)。通过启用[缓存动力学(Cache dynamics)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3CB35662-DB1D-4CF3-9135-E09B973635DE#GUID-3CB35662-DB1D-4CF3-9135-E09B973635DE__GUID-1812231C-7513-477A-AEAD-726EF185CF90)，可支持 [nParticle](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-92319246-4DE6-4B08-AAF0-9BD86A6A8855) 和 [nCloth](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-ED791F1C-8412-4785-829F-9925F2604E8A) 缓存。有关禁用缓存过程的不受支持节点的列表，请参见[“缓存播放”(Cached Playback)不支持的节点](“缓存播放”%28Cached%20Playback%29限制/“缓存播放”%28Cached%20Playback%29不支持的节点.md)。

##### 受支持

- 支持**已设置动画的可见性**，但是无法充分利用缓存系统。这可能会影响性能，因为具有已设置动画的可见性的几何体可能会重新计算而不是缓存。

- 支持**已设置动画的几何体拓扑**，但是无法充分利用缓存系统。这可能会影响性能，因为具有已设置动画的拓扑的几何体可能会重新计算而不是缓存。

##### 不受支持

- 缓存**平滑网格预览**在 Maya Catmull-Clark 模式下无法正常工作，但 OpenSubdiv 平滑模式可处理缓存。在[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)的“平滑网格”(Smooth Mesh)区域中，禁用**“平滑网格预览”(Smooth Mesh Preview)**选项。

- 不支持切换**显示模式**（线框与多边形，平滑着色与平面着色，等等）。一旦更改显示模式，则需要重建缓存。

#### 工作流

- 由于“缓存播放”(Cached Playback)依赖于[解算管理器 (EM)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-190D97E7-9AC0-4D67-8A07-1AF3A9DBAF15.htm)，因此任何禁用 EM 的流程也将禁用“缓存播放”(Cached Playback)。这包括使用[运动模糊](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-45711A48-3358-42A5-B96F-41CD07FC8760)，或当场景包含某些[经典动力学](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8A3373A4-7480-43AF-9A45-FD0E8AA3590B)（例如，粒子、布料、刚体）时。

  **注**

  提示：

  您可以运行脚本来返回导致解算管理器出现问题的动力学节点的列表。请参见

  识别制约性能的动力学节点

  。

- 当您移动摄影机视图（例如，推拉、翻滚、动态观察或缩放）时，“缓存播放”(Cached Playback)会暂时停止。**解决方法**：让“缓存播放”(Cached Playback)状态行完全填满[时间滑块(Time Slider)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-827ED8CD-C6AA-4495-8B5E-2FC98C8D49EE.htm) ，然后再更改摄影机视图。

- 由于细分网格所使用的内存量，“平滑网格预览”(Smooth Mesh Preview)会大大降低“缓存播放”(Cached Playback)的速度。**解决方法**：在[缓存播放首选项(Cached Playback Preferences)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3CB35662-DB1D-4CF3-9135-E09B973635DE)中禁用**“缓存平滑网格”(Cache Smooth Meshes)**。

- 解算图拓扑更改不会触发图表（和“播放缓存”(Playback Cache)）重建。仅在下一次解算时重建，而不是当前解算。这是因为当前场景可能会有变化。

- 释放（或清除）缓存（例如，使用“文件 > 新建”(File > New)进行完全缓存时）可能需要一些时间，并且会导致 Maya 暂停。
