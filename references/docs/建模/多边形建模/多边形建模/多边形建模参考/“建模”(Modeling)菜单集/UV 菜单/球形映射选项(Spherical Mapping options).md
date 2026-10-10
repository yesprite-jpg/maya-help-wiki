# 球形映射选项(Spherical Mapping options)

使用这些选项可设置在选择“UV > 球形”(UV > Spherical)时发生的情况。

## 投影操纵器

#### 在变形器之前插入投影(Insert projection before deformers)

默认情况下此选项为启用。当变形应用于多边形对象时，“在变形器之前插入投影”(Insert projection before deformers)选项与其相关。如果该选项处于禁用状态，并且为变形设置了动画，则纹理位置受顶点位置更改的影响。这将导致“游移”纹理。

启用该选项会在变形应用到多边形对象之前将纹理放置应用到该对象。基本上，在变形器依存关系图节点和纹理粘住几何体之前，甚至在变形之后，插入了纹理放置依存关系图节点。

## UV 集

#### 创建新 UV 集(Create new UV set)

启用该选项，可以创建新 UV 集并放置由投影在该集中创建的 UV。在“UV 集名称”(UV Set name)框中键入 UV 集名称。

## 手动调整投影操纵器

您可以使用操纵器控制柄以交互方式调整投影的 UV 映射，或使用“通道盒”(Channel Box)或“属性编辑器”(Attribute Editor)来输入值以更改“投影中心”(Projection Center)、“旋转”(Rotation)和“扫描”(Sweep)。这些值对应于将纹理映射到多边形上时显示的操纵器控制柄。

#### 投影中心(Projection Center)

投影中心将定义可投影纹理贴图的 X、Y 或 Z 轴中的原点。默认情况下，这是在 X、Y 或 Z 轴中选定面的中心。

#### 旋转(Rotate)

在 3D 视图中，键入一个值来围绕 X、Y 或 Z 轴旋转投影，随后旋转纹理。

#### 水平扫描(Horizontal Sweep)

使用滑块或键入一个值来沿着多边形对象水平缩放投影。该值对应操纵器上的“投影比例光圈”(Projection Scale Aperture)控制柄。例如，沿着对象拖动“投影比例光圈”(Projection Scale Aperture)控制柄，直到它们相交。这相当于在框中输入 360。

#### 垂直扫描(Vertical Sweep)

使用滑块或键入一个值来沿着多边形对象垂直缩放投影。该值对应操纵器上的“投影比例光圈”(Projection Scale Aperture)控制柄。例如，沿着对象拖动“投影比例光圈”(Projection Scale Aperture)控制柄，直到它们相交。这相当于在框中输入 360。

#### 图像中心(Image Center)

该值表示投影 UV 的中心。更改该值时，将相应平移中心。

#### 旋转角度(Rotation Angle)

该值将更改 UV 在 2D 窗口中旋转的角度。拖动滑块或输入值可旋转图像。

#### 图像比例(Image Scale)

该值表示相对于 2D 中心点的 2D 映射的宽度 (U) 或高度 (V)。

## 相关主题

- [球形 UV 映射](../../../../../UV/UV/映射%20UV/球形%20UV%20映射.md)
