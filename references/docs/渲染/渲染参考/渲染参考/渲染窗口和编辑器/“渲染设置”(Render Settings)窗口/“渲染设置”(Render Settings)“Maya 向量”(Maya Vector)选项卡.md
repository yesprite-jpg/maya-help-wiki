# “渲染设置”(Render Settings):“Maya 向量”(Maya Vector)选项卡

若要选择渲染器以查看“Maya 向量”(Maya Vector)选项卡，请参见[选择渲染器](../../../../选择渲染器/选择渲染器.md)。应用到所有渲染器的“渲染设置”(Render Settings)包括在[“渲染设置: 公用”选项卡](“渲染设置”%28Render%20Settings%29“公用”%28Common%29选项卡.md)中。

有关渲染设置的信息，请参见 [Maya 矢量渲染器](../../../../选择渲染器/选择渲染器/Maya%20矢量渲染器.md)。

## 图像格式选项(Image Format Options)

#### 帧速率(Frame Rate)（仅限 SWF 和 SVG）

“Flash Player”文件或 SVG 文件的帧速率（以每秒帧数测量）。

#### Flash 版本(Flash Version)（仅限 SWF）

渲染的“Flash Player”文件的版本：Flash 3、Flash 4 或 Flash 5。渲染的“Flash Player”文件可在等于或高于该“Flash 版本”(Flash Version)的任意版本“Flash Player”中播放（并且可导入任意版本的 Flash 编写应用程序中）。

**注**

当“Flash 版本”(Flash Version)为 Flash 4 且“填充样式”(Fill Style)为“区域渐变”(Area Gradient)或“网格渐变”(Mesh Gradient)时，渲染动画在其开始处包含虚拟帧。（这是为了弥补 Flash 4 编写应用程序中的限制。）在将动画导入 Flash 4 编写应用程序中后，请删除该额外帧。

#### 在浏览器中打开(Open in Browser)（仅限 SWF）

在渲染向量图像或动画（使用“渲染 > 渲染当前帧”(Render > Render Current Frame)、“渲染 > 批渲染”(Render > Batch Render)或 mayaVectorRender）后将在默认浏览器中显示它们。

**注**

必须在您的系统上安装 Flash 浏览器插件，才能显示渲的染图像或动画。

#### 组合填充和边(Combine Fills and Edges)（仅限 SWF）

在启用“组合填充”(Combine Fills)和“边”(Edges)时，曲面的轮廓和填充是单个对象。如果将文件导入 Flash 编写应用程序中，则除非分开该对象，否则无法分离轮廓和填充。但是，渲染文件的大小小于禁用“组合填充”(Combine Fills)和“边”(Edges)时的大小。

在禁用“组合填充”(Combine Fills)“组合填充”和“边”(Edges)时，曲面的轮廓和填充是单独的对象。如果将文件导入 Flash 编写应用程序中，则可以分离轮廓和填充而不用分开该对象。但是，渲染文件的大小大于启用“组合填充”(Combine Fills)“组合填充”和“边”(Edges)时的大小。

#### “SVG 动画”(Svg Animation)（仅限 Svg）

如果“SVG 动画”(Svg Animation)是“自身”，则 Maya 会创建一个 SVG 文件，其中包含动画的帧和驱动动画的脚本。

如果“SVG 动画”(Svg Animation)是“HTML 脚本”，则 Maya 会创建一个 SVG 文件（其中包含动画的帧）以及一个 HTML 文件（其中包含驱动动画的 JavaScript）。

如果动画很长（大约 40 帧或更多），文件大小会在“SVG 动画”为“自身”时增加。

#### 压缩(Compress)（仅限 SVG）

使用“压缩”(Compress)命令可压缩渲染的 SVG 文件，这会显著减小其文件大小。

如果计划将 SVG 文件直接发布到 Web 上，可能需要启用“压缩”。如果计划将 SVG 文件导入另一个应用程序并对其进行编辑，请禁用“压缩”(Compress)。不能编辑压缩的 SVG 文件。

## 外观选项(Appearance Options)

#### 曲线容差(Curve Tolerance)

介于 0 到 15 之间的值，用于确定使用曲线或一系列直线段表示对象轮廓的方式。

当“曲线容差”(Curve Tolerance)为 0 时，对象轮廓由一系列直线段表示（每条多边形边对应一段）。这会生成与多边形的轮廓完全匹配的轮廓，但同时会生成较大的文件。

当“曲线容差”(Curve Tolerance)为 15 时，对象轮廓由曲线表示。这会生成看起来可能略微扭曲的轮廓（相对于原始对象的轮廓），但同时会生成较小的文件。

可能需要基于场景调整“曲线容差”(Curve Tolerance)设置，以在轮廓精确度和文件大小之间产生最佳折衷。首先将“曲线容差”(Curve Tolerance)设定为 7.5（默认设置）。如果渲染文件大小过大，请尝试增加“曲线容差”(Curve Tolerance)。如果对象轮廓出现扭曲，或在存在曲线式轮廓的位置动画表现为跳跃，请尝试减小“曲线容差”(Curve Tolerance)。

**注**

如果其他设置（例如，填充样式）是影响文件大小的主要因素，则调整“曲线容差”(Curve Tolerance)值可能对文件大小没有明显效果。

#### 二级曲线拟合(Secondary Curve Fitting)

通过添加次过程，可对线分段转化为曲线提供更多的控制。通常，这会导致更多线性分段转化为曲线。尽管该选项会增加渲染时间，但它有助于产生更好的效果和更小的文件。

#### 细节级别预设(Detail Level Preset)、细节级别(Detail Level)

确定渲染图像中的细节级别。与“低”(Low)细节级别 (10) 相比，“高”(High)细节级别 (30) 可生成更详细的图像和更精确的渲染，但渲染所需时间更长并会增加文件大小。（当细节级别为“低”(Low)时，将小多边形与相邻多边形组合使用。）

可能需要基于场景调整“细节级别”(Detail Level)，以在图像质量和文件大小之间产生最佳折衷。首先将“细节级别”(Detail Level)设定为“低”(Low)，并根据需增加该值以产生可接受的图像质量。

将“细节级别”(Detail Level)设定为“自动”(Automatic)可允许 Maya 为场景选择适当的细节级别。

将“细节级别”(Detail Level)设定为“自定义”(Custom)，然后使用数字字段或滑块将“细节级别”Detail Level)设定为介于 1 到 50 之间的任意值。（将“细节级别”(Detail Level)设定为 0 相当于选择“自动”(Automatic)预设。）

**注**

- 双击“细节级别”(Detail Level)值可将渲染图像中的细节程度增加一倍。

- 建议不要将“细节级别”(Detail Level)设定为小于 4 的值。

## 填充选项(Fill Options)

#### 填充对象(Fill Objects)

曲面基于“填充样式”(Fill Style)着色。若要将曲面渲染为未填充的轮廓，请禁用“填充对象”(Fill Objects)并启用“包括边”(Include Edges)。

#### 填充样式(Fill Style)

用于在渲染图像中填充曲面的着色样式。

对于所有填充样式（“单色”(Single Color)除外），填充颜色仅基于点光源的表面材质颜色和照明；将忽略所有其他类型的灯光。如果您的场景不包含点光源，将在渲染过程中自动创建默认点光源（位于摄影机处）（渲染后将移除该点光源）。

**注**

曲面填充将针对每帧重新进行计算，并可能在动画期间显示为更改、偏移或跳转。

#### 单色(Single Color)

基于表面材质颜色使用一种纯色填充每个曲面。

![图：基于表面材质颜色使用一种纯色填充每个曲面。 “单色”(Single Color)可以产生类似卡通的良好效果，特别是在模型…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-123F3A18-D079-420C-9507-CE005A2C5A69.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

“单色”(Single Color)可以产生类似卡通的良好效果，特别是在模型由单独的曲面（每个曲面具有不同的彩色材质）构成时。

**注**

“单色”(Single Color)填充颜色实际基于表面材质颜色和环境光（位于摄影机处），在渲染过程中会自动创建它们（在渲染后将移除它们）。因此，填充颜色可能并不与表面材质颜色完全匹配。填充颜色在动画期间不应更改。

**注**

提示：

为了更好地定义曲面边，请启用“边”(Edges)。

#### 双色(Two Color)

基于表面材质颜色和场景照明使用两种纯色填充每个曲面。

![图：基于表面材质颜色和场景照明使用两种纯色填充每个曲面。 与“单色”(Single Color)相比，“双色”(Two Co…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-BA42FE7B-2770-46DE-8B58-2122C7FEBCEE.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

与“单色”(Single Color)相比，“双色”(Two Color)产生的效果看上去 3D 效果略强，但同时会生成更大的文件。

**注**

提示：

对于由许多平坦平面组成的几何对象（例如，立方体），“双色”(Two Color)可能会产生外观不自然的结果（即，每个平面使用两种纯色填充）。对于此类对象，“平均颜色”(Average Color)通常更适用。

#### 四色(Four Color)

基于表面材质颜色和场景照明使用四种纯色填充每个曲面。

![图：基于表面材质颜色和场景照明使用四种纯色填充每个曲面。 与“双色”(Two Color)或“单色”(Single Colo…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-9A6B055F-3D2A-4234-B593-7454AE1B8E5A.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

与“双色”(Two Color)或“单色”(Single Color)相比，“四色”(Four Color)生成的结果看上去 3D 效果更强，但同时会生成更大的文件。

**注**

提示：

对于由许多平坦平面组成的几何对象（例如，立方体），“四色”(Four Color)可能会产生外观不自然的结果（即，每个平面使用四种纯色填充）。对于此类对象，“平均颜色”(Average Color)通常更适用。

#### 全色(Full Color)

基于表面材质颜色和场景照明使用一种纯色填充曲面上的每个多边形。

![图：基于表面材质颜色和场景照明使用一种纯色填充曲面上的每个多边形。 “全色”(Full Color)会生成逼真的 3D 效果…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-3039B7AC-5262-42B3-B422-989B8189F288.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

“全色”(Full Color)会生成逼真的 3D 效果，但同时会生成非常大的文件。（模型中的多边形数越多，文件大小越大。）

**注**

提示：

如果要生成高细节级别，且文件大小不是问题，“网格渐变”(Mesh Gradient)通常会产生比“全色”(Full Color)更好的效果。

**注**

在渲染为 AI 和 EPS 格式时，“全色”(Full Color)是可用的最高质量的填充样式。

#### 平均颜色(Average Color)

基于表面材质颜色和场景照明使用一种纯色填充每个曲面。

![图：基于表面材质颜色和场景照明使用一种纯色填充每个曲面。 提示： 对于划分为具有硬边的曲面的对象，“平均颜色”(Averag…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-D9E21FAC-B4A2-432E-8C87-F8AA5482C1EB.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

**注**

提示：

对于划分为具有硬边的曲面的对象，

“平均颜色”(Average Color)

通常会产生 3D 效果和适中文件大小的最佳组合，特别是在为对象设置动画时。

对于具有很少由硬边定义的曲面的平滑、交互式对象，“平均颜色”(Average Color)产生的效果通常不会优于“单色”(Single Color)。

#### “区域渐变”(Area Gradient)（仅限 SWF 和 SVG）

基于表面材质颜色和场景照明使用一种径向渐变填充每个曲面。

![图：基于表面材质颜色和场景照明使用一种径向渐变填充每个曲面。 “区域渐变”(Area Gradient)可以生成良好的 3D…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-E526BA92-DE3E-48E7-ADD1-9C8E63B5D1B9.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

“区域渐变”(Area Gradient)可以生成良好的 3D 效果，且文件大小的增加程度很小。

**注**

提示：

- 对于包含面式对象的场景（对象由许多清晰定义的曲面组成），“区域渐变”(Area Gradient)会产生非常理想的效果。

- 对于包含平面和平滑曲面的组合的场景，“区域渐变”(Area Gradient)会产生良好的填充平衡。平滑曲面使用渐变来填充，而平面使用更均匀的颜色来填写。

- 对于仅包含平滑曲面的场景，“区域渐变”(Area Gradient)会产生惊人数量的渐变填充。

**注**

该选项仅在“文件格式”(File Format)是 SWF 或 SVG 时可用。

#### “网格渐变”(Mesh Gradient)（仅限 SWF 和 SVG）

基于表面材质颜色和场景照明使用线性渐变填充曲面上的每个多边形。

![图：基于表面材质颜色和场景照明使用线性渐变填充曲面上的每个多边形。 “网格渐变”(Mesh Gradient)会生成非常逼真…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-D2E21103-E8FA-49FD-BF13-0D904B31C2F3.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

“网格渐变”(Mesh Gradient)会生成非常逼真的 3D 效果，但同时会生成非常大的文件。（模型中的多边形数越多，文件大小越大。）

在渲染为 SWF 和 SVG 格式时，“网格渐变”(Mesh Gradient)是可用的最高质量的填充样式。

**注**

在某些极少数情况下，当“填充样式”(Fill Style)为“网格渐变”(Mesh Gradient)时，着色可能不正确。例如，应用了渐变纹理的平面可使用纯色区域进行渲染。尝试对纹理进行非常细微的调整并重新渲染。

#### 显示背面(Show Back Faces)

渲染其法线背离摄影机的曲面时，就好像它们是面向摄影机的。在禁用“显示背面”(Show Back Faces)时，将不会渲染其法线背离摄影机的曲面。

**注**

其法线背离摄影机的曲面可能不可见，即使启用“显示背面”(Show Back Faces)也是如此（如果另一个曲面在它和摄影机之间）。

**注**

提示：

禁用“显示背面”(Show Back Faces)可能减少渲染时间并减小文件大小。

#### “阴影”(Shadows)（仅限 SWF 和位图格式）

将渲染对象阴影（仅基于场景中的阴影投影点光源）。阴影可以极大地增强 3D 效果。但是，阴影也会增加文件大小并显著增加渲染时间。

![图：将渲染对象阴影（仅基于场景中的阴影投影点光源）。阴影可以极大地增强 3D 效果。但是，阴影也会增加文件大小并显著增加渲染…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-AA7F254F-C924-49C2-BA32-3C3646D97134.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

当“阴影”(Shadows)处于启用状态时，将为所有对象渲染阴影。无法仅对某些对象渲染阴影（例如，通过禁用对象对应的“投射阴影”(Casts Shadows)或“接收阴影”(Receive Shadows)）。

仅在场景中存在阴影投射点光源（即，启用了“使用深度贴图阴影”(Use Depth Map Shadows)或“使用光线跟踪阴影”(Use Ray Trace Shadows)的点光源）时才渲染阴影。

**注**

- 无法设定阴影颜色。

- 阴影未投影到具有透明材质的曲面上。

#### “高光”(Highlights)（仅限 SWF 和位图格式）

将渲染镜面反射高光（仅基于场景中的点光源和表面材质光泽度）。（当“填充样式”(Fill Style)为“单色”(Single Color)时，镜面反射高光基于场景中点光源的位置。更改点光源的强度或颜色不会更改高光的外观。

![图：将渲染镜面反射高光（仅基于场景中的点光源和表面材质光泽度）。（当“填充样式”(Fill Style)为“单色”(Sing…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-2D29CB3C-D072-4FC5-AFD6-05994BA7DDA0.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

接近垂直于点光源的曲面的区域使用比曲面其余部分更亮的大量同心纯色区域填充（基于表面材质“镜面反射颜色”(Specular Color)和“高光级别”(Highlight Level)值）。

| 对于该材质... | 曲面光泽度仅基于... |
|---|---|
| 各向异性 | 粗糙度 |
| Blinn | 偏心率 |
| Phong | 余弦幂 |
| Phong E | 粗糙度 |

**注**

- 该选项仅在“填充样式”(Fill Style)为“单色”(Single Color)、“平均颜色”(Average Color)或“区域渐变”(Area Gradient)时可用。

- 仅当场景中具有启用了“发射镜面反射”(Emit Specular)的点光源时，才会渲染“高光”(Highlights)。

- 如果使用纹理映射表面材质的“镜面反射颜色”(Specular Color)，则高光的颜色基于纹理的“默认颜色”(Default Color)。如果使用工具节点映射表面材质的“镜面反射颜色”(Specular Color)，则高光的颜色为白色。

#### “高光级别”(Highlight Level)（仅限 SWF 和位图格式）

同心纯色区域的数量用于表示镜面反射高光。有效范围为 1 到 8。默认值为 4。

![图：同心纯色区域的数量用于表示镜面反射高光。有效范围为 1 到 8。默认值为 4。 注： 该选项只有在启用“高光”(High…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-12D49936-F099-4C93-9853-2F1DDB3B4F19.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

**注**

该选项只有在启用“高光”(Highlights)时才可用。

#### “反射”(Reflections)（仅限 SWF 和位图格式）

将渲染曲面反射（基于表面材质的反射率）。

![图：将渲染曲面反射（基于表面材质的反射率）。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-37478D9C-B6BD-45F4-B5CD-F70064F37F81.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

#### “反射深度”(Reflection Depth)（仅限 SWF 和位图格式）

某个曲面可与其他曲面交互反射的最大次数。有效范围为 1 到 4。默认值为 2。

**注**

该选项只有在启用“反射”(Reflections)时才可用。

## 边选项(Edge Options)

#### 包括边(Include Edges)

曲面边和轮廓渲染为轮廓。

![图：曲面边和轮廓渲染为轮廓。 提示： 若要将曲面渲染为未填充的轮廓，请禁用“填充对象”(Fill Objects)并启用“包…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-A7E7E5DC-9BF9-493B-BF65-0F338984F214.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

**注**

提示：

若要将曲面渲染为未填充的轮廓，请禁用“填充对象”(Fill Objects)并启用“包括边”(Include Edges)。

#### 边权重预设(Edge Weight Preset)、边权重(Edge Weight)

曲面轮廓的厚度（以点为单位测量）。

![图：曲面轮廓的厚度（以点为单位测量）。 注： 当“文件格式”(File Format)是 SWF 时，“边权重”(Edge …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-E680A805-65F7-4846-A464-C79C46FC52F7.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

**注**

当“文件格式”(File Format)是 SWF 时，“边权重”(Edge Weight)的更改小于 1 并不明显，除非放大轮廓。

#### 边样式(Edge Style)

当“边样式”(Edge Style)为“轮廓”(Outlines)时，曲面边和轮廓渲染为轮廓。（使用“细节边”(Detail Edges)也可将尖锐的多边形边渲染为轮廓。）

![图：当“边样式”(Edge Style)为“轮廓”(Outlines)时，曲面边和轮廓渲染为轮廓。（使用“细节边”(Deta…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-5CF94C28-72ED-41CA-BA56-690E6B025BBB.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

当“边样式”(Edge Style)为“整个网格”(Entire Mesh)时，多边形的所有边都会渲染为轮廓。“整个网格”(Entire Mesh)会生成非常大的文件。（模型中的多边形数越多，文件大小越大。）

#### 边颜色(Edge Color)

曲面轮廓的颜色。

#### 隐藏的边(Hidden Edges)

位于另一个曲面后的曲面边在渲染图像中可见。（这可能使某些对象看起来透明或使模型显示为线框）。

![图：位于另一个曲面后的曲面边在渲染图像中可见。（这可能使某些对象看起来透明或使模型显示为线框）。 “隐藏的边”(Hidden…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-855570D7-BAB4-4219-A30C-5E7C114A59A0.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

“隐藏的边”(Hidden Edges)会因额外向量信息而增加渲染文件大小。

**注**

提示：

如果要渲染具有许多多边形的模型，请避免启用“隐藏的边”(Hidden Edges)和将“边样式”(Edge Style)设定为“整个网格”(Entire Mesh) ；可能会在渲染图像中显示过多行。

#### 边细节(Edge Detail)

多边形之间的锐边渲染为轮廓。“最小边角度”(Min Edge Angle)控制哪些多边形边渲染为轮廓。

“边细节”(Edge Detail)可帮助定义 3D 对象的形状（尤其是在该对象由很少曲面组成时），但同时会生成更大的文件。

![图：多边形之间的锐边渲染为轮廓。“最小边角度”(Min Edge Angle)控制哪些多边形边渲染为轮廓。 “边细节”(Ed…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-0FFD5C45-9074-4E88-8936-B5E97712DC45.png) <!-- baize:img-hook downloaded=false reason="正文 7339 字 ≥300，非承重" -->

**注**

该选项仅在“边样式”(Edge Style)为“轮廓”(Outlines)时可用。

#### 在相交处绘制轮廓线(Outlines at Intersections)

启用该属性时，会沿两个对象相交的点显示一个轮廓。使用“边优先级”(Edge Priority)设置可解决边轮廓冲突（当深度不能自动执行该操作时）。该属性还位于材质的“属性编辑器”(Attribute Editor)的[矢量渲染控制](../../渲染节点/对象特定的“渲染”%28render%29属性%20-“属性编辑器”%28Attribute%20Editor%29/矢量渲染控制%28Vector%20Renderer%20Control%29.md)区域。

#### 最小边角度(Min Edge Angle)

确定在启用“边细节”(Edge Detail)时将哪些多边形边渲染为轮廓。“最小边角度”(Min Edge Angle)是两个相邻多边形的法线必须具有才能使其公用边渲染为轮廓的最小角度（以度为测量单位）。

减小“最小边角度”(Min Edge Angle)会因渲染文件中的额外向量信息而产生更大的文件。

**注**

该选项仅在“边样式”(Edge Style)为“轮廓”(Outlines)时可用。

## 渲染优化(Render Optimizations)

“渲染优化”(Render Optimization)设置指定矢量渲染器如何优化当前帧以减小文件大小。可以选择下列优化类型之一：

#### 安全(Safe)

移除高细节区域中的冗余几何体，尤其是在几何体只能通过在区域上放大才能显示时。冗余边出现在场景的可见和不可见区域的相交处，并始终可以安全地移除。

#### 良好(Good)

移除高细节区域中的冗余几何体，并移除不可见的子像素几何体，除非放大高细节区域。

#### 过度(Aggressive)

移除高细节区域中的冗余几何体、子像素几何体和略高于单像素级别的几何体。该设置最多可将文件大小减小 30%。

**注**

使用“过度”(Aggressive)优化可以直观检测缺失的几何体，而不用放大区域。这也可能会导致几何体不一致（如闭合的形状）。
