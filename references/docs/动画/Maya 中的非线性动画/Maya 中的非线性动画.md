# Maya 中的非线性动画

按照可重新排列和编辑的序列（如非线性编辑器中的电影片段）集合动画。

用关键帧或运动捕捉为角色或对象设置动画后，您可以将其动画数据排列成单个可编辑序列。此动画序列称为动画片段。尽管您可以考虑到特定情节，按特定属性创建动画片段，但非线性动画会参考移动、重新排列、操纵和融合这些片段的过程，以生成新的一系列运动。

在 Maya 中，有两种类型的片段：源片段和常规剪辑。Maya 通过将角色的原始动画曲线保存在源片段中，来保留及保存角色原始动画曲线。请勿使用源片段为角色设置动画。但是，您可以使用源片段（称为*常规片段*）的副本或*实例*以非线性方式为角色设置动画。请参见[动画片段](Maya%20中的非线性动画/Trax%20编辑器/Trax%20中的非线性动画组件/Trax%20中的片段.md#GUID-D462A79C-A766-43DD-BB43-5BCDAEC5D8BD__WS17956D7ADBC6E736B6BA507117AE308213-7FF6)。

通过“时间编辑器”(Time Editor)，可以使用基于片段的非线性工作流组合、混合与编辑动画。可以将任何对象或属性导入 Maya，然后在时间编辑器中将其作为片段设置关键帧，您可通过非破坏性方式对其进行编辑，以便尝试场景中元素的不同组合和变化，然后可以进行烘焙，使其可用于 Maya。

非线性动画的基础是，移动、操纵和融合常规片段，从而为角色生成一系列平滑的动作。在 Maya 中，可以使用“Trax 编辑器”(Trax Editor)管理角色的非线性动画的所有这些方面。

您也可以使用“摄影机序列器”(Camera Sequencer)，通过它可以布置和管理摄影机快照，然后在场景中生成动画的一段渲染影片镜头。在“摄影机序列器”(Camera Sequencer)中，快照表示为排列在轨迹上的一组矩形，您可以通过操纵摄影机快照来定义和操纵在任意时间点哪个摄影机处于活动状态。如果您对摄影机的布局和计时满意，则可以播放预览动画的影片片段。

## 什么是时间编辑器？

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-4707C3B1-C599-44A9-98CA-980A1BD634D5.png) <!-- baize:img-hook downloaded=false reason="正文 2784 字 ≥300，非承重" -->

时间编辑器是一个非线性动画编辑器，支持您在易于使用的工作流中编辑和管理许多实际装备/角色。时间编辑器可用于对动画进行高级控制，使您可以一种非线性、非破坏性方式对序列进行分层和混合。它有助于您重用和微调使用关键帧、表达式和约束创建的动画。

### 相关主题

- [时间编辑器](../时间编辑器/时间编辑器.md)

## 什么是“Trax 编辑器”(Trax Editor)？

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-9129C493-8B2B-4C91-A5B5-6178E7404A4E.png) <!-- baize:img-hook downloaded=false reason="正文 2784 字 ≥300，非承重" -->

“Trax 编辑器”(Trax Editor)是一种高级动画工具，可用于选择和控制角色及其动画片段、层和融合动画序列，同步动画和音频片段，以及在映射的角色之间拖放动画片段。请参见手册的“角色设置”部分的[在角色之间映射动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-AAF92442-CDC0-46C2-B55C-276D75D292DE)。可以使用“Trax 编辑器”(Trax Editor)处理除运动路径动画以外任何类型的动画。

例如，假定您已为角色的行走设置关键帧，并且现在希望将其变成循环行走。可以为关键帧动画序列创建片段，缩放并修剪该片段使其具有合适的长度以及类似的开始姿势和结束姿势，然后循环片段以创建正确的循环行走。如果要更改循环行走的步调或节奏，可以为片段创建时间扭曲曲线，或者如果要将行走变成行进，可以直接操纵角色和关键帧进行剪辑。由于您正在使用片段，因此可以对该角色的行走序列执行所有这些操作，而不破坏原始关键帧动画。

### 相关主题

- [Trax 编辑器(Trax Editor)](Maya%20中的非线性动画/Trax%20编辑器.md)

- [Trax 中的非线性动画组件](Maya%20中的非线性动画/Trax%20编辑器/Trax%20中的非线性动画组件.md)

## 什么是摄影机序列器？

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-5A770AA6-73E3-4DBD-A828-3F609C2CD7A8.png) <!-- baize:img-hook downloaded=false reason="正文 2784 字 ≥300，非承重" -->

“摄影机序列器”(Camera Sequencer)是可用于创建、重新排列和操纵场景的摄影机快照的一种工具。每个快照定义了在任一特定时间处于活动状态的摄影机及其持续时间。

通过调整摄影机快照的放置和计时，可有效地管理场景中动画的“拍摄”。在“摄影机序列器”(Camera Sequencer)中完成操纵摄影机快照后，即可将序列播放预览到渲染的影片片段中。

**注**

注意：

(Mac OS X) 在 64 位系统上的“摄影机序列器”(Camera Sequencer)支持受限。为获得更好的性能和实时结果，在 32 位模式下运行 Maya 以使用“摄影机序列器”(Camera Sequencer)。

另请参见[摄影机序列器](Maya%20中的非线性动画/摄影机序列器%28Camera%20Sequencer%29.md)。

## 什么是“角色映射器”(Character Mapper)？

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-2419F708-E5DF-43A4-81E5-89569D336630.png) <!-- baize:img-hook downloaded=false reason="正文 2784 字 ≥300，非承重" -->

使用“角色映射器”(Character Mapper)窗口可以创建源角色和目标角色的节点或属性之间的对应关系，以便通过“Trax 编辑器”(Trax Editor)在映射的角色之间导入和导出或复制并粘贴动画片段。

### 相关主题

- [角色映射器(Character Mapper)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-20015023-4D8F-4D09-8F82-15D3A80A1554)

- [将一个角色映射到另一个角色](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-47CB74C4-4031-4A99-BB06-65D0D148FFC4)

- [在角色之间映射动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-AAF92442-CDC0-46C2-B55C-276D75D292DE)

## 什么是“Visor”、“大纲视图”(Outliner)和“片段库”(Clip Library)？

处理非线性动画时，可以通过以下三种方法访问片段：

- 将源片段从“Visor”拖放到“Trax 编辑器”(Trax Editor)

- 将常规或源片段从“大纲视图”(Outliner)拖放到“Trax 编辑器”(Trax Editor)

- 在“Trax 编辑器”(Trax Editor)中使用“片段库”(Clip Library)将源片段插入到其各自的角色

请参见[源片段](Maya%20中的非线性动画/Trax%20编辑器/Trax%20中的非线性动画组件/Trax%20中的片段.md#GUID-D462A79C-A766-43DD-BB43-5BCDAEC5D8BD__WS17956D7ADBC6E736B6BA507117AE308213-7FF5)和[常规片段](Maya%20中的非线性动画/Trax%20编辑器/Trax%20中的非线性动画组件/Trax%20中的片段.md#GUID-D462A79C-A766-43DD-BB43-5BCDAEC5D8BD__WS17956D7ADBC6E736B6BA507117AE308213-7FF4)

**注**

在可以将片段从一个角色拖放或复制并粘贴到另一个角色之前，必须首先映射角色。请参见手册的“角色设置”部分的[在角色之间映射动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-AAF92442-CDC0-46C2-B55C-276D75D292DE)。

### Visor

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-DEBC2EF4-8D60-4A0B-B74B-7FCB799F19E2.png) <!-- baize:img-hook downloaded=false reason="正文 2784 字 ≥300，非承重" -->

“Visor”将场景中的所有源片段都列为图标。可以在“Visor”中选择一个片段图标，然后使用鼠标中键将该片段拖到轨迹视图区域中的角色。将片段从“Visor”拖动到 Trax 中的角色上会将选定片段的副本添加到该角色。请参见[将 Visor 与 Trax 结合使用](Maya%20中的非线性动画/Trax%20编辑器/将“大纲视图”%28Outliner%29和“Visor”与%20Trax%20结合使用/将“Visor”与%20Trax%20结合使用.md)和 [Visor](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0065E2FA-EC3E-4BBD-A896-043621AD35D2)。

“Visor”包含四个选项卡，可用于查看场景的非线性动画数据。可以从“角色片段”(Character Clips)*、*“角色姿势”(Character Poses)*、*“未使用的片段”(Unused Clips)*和“未使用的姿势”(Unused Poses)选项卡中访问场景中的所有源片段和姿势*。场景中角色使用的所有片段将显示在“角色片段”(Character Clips)和“角色姿势”(Character Poses)选项卡中。场景中存在但角色未使用的所有片段和姿势将显示在“未使用的片段”(Unused Clips)和“未使用的姿势”(Unused Poses)选项卡中。

### 大纲视图(Outliner)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-48C43B31-515C-48EA-97E6-E57F9FA17B20.png) <!-- baize:img-hook downloaded=false reason="正文 2784 字 ≥300，非承重" -->

“大纲视图”(Outliner)将场景中的所有源片段和常规片段都列为文字。可以在“大纲视图”(Outliner)中选择一个片段名称，然后使用鼠标中键将该片段拖到轨迹视图区域中的角色。将片段从“大纲视图”(Outliner)拖动到 Trax 中的角色上会将选定片段的副本添加到该角色。请参见[将大纲视图与 Trax 结合使用](Maya%20中的非线性动画/Trax%20编辑器/将“大纲视图”%28Outliner%29和“Visor”与%20Trax%20结合使用/将“大纲视图”%28Outliner%29与%20Trax%20结合使用.md)、[将 Visor 与 Trax 结合使用](Maya%20中的非线性动画/Trax%20编辑器/将“大纲视图”%28Outliner%29和“Visor”与%20Trax%20结合使用/将“Visor”与%20Trax%20结合使用.md)和 [Visor](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0065E2FA-EC3E-4BBD-A896-043621AD35D2)。

### 片段库(Clip Library)

“片段库”(Clip Library)是“Trax 编辑器”(Trax Editor)中的一个菜单，可用于为“Trax”中加载的所有角色创建源片段和姿势的副本。从“库”(Library)中选择源片段或姿势时，会创建选定片段或姿势的副本，并将其插入到其在 Trax 中对应的角色。有关详细信息，请参见[将源片段复制到角色](Maya%20中的非线性动画/Trax%20编辑器/选择和编辑源片段/将源片段复制到角色.md)和 。
