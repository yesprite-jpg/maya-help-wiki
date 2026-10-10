# 自定义“时间滑块”(Time Slider)

您可以更改“时间滑块”(Time Slider)各种元素的颜色和尺寸以符合自己的工作样式。

## 调整“时间滑块”(Time Slider)的大小

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-8FF9AF2D-8410-4EE2-B290-AF0C1BEC175E.gif) <!-- baize:img-hook downloaded=false reason="正文 1967 字 ≥300，非承重" -->

您可以像界面中的其他元素一样调整 Maya 的[时间滑块(Time Slider)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-827ED8CD-C6AA-4495-8B5E-2FC98C8D49EE.htm)的大小，方法是将光标悬停在顶边上，直到变为分隔条光标，然后向上或向下拖动此光标。

时间滑块高度与工作区一起保存；这些设置将持续存在，直至手动更改（或“首选项”(Preferences)已[重置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-393D1ECA-9B6E-4625-B5B1-3F28E62AFB1C)）。

## 降低“时间滑块”(Time Slider)分隔条光标反应能力

如果当光标经过“时间滑块”(Time Slider)时，将光标更改为分隔条光标会过于分散注意力，那么可以更改以下选项变量：

```text
  optionVar -iv "splitterHandleMargin" 3
```

若要增加分隔条光标触发，请设置一个较大的值。

默认设置为 **3**，最大设置为 **8**。

### 禁用“时间滑块”(Time Slider)分隔条光标

若要关闭分隔条光标以使其不显示，请转到 Maya .json 文件的 prefs/workspaces/ 部分，并将 heightProperty 从 fixed 更改为 free。

## 关键帧标记

关键帧标记是“时间滑块”(Time Slider)中的红色（默认）标记，表示为选定对象设置的关键帧。受控关键点是在“时间滑块”(Time Slider)中显示为绿色标记的特殊类型关键帧。请参见[受控关键点](../../关键帧动画/关键帧动画/受控关键点.md)。

在“时间滑块”(Time Slider)中设定关键帧的厚度

1. 选择“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)。

  将显示“首选项”(Preferences)窗口。

2. 在“时间滑块”(Time Slider)区域中，设定“关键帧标记大小”(Key Tick Size)首选项设置。

  关键帧厚度以像素为单位。最小关键帧厚度为 1 像素，同时最大关键帧厚度为 63 像素。

在“时间滑块”(Time Slider)中设定曲线关键帧的颜色

1. 在“曲线图编辑器”(Graph Editor)图形视图中，选择一条曲线。

2. 在“曲线图编辑器”(Graph Editor)菜单栏中，选择“曲线 > 属性总表”(Curves > Spreadsheet)。

  所选动画曲线的属性总表显示在“属性编辑器”(Attribute Editor)中。

3. 选择“曲线颜色”(Curve Color)并启用“使用曲线颜色”(Use Curve Color)。

  所有曲线在时间滑块中的关键帧现在都是您选择的“曲线颜色”(Curve Color)。

设定时间滑块中单个关键帧的颜色

1. 选择“窗口 > 设置/首选项 > 颜色设置 > 动画”(Windows > Settings/Preferences > Color Settings > Animation)。

2. 选择“时间滑块 Tick 特殊”(Time Slider Tick Special)颜色并单击“保存”(Save)。

3. 在“曲线图编辑器”(Graph Editor)中，选择要以“时间滑块 Tick 特殊”(Time Slider Tick Special)颜色绘制的关键帧。

4. 在命令行或“脚本编辑器”(Script Editor)中，输入如下所示带有 -tickDrawSpecial (-tds) 标志的 keyframe MEL 命令：

  keyframe -tds on

  然后，按数字键区上的 Enter 键。

  您为其选择和设定 -tds 标志的关键帧当前在时间滑块中是以“时间滑块 Tick 特殊”(Time Slider Tick Special)颜色绘制的。

  有关该标志的详细信息，请参见 MEL 命令参考文档中的 **keyframe**。

  **注**

  - “时间滑块 Tick 特殊”(Time Slider Tick Special)颜色首选项将替代“曲线颜色”(Curve Color)属性设定的关键帧颜色。

  - 如果时间滑块中同时有多个关键帧并且其中一个关键帧的 -tds 标志设定为 on，则“时间滑块 Tick 特殊”(Time Slider Tick Special)颜色将优先于其他的关键帧颜色。

## 时间滑块颜色

您可以自定义“时间滑块”(Time Slider)的颜色设置，以增加可见性，尤其是对于较大的时间轴。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-2D1152F3-EF53-4AE4-A018-CD7270E72B37.png) <!-- baize:img-hook downloaded=false reason="正文 1967 字 ≥300，非承重" -->

打开“时间滑块”(Time Slider)的颜色设置

1. 选择“窗口 > 设置/首选项 > 颜色设置”(Windows > Settings/Preferences > Color Settings)。

2. 在“颜色设置”(Color Settings)窗口中，展开“动画”(Animation)标题。

更改当前时间指示器的颜色

更改“时间滑块当前帧”(Time Slider Current Frame)设置。（单击颜色平铺，然后选择一个新颜色。）

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-132439F2-1F1F-45E8-8E95-BD10FDC3D531.png) <!-- baize:img-hook downloaded=false reason="正文 1967 字 ≥300，非承重" -->

更改“时间滑块”(Time Slider)的前景或背景的颜色

更改“时间滑块前景”(Time Slider Foreground)和“时间滑块背景”(Time Slider Background)设置。
