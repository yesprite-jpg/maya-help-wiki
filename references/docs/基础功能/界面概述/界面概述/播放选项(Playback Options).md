# 播放选项(Playback Options)

通过[范围滑块](范围滑块%28Range%20Slider%29.md)旁边的播放选项，可以更改有关动画播放的设置，例如帧速率、循环和自动关键帧。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-9B1A9797-6C1C-49EA-AEFA-391A9E28A6B3.png) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

**A.**“帧速率”(Framerate)菜单 **B.** 循环(Loop) **C.** 缓存播放(Cached Playback) **D.** 音量(Volume) **E.** 自动关键帧(Auto Key) **F.** 动画首选项(Animation Preferences)

#### 帧速率(Framerate)

通过“帧速率”(Framerate)菜单可以设置场景的帧速率，以每秒帧数 (fps) 表示。它显示当前帧速率。

**注**

设置帧速率之后，Maya 中所有位置出现的该帧速率均会发生变化，无论是在

“文件打开”(File Open)

选项、

“首选项”(Preferences)

窗口中，还是在

“时间滑块”(Time Slider)

中均是如此。保存文件时，帧速率将一起保存。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-6E5993B0-9215-4383-8644-6508F1F9D141.gif) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

如果更改“帧速率”(Framerate)，它将在动画完成了一个循环或重新启动它后更新。

#### 循环(Loop)

单击此图标可循环切换 3 个动画播放状态：

##### **连续循环(Continuous Loop)** ![图：连续循环(Continuous Loop)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-5E88F9FB-731C-4536-8CD1-5E307979F381.png) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

![图：连续循环(Continuous Loop) 播放时重复播放范围。 播放一次(Play once) 对播放范围播放一次。 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-7ADCF893-619E-4606-951D-11D7626F5FAF.gif) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

播放时重复播放范围。

##### **播放一次(Play once)** ![图：播放一次(Play once)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-853DE082-0D36-43F0-8B0F-869B1A5E90BB.png) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

![图：连续循环(Continuous Loop) 播放时重复播放范围。 播放一次(Play once) 对播放范围播放一次。 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-74544456-D510-4CD4-8D3F-D4BE724731AF.gif) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

对播放范围播放一次。

##### **往返循环(Oscillating Loop)** ![图：往返循环(Oscillating Loop)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-881DA5F7-0626-4623-BCAE-E0079EE4FFDD.png) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

![图：连续循环(Continuous Loop) 播放时重复播放范围。 播放一次(Play once) 对播放范围播放一次。 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-CF66915E-6A1A-4F42-9A90-F26BAB9C3A46.gif) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

向前和向后循环播放范围。

**注**

提示：

您可以通过使用

“时间滑块”(Time Slider)首选项

中的

“设置帧和关键帧步长时循环播放范围”(Loop Play range when stepping frames and keys)

选项来设置循环，以循环播放范围或整个动画。

#### 缓存播放(Cached Playback) ![图：缓存播放(Cached Playback)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-EDBB8091-6F7E-4772-B1C6-6019FCB26E2F.png) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-159FAAA6-DB79-4578-9E36-D66EF11E4E07.gif) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

单击此图标可打开/关闭“缓存播放”(Cached Playback)。

“缓存播放”(Cached Playback)仅重新计算已在后台更改的场景部分，使您可以实时预览和处理动画。有关详细信息，请参见[使用“缓存播放”(Cached Playback)以提高播放速度](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D3D1DC33-D0CE-4BE3-B287-CDD4DC0B72C3)。

在“缓存播放”(Cached Playback) ![图：在“缓存播放”(Cached Playback) 图标上单击鼠标右键以显示用于切换缓存模式的选项，清除缓存，打开动画(A…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-EDBB8091-6F7E-4772-B1C6-6019FCB26E2F.png) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->图标上单击鼠标右键以显示用于切换缓存模式的选项，清除缓存，打开[动画(Animation)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F)或[时间滑块(Time Slider)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-51A80586-9EEA-43A4-AA1F-BF1370C24A64)设置首选项，您可在其中设置缓存填充的方向或在[时间滑块(Time Slider)](时间滑块%28Time%20Slider%29.md)上配置“缓存播放”(Cached Playback)状态行的外观，或者打开[颜色设置(Color Settings)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1FC6CC4E-6C21-44FA-A58B-AC31ED57B591)的“缓存播放”(Cached Playback)部分。

当“缓存播放”(Cached Playback)遇到一个不受支持的节点时，它将进入安全模式。“缓存播放”(Cached Playback)处于安全模式时，“缓存播放”(Cached Playback)状态行将变为黄色，并且“缓存播放”(Cached Playback) ![图：当“缓存播放”(Cached Playback)遇到一个不受支持的节点时，它将进入安全模式。“缓存播放”(Cached …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-E1962425-643E-4910-A1B0-C7A0AFD2573A.png) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->图标上会出现警告符号。出现此情况时，请参见[脚本编辑器(Script Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7C861047-C7E0-4780-ACB5-752CD22AB02E)以了解进入安全模式的原因。有关当前不受支持的节点列表，请参见[“缓存播放”(Cached Playback)不支持的节点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EF1C2D0C-622D-4FBB-B761-54E0A9765CE1)。

#### 体积 ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-A2FE50FE-BF80-4EFA-94CA-2D7DB09B34B6.png) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

单击**“音量”(Volume)**图标可显示滑块，可以在其中调整当前场景的声音级别。

双击此图标可禁用声音。图标将更改为 ![图：双击此图标可禁用声音。图标将更改为 以指示声音已禁用。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-D1AF9343-38E1-4738-B947-67232552114A.png) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" --> 以指示声音已禁用。

在图标上单击鼠标右键以访问[“音频”(Audio)菜单](时间滑块%28Time%20Slider%29/“音频”%28Audio%29菜单.md)，此菜单可用于在场景中导入或删除音频，以及选择音频波形在“时间滑块”(Time Slider)上的显示方式。

#### 自动关键帧(Auto Key) ![图：自动关键帧(Auto Key)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-1F8B7924-E708-4530-A547-41425A237DB3.png) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

可以使用此图标启用“自动关键帧”(Auto Key)模式。使用“自动关键帧”(Auto Key)后，当您更改当前时间和属性值时，系统自动在属性上设置关键帧。有关详细信息，请参见[使用自动关键帧](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4268F6E4-C35D-4222-BB47-B5BE5CD0B3A3)。

#### “时间滑块”(Time Slider)首选项 ![图：“时间滑块”(Time Slider)首选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-1EB081C1-051D-4C38-A396-22234CBDB74A.png) <!-- baize:img-hook downloaded=false reason="正文 1541 字 ≥300，非承重" -->

此图标是[“时间滑块”(Time Slider)首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-51A80586-9EEA-43A4-AA1F-BF1370C24A64)的快捷方式，通过它可以设置您想要的关键帧标记样式，以及要显示在[时间滑块(Time Slider)](时间滑块%28Time%20Slider%29.md)上的时间。
