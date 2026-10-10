# “NURBS 基本体”(NURBS Primitives)选项

使用这些选项可设置从“创建 > NURBS 基本体”(Create > NURBS Primitives)菜单创建的基本体（例如，球体或立方体）属性。另请参见[创建 NURBS 基本体](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-47BBC51D-CEBF-4233-B2DF-AF3E6A6AB8AA) 。

## 球体(Sphere)

创建的球体可以作为圆形类对象的起始点，例如，眼球、行星和人头。

#### 枢轴(Pivot)

默认情况下，将“枢轴”(Pivot)设置为“对象”(Object)，并从原点创建基本体。特别是当旋转枢轴和缩放枢轴位于原点时。

如果将“枢轴”(Pivot)设置为“用户定义”(User Defined)，则可以通过在“枢轴点”(Pivot Point) X、Y 和 Z 框中输入值对枢轴（和基本体）进行定位。

#### 轴(Axis)

选择“X”、“Y”或“Z”来指定对象预设轴的方向。

选择“自由”(Free)以启用 X、Y 和 Z“轴定义”(Axis Definition)。输入新值以选择轴方向。

选择“活动视图”(Active View)以创建垂直于当前正交视图的对象。如果当前建模视图是摄影机或透视视图，则“活动视图”(Active View)选项无作用。

#### 开始和结束扫描角度(Start and End Sweep Angles)

这些选项用于通过指定旋转度数来创建部分球体。度数值的范围是 0 到 360 度。以下示例显示 180 度“结束扫描角度”(End Sweep Angle)时的球体俯视图。

![图：这些选项用于通过指定旋转度数来创建部分球体。度数值的范围是 0 到 360 度。以下示例显示 180 度“结束扫描角度”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-47789823-91E7-48CF-A750-0C61C2B8C1C7.png) <!-- baize:img-hook downloaded=false reason="正文 2271 字 ≥300，非承重" -->

#### 半径(Radius)

设置基本体的宽度和深度。

#### 曲面次数(Surface Degree)

“线性”(Linear)曲面具有面状外观；“立方”(Cubic)曲面为圆形外观。有关曲面次数的详细信息，请参见[次数](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-84AD4364-96CA-48B5-BBBE-D0BF082CAB2F#WS17956D7ADBC6E73629BB7D5D117AE32BD12-7FFE)。

![图：“线性”(Linear)曲面具有面状外观；“立方”(Cubic)曲面为圆形外观。有关曲面次数的详细信息，请参见次数。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-D7AAD98B-054B-451E-9763-35768A4E0095.png) <!-- baize:img-hook downloaded=false reason="正文 2271 字 ≥300，非承重" -->

#### 使用容差(Use Tolerance)

可以使用此选项来提高基本体图形的精度。如果设置为“全局”(Global)容差，则使用“首选项”(Preferences)窗口内“设置”(Settings)部分中的“位置”(Positional)容差值（“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)）。值越低，曲面精度越高。

如果设置为“局部”(Local)，可以在选项窗口输入值来覆盖“首选项”(Preferences)窗口中的“位置”(Positional)容差值。

如果设置为“无”(None)，则将忽略容差并使用指定的分段数和跨度数创建球体（如下所示）。

#### 截面数(Number of Sections)

设置创建在球体某一方向上的曲面曲线数。曲面曲线（也称为等参线）显示曲面图形的轮廓。曲面的截面（和跨度）越多，就能越精确地显示曲面变形。

下图显示的两个球体中左边的球体有 8 个截面，而右边球体有 16 个截面。如果值小于 4，球体会较为粗糙。

![图：设置创建在球体某一方向上的曲面曲线数。曲面曲线（也称为等参线）显示曲面图形的轮廓。曲面的截面（和跨度）越多，就能越精确地…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-37099887-E4D5-49D5-8F1E-7EFF3BF0C6D8.png) <!-- baize:img-hook downloaded=false reason="正文 2271 字 ≥300，非承重" -->

后续章节介绍如何使用等参线新建曲面。

#### 跨度数(Number of Spans)

设置创建在球体横穿截面方向上的曲面曲线数。如果值小于 4，球体会较为粗糙。

![图：设置创建在球体横穿截面方向上的曲面曲线数。如果值小于 4，球体会较为粗糙。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-F97F5992-FD9E-49CF-B365-42E200B555BC.png) <!-- baize:img-hook downloaded=false reason="正文 2271 字 ≥300，非承重" -->

## 立方体(Cube)

立方体有六个面，每个面都是可选的。可以在视图中选择立方体的面，或单击“大纲视图”(Outliner)中的标题进行选择。例如，如果在“大纲视图”(Outliner)中选择 leftnurbsCube，即表示选择了立方体的一个面。若要选择整个立方体，请框选立方体并按下键盘上的向上键。

立方体的专有选项有：

#### 宽度(Width)、长度(Length)、高度(Height)

设置立方体尺度。

#### U 面片(U patch) / V 面片(V patch)

设置构成立方体的各边之间的“U 面片”(U Patch)和“V 面片”(V Patch)。此值将更改跨度数和分段数。

## 圆柱体(Cylinder)

可以创建带有或不带有结束端面的圆柱体。圆柱体的特殊选项是有关结束端面的。可以创建有一个、两个或没有结束端面的圆柱体。也可以作为单独变换节点创建端面，以便独立操纵圆柱体的端面。

## 圆锥体(Cone)

可以创建底部带有或不带有端面的圆锥体。其他选项类似于其他 NURBS 基本体选项。

## 平面(Plane)

平面是由指定数量的面片组成的平坦曲面。其选项类似于其他 NURBS 基本体选项。

## 圆环(Torus)

圆环是 3D 环。其选项类似于其他 NURBS 基本体选项。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-F60A5CAC-898C-491F-8F7B-3BEECBA7E8DF.png) <!-- baize:img-hook downloaded=false reason="正文 2271 字 ≥300，非承重" -->

## 圆形(Circle)

圆形是曲线，而不是曲面。其选项类似于球体选项。

## 方形(Square)

方形是一个由四个曲线组成的组，而不是曲面。在各种建模操作中方形很有用，例如，修剪建筑的窗图形。其选项类似于其他 NURBS 基本体选项。

## 交互式创建(Interactive Creation)

当“交互式创建”(Interactive Creation)处于启用状态并且选中基本体选项框时，会在工具窗口显示基本体选项的子集。工具设置中没有轴选项。此外，“半径/宽度/高度/深度”(Radius/Width/Height/Depth)选项仅适用于单击创建，不适用于交互式创建。

**注**

将视图设置为“高质量渲染”(High Quality Rendering)模式时，只有在完成基本体创建步骤后，使用“交互式创建”(Interactive Creation)选项创建的基本体才会显示着色效果。

可以在使用鼠标创建基本体时定位和缩放它们，而不必使用变换工具。除非手动禁用，否则此选项将一直处于启用状态。详细信息请参见[创建 NURBS 基本体](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-47BBC51D-CEBF-4233-B2DF-AF3E6A6AB8AA)。

## 完成时退出(Exit on Completion)

该选项可与“交互式创建”(Interactive Creation)交互。如果启用“完成时退出”(Exit on Completion)，则必须重新选择一个基本体类型才能创建另一个基本体。禁用该选项后，就可以交互地创建相同类型的多个基本体，直到选择另一个工具为止。
