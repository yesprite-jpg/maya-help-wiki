# “时间滑块”(Time Slider)首选项

可以在[“首选项(Preferences)”窗口](../“首选项”%28Preferences%29窗口.md)的“时间滑块”(Time Slider)类别中设置以下首选项。

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

**注**

若要在

“时间滑块”(Time Slider)

类别处于选定状态时打开“首选项”(Preferences)窗口，请单击 Maya 窗口右下角中的“动画首选项”(Animation Preferences)图标

。

## 时间滑块(Time Slider)

#### 帧速率(Framerate)

设置当前场景的帧速率。

帧选择包括：2 fps、3 fps、4 fps、5 fps、6 fps、8 fps、10 fps、12 fps、15 fps、16 fps、20 fps、23.976 fps、24 fps (电影)、25 fps (PAL)、29.97 fps、29.97 df (丢帧)、30 fps、40 fps、47.952 fps、48 fps (演示)、50 fps (PAL 场)、59.94 fps、60 fps (NTSC 场)、75 fps、80 fps、100 fps、120 fps、125 fps、150 fps、200 fps、240 fps、250 fps、300 fps、375 fps、400 fps、500 fps、600 fps、750 fps、1200 fps、1500 fps、2000 fps、3000 fps、6000 fps、44 100 fps 和 48 000 fps。

#### 将关键帧保持在当前帧(Keep keys at current frames)

默认情况下，在更改当前时间单位时会修改任何现有关键帧的时间，以便保留播放计时。例如，在当前时间单位更改为 NTSC 后，在帧 12 胶片处设置的关键帧会更改为帧 15ntsc，这是因为它们都表示 0.5 秒处的关键帧。该选项处于启用状态后，最初在 12 胶片处的关键帧会处于 12ntsc 处。此选项的默认设置为禁用。当前“时间”(Time)单位更改后（如上所示），将启用该选项。

#### 将时间范围舍入到整数值(Round time ranges to whole values)

激活此设置可在帧速率更改时保留整帧值。有时，在 Maya 中更改帧速率会将当前帧、帧范围和动画范围编号转化为十进制编号。

默认情况下，此选项处于活动状态。如果希望在更改帧速率后使帧编号保持精确（例如 24.80），请禁用此选项。

#### 播放开始/结束(Playback start/end)

指定播放范围开始和结束时间。播放开始和结束时间指定“时间滑块”(Time Slider)播放范围。播放范围始终在动画范围内。也可以指定时间单位。请参见[编辑动画首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D1E323B7-C582-4E32-99A3-F081422469D2)。

#### 动画开始/结束(Animation start/end)

指定动画范围开始和结束时间。动画开始和结束时间指定“范围滑块”范围。播放范围始终在动画范围内，因此更改动画开始和结束时间也会更改播放开始和结束时间。默认动画开始时间为 1.00。默认动画结束时间为 48.00。也可以指定时间单位。请参见[编辑动画首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D1E323B7-C582-4E32-99A3-F081422469D2)。

#### 油性铅笔帧(Grease Pencil Frames)

可以设置“时间滑块”(Time Slider)中[油性铅笔](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-632E78DF-97C7-406D-8510-8FE508D29FA6)帧的显示方式。默认值为“活动”(Active)，即仅显示当前摄影机的油性铅笔帧。

如果不希望在“时间滑块”(Time Slider)中显示油性铅笔帧，请设置为“无”(None)；如果希望查看所有油性铅笔帧而不管活动摄影机如何，请设置为“全部”(All)。请参见[控制“时间滑块”中油性铅笔帧的显示方式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1D82E001-DCAA-4308-A608-4AA5EB631036)。

#### 关键帧标记(Key ticks)

指定指示关键帧的线标记如何显示在“时间滑块”(Time Slider)上。单击“无”(None)、“活动”(Active)或“通道盒”(Channel Box)。默认值为“活动”(Active)。

- 无(None)：指定不显示关键帧标记。如果有大量关键帧，同时希望改善工作区选择性能，选择**“无”(None)**非常有用。

- 活动(Active)：指定将显示关键帧标记，其关联关键帧可用于选择和编辑。

- 通道盒(Channel Box)：指定仅为“通道盒”(Channel Box)中的当前选定通道显示关键帧标记。如果正使用“时间滑块”(Time Slider)来编辑已设置动画对象的特定通道上的关键帧，这将非常有用。

- 智能(Smart)：可用于在显示所有关键帧标记和与特定通道关联的关键帧标记之间切换。

#### 关键帧标记大小(Key tick size)

更改代表 Maya“时间滑块”(Time Slider)中的关键帧的标记的厚度。关键帧厚度以像素为单位进行测量。单击 **1x**（默认宽度）、**2x**（两倍宽度）或 **3x**（三倍宽度）。

#### 时间显示(Time Display)

选择时间信息以何种格式显示在时间标记上：

![图：选择时间信息以何种格式显示在时间标记上： 帧(Frames)：在所有时间标尺、当前时间标记以及显示或接受时间的输入字段上…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-1E535A29-7545-4E62-928A-7E72B91CB3FF.png) <!-- baize:img-hook downloaded=false reason="正文 5269 字 ≥300，非承重" -->

- 帧(Frames)：在所有时间标尺、当前时间标记以及显示或接受时间的输入字段上显示帧。

- 时间码(Timecode)：在所有时间标尺、当前时间标记以及显示或接受时间的输入字段上显示视频标准时间码。

- 时间标记上的时间码和帧(Timecode and frames on Time Marker)：在时间标记上显示视频标准时间码，而在时间标尺上显示帧。这是在[“时间滑块”(Time Slider)首选项](“时间滑块”%28Time%20Slider%29首选项.md)的“时间滑块”(Time Slider)选项中设置“时间码”(Timecode)时的传统显示方式。

**注**

在时间滑块中，已舍入到小数点后第二位的任何数字旁边会显示一个星号“

*

”，指示该值是近似值。如果在“时间码”(Time Code)与“帧”(Frames)之间切换，或者如果在

“时间滑块”(Time Slider)首选项

中禁用

“捕捉到整个帧”(Snap to Whole Frames)

选项，有时会出现这种情况。

![图：选择时间信息以何种格式显示在时间标记上： 帧(Frames)：在所有时间标尺、当前时间标记以及显示或接受时间的输入字段上…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-D541BB3B-1D4A-437C-A953-FF8F993A7A13.png) <!-- baize:img-hook downloaded=false reason="正文 5269 字 ≥300，非承重" -->

#### 通道盒同步(Channel Box Sync)

##### 同步时间轴显示(Sync Timeline Display)

启用时，会将“通道盒”(Channel Box)中的选择同步到“时间滑块”(Time Slider)，以便“时间滑块”(Time Slider)只显示这些选定通道的关键帧。设置关键帧（按 S 键或选择“关键帧 > 设置关键帧”(Key > Set Key)）时，将只对通道盒中选择的通道设置关键帧。如果未在“通道盒”(Channel Box)中选择任何对象，则“时间滑块”(Time Slider)会照常显示选定对象的关键帧。

##### 在曲线图编辑器中同步选择(Sync Selection in Graph Editor)

![图：注： 在先前版本的 Maya 中，此选项名为“同步曲线图编辑器显示”(Sync graph editor display…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 5269 字 ≥300，非承重" -->

**注**

在先前版本的

Maya

中，此选项名为

“同步曲线图编辑器显示”(Sync graph editor display)

。

启用时，会在“通道盒”(Channel Box)中同步您的选择，使其同时显示在“曲线图编辑器”(Graph Editor)中。如果未在“通道盒”(Channel Box)中选择通道，则“曲线图编辑器”(Graph Editor)会照常显示选定对象的曲线。

#### 当前时间指示器

捕捉到整个帧(Snap to whole frames)：启用后，Maya 会按整数值逐步通过动画时间，捕捉到最近的整数。默认设置为启用。如果处理声音或很小的时间范围，可以关闭“捕捉到整个帧”(Snap to whole frames)以获得更加平滑的拖动。

#### 自动捕捉关键帧(Auto snap keys)

启用时，关键帧在移动或缩放时会捕捉到最近的整帧。缩放时，如果两个关键帧捕捉到同一帧，它们会合并到一个关键帧中。默认情况下，此首选项处于禁用状态。也可以在“时间滑块”(Time Slider)上单击鼠标右键，然后选择“自动捕捉关键帧”(Auto snap keys)。

**注**

必须启用

“当前时间指示器 > 捕捉到整个帧”

(Current time indicator > Snap to whole frames)

设置。如果

“捕捉到整个帧”(Snap to whole frames)

处于禁用状态，则“时间滑块”(Time Slider)不会捕捉到任何对象。移动、缩放或拖动都是如此。

#### Tick 跨度(Tick Span)

指定在“时间滑块”(Time Slider)中放大或缩小时关键帧 Tick 的显示方式。“Tick 跨度”(Tick span)是以 24 的倍数测量的，因此可以显示每 6、12、24 或 48 帧的 Tick。此首选项的默认值为 0。

## 播放(Playback)

#### 播放速度(Playback speed)

指定播放场景的速度。选择“播放每一帧”(Play Every Frame)、24fps x 1、24fps x 0.5、24fps x 2或“其他”(Other)，这将激活您可以在其中输入自定义播放速度的字段。“播放速度”(Playback speed)使用在[设置首选项](“设置”%28Settings%29首选项.md)的“工作单位”(Working Units)部分中设置的帧速率。默认值为“播放每一帧”(Play Every Frame)。

也可以指定播放时间单位。请参见[编辑动画首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D1E323B7-C582-4E32-99A3-F081422469D2)。

##### 播放每一帧(Play every frame)

选定后，将播放您场景中的所有帧，在显示下一个之前更新每个。速度取决于您的工作站计算和绘制每帧所花费的时间。可以在“播放每 n 帧”字段指定播放帧增量。例如，如果播放值为 2.0，则每隔一个帧播放一次。

##### 24fps x 1

选定后，场景将按您在[设置首选项](“设置”%28Settings%29首选项.md)的“工作单位”(Working Units)部分中设置的帧速率播放。（在 Maya 中，默认 fps 为每秒 24 帧。）Maya 可能不显示所有帧，这取决于您工作站的功能、场景的复杂性和显示模式（例如，线框或平滑着色处理）。

##### 24fps x 0.5

选定后，场景将按您在[设置首选项](“设置”%28Settings%29首选项.md)的“工作单位”(Working Units)部分中设置的速度的一半播放。

##### 24fps x 2

选定后，场景将按您在[设置首选项](“设置”%28Settings%29首选项.md)的“工作单位”(Working Units)部分中设置的速度的两倍播放。

##### 其他(Other)

选定后，将以“其他速度”(Other Speed)设置中指定的自定义播放速度播放场景。

##### 其他速率(Other Speed)

仅当“播放速度”(Playback Speed)设置为“其他”(Other)时可用。

用于设置场景的自定义播放速度（每秒帧数）。例如，如果指定“其他速度”(Other Speed)值为 72，则将以 72 fps 的速度播放动画。

#### 播放每 n 帧(Playback by)

如果将“播放速度”(Playback speed)设置为“播放每一帧”(Play Every Frame)，指定播放增量。例如，如果输入 4，Maya 将只以每四帧（或时间）的速度播放。默认值为 1.000。也可以指定播放时间单位。

#### 最大播放速率(Max Playback Speed)

让您可以通过指定速度限值来钳制动画播放速度。当处理具有较大 CPU 活动波动水平的场景（如具有复杂粒子效果的场景）时，这将非常有用。

#### 自由(Free)

指定无“最大播放速率”(Max Playback Speed)。

#### 实时(24 fps) (Real-time (24 fps))

指定场景动画的总体播放速度为尽可能快，但不会超过 24 fps。

#### 一半(12 fps) (Half (12 fps))

指定场景动画的总体播放速度为尽可能快，但不会超过 12 fps。

#### 两倍(48 fps) (Twice (48 fps))

指定场景动画的总体播放速度为尽可能快，但不会超过 48 fps。

#### 更新视图(Update view)

如果工作区布局包含几个视图（例如，从“面板 > 布局”(Panels > Layouts)），可以只在当前活动视图播放场景以提高性能。单击“活动”(Active)或“全部”(All)。默认值为“活动”(Active)。

##### 活动(Active)

仅在当前活动视图播放场景。

##### 全部(All)

在所有工作区视图播放场景。

#### 循环(Looping)

指定向前播放场景时要进行的操作，然后到达播放结束时间（或者在向后播放时的播放开始时间）。单击“一次”(Once)、“往返”(Oscillate)或“连续”(Continuous)。默认为“连续”(Continuous)。

**注**

您可以使用

播放选项(Playback Options)

中的

“循环”(Loop)

图标

（位于范围滑块旁边）快速设置循环选项。

##### 一次(Once)

指定只播放一次场景，然后停止。

![图：指定只播放一次场景，然后停止。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-74544456-D510-4CD4-8D3F-D4BE724731AF.gif) <!-- baize:img-hook downloaded=false reason="正文 5269 字 ≥300，非承重" -->

##### 往返(Oscillate)

指定向前（或向后）播放场景，然后向后播放（或向前）播放，直到停止播放。

![图：指定向前（或向后）播放场景，然后向后播放（或向前）播放，直到停止播放。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-CF66915E-6A1A-4F42-9A90-F26BAB9C3A46.gif) <!-- baize:img-hook downloaded=false reason="正文 5269 字 ≥300，非承重" -->

##### 连续(Continuous)

指定向前（或向后）播放场景，然后向后播放（或向前）播放，直到停止播放。

![图：指定向前（或向后）播放场景，然后向后播放（或向前）播放，直到停止播放。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-7ADCF893-619E-4606-951D-11D7626F5FAF.gif) <!-- baize:img-hook downloaded=false reason="正文 5269 字 ≥300，非承重" -->

#### 设置帧和关键帧步长时循环播放范围(Loop play range when stepping frames and keys)

切换循环播放范围，而不是继续播放整个动画。禁用此选项后，动画将播放到结尾后再循环播放。

有关播放范围的信息，请参见[范围滑块(Range Slider)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E9E054A1-A5D0-412C-976A-F57C0F6960B1)。

- 前进一帧，动画将循环到播放范围中的第一帧。对于后退一帧，动画将往回循环到播放范围中的最后一帧。

- 前进到下一关键帧，动画将向前循环到播放范围中的第一个关键帧。对于后退到下一关键帧，动画将向后循环到播放范围中的最后一个关键帧。

默认情况下，此选项处于启用状态。
