# 新建场景选项(New Scene Options)

使用这些选项来设置在选择“文件 > 新建场景”(File > New Scene)时发生的情况。另请参见[创建、打开或保存场景文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DC183670-EF0F-4E69-AEDF-69D408D82408)。

#### 启用默认场景(Enable Default Scene)

启用时，您可以使用“默认场景”(Default scene)来选择在每次启动新场景时要加载的特定文件。

#### 默认场景(Default scene)

单击文件夹（浏览）图标，然后选择在您每次选择“文件 > 新建场景”(File > New Scene)时要加载的 Maya 文件。（仅当“启用默认场景”(Enable Default Scene)处于启用状态时可用。）

## 默认工作单位(Default Working Units)

允许指定新场景的默认工作单位。

您还可以使用[设置首选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/files/GUID-4D653DC9-57AA-4D8B-987A-5B7A9735CAF0.htm)（“窗口 > 设置/首选项 > 首选项”(Window > Settings/Preferences > Preferences)）来设置工作单位。这些首选项仅与当前场景相关联，这表示无需更改*默认*的新场景单位即可更改*当前*场景单位。

**注**

当

“启用默认场景”(Enable Default Scene)

处于启用状态时，

“默认工作单位”(Default Working Units)

选项将不可用，因为工作单位已在默认场景中设置。

打开具有不同工作单位的场景文件时，不会覆盖此处指定的单位。首次运行 Maya 时，会从首选项的“工作单位”(Working Unit)值中设定“默认工作单位”(Default Working Units)。

#### 不要重置工作单位(Do not reset working units)

允许暂时禁用您设置的、用于打开新场景的“默认工作单位”(Default Working Units)。

#### 线性(Linear)

为使用线性值的操作（例如，移动和缩放）设定度量单位。默认单位为厘米。

#### 角度(Angular)

为使用角度值的操作（例如，旋转）设定度量单位。默认单位为度。

#### 时间(Time)

为动画设定工作时间单位。[时间滑块](../../../../界面概述/界面概述/时间滑块%28Time%20Slider%29.md)将以此单位显示其时间值，并在您更改帧中指定的时间单位时进行更新。

帧选择包括：2 fps、3 fps、4 fps、5 fps、6 fps、8 fps、10 fps、12 fps、15 fps、16 fps、20 fps、23.976 fps、24 fps (电影)、25 fps (PAL)、29.97 fps、29.97 df (丢帧)、30 fps、40 fps、47.952 fps、48 fps (演示)、50 fps (PAL 场)、59.94 fps、60 fps (NTSC 场)、75 fps、80 fps、100 fps、120 fps、125 fps、150 fps、200 fps、240 fps、250 fps、300 fps、375 fps、400 fps、500 fps、600 fps、750 fps、1200 fps、1500 fps、2000 fps、3000 fps、6000 fps、44 100 fps 和 48 000 fps。

术语*“帧”*和*“时间”*指的是“时间滑块”(Time Slider)中的显示的工作时间单位。确切地说，仅当以每秒帧数 (fps) 指定“时间”(Time)时才会应用术语“帧”。通常，时间可以引用为帧值或时钟值。

**注**

设置帧速率之后，Maya 中所有位置出现的该帧速率均会发生变化，无论是在

“文件打开”(File Open)

选项、

“首选项”(Preferences)

窗口中，还是在

“时间滑块”(Time Slider)

中均是如此。保存文件时，帧速率将一起保存。

## 默认时间滑块设置(Default Time Slider Settings)

#### 播放开始/结束(Playback start/end)

指定播放范围开始和结束时间。播放开始和结束时间指定“时间滑块”(Time Slider)播放范围。播放范围始终在动画范围内。也可以指定时间单位。请参见[编辑动画首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D1E323B7-C582-4E32-99A3-F081422469D2)。

#### 动画开始/结束(Animation start/end)

指定动画范围开始和结束时间。动画开始和结束时间指定“范围滑块”范围。播放范围始终在动画范围内，因此更改动画开始和结束时间也会更改播放开始和结束时间。默认动画开始时间为 1.00。默认动画结束时间为 48.00。也可以指定时间单位。请参见[编辑动画首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D1E323B7-C582-4E32-99A3-F081422469D2)。

## 默认颜色管理设置(Default Color Management Settings)

#### 颜色管理已启用(Color Management enabled)

指定是否对新场景启用或禁用颜色管理。若要更改当前场景的颜色管理设置，请使用[“颜色管理”(Color Management)首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2D9BBB9D-49F0-44C6-8BFF-B237FD8ED746)中的选项。有关常规详细信息，请参见[颜色管理](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5320733B-F9B6-4429-BCAA-F7251D77A8E2)。
