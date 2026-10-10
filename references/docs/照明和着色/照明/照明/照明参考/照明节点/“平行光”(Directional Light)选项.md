# “平行光”(Directional Light)选项

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-B2486681-5490-4000-ADCD-DF0AA661C94C.png) <!-- baize:img-hook downloaded=false reason="正文 1268 字 ≥300，非承重" -->

根据设置这些选项的编辑器，您可能会看到以下所有属性或其子集：

#### 类型(Type)

单击箭头，从下拉列表中选择一种灯光类型。当您更改灯光的类型时，只有那些为这两个类型所共有的属性会保留以前的值或设置。非共有属性的值和设置将丢失。当您更改灯光的灯光类型时，灯光的位置也将保留。

#### 颜色(Color)

设置灯光的颜色。单击样例以在“颜色选择器”(Color Chooser)中更改灯光的颜色或将纹理映射到灯光。如果映射纹理，灯光将对它进行投影（取决于灯光“类型”(Type)）。默认设置为白色。以下显示当您将渐变纹理映射到环境光的“颜色”(Color)属性时的渲染结果。

![图：设置灯光的颜色。单击样例以在“颜色选择器”(Color Chooser)中更改灯光的颜色或将纹理映射到灯光。如果映射纹理…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-57E40885-0ED3-4311-AF1A-8A067807A828.png) <!-- baize:img-hook downloaded=false reason="正文 1268 字 ≥300，非承重" -->

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

![图：默认情况下“发射漫反射”(Emit Diffuse)和“发射镜面反射”(Emit Specular)处于启用状态。禁用这…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-93C607BE-5AC1-4C4F-8465-9CB37064644B.png) <!-- baize:img-hook downloaded=false reason="正文 1268 字 ≥300，非承重" -->

若要同时对多个灯光启用或禁用漫反射和镜面反射着色，请使用“渲染标志”(Rendering Flags)窗口（“窗口 > 渲染编辑器 > 渲染标志”(Windows > Rendering Editors > Rendering Flags)）。

#### 投射阴影(Cast Shadows)

如果启用，则灯光生成深度贴图阴影（对于平行光、点光源或聚光灯）或光线跟踪阴影（对于环境光）。默认情况下，“投射阴影”(Cast Shadows)处于禁用状态。另请参见[阴影属性](阴影属性%28Shadow%20attributes%29.md)。

**注**

提示：

- 深度贴图阴影通常用于质量不重要时的快速渲染测试。

- 光线跟踪阴影生成的结果更准确，并可以处理透明度，但是速度更慢。

#### 阴影颜色(Shadow Color)

阴影颜色是由灯光产生的。使用有色阴影可以模拟由透明有色曲面（如有色玻璃）产生的阴影。默认设置为黑色。

您还可以将纹理映射到阴影以创建所需的效果。以下示例显示了已映射到聚光灯“阴影颜色”(Shadow Color)的棋盘格纹理。

![图：阴影颜色是由灯光产生的。使用有色阴影可以模拟由透明有色曲面（如有色玻璃）产生的阴影。默认设置为黑色。 您还可以将纹理映射…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-24602A44-0BBC-45DA-993B-4289D9BE9D42.png) <!-- baize:img-hook downloaded=false reason="正文 1268 字 ≥300，非承重" -->

如果决定映射有色纹理（如以下示例中的灰泥纹理），请将纹理的颜色更改为黑色和白色（若需要）。

![图：阴影颜色是由灯光产生的。使用有色阴影可以模拟由透明有色曲面（如有色玻璃）产生的阴影。默认设置为黑色。 您还可以将纹理映射…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-5A06C306-88DD-4C88-8023-544C7C4F34BD.png) <!-- baize:img-hook downloaded=false reason="正文 1268 字 ≥300，非承重" -->

#### 交互式放置(Interactive Placement)

启用此选项，以便在创建平行光时自动沿平行光观看。

请参见[交互地放置聚光灯、区域光或平行光](../../设置直接光源/创建时交互式放置聚光灯、区域光或平行光.md)。

## 相关主题

- [定位灯光](../../调整照明/定位灯光.md)

- [确定灯光的照明区域](../../设置直接光源/灯光特定曲面/确定灯光的照明区域.md)
