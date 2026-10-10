# “渲染设置”(Render Settings):“公用”(Common)选项卡

有关渲染设置的信息，请参见[“渲染设置”(Render Settings)窗口](../“渲染设置”%28Render%20Settings%29窗口.md)。

并非所有选项都可用于所有渲染器。

## 颜色管理

此部分可能存在，具体取决于您选择的渲染器。有关使用 Arnold 进行颜色管理的信息，请参见 [Arnold for Maya 用户手册](https://docs.arnoldrenderer.com/display/A5AFMUGCHS/Arnold+for+Maya+User+Guide)。

#### 应用输出变换(Apply Output Transform)

应用选定的“输出变换”(Output Transform)，以在渲染后从工作空间转化。通常，您应该：

- 如果您正在渲染将使用未相应地处理场景线性图像的查看软件显示的图像供预览，则启用此选项。

- 如果您正在渲染用于合成或需要场景线性颜色值的其他任务的最终图像，则禁用此选项。

请注意，当应用输出变换时，默认情况下“渲染视图”(Render View)仍将应用视图变换。在“渲染视图”(Render View)中禁用视图变换，以避免应用双重变换。

#### 输出变换(Output Transform)

选择要将渲染的图像转化到其中的颜色空间。渲染完成后，将应用变换以将图像从工作颜色空间转化为此处指定的空间。

## 文件输出(File Output)

渲染图像文件的名称可以包括三个单独的部分：文件名、帧编号扩展名和文件格式扩展名。这三部分的组合称为文件名语法。

#### 文件名前缀(File name prefix)

在“文件名前缀”(File name prefix)属性上单击鼠标右键，可以将这些字段中的一个或多个添加到场景的文件名中，例如，场景名、层名称、摄影机名称、版本号、当前日期或当前时间。下面将详细介绍其中每个字段。

也可以通过在文件名前缀中添加 /（斜线）来创建子目录以保存渲染图像。有关文件名语法的详细信息，请参见[渲染图像的子文件夹和名称](../../../../可视化和渲染图像/可视化和渲染图像/渲染输出/渲染图像的子文件夹和名称.md)。

**注**

在为动画选择基本文件名时，应避免使用句点；改用下划线。例如，使用：

xxx_yyy.png.1

替代

xxx.yyy.png.1

**注**

要为渲染层创建层覆盖，请在属性名称上单击鼠标右键，以显示

“创建层覆盖”(Create Layer Override)

菜单选项。

#### <Scene>

选择该渲染标记可以将场景名称添加到输出文件名中。

#### <RenderLayer>

选择该渲染标记可以将渲染层名称添加到输出文件名中。

#### <Camera>

选择该渲染标记可以将摄影机名称添加到输出文件名中。

#### <RenderPassFileGroup>

使用过程渲染时，可以将渲染过程分组到逻辑文件组中。每个渲染过程节点都具有“过程组名称”(Pass Group Name)属性，它允许您创建逻辑组。选择该渲染标记可以将“过程组名称”(Pass Group Name)添加到输出文件名中。

#### <RenderPass>

选择该渲染标记可以将渲染过程节点名称（例如，diffuseNoShadow）添加到输出文件名中。

**注**

提示：

“<RenderPass>”

标记有两个用途：它在渲染笔直渲染过程时将过程名称添加到子文件夹/图像文件名中，并在渲染预合成曲线图时将渲染目标名称添加到子文件夹/图像文件名中。

#### <RenderPassType>

使用渲染过程属性编辑器，可以选择许多不同类型的渲染过程，例如，美景、阴影、镜面反射和折射。使用该渲染标记时，会向输出文件名附加少于 6 个字符的过程类型的唯一缩写，例如，代表折射过程的 REFR。

#### <Extension>

选择该渲染标记可以将扩展名添加到输出文件名中。在许多情况下，无需该标记，因为 Maya 会自动附加文件扩展名。但是，您可能希望使用文件类型创建目录结构。例如，如果使用的是 .png 格式，<EXT>/<RenderLayer>_<RenderPass> 可以创建如下文件：images/iff/bob_camera1_diffuse.1.png。

#### <Version>

选择该渲染标记可以将版本添加到输出文件名中。可以使用“版本标签”(Version Label)属性设定版本。

#### 当前日期(current date)

选择它可将当前日期添加到输出文件名中。该字段不是动态的，捕捉插入标记时的日期和时间。因此，在插入标记后，日期和时间不会更新。

#### 当前时间(current time)

选择它可将当前时间添加到输出文件名中。该字段不是动态的，捕捉插入标记时的日期和时间。因此，在插入标记后，日期和时间不会更新。

#### 图像格式(Image format)

用于保存渲染图像文件的格式。另请参见[文件格式](../../../../可视化和渲染图像/可视化和渲染图像/渲染输出/文件格式.md)。默认设置为 PNG。

#### 压缩...(Compression...)

（对于 Maya 软件渲染器）单击该按钮可以为 AVI (Windows) 或 QuickTime 影片 (Mac OS X) 文件选择压缩方法。单击该按钮后，“视频压缩”(Video Compression)对话框将出现。从“压缩程序”下拉列表中选择所需的压缩方法。当前，Maya 只支持不压缩和 Cinepack 编解码器压缩方法。

仅当选择 AVI (Windows) 或 QuickTime 影片 (Mac OS X) 作为图像格式时，该按钮才变为活动的（仅限 Maya 软件渲染器）。

**注**

该选项的设置保存在 Windows 注册表中，不在场景文件中。将场景文件从一台计算机复制到另一台计算机上不会传递这些设置。

#### EXR 压缩(EXR compression)/数据类型(Data type)

选择“Maya 硬件 2.0”(Maya Hardware 2.0)作为渲染器，并选择“EXR (exr)”作为图像格式时，将显示这些属性。在不同的压缩方法中以及在 16 位半浮点和 32 位浮点数据类型之间进行选择。

有关压缩方法的详细信息，请参见上面的“图像压缩”(Image compression)。

#### 帧/动画扩展名(Frame/Animation ext)

渲染图像文件名的格式（语法）。该属性可用于确定静态图像将被渲染还是序列。如果是后者，提供了几种预设来供您选择如何将帧编号附加到文件名。

#### 帧填充(Frame padding)

帧编号扩展名的位数。例如，如果“帧/动画扩展名”(Frame/Animation ext)设定为*“名称.扩展名”(name.ext)*，并且“帧填充”(Frame padding)为 3，则 Maya 将渲染图像文件命名为 name.001、name.002，依此类推。默认值为 1。

#### 自定义命名字符串(Custom Naming String)

选择“帧缓冲区命名”(Frame Buffer Naming)属性下的“自定义”(Custom)选项可以激活该字段。使用该字段可以自己选择渲染标记来自定义 OpenEXR 文件中的通道命名。

#### 使用自定义扩展名(Use custom extension) / 扩展名(Extension)

通过启用“使用自定义扩展名”(Use custom extension)，然后在“扩展名”(Extension text)文本字段中输入扩展名，可以对渲染图像文件名使用自定义文件格式扩展名。该扩展名基于文件格式替换标准扩展名，例如 .PNG、.GIF 等等。

#### 版本标签(Version Label)

可以将版本标签添加到渲染输出文件名中。使用该属性可以自定义[图像文件输出(Image File Output)](“渲染设置”%28Render%20Settings%29“公用”%28Common%29选项卡.md#WS17956D7ADBC6E736-7EB1F595117AE33AD8D-7FFA)区域中的“文件名前缀”字段中的 <Version> 标记。

可以选择下列选项之一：版本号（例如，1、2 或 3）、当前日期或当前时间。在该属性上单击鼠标右键可以添加所需的版本标签。每次插入数字版本号时，将自动更新提供的前两个选项（使用编号: n）。例如，如果已添加版本号 3，则第一个选项将自动更新为“使用编号: 2”和“使用编号: 4”。也可以创建自己的自定义版本标签。

**注**

也可以使用命令行设置

“文件名前缀”(File name prefix)

。有关详细信息，请参见

使用命令行设置文件名前缀

。

## 帧范围

#### 开始帧(Start frame)、结束帧(End frame)

指定要渲染的第一个帧（开始帧）和最后一个帧（结束帧）。仅当“帧/动画扩展名”(Frame/Animation ext)设定为包含 # 的选项时，开始帧和结束帧才可用（另请参见“设定文件名语法”）。开始帧的默认值为 1；结束帧的默认值为 10。

#### 帧数(By frame)

要渲染的帧之间的增量。仅当“帧/动画扩展名”(Frame/Animation ext)设定为包含 # 的选项时，“帧数”(By frame)才可用。默认值为 1。

如果使用小于 1 的值，请确保启用了[重建帧编号](“渲染设置”%28Render%20Settings%29“公用”%28Common%29选项卡.md#WS73099CC142F487553B93539F117EA10CE8F4B98)选项。否则，许多帧将显示为缺失，其实它们只是被覆盖了。

#### 跳过现有帧(Skip existing frames)

启用此选项后，渲染器将检测并跳过已渲染的帧。此功能可节省渲染时间。

#### 重建帧编号(Renumber frames using)

可以更改动画的渲染图像文件的编号。“重建帧编号”(Renumber frames)属性只在“帧/动画扩展名”(Frame/Animation ext)设定为具有 # 的选项（如 name.#.ext）时可用。

如果启用，Maya 将使用从开始编号开始的帧编号扩展名并按帧数增加来作为渲染图像文件名。

#### 开始编号(Start number)

希望第一个渲染图像文件名具有的帧编号扩展名。

#### 帧数(By frame)

希望渲染图像文件名具有的帧编号扩展名之间的增量。

## 可渲染摄影机

#### 可渲染摄影机(Renderable Cameras)

从一个或多个摄影机渲染场景。默认值为从一个摄影机渲染。

如果要（仅）从一个摄影机渲染场景，请从下拉列表中选择摄影机。默认情况下，perspShape 摄影机是可渲染摄影机。

下拉列表划分为多个区域，用划线分隔：

![图：从一个或多个摄影机渲染场景。默认值为从一个摄影机渲染。 如果要（仅）从一个摄影机渲染场景，请从下拉列表中选择摄影机。默认…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-52B351D4-9284-421B-96E4-617856BDC736.png) <!-- baize:img-hook downloaded=false reason="正文 7884 字 ≥300，非承重" -->

第一个区域是当前选定为可渲染的摄影机。

第二个和第三个区域列出了可选择为可渲染的现有摄影机，例如，立体摄影机与正面和侧面摄影机。

**注**

如果从列表中选择 stereoCamera（立体对），则同时渲染左和右立体摄影机。

第三个区域是“添加可渲染摄影机”(Add Renderable Camera)选项。如果要将其他现有摄影机添加到可渲染摄影机列表中，可以选择“添加可渲染摄影机”(Add Renderable Camera)。选择该选项时，将显示新的“可渲染摄影机”(Renderable Camera)区域。从下拉列表中选择要从其渲染场景的其他可渲染摄影机。

如果从多个摄影机渲染，则在默认情况下，每个摄影机的渲染图像输出将存储在不同的目录中。例如，如果从 camera1 和 camera2 渲染，则渲染图像将分别存储在 camera1/scene.gif 和 camera2/scene.gif 中。

也可以使用“文件名前缀”(File Name Prefix)属性来覆盖默认设置。在“文件名前缀”(File Name Prefix)属性上单击鼠标右键，然后选择“插入摄影机名称 <摄影机>”(Insert camera name <摄影机>)。这样，所有渲染图像将保存到同一目录中，并使用摄影机名称标识（例如，<camera>_<scene>.gif 生成 camera1_scene.gif 和 camera2_scene.gif）。有关详细信息，请参见[文件名前缀](“渲染设置”%28Render%20Settings%29“公用”%28Common%29选项卡.md#WS73099CC142F487553B93539F117EA10CE8F4B60)。

对于每个可渲染摄影机，还可以为该摄影机启用或禁用“Alpha”或“遮罩”(Mask)通道。

#### Alpha 通道(遮罩) (Alpha channel (Mask))

控制渲染图像是否包含遮罩通道。默认设置为启用。

#### 深度通道(Z 深度) (Depth channel (Z Depth))

控制渲染图像是否包含深度通道。默认设置为禁用。

#### 移除可渲染摄影机

若要使摄影机不可渲染，请通过单击摄影机名称旁边的 ![图：若要使摄影机不可渲染，请通过单击摄影机名称旁边的 按钮从列表中移除它。场景中应至少具有一个可渲染摄影机。如果仅列出了一个…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-0245CC06-3449-4E31-9BA1-321556913A91.png) <!-- baize:img-hook downloaded=false reason="正文 7884 字 ≥300，非承重" --> 按钮从列表中移除它。场景中应至少具有一个可渲染摄影机。如果仅列出了一个可渲染摄影机，则不会显示移除按钮。

## 图像大小(Image Size)

“图像大小”(Image Size)属性控制渲染图像的分辨率和像素纵横比。

有关分辨率的详细信息，请参见[分辨率](../../../../可视化和渲染图像/可视化和渲染图像/渲染输出/分辨率%28Resolution%29.md)。

**注**

- 矢量渲染器的分辨率限制为 1600x1600，EPS 和 AI 文件格式除外。

- 当使用 Maya 软件渲染器渲染大于 6k x 6k 的分辨率时，如果保存的输出图像是以下格式之一，则 Maya 将需要大量内存：tiff、Avid Softimage、Autodesk-PIX、JPEG、EPS 或 Cineon。在此类情况下，可以渲染为 Maya 支持的任何其他图像格式，然后使用转化工具（如 imgcvt）将这些图像转化为所需格式。

#### 预设(Presets)

选择胶片或视频行业标准分辨率。从“预设”(Presets)下拉列表中选择某个选项后，Maya 会自动设定“宽度”(Width)、“高度”(Height)、“设备纵横比”(Device Aspect Ratio)和“像素纵横比”(Pixel Aspect Ratio)。

也可以添加“预设”(Presets)选项以输出到未列出的设备。

| 渲染分辨率 | 宽度 | 高度 | 设备纵横比 | 像素纵横比 |
|---|---|---|---|---|
| 自定义 | 任意 | 任意 | 任意 | 任意 |
| 320x240 | 320 | 240 | 1.333 | 1.000 |
| 640x480 | 640 | 480 | 1.333 | 1.000 |
| 1k Square | 1024 | 1024 | 1.000 | 1.000 |
| 2k Square | 2048 | 2048 | 1.000 | 1.000 |
| 3k Square | 3072 | 3072 | 1.000 | 1.000 |
| 4k Square | 4096 | 4096 | 1.000 | 1.000 |
| CCIR PAL/Quantel PAL | 720 | 576 | 1.333 | 1.066 |
| CCIR 601/Quantel NTSC | 720 | 486 | 1.333 | 0.900 |
| Full 1024 | 1024 | 768 | 1.333 | 1.000 |
| Full 1280/Screen | 1280 | 1024 | 1.333 | 1.066 |
| HD 720 | 1280 | 720 | 1.777 | 1.000 |
| HD 1080 | 1920 | 1080 | 1.777 | 1.000 |
| NTSC 4d | 646 | 485 | 1.333 | 1.001 |
| PAL 768 | 768 | 576 | 1.333 | 1.000 |
| PAL 780 | 780 | 576 | 1.333 | 0.984 |
| Targa 486 (tga) | 512 | 486 | 1.333 | 1.265 |
| Targa NTSC (tga) | 512 | 482 | 1.333 | 1.255 |
| Targa PAL (tga) | 512 | 576 | 1.333 | 1.500 |
| Letter | 2550 | 3300 | 0.773 | 1.000 |
| Legal | 2550 | 4200 | 0.67 | 1.000 |
| Tabloid | 5100 | 3300 | 1.545 | 1.000 |
| A4 | 2480 | 3508 | 0.707 | 1.000 |
| A3 | 3507 | 4962 | 0.707 | 1.000 |
| B5 | 2079 | 2952 | 0.704 | 1.000 |
| B4 | 2952 | 4170 | 0.708 | 1.000 |
| B3 | 4170 | 5907 | 0.706 | 1.000 |
| 2” x 3” | 600 | 900 | 0.667 | 1.000 |
| 4” x 6” | 1200 | 1800 | 0.667 | 1.000 |
| 5” x 7” | 1500 | 2100 | 0.714 | 1.000 |
| 8” x 10” | 2400 | 3000 | 0.800 | 1.000 |

#### 保持宽度/高度比率(Maintain width/height ratio)

若要在宽度和高度方面成比例地缩放图像大小，请启用该设置。在为“宽度”或“高度”输入一个值时，会自动计算另一个值。

#### 保持比率(Maintain ratio)

指定要使用的渲染分辨率的类型：“像素纵横比”(Pixel aspect)或“设备纵横比”(Device aspect)。

“像素纵横比”(Pixel aspect ratio)是组成图像的宽度和高度的像素数之比。大多数显示设备（例如，计算机监视器）具有方形像素，其“像素纵横比”(Pixel aspect ratio)为 1。但也有一些设备具有非方形像素（例如，NTSC 视频的“像素纵横比”(Pixel aspect ratio)为 0.9）。

“设备纵横比”(Device aspect ratio)是显示器的宽度单位数乘以高度单位数。4:3 (1.33) 显示器将生成较方正的图像，而 16:9 (1.78) 比率将生成的图像是全景形状。

#### 宽度(Width)

使用“大小单位”(Size units)设置中指定的单位指定图像的宽度。

#### 高度(Height)

使用“大小单位”(Size units)设置中指定的单位指定图像的高度。

#### 大小单位(Size units)

设定指定图像大小时要采用的单位。从像素、英寸、cm（厘米）、mm（毫米）、点和派卡中选择。

#### 分辨率(Resolution)

使用“分辨率单位”(Resolution Units)设置中指定的单位指定图像的分辨率。TIFF、IFF 和 JPEG 格式可以存储该信息，以便在第三方应用程序（如 Adobe® Photoshop®）中打开图像时保持它。

#### 分辨率单位(Resolution units)

设定指定图像分辨率时要采用的单位。从像素/英寸或像素/cm（厘米）中选择。

#### 设备纵横比(Device aspect ratio)

在其上查看渲染图像的显示设备的纵横比。设备纵横比表示图像纵横比乘以像素纵横比。

#### 像素纵横比(Pixel aspect ratio)

在其上查看渲染图像的显示设备的各个像素的纵横比。

有关像素纵横比的详细信息，请参见[像素纵横比](../../../../可视化和渲染图像/可视化和渲染图像/渲染输出/像素纵横比%28Pixel%20aspect%20ratio%29.md)。

## 场景集合(Scene Assembly)

#### 渲染表示(Render representation)

可用于指定在渲染时要渲染的“场景集合”(Scene Assembly)表示。

请参见[渲染集合表示](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4D5955E2-4C09-40C5-A65A-1BE26052FFB6)。

**注**

“场景集合”(Scene Assembly)

“渲染表示”(Render representations)

选项旨在使用集合引用。使用这些选项渲染集合定义可能不会输出所需的结果。

##### 活动表示(Active Representation)

指定在渲染时渲染场景中的[活动表示](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7ED15645-3C4E-470B-BFE4-9B606601BF0E#GUID-7ED15645-3C4E-470B-BFE4-9B606601BF0E__GUID-815DD840-BBDC-4FF8-8E9B-5185C4DA6061)。

请参见[切换活动集合表示](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5F601038-BABF-474C-8BFB-AED20C4FF5F1)。

##### 自定义(Custom)

在字段中键入所需内容创建一个过滤器，以指定在渲染时要渲染哪些表示。

请参见[指定要渲染的集合表示](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1C55AFF4-588D-4560-9420-801BD01E78F3)和[创建过滤器来指定要渲染的表示](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-93C7EB8F-13EB-4438-9CDE-AC3A0A2C862D)。

###### 表示名称(Representation Name)

要渲染的表示具有指定的[名称](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7ED15645-3C4E-470B-BFE4-9B606601BF0E#GUID-7ED15645-3C4E-470B-BFE4-9B606601BF0E__GUID-91DEAF31-B0AB-46C2-B75C-F0C054345170)。

###### 表示标签(Representation Label)

要渲染的表示具有指定的[标签](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7ED15645-3C4E-470B-BFE4-9B606601BF0E#GUID-7ED15645-3C4E-470B-BFE4-9B606601BF0E__GUID-B4E0C80F-0F65-4B8B-BCE0-E306475DD838)。

###### 表示类型(Representation Type)

要渲染的表示属于指定的[类型](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7ED15645-3C4E-470B-BFE4-9B606601BF0E#GUID-7ED15645-3C4E-470B-BFE4-9B606601BF0E__GUID-B35CD5F4-E7CC-44DF-8226-D8979A75E75A)。

###### 使用正则表达式(Use Regular Expressions)

如果启用此选项，Maya 将使用“表示名称”(Representation Name)、“表示标签”(Representation Label)和“表示类型”(Representation Type)字段中的表达式来指定在渲染时要渲染哪些表示。

请参见[使用正则表达式指定要渲染的表示](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6E9D29E2-A527-4C9E-A411-EFB2634FE757)。

## 渲染选项(Render Options)

#### 启用默认灯光(Enable Default Light)

不适用于矢量渲染。

在渲染过程中启用或禁用默认照明。

有关 Maya 默认照明的详细信息，请参见 [Maya 中的默认照明](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6D4A0119-5A23-49DF-9D67-C44311BC472B)。

#### 渲染帧前 MEL(Pre render frame MEL)、渲染帧后 MEL(Post render frame MEL)

在渲染每个帧之前（“渲染帧前 MEL”(Pre render frame MEL)）或在渲染每个帧后（“渲染帧后 MEL”(Post render frame MEL)）运行的 MEL 命令或脚本。

有关“渲染帧前 MEL”(Pre render frame MEL)脚本和“渲染帧后 MEL”(Post render frame MEL)脚本的详细信息，请参见[渲染前 MEL 和渲染后 MEL 脚本](../../../../可视化和渲染图像/可视化和渲染图像/渲染输出/预渲染%20MEL%20和%20渲染后%20MEL%20脚本.md)。

注释：

- 如果需要在渲染设置中的前帧 MEL 或后帧 MEL 字段中使用多组引号，请确保为每个引号使用 \"，第一个和最后一个引号除外。print("Time to render my Maya scene, called\"bingo.mb\"");

- 在输入脚本名称时，不要输入 .mel 扩展名。您将获得与以下内容类似的错误消息：Error: Cannot link to "name.mel".Check number and types of arguments expected on procedure definition.
