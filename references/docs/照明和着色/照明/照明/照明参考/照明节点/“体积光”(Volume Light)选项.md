# “体积光”(Volume Light)选项

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-8EB364D3-FA00-4410-ACA5-E2EF3DC1741A.png) <!-- baize:img-hook downloaded=false reason="正文 3170 字 ≥300，非承重" -->

根据设置这些选项的编辑器，您可能会看到以下所有属性或其子集：

#### 类型(Type)

单击箭头，从下拉列表中选择一种灯光类型。当您更改灯光的类型时，只有那些为这两个类型所共有的属性会保留以前的值或设置。非共有属性的值和设置将丢失。当您更改灯光的灯光类型时，灯光的位置也将保留。

#### 颜色(Color)

设置灯光的颜色。单击样例以在“颜色选择器”(Color Chooser)中更改灯光的颜色或将纹理映射到灯光。如果映射纹理，灯光将对它进行投影（取决于灯光“类型”(Type)）。默认设置为白色。以下显示当您将渐变纹理映射到环境光的“颜色”(Color)属性时的渲染结果。

![图：设置灯光的颜色。单击样例以在“颜色选择器”(Color Chooser)中更改灯光的颜色或将纹理映射到灯光。如果映射纹理…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-57E40885-0ED3-4311-AF1A-8A067807A828.png) <!-- baize:img-hook downloaded=false reason="正文 3170 字 ≥300，非承重" -->

#### 强度(Intensity)

表示灯光的亮度。“强度”(Intensity)值为 0 的灯光不发光。“强度”(Intensity)值为负值的灯光从受灯光影响的区域中的场景移除灯光。该滑块范围是 0 到 10，但您可以键入更大值以获得更亮的灯光（例如，20）。默认值是 1。

**注**

提示：

使用负

“强度”(Intensity)

值减少或移除强光点或眩光。

#### 默认照明(Illuminates by Default)

如果启用该选项，灯光将照亮所有对象并包含在 defaultLightSet 中。如果禁用该选项，灯光仅照亮其链接到的对象。默认情况下“默认照明”(Illuminates by Default)处于启用状态。

#### “发射漫反射”(Emit Diffuse)和“发射镜面反射”(Emit Specular)

默认情况下“发射漫反射”(Emit Diffuse)和“发射镜面反射”(Emit Specular)处于启用状态。禁用这两个选项将对灯光禁用漫反射和镜面反射着色结果。

**注**

结果不会显示在场景视图中。若要查看结果，请在“渲染视图”(Render View)中测试渲染。

![图：默认情况下“发射漫反射”(Emit Diffuse)和“发射镜面反射”(Emit Specular)处于启用状态。禁用这…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-93C607BE-5AC1-4C4F-8465-9CB37064644B.png) <!-- baize:img-hook downloaded=false reason="正文 3170 字 ≥300，非承重" -->

若要同时对多个灯光启用或禁用漫反射和镜面反射着色，请使用“渲染标志”(Rendering Flags)窗口（“窗口 > 渲染编辑器 > 渲染标志”(Windows > Rendering Editors > Rendering Flags)）。

#### 灯光形状(Light shape)

这将决定灯光的体积形状。从下拉列表中选择灯光形状：“长方体”(Box)、“球体”(Sphere)、“圆柱体”(Cylinder)或“圆锥体”(Cone)。默认为“球体”(Sphere)。

![图：这将决定灯光的体积形状。从下拉列表中选择灯光形状：“长方体”(Box)、“球体”(Sphere)、“圆柱体”(Cylin…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-7D5F19D3-52CA-435B-81F7-FDAC1869BBF3.png) <!-- baize:img-hook downloaded=false reason="正文 3170 字 ≥300，非承重" -->

#### 投射阴影(Cast Shadows)

如果启用，则灯光生成深度贴图阴影（对于平行光、点光源或聚光灯）或光线跟踪阴影（对于环境光）。默认情况下，“投射阴影”(Cast Shadows)处于禁用状态。另请参见[阴影属性](阴影属性%28Shadow%20attributes%29.md)。

**注**

提示：

- 深度贴图阴影通常用于质量不重要时的快速渲染测试。

- 光线跟踪阴影生成的结果更准确，并可以处理透明度，但是速度更慢。

#### 阴影颜色(Shadow Color)

阴影颜色是由灯光产生的。使用有色阴影可以模拟由透明有色曲面（如有色玻璃）产生的阴影。默认设置为黑色。

您还可以将纹理映射到阴影以创建所需的效果。以下示例显示了已映射到聚光灯“阴影颜色”(Shadow Color)的棋盘格纹理。

![图：阴影颜色是由灯光产生的。使用有色阴影可以模拟由透明有色曲面（如有色玻璃）产生的阴影。默认设置为黑色。 您还可以将纹理映射…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-24602A44-0BBC-45DA-993B-4289D9BE9D42.png) <!-- baize:img-hook downloaded=false reason="正文 3170 字 ≥300，非承重" -->

如果决定映射有色纹理（如以下示例中的灰泥纹理），请将纹理的颜色更改为黑色和白色（若需要）。

![图：阴影颜色是由灯光产生的。使用有色阴影可以模拟由透明有色曲面（如有色玻璃）产生的阴影。默认设置为黑色。 您还可以将纹理映射…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-5A06C306-88DD-4C88-8023-544C7C4F34BD.png) <!-- baize:img-hook downloaded=false reason="正文 3170 字 ≥300，非承重" -->

## 颜色范围(Color Range)

#### colorRange

colorRange 是从体积中心到边缘的灯光颜色。通过更改渐变（渐变）上的值，可以沿已定义灯光方向衰退或更改颜色。渐变右侧表示在体积中心的灯光颜色。左侧是在外边界的颜色。通过从内部颜色插值（融合）到外部颜色来获得衰退效果。最外部的颜色应为黑色，以避免体积边的硬边界。

有关如何通过添加附加的颜色条目来自定义渐变的详细信息，请参见[使用渐变设定属性](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B#GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B__SECTION_D18F4FBF38B94659837688094068CAF0)。

**注**

提示：

存在高级渐变功能。有关详细信息，请参见[渐变着色器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-022F69B8-B1A3-46A3-9917-0D9CBDBB6733.htm)。

#### 选定位置(Selected Position)

指活动颜色条目在渐变中的位置。

#### 选定颜色(Selected Color)

指活动颜色条目的颜色。

#### 插值(Interpolation)

指控制颜色在渐变中的融合方式。从下拉列表中选择一个选项：“无”(None)、“线性”(Linear)、“平滑”(Smooth)、“样条线”(Spline)。默认为“线性”(Linear)。

- 无(None)：表示无插值；不同的颜色在最终纹理中显示为不同的条带。

- 线性(Linear)：值在 rgb 颜色空间中对值进行线性插值。

- 平滑(Smooth)：沿着钟形曲线对值进行插值，渐变中的每种颜色将填充其周围的区域，然后快速融合至下一种颜色。

- 样条线(Spline)：它将考虑相邻折射率，以实现更平滑的效果。

#### 体积光方向(Volume Light Dir)

体积内的灯光的方向。从下拉列表中选择一个选项：“向外”(Outward)、“向内”(Inward)、“向下轴”(Down Axis)。默认为“向外”(Outward)。

- 向外(Outward)：灯光从长方体或球体中心移开，并从圆锥体或圆柱体的中心轴移开。它的行为类似于点光源。

- 向内(Inward)：灯光方向向灯光的中心移动。这是一个不模拟区域光，而是对用于灯光计算的方向进行简单更改的特殊效果。

- 向下轴(Down Axis)：灯光方向是灯光中心轴的下方向。它的行为类似于平行光。

  **注**

  除

  “向外”(Outward)

  之外方向的阴影将无法正常工作。它始终显示阴影，就如同来自点光源。

  发射镜面反射对于内向灯光没有任何影响。

#### 弧(Arc)

通过指定旋转度数，使用该选项来创建部分球体、圆锥体、圆柱体灯光形状。值范围从 0 到 360 度。最常用的设置是默认值 180 和 360。180 类似于将灯光体积切成一半，同时 360 是完整的灯光。该选项不适用于长方体灯光形状。

#### 圆锥体结束半径(Cone End Radius)

该选项仅适用于圆锥体灯光形状。这是圆锥体一个末端的相对大小。值为 1.0 时是一个圆柱体，而在值为 0 时则是一个圆锥体。

#### 发射环境光(Emit Ambient)

启用后，灯光将以多向方式影响曲面。默认设置为“禁用”。

**注**

“发射环境光”(Emit Ambient)

会消除阴影并且看起来平坦。

当同时使用“发射漫反射”(Emit Diffuse)时，曲面照明为曲面/灯光角度的 50%，以及非平行方式的 50%。如果“发射漫反射”(Emit Diffuse)处于禁用状态，则灯光完全是泛向的。

如果“发射漫反射”(Emit Diffuse)和“发射镜面反射”(Emit Specular)处于禁用状态，同时“发射环境光”(Emit Ambient)处于启用状态，则灯光的行为类似于具有衰退和边界范围的环境光。这对于调整照明非常有用。它可与负灯光强度一起使用，以将灯光拉出已定义的区域。

## 半影(Penumbra)

该区域仅适用于圆锥体和圆柱体灯光形状。这包含属性来管理半影，这是阴影边界和灯光周围部分照明的区域。使用图形，可以调整灯光的扩散和掉落。图形左侧表示圆锥体或圆柱体外边的强度，同时右侧表示从光束中心到边缘的强度。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-74A29C8A-C822-4FBE-AF3D-FB8D673DE851.png) <!-- baize:img-hook downloaded=false reason="正文 3170 字 ≥300，非承重" -->

**注**

提示：

存在高级渐变功能。有关详细信息，请参见

渐变着色器

。

#### 选定位置(Selected Position)

该值会影响图形中的活动条目，同时在图形的 x 轴上显示。

#### 选定值(Selected Value)

该值会影响图形中的活动条目，同时在图形的 y 轴上显示。

![图：该值会影响图形中的活动条目，同时在图形的 y 轴上显示。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-54B9609A-F9BF-4B5E-AED9-CF83B860EDE6.png) <!-- baize:img-hook downloaded=false reason="正文 3170 字 ≥300，非承重" -->

#### 插值(Interpolation)

这将控制计算值的方式。从下拉列表中选择一个选项：“无”(None)、“线性”(Linear)、“平滑，样条线”(Smooth, Spline)。默认为“线性”(Linear)。

- 无(None)：表示无插值；不同的值在最终结果中显示为不同的条带。

- 线性(Linear)：对值进行线性插值。

- 平滑(Smooth)：沿着钟形曲线对值进行插值，渐变中的每个值将填充其周围的区域，然后快速融合至下一个值。

- 样条线(Spline)：它将考虑相邻折射率，以实现更平滑的效果。

  ![图：样条线(Spline)：它将考虑相邻折射率，以实现更平滑的效果。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-195DC6CF-D748-4ED7-A5E2-87D4A1F3F9E0.png) <!-- baize:img-hook downloaded=false reason="正文 3170 字 ≥300，非承重" -->

## 相关主题

- [定位灯光](../../调整照明/定位灯光.md)

- [确定灯光的照明区域](../../设置直接光源/灯光特定曲面/确定灯光的照明区域.md)
