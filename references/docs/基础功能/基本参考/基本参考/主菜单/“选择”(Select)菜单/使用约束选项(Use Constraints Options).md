# 使用约束选项(Use Constraints Options)

选择“选择 > 使用约束”(Select > Use Constraints)时，在“多边形选择约束”(Polygon Selection Constraint)窗口中提供了以下选项。这些选项取决于场景视图中的组件选择。在设置过滤器选项之前，必须先选择要过滤的组件类型示例，才能在窗口内显示相关的选项。另请参见[选择多边形组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-98B65259-DABA-4C5E-9014-4D76B2DE28B3)。

#### 约束(Constrain)

指定条件以通过不同方式过滤选择操作。这些选项适用于所有组件模式。

#### 无(Nothing)

将不使用任何选择约束。这是默认设置。

#### 下一选择(Next Selection)

约束仅会影响使用某一技术（例如，按住 Shift 键并单击鼠标左键）的下一选择模式。

#### 当前及下一个(Current and Next)

约束将应用于当前已选定的任何模式，以及选择的任何下一个模式。

#### 全部及下一个(All and Next)

约束将自动应用于整个对象，以及选择的任何下一个模式。

## 约束“特性”(Properties)选项

以下内容描述了可以在窗口的属性部分中为选定组件设定的选项。

#### 位置(Location)

允许您选择约束项目的位置。

#### 禁用(Off)

如果已选择，则不会考虑该约束。“禁用”(Off)选项对“属性”部分中的每个选项的意义相同。

#### 在边界上(On Border)

如果启用，则该选择将仅约束当前对象周长上的项目。

#### 内部(Inside)

这是“位置”属性的默认设置。Maya 仅会选择位于当前对象内部的项目。它与“在边界上”(On Border)的效果反向。

![图：这是“位置”属性的默认设置。Maya 仅会选择位于当前对象内部的项目。它与“在边界上”(On Border)的效果反向。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-200FFE83-594B-451E-894E-16E81E31D942.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

#### 平滑(Smoothing)

如果选择边缘，则“平滑”(Smoothing)选项将可用。对于任何其他组件类型，这些“特性”(Properties)选项均不会显示。

#### 硬边/平滑(Hard/Smooth)

单击以下选项之一，将选择约束为硬边或软边。

![图：单击以下选项之一，将选择约束为硬边或软边。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-4A822431-A186-4398-89A3-D491363B44FC.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

## 约束面的“特性”(Properties)

除了所有组件模式共享的属性以外，当处于面组件模式时，Maya 还会提供许多面特定的属性。例如，如果多边形为凹（而不是凸），则可以对选项进行设定，以便按顺序、平面性、形状、映射和拓扑选择面。

#### 顺序(Order)

“顺序”选项用来设定面的形状的有效范围。如果以下选项已启用，则 Maya 会将选择约束于指定的内容。

#### 三角形(Triangles)

Maya 仅选择具有三条边的面。

![图：Maya 仅选择具有三条边的面。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-36B61E64-C574-4F57-BED5-CFE6423D4FDF.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

#### 四边形(Quads)

Maya 仅选择具有四条边的面。

![图：Maya 仅选择具有四条边的面。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-F57867AD-3FDC-468F-ACB7-3C42A68DD321.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

#### N 边形(N sided)

Maya 仅选择除三角形或四边形以外的面（即：具有四条以上边的面）。

![图：Maya 仅选择除三角形或四边形以外的面（即：具有四条以上边的面）。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-2AD3FEDB-9539-43F3-A2B0-4EB733FC4E2F.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

#### 平面性(Planarity)

选择平面或非平面面。

#### 平面/非平面(Planar/Non-planar)

“平面”(Planar)仅选择平面面。“非平面”(Non-planar)仅选择非平面面。

![图：“平面”(Planar)仅选择平面面。“非平面”(Non-planar)仅选择非平面面。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-8F5519C3-FF5D-4077-9130-0D458078B410.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

#### 凸面(Convexity)

根据边的角度选择多边形。

#### 凹/凸(Concave/Convex)

“凹”(Concave)将选择至少有一个内角大于 180 度的多边形。“凸”(Convex)将选择所有内角小于或等于 180 度的多边形。

![图：“凹”(Concave)将选择至少有一个内角大于 180 度的多边形。“凸”(Convex)将选择所有内角小于或等于 1…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-6805D057-E121-4354-9EBD-B80E54EB688A.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

#### 域(Domains)

根据面是否带洞来选择面。

#### 带洞/无洞(Holed/Non-holed)

如果选择“无洞”，则仅选择不带洞的面。如果选择“带洞”(Holed)，则仅选择已在其中创建洞（使用“网格工具 > 生成洞工具”(Mesh > Make Hole Tool)）的面。有关详细信息，请参见[“生成洞工具”(Make Hole Tool)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-FC5DBB51-A000-42B1-B99E-9F88B034A66B)。

![图：如果选择“无洞”，则仅选择不带洞的面。如果选择“带洞”(Holed)，则仅选择已在其中创建洞（使用“网格工具 生成洞工具…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-22E6D3CB-F7FF-49B8-B78A-92BF7D763565.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

**注**

Maya 将考虑带有凹洞的面。

#### 映射(Mapping)

根据您所做的选择，仅选择已映射或未映射的面。已映射面为带纹理 (UV) 坐标的面，未映射面则不带纹理 (UV) 坐标。

#### 拓扑(Topology)

从各种不同的问题面中选择。

#### 层状体

选择顶部彼此粘合的一组面。例如，其法线彼此相对的两个面。

#### 不可三角化(Non-triangulable)

支持选择不可三角化的面。使用该约束选项可以选择这些有问题的面，然后使用“多切割工具”(Multi-Cut Tool)加以修复。详细信息请参见[使用多切割工具切割面](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-12DF0D57-6E5E-48E3-8FBF-F787BA4E5410)。

## “几何体”(Geometry)选项

### “最小值”(Min)和“最大值”(Max)

大部分“几何体”(Geometry)选项的“最小值”(Min)和“最大值”(Max)均与多边形面的单位对应。设定的值会将选择约束于与这些单位对应的面的大小。默认情况下，默认单位大小以厘米为单位。可以在“首选项”(Preferences)窗口（窗口 > 设置/首选项 > 首选项(Windows > Settings/Preferences > Preferences)中更改此值，然后单击“设置”(Settings)类别）。

在该示例中，多边形基本体平面的每个面均为四个单位。通过观察每个面内栅格的方形数量，可以确定该值。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-32495059-25AF-49C8-85C8-3337FB04A6EC.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

对某些面进行缩放、而对其他面进行细分时，拓扑将会更改，您可以输入的“最小值”(Min)和“最大值”(Max)也会更改，以便约束选择区域。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-3CE33632-B2AE-425B-A0B3-D821DC73635D.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

请尝试为面的“区域”(Area)选项设定不同的“最小值”(Min)和“最大值”(Max)，可以确定哪些面将符合该单位大小确定的“最小值/最大值”(Min/Max)条件。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-EFCF12B0-8A32-453C-A090-BAD4E9A6113D.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

如果将“区域”(Area)条件的“最小值”(Min)值和“最大值”(Max)分别设定为 0 和 7，则将选择所有面，因为任何面的单位区域均不会小于 0 或大于 7。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-59DAD727-A0DA-428F-9984-46A87A6CA411.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

**注**

提示：

如果要将选择约束于十分小的单位区域（例如，多边形建模面中眼下方的区域），请将“最小值”和

“最大值”(Man)

值设定为一个较小的值。反之，如果要将约束区域设定为面涵盖更多单位空间的面的面颊，则应将其设定为一个较大的值。

### 所有“几何体”(Geometry)部分公用的选项（“激活”(Activate)和“禁用”(Off)）

每个部分均包含“激活”(Activate)开关或“禁用”(Off)选项。

- 单击“激活”(Activate)（以启用），可在做出选择时要求 Maya 确认这些选项设置。

- 单击“禁用”(Off)（以启用），可在做出选择时要求 Maya 不要确认这些选项设置。

### 面的“区域”(Area)选项

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-52FCFB07-3CD6-47A9-9460-858B3B7CE42F.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

Maya 将选择其区域位于您在“最小值”(Min)和“最大值”(Max)框中指定的范围内的面。有关使用这些值的详细信息，请参见[最小值和最大值](使用约束选项%28Use%20Constraints%20Options%29.md#WS17956D7ADBC6E736-2B54A37117AE335115-7FFF)。

### 顶点和 UV 的“相邻”(Neighbors)选项

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-42B0879C-22F4-4F22-942F-B7D189276D0F.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

Maya 将选择相连边数既不小于“最小值”(Min)、且不大于“最大值”(Max)的顶点。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-57A8F623-9E4C-4096-95B5-559DCDEF8F1F.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

### 边的“长度”(Length)选项

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-7B083EC6-3C72-4811-8036-5BFFE81CCD07.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

Maya 将选择其长度位于您在“最小值”(Min)和“最大值”(Max)框中指定的范围内的边。

**注**

提示：

在收拢边（

“编辑网格 > 合并到中心”(Edit Mesh > Merge To Center)

）以移除有时因转化 NURBS 对象而生成的附加细边之后，请使用此选择约束选项。

### 边、顶点和 UV 的“角度”(Angle)选项

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-CB08737E-4547-4604-A2FC-6DE76367E158.png) <!-- baize:img-hook downloaded=false reason="正文 5444 字 ≥300，非承重" -->

Maya 根据两个共享边的面之间的角度选择边。可能的角度范围是使用“最小值”(Min)和“最大值”(Max)来设定的。

Maya 根据共享顶点的边之间的角度选择顶点。可能的角度范围是使用“最小值”(Min)和“最大值”(Max)来设定的。

如果是 UV，则 Maya 将根据为两条边（用来接合与顶点对应的 UV）之间的角度而设定的范围来选择顶点。

**注**

该选项仅适用于非边界边。

### “已映射区域”(Mapped Area)选项

这些选项用来控制在“UV 纹理编辑器”(UV Texture Editor)窗口中展平的组件的区域范围。

#### 未签名(Unsigned)

如果启用，则 Maya 将选择其展平区域位于设定的最小值和最大值内的所有面（无论是正值还是负值）。“不带符号”要求 Maya 忽略面法线为正面的方向。

#### 已签名(Signed)

如果启用，则 Maya 将选择其法线指向同一方向、其展平区域位于设定的最小值和最大值内的所有面。

#### 最小值(Min) / 最大值(Max)

可以为位于 UV 平面内的该区域输入最小（“最小值”(Min)）和最大（“最大值”(Max)）值。展平组件的已映射区域可以是正值或负值。如果面可以从前面看到，则为正值；如果可以从背面看到，则为负值。

### “距离”(Distance)选项

这些选项可用来为组件（如面中心）和指定点之间的距离设定参考点和有效范围。

#### 点(Point)

“点”(Point)选项将确定 Maya 是否确认与指定原点（P 或“PointX”、“PointY”或“PointZ”值）之间的距离。

#### 轴(Axis)

“轴”(Axis)选项确定 Maya 是否确认与由其原点 (P) 和轴 (V) 定义的线之间的距离。

#### 平面(Plane)

“平面”(Plane)选项确定 Maya 是否确认与由其原点 (P) 和法线 (V) 定义的平面之间的距离。

#### Px,Py,Pz

这些值用来定义要从中延长选择的点的位置。

#### Vx,Vy,Vz

如果已选择“轴”(Axis)，则这些值将定义做出选择所依据的轴。如果已选择“平面”，则这些值将定义做出选择所依据的法线向量。

### 面、边和顶点的“方向”(Orientation)选项

#### 方向(Orientation)

“方向”(Orientation)选项将确定 Maya 是否使用选择的组件的方向。

#### 方向(Direction)

“方向”(Direction)选项将确定 Maya 是否使用组件或选择的方向。使用该选项，甚至还可选择两个朝向彼此相对的面。

#### Vx,Vy,Vz

这些值将定义做出选择所依据的轴。

### 面、边和顶点的“可见性”(Visibility)选项

这些选项用来设定选择的目标点和焦点角度。如果目标点可从其法线作为查看轴（“Px”、“Py”和“Pz”值）、角度作为可见场的面的中心查看，则 Maya 将选择组件。

#### 角度(Angle)

该值将确定选定组件的焦点角度。

#### Px/Py/Pz

“Px”、“Py”和“Pz”值分别确定目标点在 X 轴、Y 轴和 Z 轴中的位置。

### “随机”(Random)选项

#### 比率(Ratio)

该值确定根据在面单位内设定的比率值随机选择的组件数量。例如，0 = 无任何面，1 = 所有面或 0.5 = 50% 的面。

### “传播”(Propagation)选项

可以使用传播选项来快速预览和选择一组组件。当约束从选择中过滤组件时，传播将选择扩展到同一网格上的其他组件。传播选项支持选择前亮显，允许您预览选择。

**注**

提示：

也可以按住 Ctrl + Shift 并在场景中单击鼠标右键，，从

“选择约束”(Selection Constraints)

标记菜单中选择以下选项之一。

#### 禁用(Off)

（默认）“传播”(Propagation)处于禁用状态。

#### 壳(Shell)

启用时，将光标移至网格上将自动亮显现有壳。单击亮显的壳会将其选中。此选项可用于由一系列单独片生成的对象，类似于使用“网格 > 结合”(Mesh > Combine)创建的网格。

#### 边界(Border)

启用时，将光标移至网格上将自动亮显现有边界。单击亮显的边界会将其选中。

如果框选范围包含边界组件，则将选中选取框内的所有组件，然后还会选中选取框外的其余边界组件。

**注**

提示：

若要从框选内过滤非边界组件，请启用

“边界”(Border)

传播，然后将

“约束”(Constrain)

设置为

“全部及下一个”(All and Next)

，并将

“位置”(Location)

设置为

“在边界上”(OnBorder)

。

#### 折痕(Crease)

启用时，将光标移至网格上将自动亮显现有折痕集。单击亮显的折痕集会将其选中。

如果框选范围包含折痕集成员，则将选中选取框内的所有组件，然后还会选中选取框外的其余折痕集成员。

#### 角度(Angle)

启用时，将光标移至网格上会自动亮显指定的角度容差内的连续组件。单击亮显的区域会将其选中。

“角度”(Angle)传播启用后，进行框选会选择选取框内的所有组件并将选择扩展到选取框外处于指定角度容差内的所有组件。

**注**

选择面后，会比较每个面法线的角度，以确定其是否在指定的角度容差范围内。选择边或顶点后，选择先转化为其关联的面，然后比较每个面法线的角度。

#### 循环边(Edge Loop)

启用时，将光标移至网格上将自动亮显循环边。单击亮显的循环边会将其选中。

“循环边”(Edge Loop)传播启用后，进行框选会选择选取框内的边及所有关联的循环边。在进行框选时还可以添加和移除循环边（请参见[在选择中添加和移除组件](../../../../选择/选择/在当前选择中添加和移除对象或组件.md)）。

**注**

只有

“边”(Edge)

选择模式处于启用状态时，

“循环边”(Edge Loop)

传播才可用。

#### 环形边(Edge Ring)

启用时，将光标移至网格上将自动亮显环形边。单击亮显的环形边会将其选中。

“环形边”(Edge Ring)传播启用后，进行框选会选择选取框内的边和所有关联的环形边。在进行框选时还可以添加和移除环形边（请参见[在选择中添加和移除组件](../../../../选择/选择/在当前选择中添加和移除对象或组件.md)）。

**注**

只有

“边”(Edge)

选择模式处于启用状态时，

“环形边”(Edge Ring)

传播才可用。

### 扩大选择区域(Grow Selection Region)、收缩选择区域(Shrink Selection Region)、选择当前选择边界按钮(Select Selection Boundary buttons)

这些按钮的作用与对应的“选择”(Select)菜单项的作用相同。

- 单击“扩大选择区域”(Grow Selection Region)，可以增加初时选定的组件数量。

- 单击“收缩选择区域”(Shrink Selection Region)，可以减少已选择的组件数量。如果要除去当前选择中围绕每个面的某个面，则该按钮十分有用。

- 单击“选择当前选择边界”(Select Selection Boundary)，可以定义当前选择区域的边界。无论当前选择的内容如何（面、顶点、边或 UV），这均是一种选择边界的快速方法。
