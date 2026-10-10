# “动画控件”(Animation controls)菜单

在[时间滑块](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-827ED8CD-C6AA-4495-8B5E-2FC98C8D49EE.htm)中的任意位置单击鼠标右键，将显示一个用于执行动画控件操作的菜单。在当前选定对象的关键帧上可执行这些操作。

#### “剪切”(Cut)、“复制”(Copy)和“删除”(Delete)

“剪切”(Cut)、“复制”(Copy)和“删除”(Delete)会影响在当前时间或处于选定范围内的关键帧。“剪切”(Cut)和“复制”(Copy)会将选定关键帧放置到内部剪贴板上以便粘贴，而“删除”(Delete)会从时间轴移除选定的关键帧。“复制”(Copy)、“剪切”(Cut)和“删除”(Delete)还可对整数时间范围进行操作。例如，如果当前时间是 5，则这些项目作用于 5 到 6 的范围，但不包括处于时间 6 的任何关键帧。

#### 粘贴(Paste)

“粘贴”(Paste)会在当前时间放置从剪贴板复制或剪切的所有关键帧。“粘贴 > 粘贴连接”(Paste > Paste Connect)会粘贴复制的关键帧，就像在启用“连接”(Connect)选项的情况下选择“编辑 > 关键帧 > 粘贴”(Edit > Keys > Paste)。

有两种方法可以将关键帧粘贴到“时间滑块”(Time Slider)中：

- 单击希望粘贴的关键帧开始的时间。超出该时间的现有关键帧将按粘贴的关键帧的时间范围进行偏移。

- 若要使关键帧适配到某个特定的时间范围，请按住 Shift 键并单击“时间滑块”(Time Slider)来选择时间范围。关键帧将进行缩放以适配该范围。会移除选定区域中的现有关键帧。

#### 捕捉(Snap)

使用“捕捉”(Snap)可强制选定关键帧将时间捕捉到最近的整体时间单位。

#### 关键帧(Keys)

- **“转化为关键帧”(Convert to Key)**会将选定受控关键点转化为普通关键帧。

- **“转化为受控关键点”(Convert to Breakdown)**会将普通关键帧转化为受控关键点。

- **“添加中间帧”(Add Inbetween)**将添加单个中间帧。

- **“移除中间帧”(Remove Inbetween)**将移除单个中间帧。

#### 切线(Tangents)

“切线”(Tangents)项目将设置当前时间的关键帧或选定时间范围内的所有关键帧的切线。

- **“样条线”(Spline)**将在选定关键帧之前和之后的关键帧之间创建一条平滑的动画曲线。

- **“线性”(Linear)**会将动画曲线创建为接合两个关键帧的直线。

- **“钳制”(Clamped)**将创建具有线性和样条曲线特征的动画曲线。

- **“阶跃”(Stepped)**将创建其出切线为平坦曲线的动画曲线。

- **“平坦”(Flat)**会将关键帧的入切线和出切线设置为水平（渐变为 0 度）。

- **“高原”(Plateau)**不仅可以使动画曲线缓入和缓出其关键帧（如样条线切线），而且还可以展平出现在等值关键帧（如钳制切线）之间的曲线分段。

- **“自动”(Auto)**会根据相邻关键帧值将帧之间的曲线值钳制为最大点或最小点。

有关其中每一种切线的详细描述，请参见[曲线图编辑器的“切线”(Tangents)菜单](../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md)。

#### 油性铅笔(Grease Pencil)

可以设置“时间滑块”(Time Slider)中[油性铅笔](../../../动画基础知识/动画基础知识/使用油性铅笔在场景视图上绘制/油性铅笔.md)帧的显示方式。默认值为“活动”(Active)，即仅显示当前摄影机的油性铅笔帧。

如果不希望在“时间滑块”(Time Slider)中显示油性铅笔帧，请设置为“无”(None)；如果希望查看所有油性铅笔帧而不管活动摄影机如何，请设置为“全部”(All)。请参见[控制“时间滑块”中油性铅笔帧的显示方式](../../../动画基础知识/动画基础知识/使用油性铅笔在场景视图上绘制/使用油性铅笔帧和图像/控制“时间滑块”%28Time%20Slider%29中油性铅笔帧的显示方式.md)。

有关详细信息，请参见[油性铅笔](../../../动画基础知识/动画基础知识/使用油性铅笔在场景视图上绘制/油性铅笔.md)。

#### 时间滑块书签(Time Slider Bookmarks)

“时间滑块书签”(Time Slider Bookmarks)是沿“时间滑块”(Time Slider)顶部的彩色标记，可标记场景中的事件。书签可让您及时注意特定时刻，当您想要聚焦或亮显场景中的特定区域或时刻时，这非常有用。

通过单击“时间滑块书签 > 创建”(Time Slider Bookmarks > Create)或[范围滑块(Range Slider)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E9E054A1-A5D0-412C-976A-F57C0F6960B1)中的“书签”(Bookmark)图标 ![图：通过单击“时间滑块书签 创建”(Time Slider Bookmarks Create)或范围滑块(Range Sli…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-69C40894-3EC0-46C2-A50C-CC215539EFE2.png) <!-- baize:img-hook downloaded=false reason="正文 5126 字 ≥300，非承重" -->，或者按 **Alt** (**Option**) + **T**，将书签添加到选定帧或时间范围。

  **创建(Create)**

  打开“创建书签”(Create Bookmark)对话框，以便将书签添加到选定帧。如果未选择任何帧，请在“开始帧”(Start frame)和“结束帧”(End frame)字段中输入书签范围。

  **编辑(Edit)**

  针对当前时间的书签，打开“创建书签”(Create Bookmark)对话框。（如果多个书签重叠，将选择顶部（最新创建的）书签。）

  **框显书签(Frame Bookmark)**

  在当前时间的书签上使播放范围居中，以便书签区域占用整个范围。（如果多个书签重叠，将选择顶部（最新创建的）书签。）

  热键：|（竖线）

  **框显上一个书签(Frame Previous Bookmark)**

  在当前时间书签之前的书签上使“范围滑块”(Range Slider)居中。

  热键：:（冒号）

  **框显下一个书签(Frame Next Bookmark)**

  在当前时间书签之后的书签上使“范围滑块”(Range Slider)居中。

  热键：,（逗号）

  **取消框显(Unframe)**

  将“时间滑块”(Time Slider)视图返回到播放范围。

  热键：Alt (Option) + \（反斜线）

  **删除(Delete)**

  删除当前时间最上方的书签。

  **显示书签(Show Bookmarks)**

  切换书签可见性。

  **删除所有书签(Delete All Bookmarks)**

  从场景中删除所有书签。

  **书签管理器(Bookmark Manager)**

  打开“书签管理器”(Bookmark Manager)窗口。

有关详细信息，请参见[创建书签](../../../动画基础知识/动画基础知识/时间滑块书签%28Time%20Slider%20Bookmarks%29/创建时间滑块书签.md)。

#### 缓存播放(Cached Playback)

可用于激活和配置“缓存播放”(Cached Playback)以提高动画播放性能。

##### 缓存播放(Cached Playback)

启用此选项可将动画缓存到内存以提高播放速度。请参见[使用“缓存播放”(Cached Playback)以提高播放速度](../../../缓存播放%28Cached%20Playback%29/缓存播放%28Cached%20Playback%29/使用“缓存播放”%28Cached%20Playback%29以提高播放速度.md)。

##### 缓存模式

从“解算缓存”(Evaluation cache)、“视口软件缓存”(Viewport software cache)或“视口硬件缓存”(Viewport hardware cache)中进行选择，以针对计算机硬件优化“缓存播放”(Cached Playback)。有关这些模式的描述，请参见[选择缓存播放模式](../../../缓存播放%28Cached%20Playback%29/缓存播放%28Cached%20Playback%29/使用“缓存播放”%28Cached%20Playback%29以提高播放速度/选择缓存播放模式.md)。

##### 清除缓存(Flush Cache)

清空播放缓存，并丢弃存储的内容，因此所有内容都必须重建。由于数据会立即被删除，因此它的速度可能比缓存失效慢。如果您想将缓存擦除干净，请使用“清除缓存”(Flush Cache)。请参见[“缓存播放”(Cached Playback)状态行状态](../../../缓存播放%28Cached%20Playback%29/缓存播放%28Cached%20Playback%29/使用“缓存播放”%28Cached%20Playback%29以提高播放速度/“缓存播放”%28Cached%20Playback%29状态行的状态.md)主题中的**失效**部分。（您还可以通过的[播放选项(Playback Options)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-9853B7B5-8AD5-46F6-A921-A3771A505AD1.htm)中的“缓存播放”(Cached Playback)图标 ![图：清空播放缓存，并丢弃存储的内容，因此所有内容都必须重建。由于数据会立即被删除，因此它的速度可能比缓存失效慢。如果您想将缓…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-EDBB8091-6F7E-4772-B1C6-6019FCB26E2F.png) <!-- baize:img-hook downloaded=false reason="正文 5126 字 ≥300，非承重" --> 的快捷菜单清除缓存。）

##### 缓存播放首选项(Cached Playback Preferences)

打开[缓存播放首选项(Cached Playback Preferences)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3CB35662-DB1D-4CF3-9135-E09B973635DE)窗口，以便您可以配置“缓存播放”(Cached Playback)。

##### 颜色首选项

将[颜色设置(Color Settings)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1FC6CC4E-6C21-44FA-A58B-AC31ED57B591)窗口直接打开到“缓存播放”(Cached Playback)颜色设置，您可以在其中更改在[时间滑块(Time Slider)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-827ED8CD-C6AA-4495-8B5E-2FC98C8D49EE.htm)上出现的每个“缓存播放”(Cached Playback)部分的默认颜色。您可以为缓存帧、未缓存帧和无效帧以及子帧拾取颜色。您甚至可以使用不透明度设置来设置“缓存播放”(Cached Playback)状态行的透明度。

#### 播放速度(Playback Speed)

使用该选项可设置当前场景的播放速度和帧速率。

##### **实时(Real-time)**

将当前场景的播放速度设置为每秒 24 帧。

##### **自由播放每一帧(Play Every Frame, Free)**

将当前场景的播放速度设置为播放每一帧，而不会受制于特定的最大帧速率。

##### **以最大实时速度播放每一帧(Play Every Frame, Max Real-time)**

将当前场景的播放速度设置为播放每一帧，但受制于每秒 24 帧的最大帧速率。

#### 显示关键帧 Tick(Display Key Ticks)

用于设置时间滑块上显示的关键帧标记的源。请选择：

- **活动(Active)**：在活动对象上设置的关键帧。这是默认设置。

- **来自通道盒(From Channel Box)**：在“通道盒”(Channel Box)中设置的关键帧。请参见[在通道盒中设置关键帧](../../../关键帧动画/关键帧动画/设定关键帧/在通道盒中设置关键帧.md)。

- **无(None)**：不显示时间滑块上的关键帧标记。

- **显示层权重(Show Layer Weight)**：显示选定层的权重动画。

- **从层编辑器显示选项(From Layer Editor Show Options)**：使用“动画层编辑器”(Animation Layer Editor)菜单栏的“显示”(Show)菜单中处于活动状态的任何设置。

- **全部影响(All Affecting)**：显示所有受影响的动画层的关键帧。（包含场景中所选对象属性的所有层）。

- **活动(Active)**：仅显示活动层中的关键帧。

- **选定(Selected)**：仅显示选定动画层中的关键帧。

- **活动的和选定的(Active and Selected)**：显示活动动画层和所选动画层中的关键帧。

有关详细信息，请参见[查看分层动画](../../../动画层/动画层/视图分层动画.md)。

#### 播放循环(Playback Looping)

若要选择播放循环选项，请在时间滑块上单击鼠标右键，然后选择“播放循环 > 一次”(Playback Looping > Once)、“播放循环 > 往返”(Playback Looping > Oscillate)或“播放循环 > 连续”(Playback Looping > Continuous)（有关此行为的演示，请参见[播放选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-9853B7B5-8AD5-46F6-A921-A3771A505AD1.htm)中的“循环”(Loop)）。这些选项与使用[播放选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-9853B7B5-8AD5-46F6-A921-A3771A505AD1.htm)和“首选项”(Preferences)窗口中的“循环”(Loop)图标 ![图：若要选择播放循环选项，请在时间滑块上单击鼠标右键，然后选择“播放循环 一次”(Playback Looping Once…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-5E88F9FB-731C-4536-8CD1-5E307979F381.png) <!-- baize:img-hook downloaded=false reason="正文 5126 字 ≥300，非承重" --> 相同。

#### 将范围设置为(Set Range To)

- **“开始/结束”(Start/End)**会将播放范围设置为在“播放范围”(Playback Range)数值输入字段中设置的“开始”(Start)和“结束”(End)值。

- **“最小值/最大值”(Min/Max)**会将播放范围设置为场景的第一个和最后一个关键点。

- **“选定”(Selected)**会将播放范围设定为“时间滑块”(Time Slider)上的当前选择所定义的范围。

- **“已启用片段”(Enabled clips)**会将播放范围设置为包含所有已启用片段的范围。

- **“声音长度”(Sound Length)**会将播放范围设定为当前加载到“时间滑块”(Time Slider)中的声音的持续时间。

- **“首选项”(Preferences)**会将播放范围设置为“首选项”(Preferences)窗口中的值。

#### 时间显示(Time Display)

选择时间信息以何种格式显示在时间标记上：

![图：选择时间信息以何种格式显示在时间标记上： 帧(Frames)：在所有时间标尺、当前时间标记以及显示或接受时间的输入字段上…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-1E535A29-7545-4E62-928A-7E72B91CB3FF.png) <!-- baize:img-hook downloaded=false reason="正文 5126 字 ≥300，非承重" -->

- **帧(Frames)**：在所有时间标尺、当前时间标记以及显示或接受时间的输入字段上显示帧。

- **时间码(Timecode)**：在所有时间标尺、当前时间标记以及显示或接受时间的输入字段上显示视频标准时间码。

- **时间标记上的时间码和帧(Timecode and frames on Time Marker)**：在时间标记上显示视频标准时间码，而在时间标尺上显示帧。这是在[“时间滑块”(Time Slider)首选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-51A80586-9EEA-43A4-AA1F-BF1370C24A64.htm)的“时间滑块”(Time Slider)选项中设置“时间码”(Timecode)时的传统显示方式。

#### 启用阶跃预览(Enable Stepped Preview)

您可以将**“阶跃预览”(Stepped Preview)**模式在启用和禁用间进行切换，轻松将曲线从样条线切换到阶跃切线以及从阶跃切线切换到样条线。启用此选项时，关键帧可暂时显示为阶跃切线，因此当对象位置碰撞到各个关键帧时，播放动画能提供快速查看对象位置。禁用此选项时，动画将使用原始切线如常播放。请参见[“阶跃”(Stepped)](../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-59FDEC35-60E1-446E-9CA9-0AA5A1A65744)切线。

#### 自动捕捉关键帧(Auto snap keys)

启用时，关键帧在移动或缩放时会捕捉到最近的整帧。缩放时，如果两个关键帧捕捉到同一帧，它们会合并到一个关键帧中。默认情况下，此首选项处于禁用状态。

**注**

提示：

也可以选择

“窗口 > 设置/首选项 > 首选项 > 时间滑块 > 自动捕捉关键帧”(Windows > Settings/Preferences > Preferences > Time Slider > Auto snap keys)

。

#### 音频(Audio)

该菜单用于选择要在时间滑块上显示的导入的声音。

选择“声音 > <文件名>”(Sound > <文件名>) > ![图：选择“声音 <文件名 ”(Sound <文件名 ) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5126 字 ≥300，非承重" -->。

#### 播放预览(Playblast)

选择该选项会打开“播放预览”(Playblast)窗口。选择该选项框 (![图：选择该选项会打开“播放预览”(Playblast)窗口。选择该选项框 () 会打开 “播放预览选项”(Playblast…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5126 字 ≥300，非承重" -->) 会打开[“播放预览选项”(Playblast Options)](../../../动画基础知识/动画基础知识/预览动画/播放预览动画/播放预览选项%28Playblast%20Options%29.md)窗口。
