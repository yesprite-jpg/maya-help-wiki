# “绘制脚本工具”(Paint Scripts Tool)选项

使用这些选项可设置在选择“修改 > 绘制脚本工具”(Modify > Paint Scripts Tool)时发生的情况。另请参见[使用 MEL 脚本和绘制脚本工具绘制](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-931047D8-6327-4274-B328-87CF115047B3)。

## 绘制属性(Paint Attributes)

下面描述了“绘制脚本工具”(Paint Scripts Tool)的“工具设置”(Tool Settings)编辑器的“绘制属性”(Paint Attributes)区域中的选项。有关其他区域（例如，“笔刷”(Brush)、“笔划”(Stroke)和“设置”(Setup)）中的设置的信息，请参见 [Artisan 工具设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B8F095-4A0E-4BAE-938C-CB41B3EBD533)。

#### 绘制操作(Paint Operation)

请注意笔刷图章会发生变化，以指示所选的操作。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-1C14A252-886D-4E37-84F6-1410EC777FF7.png) <!-- baize:img-hook downloaded=false reason="正文 4807 字 ≥300，非承重" -->

若要移除笔刷图章中的字母和渐变标记，请打开“工具设置”(Tool Settings)编辑器，单击“显示”(Display)选项卡并禁用“显示笔刷反馈”(Draw Brush Feedback)。

#### 替换(Replace)

对于 geometryPaint 和 spherePaint 脚本，使用指定的“值”(Value)和“不透明度”(Opacity)替换您绘制的值。

对于 emitterPaint 脚本，使用“值”(Value)和“不透明度”(Opacity)设置替换绘制的发射器的选定属性的值，并使用具有这些新属性的发射器替换绘制的发射器。例如，如果选定操作是“修改”(Modify)“速度”(Speed)发射器属性，则发射器速度将替换为“值”(Value)和“不透明度”(Opacity)设置。

#### 添加(Add)

对于 geometryPaint 和 spherePaint 脚本，将指定的“值”(Value)和“不透明度”(Opacity)与当前绘制的值相加。如果“绘制偏移”(Paint Offset)为负值，则值实际上将会减少。

对于 emitterPaint 脚本，将“值”(Value)和“不透明度”(Opacity)因子与绘制的发射器的选定属性的值相加。

#### 缩放(Scale)

对于 geometryPaint 和 spherePaint 脚本，使用“值”(Value)和“不透明度”(Opacity)因子缩放您绘制的当前值。

对于 emitterPaint 脚本，使用“值”(Value)和“不透明度”(Opacity)因子缩放绘制的发射器的选定属性的值。

#### 平滑(Smooth)

对于 geometryPaint 和 spherePaint 脚本，将值更改为周围顶点的平均值。

对于 emitterPaint 脚本，将绘制的发射器的选定属性的值更改为周围发射器的平均值。

#### 值(Value)

设定在执行任何脚本绘制操作时要应用的值。该值的含义因脚本而异。

对于 geometryPaint 和 spherePaint 脚本，当“控制”(Control)设定为“缩放”(Scale)时，“值”(Value)是指几何体的大小。几何体大小的原始值为 1。

对于 emitterPaint 脚本，“值”(Value)是指选定脚本操作的百分比。

#### 最小值/最大值(Min/Max Value)

设置可能的最小和最大绘制值。默认情况下，可以绘制介于 0 和 1 之间的值。设置“最小值/最大值”(Min/Max Values)可以扩展或缩小值的范围。负值用于减去权重。例如，如果将“最小值”(Min Value)设定为 -1，将“值”(Value)设定为 -0.5，然后选择“添加”(Add)进行操作，则绘制的顶点权重将减少 0.5。正值用于增加权重。

#### 钳制下限(Lower)、钳制上限(Upper)

选择是否要将值钳制在指定范围中，而不考虑绘制时设定的“值”(Value)。可以将钳制设定为“下限”(Lower)、“上限”(Upper)，或同时设定二者。

例如，如果钳制“下限”(Lower)并将下限“钳制值”(Clamp value)设置为 0.5，则绘制的值将永远不会小于 0.5，即使将“值”(Value)设置为 0.25 也一样。类似地，如果钳制“上限”(Upper)并将上限“钳制值”(Clamp value)设置为 0.75，则绘制的值将永远不会大于 0.75，即使将“值”(Value)设置为 1 也一样。

## geometryPaint 示例脚本设置

您可以使用此脚本选择场景中预定义的对象，然后在选定的曲面上进行绘制。

有关绘制脚本的详细信息，请参见 [MEL 脚本绘制概述](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-72D60883-07A4-4536-AE72-226A2AD0845E)和[脚本绘制](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0D87E625-C18D-4106-92DF-210A2D577938)。

#### 几何体(Geometry)

键入您希望绘制的对象名称，使用空格分隔。对象最初必须位于您的场景中。如果键入多个对象名称，Maya 将随机进行绘制。

#### 标识符(Identifier)

键入名称，以标识绘制的对象所属的层。通过在不同层上进行绘制，可以在不影响其他层上的对象的情况下，对某层的对象进行修改。例如，如果在此框中键入 Layer1 并绘制圆锥体，然后键入 Layer2 并绘制球体，当返回到 Layer1 进行绘制时，Layer2 中的球体将不受影响。

如果忘记了层名称或标识符，可以打开“大纲视图”(Outliner)，并选择属于该层的对象。标识符名称是对象名称的一部分。

#### 运算(Operation)

从以下操作中选择一项。

#### 创建/修改(Create/Modify)

创建新对象，并使用此窗口中和“绘制脚本”(Paint Scripts)选项卡上的设置修改绘制的对象。

#### 修改(Modify)

使用此窗口中和“脚本绘制”选项卡上的设置“修改”(Modifies)绘制的对象。

#### 删除(Remove)

“移除”(Removes)所绘制的对象。

#### 栅格(Grid)

启用“栅格”(Grid)可使用在“U 栅格大小”(U Grid Size)和“V 栅格大小”(V Grid Size)框中设定的栅格放置几何体。如果不启用“栅格”(Grid)Maya 将使用顶点位置来放置几何体。

请勿更改绘制的各个曲面的栅格大小。在绘制过程中更改栅格大小将导致意外结果。

另外，请记住，您的栅格设置部分由曲面上使用的 UV 映射技术解释。因此，请确保 UV 正确地投影到曲面上。

#### 抖动栅格(Jitter Grid)

启用“抖动栅格”(Jitter Grid)可随机放置栅格上已绘制的对象。

#### U 栅格大小(U Grid Size)、V 栅格大小(V Grid Size)

选择所需的“U 栅格大小”(U Grid Size)和“V 栅格大小”(V Grid Size)。Artisan 在您于此处指定的 U 和 V 栅格的栅格点上绘制几何体，不论您为曲面设定的等参线密度是多少。栅格大小越大，几何体密度越大。

在以下示例中，曲面的等参线密度为 10，但在“几何体绘制设置”(Geometry Paint Settings)窗口中，“U 栅格大小”(U Grid Size)和“V 栅格大小”(V Grid Size)均设定为 5。

![图：选择所需的“U 栅格大小”(U Grid Size)和“V 栅格大小”(V Grid Size)。Artisan 在您于…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-3D7910E5-881A-4EEA-900C-A94DAFB517C1.png) <!-- baize:img-hook downloaded=false reason="正文 4807 字 ≥300，非承重" -->

#### 控制(Control)

这些控制定义如何变换绘制的对象。请勿同时选择缩放和旋转控制。

#### X、Y 和 Z 缩放 (Scale)

根据在“脚本绘制”(Script Paint)选项卡的“值”(Value)框中设定的因子缩放对象值。

#### “X 旋转”(X Rot)、“Y 旋转”(Y Rot)和“Z 旋转”(Z Rot)

根据在“脚本绘制”(Script Paint)选项卡中设定的“值”(Value)旋转对象。“值”(Value)为 1 会将对象旋转 360 度。

#### X、Y 和 Z 平移(Z Trans)

根据在“脚本绘制”(Script Paint)选项卡中设定的“值”(Value)，向 X、Y 和/或 Z 轴方向沿曲面移动对象。“值”(Value)为 1 会将对象移动 1 个栅格位置。

#### 选项(Options)

选择下列选项之一。

#### 成比例(Proportional)

将所做更改在所有绘制的属性之间按比例分布，而不是将它们全部替换为新值。

#### 附加(Attach)

将对象附加到各自的位置，以便在修改曲面时，对象随曲面一起移动（例如，在雕刻或平移曲面时）。

此选项仅适用于 NURBS 曲面。

#### 复制(Duplicate)

创建原始对象的副本而非实例。

#### 分组(Group)

将绘制的对象按标识符或层进行分组。

#### 隔离(Isolate)

隔离缩放、旋转和平移变换，使其相互保持独立。如果启用“隔离”(Isolate)，可以通过选择控制，并在旋转和平移时整体应用“值”(Value) 0，或在缩放时整体应用值 1，将对象返回到基本位置。

#### 对齐(Align)

将对象与曲面法线对齐。

![图：将对象与曲面法线对齐。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-BA83A07E-7112-45F5-8F70-F14C6871D79E.png) <!-- baize:img-hook downloaded=false reason="正文 4807 字 ≥300，非承重" -->

#### 抖动值(Jitter value)

当启用“抖动栅格”(Jitter Grid)时，可输入要应用于选定控制的抖动值，其中值为 0 时无抖动，值为 1 时抖动幅度最大。

## emitterPaint 示例脚本设置

#### U 栅格大小(U Grid Size)、V 栅格大小(V Grid Size)

选择所需的“U 栅格大小”(U Grid Size)和“V 栅格大小”(V Grid Size)。Artisan 在您指定的 U 和 V 栅格的栅格点上绘制发射器，不论您为曲面设定的等参线密度是多少。栅格大小越大，发射器密度越大。

#### 栅格选项(Grid Options)

选择下列选项之一。

#### 抖动(Jitter)

随机放置绘制的发射器。

#### 抖动(Dither)

将发射器集中放置在笔刷图章的中心位置，少数发射器位于边缘。如果不启用此选项，发射器将均匀地分布在图章上。

#### 运算(Operation)

从以下操作中选择一项。

#### 创建(Create)

创建发射器。

#### 删除(Remove)

移除发射器。

#### 发射器属性(Emitter Attr)修改(Modify)

将选定属性（“速率”(Rate)、“扩散”(Spread)、“速度”(Speed)、“最小距离”(Min Dist)或“最大”(Max)“距离”(Dist）)的值更改为在“创建选项”(Creation Options)下设定的值。

#### 修改粒子属性(Modify Particle Attr.)

将选定属性（“寿命”(Lifespan)、“不透明度”(Opacity)、“点大小”(Point Size)、“线宽度”(Line Width)、“尾部褪色”(Tail Fade)、“尾部大小”(Tail Size)、“半径”(Radius)、“多点计数”(Multi Count)、“多点半径”(Multi Radius)）的值更改为在“脚本绘制”(Script Paint)选项卡的“图章轮廓”(Stamp Profile)下设定的值。

#### 修改渲染类型(Modify Render Type)

将粒子渲染类型更改为选定类型（多点、多条纹、数值、点、球体、精灵、条纹(Multi-Point, Multi-Streak, Numeric, Points, Spheres, Sprites, Streak,)或滴状(s/w)(Blobby (s/w))）。

### 创建选项(Creation Options)

类型(Type)

选择下列类型之一。

#### 泛向(Omni-directional)

将发射器类型设定为泛向点发射器。这将在各个方向发射粒子。

#### 定向(Directional)

将发射器类型设定为定向粒子发射器。

#### 速率(Rate)

设定粒子发射速率。速率是每单位时间发射的粒子数。

#### 速度(Speed)

设定发射的速度倍数。用发射粒子的速度乘以该值。

可以输入 0 或更大值。

#### 扩散(Spread)

设定发射粒子沿指定发射方向的扩散角度。粒子在该扩散角度内随机分布，呈 0 到 360 度的锥形扩散。此选项仅适用于定向发射器。

可以输入介于 0 和 1 之间的值。值为 1 代表 180 度。

#### 最小距离(Min Dist)

设定发射器开始发射的最小距离。可以输入 0 或更大值。

粒子按随机距离发射，该距离在“最小距离”(Min Distance)和“最大距离”(Max Distance)之间均匀分布。

#### 最大距离(Max Dist)

设定发射器开始发射的最大距离。可以输入 0 或更大值。

#### 粒子(Particles)

启用“每个发射器”(Per Emitter)可为每个发射器分别创建粒子形状。如果禁用此选项，则所有发射器将使用同一粒子形状。绘制“粒子属性”(Particle Attr)或“渲染类型”(Render Type)时必须启用“每个发射器”(Per Emitter)。
