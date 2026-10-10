# “创建片段”(Create Clip)选项

使用这些选项可设置在“Trax 编辑器”(Trax Editor)中选择“创建 > 动画片段”(Create > Animation Clip) > ![图：使用这些选项可设置在“Trax 编辑器”(Trax Editor)中选择“创建 动画片段”(Create Animati…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2013 字 ≥300，非承重" -->时发生的情况。

#### 名称(Name)

指定片段的名称。默认名称为 clip*n*。如果重命名某个片段，关联的源片段将自动重命名，以便与新的片段名称相匹配。

#### 时间范围(Time Range)

在“Trax 编辑器”(Trax Editor)中指定片段的时间范围：

#### 选定(Selected)

将在时间滑块中已选定的时间范围用于片段。若要选择时间范围，请按住 Shift 键并在“时间滑块”(Time Slider)中拖过所需的时间。

#### 时间滑块(Time Slider)

使用“时间滑块”(Time Slider)的“播放开始”(Playback Start)和“播放结束”(Playback End)时间规定的时间范围。

#### 动画曲线(Animation Curve)

使用跨越角色集动画曲线范围的时间范围。即开始时间为角色集上第一个关键帧的时间，且结束时间为最后一个关键帧的时间。

#### 开始/结束(Start/End)

指定从“开始时间”(Start Time)到“结束时间”(End Time)的时间范围。

#### 开始时间(Start Time)

可用于指定时间范围的开始（“开始/结束”(Start/End)处于启用状态的情况下可用）。

#### 结束时间(End Time)

可用于指定时间范围的结束（“开始/结束”(Start/End)处于启用状态的情况下可用）。

#### 偏移(Offset)

可以为动画通道指定从一个片段到下一个片段的偏移行为。（另请参见[绝对和相对通道偏移](../../Trax%20中的非线性动画组件/Trax%20中的片段/片段状态.md#GUID-968254A9-1044-4887-8197-63A41D0DE05A__GUID-F4A1A941-729A-4C5B-BB85-94A2854CD4BD)和[偏移片段通道](../../操纵片段/偏移片段通道.md)。）

#### 绝对(Absolute)

将片段内的通道设定为绝对偏移，这意味着通道不会从之前的通道累积运动，播放方式与在动画曲线中完全相同。如果要创建一系列循环动画，请使用此设置。

**注**

“绝对”(Absolute)

是新片段和导入片段的默认

“偏移”(Offset)

设置。

#### 相对(Relative)

将片段内的通道设定为相对偏移，这意味着通道将累积运动。将之前片段中等效通道的运动添加到片段自身的动画中。

#### 仅相对根(Relative Root(s) Only)

将设定混合偏移，其中部分通道设定为绝对偏移，部分设定为相对偏移，具体取决于它们是否为角色层次的根。如果要从先前版本的 Maya 中复制先前的默认行为，请使用此选项。

#### 子角色(Subcharacters)

设定下列选项：

#### 在片段中包括子角色(Include Subcharacters in Clip)

启用时，系统将创建单个源片段，并在其中包括角色集及其所有子角色集的所有动画曲线。

#### 包括层次(Include Hierarchy)

启用后（默认设置），选定对象之下的层次将包括在片段中。禁用后，只有选定对象本身包括在片段中。只有已设置动画的属性包括在片段中；未设置动画的对象将被忽略。

#### 关键帧(Keys)

进行下列设定：

#### 将关键帧保留在时间轴上(Leave Keys in Timeline)

启用时，当您在为当前角色创建片段时，当前角色集的关键帧不会从“时间滑块”(Time Slider)中移除。如果不希望立即使用该片段，但要存储以供将来使用，这点会有用。通过将关键帧保持在“时间滑块”(Time Slider)中，可以创建带关键帧的其他片段。

若启用“将关键帧保留在时间轴上”(Leave Keys in Timeline)，“将片段放在 Trax 编辑器和 Visor 中”(Put Clip in Trax Editor and Visor)选项太暗，无法防止“时间滑块”(Time Slider)中的关键帧向“Trax 编辑器”(Trax Editor)中的片段动画添加。此操作在动画方面具有双倍效果。如果先创建角色集的片段，然后创建角色集的关键帧，接着动画关键帧将被添加至片段动画。请参见[在片段顶部设定关键帧](../../操纵片段/在片段顶部设定关键帧.md)。

禁用时，当为当前角色的动画曲线创建片段时，当前角色集的关键帧从“时间滑块”(Time Slider)中移除。

若要为不同时间范围的角色集动画创建几个片段，请禁用 “将关键帧保留在时间轴上”(Leave Keys in Timeline)，并启用 “将片段放在 Trax 编辑器和 Visor 中”(Put Clip in Trax Editor and Visor)。创建具有全部需要的关键帧的片段，然后将片段分隔成需要的动画分段。请参见[分隔片段](../../操纵片段/分割片段.md#WS1A9193826455F5FF-6D855556117E9F816D22A25)。

### 片段(Clip)

指定正在创建的片段的放置地点：

#### 仅将片段放在 Visor 中(Put Clip in Visor Only)

如果当前不使用该片段，但要将其存储以供将来使用，此设置会有用。

#### 将片段放在 Trax 编辑器和 Visor 中(Put Clip in Trax Editor and Visor)

现在，可以在“Trax 编辑器”(Trax Editor)中的片段上进行操作。这是默认设置。

### 时间扭曲(Timewarp)

设定下列选项：

#### 创建时间扭曲曲线(Create Timewarp Curve)

为选定的片段创建时间扭曲曲线。请参见[为片段创建时间扭曲](../../操纵片段/使用%20Trax%20创建和编辑时间扭曲.md#WS1A9193826455F5FF-6D855556117E9F816D22AD7)。
