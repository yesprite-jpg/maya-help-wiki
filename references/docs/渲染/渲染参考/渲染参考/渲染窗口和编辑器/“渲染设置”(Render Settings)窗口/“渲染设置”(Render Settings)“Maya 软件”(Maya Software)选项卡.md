# “渲染设置”(Render Settings):“Maya 软件”(Maya Software)选项卡

有关渲染设置的信息，请参见[“渲染设置”(Render Settings)窗口](../“渲染设置”%28Render%20Settings%29窗口.md)。

## 抗锯齿质量(Anti-aliasing Quality)

控制渲染过程中 Maya 如何实现对象的抗锯齿。

有关抗锯齿和图像质量的详细信息，请参见[抗锯齿和闪烁](../../../../质量、渲染速度、诊断/质量、渲染速度、诊断/提高渲染图像质量/抗锯齿和闪烁.md)。

## 质量(Quality)

从下拉列表中选择一个预设的抗锯齿质量。选择预设时，Maya 会自动设置所有“抗锯齿质量”(Anti-aliasing Quality)属性。默认设置为“自定义”(Custom)。

#### 自定义(Custom)

更改不匹配任何预设属性值的抗锯齿属性时，Maya 会自动将“预设”(Presets)设置为“自定义”(Custom)。

#### 预览质量(Preview quality)

用在测试渲染场景时（最快）。

#### 中间质量(Intermediate quality)

用在测试渲染场景以产生稍微优于预览质量的质量时。

#### 产品级质量(Production quality)

用在测试或最终渲染不包含 3D 运动模糊的场景或低对比度场景时。

#### 对比度敏感产品级(Contrast sensitive production)

用在测试或最终渲染高对比度场景时（例如对场景进行光线跟踪时。另外对抗锯齿噪波的凹凸贴图也很有用）。

#### 3D 运动模糊产品级(3D motion blur production)

用在测试或最终渲染包含 3D 运动模糊的场景时。

## 边缘抗锯齿(Edge anti-aliasing)

控制对象的边缘在渲染过程中如何进行抗锯齿处理。从下拉列表中选择一种质量设置。质量越低，对象的边缘越显得锯齿状，但渲染速度较快；质量越高，对象的边缘越显得平滑，但渲染速度较慢。

从下拉列表选择“边缘抗锯齿”(Edge anti-aliasing)质量时，Maya 会自动设置所有“抗锯齿质量”(Anti-aliasing Quality)属性（在子区域中）。

#### 低质量(Low quality)

最快的抗锯齿设置。对于每个渲染像素，将分析 2 个点并用其确定对象的哪个部分是可见的，从而生成低质量边缘抗锯齿。

#### 中等质量(Medium quality)

对于每个渲染像素，将分析 8 个点并用其确定对象的哪个部分是可见的，从而生成中等质量边缘抗锯齿。

虽然速度慢一点，但是可以产生比较好的边缘抗锯齿效果。这适合用于测试渲染比较复杂的场景。

#### 高质量(High quality)

对于每个渲染像素，将分析 32 个点并用其确定对象的哪个部分是可见的，从而生成高质量边缘抗锯齿。

可以用于测试以及产品级渲染。

#### 最高质量(Highest quality)

“最高质量”(Highest quality)抗锯齿使用两个过程计算图像，以便在像素内和周围像素中查找颜色对比度，如高光。第一个过程是“高质量”(High quality)计算，第二个过程在第一个过程的结果中查找颜色对比度。在颜色对比度很高的区域（例如，在包含高光的区域）中，将进行更多的着色采样。。

在“高质量”(High quality)基础上进行了改进，非常适合于拾取单个过程（当使用“高质量”(High quality)时）中可能缺失的高光。

## 采样数(Number of Samples)

#### 着色(Shading)

所有曲面的着色采样数。该选项与“着色采样数”(Shading Samples)结合使用，“着色采样数”是曲面“属性编辑器”(Attribute Editor)的“渲染统计信息”区域的一个属性。“着色采样数”(Shading Samples)设定 Maya 对一个像素进行着色的次数。有关详细信息，请参见“渲染统计信息”(Render Stats)和“着色采样数”(Shading Samples)。

#### 最大着色(Max Shading)

如果从“预设”菜单中选择“预览质量”(Preview Quality)作为“抗锯齿质量”(Anti-aliasing Quality)，则该选项不可用。

所有曲面的最大着色采样数。该选项与“最大着色采样数”(Max Shading Samples)结合使用，“最大着色采样数”是曲面“属性编辑器”(Attribute Editor)的“渲染统计信息”(Render Stats)区域的一个属性。“最大着色采样数”(Max Shading Samples)设定在“最高质量”(Highest Quality)渲染的第二个过程中对一个像素进行着色的最大次数。该数目越高，渲染所需时间越长，但会生成更精确的图像。。

#### 3D 模糊可见性(3D blur visib.)

当一个移动对象通过另一个对象时，Maya 精确计算移动对象可见性所需的可见性采样数。

**注**

提示：

- “3D 模糊可见性”(3D Blur Visib)和“最大 3D 模糊可见性”(Max 3D Blur Visib)与“最大可见性采样数”(Max Visib Samples)相关联，后者位于曲面“属性编辑器”(Attribute Editor)的“3D 运动模糊”(3D Motion Blur)区域中。有关详细信息，请参见[渲染统计信息(Render Stats)](../../渲染节点/对象特定的“渲染”%28render%29属性%20-“属性编辑器”%28Attribute%20Editor%29/渲染统计信息%28Render%20Stats%29.md)。

- 仅当在[“渲染设置”(Render Settings)](../“渲染设置”%28Render%20Settings%29窗口.md)窗口的“运动模糊”(Motion Blur)区域中启用“3D 运动模糊”(3D Motion Blur)时，“3D 模糊可见性”(3D Blur Visib)和“最大 3D 模糊可见性”(Max 3D Blur Visib)才可用。

- “最大可见性采样数”(Max Visib Samples)是在启用“运动模糊”(Motion Blur)的情况下为获得可见性而对一个像素进行采样的最大次数。

#### 最大 3D 模糊可见性(Max 3D blur visib.)

在启用“运动模糊”(Motion Blur)的情况下为获得可见性而对一个像素进行采样的最大次数。

#### 粒子(Particles)

粒子的着色采样数。此选项与“着色采样数”(Shading Samples)结合使用，“着色采样数”是曲面“属性编辑器”(Attribute Editor)的“渲染统计信息”(Render Stats)区域的一个属性。着色采样数设置 Maya 对一个像素中的每个碎片进行着色的次数。有关详细信息，请参见“渲染统计信息”(Render Stats)和“着色采样数”(Shading Samples)。

## 多像素过滤(Multi-pixel Filtering)

多像素过滤模糊或柔化整个渲染图像，以帮助消除在渲染图像中的锯齿或锯齿边缘，或者消除渲染动画中的挂绳或闪烁。

这些选项仅当“边缘抗锯齿”(Edge Anti-aliasing)质量设置为“高质量”(High Quality)或“最高质量”(Highest Quality)时有效。

#### 使用多像素过滤器(Use multi pixel filter)

如果启用，Maya 通过对渲染图像中的每个像素使用其相邻像素进行插值来处理、过滤或柔化整个渲染图像，插值是基于“像素过滤器类型”(Pixel filter type)和“像素过滤器宽度 X”(Pixel filter width X)、“Y”设置。

**注**

如果要渲染场，Maya 不会过滤渲染图像，即使“使用多像素过滤器”(Use multi pixel filter)处于启用状态。

#### 像素过滤器类型(Pixel filter type)

控制当“使用多像素过滤器”(Use multi pixel filter)处于启用状态时渲染图像模糊或柔化的程度。有五种预设过滤器供选择 —“长方体过滤器”(Box filter)（非常软）、“三角形过滤器”(Triangle filter)（软）、“高斯过滤器”(Gaussian filter)（略微软）、“二次 B 样条线过滤器”(Quadratic B-Spline filter)（Maya 1.0中使用的过滤器）和“插件过滤器”(Plug-in filter)。默认为“三角形过滤器”(Triangle filter)。

若要使用自定义过滤器，选择“插件过滤器”(Plug-in Filter)。

若要创建插件过滤器，请见[创建和加载插件多像素过滤器](../../../../可视化和渲染图像/可视化和渲染图像/为渲染调整场景设置/创建和加载插件多像素过滤器.md)。

#### 像素过滤器宽度 X (Pixel filter width X)、像素过滤器宽度 Y (Pixel filter width Y)

当“使用多像素过滤器”(Use multi pixel filter)处于启用状态，控制用于对渲染图像中每个像素进行插值的过滤器宽度。如果大于 1，它使用来自相邻像素的信息。值越大，图像越模糊。有效范围是 1 到 3。默认值为 2.2。

**注**

提示：

“像素过滤器宽度 X”(Pixel filter width X)和“像素过滤器宽度 Y”(Pixel filter width Y)值并不需要相同；但是，为了在两个方向上同等模糊渲染图像，这些值应该相同。

## 对比度阈值(Contrast Threshold)

确定自适应采样。当“边缘抗锯齿”(Edge anti-aliasing)设置为“最高质量”(Highest quality)时，控制在第二次过程计算中使用的着色采样数 。

#### 红(Red)、绿(Green)、蓝(Blue)

在每个颜色通道中进行解算，且如果相邻像素的对比度超过了阈值，则进行更多采样。有效范围是 0 到 1。默认值为 0.4（“红”(Red)）、0.3（“绿”(Green)）和 0.6（“蓝”(Blue)）。如果“预设”(Presets)设置为“对比度敏感产品级”(Contrast Sensitive Production)，默认值为 0.2（“红”(Red)）、0.15（“绿”(Green)）和 0.3（“蓝”(Blue)）。

**注**

提示：

- 降低 RGB 值有时会在渲染的图像中产生有趣的功能（例如，小高光或阴影边界），但也会增加渲染时间。

- 在有着色锯齿的相对无色图像中（例如，灰色阴影看起来呈挂绳状），尝试设置“红”(Red)为 0.3、“绿”(Green)为 0.2 以及“蓝”(Blue)为 0.5。

#### 覆盖(Coverage)

只有当“3D”运动模糊”处于启用状态才可用。

控制在“3D”运动模糊”计算过程中“可见性采样数”(Visibility Samples)的次数。如果可见性变化超过了阈值，将进行更多采样。例如，减小此数值有助于渲染器检测到可见对象在像素中的更改（但也会增加渲染时间）。有效范围是 0 到 1。默认值为 0.125。

## 场选项(Field Options)

使用这些选项可控制 Maya 如何将图像渲染为场。

若要了解有关帧和场的详细信息，请参见[帧与场](../../../../可视化和渲染图像/可视化和渲染图像/渲染输出/帧与场.md)和[指定帧或场渲染](../../../../可视化和渲染图像/可视化和渲染图像/为渲染调整场景设置/指定帧或场渲染.md)。

#### 渲染(Render)

控制是否 Maya 将图像渲染为帧或场，用于输出到视频。

**注**

可以使用交替 (Linux)，或 fieldAssembler (Windows)，或者合成或 NLE 应用程序 (Mac OS X) 以交替渲染场。有关交替的详细信息，请参见[交替](../../../../渲染实用程序/渲染实用程序/小工具/交替.md)。

#### 帧(Frames)

渲染常规帧。

#### 两种场，交替(Both fields, interlaced)

渲染奇场和偶场（对于视频）并自动将结果交替成为完全帧。

#### 两种场，单独(Both fields, separate)

同上，但无交替。结果为一序列的奇场和偶场图像。

#### 奇场(Odd fields)

仅渲染奇场。

#### 偶场(Even fields)

仅渲染偶场。

#### 场顺序(Field dominance)

控制 Maya 如何渲染，可以在时间 *X* 渲染“奇场”(Odd fields)并在时间 *X + 0.5* 渲染偶场，或者在时间 *X* 渲染“偶场”(Even fields)并在时间 *X + 0.5* 渲染奇场。

**注**

如果在“场选项”(Field Options)下的“渲染”(Render)属性设置为“帧”(Frames)，“场顺序”(Field dominance)选项将不可用。如果设置为“两种场，交替”(Both fields, interlaced)，Maya 根据格式标准（NTSC 或 PAL）设置相应的场顺序。

#### 第零条扫描线(Zeroth scanline)

（仅适用于高级用户。）

控制 Maya 渲染的第一个场的第一行是在图像顶部还是在底部。

**注**

如果在“场选项”(Field Options)下的“渲染”(Render)属性设置为“帧”(Frames)或“两种场，交替”(Both Fields, Interlaced)，“第零条扫描线”(Zeroth Scanline)选项将不可用。Maya 根据格式标准（NTSC 或 PAL）选择相应的设置。

#### 位于顶部/位于底部(At top/At bottom)

“位于顶部”(At Top)在默认情况下处于启用状态。如果在动画中遇到问题，场顺序显示错误（例如，对象向上和向下摆动），请更改“第零条扫描线”(Zeroth Scanline)设置并重新渲染动画。如果这无法解决问题，或者如果在动画中的对象从左到右摆动，请尝试“场顺序”(Field Dominance)和“第零条扫描线”(Zeroth Scanline)的不同组合，直到问题已解决。

#### 场扩展名(Field extension)

选择下列选项之一：

#### 无场扩展名(No field extension)

如果场是自动交替，本区域的属性不会生效。

没有扩展名将添加到奇场和偶场文件名。

#### 默认场扩展名(o 和 e) (Default field extension (o and e))

如果场是自动交替，本区域的属性不会生效。

Maya 通过添加 *e*（对于偶场）和 *o*（对于奇场）到帧编号扩展名或文件名上的方式保存两个场图像文件。例如，name.001e.png 和 name.001o.png。这是默认设置。

#### 自定义扩展名(Custom extension)

如果场是自动交替，本区域的属性不会生效。

设置启用以指定添加到奇场和偶场文件名的自定义扩展名。例如，如果键入 x，结果是 name.001x.png。

#### 奇场(Odd field)

添加到奇场文件名的扩展名。

#### 偶场(Even field)

添加到偶场文件名的扩展名。

## 光线跟踪质量(Raytracing Quality)

控制是否在渲染过程中对场景进行光线跟踪，并控制光线跟踪图像的质量。更改这些全局设置时，关联的材质属性值也会更改。结果值是两个属性设置中较小的那个值。

有关光线跟踪的详细信息，请参见[深度贴图和光线跟踪阴影](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BC9C9AFE-D90E-4B54-8A2E-22ED1C89A06C)。

#### 光线跟踪(Raytracing)

如果启用，Maya 在渲染期间将对场景进行光线跟踪。光线跟踪可以产生精确反射、折射和阴影（这会显著增加渲染时间，因此请慎用）。

#### 反射(Reflections)

灯光光线可以反射的最大次数。有效范围是 0 到 10。默认值为 1。有关详细信息，请参见“反射限制”。

#### 折射(Refractions)

灯光光线可以折射的最大次数。有效范围是 0 到 10。默认值为 6。有关详细信息，请参见“折射限制”。

**注**

提示：

如果折射变成黑色，确保折射限制设置为足够高的值，并且对象的

“在折射中可见”(Visible in Refractions)

处于启用状态，该属性位于

“属性总表”(Attribute Spreadsheet)

（

“窗口 > 常规编辑器 > 属性总表”(Windows > General Editors > Attribute Spread Sheet)

）和“渲染标志”(Rendering Flags)窗口（

“窗口 > 渲染编辑器 > 渲染标志”(Windows > Rendering Editors > Rendering Flags)

）中。请参见

属性总表

和

“渲染标志”(Rendering Flags)窗口

。

#### 阴影(Shadows)

灯光光线可以反射或折射且仍然导致对象投射阴影的最大次数。值 0 表示禁用阴影。

例如，如果“阴影”(Shadows)值设置为 2，则仅当灯光光线反射或折射一次时能导致对象投射阴影。有效范围是 0 到 10。默认值为 2。

#### 偏移(Bias)

如果场景包含 3D 运动模糊对象和光线跟踪阴影，可能会在运动模糊对象上发现暗区域或错误的阴影。若要解决此问题，请将“偏移”值设置在 0.05 到 0.1 之间。如果场景不包含 3D 运动模糊对象或光线跟踪阴影，保留“偏移”(Bias)值为 0。有效范围是 0 到 1。默认值为 0。

## 运动模糊(Motion Blur)

渲染动画时，运动模糊通过对场景中的对象进行模糊处理来产生移动的效果。可以为对象启用或禁用“运动模糊”(Motion blur)。Maya 使用“快门角度”(Shutter Angle)和“运动模糊”(Motion blur)属性之间的关系来确定将多大程度的模糊应用到对象上。

有关摄影机的快门速度/角度如何影响运动模糊的信息，请参见 [fStop（光圈）和快门速度/角度](../../../../摄影机设置/摄影机设置/聚焦和模糊.md#GUID-39B2D99C-A395-43D5-AD51-BF14F62A6C5C__SECTION_73E6952285484C7599EC5B3FFA93A49D)。

#### 运动模糊(Motion Blur)

如果启用该选项，则“3D”“运动模糊类型”(Motion blur type)以及“按帧模糊”(Blur by frame)也会启用。这意味着移动的对象会显得模糊。如果禁用该选项，移动的对象会显得明晰。默认情况下“运动模糊”(Motion blur)处于禁用状态。

#### 运动模糊类型(Motion blur type)

Maya 对对象进行运动模糊处理的方法。

#### 2D

“2D”运动模糊属于后期处理；Maya 在渲染整个图像之后基于对象的运动向量（其速度和方向）模糊图像中的每个对象。

#### 3D

“3D”运动模糊类似于现实世界中的运动模糊，但所需的渲染时间要长于 2D 运动模糊。默认设置为 3D。

#### 模糊帧数(Blur by frame)

对移动对象进行模糊处理的量。值越大，应用于对象的运动模糊越显著。例如，如果按 1 帧进行运动模糊，模糊计算是基于对象从一帧到下一帧的运动；如果按 4 帧进行运动模糊，模糊计算基于对象的每四个帧长度的运动，在此期间会检测到很多的运动，因此将应用很多模糊。默认值为 1。对移动对象进行模糊处理的量也基于摄影机的“快门角度”。帧的长度由以下因素决定：

（快门角度/360）* 按帧模糊

“快门角度”(Shutter Angle)可以在摄影机的“属性编辑器”(Attribute Editor)的“特殊效果”(Special Effects)区域中修改。

#### 模糊长度(Blur length)

缩放移动对象模糊处理的量。有效范围是 0 到无限。默认值为 1。

#### 使用快门打开/快门关闭(Use Shutter Open/Close)

启用该选项可自定义“快门打开”(Shutter Open)和“快门关闭”(Shutter Close)值。

#### 快门打开/快门关闭(Shutter Open /Shutter Close)

快门打开和关闭值。“快门打开”(Shutter Open)的默认值为 -0.5，“快门关闭”(Shutter Close)的默认值为 0.5。“使用快门打开/快门关闭”(Use Shutter Open/Close)、“快门打开”(Shutter Open)和“快门关闭”(Shutter Close)属性也可以使用 renderGlobals 节点来设置。快门持续时间不能为负值。如果用户在“渲染设置”(Render Settings)窗口中更改值，使得快门持续时间为负值，这些值将被修改以符合正的持续时间。如果在 renderGlobals 节点中设置了负的快门持续时间，则软件渲染器将忽略这些值并进行渲染，就好像“快门打开”(Shutter Open) /“快门关闭”(Shutter Close)值从未设置一样。

该功能是运动模糊功能的附加功能。如果“运动模糊”(Motion Blur)和“使用快门打开/快门关闭”(Use Shutter Open/Close)都已禁用，则不使用运动模糊进行渲染。如果“运动模糊”(Motion Blur)已启用，但“使用快门打开/快门关闭”(Use Shutter Open/Close)处于禁用状态，则 Maya 渲染时使用运动模糊并且使用快门打开及关闭的默认值，即 [-0.5，0.5]。如果“运动模糊”(Motion Blur)和“使用快门打开/快门关闭”(Use Shutter Open/Close)都已启用，则 Maya 将按照指定的时间打开和关闭摄影机的快门。

#### 模糊锐度(Blur sharpness)

运动模糊对象的锐度。“模糊锐度”(Blur sharpness)越大，模糊越分散。有效范围是 0 到无限。默认值为 1。

#### 平滑(Smooth)

选择下列选项之一：

#### Alpha/颜色(Alpha/Color)

有时，“平滑值”属性进行的抗锯齿可能失败，并在未模糊图像的 Alpha 通道中的对应边上产生瑕疵。例如，当明亮的不透明对象在暗灯光雾前通过时。在这种情况下启用“Alpha”或“颜色”(Color)可以通过额外模糊对象来消除瑕疵。。

#### 平滑值(Smooth value)

Maya 模糊运动模糊边的量。值越大，运动模糊抗锯齿效果会越强。有效范围是 0 到无限。默认值为 2。

**注**

提示：

- 增加“平滑值”(Smooth value)也可能模糊静态对象的边，因此如果不希望该效果，请将“平滑值”(Smooth value)设置为 0。

- 可能不希望总是进行额外的模糊，因此仅在必要时使用此属性。也可以尝试将“平滑值”(Smooth value)设置为 0，这将减少抗锯齿，但可能只在某些情况下可接受。

- 对于使用“渐变着色器”(Ramp Shader)着色的对象，2D 运动模糊比 3D 运动模糊（瑕疵）提供更好的结果，但是“平滑”(Smooth)属性必须设置为“颜色”(Color)而不是“Alpha”。

#### 保持运动向量(Keep motion vectors)

如果启用，Maya 保存所有在渲染图像中可见对象的运动向量信息，但是不会模糊图像。这使得可以使用向量数据与其他“2D”模糊软件（例如 blur2d）来模糊渲染图像。

**注**

这仅适用于 Maya IFF 图像。

如果禁用此选项，Maya 模糊渲染图像但不会保存运动向量信息。“保持运动向量”(Keep motion vectors)默认情况下处于禁用状态。

#### 使用 2D 模糊内存限制(Use 2d blur memory limit)

可以指定用于 2D 模糊操作的内存的最大数量。Maya 使用所有可用内存以完成 2D 模糊操作。

#### 2D 模糊内存限制(2D blur memory limit)

可以指定操作使用的内存的最大数量。如果“运动模糊”(Motion blur)处于启用状态并且“运动模糊类型”(Motion blur type)设置为 2D，则“使用 2D 模糊内存限制”(Use 2d blur memory limit)在默认情况下处于启用状态，且提供的默认内存限制为 200 MB。此默认限制应足以消除大多数问题。不过可以在提供的字段中指定内存容量（以 MB 为单位）的大小。

## 渲染选项(Render Options)

### 后期处理(Post Processing)

#### 环境雾(Environment fog)

创建环境雾节点。“环境雾”(Environment fog)（一种“体积材质”）用于模拟空气中的精细粒子的效果（雾、烟或灰尘）。这些粒子影响大气的外观以及大气中对象的外观。

有关“环境雾”(Environment Fog)的详细信息，请参见[环境雾](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A88206BD-28F0-404A-92EB-DD7F929986C8)。

#### 后期应用雾(Apply fog in post)

仅在后期处理渲染雾。启用时，可以设置“后期雾模糊”(Post fog blur)。

#### 后期雾模糊(Post fog blur)

如果结合“后期应用雾”(Apply fog in post)使用，允许环境雾效果看起来好像正在从几何体的边上溢出。增加该值将获得更多模糊。

**注**

该选项的结果不能在 IPR 中看到。

### 摄影机(Camera)

#### 忽略胶片门(Ignore film gate)

如果启用，Maya 将渲染在“分辨率门”(Resolution Gate)中可见的场景区域。如果禁用，Maya 将渲染在“胶片门”(Film Gate)中可见的场景区域，外部区域将渲染为背景色。有关如何以交互方式查看胶片门边界的信息，请参见“摄影机设置”(Camera Settings)和“胶片门”(Film Gate)。“忽略胶片门”(Ignore Film Gate)在默认情况下处于启用状态。

### 灯光和阴影(Lights and Shadows)

#### 阴影链接(Shadow linking)

可以缩短场景所需的渲染时间，采用的方法是链接灯光与曲面，以便只有指定的曲面包含在给定灯光的阴影（阴影链接）或照明（灯光链接）的计算中。

使用下拉列表从该选项的三个可用选项中选择一个：

- 阴影遵守阴影链接(Shadows obey shadow linking)

- 阴影遵守灯光链接(Shadows obey light linking)属性

- 阴影忽略链接(Shadows ignore linking)

场景中的阴影仅可以遵守灯光链接或阴影链接中的一个，而不能同时遵守二者。因此，必须确定要在场景中融入灯光链接还是阴影链接，并从下拉列表中进行相应的选择。

也可以使用默认设置（而不是遵守已创建链接）渲染场景的一部分。选择“阴影忽略链接”(Shadows Ignore Linking)，忽略使用阴影链接或灯光链接建立或断开的所有链接。

默认设置为“阴影遵守灯光链接”(Shadows obey light linking)。

有关阴影链接的详细信息，请参见[阴影链接](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-604555C2-9853-46F7-A4DF-9908F8B75B25)。有关灯光链接的详细信息，请参见[灯光链接](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-08A2A23B-15DB-4F01-96F4-F5011DAE0322)。

#### 启用深度贴图(Enable depth maps)

如果启用，Maya 针对所有深度贴图阴影启用的灯光渲染所有的深度贴图阴影。如果禁用，Maya 不渲染深度贴图阴影。“启用深度贴图”(Enable depth maps)在默认情况下处于启用状态。

### 颜色/合成(Color/Compositing)

#### Gamma 校正(Gamma correction)

根据以下公式颜色校正渲染图像。默认值为 1（无颜色校正）。

![图：根据以下公式颜色校正渲染图像。默认值为 1（无颜色校正）。 注： 较大的 Gamma 值会使图像的中间色调变亮。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-1F843435-93E2-4BF3-8480-6E476ECEF693.png) <!-- baize:img-hook downloaded=false reason="正文 14940 字 ≥300，非承重" -->

**注**

较大的 Gamma 值会使图像的中间色调变亮。

#### 片段最终着色颜色(Clip final shaded Color)

如果启用，渲染图像中的所有颜色值将保持在 0 和 1 之间。这样可以确保图像的任何部分（例如，前景对象）都不会曝光过度。如果禁用，渲染图像中的颜色值可能大于 1。“片段最终着色颜色”(Clip final shaded color)在默认情况下处于启用状态。

#### 抖动最终颜色(Jitter final color)

如果启用，则图像的颜色将抖动以减少条纹。

#### 预乘(Premultiply)

如果此选项处于启用状态（默认），将进行预乘（请参见[预乘图像](../../../../可视化和渲染图像/可视化和渲染图像/传统渲染层和渲染过程/传统渲染层概念.md#WS17956D7ADBC6E7366A2D893A117AE33D52A-7FDF)）。如果此选项处于禁用状态，则预乘阈值选项启用。

如果禁用，Maya 渲染对象时不会针对背景进行抗锯齿处理。例如，对象边上的像素不会与背景色混合。（用 TIFF 术语来讲，Maya 会生成非关联的 Alpha。）如果启用，Maya 将针对背景对对象进行抗锯齿处理。“预乘”(Premultiply)在默认情况下处于启用状态。

**注**

提示：

如果为胶片或视频渲染图像，应禁用

“预乘”(Premultiply)

。如果要为视频游戏渲染图像，应启用“预乘”。

#### 预乘阈值(Premultiply threshold)

如果此选项处于启用状态（当默认预乘处于禁用状态），每个像素的颜色值仅在像素的 alpha 通道值高于在此设置的阈值时才输出。

控制在“预乘”(Premultiply)处于启用状态下蒙版中边缘抗锯齿的量。如果在渲染视频游戏中使用的图像，并且使用的是 8 位或 16 位颜色，将“预乘阈值”(Premultiply threshold)设置为 1 以产生没有锯齿边的平滑蒙版边。默认值为 0。

## 内存与性能选项(Memory and Performance Options)

“内存与性能选项”(Memory and Performance Options)属性有助于优化渲染以使场景的渲染速度更快。

有关渲染速度和图像质量的详细信息，请参见[质量、渲染速度、诊断￼](../../../../质量、渲染速度、诊断/质量、渲染速度、诊断.md)。

### 细分(Tessellation)

有助于管理 Maya 如何处理曲面的细分信息。

#### 使用文件缓存(Use file cache)

启用将几何体信息存储到在指定目录中的“缓存”文件，该目录由系统的 TEMP（Windows 和 Mac OS X）或 TMPDIR (Linux) 环境变量指定，以降低用于存储几何体数据的内存。启用此选项允许渲染器执行其自身的交换。

在 Maya.env 文件中，输入 Temp = defaultPath，其中 defaultPath 是新的临时目录的路径名。

- (Linux)。如果 TMPDIR 已设置，Maya 将使用该目录，除非它有写入权限问题，在有写入权限问题的情况下，Maya 默认为 /usr/tmp。如果仍然无法写入 /usr/tmp，将出现警告消息。

- (Windows)。如果 TEMP 已设置，且可写入的话将使用该目录。如果不可写入，将出现警告消息。

- (Mac OS X)。如果 TEMP 已设置，Maya 将检查是否具有写入权限，如果该目录不可写入，则默认为使用在 Home 目录下的 Documents/temp 目录。如果无法写入 Documents/temp，将出现警告消息。

如果以上方法仍然无法找到临时目录，最终将尝试把正在使用的当前目录设置为临时目录。

**注**

“使用文件缓存”(Use file cache)

有助于防止在多处理器计算机上渲染大场景时超出最大内存带宽和磁盘空间。

在渲染非常大的场景之前，键入：

Linux：

setenv TMPDIR *NAMEOFDIR*

Windows：

SET TEMP= *NAMEOFDIR*

其中 *NAMEOFDIR *具有大量磁盘空间的分区的位置。

#### 优化实例(Optimize instances)

如果启用，并且场景中包含几个相同的曲面（例如，实例化的曲面或单独创建的相同曲面），Maya 只细分其中一个以节约时间和磁盘空间。“优化实例”(Optimize instances)在默认情况下处于启用状态。

#### 重用细分(Reuse tessellations)

如果启用，Maya 会暂时将每个帧的细分信息保存到磁盘。

如果场景中包含深度贴图阴影，该选项将十分有用。例如，Maya 在生成灯光的深度贴图时细分曲面（并将细分信息保存到磁盘），然后在生成其他灯光的深度贴图和渲染帧时可以重用细分信息。（Maya 从磁盘移除细分信息，并为下一个帧重新计算。）“重用细分”(Reuse tessellations)在默认情况下处于启用状态。

**注**

重用细分是一种受 I/O 限制的进程，在同一台计算机上运行多个渲染作业时可能会超出最大带宽。在一台多处理器计算机上运行最多四个作业的情况下，“重用细分”将有所帮助。可以尝试禁用“渲染设置 > 使用文件缓存”(Render Settings > Use file cache)。

#### 使用置换边界框(Use displacement bounding box)

使用置换贴图时，可能需要很长时间才能完成渲染，因为在渲染分片之前，Maya 会细分所有置换贴图的曲面并计算其边界框。启用“使用置换边界框”(Use displacement bounding box)时，Maya 会计算您为所有置换贴图的曲面定义的边界框比例，这将使渲染速度更快。禁用此选项后，Maya 会在渲染前预细分所有置换贴图的对象。有关详细信息，请参见“边界框比例”。

### 光线跟踪(Ray Tracing)

有助于控制光线跟踪。有关光线跟踪属性的信息，请参见“光线跟踪质量”(Raytracing Quality)。

有关光线跟踪的详细信息，请参见[深度贴图和光线跟踪阴影](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BC9C9AFE-D90E-4B54-8A2E-22ED1C89A06C)。

#### 递归深度(Recursion depth)

确定使用多少级别的递归，以用于渲染的光线跟踪体素数据结构。对于非常复杂的场景应设置为 2 或 3。对于不太复杂的场景，设置为 1 即可。默认值为 2。

#### 叶基本体(Leaf primitives)

确定在转到下一个递归级别前体素中允许的最多三角形数。默认值为 200。

#### 细分幂(Subdivision power)

代表体素内三角形数量升至的幂，以计算当需要递归时应创建的体素数量。默认值为 0.2500，应当适用于大多数场景。对于非常复杂的场景或具有复杂部分的场景，该值可以稍微增加。

### 多重处理(Multi Processing)

多线程交互式渲染可用于“渲染视图”(Render View)。它为批渲染提供了相同种类的性能增益。用于交互式渲染和 IPR 的 CPU 数将单独进行设置。Maya 保存为场景设置的值。

有关详细信息，请参见[使用 Maya 软件进行网络渲染](../../../../网络渲染/网络渲染/使用%20Render%20命令行实用程序进行网络渲染.md)。

#### 使用所有可用 CPU (Use all available CPUs)

默认情况下，使用所有可用 CPU。如果禁用，则选项下方的滑块处于启用状态。

#### 要使用的CPU 数 (Num. CPUs to use)

滑块值可以从 1 到 8 拖动，但如果需要的话可输入最高达 256 的更大值。输入值 0 或启用该选项将启用所有 CPU 进行交互式渲染。

注释

- 如果希望多处理器批渲染，在“批渲染”窗口设置要使用的处理器数，或在命令行渲染时使用 -n 标志（Maya 软件渲染）。

- 如果 IPR 正在使用中，在当前 IPR 过程关闭之前 CPU 数不能更改。将出现以下警告信息：// Warning: IPR will need to be closed before this change in CPUs will take effect. //

## IPR 选项(IPR Options)

这些属性确定当执行 IPR 渲染时哪些着色元素将保存至磁盘。这样可以节省时间和磁盘空间。

有关 IPR 的详细信息，请参见[关于交互式真实照片级渲染 (IPR)](../../../../可视化和渲染图像/可视化和渲染图像/渲染方法/关于交互式真实照片级渲染%20%28IPR%29.md)。

#### 渲染着色、照明和辉光(Render shading, lighting and glow)

确定是否处理下一个 IPR 渲染的着色、照明和辉光特征。

#### 渲染阴影贴图(Render shadow maps)

深度贴图阴影包括在 IPR 渲染中。

启用之后可显示场景中的深度贴图阴影，并可以在进行调整时更新。由于生成深度贴图是一个耗时且密集使用处理器的操作（例如从灯光角度进行的完整渲染），IPR 不会在调整属性时自动生成深度贴图。

**注**

- 灯光属性编辑器的“深度贴图阴影属性”(Depth Map Shadow Attributes)区域第一部分中的属性将影响深度贴图的创建方式。必须选择“IPR > 更新阴影贴图”(IPR > Update Shadow Maps)，才能查看更改这些属性所产生的效果。

- 灯光“属性编辑器”(Attribute Editor)“深度贴图阴影属性”(Depth Map Shadow Attributes)区域第二部分中的属性会影响深度贴图的使用方式；可以调整这些属性，并在 IPR 会话中立即查看结果。

#### 渲染 2D 运动模糊(Render 2D motion blur)

启用之后能够为下一个 IPR 渲染调整 2D 运动模糊。只有 2D 运动模糊是可调整的。

## Paint Effects 渲染选项(Paint Effects Rendering Options)

有关 Paint Effects 的详细信息，请参见 [Paint Effects](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-57DB1F5B-E375-45C6-8EDD-76D26A277F3A)。

以下仅说明绘制工具的渲染选项。

#### 启用笔划渲染(Enable stroke rendering)

启用此选项以渲染场景中的“Paint Effects”笔划。如果禁用此选项，场景渲染时没有笔划。默认情况下，该选项处于启用状态。

#### 过采样(Oversample)

以双倍的分辨率渲染“Paint Effects”，以获得更好的抗锯齿。

#### 过采样后置过滤器(Oversample post filter)

将加权过滤器应用到过采样图像以获得更好的平滑。

**注**

“过采样”(Oversample)和“过采样后置过滤器”(Oversample post filter)选项在渲染“Paint Effects”毛发或头发时特别有用。如果不转化“Paint Effects 到多边形”(Paint Effects to Polygons)，新的“网格笔刷类型”(Mesh Brush Type)也需要过采样以用于管边的抗锯齿。

#### 仅渲染笔划(Only render strokes)

启用该选项将仅渲染场景中的“Paint Effects”笔划。您可能希望将笔划与场景其余部分分开渲染，然后合成笔划与场景。有关 Paint Effects 的详细信息，请参见 [Paint Effects](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-57DB1F5B-E375-45C6-8EDD-76D26A277F3A)。

#### 读取此深度文件(Read this depth file)

如果合成渲染的场景与渲染的“Paint Effects”笔划，请键入渲染场景的深度文件的位置和名称。使用绝对路径名称（例如，/h/username/rainyday.iff (Linux)，或 c:\username\rainyday.iff (Windows)，或 /username/rainyday.iff (Mac OS X)）。

**注**

当仅渲染笔划时，还必须在“读取此深度文件”(Read this depth file)字段中指定一个 .IFF 文件（参见下文）。文件可以是空的。它不必包含深度数据。

如果渲染动画并且有动画输入文件，请将 # 字符放在源输入文件中帧编号的位置。例如，对于文件 foo1.iff、foo2.iff 等，输入 foo #.iff。对于文件 foo1、foo2 等，输入 foo #。渲染时，# 字符替换为当前帧编号。

有关 Paint Effects 笔划的详细信息，请参见 [Paint Effects](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-57DB1F5B-E375-45C6-8EDD-76D26A277F3A)。

**注**

最好提供深度文件并允许 Maya

“Paint Effects”

进行合成，而不是尝试使用合成器将“Paint Effects”作为后期处理来合成。Maya

“Paint Effects”

使用多层深度和 RGB 缓冲区来执行与场景的合成，并能获得比后期处理合成器更好的合成效果。

另外，如果不提供深度文件（具有深度信息的 .IFF 文件），将渲染场景中对象后面的“Paint Effects”笔划。Maya 不会覆盖作为深度文件提供的现有图像，输出将按[“渲染设置”(Render Settings)窗口](../“渲染设置”%28Render%20Settings%29窗口.md)顶部显示的那样命名。
