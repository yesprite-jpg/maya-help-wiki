# “播放”(Playback)菜单

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 1767 字 ≥300，非承重" -->

位于“动画”(Animation)菜单集中。

#### 播放预览(Playblast)

可以通过输出影片或单独帧序列来预览场景中的动画，具体取决于您设置的[“播放预览选项”(Playblast Options)](../../../动画基础知识/动画基础知识/预览动画/播放预览动画/播放预览选项%28Playblast%20Options%29.md)。（选择“播放 > 播放预览”(Playback > Playblast) > ![图：可以通过输出影片或单独帧序列来预览场景中的动画，具体取决于您设置的“播放预览选项”(Playblast Options)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1767 字 ≥300，非承重" -->可打开并设置这些选项。）

默认输出格式如下：.avi (Windows)、.image (Linux) 和 .qt (Mac OS X)。

另请参见[播放预览动画](../../../动画基础知识/动画基础知识/预览动画/播放预览动画.md)。

#### 缓存播放(Cached Playback)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 1767 字 ≥300，非承重" -->

使您可以激活“缓存播放”(Cached Playback)，此功能将场景的动画存储在内存中，以提高性能并减少对播放预览的需求。

您还可以从此菜单中切换“缓存”(Caching)模式、清除缓存、打开[缓存播放首选项(Cached Playback Preferences)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3CB35662-DB1D-4CF3-9135-E09B973635DE)和“缓存播放”(Cached Playback) [颜色](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1FC6CC4E-6C21-44FA-A58B-AC31ED57B591)窗口。

有关详细信息，请参见[使用“缓存播放”(Cached Playback)以提高播放速度](../../../缓存播放%28Cached%20Playback%29/缓存播放%28Cached%20Playback%29/使用“缓存播放”%28Cached%20Playback%29以提高播放速度.md)。

## 控件

#### 播放控件(Play Controls)

此部分包含播放场景所需的控件。请参见[播放控件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-277ADCBF-6277-4B32-81E0-AEB6D081153F)。

## 设置

#### 将范围设置为(Set Range To)

- **“开始/结束”(Start/End)**会将播放范围设置为在“播放范围”(Playback Range)数值输入字段中设置的“开始”(Start)和“结束”(End)值。

- **“最小值/最大值”(Min/Max)**会将播放范围设置为场景的第一个和最后一个关键点。

- **“选定”(Selected)**会将播放范围设定为“时间滑块”(Time Slider)上的当前选择所定义的范围。

- **“已启用片段”(Enabled clips)**会将播放范围设置为包含所有已启用片段的范围。

- **“声音长度”(Sound Length)**会将播放范围设定为当前加载到“时间滑块”(Time Slider)中的声音的持续时间。

- **“首选项”(Preferences)**会将播放范围设置为“首选项”(Preferences)窗口中的值。

#### 播放速度(Playback Speed)

使用该选项可设置当前场景的播放速度和帧速率。

自由播放每一帧(Play Every Frame, Free)

将当前场景的播放速度设置为播放每一帧，而不会受制于特定的最大帧速率。

以最大实时速度播放每一帧(Play Every Frame, Max Real-time)

将当前场景的播放速度设置为播放每一帧，但受制于每秒 24 帧的最大帧速率。

实时(Real-time)

将当前场景的播放速度设置为每秒 24 帧。

另请参见[为播放优化场景](../../../动画基础知识/动画基础知识/播放动画/优化场景播放.md)

#### 播放循环(Playback Looping)

若要选择播放循环选项，请在时间滑块上单击鼠标右键，然后选择“播放循环 > 一次”(Playback Looping > Once)、“播放循环 > 往返”(Playback Looping > Oscillate)或“播放循环 > 连续”(Playback Looping > Continuous)（有关此行为的演示，请参见[播放选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-9853B7B5-8AD5-46F6-A921-A3771A505AD1.htm)中的“循环”(Loop)）。这些选项与使用[播放选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-9853B7B5-8AD5-46F6-A921-A3771A505AD1.htm)和“首选项”(Preferences)窗口中的“循环”(Loop)图标 ![图：若要选择播放循环选项，请在时间滑块上单击鼠标右键，然后选择“播放循环 一次”(Playback Looping Once…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-5E88F9FB-731C-4536-8CD1-5E307979F381.png) <!-- baize:img-hook downloaded=false reason="正文 1767 字 ≥300，非承重" --> 相同。

**注**

提示：

您可以通过使用

“时间滑块”(Time Slider)首选项

中的

“设置帧和关键帧步长时循环播放范围”(Loop Play range when stepping frames and keys)

选项来设置循环，以循环播放范围或整个动画。

#### 启用阶跃预览(Enable Stepped Preview)

您可以将**“阶跃预览”(Stepped Preview)**模式在启用和禁用间进行切换，轻松将曲线从样条线切换到阶跃切线以及从阶跃切线切换到样条线。启用此选项时，关键帧可暂时显示为阶跃切线，因此当对象位置碰撞到各个关键帧时，播放动画能提供快速查看对象位置。禁用此选项时，动画将使用原始切线如常播放。请参见[“阶跃”(Stepped)](../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-59FDEC35-60E1-446E-9CA9-0AA5A1A65744)切线。

#### 播放缓存

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1767 字 ≥300，非承重" -->

打开和关闭播放缓存。播放缓存仅重新计算已在后台更改的场景部分，使您可以实时预览和处理动画。有关详细信息，请参见[使用“缓存播放”(Cached Playback)以提高播放速度](../../../缓存播放%28Cached%20Playback%29/缓存播放%28Cached%20Playback%29/使用“缓存播放”%28Cached%20Playback%29以提高播放速度.md)。

## 渲染

#### 渲染当前帧(Render Current Frame)

打开“渲染视图”(Render View)窗口，并渲染当前场景。

#### 显示渲染设置(Display Render Settings)

打开[渲染设置窗口](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-59DFB8B7-776B-4243-B404-A3D602FF8CFD)。
