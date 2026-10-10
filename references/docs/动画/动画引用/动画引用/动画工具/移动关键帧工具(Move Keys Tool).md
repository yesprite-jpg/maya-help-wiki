# 移动关键帧工具(Move Keys Tool)

在[曲线图编辑器(Graph Editor)](../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29.md)中，选择“编辑 > 变换工具 > 移动关键帧工具”(Edit > Transformation Tools > Move Keys Tool)，以使用“移动关键帧工具”(Move Keys Tool)操纵关键帧组（按比例或相对于选定关键帧）。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-4A7379A1-56AA-4919-877F-A97D4B45EC8F.gif) <!-- baize:img-hook downloaded=false reason="正文 3661 字 ≥300，非承重" -->

**注**

仅当

“曲线图编辑器”(Graph Editor)

处于活动状态时，

“移动工具”(Move Tool)

的

“移动关键帧设置”(Move Key Settings)

才可用。

**注**

提示：

若要将关键帧一次移动一帧，可按

Shift

+

9

将其向左移动，按

Shift

+

0

将其向右移动。

选择“编辑 > 变换工具 > 移动关键帧工具”(Edit > Transformation Tools > Move Keys Tool) > ![图：选择“编辑 变换工具 移动关键帧工具”(Edit Transformation Tools Move Keys Tool…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3661 字 ≥300，非承重" --> 以打开“移动关键帧设置”(Move Key Settings)。

## 移动设置(Move Settings)

#### 轴方向(Axis Orientation)

为“移动工具”(Move Tool)指定坐标系。

**注**

提示：

使用鼠标中键单击

按钮，可在最后两个选定方向模式之间切换。

#### 对象(Object)

在对象空间坐标系中移动对象。轴方向包括对象本身的旋转。如果选中了多个对象，则每个对象会相对于其自己的对象空间坐标系，移动相同的量。

#### 世界(World)

（默认）在世界空间坐标系中移动。对象将与世界空间轴对齐。

#### 组件(Component)

沿使用组件特性（如法线）计算的平均局部参考帧移动选定的组件。

选定对象后，在对象空间坐标系中移动该对象。

**注**

在

Maya

2015 和早期版本中，

“组件”(Component)

模式称为

“法线平均化”(Normals average)

模式。

#### 父对象(Parent)

将对象与父对象的旋转对齐。移动受局部空间坐标系中这些轴约束。该对象将对齐到父对象的旋转，但不包括对象本身的旋转。如果选中了多个对象，则每个对象会相对于其自己的对象空间坐标系，移动相同的量。

**注**

在 Maya 2015 和早期版本中，

“父对象”(Parent)

模式称为

“Local”(局部)

模式。

#### 法线(Normal)

在曲面的 U 向或 V 向移动选定的顶点或 CV。通常，应针对小型的 CV 集使用此选项。操纵器将指示曲面法线、U 方向和 V 方向。

![图：在曲面的 U 向或 V 向移动选定的顶点或 CV。通常，应针对小型的 CV 集使用此选项。操纵器将指示曲面法线、U 方向…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-53A2617B-6A1B-42E0-8C92-79BA95C948A4.png) <!-- baize:img-hook downloaded=false reason="正文 3661 字 ≥300，非承重" -->

选择“法线”(Normal)时，将显示“更新 [UVN] 三轴架”(Update [UVN] Triad)复选框。启用该选项后，此选项将导致操纵器方向反映移动的曲面，而不是原始曲面。这是默认设置。禁用此选项后，该操纵器将保留原始曲面的方向。

#### 沿旋转轴(Along Rotation Axis)

与对象中“旋转工具”(Rotate Tool)的轴对齐。如果已将对象“变换属性”(Transform Attributes)中的“旋转轴”(Rotate Axis)设置为不同的值（这将使对象方向相对于对象局部旋转轴的方向发生偏移），则该属性将产生效果。否则，“沿旋转轴”(Along Rotation Axis)的效果将与“对象”(Object)的效果相同。

#### 沿激活对象的轴(Along Live Object Axis)

（该设置不可与“反射”(Reflection)结合使用。）设置“移动工具”(Move Tool)来沿活动对象的轴移动对象。通常用户会激活构造平面，但实际上所有对象均可以激活。如果有一个激活的对象且已选择该选项，则“移动工具”(Move Tool)的移动箭头将对齐到激活的构造平面。（激活对象的几何体并不重要；移动始终会对齐到激活对象的轴。）

#### 自定义(Custom)

可以设置自定义方向。激活自定义枢轴编辑模式时，将自动选择“自定义”(Custom)轴方向。编辑枢轴的方向时，偏移坐标会更新。请参见[激活自定义枢轴编辑模式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6BCE41D8-07CB-4A99-99CD-1D3986896157)。

通过单击“自定义”(Custom)轴字段旁边的 ![图：可以设置自定义方向。激活自定义枢轴编辑模式时，将自动选择“自定义”(Custom)轴方向。编辑枢轴的方向时，偏移坐标会更…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-D78345F7-0FE4-45BF-AB44-307DB98C0997.png) <!-- baize:img-hook downloaded=false reason="正文 3661 字 ≥300，非承重" --> 并选择以下选项之一，可以使“移动工具”(Move Tool)的 X 轴面向场景中的组件：

**注**

提示：

使用鼠标中键单击

按钮，可激活上次选定的选项。

  设置为对象(Set to Object)：将“移动工具”(Move tool)设置为沿其他对象的轴方向移动选定的对象。

- 设定为组件(Set To Component)：将“移动工具”(Move tool)设置为沿通过选择任何组件而定义的轴移动选定的对象。

- 设置为点(Set To Point)：将“移动工具”(Move tool)设置为沿通过选择点而定义的轴移动选定的对象。

- 设置为边(Set To Edge)：将“移动工具”(Move tool)设置为沿通过选择边而定义的轴移动选定的对象。

- 设置为面(Set To Face)：将“移动工具”(Move tool)设置为沿通过选择面而定义的轴移动选定的对象。

- 重置(Reset)：将自定义轴字段重置为 0。

#### 枢轴(Pivot)

#### 编辑枢轴(Edit Pivot)

激活自定义枢轴编辑模式。请参见[激活自定义枢轴编辑模式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6BCE41D8-07CB-4A99-99CD-1D3986896157)。

#### 重置(Reset)

重置自定义枢轴的位置和方向。请参见[更改枢轴点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-150B390E-840B-4FE3-B8E9-8DEBCE7CEC97)。

#### 位置(Position)

启用时，将枢轴位置捕捉到选定组件。默认情况下，枢轴位置捕捉处于启用状态。

#### 方向(Orientation)

启用时，将枢轴方向捕捉到选定组件。默认情况下，枢轴方向捕捉处于启用状态。

#### 固定组件枢轴(Pin Component Pivot)

启用时，会将对自定义枢轴的编辑锁定在原地，允许您使用同一自定义枢轴对同一网格或其他网格上的组件进行变换。请参见[固定自定义枢轴](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4EEF6117-AA0C-4A92-942D-3E467528DEEB)。

在组件选择更改、对象选择更改期间以及切换到“对象”(Object)选择模式时，枢轴固定将保持锁定状态。

**注**

枢轴固定仅在已设置自定义枢轴时可用。请参见

更改枢轴点

。

#### 烘焙枢轴方向(Bake Pivot Orientation)

启用后，在进行任何枢轴方向更改时，系统会立即将更改保存到选定对象的变换。

#### 显示方向控制柄(Show Orientation Handle)

确定是否在枢轴编辑模式下显示旋转控制。禁用此选项可避免在仅希望移动枢轴时意外重新确定枢轴的方向。

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

（默认）禁用变换约束。允许您使用“移动工具”(Move Tool)在没有约束的情况下平移组件。

#### 边(Edge)

允许您沿活动对象的边滑动选定组件。[滑动多边形边](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A7C41EA4-3249-4A24-A0AA-788D1F7D3DBF)。

#### 表面(Surface)

允许您在活动对象的曲面上滑动选定组件。请参见[沿曲面移动多边形组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A92868C4-6460-41C4-A198-C86411D30016)。

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

（默认）启用后，“移动工具”(Move Tool)沿法线方向（而不是使用最接近曲面的点）将点捕捉到曲面。启用“沿法线”(Along Normals)可产生预期的滑动行为，并防止点弹出网格的曲面。

**注**

“沿法线”(Along Normals)

仅适用于

“变换约束”(Transform Constraint)

选项。

#### 最近点(Closest Point)

启用后，在曲面上滑动组件时，将沿最近点的方向移动组件。

**注**

“最近点”(Closest Point)

仅适用于

“变换约束”(Transform Constraint)

选项。

#### 步长捕捉(Step Snap)

允许您在移动对象的同时保持相对间距。如果平移时无需保持相对间距，请禁用此选项。选择“相对”(Relative)，然后输入一个值，以确定对象按增量移动时的移动量。

在 Maya 2015 和先前版本中，“步长捕捉”(Step Snap)称为“步长”(Step Size)，且仅当启用“离散移动”(Discrete Move)时才可用。

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

#### 调整模式(Tweak mode)

允许您快速移动组件，在场景中放置对象，并调整特定的网格。请参见[在调整模式下移动组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4E480668-4BF3-4E27-823B-41DB4C61C19A)。

**注**

如果在

“调整模式”(Tweak mode)

中将

“显示操纵器工具”(Show Manipulator tool)

的活动控制柄设置为特定轴，则激活的控制柄将保持相同的轴，即使您选择多个面。如果要使用具有中心控制柄的

“调整模式”(Tweak mode)

，则使中心控制柄变为默认控制柄。
