# 文件(File)纹理节点

允许您将图像文件用作 2D 纹理。

若要了解有关“文件”(File)纹理及其创建方式的更多信息，请参见[文件纹理](../../../../关于着色和纹理曲面/纹理/文件纹理.md)。

在“Hypershade”窗口的[“创建”(Create)选项卡](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-76B10C8D-EC19-4AFE-8433-743326C49DBE.htm)中找到此纹理。若要将该纹理应用为纹理贴图，请参见[将 2D 或 3D 纹理映射到材质](../../../../关于着色和纹理曲面/纹理/纹理映射/将%202D%20或%203D%20纹理映射到材质.md)。

## 文件属性

#### 过滤器类型(Filter Type)

指渲染过程中应用于图像文件的采样技术。“二次方”(Quadratic)、“四次方”(Quartic)和“高斯”(Gaussian)过滤器仅在“文件”(File)纹理直接映射到着色组时才会起作用。默认设置为“二次方”(Quadratic)。

如果禁用，则不过滤。对于游戏设计，这可以有助于查看纹理的像素而不用渲染器插值。

**注**

提示：

- 二次方过滤器类型具有最佳的性价比。使用默认设置，该过滤方案能够以合理的成本提供比 mipmap 更清晰的详细信息。

- IFF 图像文件格式具有最佳的性能。

对于 Viewport 2.0，支持的过滤器类型如下所示：

- 禁用(Off)：无过滤器。不构建 Mipmap，使用点采样。生成的图像可能会像素化。

- 长方体(Box)：对 mipmap 纹理执行点采样。缩小对象时使用 Mipmap 纹理，以便缩小纹理时显示较少噪波。

- Mipmap、二次方(Quadratic)、四次方(Quartic)、高斯(Gaussian)：使用三线性过滤并在 mipmap 之间执行采样。此选项提供最平滑的效果，并在缩小对象时生成平滑效果。

##### 二次方(Quadratic)、四次方(Quartic)、高斯(Gaussian)

它们均属于钟形曲线类型。在这类曲线中，极端值的权重小于曲线中心的值。

极端是指过距滤器采样区域最远的纹理中的点。

曲线中心是指要过滤的区域的中心。

“二次方”(Quadratic)和“四次方”(Quartic)与“高斯”(Gaussian)过滤器类型十分类似，但其速度已经过优化。由于高斯方法可能会降低渲染速度，因此，它主要用于高质量的渲染。“二次方”(Quadratic)是最有效的过滤器类型。

##### Mipmap

“Mipmap”将从较大的纹理贴图大小的平均值开始存储值，并按线性方式将贴图大小减少至单个像素值。

使用该过滤器可以进行预览，它运行速度快，而且结果比较理想。但是，请勿将它用于较高质量的渲染。纹理可能会游移或出现模糊。

“Mipmap”的使用成本非常低。默认情况下，Maya 将它用作存储颜色值的技术。与使用其他过滤器类型相比，使用“Mipmap”类型过滤器类型的相关性能成本可以忽略不计。

##### 长方体(Box)

为纹理贴图使用简单的框采样方法。每个贴图采样均会获得相同的着色采样权重。“长方体”(Box)过滤器将使用采样值的总和除以采样数。

#### 预过滤(Pre-Filter)

![图：“预过滤”(Pre-Filter)和“预过滤半径”(Pre-Filter Radius)属性用于校正已混淆的、或者在不需…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-C501282A-0D1B-4894-B008-CA20564A3C07.png) <!-- baize:img-hook downloaded=false reason="正文 7252 字 ≥300，非承重" -->

“预过滤”(Pre-Filter)和“预过滤半径”(Pre-Filter Radius)属性用于校正已混淆的、或者在不需要的区域中包含噪波的文件纹理。这在置换映射时十分有用。

启用时，图像文件将会预过滤，以去除噪波和锯齿，从而提供更优质的结果，特别是对于凹凸贴图尤其如此。默认情况下，“预过滤”(Pre-Filter)已禁用。请启用它，以启用“预过滤半径”(Pre-Filter Radius)属性。

#### 预过滤半径(Pre-Filter Radius)

确定过滤半径的大小。默认值为 2.0，适用于大多数图像，但您可以增加半径以提供更平滑的结果。

#### 图像名称(Image Name)

由“文件”(File)纹理使用的图像文件或影片文件的名称。

有关为“文件”(File)纹理创建图像的提示，请参见[文件纹理](../../../../关于着色和纹理曲面/纹理/文件纹理.md)主题中的“创建文件纹理的注意事项”。

若要使用图像文件序列来创建动画，则该文件名必须以下列三种格式之一来表示：

```text
name.#.ext
name.ext.#
name.#
```

其中，name 是文件的基本名称；# 是帧编号（含或不含前导 0），ext 是文件的文件扩展名。

若要使用图像文件序列来创建动画文件纹理，则文件扩展名必须用句号与基本名称和/或扩展名隔开。

例如，以下格式有效：

```text
test.1.iff
test.0001.iff
test.1
test.0001
test.iff.1
test.iff.0001
```

但不会出现以下情况：

```text
test1
test0001
test1.iff
test0001.iff
```

#### 重新加载(Reload)

使用该按钮可强制刷新（从磁盘读取到临时内存）纹理。如果需要由其他美工人员更新要使用的纹理，建议使用该按钮。

#### 编辑(Edit)

将启动外部应用程序，以便您能够编辑纹理。除非已在[“应用程序”(Applications)首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B58D57D3-9DFA-4C3C-9C64-333D6C8D774A)中指定特定的应用程序，否则将使用默认的系统图像编辑器。

#### 视图(View)

将启动外部应用程序，以便您能够查看纹理。除非已在[“应用程序”(Applications)首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B58D57D3-9DFA-4C3C-9C64-333D6C8D774A)中指定特定的应用程序，否则将使用默认的系统图像查看器。

#### UV 平铺模式(UV Tiling Mode)

选择该选项可使用单个“文件”(File)纹理节点加载、预览和渲染包含对应于 UV 布局中栅格平铺的多个图像的纹理。在 UV 空间中，每个平铺的宽度和高度为单位宽，即 (1x1)。

通过“图像名称”(Image Name)属性加载第一个 UV 平铺，然后选择以下“UV 平铺模式”(UV Tiling Mode)之一：

- “0 型 (Zbrush)”(0-based (Zbrush)) - 如果 UV 坐标起点为 0，请选择此选项

  某些应用程序（例如，Zbrush）使用左下角 UV 坐标对 UV 平铺进行编号。即，UV 平铺 [0,0]x(1,1) 将在其文件名中使用 u0_v0。

- “1 型 (Mudbox)”(1-based (Mudbox)) - 如果 UV 坐标起点为 1，请选择此选项

  某些应用程序（例如，Mudbox）使用右上角 UV 坐标对 UV 平铺进行编号。即，UV 平铺 [0,0]x(1,1) 将在其文件名中使用 u1_v1。

- UDIM (Mari) - 如果 UV 坐标使用公式 1000+(u+1+v*10) 表示为四位数，请选择此选项

- “显式平铺”(Explicit Tiles) - 选择此选项可分别加载每个平铺并显式输入 U 值和 V 值。对于每个平铺，输入与纹理相对应的左下角 UV 坐标的值。

**注**

上面列出的命名约定为每个应用程序的默认设置。可以使用其他约定。

在选择“UV 平铺模式”(UV Tiling Mode)后，“图像名称”(Image Name)字段将使用标记进行更新，这些标记指示 Maya 如何解析文件名：

- “0 型 (Zbrush)”(0-based (Zbrush)) - u<u>_v<v>

- “1 型(Mudbox)”(1-based (Mudbox)) - u<U>_v<V>

- UDIM (Mari) - <UDIM>

解析 UV 坐标后，Maya 指示在指定路径中找到的 UV 平铺数量。

**注**

提示：

如果将鼠标悬停在指示发现的 UV 平铺数量的文本上，则显示工具提示，指示涉及的 UV 范围。

有关 UV 平铺的详细信息，请参见[通过单个纹理节点加载多平铺 UV 纹理](../../../../关于着色和纹理曲面/纹理/纹理映射/通过单个纹理节点加载多个平铺%20UV%20纹理.md)。

#### 预览质量(Preview quality)

将此属性与“UV 平铺模式”(UV Tiling Mode)结合使用。

可以在工作区中调整 UV 平铺纹理的“预览质量”(Preview quality)以减少纹理内存的使用。在“高质量”(High Quality)、“中等质量”(Medium Quality)和“低质量”(Low Quality)间进行选择。也可以选择“禁用预览”(Disable Preview)。

在“Viewport 2.0”中，UV 平铺纹理将烘焙到单个纹理以用于预览。此纹理的分辨率取决于您选择的“预览质量”(Preview Quality)：

- 高质量(High Quality)：4K

- 中等质量(Medium Quality)：2K

- 低质量(Low Quality)：1K

您在“不支持的纹理类型的烘焙分辨率”(Bake Resolution for Unsupported Texture Types)（位于“渲染设置”(Render Settings)窗口）中的设置不会对显示分辨率有任何影响。

在设置“预览质量”(Preview Quality)后，基于“最大纹理分辨率”(Maximum Texture Resolution)设置（位于[“Viewport 2.0 选项”(Viewport 2.0 Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9BBB6035-2A02-41BB-AF2D-99D9BEE580F1)中）应用硬钳制。但是，如果平铺数据不是方形（即，分块线的行列比率小于 0.5 或大于 2），将忽略钳制。

#### 生成预览(Generate Preview)

将此属性与“UV 平铺模式”(UV Tiling Mode)结合使用。

在“图像名称”(Image Name)选项中指定第一个 UV 平铺，并选择“UV 平铺模式”(UV Tiling Mode)后，必须选择“预览质量”(Preview Quality)，然后单击此按钮以生成 UV 平铺纹理的预览。按 6 即可在纹理模式下可视化场景视图中的平铺。

如果在场景中有多个 UV 平铺集，可以通过选择“渲染器 > Viewport 2.0”(Renderer > Viewport 2.0) > ![图：如果在场景中有多个 UV 平铺集，可以通过选择“渲染器 Viewport 2.0”(Renderer Viewport …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 7252 字 ≥300，非承重" -->，然后单击“重新生成所有 UV 平铺预览纹理”(Regenerate All UV Tile Preview Textures)生成所有 UV 平铺集的预览。此全局选项将遵循为每个文件节点保存的“预览质量”(Preview Quality)设置。

如果自上次您单击“生成预览”(Generate Preview)后您的纹理已更改（例如，已重新加载纹理），则按钮将指示“生成预览*”(Generate Preview*)（红色）提示您重新生成预览。

默认情况下，首次打开场景时，Maya 不会加载“Viewport 2.0”中的UV 平铺纹理。您可以选择在场景加载时在“Viewport 2.0”中预览 UV 平铺，方法是：选择“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)打开“首选项”(Preferences)窗口，并在“显示”(Display)部分中启用“场景加载时生成 UV 平铺预览”(Generate UV tile previews on scene load)。如果不修改 UV 平铺，您可以始终在场景加载时自动预览纹理。但是，如果修改 UV 平铺，您必须通过单击“生成预览*”(Generate Preview*)再次手动重新生成预览。

“预览质量”(Preview Quality)设置同时适用于 UV 编辑器和 Viewport 2.0。

#### “使用图像序列”(Use Image Sequence)/“图像编号”(Image Number)/“帧偏移”(Frame Offset)

若要在渲染时使用图像文件序列作为动画纹理，请启用“使用图像序列”(Use Image Sequence)。默认情况下，“使用图像序列”(Use Image Sequence)已禁用。

使用图像序列时，可以设定“图像编号”(Image Number)值的关键帧（默认情况下，它将自动设定关键帧 1）。此外，还可以通过在“帧偏移”(Frame Offset)中输入帧编号，从而偏移“图像编号”(Image Number)关键帧。

[“UV 平铺”(UV Tiling)](文件%28File%29纹理节点.md#GUID-309A77DA-F5ED-4474-8413-317D7AB241E6__GUID-9DE4009C-CD2D-4BF0-B0FE-AFB088FD8858)也支持图像序列。

当您选择“使用图像序列”(Use Image Sequence)时，Maya 会在“图像名称”(Image Name)下通过标记指明将文件名的哪一部分解释为帧编号。例如：

filename.u<U>_v<V>_<f>.tif

在此示例中，第一个标记代表 U 值，第二个标记代表 V 值，第三个标记 <f> 代表帧编号。

有关 UV 平铺的详细信息，请参见[通过单个纹理节点加载多平铺 UV 纹理](../../../../关于着色和纹理曲面/纹理/纹理映射/通过单个纹理节点加载多个平铺%20UV%20纹理.md)。

对于每个帧，Maya 都会指明其在指定路径找到的 UV 平铺数量。

#### 颜色空间(Color Space)

允许您指定图像使用的输入颜色空间。启用颜色管理后，颜色值会自动从此空间变换到用于渲染的工作颜色空间。

您可以在[“颜色管理”(Color Management)首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2D9BBB9D-49F0-44C6-8BFF-B237FD8ED746)中指定用于将颜色空间指定给新节点的规则，以及您的渲染空间和其他设置。可以选择的可用颜色空间取决于您使用 OCIO 配置文件还是用户变换。

不管规则最初指定了哪个颜色空间，您可以始终在此处为单独的节点指定不同的值。此选项非常有用，例如，如果大多数图像是 sRGB，但也在其他颜色空间中使用少数图像，可以使用此选项。指定输入颜色空间后，它就保持不变，除非您手动更改它或者将颜色空间输入规则重新应用于整个场景（请参见[通过重新应用规则自动更改现有的输入颜色空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2BE11876-CF33-45B5-9E7E-CCBFB7611BB6)）。

如果为节点指定的输入颜色空间在当前配置中不可用，其名称将以红色显示，且改用默认输入颜色空间。但是，缺少的颜色空间的名称会保留在场景中，并在您切换为包含该颜色空间的配置时再次使用。或者，可以从此列表中选择可用的颜色空间。如果有许多需要更改的图像输入，则可以更新规则（如有必要）并重新应用它们。

有关颜色管理的常规详细信息，请参见[颜色管理](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5320733B-F9B6-4429-BCAA-F7251D77A8E2)。

#### 忽略颜色空间输入规则(Ignore Color Space Input Rules)

重新应用“输入颜色空间规则”(Input Color Space Rules)时，防止更改已指定的“颜色空间”(Color Space)。如果已手动更改“颜色空间”(Color Space)，但重新应用规则时不希望更改它（例如，具有使用特定颜色空间而不是规则设置的颜色空间的特定图像文件时），则这是很有用的。

#### 使用 BOT (Use BOT)

使用块有序纹理。

如果图像文件不是 BOT 文件，则在渲染过程中，Maya 会为该图像文件创建临时 BOT 文件。这样会降低渲染的速度，并且会增加渲染过程中所使用的磁盘空间量。但是，渲染过程中所使用的内存较少。因此，在使用“优化场景”(Optimize Scene)命令进行渲染之前，将所有图像文件纹理转化为 BOT 文件可能非常有用。

#### 禁用文件加载(Disable File Load)

如果已设定，则不会加载纹理。相反，系统将输出灰色，而不是图像。

## 交互式序列缓存选项(Interactive Sequence Caching Options)

#### 使用交互式序列缓存(Use Interactive Sequence Caching)

“交互式序列缓存”(Interactive Sequence Caching)用于在为纹理设置动画以便以正常速度播放动画时缓存文件纹理。

当“使用交互式序列缓存”(Use Interactive Sequence Caching)处于启用状态时，“序列开始”(Sequence Start)、“序列结束”(Sequence End)和“序列增量”(Sequence Increment)指定的文件纹理只能加载到内存中一次。这将加快文件纹理的交互式动画。

在以下情况中，启用“使用交互式序列缓存”(Use Interactive Sequence Caching)可获得更佳的性能：

- 使用帧序列作为文件纹理

- 在 3D 视图中使用“硬件纹理”(Hardware texturing)

- 需要沿时间线前后拖动（前后移动时间滑块），并查看动画纹理的更新。

在 Viewport 2.0 中缓存图像序列时，如果具有两个序列，每个序列具有不同的帧数，则应该将这两个序列的缓存设置为与时间轴的缓存相同的帧数。

**注**

在 Viewport 2.0 中，PSD 纹理和 UV 平铺不支持“使用交互式序列缓存”(Use Interactive Sequence Caching)。

使用以下属性可指示要加载的帧。如果未全部加载，则 Maya 将使用播放时最近的可用帧。

这些属性不会改变最终渲染的图像。

#### 序列开始(Sequence Start)

“使用交互式序列缓存”(Use Interactive Sequence Caching)处于启用状态时，加载到内存中的第一帧的编号。

#### 序列结束(Sequence End)

“使用交互式序列缓存”(Use Interactive Sequence Caching)处于启用状态时，加载到内存中的最后一帧的编号。

#### 序列增量(Sequence Increment)

控制“使用交互式序列缓存”(Use Interactive Sequence Caching)处于启用状态时 Maya 跳过多少帧（如果存在）执行一次加载到内存的操作。如果为 1，会加载“序列开始”(Sequence Start)和“序列结束”(Sequence End)之间的每一帧。如果为 2，则每隔一帧执行一次加载，依此类推。

## Ptex 控件

#### 过滤器类型(Filter Type)

  “点”(Point)：点采样；即，不进行过滤。

  “高斯”(Gaussian)：创建摄影机软模糊效果。“高斯”(Gaussian)使用曲线衰减的采样贡献。几乎像素中心所有的采样都具有近乎相同的贡献权重，但迅速衰减（平滑）。

  “线性”(Linear)：双线性插值。2x2 方形过滤器用于插值，生成的加权平均为 4 像素。

  “长方体”(Box)：1×1 方形过滤器用于插值。在过滤期间均匀地为所有采样进行加权并具有长方体状外观。

  “双三次”(Bicubic)：4x4 方形用于双三次插值，因此采样 16 像素。更接近原始点的像素的权重高于其他像素。将“锐度”(Sharpness)属性与此过滤方法结合使用。因此会产生附加细节（对于此过滤器方法和后面的过滤器方法），但它是一个处理器密集型的方法，可能会花费较长的时间来渲染。

  “B 样条线”(B-spline)：类似于“双三次”(Bicubic)，但没有锐度。

  “Catmull-Rom”/“Mitchell”：使用 4x4 方形过滤器并生成非常清晰的图像。Mitchell 产生的图像比“Catmull-Rom”清晰，并且针对包含高细节的图像可能会产生更好的结果。

#### 宽度(Width)

过滤器宽度的比例因子。

#### 模糊(Blur)

调整渲染的模糊数量，比例从 0 到 1。

#### 锐度(Sharpness)

“双三次”(Bicubic)选项的锐度级别。

#### 插值级别(Interpolate Levels)

如果 .ptex 文件包含嵌入的 Mipmap 级别，启用该选项可启用 Mipmap 级别之间的插值。

**注**

对于置换贴图，请勿启用此选项。
