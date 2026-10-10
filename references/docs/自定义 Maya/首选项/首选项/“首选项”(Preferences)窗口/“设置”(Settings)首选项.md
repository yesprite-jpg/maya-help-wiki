# “设置”(Settings)首选项

可以在[首选项(Preferences)窗口](../“首选项”%28Preferences%29窗口.md)的“设置”(Settings)类别中设置以下首选项。

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

## 世界坐标系(World Coordinate System)

#### 上方向轴(Up axis)

将上方向轴设定为 Y 或 Z。默认为 Y。

## 工作单位(Working Units)

此处设置的值仅用于当前场景；这样，无需更改默认的新场景单位即可更改当前场景单位。

若要设置新场景的默认工作单位，请更新[新建场景选项(New Scene Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8F961875-1D41-4C52-9CD5-B90DE75C546C)（“文件 > 新建场景”(File > New Scene) > ![图：若要设置新场景的默认工作单位，请更新新建场景选项(New Scene Options)（“文件 新建场景”(File N…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1539 字 ≥300，非承重" -->）中的设置。可以指定线性单位、角度单位和时间设置。

打开具有不同单位的场景文件时，不会覆盖此处指定的单位。首次运行 Maya 时，您在首选项此处设置的“工作单位”(Working Unit)值均会用来设置“默认工作单位”(Default Working Units)。

#### 线性(Linear)

为使用线性值的操作（例如，移动和缩放）设置度量单位。默认单位为厘米。

#### 角度(Angular)

为使用角度值的操作（例如，旋转）设置度量单位。默认单位为度。

#### 时间(Time)

为动画设定工作时间单位。[时间滑块](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/files/GUID-827ED8CD-C6AA-4495-8B5E-2FC98C8D49EE.htm)将以此单位显示其时间值，并在您更改帧中指定的时间单位时进行更新。

帧选择包括：2 fps、3 fps、4 fps、5 fps、6 fps、8 fps、10 fps、12 fps、15 fps、16 fps、20 fps、23.976 fps、24 fps (电影)、25 fps (PAL)、29.97 fps、29.97 df (丢帧)、30 fps、40 fps、47.952 fps、48 fps (演示)、50 fps (PAL 场)、59.94 fps、60 fps (NTSC 场)、75 fps、80 fps、100 fps、120 fps、125 fps、150 fps、200 fps、240 fps、250 fps、300 fps、375 fps、400 fps、500 fps、600 fps、750 fps、1200 fps、1500 fps、2000 fps、3000 fps、6000 fps、44 100 fps 和 48 000 fps。

**注**

设置帧速率之后，Maya 中所有位置出现的该帧速率均会发生变化，无论是在

“文件打开”(File Open)

选项、

“首选项”(Preferences)

窗口中，还是在

“时间滑块”(Time Slider)

中均是如此。保存文件时，帧速率将一起保存。

时钟值包括：毫秒、秒、分钟、小时

术语*“帧”*和*“时间”*指的是“时间滑块”(Time Slider)中的显示的工作时间单位。确切地说，仅当以每秒帧数 (fps) 指定“时间”(Time)时才会应用术语“帧”。通常，时间可以引用为帧值或时钟值。

**注**

在时间滑块中，已舍入到小数点后第二位的任何数字旁边会显示一个星号“

*

”，指示该值是近似值。如果在“时间码”(Time Code)与“帧”(Frames)之间切换，或者如果在

“时间滑块”(Time Slider)首选项

中禁用

“捕捉到整个帧”(Snap to Whole Frames)

选项，有时会出现这种情况。

![图：为动画设定工作时间单位。时间滑块将以此单位显示其时间值，并在您更改帧中指定的时间单位时进行更新。 帧选择包括：2 fps…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-D541BB3B-1D4A-437C-A953-FF8F993A7A13.png) <!-- baize:img-hook downloaded=false reason="正文 1539 字 ≥300，非承重" -->

## 容差(Tolerance)

“容差”(Tolerance)值可确定原始曲线和适配曲线（或插值曲线）之间保持的精确度。此设置将全局应用于 Maya。此设置可根据具体情况进行更改。设定以下容差选项：

#### 位置(Positional)

设定原始曲线和插值曲线的实际位置之间的精确度。

#### 切向(Tangential)

设定用以确定两个 NURBS 对象是否会跨共享的边或点切线所需的精确度。

## 相关主题

- [Maya 如何计算时间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A9F91D81-3149-47AF-9E37-83A89242D870)

- [时间滑块(Time Slider)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/files/GUID-827ED8CD-C6AA-4495-8B5E-2FC98C8D49EE.htm)
