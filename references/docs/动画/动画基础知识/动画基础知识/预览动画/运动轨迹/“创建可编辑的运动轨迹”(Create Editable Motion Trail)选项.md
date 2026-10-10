# “创建可编辑的运动轨迹”(Create Editable Motion Trail)选项

- 在“动画”(Animation)菜单集中：“可视化 > 创建可编辑的运动轨迹”(Visualize > Create Editable Motion Trail) > ![图：在“动画”(Animation)菜单集中：“可视化 创建可编辑的运动轨迹”(Visualize Create Edita…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1104 字 ≥300，非承重" -->

运动轨迹显示已设置动画的对象已经或正在经过的位置。请参见[创建可编辑的运动轨迹](创建可编辑的运动轨迹.md)。

**注**

如果要改为沿路径设置对象的动画，请参见

路径动画

。

#### 时间范围(Time Range)

选择下列选项之一：

#### 开始/结束(Start/End)

为“开始时间”(Start Time)和“结束时间”(End Time)指定的帧创建运动拖尾。

#### 时间滑块(Time Slider)

为时间滑块中的所有帧创建运动拖尾。

#### 开始时间(Start Time)

运动拖尾开始的时间。仅当在“时间范围”(Time Range)下选中了“开始/结束”(Start/End)时才可用。

#### 结束时间(End Time)

运动拖尾结束的时间。仅当在“时间范围”(Time Range)下选中了“开始/结束”(Start/End)时才可用。

#### 增量(Increment)

设定对运动拖尾线进行采样和绘制的频率，本质上是指定运动拖尾线的分辨率。默认值为 1，因此在每一帧对运动拖尾进行采样。例如，如果将“增量”设定为 5，则每 5 帧对一个运动拖尾点进行采样和绘制。如果运动拖尾关键帧落在采样点上，则在拖尾上绘制。

将“增量”设定为较大的值可以提高性能，因为在运动拖尾上绘制的关键帧较少。在某些情况下，可以偏移拖尾绘制未落在采样点上的运动拖尾关键帧。

#### 渲染前帧(Pre frames)

指定要绘制运动拖尾的当前时间前的帧数。值 0（默认值）从当前帧到开始帧绘制运动拖尾。

#### 渲染后帧(Post frames)

指定要绘制运动拖尾的当前时间后的帧数。值 0（默认值）从当前帧到最后一帧绘制运动拖尾。

#### 固定(Pinning)

允许您设定在场景中绘制运动拖尾的时间。如果要比较身体的不同侧或者要确保运动流在不同的身体部位之间是平滑的，则固定运动拖尾可能非常有用。

从下列选项中进行选择：

#### 始终绘制(Always draw)

运动拖尾在场景中总是可见，甚至未选择关联对象时也是如此。

#### 选择时绘制(Draw when selected)

仅在选择对象时绘制运动拖尾，未选择对象时不显示。

#### 轨迹厚度(Trail thickness)

设定在场景中显示的运动拖尾线的粗细。默认值为 3。

#### 关键帧大小(Key size)

设定在运动拖尾上呈现的关键帧的大小。默认值为 0.15。

#### 显示帧数(Show frame numbers)

显示或隐藏运动拖尾上每个关键帧处的帧数。

![图：显示或隐藏运动拖尾上每个关键帧处的帧数。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-CA500F3C-4252-4A3F-BA1E-12DE74187D57.png) <!-- baize:img-hook downloaded=false reason="正文 1104 字 ≥300，非承重" -->

#### 使用锚点变换(Use Anchor Transform)

隔离变换相对于动画其余部分的运动。可以将此应用于摄影机动画以可视化移动摄影机快照内对象的运动。请参见[在世界空间中分析动画](在世界空间中分析动画.md)。
