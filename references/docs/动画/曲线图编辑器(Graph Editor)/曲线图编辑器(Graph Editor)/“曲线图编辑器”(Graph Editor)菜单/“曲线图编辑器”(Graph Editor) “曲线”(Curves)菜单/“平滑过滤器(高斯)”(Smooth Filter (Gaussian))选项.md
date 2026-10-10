# “平滑过滤器(高斯)”(Smooth Filter (Gaussian))选项

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 820 字 ≥300，非承重" -->

- 在[“曲线图编辑器”(Graph Editor)“曲线”(Curves)菜单](../“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)中，选择“平滑过滤器(高斯)”(Smooth Filter (Gaussian)) > ![图：在“曲线图编辑器”(Graph Editor)“曲线”(Curves)菜单中，选择“平滑过滤器(高斯)”(Smooth …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 820 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-2DAC14D6-10C6-440E-95B9-3B60A30C9715.gif) <!-- baize:img-hook downloaded=false reason="正文 820 字 ≥300，非承重" -->

应用于一个通道的平滑（高斯）过滤器

“平滑过滤器(高斯)”(Smooth Filter (Gaussian))类似于 MotionBuilder 平滑过滤器，因为它对关键帧进行平均以创建平滑移动。在过滤立方（自动）或重采样曲线时，“平滑过滤器(高斯)”(Smooth Filter (Gaussian))效果非常好。

#### 时间范围(Time Range)

指定简化曲线的时间范围。

#### 全部(All)

简化整个时间范围的曲线。

![图：简化整个时间范围的曲线。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F6782F25-43D0-4D8A-9689-0044259B0589.gif) <!-- baize:img-hook downloaded=false reason="正文 820 字 ≥300，非承重" -->

#### 选择(Selection)

使您可以选择曲线的一部分，以便可以将过滤器应用于限定区域，而不是影响整个曲线。按住 **Ctrl** 键可一次选择多个区域。

![图：使您可以选择曲线的一部分，以便可以将过滤器应用于限定区域，而不是影响整个曲线。按住 Ctrl 键可一次选择多个区域。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-2EF8DBA1-E778-40FC-9F60-FAADE9118644.gif) <!-- baize:img-hook downloaded=false reason="正文 820 字 ≥300，非承重" -->

#### 开始/结束(Start/End)

指定的时间范围（开始时间/结束时间）内的所有关键帧均会简化。

![图：指定的时间范围（开始时间/结束时间）内的所有关键帧均会简化。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-15C2134E-FB63-4142-83F2-B1047B7D24FA.gif) <!-- baize:img-hook downloaded=false reason="正文 820 字 ≥300，非承重" -->

#### 时间滑块(Time Slider)

简化由时间滑块的“播放开始”(Playback Start)和“播放结束”(End)时间定义的时间范围内的曲线。

![图：简化由时间滑块的“播放开始”(Playback Start)和“播放结束”(End)时间定义的时间范围内的曲线。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-7A42DEB4-22E2-43CA-9211-C6AF1AAE2433.gif) <!-- baize:img-hook downloaded=false reason="正文 820 字 ≥300，非承重" -->

#### 开始时间(Start Time)

指定时间范围的开始。仅当“开始/结束”(Start/End)启用时，该选项才可用。

#### 结束时间(End Time)

指定时间范围的结束。仅当“开始/结束”(Start/End)启用时，该选项才可用。

#### 预览(Preview)

使您可以在应用之前直观地看到曲线上的效果。 默认情况下，此选项处于启用状态。

![图：使您可以在应用之前直观地看到曲线上的效果。 默认情况下，此选项处于启用状态。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-2E64520D-31D5-4A7E-A213-EF685CA83973.gif) <!-- baize:img-hook downloaded=false reason="正文 820 字 ≥300，非承重" -->

#### Filter Width

用于设置平滑窗口宽度。默认值为 3。 值越大，平滑效果越强；值越小，平滑效果越弱。

#### 采样计数(Sample Count)

用于设置在曲线上采用的采样数。默认值是 8。

#### 使用四元数(Use Quaternions)

在平滑之前，将旋转曲线转化为四元数。在平滑之后，四元数将转化回 Euler 曲线。 若要应用“使用四元数”(Use Quaternions)，请选择所有 3 个旋转通道。

默认情况下该选项处于禁用状态。
