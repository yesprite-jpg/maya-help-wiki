# Trax 中的片段

## 动画片段

片段是 Maya 中非线性动画的基本组件。片段是角色的动画曲线组合。如果为尚不是角色集一部分的已设置动画对象创建片段，“Trax 编辑器”(Trax Editor)将自动为该片段创建角色。请参见[角色、组和子角色](角色、组和子角色.md)。

通过片段，您可以将角色的关键帧或运动捕捉动画曲线聚成一束，这样您就能够以非线性方式操纵角色的动画数据。

创建片段时，系统将生成两种片段：源片段和常规片段。

源片段将添加到角色的场景中，常规片段将插入“Trax 编辑器”(Trax Editor)中该片段角色的下方。有关创建片段时 Maya 依存关系图 (DG) 中所发生内容的低级别信息，请参见 [animClip](../../../../动画引用/动画引用/动画节点/animClip.md)。另请参见[依存关系图](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-51096BC4-32B7-4391-BE39-21641B374745)。

### 源片段

源片段可以在“Visor”、“大纲视图”(Outliner)和“库”(Library)中找到。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-961063EC-B761-4BDE-8A2C-9E7293703286.png) <!-- baize:img-hook downloaded=false reason="正文 2029 字 ≥300，非承重" -->

源片段包含将原始的未操纵关键帧动画数据变成片段时的这些原始未操纵关键帧动画数据。源片段不会显示在“Trax 编辑器”(Trax Editor)中。相反，Maya 会将源片段保存在“Trax 编辑器”(Trax Editor)外部，以防原始动画曲线被意外修改，并确保您具有可以还原到的未经修改片段。

每个常规片段都是源片段的一个实例。更改源片段的属性时，也将修改“Trax 编辑器”(Trax Editor)中源片段的每个常规片段。

源片段可以从 Trax 中的“Visor”、“大纲视图”(Outliner)或“库”(Library)菜单访问。请参见[什么是 Visor、大纲视图和片段库？](../../../Maya%20中的非线性动画.md#GUID-B90726CA-6C86-4E9B-80F3-1F65745C3B3F__WS17956D7ADBC6E736B6BA507117AE308213-7FFB). 通过在“通道盒”(Channel Box)中修改源片段的属性，可以编辑源片段。请参见[编辑源片段](../选择和编辑源片段/编辑源片段.md)。

### 常规片段

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-DDEB63B5-DF00-4D22-AB86-1DD4F97148BD.png) <!-- baize:img-hook downloaded=false reason="正文 2029 字 ≥300，非承重" -->

常规片段是其源片段子对象或实例的动画片段。常规片段的播放范围可以是源片段中存储的部分范围或全部范围。请参见[源输入/输出](../轨迹视图区域.md#GUID-42EF9259-F328-421D-823C-2571717EB564__WS17956D7ADBC6E736475032DC117AE308AAE-7F79)。显示在“Trax 编辑器”(Trax Editor)中的动画片段是常规片段。

常规片段可以从“Trax 编辑器”(Trax Editor)或“大纲视图”(Outliner)访问。通过在“Trax 编辑器”(Trax Editor)中修改常规片段或在“属性编辑器”(Attribute Editor)中更改常规片段属性，可以编辑常规片段。

### 表达式片段和约束片段

可以使用表达式或约束为动画创建特殊片段。表达式片段和约束片段可以仅包含表达式或约束通道。通过将表达式和约束与常规动画片段分开，Maya 可以让用户进一步控制它们在角色动画中的生效时间以及包含在片段的表达式或约束的范围。

例如，如果设置动画的角色具有关键帧动画通道和表达式通道，则您需要为关键帧通道创建常规片段，为角色的表达式通道创建单独的表达式片段。请参见[创建表达式片段或约束片段](../创建片段和姿势/创建表达式片段或约束片段.md)。

在“Trax 编辑器”(Trax Editor)中，可以如常规动画片段一般访问和编辑表达式片段和约束片段。

### 摘要片段

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-CAB17363-A605-4FB0-B2FA-B9BD34F3D85D.png) <!-- baize:img-hook downloaded=false reason="正文 2029 字 ≥300，非承重" -->

摘要片段代表对象所有片段的累积范围，可以让您同时移动对象中的所有片段。请参见[摘要](../轨迹视图区域.md#GUID-42EF9259-F328-421D-823C-2571717EB564__WS17956D7ADBC6E736475032DC117AE308AAE-7F7D)。

### 您可以对动画片段执行什么操作？

您可以对片段执行以下操作：

- 将片段移动到不同的播放时间

- 循环片段以重复动画。请参见[循环片段](../操纵片段/循环片段.md)。

- 保持片段以将其动画冻结为指定帧数的特定姿势。请参见[保持片段](../操纵片段/保持片段.md)。

- 分割、修剪、复制或合并片段以创建新的动画片段。请参见[分割片段](../操纵片段/分割片段.md)、[合并片段](../操纵片段/合并片段.md)和[复制片段](../创建片段和姿势/复制片段.md)。

- 融合动画片段以创建片段之间的平滑过渡。请参见[创建和编辑融合](../操纵片段/创建和编辑融合.md)。

- 在片段中设置关键帧到片段以更改或添加到片段中的动画曲线。请参见[在片段中设置关键帧](../操纵片段/在片段中设置关键帧.md)和[活动/非活动片段](Trax%20中的片段/片段状态.md#GUID-968254A9-1044-4887-8197-63A41D0DE05A__WS17956D7ADBC6E736475032DC117AE308AAE-7F6F)。

- 同步单个角色或多个角色的片段

- 为片段创建时间扭曲以更改片段计时，而不修改片段的动画曲线。请参见[创建和编辑时间扭曲](../操纵片段/使用%20Trax%20创建和编辑时间扭曲.md)。

- 在映射角色之间复制片段。请参见[在角色之间映射动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-AAF92442-CDC0-46C2-B55C-276D75D292DE)。

- 导入和导出片段。请参见[导入或导出动画片段](../操纵片段/导入或导出动画片段.md)。

- 将源片段从“Visor”或“大纲视图”(Outliner)拖放到“Trax 编辑器”(Trax Editor)中。请参见[将 Visor 与 Trax 结合使用](../将“大纲视图”%28Outliner%29和“Visor”与%20Trax%20结合使用/将“Visor”与%20Trax%20结合使用.md)和[将大纲视图与 Trax 结合使用](../将“大纲视图”%28Outliner%29和“Visor”与%20Trax%20结合使用/将“大纲视图”%28Outliner%29与%20Trax%20结合使用.md)。

请参见[片段交互控件](../轨迹视图区域.md#GUID-42EF9259-F328-421D-823C-2571717EB564__WS17956D7ADBC6E736475032DC117AE308AAE-7F78)和[片段状态](Trax%20中的片段/片段状态.md)。

## 音频片段

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-170E1162-1031-4508-94FC-1EF051C9CD41.png) <!-- baize:img-hook downloaded=false reason="正文 2029 字 ≥300，非承重" -->

音频片段是包含音频文件数据的片段。将 .wav 或 .aiff 文件导入到“Trax 编辑器”(Trax Editor)中时，这些音频文件将在“声音轨迹”(Soundtrack)下显示为音频片段。请参见[声音轨迹](../轨迹视图区域.md#GUID-42EF9259-F328-421D-823C-2571717EB564__WS17956D7ADBC6E736475032DC117AE308AAE-7F7B)。使用 Trax 中的音频片段可以设定动画数据的计时以及它们各自的音频文件。

在动画播放过程中，一次只播放一个音频片段，且音频片段的播放优先级是从最顶层的片段到最底层的片段。例如，您有时间上重叠的多个音频轨迹和片段，则将总是播放最顶层轨迹中的音频片段，而不是播放 Trax 时间轴上相同位置处其他轨迹上的其他音频片段。

不能在 Trax 中操纵（修剪、缩放、分割等）音频片段。只能沿 Trax 时间轴移动音频片段。请参见[在 Trax 中处理音频](../在%20Trax%20中处理音频.md)。

**注**

如果要在动画播放过程中听到“声音轨迹”(Soundtrack)中出现的音频片段，请参见[在 Trax 中处理音频](../在%20Trax%20中处理音频.md)。当音频片段在播放过程中可听见时，它们的位置和长度将通过“时间滑块”(Time Slider)中的水平绿色线表示。
