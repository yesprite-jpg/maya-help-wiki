# 缩放工具(Scale Tool)

若要激活“缩放工具”(Scale Tool)，请单击[工具箱(Tool Box)](../工具箱%28Tool%20Box%29.md)中的“缩放工具”(Scale Tool)图标 ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-21E8F2EA-C392-458E-8DD8-70C3BD6AF97F.png) <!-- baize:img-hook downloaded=false reason="正文 4150 字 ≥300，非承重" --> 或按 R 键。有关详细信息，请参见[缩放对象和组件](../../../变换对象/变换对象/变换对象和组件/缩放对象和组件.md)。

**注**

使用

UV 编辑器(UV Editor)

时，这将更改为

“缩放 UV 工具”(Scale UV Tool)

，其中仅包含以下用于处理 UV 的部分选项。

- 拖动操纵器的中心，或者使用鼠标中键在屏幕中的任意位置上进行拖动，以在三条轴方向上缩放。

- 拖动操纵器控制柄，或使用鼠标中键将选定的操纵器控制柄拖动到任意位置，以在单个轴方向上缩放。

- 在“组件模式”(Component Mode)中按住 Shift 键并拖动以便挤出（请参见[挤出多边形面、边或顶点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-20202ED3-5EC7-420E-860E-EC29D101A7A8)）。

- 在“对象模式”(Object Mode)中按住 Shift 键并拖动以便复制（请参见[复制](../../../创建和编辑对象/创建和编辑对象/复制%28Duplicate%29.md)）。

- 在“组件模式”(Component Mode)中同时按住 Ctrl 和 Shift 键并拖动，以便沿边滑动组件（请参见[沿边滑动组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A7C41EA4-3249-4A24-A0AA-788D1F7D3DBF)）。

双击“缩放工具”(Scale Tool)图标，可在“工具设置”(Tool Settings)面板中显示其选项，如下所述。

**注**

如果

“缩放工具”(Scale Tool)

停滞或无法正确缩放，请单击“工具”(Tool)选项中的

“重置工具”(Reset Tool)

。请参见

设置或重置工具或菜单项的选项

。

## 缩放设置(Scale Settings)

#### 轴方向(Axis Orientation)

为“缩放工具”(Scale Tool)指定坐标系。

**注**

提示：

使用鼠标中键单击

按钮，可在最后两个选定方向模式之间切换。

#### 对象(Object)

在对象空间坐标系中缩放对象。轴方向包括对象本身的旋转。如果已选择多个对象，则每个对象将缩放与其自身对象空间坐标系相关的相同数量。

但是，如果同时在所有三个轴上缩放对象，则无论当前“轴方向”(Axis Orientation)如何，“对象”(Object)空间中始终会出现变换。

**注**

您只能在

“对象”(Object)

空间中设置缩放操作的关键帧。在

“对象”(Object)

空间中也只能缩放对象，不能缩放组件（例如关节）。

#### 世界(World)

（默认）在世界空间坐标系中缩放。对象将与世界空间轴对齐。

#### 组件(Component)

沿使用组件特性（如法线）计算的平均局部参考帧缩放选定的组件。

**注**

在 Maya 2015 和早期版本中，

“组件”(Component)

模式称为

“法线平均化”(Normals average)

模式。

#### 父对象(Parent)

将对象与父对象的旋转对齐。缩放受局部空间坐标系中的轴的约束。该对象将对齐到父对象的旋转，但不包括对象本身的旋转。如果已选择多个对象，则每个对象将缩放与其自身对象空间坐标系相关的相同数量。

**注**

在 Maya 2015 和早期版本中，

“父对象”(Parent)

模式称为

“Local”(局部)

模式。

#### 法线(Normal)

在曲面的 U 方向或 V 方向缩放选定的顶点或 CV。通常，应针对小型的 CV 集使用此选项。操纵器将指示曲面法线、U 方向和 V 方向。

#### 沿旋转轴(Along rotation axis)

与对象中“旋转工具”(Rotate Tool)的轴对齐。如果已将对象“变换属性”(Transform Attributes)中的“旋转轴”(Rotate Axis)设定为不同的值（这将使对象方向相对于对象局部旋转轴的方向发生偏移），则该属性将产生效果。否则，“沿旋转轴”(Along Rotation Axis)的效果将与“对象”的效果相同。

#### 沿激活对象的轴(Along live object axis)

（该设置不可与“反射”(Reflection)结合使用。）设定“缩放工具”(Scale Tool)以沿激活对象的轴移动对象。通常用户会激活构造平面，但实际上所有对象均可以激活。如果有一个激活的对象且已选择该选项，则“移动工具”(Move Tool)的移动箭头将对齐到激活的构造平面。（激活对象的几何体并不重要；移动始终会对齐到激活对象的轴。）

#### 自定义(Custom)

可以设置自定义轴方向。激活自定义枢轴编辑模式时，将自动选择“自定义”(Custom)轴方向。编辑自定义枢轴的方向时，偏移坐标会更新。请参见[激活自定义枢轴编辑模式](../../../变换对象/变换对象/更改枢轴点/激活自定义枢轴编辑模式.md)。

通过单击“自定义”(Custom)轴字段旁边的 ![图：可以设置自定义轴方向。激活自定义枢轴编辑模式时，将自动选择“自定义”(Custom)轴方向。编辑自定义枢轴的方向时，偏移…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-D78345F7-0FE4-45BF-AB44-307DB98C0997.png) <!-- baize:img-hook downloaded=false reason="正文 4150 字 ≥300，非承重" --> 并选择以下选项之一，可以使“缩放工具”(Scale Tool)的 X 轴面向场景中的组件：

**注**

提示：

使用鼠标中键单击

按钮，可激活上次选定的选项。

- 设置为对象(Set to Object)：将“缩放工具”(Scale tool)设置为沿其他对象的轴方向缩放选定的对象。

- 设定为组件(Set To Component)：将“缩放工具”(Scale tool)设置为沿通过选择任何组件而定义的轴缩放选定的对象。

- 设置为点(Set To Point)：将“缩放工具”(Scale tool)设置为沿通过选择点而定义的轴缩放选定的对象。

- 设置为边(Set To Edge)：将“缩放工具”(Scale tool)设置为沿通过选择边而定义的轴缩放选定的对象。

- 设置为面(Set To Face)：将“缩放工具”(Scale tool)设置为沿通过选择面而定义的轴缩放选定的对象。

- 重置(Reset)：将自定义轴字段重置为 0。

#### 枢轴(Pivot)

#### 编辑枢轴(Edit Pivot)

激活自定义枢轴编辑模式。请参见[激活自定义枢轴编辑模式](../../../变换对象/变换对象/更改枢轴点/激活自定义枢轴编辑模式.md)。

#### 重置(Reset)

重置自定义枢轴的位置和方向。请参见[更改枢轴点](../../../变换对象/变换对象/更改枢轴点.md)。

#### 位置(Position)

启用时，将枢轴位置捕捉到选定组件。默认情况下，枢轴位置捕捉处于启用状态。

#### 方向(Orientation)

启用时，将枢轴方向捕捉到选定组件。默认情况下，枢轴方向捕捉处于启用状态。

#### 固定组件枢轴(Pin Component Pivot)

启用时，会将对自定义枢轴的编辑锁定在原地，允许您使用同一自定义枢轴对同一网格或其他网格上的组件进行变换。请参见[固定自定义枢轴](../../../变换对象/变换对象/更改枢轴点/固定自定义枢轴.md)。

在组件选择更改、对象选择更改期间以及切换到“对象”(Object)选择模式时，枢轴固定将保持锁定状态。

**注**

枢轴固定仅在已设置自定义枢轴时可用。请参见

更改枢轴点

。

#### 烘焙枢轴方向(Bake Pivot Orientation)

启用后，在进行任何枢轴方向更改时，系统会立即将更改保存到选定对象的变换。

#### 显示方向控制柄(Show Orientation Handle)

确定是否在枢轴编辑模式下显示旋转控制。禁用此选项可避免在仅希望移动枢轴时意外重新确定枢轴的方向。

#### 缩放中心(Scale Center)

支持围绕对象的枢轴点缩放对象组件。

#### 默认(Default)

可以围绕每个对象的单个枢轴点缩放选定对象。

**注**

在组件选择模式下，所有对象围绕选择中心的枢轴点进行缩放。

#### 对象(Object)

可以围绕每个对象的单个枢轴点缩放选定对象。

#### 操纵器(Manip)

可以通过将操纵器用作枢轴点来缩放所有选定对象。

#### 变换约束(Transform Constraint)

允许您沿活动网格的边或曲面滑动组件。

可以在[“建模工具包”(Modeling Toolkit)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D4CD168A-34F2-465B-A39C-DE20B34E5535)或任何变换工具的工具设置中启用变换约束。

**注**

提示：

使用鼠标中键单击

按钮可在上次选定的变换约束和

“禁用”(Off)

之间切换。

#### 禁用(Off)

（默认）禁用变换约束。允许您使用“缩放工具”(Scale Tool)在没有约束的情况下缩放组件。

#### 边(Edge)

允许您沿当前对象的边滑动选定组件。请参见[滑动多边形边](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A7C41EA4-3249-4A24-A0AA-788D1F7D3DBF)。

#### 表面(Surface)

允许您在选定对象的曲面上滑动选定组件。请参见[沿曲面移动多边形组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A92868C4-6460-41C4-A198-C86411D30016)。

**注**

您也可以使用

“激活”(Make Live)

将工具约束到曲面。例如，您可以使用

“激活”(Make Live)

将

“四边形绘制”(Quad Draw)

工具约束到要重新拓扑的网格的曲面。

“激活”(Make Live)

处于活动状态期间，变换约束会遭到禁用。有关重新拓扑的详细信息，请参见

使用四边形绘制重新拓扑网格

。

#### 沿法线(Along Normals)

（默认）启用后，“缩放工具”(Scale Tool)沿法线方向（而不是使用最接近曲面的点）将点捕捉到曲面。启用“沿法线”(Along Normals)可产生预期的滑动行为，并防止点弹出网格的曲面。

**注**

“沿法线”(Along Normals)

仅适用于

“变换约束”(Transform Constraint)

选项。

#### 最近点(Closest Point)

启用后，“缩放工具”(Scale Tool)使用曲面上的最近点将点捕捉到曲面。

**注**

“最近点”(Closest Point)

仅适用于

“变换约束”(Transform Constraint)

选项。

#### 步长捕捉(Step Snap)

允许您在缩放对象的同时保持相对间距。如果缩放时无需保持相对间距，请禁用此选项。选择“相对”(Relative)，然后输入一个值，以确定对象按增量缩放时的缩放量。

在 Maya 2015 和先前版本中，“步长捕捉”(Step Snap)称为“步长”(Step Size)，且仅当启用“离散比例”(Discrete Scale)时才可用。

**注**

提示：

使用鼠标中键单击

按钮，可在

“相对”(Relative)

和

“禁用”(Off)

之间切换。

#### 保持子对象(Preserve Children)

启用此选项后，移动父对象后不移动其子对象。

**注**

在 Maya 2015 和早期版本中，

“保持子对象”(Preserve Children)

称为

“保持子对象变换”(Preserve Child Transform)

。

#### 保持 UV (Preserve UVs)

选择该选项之后，移动场景视图中的组件时，会导致对应的 UV 移动到相应的 UV 空间中。最终结果是纹理不会变得扭曲。

#### 防止负比例(Prevent Negative Scale)

启用后，Maya 会禁用组件的负缩放。沿每个轴的缩放限制为正值。

**注**

“防止负比例”(Prevent Negative Scale)

不支持对象。

## 公用选择选项(Common Selection Options)

请参见[选择工具(Select Tool)](选择工具%28Select%20Tool%29.md)。

## “软选择”(Soft Selection)设置

请参见[软选择设置](选择工具%28Select%20Tool%29.md#WS17956D7ADBC6E73662C853C8117AE30BF5B-7FFA)。

## 对称设置(Symmetry Settings)

请参见[对称设置](选择工具%28Select%20Tool%29.md#WS17956D7ADBC6E73662C853C8117AE30BF5B-7FFB)。

## 智能复制设置(Smart Duplicate Settings)

请参见[智能复制设置(Smart Duplicate Settings)](移动工具%28Move%20Tool%29.md)

## 相关主题

- [变换对象](../../../变换对象/变换对象.md)

- [缩放对象和组件](../../../变换对象/变换对象/变换对象和组件/缩放对象和组件.md)

- [更改枢轴点](../../../变换对象/变换对象/更改枢轴点.md)

- [世界空间、对象空间和局部空间](../../../变换对象/变换对象/世界空间、对象空间和局部空间.md)
