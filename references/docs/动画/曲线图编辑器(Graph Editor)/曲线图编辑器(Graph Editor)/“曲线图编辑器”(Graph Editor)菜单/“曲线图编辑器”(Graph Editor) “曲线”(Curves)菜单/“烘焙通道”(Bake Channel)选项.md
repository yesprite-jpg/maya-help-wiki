# “烘焙通道”(Bake Channel)选项

- 在[“曲线图编辑器曲线”(Graph Editor Curves)菜单](../“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)中，选择“烘焙通道”(Bake Channel) > ![图：在“曲线图编辑器曲线”(Graph Editor Curves)菜单中，选择“烘焙通道”(Bake Channel)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 800 字 ≥300，非承重" -->

**注**

若要还原过滤器默认设置，请单击“过滤器”(Filter)窗口中的“编辑 > 重置设置”(Edit > Reset Settings)。

### 时间范围(Time Range)

指定烘焙的关键帧。

#### 时间滑块(Time Slider)

在“时间滑块”(Time Slider)中，位于“播放开始”(Playback Start)和“播放结束”(End)时间之间的区域中的所有关键帧均会烘焙到新通道。

![图：在“时间滑块”(Time Slider)中，位于“播放开始”(Playback Start)和“播放结束”(End)时间…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-7A42DEB4-22E2-43CA-9211-C6AF1AAE2433.gif) <!-- baize:img-hook downloaded=false reason="正文 800 字 ≥300，非承重" -->

#### 开始/结束(Start/End)

指定的时间范围（开始时间/结束时间）内的所有关键帧均会烘焙到新通道。

![图：指定的时间范围（开始时间/结束时间）内的所有关键帧均会烘焙到新通道。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-15C2134E-FB63-4142-83F2-B1047B7D24FA.gif) <!-- baize:img-hook downloaded=false reason="正文 800 字 ≥300，非承重" -->

#### 开始时间(Start Time)

指定时间范围的开始。仅当“开始/结束”(Start/End)启用时才可用。

#### 结束时间(End Time)

指定时间范围的结束。仅当“开始/结束”(Start/End)启用时才可用。

#### 采样频率(Sample By)

指定 Maya 对动画求值并生成关键帧时使用的频率。增加该值时，Maya 为动画设置关键帧的频率将会减少。减少该值时，效果相反。

“采样频率”(Sample By)值以“时间单位”(Time Unit)设置为基础。它表示 Maya 分析对象动画并生成关键帧时使用的频率。如果值为 1，则在每个时间单位处创建一个关键帧。增大该值将会减小生成关键帧的频率；减小该值将会增大频率。

#### 保持未烘焙关键帧(Keep Unbaked Keys)

默认情况下，该选项已启用。该选项将保留位于烘焙时间范围之外的关键帧，并且仅应用于直接连接的动画曲线。

启用时，烘焙模拟不会移除位于烘焙范围之外的关键帧。

禁用时，只有在烘焙期间在指定时间范围内创建的关键帧才会在操作之后出现在动画曲线上。

#### 稀疏曲线烘焙(Sparse Curve Bake)

该选项仅对直接连接的动画曲线起作用。该选项会生成烘焙结果，该烘焙结果仅创建足以表示动画曲线的形状的关键帧。
