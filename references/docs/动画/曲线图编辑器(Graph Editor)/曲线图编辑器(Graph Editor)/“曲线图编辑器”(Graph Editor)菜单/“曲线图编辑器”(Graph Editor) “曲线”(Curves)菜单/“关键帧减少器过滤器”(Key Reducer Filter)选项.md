# “关键帧减少器过滤器”(Key Reducer Filter)选项

- 在[“曲线图编辑器”(Graph Editor)“曲线”(Curves)菜单](../“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)中，选择“关键帧减少器过滤器”(Key Reducer Filter) > ![图：在“曲线图编辑器”(Graph Editor)“曲线”(Curves)菜单中，选择“关键帧减少器过滤器”(Key Red…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 975 字 ≥300，非承重" -->

“关键帧减少器过滤器”(Key Reducer Filter)使用与[“平滑过滤器(Butterworth)”(Smooth Filter (Butterworth))](“平滑过滤器%28Butterworth%29”%28Smooth%20Filter%20%28Butterworth%29%29选项.md)不同的算法，并通过移除曲线上不必要的关键帧来减少关键帧的数量。

**注**

若要还原过滤器默认设置，请单击“过滤器”(Filter)窗口中的“编辑 > 重置设置”(Edit > Reset Settings)。

#### 时间范围(Time Range)

指定简化曲线的时间范围。

##### 全部(All)

简化整个时间范围的曲线。

![图：简化整个时间范围的曲线。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F6782F25-43D0-4D8A-9689-0044259B0589.gif) <!-- baize:img-hook downloaded=false reason="正文 975 字 ≥300，非承重" -->

##### 选择(Selection)

使您可以选择曲线的一部分，以便可以将过滤器应用于限定区域，而不是影响整个曲线。按住 **Ctrl** 键可一次选择多个区域。

![图：使您可以选择曲线的一部分，以便可以将过滤器应用于限定区域，而不是影响整个曲线。按住 Ctrl 键可一次选择多个区域。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-2EF8DBA1-E778-40FC-9F60-FAADE9118644.gif) <!-- baize:img-hook downloaded=false reason="正文 975 字 ≥300，非承重" -->

##### 时间滑块(Time Slider)

简化由时间滑块的“播放开始”(Playback Start)和“播放结束”(End)时间定义的时间范围内的曲线。

![图：简化由时间滑块的“播放开始”(Playback Start)和“播放结束”(End)时间定义的时间范围内的曲线。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-7A42DEB4-22E2-43CA-9211-C6AF1AAE2433.gif) <!-- baize:img-hook downloaded=false reason="正文 975 字 ≥300，非承重" -->

##### 开始/结束(Start/End)

指定的时间范围（开始时间/结束时间）内的所有关键帧均会简化。

![图：指定的时间范围（开始时间/结束时间）内的所有关键帧均会简化。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-15C2134E-FB63-4142-83F2-B1047B7D24FA.gif) <!-- baize:img-hook downloaded=false reason="正文 975 字 ≥300，非承重" -->

###### 开始时间(Start Time)

指定时间范围的开始。仅当“开始/结束”(Start/End)启用时，该选项才可用。

###### 结束时间(End Time)

指定时间范围的结束。仅当“开始/结束”(Start/End)启用时，该选项才可用。

#### 预览(Preview)

使您可以在应用之前直观地看到曲线上的效果。 默认情况下，此选项处于启用状态。

![图：使您可以在应用之前直观地看到曲线上的效果。 默认情况下，此选项处于启用状态。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-2E64520D-31D5-4A7E-A213-EF685CA83973.gif) <!-- baize:img-hook downloaded=false reason="正文 975 字 ≥300，非承重" -->

#### **精度模式(Precision Mode)**

从两种不同的方法中进行选择以应用过滤器容差，并使用“精度”(Precision)滑块来设置值。

##### 绝对(Absolute)

丢弃与“精度”(Precision)滑块中指定的误差容差不匹配的关键帧。

##### 百分比(Percentage)

丢弃某一百分比曲线值内的关键帧。

**注**

您可以将

“百分比”(Percentage)

设置为

0

，并将过滤器转换为固定关键帧减少器来消除冗余的关键帧。

#### 在曲线上同步关键帧(Sync Keys on Curves)

用于同级曲线（例如，平移 X、Y 和 Z），以确保若在一个同级曲线上有一个关键帧，它将应用于所有曲线，从而在相同的帧时间保持关键帧对齐。

#### 按切线保留关键帧(Preserve Keys by Tangent)

使您可以将选定的切线类型从过滤中排除。
