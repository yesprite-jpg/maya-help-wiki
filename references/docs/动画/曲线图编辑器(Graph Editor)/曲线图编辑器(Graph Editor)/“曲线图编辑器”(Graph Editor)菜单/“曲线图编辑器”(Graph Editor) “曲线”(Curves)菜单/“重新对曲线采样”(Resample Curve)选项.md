# “重新对曲线采样”(Resample Curve)选项

- 在[“曲线图编辑器”(Graph Editor)的“曲线”(Curves)菜单](../“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)中，选择“重新对曲线采样”(Resample Curve) > ![图：在“曲线图编辑器”(Graph Editor)的“曲线”(Curves)菜单中，选择“重新对曲线采样”(Resample…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 840 字 ≥300，非承重" -->

**注**

若要还原过滤器默认设置，请单击“过滤器”(Filter)窗口中的“编辑 > 重置设置”(Edit > Reset Settings)。

#### 时间范围(Time Range)

指定关键帧重采样的时间范围。

![图：指定关键帧重采样的时间范围。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23F238AE-C22B-47CF-9670-5B96BD111B69.gif) <!-- baize:img-hook downloaded=false reason="正文 840 字 ≥300，非承重" -->

#### 全部(All)

对整个时间范围的曲线重采样。

![图：对整个时间范围的曲线重采样。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23F238AE-C22B-47CF-9670-5B96BD111B69.gif) <!-- baize:img-hook downloaded=false reason="正文 840 字 ≥300，非承重" -->

#### 开始/结束(Start/End)

指定的时间范围（开始时间/结束时间）内的所有关键帧均会重采样。

![图：指定的时间范围（开始时间/结束时间）内的所有关键帧均会重采样。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-15C2134E-FB63-4142-83F2-B1047B7D24FA.gif) <!-- baize:img-hook downloaded=false reason="正文 840 字 ≥300，非承重" -->

#### 时间滑块(Time Slider)

对“时间滑块”(Time Slider)的“播放开始”(Playback Start)和“播放结束”(End)时间定义的时间范围内的曲线重采样。

![图：对“时间滑块”(Time Slider)的“播放开始”(Playback Start)和“播放结束”(End)时间定义的…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-7A42DEB4-22E2-43CA-9211-C6AF1AAE2433.gif) <!-- baize:img-hook downloaded=false reason="正文 840 字 ≥300，非承重" -->

#### 开始时间(Start Time)

指定时间范围的开始。仅当“开始/结束”(Start/End)启用时，该选项才可用。

#### 结束时间(End Time)

指定时间范围的结束。仅当“开始/结束”(Start/End)启用时，该选项才可用。

#### 重采样类型(Resample Type)

指定重采样过滤器，它是定义曲线中的关键帧如何重采样的算法。请选择下列选项之一：

#### 最近的采样(Closest Sample)

使用距最近时间步最近的采样值。

#### 线性插值(Linear Interpolation)

使用距最近时间步最近的两个采样之间的线性插值。

#### 长方体过滤器(Box Filter)

使用相等的权重计算过滤区域中所有采样的总和。

![图：使用相等的权重计算过滤区域中所有采样的总和。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F8FA1BE4-2CFF-4F9D-9AF0-76A42B3EBA3D.png) <!-- baize:img-hook downloaded=false reason="正文 840 字 ≥300，非承重" -->

#### 三角形过滤器(Triangle Filter)

使用影响关键帧的线性曲线，以便采样区域的边中发生最少的过滤。

![图：使用影响关键帧的线性曲线，以便采样区域的边中发生最少的过滤。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-717BBA76-1557-4230-BD0E-6A4A02BB4C2D.png) <!-- baize:img-hook downloaded=false reason="正文 840 字 ≥300，非承重" -->

#### Gaussian2

使用在峰值顶部逐渐将采样加权、并朝向采样区域的边的渐变曲线。这是默认设置。

![图：使用在峰值顶部逐渐将采样加权、并朝向采样区域的边的渐变曲线。这是默认设置。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-1F0781D5-642A-4AC5-AC64-DCAFCDF355FD.png) <!-- baize:img-hook downloaded=false reason="正文 840 字 ≥300，非承重" -->

#### Gaussian4

与“Gaussian2” 过滤器十分类似，但其根部更窄。

![图：与“Gaussian2” 过滤器十分类似，但其根部更窄。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-535C85C5-C923-4A08-9503-44F84F204A4B.png) <!-- baize:img-hook downloaded=false reason="正文 840 字 ≥300，非承重" -->

#### 时间步(Time Step)

设定重采样的周期。如果将“时间步”(Time Step)设置为 4，则系统会每隔四个帧放置一个关键帧。当“时间步”(Time Step)周期大于曲线中的关键帧的频率时，重采样的效果最佳。

![图：设定重采样的周期。如果将“时间步”(Time Step)设置为 4，则系统会每隔四个帧放置一个关键帧。当“时间步”(Ti…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-E9DE77D5-7B96-48D5-B039-EB8173E79CF4.png) <!-- baize:img-hook downloaded=false reason="正文 840 字 ≥300，非承重" -->

![图：设定重采样的周期。如果将“时间步”(Time Step)设置为 4，则系统会每隔四个帧放置一个关键帧。当“时间步”(Ti…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F2C9E367-1625-46B5-A47B-368277601235.png) <!-- baize:img-hook downloaded=false reason="正文 840 字 ≥300，非承重" -->
