# “抖动磁盘缓存”(Jiggle Disk Cache)选项

- 在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 > (创建)抖动 > 抖动磁盘缓存”(Deform > (Create) Jiggle > Jiggle Disk Cache) > ![图：在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 (创建)抖动…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 872 字 ≥300，非承重" -->

#### 缓存时间范围(Cache Time Range)

指定要缓存哪些帧。最容易缓存“时间轴”(Time Line)的整个帧范围。但是，您可以通过仅缓存对象在其中抖动的帧来创建较小的缓存文件，以节约磁盘空间。

#### 时间滑块(Time Slider)

缓存“播放开始/结束”(Playback Start/End)范围内的所有帧。

#### 渲染设置(Render Settings)

缓存在“渲染设置”(Render Settings)窗口的“帧范围”(Frame Range)区域中指定的帧范围。

有关详细信息，请参见[渲染设置窗口](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-59DFB8B7-776B-4243-B404-A3D602FF8CFD)。

#### 开始/结束(Start/End)

缓存在“开始/结束”(Start/End)时间框中指定的帧范围。

#### 开始时间/结束时间(Start Time End Time)

设定已缓存的帧范围。仅当为“缓存帧范围”(Cache Frame Range)选择“自定义”(Custom)时才可用。

#### 采样(Sampling)

过采样和欠采样指定 Maya 计算逐帧抖动的频率。

#### 过(Over)

“速率”(Rate)值大于等于 2 时可能会增大场景中已缓存抖动的精度，在这些场景中，抖动对象快速而反复地与刚体碰撞。

#### 欠(Under)

“速率”(Rate)值大于等于 2 时会降低已缓存抖动的精度，但是会加快缓存操作。例如，“欠采样”(Under Sample)“速率”(Rate) 为 2，表示 Maya 每两个帧计算一次抖动。

如果抖动对象与刚体的碰撞不切实际，请选择“过采样”(Over Sample)，并设置与在“解算器”(Solvers) > “编辑过采样或缓存设置”(Edit Oversampling or Cache Settings)中可用的“过采样”(Over Samples)设置匹配的“速率”(Rate)。

#### 速率(Rate)

为“过采样”(Over Sample)或“欠采样”(Under Sample)设定整数值。
