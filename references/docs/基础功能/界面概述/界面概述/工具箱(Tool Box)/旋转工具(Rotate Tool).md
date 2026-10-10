# 旋转工具(Rotate Tool)

若要激活“旋转工具”(Rotate Tool)，请单击[工具箱(Tool Box)](../工具箱%28Tool%20Box%29.md)中的“旋转工具”(Rotate Tool)图标 ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-11C51FA9-0F47-4A3F-BFAC-117056299916.png) <!-- baize:img-hook downloaded=false reason="正文 3641 字 ≥300，非承重" --> 或按 E 键。有关详细信息，请参见[旋转对象和组件](../../../变换对象/变换对象/变换对象和组件/旋转对象和组件.md)。

**注**

在

UV 编辑器(UV Editor)

中执行操作时，这将更改为

“旋转 UV 工具”(Rotate UV Tool)

，它仅包含以下用于处理 UV 的部分选项。

- 拖动操纵器的中心，或者使用鼠标中键在屏幕中的任意位置上进行拖动，以在三条轴方向上旋转。

- 拖动操纵器控制柄，或使用鼠标中键将选定的操纵器控制柄拖动到任意位置，以在单个轴方向上旋转。

- 在“组件模式”(Component Mode)中按住 Shift 键并拖动以便挤出（请参见[挤出多边形面、边或顶点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-20202ED3-5EC7-420E-860E-EC29D101A7A8)）。

- 在“对象模式”(Object Mode)中按住 Shift 键并拖动以便复制（请参见[复制](../../../创建和编辑对象/创建和编辑对象/复制%28Duplicate%29.md)）。

- 在“组件模式”(Component Mode)中同时按住 Ctrl 和 Shift 键并拖动，以便沿边滑动组件（请参见[沿边滑动组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A7C41EA4-3249-4A24-A0AA-788D1F7D3DBF)）。

双击“旋转工具”(Rotate Tool)图标，可在“工具设置”(Tool Settings)面板中显示其选项，如下所述。

## 旋转设置

#### 轴方向(Axis Orientation)

为“旋转工具”(Rotate Tool)指定坐标系。

**注**

提示：

使用鼠标中键单击

按钮，可在最后两个选定方向模式之间切换。

#### 对象(Object)

（默认）绕对象空间轴旋转对象。

**注**

在 Maya 2015 和更早版本中，

“对象”(Object)

模式称为

“Local”(局部)

模式。

#### 世界(World)

绕世界空间 XYZ 轴旋转对象。在此模式下，环行从不更改。

#### 组件(Component)

沿使用组件特性（如法线）计算的平均局部参考帧旋转选定的组件。

#### 万向(Gimbal)

只更改 X、Y 或 Z 旋转值。在局部和世界模式下，XYZ 约束环可能会更改多个旋转 XYZ 通道。

#### 自定义(Custom)

可以设置自定义轴方向。激活自定义枢轴编辑模式时，将自动选择“自定义”(Custom)轴方向。编辑自定义枢轴的方向时，偏移坐标会更新。请参见[激活自定义枢轴编辑模式](../../../变换对象/变换对象/更改枢轴点/激活自定义枢轴编辑模式.md)。

通过单击“自定义”(Custom)轴字段旁边的 ![图：可以设置自定义轴方向。激活自定义枢轴编辑模式时，将自动选择“自定义”(Custom)轴方向。编辑自定义枢轴的方向时，偏移…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-D78345F7-0FE4-45BF-AB44-307DB98C0997.png) <!-- baize:img-hook downloaded=false reason="正文 3641 字 ≥300，非承重" --> 并选择以下选项之一，可以使“旋转工具”(Rotate Tool)的 X 轴面向场景中的组件：

**注**

提示：

使用鼠标中键单击

按钮，可激活上次选定的选项。

  设置为对象(Set to Object)：将“旋转工具”(Rotate tool)设置为沿其他对象的轴方向旋转选定的对象。

- 设定为组件(Set To Component)：将“旋转工具”(Rotate tool)设置为沿通过选择任何组件而定义的轴旋转选定的对象。

- 设置为点(Set To Point)：将“旋转工具”(Rotate tool)设置为沿通过选择点而定义的轴旋转选定的对象。

- 设置为边(Set To Edge)：将“旋转工具”(Rotate tool)设置为沿通过选择边而定义的轴旋转选定的对象。

- 设置为面(Set To Face)：将“旋转工具”(Rotate tool)设置为沿通过选择面而定义的轴旋转选定的对象。

- 重置(Reset)：将自定义轴字段重置为 0。

#### 枢轴(Pivot)

#### 编辑枢轴(Edit Pivot)

激活枢轴编辑模式。请参见[激活自定义枢轴编辑模式](../../../变换对象/变换对象/更改枢轴点/激活自定义枢轴编辑模式.md)。

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

仅在已启用自定义枢轴编辑模式时，枢轴固定才起作用。请参见

更改枢轴点

。

#### 烘焙枢轴方向(Bake Pivot Orientation)

启用后，在进行任何枢轴方向更改时，系统会立即将更改保存到选定对象的变换。

#### 显示方向控制柄(Show Orientation Handle)

确定是否在枢轴编辑模式下显示旋转控制。禁用此选项可避免在仅希望移动枢轴时意外重新确定枢轴的方向。

#### 旋转中心(Rotate Center)

用于围绕对象的枢轴旋转对象组件。

#### 默认(Default)

用于围绕每个对象的单个枢轴点旋转选定的对象。

**注**

在组件选择模式下，所有对象将围绕选择中心的枢轴点进行旋转。

#### 对象(Object)

用于围绕每个对象的单个枢轴点旋转选定的对象。

#### 操纵器(Manip)

用于将操纵器用作枢轴点来旋转所有选定的对象。

#### 选择(Selection)

允许您围绕选择的公共中心点旋转一组选定的对象。

#### 修改平移(Modify Translation)

启用时，围绕公共中心点旋转对象会影响对象的平移值，而不是其旋转枢轴值。

“修改平移”(Modify Translation)与“旋转中心: 选择”(Rotate Center: Selection)设置一起使用。在围绕公共中心点旋转一组对象时，只要重新定位某对象，就会更新该对象的平移值。

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

（默认）禁用变换约束。允许您使用“旋转工具”(Rotate Tool)在没有约束的情况下旋转组件。

#### 边(Edge)

允许您沿当前对象的边滑动选定组件。请参见[滑动多边形边](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A92868C4-6460-41C4-A198-C86411D30016)。

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

（默认）启用后，“旋转工具”(Rotate Tool)沿法线方向（而不是使用最接近曲面的点）将点捕捉到曲面。启用“沿法线”(Along Normals)可产生预期的滑动行为，并防止点弹出网格的曲面。

**注**

“沿法线”(Along Normals)

仅适用于

“变换约束”(Transform Constraint)

选项。

#### 最近点(Closest Point)

启用后，“旋转工具”(Rotate Tool)使用曲面上的最近点将点捕捉到曲面。

**注**

“最近点”(Closest Point)

仅适用于

“变换约束”(Transform Constraint)

选项。

#### 步长捕捉(Step Snap)

允许您在旋转对象的同时保持相对间距。如果旋转时无需保持相对间距，请禁用此选项。选择“相对”(Relative)，然后输入一个值，以确定对象按增量旋转时的旋转量。

在 Maya 2015 和先前版本中，“步长捕捉”(Step Snap)称为“步长”(Step Size)，且仅当启用“离散旋转”(Discrete Rotate)时才可用。

**注**

提示：

使用鼠标中键单击

按钮，可在

“相对”(Relative)

和

“禁用”(Off)

之间切换。

#### 保持子对象(Preserve Children)

选择该选项之后，移动父对象时，不会移动其子对象。

**注**

在 Maya 2015 和早期版本中，

“保持子对象”(Preserve Children)

称为

“保持子对象变换”(Preserve Child Transform)

。

#### 保持 UV (Preserve UVs)

选择该选项之后，移动场景视图中的组件时，会导致对应的 UV 移动到相应的 UV 空间中。最终结果是纹理不会变得扭曲。

#### 自由旋转(Free Rotate)

如果启用此选项，在“旋转”(Rotate)操纵器控制柄内部拖动区域可自由地旋转对象或组件。如果禁用此选项，则只能通过拖动操纵器控制柄来旋转对象或组件。禁用此选项后，还可以通过在“旋转”(Rotate)操纵器的中心区域中单击来选择对象或组件，这在进行组件选择时会很有用。

**注**

在 Maya 2015 和早期版本中，

“自由旋转”(Free Rotate)

称为

“置于虚拟轨迹球中心”(Center as Virtual Trackball)

。

## 公用选择选项(Common Selection Options)

请参见[选择工具(Select Tool)](选择工具%28Select%20Tool%29.md)。

## 软选择(Soft Selection)

请参见[软选择设置](选择工具%28Select%20Tool%29.md#WS17956D7ADBC6E73662C853C8117AE30BF5B-7FFA)。

## 对称设置(Symmetry Settings)

请参见[对称设置](选择工具%28Select%20Tool%29.md#WS17956D7ADBC6E73662C853C8117AE30BF5B-7FFB)

## 智能复制设置(Smart Duplicate Settings)

请参见[智能复制设置(Smart Duplicate Settings)](移动工具%28Move%20Tool%29.md)

## 相关主题

- [变换对象](../../../变换对象/变换对象.md)

- [更改枢轴点](../../../变换对象/变换对象/更改枢轴点.md)

- [世界空间、对象空间和局部空间](../../../变换对象/变换对象/世界空间、对象空间和局部空间.md)

- [旋转对象和组件](../../../变换对象/变换对象/变换对象和组件/旋转对象和组件.md)
