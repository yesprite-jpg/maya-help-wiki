# Maya 旧版视口

不再支持 Maya 旧版视口。所提供的以下信息仅用于参考。本主题包含三个部分：

- Maya 硬件渲染器

- 旧版视口选项

- 面板菜单：“渲染器”(Renderer)

## Maya 硬件渲染器

有关渲染设置的信息，请参见[“渲染设置”(Render Settings)窗口](渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)。

#### 质量(Quality)

有关渲染速度和图像质量的详细信息，请参见[质量、渲染速度、诊断￼](../../质量、渲染速度、诊断/质量、渲染速度、诊断.md)。

#### 预设(Presets)

使用这些设置可以基于给定质量、特定效果来渲染图像。

在较高的质量设置下，对象显示更平滑，但渲染时间可能会更长。在较低的质量设置下，对象可能会显示少量锯齿，但渲染速度越快。

#### 自定义(Custom)

用于独立指定硬件质量设置。

#### 预览质量(Preview quality)

“采样数”(Number Of Samples)设定为 1。“颜色分辨率”(Color resolution)设定为 128。“凹凸分辨率”(Bump resolution)设定为 256。

#### 中间质量(Intermediate quality)

“采样数”(Number Of Samples)设定为 1。“颜色分辨率”(Color resolution)设定为 256。“凹凸分辨率”(Bump resolution)设定为 512。

#### 产品级质量(Production quality)

“采样数”(Number Of Samples)设定为 9。“颜色分辨率”(Color resolution)设定为 512。“凹凸分辨率”(Bump resolution)设定为 1024。

#### 带透明度的产品级质量(Production quality with transparency)

“采样数”(Number Of Samples)设定为 9。“颜色分辨率”(Color resolution)设定为 512。“凹凸分辨率”(Bump resolution)设定为 1024。允许透明度。

#### 采样数(Number Of Samples)

可选择用于控制对象在渲染期间抗锯齿效果的每像素精确采样数。

对于软件渲染，首先在中心对每个像素进行采样，然后稍微偏离中心进行后续的采样。对于硬件渲染，则对中心的每个像素进行采样。对于后续的采样，将通过稍微偏移来重新渲染图像，并再次对中心的每个像素进行采样。然后对齐图像以生成最终图像。

#### 帧缓冲区格式(Frame buffer format)

帧缓冲区是一块视频内存，用于保存刷新视频显示（帧）所用的像素。从下拉列表中选择要使用的帧缓冲区类型：

- RGBA: 每通道 8 字节(RGBA: 8 bytes per channel)

- RGBA: 每通道 16 位浮点(RGBA: 16-bit float per channel)

  #### 透明阴影贴图(Transparent shadow maps)

  如果要使用透明阴影贴图，就要先启用它。

  #### 透明度排序(Transparency sorting)

  在渲染之前进行排序以提高透明度的方法。

  #### 每对象(Per object)

  从最远到最近距离对透明对象进行排序和绘制。该选项能够更快速地提供结果，但可能无法正确渲染复杂的透明对象。

  #### 每多边形(Per polygon)

  按照距查看器最远到最近的距离，对每个对象的多边形进行排序和绘制。该选项提供了更精确的透明度表示，但可能花费较长的处理时间。

  #### 颜色分辨率(Color resolution)

  如果硬件渲染无法直接对着色网络解算，着色网络将被烘焙为硬件渲染器可以使用的 2D 图像。该选项为材质上的支持映射颜色通道指定烘焙图像的尺度。支持的通道包括颜色、白炽度、环境光、反射的颜色和透明度。默认值为 128，表明所有烘焙颜色图像的尺度均为 128 x 128 像素。

  #### 凹凸分辨率(Bump resolution)

  如果硬件渲染无法直接对着色网络解算，着色网络将被烘焙为硬件渲染器可以使用的 2D 图像。该选项指定支持凹凸贴图的烘焙图像尺度，通常必须具有比映射颜色通道更高的分辨率。该选项的默认值为 256，表明所有烘焙凹凸图像的尺度均为 256 x 256 像素。

  #### 纹理压缩(Texture compression)

  #### 已禁用/已启用(Disabled/Enabled)

  纹理压缩可减少最多 75% 的内存使用量，并可改进绘制性能。所用的算法 (DXT5) 通常只产生很少量的压缩瑕疵，因此适用于各种纹理。

渲染选项(Render Options)

#### 消隐(Culling)

可控制用于渲染的消隐类型。

#### 每对象(Per object)

“消隐”(Culling)选项基于选定对象“属性编辑器”(Attribute Editor)的“渲染统计信息”(Render Stats)部分的每对象设置。当前选项为：

- 双面：使用对象上的当前法线渲染双面照明。

- 单面：使用对象上的当前法线渲染单面照明。

- 反向：使用对象上的反转法线渲染单面照明。

#### 所有双面(All Double Sided)

强制所有对象使用“所有双面”(All Double Sided)选项进行渲染，无论是否在对象上设定该选项。“所有单面”(All Single Sided)提供比“所有双面”(All Double Sided)更好的渲染性能。

#### 所有单面(All Single Sided)

强制所有对象使用选项进行渲染，无论是否在对象上设定该选项“所有单面”(All Singled Sided)。如果“反向”(Opposite)子选项处于启用状态，则使用该子选项。“所有单面”(All Single Sided)提供比“所有双面”(All Double Sided)更好的渲染性能。

小对象消隐阈值(Small object culling threshold)

如果该性能增强选项处于启用状态（默认），则不绘制小于指定阈值的不透明对象。

该选项提供了与场景视图的“高质量渲染”(High Quality Rendering)模式中的“遮挡消隐”(Occlusion Culling)选项相同的功能。

#### 图像大小的百分比(Percent of image size)

这是“小对象消隐”(Small Object Culling)选项的阈值子选项。提供的阈值是对象占输出图像的图像大小百分比。

如果一个对象的大小小于该百分比，就不会被绘制。大小以屏幕空间（相对于用于渲染的摄影机）中的像素为单位。默认百分比为 0%。

该选项将忽略仅用于图像输出的“视图 > 摄影机设置”(View->Camera Settings)选项（如“门”(Gate)和“填充”(Fill)选项）。

例如，若百分比 = 10.0，图像大小为 100 x 100（像素）。阈值（以像素为单位）为 100 x 100 * .10 = 1000 像素。如果某个对象的大小小于 1000 像素，就不会被绘制。

例如，若百分比 = 0.0，图像大小为 100 x 100（像素）。阈值（以像素为单位）为 100 x 100 * 0 = 0 像素。如果某个对象的大小小于 0 像素，就不会被绘制。当一个不透明对象完全挡住另一个对象（对于当前用于渲染的摄影机）时，就会发生这种情况。

#### 硬件几何缓存(Hardware geometry cache)

当显卡内存未被用于其他场合时，启用该设置以将几何体缓存到显卡。在某些情况下，这样做可以提高性能。如果要限制使用可用显卡内存的特定部分，可以将“最大缓存大小(MB)”(Maximum cache size (in MB))设置为最多 512 MB。

#### 硬件环境查找(Hardware Environment Lookup)

如果禁用该选项，则以与 Maya 软件渲染器相同的方式解释“环境球/环境立方体”(Env Ball/Env Cube)贴图。

启用以根据“Maya 硬件渲染器”(Maya Hardware Renderer)解释“环境球/环境立方体”(Env Ball/Env Cube)贴图。

#### 运动模糊(Motion blur)

如果该选项处于启用状态，可以更改“运动模糊帧数”(Motion Blur by Frame)选项和“曝光次数”(Number of Exposures)选项。

#### 运动模糊帧数(Motion blur by frame)

在硬件渲染器中，通过渲染时间方向的特定点场景，并将生成的采样渲染融合到单个图像来实现运动模糊。

模糊帧数代表从当前模糊的帧开始的绝对时间范围。这样可确定模糊的大致开始时间和结束时间。然后，根据“属性编辑器”(Attribute Editor)中的摄影机“摄影机快门角度”(Camera Shutter Angle)属性调整该时间范围。

#### 曝光数量(Number of exposures)

曝光次数将“运动模糊帧数”(Motion Blur by Frame)选项确定的以上时间范围分成时间方向的离散时刻，对整个场景进行重新渲染。最终图像是所有曝光的累积平均效果。因此，若要获得平滑模糊，需要更多的曝光次数。同样，对于运动轨迹，最好选择较少的曝光次数。

#### 启用几何体遮罩(Enable Geometry Mask)

用于硬件渲染。启用该选项后，不透明几何体对象将遮罩粒子对象，而且不绘制透明几何体。当通过软件渲染几何体合成粒子时，这个选项就非常有用。

#### 使用 Alpha 融合镜面反射(Blend Specular With Alpha)

启用该选项以避免镜面反射看上去像悬浮在曲面上方。启用该选项后，镜面反射将与 Alpha 相乘，由此产生的高光仅显示在不透明曲面而不是透明曲面上。

#### 阴影链接(Shadow linking)

可以缩短场景所需的渲染时间，采用的方法是链接灯光与曲面，以便只有指定的曲面包含在给定灯光的阴影（阴影链接）或照明（灯光链接）的计算中。

使用下拉列表从该选项的三个可用选项中选择一个：

- 阴影遵守阴影链接(Shadows obey shadow linking)

- 阴影遵守灯光链接(Shadows obey light linking)属性

- 阴影忽略链接(Shadows ignore linking)

场景中的阴影仅可以遵守灯光链接或阴影链接中的一个，而不能同时遵守二者。因此，必须确定要在场景中融入灯光链接还是阴影链接，并从下拉列表中进行相应的选择。

也可以使用默认设置（而不是遵守已创建链接）渲染场景的一部分。选择“阴影忽略链接”(Shadows Ignore Linking)，忽略使用阴影链接或灯光链接建立或断开的所有链接。

默认设置为“阴影遵守灯光链接”(Shadows Obey Light Linking)。

有关阴影链接的详细信息，请参见[阴影链接](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-604555C2-9853-46F7-A4DF-9908F8B75B25)。有关灯光链接的详细信息，请参见[灯光链接](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-08A2A23B-15DB-4F01-96F4-F5011DAE0322)。

## 旧版视口选项

选择“渲染器 > 旧版高质量视口”(Renderer > Legacy High Quality Viewport) > ![图：选择“渲染器 旧版高质量视口”(Renderer Legacy High Quality Viewport) ，以打开“…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5535 字 ≥300，非承重" -->，以打开“硬件渲染器显示选项”(Hardware Renderer Display Options)窗口设置这些选项。

### 显示质量(Display Quality)

#### 低质量照明(Low Quality Lighting)

低质量照明实质上就是逐顶点照明，仅在顶点上计算灯光，然后融合结果。渲染的速度较快，且质量非常高。

#### 匹配视口灯光(Match Viewport Lights)

启用该选项时，显卡支持多少灯光，便使用多少灯光（通常 8 个灯光）。

#### 透明阴影贴图(Transparent Shadow Maps)

完全透明的对象区域将不投射阴影。例如，如果将着色器（在对象上）的透明度通道映射到棋盘格纹理，那么对象的完全透明部分将不投射阴影。

### 显示参数(Display Parameters)

#### 遮挡消隐(Occlusion Culling)

该选项可提高具有许多对象的场景的性能，在此类场景中，可从活动摄影机的视点遮挡一个或多个对象。启用该选项时，该选项可通过阻止绘制看不见的对象来提高性能。

#### 消隐覆盖(Culling Override)

曲面上的每个位置都有法线，该法线指向被认为（为了消隐）是曲面的“前侧”的方向。

- 单面表示如果从灯光可以看到法线，那么灯光就会照明曲面。

- 双面表示在前端和后端照明曲面。

  #### 颜色纹理分辨率(Color Texture Resolution)

  如果硬件渲染不能处理图形硬件上的着色网络，那么会对着色网络解算，并将着色网络转化为硬件渲染器可以使用的文件纹理（2D 图像）。

  该选项指定结果纹理的尺度。受影响的通道为颜色、白炽度、环境、反射的颜色和透明度。默认值为 128，意味着任何已烘焙颜色图像的尺度均为 128 x 128 像素。

  #### 凹凸纹理分辨率(Bump Texture Resolution)

  如果硬件渲染无法直接处理图形硬件上的着色网络，那么会对着色网络解算，并将着色网络转化为硬件渲染器可以使用的文件纹理（2D 图像）。

  该选项指定结果纹理的尺度。该选项的默认值为 256，意味着任何已烘焙凹凸图像的尺度均为 256 x 256 像素。

## 面板菜单：“渲染器”(Renderer)

此 “渲染器”(Renderer) 菜单显示在场景视图之上，或者显示在具有多个场景视图的布局中每个视图面板之上。

选择“渲染器 > Viewport 2.0”(Renderer > Viewport 2.0) > ![图：选择“渲染器 Viewport 2.0”(Renderer Viewport 2.0) ，以设置 Viewport 2.…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5535 字 ≥300，非承重" -->，以设置 [Viewport 2.0 选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9BBB6035-2A02-41BB-AF2D-99D9BEE580F1)。

#### [自定义渲染器]

可以编写自己的插件，并使用创建的交互式渲染器覆盖场景视图渲染器。一旦通过“插件管理器”(Plug-in Manager)加载插件后，自定义渲染器的名称将显示在“渲染器面板”(Renderer Panel)菜单下（例如，“渲染器 > openGLViewport 渲染器”(Renderer > openGLViewport Renderer)）。如果选择加载多个自定义渲染器，则这些渲染器将按照加载顺序一一列出。

随 SDK 一起提供的还包括两个示例插件，其中一个用于“OpenGL”，另一个用于“Direct 3D”。（请注意，这两个示例插件尚未进行编译，需要先进行编译，才能通过“插件管理器”(Plug-in Manager)进行访问。）有关可用于创建这些插件的 API 类的更多详细信息，请参见 Maya 开发人员帮助。
