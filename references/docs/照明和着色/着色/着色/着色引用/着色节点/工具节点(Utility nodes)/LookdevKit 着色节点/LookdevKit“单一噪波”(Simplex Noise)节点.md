# LookdevKit“单一噪波”(Simplex Noise)节点

lookdevKit 插件提供了“单一噪波”(Simplex Noise)节点，以及一组在“Hypershade”中创建程序网络时最有用的数学和工具节点。

要创建“单一噪波”(Simplex Noise)节点，请确保已在“插件管理器”(Plug-in Manager)（“窗口 > 设置/首选项”(Windows > Settings/Preferences)）中启用 lookdevKit.mll 插件。

有关您可以使用此插件创建其他节点的信息，请参见 [LookdevKit 着色节点](../LookdevKit%20着色节点.md)。

此节点创建程序噪波。从三种噪波图案中选择：

- “分形”(Fractal)：类似于“分形”(Fractal) 2D 纹理，但从不会平铺瑕疵，且可快速求值。对于纹理、污垢和地形效果十分有用。

- “细胞”(Cellular)：可用于创建虚线图案，例如：蜂巢、毛孔、蜥蜴皮等。

- “隆起”(Ridged)：可用于创建具有辉光、纹理图案或地形侵蚀效果的电力或照明效果。

通过调整 place2DTexture 节点上的“UV 向重复”(Repeat UV)属性或噪波节点上的“比例”(Scale)属性，可以重复噪波图案。可以重复此节点，而不带任何平铺瑕疵。

通过将单一颜色通道连接到“扭曲 U”(Distortion U)和“扭曲 V”(Distortion V)输入，可以扭曲噪波。此外，您还可以使用一个噪波扭曲另一个噪波。请参见以下其他示例。

此节点可以连接到“渐变”(Ramp)纹理节点的“UV 坐标”(Uv Coord)输入，使用噪波值帮助选择渐变颜色。

## 样例应用程序

您可以将噪波节点组合并分层。例如，您可以按如下所示执行：

- 创建“颜色合成”(Color Composite)节点，以便使用“混合”(Mix) “操作”(Operation)组合两个“单一噪波”(Simplex Noise)节点，并使用“因子”(Factor)属性调整效果强度。

  使用一个噪波扭曲另一噪波。创建两个“单一噪波”(Simplex Noise)节点，然后将 simplexNoise1 的“输出颜色”(Out Color R)输出到 simplexNoise2 的“扭曲 U”(Distortion U)和“扭曲 V”(Distortion V)输入。

  创建第三个“单一噪波”(Simplex Noise)，并将其 “输出颜色”(Out Color R)输出连接到 simplexNoise2 的“扭曲比”(Distortion Ratio)输入。

  通过组合各种噪波节点，可以创建不规则图像，生成更自然的图案。

  **注**

  若要使用一个噪波扭曲另一噪波，必须将

  “输出颜色”(Out Color R)

  或

  “输出 Alpha”(Out Alpha)

  连接到

  “扭曲 U”(Distortion U)

  和

  “扭曲 V”(Distortion V)

  。

## 示例着色器网络：熔岩

以下着色器网络创建熔岩材质并使用以下 Lookdevkit 节点：

- 单一噪波

- 颜色恒定

- 颜色合成

- 颜色修正

**注**

本示例中使用了来自第三方渲染器 mental ray 的 mia_material_x_passes 着色器（NVIDIA 供图）。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-BF828B16-7227-482C-8DDA-A3592B14A18E.png) <!-- baize:img-hook downloaded=false reason="正文 3352 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-79E72135-8968-4995-BACE-279D3C19A15E.png) <!-- baize:img-hook downloaded=false reason="正文 3352 字 ≥300，非承重" -->

### 漫反射

要创建漫反射颜色，则需创建“单一噪波”(Simplex Noise)，且使用其“输出颜色”(Out Color R)通道驱动另一“单一噪波”(Simplex Noise)的“扭曲 U”(Distortion U)和“扭曲 V”(Distortion U)，而“颜色恒定”(Color Constant)的 Alpha 通道则驱动两个噪波的“缩放”(Scale)属性。使用一个噪波节点扭曲另一个噪波节点时，将创建更有机、更逼真的图案，而使用一个“颜色恒定”(Color Constant)驱动两个“比例”(Scale)时，则意味着您可以少考虑一项控制。“缩放”(Scale)属性确定噪波图案的重复频率。

稍后，第二个噪波的结果连接到“渐变”(Ramp)的“UV 坐标”(Uv Coord)，使用噪波值帮助选择渐变颜色。“渐变”(Ramp)颜色值均设置为大于 1 时，将产生照明效果，模拟现实生活中的熔岩。此“渐变”(Ramp)结果用作 mia_material_x_passes 着色器的漫反射颜色。

### 凹凸和置换

通过使用“颜色合成”(Color Composite)节点创建第一个和第二个噪波节点，可以创建更复杂的凹凸效果。红色通道用于创建凹凸图案。系统将创建“通道”(Channels)节点，其中“Alpha”通道将输出“红色”(Red)通道。此节点十分方便，因为它允许您使用颜色输出，而不是 Alpha。稍后，此“Alpha”输出通过 bump2D 节点用作 mia_material_x_passes 着色器的“总体凹凸”(Overall Bump)。

要为熔岩材质创建逼真的置换，则渐变的黑色区域（表示冷却的熔岩岩石）应为曲面的最高部分。因此，“渐变”(Ramp)输出将使用“反转”(Reverse)节点反转，以便黑色区域为曲面的最高点，并作为置换材质连接到 mia_material_x_passes 着色器。

### 反射率

若要添加逼真的熔岩，则应反射其黑色区域，因为它是冷熔岩岩石。与创建位移类似，在这种情况下再次使用“渐变”(Ramp)反转输出。若要为高光添加其他关注区域，则应使用“颜色合成”(Color Composite)节点将它乘以另一个“单一噪波”(Simplex Noise)。反光对象（如金属）的镜面反射度具有密集噪波图案，且“单一噪波”(Simplex Noise)允许您通过调整“缩放”(Scale)属性创建该图案，而不是使用平铺瑕疵。“颜色合成”(Color Composite)节点的 Alpha 输出是 mia_material_x_passes 着色器的“反射率”(Reflectivity)属性的输入。

### 辉光

要添加其他辉光，则使用“颜色修正”(Color Correct)节点使“渐变”(Ramp)结果变暗，且将其作为输入连接到 mia_material_x_passes 着色器的“其他颜色”(Additional Color)属性。使用附加的“颜色修正”(Color Correct)节点，您可以仅将输出着色器的辉光程度变暗，而不会将任何其他对象变暗。相反，如果已更改渐变颜色，则所有其他属性（“漫反射”(Diffuse)和“反射”(Reflectivity)等）也会更改。

### 透明度

同样，您可以创建“颜色修正”(Color Correct)节点，以便仅调整“透明度”(Transparency)属性。将“渐变”(Ramp)输出连接到“颜色修正”(Color Correct)节点，然后将“颜色修正”(Color Correct)节点的“输出颜色 R”(Out Color R)属性连接到 mia_material_x_passes 着色器的“透明度”(Transparency)输入。

### 程序

完整着色器网络由噪波节点控制。要更改熔岩图案，更改“单一噪波”(Simplex Noise)的噪波类型，且所有下游节点更新为结果。

通过调整“颜色恒定”(Color Constant)的“Alpha”值更改熔岩图案的密度，所有后续结果将自动更新。现在，您可以通过更改一个或两个节点（而不是整个着色器网络）修改熔岩图案。

## 示例着色器网络：塑料

在此示例中，逼真的塑料灰色材质是通过使用“单一噪波”(Simplex Noise)节点创建凹凸图案的方式创建的。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-39E72ECA-FEFB-4D0C-B095-F713863C22C6.png) <!-- baize:img-hook downloaded=false reason="正文 3352 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-B89F2AE2-8CA0-4255-B966-6A6E9C96E345.png) <!-- baize:img-hook downloaded=false reason="正文 3352 字 ≥300，非承重" -->

“单一噪波”(Simplex Noise)节点连接到“颜色修正”(Color Correct)节点。“颜色修正”(Color Correct)的输出是“通道”(Channels)节点，它会将红色通道作为 Alpha（“通道”(Channels)设置为“R”）输出。此 Alpha 输出值用作“Blinn”着色器的凹凸贴图。

要调整凹凸深度，请调整“颜色修正”(Color Correct)的“颜色增益”(Color Gain)。使用此网络，您可以通过在“单一噪波”(Simplex Noise)的“输出颜色”(Out Color)和“凹凸 2D”(Bump 2D)节点之间插入“颜色修正”(Color Correct)节点，使凹凸输入与镜面反射输入分开，从而精确控制着色器中的凹凸程度。否则，您对“凹凸”(Bump)属性所做的任何调整也适用于“镜面反射”(Specular)属性。
