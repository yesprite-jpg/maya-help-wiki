# 渲染统计信息(Render Stats)

从属性总表（“窗口 > 常规编辑器 > 属性总表”(Windows > General Editors > Attribute Spread Sheet)）或[“渲染标志”(Rendering Flags)窗口](../../渲染窗口和编辑器/“渲染标志”%28Rendering%20Flags%29窗口.md)（“窗口 > 渲染编辑器 > 渲染标志”(Windows > Rendering Editors > Rendering Flags)）的某些选定对象的属性编辑器中可找到此部分。

当适用于选定对象时，“渲染统计信息”(Render Stats)部分将显示在“属性编辑器”(Attribute Editor)中。这些选项可以为选定对象启用或禁用各种渲染选项。

#### 投射阴影(Casts Shadows)

确定曲面是否投射阴影。若要使阴影渲染速度更快，请为不需要投射阴影的曲面禁用“投射阴影”(Casts Shadows)。

如果希望渲染对象的阴影（投射到其他对象上），请启用“投射阴影”(Casts Shadows)。如果不希望对象的阴影投射到要渲染的其他对象上，请将其禁用。

**注**

- 如果要单独渲染阴影，请使用合成软件中的已渲染阴影图像的遮罩通道来降低另一个图像的亮度。

- 从“渲染视图”(Render View)窗口渲染时，通过选择“渲染 > 仅渲染选定对象”(Render>Render Selected Objects Only)，可以仅渲染选定对象。

#### 接收阴影(Receive Shadows)

启用曲面的阴影捕捉功能。

#### 延续(Hold-Out)

逐对象启用此选项，以便对象渲染透明度，并直接显示到背景环境；例如，图像平面。适用于 Viewport 2.0。此功能支持阴影（“接收阴影”(Receive Shadows)）。

**注**

在已启用“延续”(Hold-Out)选项的对象上可能会显示瑕疵（如果还为这些对象启用了阴影）。

在已使用“屏幕空间环境光遮挡”(Screen-space Ambient Occlusion)和“多采样抗锯齿”(Multisampling Anti-aliasing)的场景中，已启用“延续”(Hold-Out)选项的对象可能会阻止图像平面。若要解决此问题，请禁用“屏幕空间环境光遮挡”(Screen-space Ambient Occlusion)和“多采样抗锯齿”(Multisampling Anti-aliasing)。

#### 运动模糊(Motion Blur)

启用表面的运动模糊。还必须在[“渲染设置”窗口](../../渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)中启用“运动模糊”(Motion Blur)。

#### 主可见性(Primary Visibility)

启用时，曲面将包含在软件渲染中。

**注**

提示：

但是，如果曲面的“主可见性”(Primary Visibility)已禁用且“投射阴影”(Cast Shadows)已启用，则曲面的阴影会渲染。这也适用于反射和折射。

#### 平滑着色处理(Smooth Shading)

如果启用该选项，则每个顶点都使用其自身的法线向量，这就意味着两个面之间的过渡更为平滑。如果该选项已禁用，则一个法线向量会用于一个面；三角形中的 3 个顶点会使用同一法线向量，从而产生平坦外观着色。

#### 在反射中可见(Visible In Reflections)

启用时，曲面会在反射曲面中反射。

#### 在折射中可见(Visible In Refractions)

启用时，曲面将在透明曲面中发生折射。

#### 双面(Double Sided)

确定表面是否为双面。如果是单面的，则可以减少内存使用，并使用“反向”(Opposite)选项。

#### 反向(Opposite)

“反向”会翻转曲面法线。必须禁用“双面”以设定为“反向”。

#### 几何体抗锯齿覆盖(Geometry Anti-aliasing Override)

启用该选项后，表面将覆盖几何体抗锯齿设置。

**注**

提示：

运动模糊对象会忽略对

“几何体抗锯齿覆盖”(Geometry Anti-aliasing Override)

设置的任何更改。模糊通常会隐藏所有锯齿瑕疵。

#### 抗锯齿级别(Antialiasing Level)

选择下列选项之一：

#### 级别 1

默认值。它采用 32 个可见性采样。

#### 级别 2

采用 96 个可见性采样。

#### 级别 3

采用 288 个可见性采样。

#### 级别 4

采用 512 个可见性采样。

#### 级别 5

采用 800 个可见性采样。级别 5 可提供最佳的边抗锯齿质量，但系统开销也最高（就内存和速度两方面而言）。

#### 着色采样数覆盖(Shading Samples Override)

启用时，曲面会覆盖[“渲染设置”窗口](../../渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)中的全局着色采样设置。

#### 着色采样数(Shading Samples)

设置 Maya 对每个像素采样的最少次数。例如，如果设置为 1，Maya 会对每个像素采样 1 次；如果设置为 8，Maya 会对每个像素采样 8 次。对每个像素进行的着色采样数受“边缘抗锯齿”(Edge Anti-Aliasing)计算执行的可见性采样数限制。因此，如果使用“中等质量”(Medium Quality)（逐像素执行 8 个可见性采样），则无法获得 8 个以上的着色采样数，而不管“着色采样数”(Shading Samples)属性设置如何。

因为“着色采样数”(Shading Samples)计算开销很大，所以应该首先尝试调整下面的“最大着色采样数”(Max Shading Samples)。

#### 最大着色采样数(Max Shading Samples)

在“最高质量”(Highest Quality)渲染的第二过程（自适应着色过程）中设定对像素进行采样的最大次数。该数字越大，渲染花费的时间就越长，但产生的图像越精确。

仅当与“最高质量边缘抗锯齿”(Highest Quality edge anti-aliasing)一起使用时，“最大着色采样数”(Max Shading Samples)才有效。另外，根据进行精确解算的要求，采用的“着色采样数”(Shading Samples)的数量可以小于“最大着色采样数”(Max Shading Samples)的数量。

**注**

提示：

- 有时，在对象移动时，对象的带纹理边看起来会失真。若要解决该问题，请尝试增加“最大着色采样数”(Max Shading Samples)的数量。

- 有时，细条状高光可能显示出挂绳状瑕疵或闪烁瑕疵。请尝试增大“最大着色采样数”(Max Shading Samples)设置。还可能需要增加“着色采样数”(Shading Samples)设置，但可以对每个对象进行设定。

#### “已预乘”(Already Premult)

选择该选项表明图像平面已预乘 Alpha 通道；也就是说，RGB 值已与 Alpha 通道相乘。

**注**

下列属性仅适用于体积基本体和流体形状。它们仅显示在体积基本体或流体形状的形状节点的“属性编辑器”(Attribute Editor)中。

#### 体积采样数覆盖(Volume Samples Override)

如果启用该选项，对象会覆盖全局体积着色设置，并可以在“渲染设置”(Render Settings)窗口中启用“深度抖动”(Depth Jitter)选项。

#### 体积采样数(Volume samples)

调整放置在雾体积内的采样数。

#### 深度抖动(Depth Jitter)

如果设定启用“体积采样数覆盖”(Volume Sample Override)，则可以启用“深度抖动”(Depth Jitter)选项。随机化其体积将使用噪波替换体积渲染中的带状瑕疵的体积采样数。可以通过增加体积采样数和抗锯齿级别来大幅减少噪波。

## 3D 运动模糊

#### 最大可见性采样数覆盖(Max Visibility Samples Override)/最大可见性采样数(Max Visib Samples)

对于选定的形状节点，在渲染过程中覆盖表面采用的全局最大运动模糊可见性采样数。
