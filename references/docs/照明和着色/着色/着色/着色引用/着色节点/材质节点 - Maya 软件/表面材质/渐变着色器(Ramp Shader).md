# 渐变着色器(Ramp Shader)

您可以在“Hypershade” [创建(Create)](../../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)选项卡中的“表面”(Surface)类别下找到此材质。

“渐变着色器”(Ramp Shader)是一种可用来附加控制颜色随灯光和观察角度变化方式的材质（着色器）。您可模拟各种新奇材质，并以精细的方式调整传统的着色。

“渐变着色器”(Ramp Shader)中的所有颜色相关的属性均由渐变（百分度）控制。使用图表，可以制作更易于实现的特定外观（如卡通着色），避免复杂的着色网络。

可以设定“渐变着色器”(Ramp Shader)的多个属性，以此控制对象的外观。

渐变中的每个颜色条目在该渐变的上方都有一个圆形彩色控制柄，在其下方有一个方形颜色图标。活动颜色的颜色控制柄和图标周围有一个白色边界。

有关如何通过添加额外的颜色项目自定义渐变的详细信息，请参见[使用渐变设置属性](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B#GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B__SECTION_D18F4FBF38B94659837688094068CAF0)。

**注**

提示：

若要制作一个曲面远离灯光、边中避免出现线性瑕疵的着色器，请尝试以下设置：

“漫反射”(Diffuse) = 0

“半透明”(Translucence) = 1

“颜色”(Color)：两个项目，其中后颜色为 0.5，曲面颜色为 1.0

选择“插值 > 线性”(Interpolation > Linear)时，此设置与法线朗伯 (lambertian) 衰减具有相同的效果。选择“插值 > 平滑”(Interpolation > Smooth)时，此设置将使线性着色瑕疵消失。

## 将纹理应用于渐变

除了颜色条目以外，还可以将纹理条目添加到渐变中。可以将纹理映射到渐变的位置或颜色。

### 将渐变索引的颜色映射到纹理

单击渐变上方的控制柄，再单击“属性编辑器”(Attribute Editor)（或“渐变编辑器”(Ramp Editor)）中“选定颜色”(Selected Color)属性旁边的 ![图：单击渐变上方的控制柄，再单击“属性编辑器”(Attribute Editor)（或“渐变编辑器”(Ramp Editor…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-C1778F8F-4979-4511-A5E6-43C0002BE751.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->。可以将纹理映射“渐变编辑器”(Ramp Editor)和“属性编辑器”(Attribute Editor)内的渐变中。但是，只能在材质采样样例和着色器图标（位于 Hypershade 内）中、而不能在“渐变编辑器”(Ramp Editor)中查看纹理的效果。

请看下面的示例。渐变中已输入三个条目：第一个是颜色条目，第二个是棋盘纹理，第三个是山脉纹理。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-F15742B8-7C2F-4189-921C-1A9645B1413A.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->

渲染结果显示了曲面颜色从黄色过渡（渲染）到棋盘格纹理、再到山脉纹理的情景。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-554B3071-926A-44F9-AF9F-36E6B0E99B44.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->

### 将渐变索引的位置映射到纹理

可以将渐变索引的位置映射到纹理，达到生动有趣的效果。使用此技术，可以在渐变的颜色边界范围内创建各种变化。例如，可以使用噪波纹理将两种颜色之间的边界形成一种模糊的相似噪波图案。或者，也可以尝试使用这些设置来创建复杂的效果，如模拟自然的水颜色，或者使某些区域中的百分度变得更模糊，而另一些则变得更明晰。

单击渐变上方的控制柄以选择它。右键单击“属性编辑器”(Attribute Editor)（或“渐变编辑器”(Ramp Editor)）中的“选定位置”(Selected Position)属性，然后选择“创建新纹理”(Create New Texture)以映射纹理。

将纹理映射到控制柄的位置之后，该位置字段将变为锁定（文本框将显示为黄色）。现在，该位置已完全由选择的纹理定义。

若要改变控制柄的位置，请在“属性编辑器”(Attribute Editor)中展开该纹理的“颜色平衡”(Color Balance)区域。增加或减少“Alpha 偏移”(Alpha Offset)值。

若要改变纹理效果，请增加或减少“Alpha 增益”(Alpha Gain)值。

若要获得更有趣的效果，还可以在“属性编辑器”(Attribute Editor)中改变渐变的“插值”方法。有关详细信息，请参见[插值](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B#GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B__SECTION_A26BB5B0120C4D1797A3AA77DBA8E0B9)。

可以将纹理映射到“渐变编辑器”(Ramp Editor)和“属性编辑器”(Attribute Editor)内的渐变中。但是，只能在材质采样样例和着色器图标（位于 Hypershade 内）中、而不能在“渐变编辑器”(Ramp Editor)中查看纹理的效果。

请看下面的示例。渐变中已输入两个颜色条目，其中第一个颜色条目的位置已映射到分形纹理中。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-2B82F640-E15E-46CB-AC0C-5EDE1E6B50AD.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-CC380A27-20E0-416E-9D9C-4CB6BAC0507D.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-425C3B83-70B5-4EE1-80F8-9987D1F8FA0F.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-AC6422D9-CE4C-4378-A196-B0897FE79032.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->

## 颜色(Color)

指曲面的基本颜色。

#### 选定位置(Selected Position)

指活动颜色条目在渐变中的位置。

#### 选定颜色(Selected Color)

指活动颜色条目的颜色。

#### 插值(Interpolation)

有关详细信息，请参见[插值](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B#GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B__SECTION_A26BB5B0120C4D1797A3AA77DBA8E0B9)。

#### 颜色输入(Color Input)

它将确定颜色如何扩散到曲面上。请从下拉列表中选择一个选项：“灯光角度”(Light Angle)、“正面角度”(Facing Angle)、“亮度”(Brightness)、“归一化亮度”(Normalized Brightness)。默认值为“灯光角度”(Light Angle)。

#### 灯光角度(Light Angle)

渐变的位置由灯光角度和曲面法线确定。渐变右侧是法线直接指向灯光的颜色。渐变中心是指曲面法线与灯光垂直的点。左侧是法线直接远离灯光的颜色。除非着色器半透明，否则渐变中心左侧的颜色值是不可见的。该选项将考虑场景中的所有灯光。

![图：渐变的位置由灯光角度和曲面法线确定。渐变右侧是法线直接指向灯光的颜色。渐变中心是指曲面法线与灯光垂直的点。左侧是法线直接…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-9D969C99-6F06-4523-87B0-C4174304F3ED.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->

#### 正面角度(Facing Angle)

渐变的位置由曲面角度和视图方向确定。渐变右侧是曲面法线朝向摄影机的颜色。左侧是曲面法线垂直于摄影机的颜色。

![图：渐变的位置由曲面角度和视图方向确定。渐变右侧是曲面法线朝向摄影机的颜色。左侧是曲面法线垂直于摄影机的颜色。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-AF9807EA-BE94-4418-830C-47F0C60BE9C2.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->

#### 亮度(Brightness)

灯光总亮度可用来设置渐变的索引。通过使用渐变和阶跃值，该选项可用来创建卡通样式着色。渐变右侧是漫反射亮度和半透明照明大于等于 1.0 时的输出颜色。左侧是亮度为 0 时的输出颜色。

![图：灯光总亮度可用来设置渐变的索引。通过使用渐变和阶跃值，该选项可用来创建卡通样式着色。渐变右侧是漫反射亮度和半透明照明大于…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-DDCEC430-C7D7-40F8-B89D-E6AB7F522BDA.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->

#### 归一化亮度(Normalized Brightness)

“归一化亮度”(Normalized Brightness)选项与标准“亮度”(Brightness)选项十分类似，但总灯光已归一化。更改整个灯光强度不会影响着色。即使照明设置有可能非常复杂，但如果仍希望色带间距相对固定，则此选项对于“卡通”(Toon)着色十分有用。

## “透明度”(Transparency)属性

控制材质透明或不透明的程度，以及透明度颜色。“黑色”默认值是指完全不透明，而“白色”则是指完全透明。可以将它设定为二者之间的任何级别。如果渐变中存在多个索引，则透明度的值将随着正面角度的变化而变化。

这些属性与“颜色”(Color)属性相同，有关它们的描述，请参见[颜色](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-022F69B8-B1A3-46A3-9917-0D9CBDBB6733.htm#WS17956D7ADBC6E73638876AF8117AE33FA94-7FD6)。

## “白炽度”(Incandescence)属性

使材质看起来就像在发光，如熔岩或发磷光的苔藓。默认颜色为黑色，它对曲面无效果。如果渐变中存在多个索引，则白炽度的值将随着正面角度的变化而变化。

前几个属性与“颜色”(Color)属性相同，有关它们的描述，请参见[颜色](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-022F69B8-B1A3-46A3-9917-0D9CBDBB6733.htm#WS17956D7ADBC6E73638876AF8117AE33FA94-7FD6)。

#### 环境色(Ambient color)

请参见[环境色](公用表面材质属性.md#WS73099CC142F48755-3D114B7511812357EFE-68D7)。

#### 凹凸贴图(Bump Mapping)

请参见[凹凸贴图](公用表面材质属性.md#WS73099CC142F48755-3D114B7511812357EFE-68CC)。

#### 漫反射(Diffuse)

请参见[漫反射](公用表面材质属性.md#WS73099CC142F48755-3D114B7511812357EFE-68C8)。

#### 正向散射(Forward Scatter)

控制有多少灯光沿着灯光方向以漫反散的形式散射。当值为 0 时，灯光将以朗伯形式均匀地散射，这适用于大多数曲面。有些材质（如蒙皮）会沿向前方向散射更多灯光。因此，大于零的值更有助于模拟这类材质。

#### 半透明(Translucence)

请参见[半透明](公用表面材质属性.md#WS73099CC142F48755-3D114B7511812357EFE-68C5)。

#### 半透明聚焦(Translucence Focus)

请参见[半透明聚集](公用表面材质属性.md#WS73099CC142F48755-3D114B7511812357EFE-68B6)。

#### 半透明深度(Translucence Depth)

请参见[半透明深度](公用表面材质属性.md#WS73099CC142F48755-3D114B7511812357EFE-68BA)。

## “镜面反射着色”(Specular Shading)属性

#### 镜面反射度(Specularity)

控制镜面反射高光的亮度如何。它是一个简单的镜面反射颜色倍增。

#### 偏心率(Eccentricity)

控制镜面反射高光或热点的大小。有关详细信息，请参见[镜面反射着色(Blinn)](Blinn.md#WS17956D7ADBC6E73638876AF8117AE33FA94-7FEA)。

#### 镜面反射颜色(Specular Color)

指镜面反射（也称为热点）在材质中的颜色。高光反射的最终颜色是“镜面反射颜色”(Specular Color)和和灯光颜色的组合。通过使“镜面反射颜色”(Specular Color)更亮或更暗，可以控制高光反射在对象中的亮度。如果存在多个渐变索引，则镜面反射颜色将根据高光亮度的变化而变化。

这些属性与“颜色”(Color)属性相同，有关它们的描述，请参见[颜色](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-022F69B8-B1A3-46A3-9917-0D9CBDBB6733.htm#WS17956D7ADBC6E73638876AF8117AE33FA94-7FD6)。

#### 镜面反射衰减(Specular Roll Off)

它将相乘或缩放镜面反射高光的强度。正面比是指图表的输入。使图表向右下方倾斜，模拟菲涅尔效果。这样一来，折射率较低的对象将会更向边折射（在边的位置，法线与该视图垂直）。水和蜡的折射率均相对较低，因此有助于模拟打蜡汽车涂层、海洋表面或打湿对象的外观。图表的水平维度表示高光反射的亮度，垂直维度则表示视图的正面角度。

“镜面反射衰减”(Specular Roll Off)不会影响使用光线跟踪渲染时产生的反射。

**注**

提示：

若要获得湿亮外观（如未干的油漆），请使边更反射。

![图：它将相乘或缩放镜面反射高光的强度。正面比是指图表的输入。使图表向右下方倾斜，模拟菲涅尔效果。这样一来，折射率较低的对象将…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-DFCA5F22-BD9F-4542-BB80-38B595A3D21A.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->

#### 选定位置(Selected Position)

指渐变图表的 X 轴中的活动值。

#### 选定值(Selected Value)

指渐变图表的 Y 轴中的活动值。

#### 插值(Interpolation)

控制计算渐变中的值的方式。从下拉列表中选择选项：“无”(None)、“线性”(Linear)、“平滑”(Smooth)、“样条线”(Spline)。默认值为“平滑”(Smooth)。

#### 无(None)

指无插值；不同的颜色在最终纹理中显示为不同的条带。

#### 线性(Linear)

值在 RGB 颜色空间中以线性插值。

#### 平滑(Smooth)

值沿着钟形曲线插值，渐变中的每个值将填充其周围的区域，然后快速融合至下一个值。

#### 样条线(Spline)

它将考虑相邻折射率，以实现更平滑的效果。

### “反射率”(Reflectivity)属性

此功能与镜面反射衰减类似，但它将与环境反射的颜色相乘，而不是与镜面反射度相乘。它还会影响光线跟踪反射。“反射率”(Reflectivity)就像一面镜子一样，用来使对象反射灯光及其环境。设定为 0 时，没有反射。该值越大，反射越亮。请注意，反射越亮，隐藏的基础曲面颜色越多。仅当存在反射贴图或者正在光线跟踪渲染时，此属性才有意义。

**注**

如果正在执行光线跟踪，且需要反射中能够看到场景中的其他对象，则对于这些对象，必须确保已启用“属性编辑器”(Attribute Editor)的“渲染统计信息”(Render Stats)区域中的“在反射中可见”(Visible In Reflections)属性。（默认情况下，该选项处于启用状态。）

有关“选定位置”(Selected Position)、“选定值”(Selected Value)和“插值”(Interpolation)属性的描述，请参见[镜面反射衰减(Specular Roll Off)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-022F69B8-B1A3-46A3-9917-0D9CBDBB6733.htm#WS73099CC142F48755-3D114B7511812357EFE-6762)。

### “环境”(Environment)属性

使用渐变定义一个简单的天空对地面环境的反射情景。渐变的左侧为天空顶部，右侧为天边。

有关“选定位置”(Selected Position)、“选定颜色”(Selected Color)和“插值”(Interpolation)属性的描述，请参见[颜色](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-022F69B8-B1A3-46A3-9917-0D9CBDBB6733.htm#WS17956D7ADBC6E73638876AF8117AE33FA94-7FD6)。

#### 反射的颜色(Reflected Color)

它将影响材质反射的灯光颜色。若要进行虚设反射（所需内存比光线跟踪更少），则可将图像、纹理或环境贴图映射到此属性中。这一过程称为“反射贴图”。反射贴图可以与光线跟踪一起使用。在这种情况下，反射贴图将用作背景，而光线跟踪反射则会用作前景。

## “阴影控制”(Shadow Control)属性

#### 阴影模式(Shadow Mode)

请指定要使用的阴影模式。从下拉列表中选择以下选项之一：

#### 法线(Normal)

如果需要阴影颜色与渐变着色器中最低颜色位置相同，请使用此模式。“阴影颜色”(Shadow Color)和“阴影阈值”(Shadow Threshold)选项在“法线”(Normal)模式中不可用。

#### 着色颜色(Shaded Color)

如果需要根据阴影投射的背景或对象指定具有渐变的特定阴影颜色，请使用此模式。可以使用“阴影颜色”(Shadow Color)属性来设定阴影颜色。

#### 恒定颜色(Constant Color)

如果需要指定与阴影投射的背景或对象无关、且在整个阴影中采用同一纯色的特定阴影颜色，请使用此模式。可以使用“阴影颜色”(Shadow Color)属性来设定阴影颜色。

#### 阴影颜色(Shadow Color)

指定使用“着色颜色”(Shaded Color)或“恒定颜色”(Constant Color)模式时的阴影颜色。

#### 阴影阈值(Shadow Threshold)

指定阴影的扩散。设置的值越大，阴影的扩散越小。当该值为 1 时，不会渲染任何阴影。
