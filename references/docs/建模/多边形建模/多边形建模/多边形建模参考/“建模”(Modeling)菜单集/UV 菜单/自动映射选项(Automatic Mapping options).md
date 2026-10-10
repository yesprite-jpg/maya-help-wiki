# 自动映射选项(Automatic Mapping options)

使用这些选项可查看在选择“UV > 自动”(UV > Automatic)时发生的情况。

## 映射设置(Mapping Settings)

#### 平面(Planes)

为“自动”(Automatic)投影选择平面数。根据 3、4、5、6、8 或 12 个平面的形状，您可以选择一个投影映射。使用的平面越多，发生的扭曲就越少且在 UV 编辑器中创建的 UV 壳越多。显示在“自动映射投影”(Automatic Mapping Projection)操纵器上的平面数与在该选项中设定的平面数直接相关。

#### 以下项的优化(Optimize for)

为自动投影设定优化类型。

#### 较少的扭曲(Less distortion)

均衡投影所有平面。该方法可以为任何面提供最佳投影，但结束时可能会创建更多的壳。如果您有对称模型并需要投影的壳是对称的，此方法尤其有用。

#### 较少的片数(Fewer pieces)

投影每个平面，直到投影遇到不理想的投影角度。这可能会导致壳增大而壳的数量减少。这是默认设置。

![图：投影每个平面，直到投影遇到不理想的投影角度。这可能会导致壳增大而壳的数量减少。这是默认设置。 注： 在某些情况下，如果将…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-57210E78-7E44-4C99-96EF-AF5BE24928DE.png) <!-- baize:img-hook downloaded=false reason="正文 2953 字 ≥300，非承重" -->

**注**

在某些情况下，如果将

“以下项的优化”(Optimize for)

设置设定为

“较少的扭曲”(Less Distortion)

，则在另一个操作系统上打开同一文件时可以产生略微不同的 UV 布局。如果出现此情况，您可以执行以下操作之一：

- 将“以下项的优化”(Optimize for)设定为“较少的片数”(Fewer pieces)。

- 保留“较少的扭曲”(Less Distortion)设置，但是删除对象上的历史（编辑 > 按类型删除 > 历史(Edit > Delete by Type > History)。该操作会将 UV 直接指定给曲面。

#### 在变形器之前插入投影(Insert projection before deformers)

当多边形对象应用了变形时，“在变形器之前插入投影”(Insert projection before deformers)选项才相关。如果该选项已禁用并且为变形设置了动画，则纹理放置会受到顶点位置更改的影响。这将导致“游移”纹理。

启用该选项会在变形应用到多边形对象之前将纹理放置应用到该对象。基本上，在变形器依存关系图节点之前插入纹理放置依存关系图节点，并且即使在变形之后纹理也会“粘住”几何体。

## 投影(Projection)

#### 加载投影(Load projection)

允许您指定一个自定义多边形对象作为用于自动映射的投影对象。您必须首先在对象空间 (X, Y, Z) 中创建该多边形对象。“加载投影”(Load Projection)对象必须存在于当前场景中。投影对象可以围绕对象形成框架，或由在对象中心彼此相交的若干分隔的面组成。投影对象的面必须具有 UV 纹理坐标。建议您使用分隔的面。可以使用“编辑网格 > 提取”(Edit Mesh > Extract)分隔多边形基本体的面。对于“加载投影”(Load Projection)，NURBS 曲面和细分曲面不是有效的曲面类型。可以为投影对象指定的多边形面的最大数量为 31。

您可以将任何面从“加载投影”(Load Projection)对象沿着其法线平移，这不会影响结果投影。但是，从“加载投影”(Load Projection)对象缩放或旋转任何面将影响最终 UV 投影的结果方向和比例。更改投影对象上的 UV 纹理坐标也会影响产生的结果 UV 投影映射。每当发生这种情况，“自动映射投影”(Automatic Mapping Projection)操纵器都会更新以反映方向的变化。

#### 投影对象(Projection object)

标识当前在场景中加载的投影对象。通过在该字段中键入投影对象的名称指定投影对象。另外，当选中场景中所需的对象并选择“加载选定项”按钮时，投影对象的名称将显示在该字段中。

#### 投影全部两个方向(Project both directions)

当“投影全部两个方向”(Project both directions)禁用时（默认），加载投影会将 UV 投影到多边形对象上，该对象的法线指向与加载投影对象的投影平面大致相同的方向。当“投影全部两个方向”(Project both directions)启用时，投影面两侧的法线对齐会确定哪些对象将从特定投影平面接收投影。即，法线从“加载投影”(Load Projection)对象两侧向外投影，并相应地对法线对齐的曲面求值。

#### 加载选定项(Load selected)

加载当前在场景中选定的多边形面作为指定的投影对象。指定的面用于更新自动投影操纵器。虽然可以为投影对象指定的最大多边形面数为 31，但建议的范围是 3 至 8。

## 排布(Layout)

#### 壳布局(Shell layout)

设定排布的 UV 壳在 UV 纹理空间中的位置。

#### 重叠(Overlap)

在 UV 编辑器中 0 到 1 范围的 UV 纹理空间内重叠结果投影。当 UV 纹理壳需要共享相同的纹理时，重叠很有用。当“加载投影”(Load Projection)选项启用时，“重叠”(Overlap)成为默认布局。

#### 沿 U 方向(Along U)

沿 U 轴定位壳。

#### 置于方形(Into Square)

在 0 到 1 范围的纹理空间内定位壳。这是默认设置。

#### 平铺(Tile)

分离结果 UV 投影，以便其位于单独的 0 到 1 的 UV 空间中。当期望对 UV 投影进行额外的编辑或操纵并需要其保持分隔时，平铺很有用。

![图：分离结果 UV 投影，以便其位于单独的 0 到 1 的 UV 空间中。当期望对 UV 投影进行额外的编辑或操纵并需要其保…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-3B3B022E-F80E-4591-A581-9F3D22489886.png) <!-- baize:img-hook downloaded=false reason="正文 2953 字 ≥300，非承重" -->

#### 缩放模式(Scale mode)

设定 UV 壳在 UV 纹理空间中的缩放方式。

#### 无(None)

不执行缩放。

#### 一致(Uniform)

缩放壳以适配 0 到 1 的纹理空间而不更改纵横比。这是默认设置。

#### 拉伸至方形(Stretch to Square)

拉伸壳以适配 0 到 1 的纹理空间。壳可能扭曲。

![图：拉伸壳以适配 0 到 1 的纹理空间。壳可能扭曲。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-79685199-EEBD-4245-89AC-053FA5F9CFBE.png) <!-- baize:img-hook downloaded=false reason="正文 2953 字 ≥300，非承重" -->

#### 壳堆叠(Shell stacking)

确定 UV 壳在 UV 编辑器中排布时相互堆叠的方式。

#### 边界框(Bounding Box)

围绕每个 UV 壳创建一个矩形边界框，然后基于边界框的边界堆叠壳。设定为该选项时，UV 壳间将有更多空间。

#### 形状(Shape)

基于每个壳的边界堆叠 UV 壳。设定该选项后，UV 壳可以更加紧密地排列以适配任何可用空间。

![图：基于每个壳的边界堆叠 UV 壳。设定该选项后，UV 壳可以更加紧密地排列以适配任何可用空间。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-78EB7AC6-438F-45CB-8189-84979011879A.png) <!-- baize:img-hook downloaded=false reason="正文 2953 字 ≥300，非承重" -->

## 壳间距(Shell Spacing)

#### 间距预设(Spacing presets)

Maya 围绕每个片段放置一个边界框并对壳进行布局以便边界框相互靠近。如果壳最终精确地彼此靠在一起，则不同壳上的两个 UV 可以共享相同的像素，并且当使用“3D 绘制工具”(3D Paint Tool)绘制时，过扫描也会引起涂料溢到相邻的壳。

![图：Maya 围绕每个片段放置一个边界框并对壳进行布局以便边界框相互靠近。如果壳最终精确地彼此靠在一起，则不同壳上的两个 U…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-C4696EB9-5A3B-4DA5-884F-A297BF61F0B7.png) <!-- baize:img-hook downloaded=false reason="正文 2953 字 ≥300，非承重" -->

若要避免该情况，请从该菜单中选择间距预设以确保边界框之间至少存在一个像素。选择一个与纹理贴图大小相对应的预设。如果不知道纹理贴图的尺寸，请选择一个较小的贴图，这将导致 UV 空间中相邻壳之间的间距较大。（以像素为单位的贴图越小，边界框之间的 UV 间距肯定越大。）

选择“自定义”(Custom)将按照贴图大小的百分比设定间距大小（在“百分比间距”(Percentage Space)框中）。

#### 百分比间距(Percentage space)

如果选择“间距预设”(Spacing Presets)旁边的“自定义”(Custom)，请按照贴图大小的百分比输入边界框之间的间距大小。

## UV 集(UV Set)

#### 创建新 UV 集(Create new UV set)

启用该选项可创建新的 UV 集，并在该集中放置新创建的 UV。在“UV 集名称”(UV set name)框中键入 UV 集的名称。

## 相关主题

- [自动 UV 映射](../../../../../UV/UV/映射%20UV/自动%20UV%20映射.md)

- [提取选项(Extract Options)](../“编辑网格”%28Edit%20Mesh%29菜单/提取选项%28Extract%20Options%29.md)
