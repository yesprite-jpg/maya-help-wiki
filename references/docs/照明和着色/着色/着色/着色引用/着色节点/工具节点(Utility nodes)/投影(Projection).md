# 投影(Projection)

使用可用投影类型之一，将任何 2D 纹理转化为可以放置在表面上的 3D 纹理。用于调整表面上的纹理放置。

在“创建”(Create)选项卡中找到该工具（请参见[“创建”(Create)选项卡](../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)）。

若要使用该工具，请参见[使用投影工具](../../../渲染节点工具/使用“投影”%28Projection%29工具.md)。

#### 交互式放置(Interactive Placement)

在场景视图中显示“投影”(Projection)操纵器。

![图：在场景视图中显示“投影”(Projection)操纵器。 提示： 使用“适应边界框”(Fit To BBox)可以使操纵…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-8E38A15E-9E0E-4773-AD69-0D409CD12293.png) <!-- baize:img-hook downloaded=false reason="正文 2380 字 ≥300，非承重" -->

**注**

提示：

使用[“适应边界框”(Fit To BBox)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-B7E73748-5F8E-4E66-BE88-DF3C2A3DF438.htm#WS73099CC142F48755-3D114B7511812357EFE-5A34)可以使操纵器聚集在对象周围。

![图：在场景视图中显示“投影”(Projection)操纵器。 提示： 使用“适应边界框”(Fit To BBox)可以使操纵…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A0EAF603-B23C-4931-931C-A63E55D98EAA.png) <!-- baize:img-hook downloaded=false reason="正文 2380 字 ≥300，非承重" -->

结合使用这些操纵器和 Maya 的变换工具，可以在三个维度上定向和定位纹理贴图。用于纹理映射的操纵器与用于纹理多边形的操纵器完全相同。详细信息请参见[多边形建模概述](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5855E588-E3C9-4543-A152-989C1BCDDFE1)（位于手册的“多边形建模”部分）。

**注**

如果不存在 place3dTexture 节点，Maya 将显示以下警报框：

![图：在场景视图中显示“投影”(Projection)操纵器。 提示： 使用“适应边界框”(Fit To BBox)可以使操纵…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-B6501751-705C-4D73-8929-6D1F162D7BAC.png) <!-- baize:img-hook downloaded=false reason="正文 2380 字 ≥300，非承重" -->

单击“创建一个放置节点”(Create a placement node)按钮可以创建 place3dTexture 节点。

#### 适应边界框(Fit To BBox)

纹理贴图与贴图对象或集的边界框重叠。另请参见[交互式放置](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-B7E73748-5F8E-4E66-BE88-DF3C2A3DF438.htm#WS73099CC142F48755-3D114B7511812357EFE-5A3E)。

### 投影类型(Proj Type)

从下拉列表中选择投影类型可以显示七个投影操纵器。

#### 禁用(Off)

不使用投影类型。

#### 平面(Planar)

默认的“投影类型”(Proj Type)。将纹理放置在平面表面上，并将其投影到对象上。

![图：默认的“投影类型”(Proj Type)。将纹理放置在平面表面上，并将其投影到对象上。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-205F2631-A931-4B82-98B0-D650AB938FE1.png) <!-- baize:img-hook downloaded=false reason="正文 2380 字 ≥300，非承重" -->

#### 球形(Spherical)

将纹理放置在球体内，并将其投影到对象上。

![图：将纹理放置在球体内，并将其投影到对象上。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-B76538F7-E66A-4017-B4AC-553C6BECE9C4.png) <!-- baize:img-hook downloaded=false reason="正文 2380 字 ≥300，非承重" -->

#### 圆柱形(Cylindrical)

将纹理放置在圆柱体内，并将其投影到对象上。

![图：将纹理放置在圆柱体内，并将其投影到对象上。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-0179022E-01CF-42C8-8660-BB3966A3B8D5.png) <!-- baize:img-hook downloaded=false reason="正文 2380 字 ≥300，非承重" -->

#### 球(Ball)

将纹理放置在球内，并将其投影到对象上。例如，Maya 投影纹理的方式就像绕棒棒糖拉动糖果包装纸一样。-z 极上有一个映射收缩点，与球形和圆柱形映射中的 +y 和 -y 极上的两个收缩点相对。

![图：将纹理放置在球内，并将其投影到对象上。例如，Maya 投影纹理的方式就像绕棒棒糖拉动糖果包装纸一样。-z 极上有一个映射…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-0DC28BCF-43C2-4560-9BF6-21D41EF04E14.png) <!-- baize:img-hook downloaded=false reason="正文 2380 字 ≥300，非承重" -->

#### 立方(Cubic)

将投影表面定义为长方体。Maya 将图像放置在每个平面上，并将它们投影到对象上。

![图：将投影表面定义为长方体。Maya 将图像放置在每个平面上，并将它们投影到对象上。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-50E47B33-5BF5-4E1D-B435-4C4B0B0EC30E.png) <!-- baize:img-hook downloaded=false reason="正文 2380 字 ≥300，非承重" -->

#### 三平面(Triplanar)

沿曲面法线的最大方向所定义的轴挤出纹理。纹理的投影方式很像绕圆弧拉动织物。

![图：沿曲面法线的最大方向所定义的轴挤出纹理。纹理的投影方式很像绕圆弧拉动织物。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-96C68ECE-E082-4734-941A-984F04AC9F8C.png) <!-- baize:img-hook downloaded=false reason="正文 2380 字 ≥300，非承重" -->

#### 同心(Concentric)

将纹理的垂直切片从体素的内边缘投影到外边缘。用于每个体素的垂直切片是随机选择的。体素是 3D 版本的矩形 — 体素栅格是一系列 3D 立方体，它们整齐排列形成较大立方体。

![图：将纹理的垂直切片从体素的内边缘投影到外边缘。用于每个体素的垂直切片是随机选择的。体素是 3D 版本的矩形 — 体素栅格是…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-9AEFA17B-46A3-4F68-B06B-1C4AD263705C.png) <!-- baize:img-hook downloaded=false reason="正文 2380 字 ≥300，非承重" -->

#### 透视(Perspective)

将 3D 元素与背景图像或活动动作序列集成。

## 示例

您的背景序列是桌子上的花瓶，您希望放大它。生成与花瓶完全匹配的参数化或实体纹理贴图可能很难，但如果使用“透视投影类型”(Perspective Proj Type)，则可以将背景序列中花瓶的真实图像投影到放置在匹配位置的 3D 花瓶上。这从摄影机的视点实现了纹理的完全匹配。

您希望将 3D 飞碟放置在街道场景的图像中。街道场景的图像应精确反射到飞碟上。使用环境纹理可以实现该目的，但这将要求您提供其他图像 — 如果使用“透视投影类型”(Perspective Proj Type)，可以将街道场景的图像投影到替代几何体上。投影到替代几何体上的图像精确反射到飞碟上。

#### 图像(Image)

用作贴图的 2D 纹理。

**注**

提示：

若要撤消映射，请在“属性编辑器”(Attribute Editor)中，当光标位于属性名称上时单击鼠标右键，然后从弹出菜单中选择“断开连接”(Break Connection)。

#### U 向角度(U angle)

仅限球形和圆柱形映射。更改“U 向角度”(U angle)。

#### V 向角度(V angle)

仅限球形映射。更改“V 向角度”(V angle)。

## 摄影机投影属性(Camera Projection Attributes)

当“投影类型”(Proj Type)为[透视](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-B7E73748-5F8E-4E66-BE88-DF3C2A3DF438.htm#WS73099CC142F48755-3D114B7511812357EFE-5A10)时，控制投影节点。

#### 链接到摄影机(Link To Camera)

下拉列表包含场景中的透视摄影机的列表。选择要从其投影图像的摄影机。

#### 适配类型(Fit Type)

当“投影类型”(Proj Type)为[透视](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-B7E73748-5F8E-4E66-BE88-DF3C2A3DF438.htm#WS73099CC142F48755-3D114B7511812357EFE-5A10)时，控制纹理如何适应摄影机。从下列选项中选择：

#### 无(None)

不会挤压或拉伸图像以适配。它的一个轴（由“适配填充”(Fit Fill)设置确定）适应胶片门，另一个轴相应调整大小。

#### 匹配摄影机胶片门(Match Camera Film Gate)

压缩图像以适应胶片门。

#### 匹配摄影机分辨率(Match Camera Resolution)

如果使用该选项来匹配背景，请将这些设置与“图像平面”(Image Plane)中的设置匹配。通常，图像平面与渲染图像的大小相同。如果是这样，请使用“匹配摄影机分辨率”(Match Camera Resolution)设置。

#### 适配填充(Fit Fill)

*仅当* “投影类型”(Proj Type) *为* “透视”(Perspective) *且* “适配类型”(Fit Type) *为* “无”(None)时可用。如果图像平面纵横比与胶片门纵横比不同，则该属性决定图像的哪个轴适应胶片门。

## 噪波属性(Noise Attributes)

控制添加到“投影”(Projection)节点的分形噪波量。（添加分形噪波会随机化或模糊纹理）。

#### 振幅 X (Amplitude X) /振幅 Y (Amplitude Y)

缩放添加到投影的 X 或 Y 方向上的分形噪波量。当“振幅 X”(Amplitude X)和“振幅 Y”(Amplitude Y)为 0 时，不添加分形噪波。

#### 比率(Ratio)

控制分形噪波的频率。增加该值可以增加细节的精细度。

#### 涟漪(Ripples)

确定投影图像投影时的波动程度，但控制添加到纹理的任何分形噪波的频率的缩放。如果在任何方向上增加，则分形细节看起来像是在该方向上进行了涂抹。

## 递归深度(Recursion Depth)

#### 深度(Depth)

控制添加“涟漪”(Ripples)时纹理执行的计算量。分形噪波（如涟漪）由数学进程创建；该进程通过的级别越多，它生成的分形越详细，但所需的时间也越长。通常，纹理会选择适合渲染体积的级别。可以使用“最小深度”(Depth Min)和“最大深度”(Depth Max)来控制计算的最小量和最大量。
