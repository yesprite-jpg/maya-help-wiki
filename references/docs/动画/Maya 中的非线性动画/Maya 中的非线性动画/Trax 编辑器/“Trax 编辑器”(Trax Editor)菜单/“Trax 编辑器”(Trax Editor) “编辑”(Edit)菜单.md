# “Trax 编辑器”(Trax Editor)  “编辑”(Edit)菜单

#### 撤消(Undo)

删除“Trax 编辑器”(Trax Editor)中的上一个操作。

#### 重做(Redo)

重复“Trax 编辑器”(Trax Editor)中删除的上一个操作。

#### 剪切(Cut)

*仅用于动画片段。*

从“Trax 编辑器”(Trax Editor)移除选定动画片段并存储在系统的虚拟剪贴板中。请参见[剪切、复制和粘贴 Trax 片段](../创建片段和姿势/剪切、复制和粘贴%20Trax%20片段.md)。

#### 复制(Copy)

*仅用于动画片段。*

复制“Trax 编辑器”(Trax Editor)中的选定动画片段并存储在系统的虚拟剪贴板中。

#### 粘贴(Paste)

*仅用于动画片段。*

将系统虚拟剪贴板中复制或剪切的动画片段粘贴到“Trax 编辑器”(Trax Editor)中亮显的“角色”(Character)。

选择“编辑 > 粘贴”(Edit > Paste) > ![图：选择“编辑 粘贴”(Edit Paste) 以打开“粘贴片段选项”(Paste Clip Options)： 粘贴方法(…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4894 字 ≥300，非承重" --> 以打开“粘贴片段选项”(Paste Clip Options)：

##### 粘贴方法(Paste Method)

如果要将复制或剪切的动画片段粘贴到其他角色，请选择一种“粘贴方法”(Paste Method)。

**注**

只应在

已映射

角色之间复制和粘贴片段。请参见

将一个角色映射到另一个角色

。

###### 按属性名称(By Attribute Name)

将属性值粘贴到目标角色集的匹配属性名称。对象名称将被忽略。

###### 按属性顺序(By Attribute Order)

根据“通道盒”(Channel Box)中的属性顺序（降序）将属性值粘贴到目标角色集。

###### 按节点名称(By Node Name)

将属性值粘贴到目标角色集的匹配对象和属性名称。

###### 按角色映射(By Character Map)

仅在计划导出目标角色的角色映射时才选择该选项。请参见[导入或导出动画片段](../操纵片段/导入或导出动画片段.md)。

##### 开始帧(Start Frame)

指定将复制的动画片段粘贴到何处。

###### 当前时间(Current Time)

如果启用，已复制片段将被粘贴到 Trax 当前时间指示器位置的源片段轨迹。例如，如果 Trax 当前时间指示器在第 40 帧，那么在粘贴片段时，它将显示在第 40 帧。

如果片段已占据当前时间指示器指定的时间，就会创建新轨迹并为其插入已复制片段。

###### 时间轴开始(Timeline Start)

如果启用，复制的片段将被粘贴到当前场景的“播放开始时间”(Playback Start Time)。例如，如果当前场景的“播放开始时间”(Playback Start Time)是第 10 帧，复制的片段将被粘贴到第 10 帧。

###### 剪贴板开始(Clipboard Start)

如果启用，复制的片段将被粘贴到其源片段开始帧的新轨迹中。例如，如果复制一个开始帧为第 15 帧的片段，就会创建一个新的轨迹，同时将复制片段插入第 15 帧的轨迹。

#### 分割(Split)

将选定的动画或几何缓存片段分割为两个单独片段。请参见[分割片段](../操纵片段/分割片段.md)。

默认情况下，生成的第一个新片段被命名为 Start，第二个新片段被命名为 End。此外，如果分割动画片段，两个新源片段将被命名为 clipnStartSource 和 clipnEndSource。

单击“拆分”(Split) > ![图：单击“拆分”(Split) 以打开“分割片段选项”(Split Clip Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4894 字 ≥300，非承重" -->以打开“分割片段选项”(Split Clip Options)。

##### 分割片段选项(Split Clip Options)

###### 源片段(Source Clip)

*仅用于动画片段。*

指定选定片段的源片段在分割后的状态。

###### 删除原始源(Delete Original Source)

如果启用，将从“Visor”中删除选定片段的源片段。如果今后不再使用该源片段，请使用该选项。

###### 保持原始源(Keep Original Source)

如果启用，选定片段的源片段将被保留在 Visor 中。如果今后要使用该源片段，请使用该选项。

###### 分割时间(Split Time)

设定片段的分割位置。

###### 当前时间(Current Time)

如果启用，将在“Trax”“当前时间”(current time)指示器的位置分割选定片段。

**注**

无法分割循环片段。在分割片段前，首先要合并片段（没有其他片段）。请参见

合并片段

。

###### 指定时间(Specify Time)

如果启用，将在“分割时间”(Split Time)字段指定的时间分割选定片段。

###### 时间值(Time Value)

用于指定分割片段的自定义时间。该字段仅在“指定时间”(Specify Time)处于活动状态时可用。

#### 合并(Merge)

*仅用于动画片段。*

合并选定的动画缓存片段。请参见[合并片段](../操纵片段/合并片段.md)。

可以合并一个轨迹内的片段，或合并来自单独轨迹的片段。第一个开始的片段将成为合并片段的第一部分。当合并时间方向上存在重叠的片段时，将自动融合这些片段的动画。

若要合并几何缓存片段，请参见[合并几何缓存片段](../../../../几何缓存/几何缓存/创建和编辑几何缓存/使用几何缓存片段/合并几何缓存片段.md)。

单击“合并”(Merge) > ![图：单击“合并”(Merge) 以打开“合并片段选项”(Merge Clip Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4894 字 ≥300，非承重" -->以打开“合并片段选项”(Merge Clip Options)。

##### 合并片段选项(Merge Clip Options)

###### 名称(Name)

用于输入合并动画片段的名称。

###### 合并的片段(Merged Clip)

设定下列选项之一：

###### 添加到 Trax(Add to Trax)

合并轨迹视图区域中选定的动画片段。可以只合并来自同一角色的片段。

###### 只添加到 Visor (在 Trax 中保持原始) (Add to Visor Only(Keep Originals in Trax))

合并轨迹视图区域中选定的动画片段，在“Visor”中存储该合并片段，并在 Trax 中保留选定片段。

##### 合并缓存片段(Merge Cache Clips)

仅用于“几何体”(geometry)或“nCloth 缓存”(nCloth cache)片段。

单击“合并”(Merge) > ![图：单击“合并”(Merge) 以打开“合并片段选项”(Merge Clip Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4894 字 ≥300，非承重" -->以打开“合并片段选项”(Merge Clip Options)。

###### 合并缓存片段选项(Merge Cache Clip Options)

###### 缓存目录(Cache Directory)

指定希望创建的合并后“几何体”(geometry)或“nCloth 缓存”(nCloth cache)在服务器或本地磁盘中的保存位置。单击文件夹图标 (![图：指定希望创建的合并后“几何体”(geometry)或“nCloth 缓存”(nCloth cache)在服务器或本地磁盘…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-A66E3A22-1319-4CC8-B9C8-76E8CD6EE002.png) <!-- baize:img-hook downloaded=false reason="正文 4894 字 ≥300，非承重" -->) 以浏览到其他目录。

###### 名称(Name)

指定要创建的合并后“几何体”(geometry)或“nCloth 缓存”(nCloth cache)片段的基础名称。默认的基础名称是 mergedClip。

###### 文件分布(File Distribution)

设定下列选项之一：

###### 每帧一个文件(One File Per Frame)

为指定的“缓存时间范围”(Cache Time Range)指定创建每帧合并后几何体或 nCloth 缓存文件。

###### 一个文件(One File)

为指定的“缓存时间范围”(Cache Time Range)指定创建一个合并后几何体或 nCloth 缓存文件。

###### “帧求值频率”(Evaluate every frame(s))和“求值保存频率”(Save every evaluation(s))

默认情况下，在创建几何体或 nCloth 缓存时，将在每帧对对象变形进行一次采样，并保存在缓存中。

“帧求值频率”(Evaluate every frame(s))指定几何体或 nCloth 缓存创建期间的采样频度。例如，当值为 2 时，将在“缓存时间范围”(Cache Time Range)内每隔一帧缓存当前对象的变形或模拟。

“求值保存频率”(Save every evaluation(s))指定创建几何体或 nCloth 缓存期间要保存的采样。例如，当值为 2 时，即指定仅按“帧求值频率”(Evaluate every frame(s))选项的要求，以每隔一个采样的频率，将采样保存到“几何体”(geometry)或“nCloth 缓存”。

有关详细信息，请参见[创建几何缓存](../../../../几何缓存/几何缓存/创建几何缓存.md)。

###### 文件清理: 合并后删除缓存文件(File Clean Up: Delete cache files after merge)

指定在创建完合并缓存片段后删除所有启用的几何体或 nCloth 缓存节点。但是，磁盘上的几何体或 nCloth 缓存将被保留。

##### 剪去前方(Trim Before)

移除在 Trax 当前时间指示器位置前的选定动画或几何缓存片段的分段。

##### 剪去后方(Trim After)

移除在 Trax 当前时间指示器位置后的选定动画或几何缓存片段的分段。

##### 复制(Duplicate)

*仅用于动画片段。*

在复制动画片段时，将生成新轨迹，并将片段副本添加到该轨迹中。

单击“复制”(Duplicate) > ![图：单击“复制”(Duplicate) 以打开“复制片段选项”(Duplicate Clip Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4894 字 ≥300，非承重" -->以打开“复制片段选项”(Duplicate Clip Options)。

###### 复制片段选项(Duplicate Clip Options)

###### 复制输入连接(Duplicate Input Connections)

启用后，将创建选定动画片段的副本，该片段的复制动画独立于原始片段的源动画。这样就可以在新片段上编辑动画，同时不会影响原始片段上的动画（仅会影响副本）。

*禁用*后，将创建选定动画片段的副本，该片段的复制动画依存于原始片段的源动画。在这种情况下，对原始片段动画所作的任何修改将被传播到复制片段中。

默认情况下，“复制输入连接”(Duplicate Input Connections)处于禁用状态。

###### 复制(Copy)

设定下列选项之一：

###### 仅将副本置于 Visor 中(Put Copy in Visor Only)

仅将复制片段置于“Visor”中。

“仅将副本置于 Visor 中”(Put Copy in Visor Only)只在“复制输入连接”(Duplicate Input Connections)启用时才可用。

**注**

将片段放置在

“Visor”

中时，可以从

“大纲视图”(Outliner)

查看并访问它们。有关在

“大纲视图”(Outliner)

中查看片段的信息，请参见

将大纲视图与 Trax 结合使用(Use the Outliner with Trax)

。

###### 将副本置于 Trax 编辑器和 Visor 中(Put Copy in Trax Editor and Visor)

将复制动画片段放在“Trax 编辑器”(Trax Editor)和“Visor”中。

将副本置于 Trax 编辑器和 Visor 中仅在“复制输入连接”(Duplicate Input Connections)启用时才可用。

###### 时间扭曲(Time Warp)

设定下列选项之一：

###### 复制时间扭曲曲线(Duplicate Time Warp Curve)

如果启用，将为复制片段创建选定动画片段的时间扭曲曲线的独立副本。该选项非常有用，例如，需要一组角色具有相同的跑步循环动画，但希望每个角色以不同速度跑步。

###### 实例时间扭曲曲线(Instance Time Warp Curve)

如果启用，将为复制片段创建选定动画片段的时间扭曲曲线的依存副本。对原始片段的时间扭曲曲线所作的任何修改将被传播到复制时间扭曲曲线。

默认情况下，“实例时间扭曲曲线”(Instance Time Warp Curve)处于启用状态。

###### 无时间扭曲曲线(No Time Warp Curve)

如果启用，选定片段的时间扭曲曲线将不会复制到重复片段。

#### 复制通道偏移(Copy Channel Offsets)

用于将当前通道偏移设置从一个动画片段应用到其他片段。当希望多个片段具有相同的偏移设置时，该选项将非常有用。

**注**

- 源和目标片段必须属于同一角色。

- 源和目标片段必须具有公用通道。

- 不能将片段通道偏移设置从一个源片段复制到多个目标片段。

#### 快速选择集(Quick Select Sets)

用于选择“快速选择集”(Quick Select Set)。在 Trax 中选择“快速选择集”(Quick Select Set)后，将快速加载作为选择集一部分的动画或几何缓存片段，并显示在轨迹视图区域中。

有关创建片段的“快速选择集”(Quick Select Set)的信息，请参见[快速选择集](Trax%20编辑器%28Trax%20Editor%29%20创建%28Create%29菜单.md#GUID-C9A3BC4F-42C2-49A7-8265-8C31A58080A8__GUID-AC488ABC-A30A-45E5-BBD3-11A35BD45D0E)。

#### 成组(Group)

*仅用于动画片段。*

在当前角色下创建一个组，并在该组下的轨迹中放置选定动画片段。

#### 解组(Ungroup)

*仅用于动画片段。*

从角色中移除选定组，并直接将该组的轨迹放置到其角色或父对象组下。

#### 设置片段重影根(Set Clip Ghost Root)

可以指定要将哪个对象作为场景中的片段重影进行查看。片段重影以 3D 线框显示片段中的第一个姿势和最后一个姿势，并以一条线表示动画的轨迹。另请参见[显示和编辑片段重影](../操纵片段/显示和编辑片段重影.md)。

例如，选择角色骨架的根对象作为片段重影可查看片段开头和结尾处角色姿势的轮廓。

**注**

在 Maya 2014 中，角色集将自动确定角色的偏移对象（或根）。如果偏移对象超出 DAG 层次结构，但已连接到该结构，则 Maya 不会将其标识为您的角色的根。
