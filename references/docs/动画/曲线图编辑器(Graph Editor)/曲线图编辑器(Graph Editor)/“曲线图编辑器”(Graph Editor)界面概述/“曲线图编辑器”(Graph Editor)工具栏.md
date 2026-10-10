# “曲线图编辑器”(Graph Editor)工具栏

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

曲线图编辑器工具栏包含许多常用选项（位于菜单中，也可通过在“曲线图编辑器”(Graph Editor)界面上单击鼠标右键找到）的图标。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-8A6D1DE9-BD60-454B-BA6F-7A19E71B2AAA.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

曲线图编辑器工具栏 (**A**) 默认 (**B**) 简单

**注**

此工具栏有两个版本：默认版本具有一套完整的曲线编辑和显示选项，

“简单工具栏”(Simple Toolbar)

仅包含选定的编辑和显示选项。可以使用

“曲线图编辑器”(Graph Editor)“视图”(View)菜单

中的

“简单工具栏”(Simple Toolbar)

开关在这些工具栏之间切换。

## 移动最近拾取的关键帧工具(Move Nearest Picked Key Tool)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-9CB815BF-DD09-415F-8E4E-979CF5270544.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

使用该工具可以通过单一鼠标操作来操纵各个关键帧和切线。

该工具与“移动工具”(Move Tool)有所不同。该工具同一时间只能操纵一个关键帧，或者操纵某条活动曲线的最近选定关键帧，而无需在图表视图中精确地选择关键帧或切线控制柄。

### “移动最近拾取的关键帧工具”(Move Nearest Picked Key Tool)选项窗口

双击“移动最近拾取的关键帧工具”(Move Nearest Picked Key Tool)图标可打开“工具设置”(Tool Settings)窗口。

直接关键帧设置(Direct Key settings)

设定下列选项之一：

#### 仅移动(Move Only)

禁用“移动最近拾取的关键帧工具”(Move Nearest Picked Key tool)的功能以在曲线的所有关键帧中扫描（请参见下面的“移过”(Move Over)）。

#### 移过(Move Over)

使用默认设置可以使工具沿曲线的关键帧扫描整个活动曲线。这样可加快动画曲线的精细调整。

#### 仅选定对象(Selected only)

如果启用该选项（默认），则单击编辑仅适用于选定曲线。如果禁用该选项，则可以单击来编辑所有曲线。如果希望可以对所有曲线进行单击操纵，请禁用该选项。

**注**

提示：

如果需要使用单击切线编辑工作流，请从“曲线图编辑器”(Graph Editor)菜单栏中选择“视图 > 切线 > 始终”(View > Tangents > Always)，将切线控制柄设定为始终显示。

请参见[使用单击曲线编辑](../../../关键帧动画/关键帧动画/编辑曲线/使用单击曲线编辑.md)。

## 晶格变形关键帧工具(Lattice Deform Keys Tool)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-7DFFB022-8187-4F24-A4E7-435E7776578C.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

使用该工具可以通过围绕关键帧组绘制一个晶格变形器，在“曲线图编辑器”(Graph Editor)中操纵曲线，从而可以同时操纵许多关键帧。该工具可提供对动画曲线的高级别控制。

请参见[晶格变形关键帧工具](../../../动画引用/动画引用/动画工具/晶格变形关键帧工具%28Lattice%20Deform%20Keys%20Tool%29.md)。

## 区域工具(Region Tool)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-38E8A26E-F981-406B-91D4-CE47B3030208.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

启用区域选择模式，使您可以在图表视图区域中拖动以选择一个区域，然后在该区域内在时间和值上缩放关键帧。请参见[缩放关键帧](../../../关键帧动画/关键帧动画/编辑关键帧/缩放关键帧.md)或[缩放曲线](../../../关键帧动画/关键帧动画/编辑曲线/缩放曲线.md)。

## 重定时工具(Retime Tool)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96B1004C-80CD-490F-87AA-87F06CE320BE.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

启用[“重定时工具”(Retime Tool)](../../../动画引用/动画引用/动画工具/重定时工具%28Retime%20Tool%29.md)，从而可以双击图表视图区域来创建重定时标记。然后，可以拖动这些标记来直接调整动画中关键帧移动的计时，使其发生得更快或更慢，以及拖动它们以提前或推后发生。请参见[重定时动画](../../../关键帧动画/关键帧动画/编辑曲线/重定时动画.md)。

**注**

提示：

您也可以从

“曲线图编辑器”(Graph Editor)

“编辑 > 变换工具 > 重定时工具”(Edit > Transformation Tools > Retime Tool)

菜单中访问

“重定时工具”(Retime Tool)

。

## 统计信息(Stats)

“统计信息”(Stats)字段以数值表示选定关键帧的时间和值。可以通过从键盘输入值来编辑这些字段，或者通过在输入中使用下列运算符进行相对应的操作：

| 运算符 | 功能 |
|---|---|
| **+=value** | 会将输入的值与现有值相加 |
| ***=value** | 会将输入的值与现有值相乘 |
| **-=value** | 会从现有值减去输入的值 |
| **/=value** | 将现有值除以输入的值 |

## 框显全部(Frame all)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-AC8F3337-DCAE-42E6-89BD-B5CC5E392A61.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

在“曲线图编辑器”(Graph Editor)图表视图中框显所有当前动画曲线的关键帧。

## 框显播放范围(Frame playback range)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-CA6CD768-52B3-4278-8DD3-3F07760D450D.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

在“曲线图编辑器”(Graph Editor)图表视图中框显当前“播放范围”(Playback Range)内的所有关键帧。

## 使视图围绕当前时间居中(Center the view about the current time)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-08D37895-563C-4696-A7CD-8EE29CA70A12.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

在“曲线图编辑器”(Graph Editor)图表视图中使当前时间居中。

## 自动跨度(旧版)(Auto Span (Legacy))

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F93BEEC0-9072-40F7-A8A6-813CBD4BB7CC.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

（此选项存在于先前版本的 Maya 中，但仅称为**“自动”(Auto)**。）

提供对“曲线图编辑器”(Graph Editor)菜单项“切线 > 自动”(Tangents > Auto)的轻松访问。请参见[自动](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-4AC9EE2F-74F2-4B29-A5A2-FAC691CB9B7F)。

## 自动缓入缓出(Auto Ease)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-6B8497F1-ED5B-4E0F-A701-94D9A4C9A044.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

对切线应用立方融合权重，这些权重受到相邻关键帧显著影响。

## 自动混合(Auto Mix)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-D90BE8C9-1D6E-4B6C-998F-71FC1C9A1662.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

将两个坡度的线性融合应用于切线。

## 自动自定义(Auto Custom)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-72D92338-25BA-4890-8836-5A63A4336726.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

选择“自动自定义”(Auto Custom) > ![图：选择“自动自定义”(Auto Custom) 时，应用“自动自定义”(Auto Custom)选项中指定为系数的值。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->时，应用“自动自定义”(Auto Custom)选项中指定为系数的值。

## 样条线切线(Spline Tangents)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-BEFE3165-FE9C-473D-A543-09603B452F45.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“切线 > 样条线”(Tangents > Spline)的轻松访问。请参见[样条线](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-E4382866-B01E-4DDF-81FF-57B625A999E8)。

## 钳制切线(Clamped Tangents)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-DB3C2042-5902-4F1B-B830-97889C991F27.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“切线 > 钳制”(Tangents > Clamped)的轻松访问。请参见[钳制](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-D86099CD-5983-408F-B33F-202C53D71E50)。

## 线性切线(Linear Tangents)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-D6A24010-D3FE-489A-9267-9C8E0BA92AF5.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“切线 > 线性”(Tangents > Linear)的轻松访问。请参见[线性](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-809B2936-77CF-4A06-BC13-2211644D26BD)。

## 平坦切线(Flat Tangents)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-CC64427A-F9D0-4F72-AA73-E33BA931A6AC.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“切线 > 平坦”(Tangents > Flat)的轻松访问。请参见[平坦](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-DBA1B6F6-77C7-4AAF-8FC6-6734A385843E)。

## 阶跃切线(Step Tangents)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-BE4EC725-E303-4C5D-BBE7-A7E5B0EDC913.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“切线 > 阶跃”(Tangents > Stepped)的轻松访问。请参见[阶跃](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-78B1A9BB-7730-4DCC-8DD3-00FA60E2C7E9)。

## 高原切线(Plateau Tangents)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-C89A97DB-1672-4FDF-B2CE-08918F2BA77C.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“切线 > 高原”(Tangents > Plateau)的轻松访问。请参见[高原](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-9A1E3DC1-3EDB-4F02-A2D7-EC90AF655AEC)。

## 默认入切线(Default In Tangent)/默认出切线(Default Out Tangent)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-E94B1305-E371-4B73-A675-BD3CDA6FE7CE.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-AC4FDC7A-BAD9-4511-9A94-AB8D7111DE06.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

打开一个菜单，从中可以为关键帧选择默认的入切线或出切线设置。请参见[“曲线图编辑器”(Graph Editor)“切线”(Tangents)菜单](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md)中的“默认入切线”(Default In Tangent)和“默认出切线”(Default Out Tangent)。

## 缓冲区曲线快照(Buffer Curve Snapshot)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-3908161D-BD37-4507-B182-766916F43FA8.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

若要拍摄曲线的快照，请选择该动画曲线，然后使用“曲线 > 缓冲区曲线快照”(Curves > Buffer Curve Snapshot)或“缓冲区曲线快照”(Buffer Curve Snapshot)按钮。请参见[缓冲区曲线快照](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md#GUID-619CAE9C-107D-4504-A769-227DDC847153__GUID-38366EE1-ACDB-4CD3-AE18-59BFCE6BA1D0)。

使用“缓冲区曲线快照”(Buffer Curve Snapshot)和“交换缓冲区曲线”(Swap Buffer Curves)将对当前动画曲线所做的更改与其先前的形状相比较。请注意，代表原始曲线的灰色曲线是可见的。

## 交换缓冲区曲线(Swap Buffer Curve)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-E669CC84-B51B-4D22-A974-66F4101D36FE.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

若要将缓冲区曲线与已编辑的曲线交换，请使用“曲线 > 交换缓冲区曲线”(Curves > Swap Buffer Curve)或“交换缓冲区曲线”(Swap Buffer Curve)按钮。请参见[交换缓冲区曲线](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md#GUID-619CAE9C-107D-4504-A769-227DDC847153__GUID-C51069F1-EB79-4663-AAB6-A363F98D08B9)。

使用“缓冲区曲线快照”(Buffer Curve Snapshot)和“交换缓冲区曲线”(Swap Buffer Curves)将对当前动画曲线所做的更改与其先前的形状相比较。通过在这些曲线之间自由地来回切换来测试动画。

## 断开切线(Break Tangents)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-C5E4603B-05DF-492F-ABE0-731C7A5CBA20.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“切线 > 断开切线”(Tangents > Break Tangents)的轻松访问。请参见[断开切线](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-1C0AE09E-3014-4E40-82FC-F70F0FEED385)。

断开的切线会显示为蓝色。

## 统一切线(Unify Tangents)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-E8E41555-E73E-4BC9-A6DB-4A780F961F7B.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“切线 > 统一切线”(Tangents > Unify Tangents)的轻松访问。请参见[统一切线](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-5D1C4E6A-77C3-4457-8DFB-EB2F4E287202)。

## 自由切线长度(Free Tangent Length)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-73B67904-2E93-4533-9D76-1C518D9891F7.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

（在 Maya 的早期版本中，以前称为“自由切线权重”(Free Tangent Weight)。）

提供对“曲线图编辑器”(Graph Editor)菜单栏项“切线 > 自由切线权重”(Tangents > Free Tangent Weight)的轻松访问。请参见[自由切线长度(Free Tangent Length)](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-A257D0ED-4018-47DA-B532-DE842106790B)。切线控制柄在未加权时呈浅灰色。

## 锁定切线长度(Lock Tangent Length)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-DE292D0F-418D-4A06-A653-264AB2667062.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

（在 Maya 的早期版本中，以前称为“锁定切线权重”(Lock Tangent Weight)。）

提供对“曲线图编辑器”(Graph Editor)菜单栏项“切线 > 锁定切线长度”(Tangents > Lock Tangent Length)的轻松访问。请参见[锁定切线长度(Lock Tangent Length)](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md#GUID-43A4FE2C-4863-4EA6-B6AE-6D2B6757F6C7__GUID-3B1C1A1E-711E-4734-A03A-17BCCCD16960)。切线控制柄被锁定时为黑色。

可以直观地识别锁定的切线或断开的切线，并为锁定的切线设置权重。

“曲线图编辑器”(Graph Editor)会显示锁定的切线或断开的切线的状态。默认情况下，解除锁定的切线会显示为绿色。锁定时，这两种切线都显示为相同的颜色。

## 自动加载曲线图编辑器(Auto Load Graph Editor)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-C20F2280-37ED-4EC4-8371-2691067872C4.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

启用或禁用在“列表”(List)菜单中找到的“自动加载选定对象”(Auto Load Selected Objects)选项。请参见[自动加载选定对象](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“列表”%28List%29菜单.md#GUID-0480EB20-E2F2-4FC9-AB8B-C73B281603C1__GUID-E071392C-94C9-4961-AD1A-F2D5C664F688)。

## 从当前选择加载曲线图编辑器(Load Graph Editor from Selection)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-FA318013-7CC8-4D41-841A-5317438891F3.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

未启用“自动加载选定对象”(Auto Load Selected Objects)时，将选定对象加载到“曲线图编辑器”(Graph Editor)中。请参见[加载选定对象](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“列表”%28List%29菜单.md#GUID-0480EB20-E2F2-4FC9-AB8B-C73B281603C1__GUID-315316CF-E51F-4A09-8C50-EB570E549B39)。

## 时间捕捉(Time Snap)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-75831B17-DD28-485F-90A3-D86C93C84ECF.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

强制在图表视图中移动的关键帧成为最接近的整数时间单位值。默认情况下会启用该选项。

## 值捕捉(Value Snap)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-FD324C64-87ED-479D-B412-1E6958D4ADC6.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

强制图表视图中的关键帧成为最接近的整数值。

**注**

捕捉设置对切线操纵没有任何影响。

## 绝对视图(Absolute View)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-0D859DA2-9243-4C40-BBA6-7F71AA7E725F.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

**注**

这些图标以前称为

归一化/取消归一化曲线(Normalize/Denormalize curves)

。

提供对曲线图编辑器”(Graph Editor)菜单栏项“视图 > 绝对视图”(View > Absolute View)的轻松启用或禁用。请参见[曲线图编辑器的视图(View)菜单](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“视图”%28View%29菜单.md)中的“绝对视图”(Absolute View)。

## 堆叠视图(Stacked View)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-DF6E9DD3-04E7-4DA7-B7D7-CCD590D2A887.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“视图 > 堆叠视图”(View > Stacked View)的轻松启用或禁用。请参见[曲线图编辑器的视图(View)菜单](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“视图”%28View%29菜单.md)中的“堆叠视图”(Stacked View)。

## 重新归一化(Renormalize)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-234B5E3B-F4BB-49FB-A8B4-222085D1C8EB.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单项“视图 > 重新归一化”(View > Renormalize)的轻松访问。请参见[重新归一化](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“视图”%28View%29菜单.md#GUID-ABB47176-9119-47F2-8466-6FA19C427F9F__GUID-230732CD-D519-463D-AFE9-A34ADFDEE830)。

## 启用/禁用堆叠的曲线的显示(Enable/Disable Stacked Curve Display)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-9C96B575-AECE-42C9-98A6-FDBD0C6CF81B.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F91F066A-9C3B-48E3-B5AD-E594AD751D95.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单项“视图 > 堆叠的曲线”(View > Stacked Curves)的轻松访问。请参见[堆叠的曲线](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“视图”%28View%29菜单.md#GUID-ABB47176-9119-47F2-8466-6FA19C427F9F__GUID-6EC326DA-F871-40BA-B8EE-6C443ECFFC59)。

## 前方循环(Cycle Before)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-942CEA24-AD1C-4DA2-B5A8-245E75052737.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“曲线 > 前方无限 > 循环”(Curves > Pre Infinity > Cycle)的轻松访问。请参见[循环](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md#GUID-619CAE9C-107D-4504-A769-227DDC847153__GUID-8B71D8A5-6836-45CA-A592-AB480C546370)。

## 带偏移的前方循环(Cycle Before with Offset)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-22C47AC3-C385-41A8-9572-C874D5B01DEB.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“曲线 > 前方无限 > 带偏移的循环”(Curves > Pre Infinity > Cycle with Offset)的轻松访问。请参见[带偏移的循环](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md#GUID-619CAE9C-107D-4504-A769-227DDC847153__GUID-DE9B8381-60E0-43B1-A277-1600E3B6B4E6)。

## 后方循环(Cycle After)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-8E40C34A-BDA1-4A85-9563-B67C3CDBBC71.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“曲线 > 后方无限 > 循环”(Curves > Post Infinity > Cycle)的轻松访问。请参见[循环](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md#GUID-619CAE9C-107D-4504-A769-227DDC847153__GUID-8B71D8A5-6836-45CA-A592-AB480C546370)。

## 带偏移的后方循环(Cycle After with Offset)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-522B4984-BC70-4A69-A84D-F6720078E8DF.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

提供对“曲线图编辑器”(Graph Editor)菜单栏项“曲线 > 后方无限 > 带偏移的循环”(Curves > Post Infinity > Cycle with Offset)的轻松访问。请参见[带偏移的循环](../“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md#GUID-619CAE9C-107D-4504-A769-227DDC847153__GUID-DE9B8381-60E0-43B1-A277-1600E3B6B4E6)。

## 未约束的拖动(Unconstrained Drag)/受约束的 X 轴拖动(Constrained X-axis drag)/受约束的 Y 轴拖动(Constrained Y-axis drag)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-1732886D-555F-401B-A85B-467F841E5607.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F676D14E-0907-4D9E-9C0C-DE333B876964.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-85B0D584-D98E-4A00-964C-7B70BFE26C96.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-402530DA-D7CD-44AA-974E-424D5A8BD233.gif) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

将光标操纵器切换到轴或无轴。

## 打开摄影表(Open the Dope Sheet)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-AB7049C4-59FF-4D5E-B1B4-AB8436DFD660.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

打开“摄影表”(Dope Sheet)并加载当前对象的动画关键帧。

## 打开 Trax 编辑器(Open the Trax Editor)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-EACA869F-C0BC-4F09-99C4-3D859DC9436E.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

打开“Trax 编辑器”(Trax Editor)并加载当前对象的动画片段。

## 打开时间编辑器(Open the Time Editor)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-1A1665A3-5CB3-4B17-AC72-DD537D403319.png) <!-- baize:img-hook downloaded=false reason="正文 5372 字 ≥300，非承重" -->

打开“时间编辑器”(Time Editor)并加载当前对象的动画关键帧。请参见“时间编辑器”。
