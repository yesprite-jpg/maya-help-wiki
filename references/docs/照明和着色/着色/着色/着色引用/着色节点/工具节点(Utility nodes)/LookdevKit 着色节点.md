# LookdevKit 着色节点

lookdevKit 插件提供了一组噪波、数学和工具节点，最适合在“Hypershade”中创建程序网络。

若要创建这些节点，请确保在“插件管理器”(Plug-in Manager)（“窗口 > 设置/首选项”(Windows > Settings/Preferences)）中启用 lookdevKit.mll 插件。

有关噪波节点的信息，请参见 [LookdevKit 单一噪波节点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-615F0CA0-ADE4-4A79-9FDB-90B2B51AED0C.htm)。

每个节点都具有颜色和 Alpha 输入，其中颜色输入仅影响颜色值，而 Alpha 输入仅影响 Alpha 值。

下面列出的所有**颜色**节点都具有对应的**浮点型**对象，例如“浮点合成”(Float Composite)与“颜色合成”(Color Composite)，其仅接受一个浮点输入（如置换贴图），而不是浮点 3 输入（例如颜色）。如果您只需要处理单个通道，更有效率的方法是使用浮点节点。

## 颜色合成

使用此节点对纹理分层，然后从若干“操作”(Operation)模式中进行选择。尝试使用不同的分层模式来创建最适合您的效果。

调整“系数”(Factor)属性来控制合成效果的强度；例如，用于淡出特定效果，或为着色图表的某个方面制作动画。

在此示例中，使用“颜色合成”(Color Composite)节点将天空图像与鞋带图案结合起来。此图像比较所有不同模式的结果。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-4B54F34C-4171-4F83-955B-4A1F9A41616B.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

纹理由 www.cgtextures.com 提供。

分层模式如下：

- 相加(Add)：将颜色 A 与颜色 B 的值相加。使用此模式可为纹理添加光晕效果。

- 相减(Subtract)：从颜色 A 中减去颜色 B 以使纹理变暗。您也可以使用此模式在纹理中创建洞。

- 混合(Mix)：混合颜色 A 与颜色 B 的值。使用此模式可在两个纹理之间淡入淡出，或混合两种设置了动画的纹理。

- 相乘(Multiply)：将颜色A 的值与颜色 B 的值相乘以使纹理变暗。使用此模式可应用环境光阻光贴图，以创建阴影或添加污垢层。

  通常使用此模式将漫反射纹理与带有暗色区域的白色纹理相乘。所有暗色区域都将被调暗。

  **注**

  提示：

  您可以使用

  “反转”(Reverse)

  节点反转纹理的白色与暗色图案。

  在此示例中，“颜色合成”(Color Composite)设置为“相乘”(Multiply)，以便将渐变用于变暗天空纹理中低于地平线的区域。

  ![图：相乘(Multiply)：将颜色A 的值与颜色 B 的值相乘以使纹理变暗。使用此模式可应用环境光阻光贴图，以创建阴影或添…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-6EE0058E-8593-4776-A23D-B3017FE760C8.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

  天空纹理由 www.cgtextures.com 提供。

- 屏蔽(Screen)：合成两个纹理并使较暗的区域变得透明。它类似于“相加”(Add)模式，但不会添加“相加”(Add)产生的放射光效果。应用它的一个例子是将层灰尘添加到漫反射纹理。

- 叠加(Overlay)：较暗区域变得更暗，较亮区域变得更亮，而中间色调是透明的。此模式会调整对比度。

  它可使细节变得更清晰；例如，使角色面部纹理的眼睛亮显。

  ![图：叠加(Overlay)：较暗区域变得更暗，较亮区域变得更亮，而中间色调是透明的。此模式会调整对比度。 它可使细节变得更清…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-FEDD9689-9744-4FE7-AECE-05AE1339CBE3.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

- 差集(Difference)：比较两个纹理并仅输出两者之间不同的像素。

  应用它的一个例子是获得两个纹理（例如两个噪波）之间的交集，然后将合成结果应用到另一个纹理。

  在此示例中，通过将 Difference_ColorComposite 设置为“差集”(Difference)模式获得两个噪波节点之间的交集。然后，使用另一个“颜色合成”节点 (MultiplyDifference_ColorComposite) 将结果与黄色 (Yellow_ColorConstant) 融合在一起。

  ![图：差集(Difference)：比较两个纹理并仅输出两者之间不同的像素。 应用它的一个例子是获得两个纹理（例如两个噪波）之…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-3F05BC30-9387-472F-9C78-B361C3267BF7.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

- 减淡(Dodge)：增加白色区域的曝光。将漫反射纹理与具有白色区域的纹理相结合，以亮显白色区域。

  使用此模式可**合并两个法线贴图**，如以下示例中所示。对于每个法线贴图，创建一个“Bump2d”节点，并将法线贴图的“输出 Alpha”(Out Alpha)连接到“Bump2d”节点的“凹凸值”(Bump Value)输入。将每个“Bump2d” “输出法线”(Out Normal)值连接到“颜色合成”(Color Composite)节点作为输入颜色。

  ![图：减淡(Dodge)：增加白色区域的曝光。将漫反射纹理与具有白色区域的纹理相结合，以亮显白色区域。 使用此模式可合并两个法…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-67476E21-209B-4FFD-A220-26783A215889.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

  ![图：减淡(Dodge)：增加白色区域的曝光。将漫反射纹理与具有白色区域的纹理相结合，以亮显白色区域。 使用此模式可合并两个法…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-CCD263CF-064C-460F-9D57-838078932F30.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

- 焚烧(Burn)：使黑色区域变暗。将漫反射纹理与具有黑色区域的纹理相结合，以使黑色区域变暗。

## 数学颜色

使用该节点可将输入结合在一起。此节点类似于“颜色合成”(Color Composite)节点，但是进行了简化，而且可选择数学运算。

## 颜色校正

将输入纹理连接到此节点，以更正其颜色和/或 Alpha 值。例如，可以调整饱和度或颜色对比度，调整 Alpha 增益和偏移，以及钳制颜色或 Alpha 通道。颜色和 Alpha 是独立的输入，可以单独调整。

“颜色校正”(Color Correct)节点使您可以试验各种不同的颜色校正设置。例如，可以创建一个“文件”(File)节点，然后将其连接到三个“颜色校正”(Color Correct)节点，且每个节点都具有不同的颜色校正设置，您可以轻松地在这些设置之间切换以找到最适合您的效果。同时，您也可以将同一“文件”(File)节点连接到节点网络的另一部分，而无需执行任何颜色校正。如果您的纹理文件发生更改，则只需调整一个“文件”(File)节点的文件路径。

在此示例中，您可以在红色、绿色和蓝色颜色校正之前进行切换，只需将 Blinn 颜色输入重新连接到其他颜色校正输出。也可以将相同的文件纹理（不进行任何颜色校正）连接到着色器网络的另一个部分。

另一方面，如果通过调整“文件”(File)节点上的“颜色平衡”(Color Balance)属性来执行颜色校正，则必须通过三组颜色设置来创建三个“文件”(File)节点，以完成相同的目标。如果纹理文件发生更改，必须调整三个文件节点的文件路径。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-B0B6F8AD-896F-4BA3-A33A-510E207C2D20.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

## 恒定颜色

使用该节点可以输出一个简单的实体颜色，用于您的着色图表。

使用该节点可按程序控制着色图表的多个方面，并且轻松调整和控制着色器。应用示例包括：

- 作为“单一噪波”(Simplex Noise)的“扭曲 U”(Distortion U)和“扭曲 V”(Distortion V)属性的输入，用于扭曲噪波图案

- 作为合并两个程序纹理的“融合颜色”(Blend Colors)节点的“融合器”(Blender)属性输入

在此示例中，“恒定颜色”(Color Constant)提供纯绿色，其可以与“单一噪波”(Simplex Noise)结合以创建绿色蜥蜴蒙皮图案。您只需调整“恒定颜色”(Color Constant)节点，即可轻松更改蒙皮的颜色，同时保持图案不变。使用单独的节点设置蒙皮颜色，使您可以轻松查找和更改颜色，以及将其连接到多个节点以进行程序控制。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-B3774078-B75C-4A9C-81FD-79FC33705DCF.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

在此示例中，“恒定颜色”(Color Constant)连接到输出其红色通道的“通道”(Channels)节点。此红色通道连接到三个不同的“颜色校正”(Color Correct)节点，每个节点都有不同的“Alpha 增益”(Alpha Gain)值，该值作为乘数用于控制“单一噪波”(Simplex Noise)节点上的三个不同属性：“比例”(Scale)、“频率”(Frequency)和“频率比”(Frequency Ratio)。红色通道也可以直接控制噪波节点的“振幅”(Amplitude)。此噪波节点控制 Blinn 着色器的凹凸。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-FAC7FEC5-D046-44DB-BC6B-E729734831D0.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-D6E389B7-5FED-4EAD-992A-1A8437F0C553.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

若要调整凹凸效果，您只需要调整“恒定颜色”(Color Constant)。此示例演示了通过将单个节点连接到不同的乘数，从而调整多个效果。

在调整“恒定颜色”(Color Constant)时，观察“单一噪波”(Simplex Noise)上的效果。

## 颜色遮罩

连接输入颜色或纹理以及作为 Alpha 遮罩的纹理，以生成遮罩的输出。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-932C05DD-1123-4BB8-93E5-F8FA358E654F.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

叶纹理由 www.cgtextures.com 提供。

应用它的一个例子是使用“颜色合成”(Color Composite)节点在漫反射纹理上分层“颜色遮罩”(Color Mask)结果。

## 通道(Channels)

将纹理节点作为输入连接到“通道”(Channels)节点，然后使用该节点重新关联其输出中的 RGBA 通道。例如，通过将任何通道 R/G/B 设置为 A，在任何 RGB 通道中输出 Alpha。

您也可以使用此节点来修改遮罩。例如，在使用红色、绿色和蓝色遮罩纹理不同区域的绘制应用程序中绘制纹理贴图：绿色用于遮罩衬衫，红色用于遮罩帽子，蓝色用于遮罩运动鞋。若要输出仅包含帽子和衬衫的纹理，请创建一个“通道”(Channels)节点，并将“通道 A”(Channel A)设置为“R”以输出红色通道，然后创建第二个“通道”(Channels)节点并将“通道 A”(Channel A)设置为“G”，以输出绿色通道，然后创建一个“颜色合成”(Color Composite)节点来添加两个 Alpha 通道。

## 预乘(Premultiply)

将输入颜色 RGB 通道乘以“Alpha”值。将输入纹理连接到“颜色”(Color)属性，并将具有 Alpha 通道的纹理连接到“Alpha”属性。Alpha 通道中的所有黑色像素都将在输出中变为黑色，并且 Alpha 通道中的所有白色像素都使输入纹理保持不变。

## 取消预乘(Unpremultiply)

将输入颜色除以“Alpha”值。连接预乘图像作为输入纹理并使用该节点反转预乘。

例如，您可能希望先取消预乘图像，然后再执行一组颜色校正，随后再次预乘以便不会意外对任何透明 Alpha 边进行颜色校正。

在此示例中，已预乘纹理图像。因此，必须先取消预乘其颜色通道，然后才可钳制其值，并随后再次相乘。相同的 Alpha 输出（从纹理图像）将输入到“取消预乘”(Unpremultiply)和“预乘”(Premultiply)节点。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-8B68D194-4EB1-4A68-87CC-1EBD7BB8110A.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

## 颜色逻辑

此节点会使用各种等式运算符（如 <= 或 !=）比较“颜色 A”(Color A)和“颜色 B”(Color B)=. 如果比较返回 true 结果，它始终输出布尔值：1（白色），如果比较返回 false 结果，则值为 0（黑色）。

“颜色逻辑”(Color Logic)和“颜色条件”(Color Condition)通常彼此结合使用。

在此示例中，“颜色逻辑”(Color Logic)比较两个输入值是否相等。如果它们相等，则使用“颜色 A”(Color A)提供用于“表面着色器”(Surface Shader)的颜色。否则，使用“颜色 B”(Color B)。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-03E43A6D-A5DE-4AAC-BAD7-5AA4C2B61F28.png) <!-- baize:img-hook downloaded=false reason="正文 4116 字 ≥300，非承重" -->

## 颜色条件

如果条件为 true，则使用“颜色 A”(Color A)。否则，使用“颜色 B”(Color B)。
