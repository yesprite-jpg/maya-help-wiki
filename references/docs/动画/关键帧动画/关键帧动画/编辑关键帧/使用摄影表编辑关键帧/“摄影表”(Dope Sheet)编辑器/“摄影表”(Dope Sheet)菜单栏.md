# “摄影表”(Dope Sheet)菜单栏

## “编辑”(Edit)菜单

许多菜单项的显示和行为方式都类似于场景视图中的主“编辑”(Edit)菜单。但是，由于“摄影表”(Dope Sheet)直接处理动画曲线和属性，因此编辑功能的设置窗口内没有可用的层次选项。

**注**

“摄影表”(Dope Sheet)、“编辑 > 关键帧”(Edit > Keys)菜单选择和时间滑块都共享一个公用关键帧剪贴板。利用一个工具复制或剪切到剪贴板的关键帧也可用于其他工具。

#### 撤消/重做(Undo/Redo)

撤消会取消上一个操作。重做会重做上次撤消的操作。

#### 剪切(Cut)

“剪切”可从选定属性中移除现有关键帧，并将该信息的副本放置在关键帧剪贴板中。如果在图表视图中选择了曲线分段，该区域将在选择“编辑 > 剪切”(Edit > Cut)后移除。如果未选择曲线分段，“剪切”将在“摄影表”(Dope Sheet)的“大纲视图”(Outliner)区域中选定的项目上操作。请参见[“关键帧”(Key)菜单](../../../../../动画引用/动画引用/“动画”%28Animation%29菜单集/“关键帧”%28Key%29菜单.md)中的“关键帧 > 剪切”(Key > Cut)。

#### 复制(Copy)

“复制”可复制选定属性中的现有关键帧，并将该信息放置在关键帧剪贴板中。如果在图表视图中选定了曲线分段，该区域将在选择“编辑 > 复制”(Edit > Copy)后移除。如果未选择曲线分段，“复制”(Copy)将在“摄影表”(Dope Sheet)的“大纲视图”(Outliner)区域中选定的项目上操作。请参见“关键帧”(Key)菜单中的[“关键帧 > 复制”(Key > Copy)](../../../../../动画引用/动画引用/“动画”%28Animation%29菜单集/“关键帧”%28Key%29菜单.md)。

#### 粘贴(Paste)

“粘贴”可将关键帧剪贴板中的关键帧添加到属性。已粘贴的关键帧可与现有关键帧合并、一次性插入（置换现有关键帧）或用来一次性替换关键帧。请参见“关键帧”(Key)菜单中的[“关键帧 > 粘贴”(Key > Paste)](../../../../../动画引用/动画引用/“动画”%28Animation%29菜单集/“关键帧”%28Key%29菜单.md)。

#### 删除(Delete)

删除操作将从选定属性中移除现有关键帧。它与“剪切”(Cut)的工作原理一样，但不会将已移除关键帧的副本放进关键帧剪贴板。请参见“关键帧”(Key)菜单中的[“关键帧 > 删除”(Key > Delete)](../../../../../动画引用/动画引用/“动画”%28Animation%29菜单集/“关键帧”%28Key%29菜单.md)。

#### 缩放(Scale)

缩放的操作对象是选定的关键帧范围，通过延长或压缩动画来对应新的时间范围。请注意，如果在摄影表大纲视图中选定了一个属性，同时未选择曲线分段，“缩放”(Scale)将作用于整个关键帧范围。请参见“关键帧”(Key)菜单中的[“关键帧 > 缩放”(Key > Scale)](../../../../../动画引用/动画引用/“动画”%28Animation%29菜单集/“关键帧”%28Key%29菜单.md)。

#### 捕捉(Snap)

使用“捕捉”(Snap)以在时间方向上强制将选定关键帧捕捉到最近的整个时间单位。使用“选择未捕捉对象”(Select Unsnapped)来检查未在整个时间单位内的关键帧。请参见“关键帧”(Key)菜单中的[“关键帧 > 捕捉”(Key > Snap)](../../../../../动画引用/动画引用/“动画”%28Animation%29菜单集/“关键帧”%28Key%29菜单.md)。

#### 选择未捕捉对象(Select Unsnapped)

从选定通道选择所有关键帧。如果未选择对象或属性，就会选择“视图区域”(View Area)中的任意关键帧。

#### 选择曲线节点(Select Curve Nodes)

请参见[选择曲线节点](../../../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单.md)。

#### 更改曲线颜色(Change Curve Color) > ![图：更改曲线颜色(Change Curve Color)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5691 字 ≥300，非承重" -->

请参见[更改曲线颜色](../../../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单.md)。

#### 移除曲线颜色(Remove Curve Color)

请参见[移除曲线颜色](../../../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单.md)。

## “视图”(View)菜单

该菜单控制“摄影表”(Dope Sheet)视图区域的布局。

**注**

当框显所需范围时，“摄影表”(Dope Sheet)可能会在图表视图内水平/垂直缩放区域，以显示所需范围。

#### 框显全部(Frame All)

“框显全部”(Frame All)会调整图表视图，以适应窗口中的所有动画。

#### 框显当前选择(Frame Selection)

调整图表视图以适应窗口中的选定动画。

#### 框显播放范围(Frame Playback Range)

“框显播放范围”(Frame Playback Range)通过调整图表视图来适应窗口中的播放范围。

#### 居中当前时间(Center Current Time)

如果要移动视图以使当前时间在编辑器内居中，请从“视图”(View)菜单选择“居中当前时间”(Center Current Time)。

#### 自动框显(Auto Frame)

这将调整图表视图，以在与选定对象关联的新曲线被加载到“摄影表”(Dope Sheet)时适应显示。

**注**

“自动框显”(Auto Frame)在“摄影表”(Dope Sheet)中的工作方式与“曲线图编辑器”(Graph Editor)中的工作方式有所不同。

#### 摄影表摘要(Dope Sheet Summary)

该选项将“摄影表摘要”(Dope Sheet Summary)加载到“摄影表”(Dope Sheet)大纲视图。有关摘要对象的详细信息，请参见[“摄影表”(Dope Sheet)大纲视图](“摄影表”%28Dope%20Sheet%29大纲视图.md)。

#### 场景摘要(Scene Summary)

该选项将“场景摘要”(Scene Summary)加载到“摄影表”(Dope Sheet)大纲视图。

## “曲线”(Curves)菜单

“曲线”(Curves)菜单项是用于处理动画曲线的功能。

#### “前方无限”(Pre Infinity)和“后方无限”(Post Infinity)动画曲线选项

在 Maya 中，动画曲线被外推到曲线的第一个和最后一个关键帧之外。第一个关键帧之前和最后一个关键帧之后的曲线是平坦的（值未随时间更改），除非将前方和后方切线控制设定为任意非恒定值。可以使用这些选项来自动生成特定类型的重复动画。有关前方无限和后方无限曲线类型的定义，请参见[曲线图编辑器“曲线”(Curves)菜单](../../../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)中的“前方无限”(Pre Infinity)和“后方无限”(Post Infinity)。

**注**

如果要创建重复或循环性质的可编辑动画，可以在启用无限后烘焙通道。

#### 烘焙通道(Bake Channel)

该操作将使用对其特性提供帮助的输入节点来计算属性的新动画曲线。请参见[曲线图编辑器“曲线”(Curves)菜单](../../../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)中的“烘焙通道选项”(Bake Channel Options)窗口。“烘焙通道”(Bake Channel)可用于：

- 编辑一条动画曲线，而不是影响单个属性行为的所有起作用属性，例如，受驱动关键帧或“表达式”(Expression)影响的对象。

- 将关键帧添加到现有曲线

#### 更改旋转插值(Change Rotation Interp)

可以更改现有曲线的旋转插值类型。

只能对在所有三个通道（rotateX、rotateY、rotateZ）都有关键帧的旋转通道更改旋转插值类型。此外，由于 rotateX、rotateY 和 rotateZ 通道始终共享相同的插值类型，更改单个通道（如 rotateX）的插值时会自动更改其他（rotateY 和 rotateZ）插值。

请参见[曲线图编辑器“曲线”(Curves)菜单](../../../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)中的“更改旋转插值”(Change Rotation Interp)。

#### 简化曲线(Simplify Curve)

使用该操作来移除无需描述动画曲线形状的关键帧。如果手动添加关键帧或执行“烘焙通道”(Bake Channel)等操作，可能会在动画曲线上累积过多的关键帧。可能需要从动画曲线移除关键帧以降低图表视图的复杂性。可能还要提供更大的跨度数以调整曲线切线。

请参见[曲线图编辑器“曲线”(Curves)菜单](../../../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)中的“简化曲线”(Simplify Curve)。

#### Euler 过滤器(Euler Filter)

请参见[曲线图编辑器“曲线”(Curves)菜单](../../../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)中的“Euler 过滤器”(Euler Filter)、[关键帧动画和曲线图编辑器](../../../关键帧动画和“曲线图编辑器”%28Graph%20Editor%29.md)中的“Euler 角过滤”(Euler angle filtering)。

#### 重新对曲线采样(Resampling curves)

可以使用“曲线图编辑器”(Graph Editor)或“摄影表”(Dope Sheet)中的“曲线 > 重新对曲线采样”(Curve > Resample Curves)选项，重新对密集数据曲线进行采样。重采样会以一致间隔放置关键帧，创建周期性帧速率。

若要对曲线重采样，请选择采样过滤器，它是一种定义如何对曲线中的关键帧重采样的算法。切线和曲线值将被忽略。过滤器将带有一致/非一致间隔关键帧的动画曲线转化为具有指定的一致间隔关键帧的曲线。请参见[曲线图编辑器“曲线”(Curves)菜单](../../../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)中的“重新对曲线采样选项”(Resample Curve Options)。

**注**

提示：

重采样过滤器旨在减少稠密数据曲线中的关键帧数。如果将其用于带有少量关键帧的曲线，可能不会产生期望的结果。

#### 属性总表(Spreadsheet)

该菜单选择用于在“属性编辑器”(Attribute Editor)属性总表中编辑选定动画曲线的属性。

#### “非加权切线”(Non-Weighted)和“加权切线”(Weighted Tangents)

指定选定关键帧的切线权重。默认设置为非加权切线，其中提供了简单的控制柄来操纵切线角度。

加权切线表示切线对动画曲线分段的影响程度。通过启用“自由切线权重”(Free Tangent Weight)，可以快速直观地同时编辑切线的影响和角度。当使用该模式时，桌面插图软件包用户将看到熟悉的 Bezier 式行为。

## “关键帧”(Keys)菜单

#### 转化为关键帧(Convert to Key)

将选定的受控关键点转化为关键帧。

#### 转化为受控关键点(Convert to Breakdown)

将选定关键帧转化为受控关键点。

#### 添加中间帧(Add Inbetween)

在当前时间插入中间帧。

#### 移除中间帧(Remove Inbetween)

移除当前时间的中间帧。

#### 禁用关键帧(Mute Key)

禁用选定关键帧。禁用的关键帧并不会有助于其通道中的动画。

禁用关键帧后，会出现以下情况：

- 一个绿色符号 ![图：一个绿色符号 将显示在“摄影表大纲视图”(Dope Sheet Outliner)中禁用的关键帧通道名称的旁边。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-DE586144-9F80-4136-A041-A77FB05C38B1.png) <!-- baize:img-hook downloaded=false reason="正文 5691 字 ≥300，非承重" --> 将显示在“摄影表大纲视图”(Dope Sheet Outliner)中禁用的关键帧通道名称的旁边。

- 带关键帧的“禁用”(Mute)通道显示在“摄影表”(Dope Sheet)中禁用的关键帧通道下。

  “禁用”(Mute)通道具有与禁用关键帧动画通道相同数量的关键帧，其关键帧定位与禁用关键帧动画通道上的定位相同。

#### 取消禁用关键帧(Unmute Key)

取消禁用选定关键帧。未被禁用的关键帧将为其通道上的动画提供帮助。取消禁用关键帧将禁用其“禁用通道”(Mute channels)（在“摄影表大纲视图”(Dope Sheet Outliner)中以禁用关键帧通道名称旁的红色 x 符号 ![图：取消禁用选定关键帧。未被禁用的关键帧将为其通道上的动画提供帮助。取消禁用关键帧将禁用其“禁用通道”(Mute chann…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-1D54B8F7-686A-4AD6-98B4-68E42852004F.png) <!-- baize:img-hook downloaded=false reason="正文 5691 字 ≥300，非承重" --> 表示），但不会将它们移除。

若要移除“禁用通道”(Mute channels)，请参见[禁用摄影表或曲线图编辑器中的关键帧](../../禁用关键帧.md)。

## “切线”(Tangents)菜单

切线用于描述关键帧中曲线分段的进出。该菜单作用于选定关键帧周围的曲线分段形状。请注意，这些设置仅影响现有动画曲线分段的切线。请参见[“曲线图编辑器”(Graph Editor)“切线”(Tangents)菜单](../../../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“切线”%28Tangents%29菜单.md)。

## “列表”(List)菜单

#### 以下层次(Hierarchy Below)

使用“以下层次”(Hierarchy Below)切换对象（作为下面对象的摘要对象）显示。

例如，在下图中，带“平移 X”(Translate X)通道的圆锥体在一个上面没有动画的组下面。启用“以下层次”(Hierarchy Below)后，group1 节点将作为摘要组，并显示其子节点（圆锥体）的动画信息。禁用“以下层次”(Hierarchy Below)后，只有摘要对象（“摄影表摘要”(Dopesheet Summary)、“场景摘要”(Scene Summary)）显示摘要信息。

![图：使用“以下层次”(Hierarchy Below)切换对象（作为下面对象的摘要对象）显示。 例如，在下图中，带“平移 X…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-3F278648-6B09-44BC-A655-EC73620A3A61.png) <!-- baize:img-hook downloaded=false reason="正文 5691 字 ≥300，非承重" -->

#### 自动加载选定对象(Auto Load Selected Objects)

当启用“列表 > 自动加载选定对象”(List > Auto Load Selected Objects)后，显示在“摄影表大纲视图”(Dope Sheet Outliner)中的对象将在每次作出选择时更改，以显示当前选定的对象。如果禁用“列表 > 自动加载选定对象”(List > Auto Load Selected Objects)，它会锁定“摄影表大纲视图”(Dope Sheet outliner)中当前显示的对象，以便继续编辑其动画曲线，即使在场景视图中做出新的选择。

#### 加载选定对象(Load Selected Objects)

只能在禁用“列表 > 自动加载选定对象”(List > Auto Load Selected Objects)后才能使用该项目。当禁用“自动加载选定对象”(Auto Load Selected Objects)后，显示在“摄影表大纲视图”(Dope Sheet outliner)中的对象可能无法与场景视图中的当前选择同步。若要加载当前选定对象，选择“列表 > 加载选定对象”(List > Load Selected Objects)。

#### 添加选定对象(Add Selected Objects)

如果要处理“摄影表”(Dope Sheet)中的某个对象的动画，或未加载到“摄影表大纲视图”(Dope Sheet outliner)中的其他对象的动画，请选择该对象，然后选择“选项 > 将选定对象添加到列表”(Options > Add Selected to List)。这会将选定对象添加到“摄影表大纲视图”(Dope Sheet outliner)，而不破坏“摄影表”(Dope Sheet)中的布局。

#### 书签(Bookmarks)

若要处理“摄影表”(Dope Sheet)中一个或一组对象的动画，并保存当前编辑环境，可以创建一个书签。

#### 为当前对象建立书签(Bookmark Current Objects)

请参见[曲线图编辑器“列表”(List)菜单](../../../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“列表”%28List%29菜单.md)中的“为当前对象建立书签”(Bookmark Current Objects)。

**注**

将书签加载到“摄影表”(Dope Sheet)时，“列表 > 自动加载选定对象”(List > Auto Load Selected Objects)将被自动禁用。

#### 为选定曲线添加书签(Bookmark Selected Curves)

请参见[曲线图编辑器“列表”(List)菜单](../../../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“列表”%28List%29菜单.md)中的“为选定曲线添加书签”(Bookmark Selected Curves)。

#### 移除所有书签(Remove All Bookmarks)

从“摄影表”(Dope Sheet)中显示的当前对象和关键帧移除所有书签。

#### “显示”(Show)菜单

该菜单与其在[“大纲视图”(Outliner)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4B9A9A3A-83C5-445A-95D5-64104BC47406)中对应的菜单相同。
