# PSD 文件(PSD File)

允许将 PSD 文件用作 2D 纹理。

### 过滤器类型(Filter Type)

指渲染过程中应用于图像文件的采样技术。“二次方”(Quadratic)、“四次方”(Quartic)和“高斯”(Gaussian)过滤器仅在“文件”(File)纹理直接映射到着色组时才会起作用。默认设置为“二次方”(Quadratic)。

如果禁用，则不过滤。对于游戏设计，这可以有助于查看纹理的像素而不用渲染器插值。

**注**

提示：

- 二次方过滤器类型具有最佳的性价比。使用默认设置，该过滤方案能够以合理的成本提供比 mipmap 更清晰的详细信息。

- IFF 图像文件格式具有最佳的性能。

#### 二次方(Quadratic)、四次方(Quartic)、高斯(Gaussian)

它们均属于钟形曲线类型。在这类曲线中，极端值的权重小于曲线中心的值。

极端是指过距滤器采样区域最远的纹理中的点。

曲线中心是指要过滤的区域的中心。

“二次方”(Quadratic)和“四次方”(Quartic)与“高斯”(Gaussian)过滤器类型十分类似，但其速度已经过优化。由于高斯方法可能会降低渲染速度，因此，它主要用于高质量的渲染。“二次方”(Quadratic)是最有效的过滤器类型。

#### Mipmap

“Mipmap”将从较大的纹理贴图大小的平均值开始存储值，并按线性方式将贴图大小减少至单个像素值。

使用该过滤器可以进行预览，它运行速度快，而且结果比较理想。但是，请勿将它用于较高质量的渲染。纹理可能会游移或出现模糊。

“Mipmap”的使用成本非常低。默认情况下，Maya 将它用作存储颜色值的技术。与使用其他过滤器类型相比，使用“Mipmap”类型过滤器类型的相关性能成本可以忽略不计。

#### 长方体(Box)

为纹理贴图使用简单的框采样方法。每个贴图采样均会获得相同的着色采样权重。“长方体”(Box)过滤器将使用采样值的总和除以采样数。

#### 预过滤(Pre-Filter)

“预过滤”(Pre-Filter)和“预过滤半径”(Pre-Filter Radius)属性用于校正已混淆的、或者在不需要的区域中包含噪波的文件纹理。这在置换映射时十分有用。

启用时，图像文件将会预过滤，以去除噪波和锯齿，从而提供更优质的结果，特别是对于凹凸贴图尤其如此。默认情况下，“预过滤”(Pre-Filter)已禁用。请启用它，以启用“预过滤半径”(Pre-Filter Radius)属性。

#### 预过滤半径(Pre-Filter Radius)

确定过滤半径的大小。默认值为 2.0，适用于大多数图像，但您可以增加半径以提供更平滑的结果。

![图：确定过滤半径的大小。默认值为 2.0，适用于大多数图像，但您可以增加半径以提供更平滑的结果。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-C501282A-0D1B-4894-B008-CA20564A3C07.png) <!-- baize:img-hook downloaded=false reason="正文 2939 字 ≥300，非承重" -->

#### 图像名称(Image Name)

由“文件”(File)纹理使用的图像文件或影片文件的名称。

有关为“文件”(File)纹理创建图像的提示，请参见[文件纹理](../../../../关于着色和纹理曲面/纹理/文件纹理.md)。

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

但以下格式无效：

```text
test1
test0001
test1.iff
test0001.iff
```

#### 重新加载(Reload)

使用该按钮可强制刷新（从磁盘读取到临时内存）纹理。如果需要由其他美工人员更新要使用的纹理，建议使用该按钮。

#### 编辑(Edit)

将从 Maya 中启动外部应用程序，以便您能够编辑纹理。除非已在“应用程序”首选项中指定特定的应用程序，否则将使用默认的系统图像编辑器。有关详细信息，请参见手册“基础知识”部分中的[应用程序首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B58D57D3-9DFA-4C3C-9C64-333D6C8D774A)。

#### 视图(View)

将从 Maya 中启动外部应用程序，以便您能够查看纹理。除非已在“应用程序”首选项中指定特定的应用程序，否则将使用默认的系统图像查看器。有关详细信息，请参见手册的“基础知识”部分中的[应用程序首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B58D57D3-9DFA-4C3C-9C64-333D6C8D774A)。

#### 链接到层集(Link to Layer Set)

如果 PSD 文件具有多个层集或组，则可以选择仅链接到一个组。从该属性中选择层，以显示所需的层集。

#### 要使用的 Alpha (Alpha to Use)

选择要在场景视图中查看的遮罩通道。

#### 禁用文件加载(Disable File Load)

如果已设定，则不会加载纹理。相反，系统将输出灰色，而不是图像。

#### 使用图像序列的图像编号的帧偏移(Use Image Sequence Image Number Frame Offset)

若要在渲染时使用图像文件序列作为动画纹理，请启用“使用图像序列”(Use Image Sequence)。默认情况下，“使用图像序列”(Use Image Sequence)已禁用。

使用图像序列时，可以设定“图像编号”(Image Number)值的关键帧（默认情况下，它将自动设定关键帧 1）。此外，还可以通过在“帧偏移”(Frame Offset)中输入帧编号，从而偏移“图像编号”(Image Number)关键帧。

## 硬件纹理循环选项(Hardware Texture Cycling Options)

#### 使用硬件纹理循环(Use Hardware Texture Cycling)

“硬件纹理循环”(Hardsware Texture Cycling)用于在设置纹理的动画时缓存文件纹理，以便按常规速度播放动。

当“使用硬件纹理循环”(Use Hardware Texture Cycling)启用时，在“开始循环扩展”(Start Cycle Extension)、“结束循环扩展”(End Cycle Extension)和“按循环增量”(By Cycle Increment)范围内指定的文件纹理仅需一次即可加载到内存中。这样有助于加快设置文件纹理的交互式动画。

在以下情况中，启用“使用硬件纹理循环”(Use Hardware Texture Cycling)可以获得更好的性能：

- 使用帧序列作为文件纹理

- 在 3D 视图中使用“硬件纹理”(Hardware texturing)

- 需要沿时间线前后拖动（前后移动时间滑块），并查看动画纹理的更新。

使用以下属性可指示要加载的帧。如果未全部加载，则 Maya 将使用播放时最近的可用帧。

**注**

这些属性不会改变最终渲染的图像。

#### 开始循环扩展(Start Cycle Extension)

指当“使用硬件纹理循环”(Use Hardware Texture Cycling)启用时 Maya 加载到内存的第一帧的编号。

#### 结束循环扩展(End Cycle Extension)

指当“使用硬件纹理循环”(Use Hardware Texture Cycling)启用时 Maya 加载到内存的上一帧的编号。

#### 按循环增量(By Cycle Increment)

控制当“使用硬件纹理循环”(Use Hardware Texture Cycling)启用时跳过的 Maya 加载到内存的帧数（如有）。如果值为 1，则 Maya 将加载“开始循环扩展”(Start Cycle Extension)和“结束循环扩展”(End Cycle Extension)之间的每一帧。如果数量为 2，则 Maya 将每隔一个帧加载一个，依此类推。
