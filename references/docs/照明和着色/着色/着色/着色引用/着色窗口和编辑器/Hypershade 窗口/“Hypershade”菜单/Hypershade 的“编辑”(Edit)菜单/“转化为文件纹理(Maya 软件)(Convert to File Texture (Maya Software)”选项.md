# “转化为文件纹理(Maya 软件)(Convert to File Texture (Maya Software)”选项

在“Hypershade”菜单中选择“编辑 > 转化为文件纹理(Maya 软件)”(Edit > Convert to File Texture (Maya Software)) > ![图：在“Hypershade”菜单中选择“编辑 转化为文件纹理(Maya 软件)”(Edit Convert to File…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2467 字 ≥300，非承重" -->，以设定以下选项。

**注**

若要使“转化为文件纹理”(Convert to File Texture)针对多边形对象可正常使用，则多边形必须具有 (UV) 值和跨曲面的唯一 (UV) 值。否则，可能得不到预期结果。

#### 抗锯齿(Anti-alias)

如果启用，则实体纹理中的锐边和锯齿状边会被模糊化或抗锯齿化。

### 背景模式(Background Mode)

在将文件转换为纹理时，有时会丢失纹理边缘的一些像素。因此，几何体的某些部分未被合理覆盖而使背景色穿透显示。“背景模式”(Background Mode)下拉列表中有三个选项可用于管理此情况。

#### 着色器默认值(Shader Default)

为背景应用默认颜色。此颜色可以是着色器颜色的融合。此选项旨在与先前版本 Maya 兼容。这是默认设置。

#### 自定义颜色(Custom Color)

使用“背景色”(Background Color)字段指定用于背景的颜色。例如，如果要将文件纹理导入图像编辑软件并需要特殊关键帧（颜色）来选择要处理的背景，则该功能非常有用。

#### 延伸边颜色(Extend Edge Color)

依据相邻像素的颜色确定用于在边处延伸纹理图案的适当背景色。此选项在某些情况下可提供最佳质量。

**注**

提示：

在“硬件纹理显示选项”(Hardware Texture Display Options)窗口中，将“纹理过滤器”(Texture Filter)选项设定为已过滤的方法，以获得最佳质量。将“纹理过滤器”(Texture Filter)选项设定为“未过滤”(Unfiltered)以查看潜在的瑕疵。

#### 填充纹理接缝(Fill Texture Seams)

如果选定的 UV 空间包含边界，则这些边界在使用烘焙纹理的渲染中可能显示为黑色条纹。如果对纹理进行采样时距离边界太近，导致过滤器从所需空间外部拾取值（通常为黑色），则会发生这种情况。

该设置通过以人工方式精细地延伸边界，缓解了上述问题。它是以 texel（纹素）为单位。通常，该过滤器的直径仅为几 texel，在这些边界空间中只能达到其半径以内的范围，因此值为 1 或 2 通常已足够。

**注**

“转化为文件纹理”(Convert to File Texture)算法默认由两个过程组成。第一个过程从三角形的内部进行颜色取样；第二个过程沿多边形边界向各个方向略微延伸已采样的颜色以填充纹理的接缝。游戏开发者或其他没有时间进行过扫描的用户，可以通过禁用“填充纹理接缝”(Fill Texture Seams)属性禁用第二个过程。

#### 烘焙着色组照明(Bake Shading Group Lighting)

当将纹理或材质转换为图像文件时，将照亮选定曲面的灯光烘焙为新的图像文件。新图像文件由场景中链接到曲面的相同灯光照亮。（此选项是进行颜色匹配的理想选择。）

#### 使用虚拟平面烘焙(Bake Using Virtual Plane)

通过此选项，可以不用基于对象的 UV 剪裁图像，即可合理地为分层着色器或其他非直接支持的着色网络创建图像贴图。此选项使用 UV 为从 0,0 到 1,1 正方形的虚拟平面烘焙出一个示例图像。

#### 烘焙阴影(Bake Shadows)

指定烘焙照明时是否计算阴影。使用基于磁盘的阴影贴图。仅使用启用了有深度贴图阴影的灯光（灯光的“属性编辑器”(Attribute Editor)中的“使用深度贴图阴影”(Use Depth Map Shadows)）。

#### 烘焙透明度(Bake Transparency)

指定烘焙照明时是否计算透明度。烘焙透明度会针对着色网络的颜色和透明度采样 — Maya 将文件纹理的 Alpha 通道设定为与采样的透明度结果相对应。默认情况下不会计算透明度。

#### 双面(Double Sided)

烘焙照明或阴影时请禁用此选项。如果启用，则采样着色网络时所需的法线将翻转为面向摄影机。（烘焙着色网络照明时可使用此选项来照亮曲面的两侧）。

**注**

启用“双面”(Double Sided)会使转换依赖于摄影机，而在某些情况下并不需要摄影机，尤其是在使用烘焙照明和阴影时。

### UV 范围(UV Range)

指定在 UV 空间中要采样的曲面的量。例如，如果选择多边形对象的一个或多个面，而不是采样整个曲面，则仅针对选定的面进行采样。

**注**

“UV 范围”(UV Range)可以与选定的多边形面结合使用。

#### 默认(Default)

对于 NURBS 曲面，Maya 会采样整个曲面。对于多边形和细分曲面，Maya 会针对从 [0,0] 到 [1,1] 的区域采样。

#### 整个范围(Entire Range)

针对整个曲面采样（例如，针对多边形立方体是从 [-1,0] 到 [2,4] 采样）。这时会创建一个 place2dTexture 节点并连接到文件纹理。

#### 用户指定(User Specified)

启用此选项以启用“U 最小值/最 值”(U Min/M x)和“V 最小值/最大值”(V Min/Ma)选项（参见下节）这时会创建一个 place2dTexture 节点并连接到文件纹理。

#### U 最小值/最大值(U Min/Max)、V 最小值/最大值(V Min/Max)

滑块值指定 U 或 V 组件采样范围的拉伸程度。Maya 会在 [0,0] 到 [1,1] 采样范围内拉伸采样区域以适合输出图像大小。

#### X 分辨率(X Resolution)、Y 分辨率(Y Resolution)

图像文件的水平和垂直分辨率以像素为测量单位。默认值为 256。

#### 文件格式(File Format)

允许您选择保存文件纹理的格式。

可用的图像格式包括：

- Alias PIX(als)

- Cineon (cin)

- DDS (dds)

- EPS (eps)

- GIF (gif)

- JPEG (jpg)

- Maya IFF (iff)

- PSD (psd)

- PNG (png)

- RLA (rla)

- SGI (sgi)

- Avid ® Softimage ® (pic)

- Targa (Tga)

- TIff (tif)

- Tiff16 (tif)

- Windows 位图(bmp)(Windows Bitmap (bmp))

- Sony Playstation ® (tim)
