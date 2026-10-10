# 最有效地使用 Maya

一般来说，当您使用最新的显卡驱动程序和硬件时，Maya 运行效果最好。您可以检查硬件在 [Maya 认证硬件](https://knowledge.autodesk.com/zh-hans/support/maya/troubleshooting/caas/simplecontent/simplecontent/CHS/content/maya-certified-hardware.html)列表上是否受支持。

使用以下最佳实践以优化性能。

## 交互式绘图

- 为获得最佳视口性能，请参见[优化 Viewport 2.0](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B7C04719-3D25-4A02-9F90-96208FB223C2) 中的提示。

- 启用“着色 > 交互式着色”(Shading > Interactive Shading)以提高移动摄影机时的性能。

- 将文件以最简单的显示模式保存以缩短加载时间。避免以纹理显示模式保存文件。

- 使用多边形的默认显示选项。

- 关闭所有非必要的 UI 的显示，这些 UI 随场景视图的更新而更新，例如：“平视显示仪”(Heads Up Display)、“时间滑块”(Time Slider)、范围滑块(Range Slider)、“Hypershade”、“属性编辑器”、“UV 纹理编辑器”(UV Texture Editor)。

- 关闭所有非必要的场景元素的显示，范围从栅格到绘图骨架。

- 使用仅包含单个建模面板的布局。

- 通过执行以下操作以有效地划分场景：

  - 将场景转分段成不重叠的区域（例如，使用栅格布局）。

  - 使用显示层来根据要求打开或关闭区域的显示。

  将场景拆分到不重叠的矩形栅格也有助于设置可见性层，因为可以逐个区域设置场景。但是，请注意，Maya 针对每个对象执行前、后和侧摄影机视锥消隐。因此，即使只显示了一个三角形，Maya 也会完整地绘图。

- 使用硬件“Mipmap”的过滤选项，这些选项位于着色器节点的“硬件纹理”(Hardware Texturing)部分的“纹理过滤器”(Texture Filter)下拉列表中。

- 启用“使用默认材质”(Use default material)显示模式（如果适用）。

- 如果不需要，不要使用额外的“着色”(Shading)菜单设置，例如，“着色对象上的线框”(Wireframe on Shaded)。

- 如果可能，使用“显示 > 隔离选择”(Show > Isolate Select)来限制场景中显示和刷新的内容。

- 如果对象具有的三角形不足几百个，特别是如果只具有几个三角形时，这些对象将具有较高的性能开销。如果可能，将这些对象合并为一个对象。与对象很多但每个对象只具有几个三角形相比，对象较少但每个对象具有数千个三角形时 Maya 的性能更高。

- 尽可能使用实例化。这包括实例化几何体、材质和纹理。如果使用文件纹理节点，最好使用实例化的一个文件纹理节点，而不是使用该节点的多个副本。这将影响文件加载时以及在磁盘上占用的内存。

- 请确保将显卡设定为 Maya 设置并禁用垂直同步（同步）。

  - 默认材质显示选项可以用于查看针对所有对象使用 1 个着色器与使用 *n* 个着色器之间的差别。

  - 如果将曲面划分为许多层，这可能会减慢着色模式显示。如果可能，尝试使用较少的划分，如果使用划分，为了可见性应将曲面划分成为栅格区域。这有助于实现可见性消隐。

- 尽量尝试构建边界（边界框）彼此不相交的曲面。可见性测试性能在这些情况下较差。

- 按显示属性类型对 DAG 层次进行排序可能会有所帮助。此操作可以通过在“大纲视图”(Outliner)中重新排序 DAG 对象来完成。

- 对 DAG 层次进行排序可能有助于：

  - 首先是所有曲面，然后是所有非曲面

  - 按在给定区域内的可见性（如果层用于可见性划分，则可能是按层）

  - 按到查看器的深度（如果可行）

  - 材质和照明属性：例如，依次是所有 lambert、所有 blinn、所有不使用照明的着色器、所有使用照明的着色器、所有不具有透明度的着色器、所有具有透明度的着色器

- 针对对象尽量使用最少的着色器。例如，当不需要照明时可以使用一个曲面着色器，否则将替代其他位置的光源，例如逐顶点颜色。

- 移除重复的着色网络。

## 内存

- 不受限制的撤消队列比受限制的撤消队列占用更多的内存。在“首选项”(Preferences)窗口中默认“撤销”(Undo)队列设置为 50。

- 利用在 Windows XP 上高达 3 GB 的大地址识别能力。

- 尽可能使用实例化。这包括几何体、材质、纹理、灯光等等。

- 平行内存复制可能在某些情况下提高 Opterm 或 Nehalem 系统的速度。但是，也会潜在减慢 Xeon 系统。如果发现速度已受到影响，使用 MAYA_NO_PARALLEL_MEMCPY 以禁用平行内存复制。但是，请注意，在 Maya 中还有其他因素可能会影响速度，例如场景的复杂性和工作量。

### IK、依存关系循环和性能

- 加载文件后，等待光标可能会出现而且 Maya 将较长时间（至少几分钟）地使用所有可用 CPU 周期。该问题似乎出现在具有 IK 和依存关系循环的文件。

  理想的解决方法是找到并移除依存关系循环。这些循环可能很难查找。例如，A 可能为 pointConstraint B 所转换，B 使用目标 C，C 的父是 D，D 为表达式 E 所旋转，E 有一个输入 F，F 受约束于 G，而 G 是 A 的一个子对象。一个提示是查找具有在许多不同节点上的属性输出的表达式。

  即，有些复杂场景需要花费很长的时间来进行求值，在加载文件时可能会遇到这种情况。

### 多边形绘图缓存

- 在 Maya 中，使用多边形绘图缓存通常可以提高速度和性能。但是，在 Maya 中加载某些非常大的文件时，多边形绘图缓存可能导致 Maya 使用的内存超过在系统上应用程序的可用内存，从而导致不稳定。

  （注意：在 Windows 和 Linux 上的 64 位版本的 Maya 提供了足够的内存空间从而不会出现此问题。）

  也可以禁用多边形绘图缓存，以便可以更轻松地加载非常大的文件。有一个环境变量称为 MAYA_DISABLE_POLYGON_DRAW_CACHE。将其设置为 1 以禁用多边形绘图缓存。

  如果禁用多边形绘图缓存，交互式绘图性能将减慢。建议您不要使此环境变量设置为 1，而是仅在处理出现此问题的文件时将其这样设置。

## 动画

  请参见[使用求值管理器提高性能](使用解算管理器提高性能.md)主题了解如何通过“求值管理器”(Evaluation Manager)同时提高播放和操纵角色装备的速度。新系统是多线程的，以利用可用的计算资源（核心和图形处理器）。

- 使用“蒙皮 > 编辑影响 > 设置最大影响”(Skin > Edit Influences > Set Max Influences)可限制最大影响，移除未使用的影响并删减小影响。

- 使用“编辑变形器 > 删减成员身份”(Edit Deformers > Prune Membership)命令移除不受变形器影响的组件。

  使用“分析器”(Profiler)。“分析器”(Profiler)允许您通过录制和演示每个过程消耗的时间量（以图表的形式呈现），定位场景内的性能瓶颈。详细信息请参见[分析场景以提高性能](分析场景以提高性能.md)。

## 音频

- 当在 Maya 中使用导入的音频文件时，不建议有使用音频功能的背景应用程序在运行。运行使用音频的其他应用程序可能会导致 Maya 挂起。

## 毛发

- 降低“毛发反馈”(Fur Feedback)头发的“毛发精确度”(Fur Accuracy)值显著地增加交互式绘图速度，但会造成不太容易预览“扭曲度”(Scraggle)、“卷曲”(Curl)或“成束”(Clumping)。

- 由于“阴影贴图”(Shadow Maps)的渲染成本很高，只有在需要时才使用。Autoshading 的成本很低，并且在使用“Maya 软件”(Maya Software)渲染器时可以为一些灯光提供一种可接受的替代方案。

## 杂项

- 在 Windows 上，碎片化的硬盘驱动器会导致严重的性能问题。建议使用专用的应用程序定期且彻底地消除碎片化。由操作系统提供的标准工具通常不足以获得性能优势。

- 利用文件引用。详细信息请参见[文件引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-238914C9-4129-454C-99D7-B8C57AF423DB)。

- 熟练掌握[性能设置(Performance Settings)](性能设置%28Performance%20Settings%29.md)。（Windows > 设置/首选项 > 性能设置(Windows > Settings/Preferences)）。

- 使用“文件 > 优化场景大小”(File > Optimize Scene Size)移除未使用的场景数据。

- 在屏幕保护程序激活后返回 Maya 可能在一些使用旧的或低端显卡的机器上导致选择蚂蚁线或面板内容消失。

  按空格键或使用“布片”菜单来更改当前的“面板”(Panels)配置。所有面板现在应正常绘图。若要返回到上一个配置，请再次按空格键，或者从“面板”(Panels)菜单选择相应的条目。

- 发生在属性求值期间的循环检查可能会丢失一个循环，在此循环中 DAG 节点上的传入连接形成一个在其子节点上包含任何世界空间属性的循环。如果怀疑有这样的情况，可以用 MEL 命令 *cycleCheck* NODE 来检测这些周期。

## 建模

- 使用多边形的“重用三角形”(Reuse Triangles)属性。

- 使用“多边形减少”(Poly Reduce)来简化复杂的几何体。不具有以下特征的多边形模型将显示得更快：非共享法线、非共享纹理坐标、未映射面和不是三角形的面（未三角化）。

## 动力学

- 使用刚体几何体的“替代对象”(Stand In)属性。

- 当开始或设置模拟时，在粒子上使用较少的几何体。

## 经典布料

- 针对初始设置和模拟测试，禁用“经典布料”(Classic Cloth)碰撞。

- 动画设置例如“帧示例”(Frame Samples)和“时间步长”(Time Step Size)等属性，以减少解算时间。

- 在批处理模式下解算

## 渲染

- 使用“渲染诊断”(Render Diagnostics)来获得在提高性能方面的提示。详细信息请参见 [Maya 渲染诊断](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E3202038-06CF-44D6-BDEC-03ED3187B82F)。

- 移除重复的着色网络。

## Artisan

- 如果可能，增加“图章间距”(Stamp Spacing)（“Artisan 工具”(Artisan Tool)的设置编辑器中的“笔划”(Stroke)区域）。

- 如果可能，使用“屏幕投影”(Screen Projection)（“Artisan 工具”(Artisan Tool)的设置编辑器中的“笔划”(Stroke)区域）。

## Paint Effects

- 在“Paint Effects 工具”(Paint Effects Tool)的设置编辑器中降低“显示质量”(Display Quality)。
