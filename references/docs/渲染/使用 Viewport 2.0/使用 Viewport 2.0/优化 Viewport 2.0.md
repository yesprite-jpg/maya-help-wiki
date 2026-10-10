# 优化 Viewport 2.0

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 2511 字 ≥300，非承重" -->

## 优化场景复杂度

使用以下准则作为优化 Viewport 2.0 的方法，尤其是当场景包含大量对象、包括高分辨率纹理时，或者需要同时运行使用大量 GPU 内存的其他应用程序时。

### 启用“GPU 实例化”(GPU Instancing)

“GPU 实例化”(GPU Instancing)功能使用硬件实例化，渲染使用相同材质的 Maya 形状的大量实例。 这将减轻显卡的计算负荷，并显著改善包含海量几何体或已缓存动画（无法装入 GPU 内存）的场景的性能。

### 合并世界(Consolidate World)

“合并世界”(Consolidate World)通过组合摄影机视图中几何体的所有对象来减少显卡的调用次数，从而提高性能。 此选项默认处于启用状态。

为了优化“合并世界”(Consolidate World)功能，需要尽可能重用类似的着色器（特别是对小型静态对象）。 可以通过选择“文件 > 优化场景大小”(File > Optimize Scene Size) > ![图：为了优化“合并世界”(Consolidate World)功能，需要尽可能重用类似的着色器（特别是对小型静态对象）。 可…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2511 字 ≥300，非承重" --> 并启用“移除重复项: 着色网络”(Remove duplicate: Shading networks)选项来完成该操作。 要充分利用合并，需要在[“面板”(Panel)菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C6188583-EA9E-4880-AAE7-8D895FD94DD6)中选择“着色”(Shading) > “使用默认材质”(Use Default Material)，以便在视口中自动使用单一材质。 如果材质对工作流来说不重要，则此举会大大提高慢场景的性能。

**注**

启用

“合并世界”(Consolidate World)

会增加显卡内存。 有关详细信息，请参见

管理 Viewport 2.0 的 GPU 内存

。

### 使用“Alpha 切割”(Alpha Cut)透明度

在 [Viewport 2.0 选项(Viewport 2.0 options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9BBB6035-2A02-41BB-AF2D-99D9BEE580F1#GUID-9BBB6035-2A02-41BB-AF2D-99D9BEE580F1__GUID-02951C60-4673-47BC-A8C1-390A1EC659B7)中，选择“Alpha 切割 透明度算法”(Alpha Cut > Transparency Algorithm)。 此选项可提供高质量的透明度，而不会影响性能。 “Alpha 切割”(Alpha Cut)非常适合完全透明或不透明的对象。

### 减少纹理使用的内存

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 2511 字 ≥300，非承重" -->

要减少高分辨率纹理使用的内存量，需要启用[“Viewport 2.0 选项”(Viewport 2.0 Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9BBB6035-2A02-41BB-AF2D-99D9BEE580F1#GUID-9BBB6035-2A02-41BB-AF2D-99D9BEE580F1__GUID-02951C60-4673-47BC-A8C1-390A1EC659B7)中的“钳制纹理分辨率”(Clamp Texture Resolution)。 将它设置为“自动”(Automatic)可允许 Maya 自动对纹理进行缩减采样以节省内存，或者您可以将它设置为“自定义”(Custom)并设置特定的最大分辨率。然后，Maya 将对最大分辨率以上的任何用户纹理进行缩减采样。

### 使用平滑网格预览

要获得更快的性能，请使用“平滑网格预览”(Smooth Mesh Preview)，而非平滑网格变形器。 请注意，在实时着色器（如 GLSL 或 HLSL 着色器）中启用细分时，这些改进效果将减弱。

### 管理视口效果

同时使用以下所有功能时性能可能下降：

- 启用多采样抗锯齿(Multisample Anti-aliasing Enable)

- 屏幕空间环境光遮挡(Screen-space Ambient Occlusion)

- 浮点渲染目标(Floating Point Render Target)

禁用阴影可以改善这些下降。 通常，启用这些选项可提高显示质量，而禁用它们可提高性能。

### 暂停 Viewport 2.0

若要缩短复杂场景的加载时间，请在“首选项”(Preference)窗口的“显示”(Display)类别中启用“暂停 Viewport 2.0 (启动)”(Pause Viewport 2.0 (startup))选项。 这允许您在场景中进行更改，而不必等待视口更新。 也可以单击状态行中的 ![图：若要缩短复杂场景的加载时间，请在“首选项”(Preference)窗口的“显示”(Display)类别中启用“暂停 Vi…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-A856707B-0550-4DFA-AEB1-590B0FF7D219.png) <!-- baize:img-hook downloaded=false reason="正文 2511 字 ≥300，非承重" --> 图标来暂停 Viewport 2.0。

## 优化 GPU 内存使用

预览包含大量纹理、几何体或缓存动画的场景时，必须管理 Viewport 2.0 使用的内存量。 请参见[管理 Viewport 2.0 的 GPU 内存](管理%20Viewport%202.0%20的%20GPU%20内存.md)。

## 动画的优化

- 不使用 Alpha 融合时 HumanIK 的渲染速度更快。

- 缓存图像序列时，如果具有两个序列，每个序列具有不同的帧数，则应该将这两个序列的缓存设置为与时间轴的缓存相同的帧数。

  可以在属性编辑器的“交互式序列缓存选项”(Interactive Sequence Caching Options)部分中设置文件节点的序列缓存。 对于图像平面，可以通过在 imagePlaneShape 属性编辑器的“帧缓存”(Frame Cache)属性中设置帧数来设置缓存。

## 着色器和纹理优化

### DirectX 11 着色器

- 在使用 DirectX 11 AutodeskUberShader 时，默认情况下启用 Mipmap 生成，从而为较远对象提供更好的纹理质量。 您可以禁用 Mipmap 生成以提高性能；但对于较远纹理，您可能会看到云纹图案。 在 <maya 目录>\presets\HLSL11\examples\AutodeskUberShader.fxo 文件中，设置 #define NumberOfMipMaps 1。

- dx11Shader 节点支持未编译 (.fx) 和已编译 (.fxo) 效果。 对于大型场景和复杂着色器，仅使用已编译效果。

### 纹理

- 不受支持的纹理类型烘焙在 Viewport 2.0 内部进行。为了提高性能，请避免使用不受支持的纹理（请参见 [Viewport 2.0 限制](Viewport%202.0%20限制.md)）。

  如果场景包含 Viewport 2.0 本身不支持的 3D 纹理，则可以通过在 [Viewport 2.0 选项(Viewport 2.0 options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9BBB6035-2A02-41BB-AF2D-99D9BEE580F1#GUID-9BBB6035-2A02-41BB-AF2D-99D9BEE580F1__GUID-02951C60-4673-47BC-A8C1-390A1EC659B7)的“不支持的纹理类型的烘焙分辨率”(Bake Resolution for Unsupported Texture Types)设置中使用低烘焙分辨率值，减少这些纹理的烘焙时间。

  请参见[Viewport 2.0 的内部纹理烘焙](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-71E00045-A4F6-49CB-9D59-16FBC027D819)。

- 纹理尺寸不一定必须是 2 的幂（即，256、512、1024），也不一定必须为方形。 尺寸为 2 的幂的纹理不一定提供任何性能优势。

## 其他优化提示

### 使用 particleSamplerInfo 节点

使用 particleSamplerInfo 节点时，为了获得最佳性能，应从粒子采样器断开不需要的每粒子属性，并仅保留所需的每粒子属性。 如果需要大量每粒子属性，请使用 DirectX 11 作为渲染引擎，而不是 OpenGL。 如果您必须使用 OpenGL，也可以使用高端显卡来增加顶点纹理坐标计数。

## 相关主题

- [Viewport 2.0 疑难解答](Viewport%202.0%20疑难解答.md)
