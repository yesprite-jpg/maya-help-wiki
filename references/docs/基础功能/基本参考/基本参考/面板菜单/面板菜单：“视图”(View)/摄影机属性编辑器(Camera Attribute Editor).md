# 摄影机属性编辑器(Camera Attribute Editor)

选择“视图 > 摄影机属性编辑器”(View > Camera Attribute Editor)以在“属性编辑器”(Attribute Editor)中查看摄影机属性。

## 摄影机属性(Camera attributes)

**注**

提示：

如果单击此编辑器中某些属性右侧的框，将显示

“创建渲染节点”(Create Render Node)窗口

，这意味着可以将某些渲染节点映射到摄影机属性。

#### 控制(Controls)

有关摄影机类型（“摄影机”(Camera)、“摄影机和目标”(Camera and Aim)、“摄影机”(Camera)、和目标(Aim)和“上方向”(Up)”）的信息，请参见 [Maya 摄影机类型](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B9BCF462-A8FB-4533-9FDE-82C23BA97BEA)。

#### 视角(Angle of view)

有关视角和其如何受摄影机聚焦距离影响的详细信息，请参见[视角（焦距）](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B45D6241-AF72-4AA3-B8F6-EC5EB76CDB28)。

**注**

提示：

尽量避免使用角度非常小（小于 5 度）的透视摄影机。这样做可能会导致深度精度明显降低，从而产生深度冲突瑕疵。请改为尝试使用正交摄影机以获得相似的外观。

#### 焦距(Focal length)

请参见[焦距](../../主菜单/“创建”%28Create%29菜单/创建摄影机选项%28Create%20Camera%20Options%29.md#GUID-35B872B1-840E-4DEE-B80F-F2715B1E8BF0__WS1A9193826455F5FF-4F542F6211C79DEA861-130C)。

#### 摄影机比例(Camera scale)

请参见[摄影机比例(Camera scale)](../../主菜单/“创建”%28Create%29菜单/创建摄影机选项%28Create%20Camera%20Options%29.md#GUID-35B872B1-840E-4DEE-B80F-F2715B1E8BF0__WS17956D7ADBC6E73642AE5CD3117AE33B5CB-7FF7)。

#### 自动渲染剪裁平面(Auto Render Clip Plane)

仅限 Maya 软件。如果此选项处于启用状态（默认设置），则会自动设置近剪裁平面和远剪裁平面，因此它们会在摄影机视图中包含所有对象。（对于所有其他渲染器，您必须手动设置近剪裁平面和远剪裁平面。也可以手动为 Maya 软件渲染设置平面。）

**注**

Maya

使用独立的水平和垂直视野角度。摄影机模型基于独立的水平和垂直胶片光圈以及聚焦距离。

所有对象渲染和深度精度问题都将被排除。剪裁平面在视图中不可见。

“自动渲染剪裁平面”(Auto Render Clip Plane)在默认情况下处于启用状态。如果禁用此选项，近剪裁平面和远剪裁平面的属性值将设置为“近剪裁平面”(Near Clip Plane)和“远剪裁平面”(Far Clip Plane)。

禁用“自动渲染剪裁平面”(Auto Render Clip Plane)（并设置“近剪裁平面”(Near Clip Plane)和“远剪裁平面”(Far Clip Plane)），以根据与摄影机的距离来限制渲染对象（如果您基于深度进行合成）。

#### 近剪裁平面(Near Clipping Plane)、远剪裁平面(Far Clipping Plane)

这些选项在[创建摄影机选项](../../主菜单/“创建”%28Create%29菜单/创建摄影机选项%28Create%20Camera%20Options%29.md)中进行了介绍。另请参见[剪裁平面](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D69C23DA-ECFB-4D95-82F5-81118ED41C95)。

## 视锥显示控件(Frustum Display Controls)

以下是非立体摄影机的视椎显示控件。对于立体摄影机，通过[“立体显示控制”(Stereo Display Controls)](摄影机属性编辑器%28Camera%20Attribute%20Editor%29.md#GUID-C3EBB008-7DBE-4B9D-B9AC-1DA974CEFE15__WS1A9193826455F5FF-4FDFBFFB11A5310C890-848)来控制这些属性。 对于立体摄影机的左/右摄影机，将禁用这些属性。

#### 显示近剪裁平面(Display Near Clip)

启用此选项可显示近剪裁平面。

#### 显示远剪裁平面(Display Far Clip)

启用此选项可显示远剪裁平面。

#### 显示视锥(Display Frustum)

启用此选项可显示视锥。

## 立体(Stereo)

“立体”(Stereo)、“立体调整”(Stereo Adjustments)和“立体显示控制”(Stereo Display Controls)区域中包含了立体摄影机（“stereoCameraCenterCamShape”节点）的属性：

#### 立体(Stereo)

通过以下模式之一，选择计算零视差平面的方法：

#### 禁用(Off)

对节点禁用任何眼分离“枢轴间分离”(InteraxialSeparation)和“零视差”(Zero Parallax)平面计算。此选项将禁用立体效果。

#### 已收敛(Converged)

通过在摄影机中前束来计算零视差平面。可以将此效果与通过向内旋转瞳孔来聚焦对象相比较。但是，如果在成对的渲染图像中获得梯形失真效果，从而导致场景中其他元素的视觉混乱，则可能会产生危险的副作用。在渲染的图像中，我们的焦点往往在整个图像上扫视，而不会聚焦在单个对象上，后者在现实生活中是不真实的。如果对象位于场景中央，并且在摄影机视锥左侧或右侧的渲染边界上不具有场景元素，则应该仅使用“已收敛”(Converged)。

#### 离轴(Off-axis)（默认）

通过使用摄影机胶片背移动视锥，来计算收敛平面。以下是计算立体图像对，并避免根基瑕疵的可靠方法。

#### 平行(Parallel)

平行摄影机设置实际上没有收敛的平面。这对于横向设置对象在有效无限中的位置非常有效。

#### 枢轴间分离(Interaxial Separation)

左侧和右侧摄影机之间的距离。

#### 零视差(Zero Parallax)

发生零视差平面的摄影机视图枢轴的距离，也就是，对象在屏幕中不显示的点。如果对象位于零视差平面的前面，它具有负视差，如果对象位于零视差平面的后面，它具有正视差。

通常，对象应位于零视差平面的后面。也就是说，摄影机距离应大于零视差平面值。零视差值、摄影机分离和聚焦距离都用于确定必须应用于胶片背在各自的左侧和右侧摄影机上的移动。零视差距离仅在** “离轴”(Off-Axis) **或**“脚趾输入”**模式中可用。

## 立体调整(Stereo Adjustments)

#### 前束调整(Toe In Adjust)

当您在“已收敛”(Converged)模式中时，使用此属性来偏移计算脚趾输入效果。此值以度为单位，并作为计算出的脚趾输入的偏移。

#### 右侧摄影机胶片偏移(Film Offset Right Cam)

控制右侧摄影机的胶片偏移。

#### 左侧摄影机胶片偏移(Film Offset Left Cam)

控制左侧摄影机的胶片偏移。

## 立体显示控制(Stereo Display Controls)

#### 显示近剪裁平面(Display Near Clip)

显示近剪裁平面的方法。有效值为：

0：无。显示已禁用。

1：左侧。显示左摄影机剪裁平面。

2：右侧。显示右摄影机剪裁平面。

3：左右两侧。显示左摄影机和右摄影机剪裁平面。

4：中心。显示中心摄影机剪裁平面。

5：全部。显示所有摄影机剪裁平面。

#### 显示远剪裁平面(Display Far Clip)

显示远剪裁平面的方法。有效值请参见“显示近剪裁平面”(Display Near Clip)。

#### 显示视锥(Display Frustum)

显示视锥的方法。有效值请参见“显示近剪裁平面”(Display Near Clip)。

#### 零视差平面(Zero Parallax Plane)

启用此选项可以禁用零视差平面的显示。

#### 零视差颜色(Zero Parallax Color)

使用此属性设置零视差平面的颜色。

#### 零视差透明度(Zero Parallax Transparency)

使用此属性设置零视差平面的透明度。

#### 安全查看体积(Safe Viewing Volume)

启用此选项后，将禁用视图体积的显示。

#### 安全体积颜色(Safe Volume Color)

使用此属性以设置视图体积的颜色。

#### 安全体积透明度(Safe Volume Transparency)

使用此属性，以设置视图体积的透明度。

#### 安全立体(Safe Stereo)

左侧和右侧视图视锥的交集。场景元素在属于交集的两个视锥中可见。通常，不放置仅能在一个摄影机中看到的对象。

## 胶片背(Film Back)

“胶片背”(Film Back)属性控制摄影机的基本属性（例如，摄影机的胶片格式：16mm、35mm、70mm）。

#### 胶片门(Film Gate)

允许您选择某个预设的摄影机类型。Maya 会自动设置“摄影机光圈”(Camera Aperture)、“胶片纵横比”(Film Aspect Ratio)和“镜头挤压比”(Lens Squeeze Ratio)。若要单独设置这些属性，请设置“用户胶片门”(Film Gate to User)。默认设置为“用户”。

#### “摄影机光圈(英寸)”(Camera Aperture (inch))/“摄影机光圈(mm)”(Camera Aperture (mm))

摄影机的“胶片门”(Film Gate)高度和宽度设置。

如果您选择输入值（以英寸为单位），则默认值为 1.417 和 0.945。

如果您选择输入值（以毫米为单位），则默认值为 36.000 和 24.000。

无论选择哪个选项，值均以英寸为单位进行保存。

此设置对摄影机的视角具有直接影响（详细信息请参见“视角”(Angle of view)）。

**注**

“摄影机光圈”(Camera Aperture)设置不影响 F 制光圈。有关 F 制光圈的详细信息，请参见[聚焦和模糊](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-39B2D99C-A395-43D5-AD51-BF14F62A6C5C)。

#### 胶片纵横比(Film Aspect Ratio)

摄影机光圈的宽度和高度的比。Maya 会自动更新“胶片纵横比”(Film Aspect Ratio)（反之亦然）。有效值的范围从 0.01 到 10。默认值为 1.5。

#### 镜头挤压比(Lens Squeeze Ratio)

请参见[镜头挤压比](../../主菜单/“创建”%28Create%29菜单/创建摄影机选项%28Create%20Camera%20Options%29.md#GUID-35B872B1-840E-4DEE-B80F-F2715B1E8BF0__WS17956D7ADBC6E73642AE5CD3117AE33B5CB-7FF8)。

#### 适配分辨率门(Fit Resolution Gate)

请参见[胶片适配](../../主菜单/“创建”%28Create%29菜单/创建摄影机选项%28Create%20Camera%20Options%29.md#GUID-35B872B1-840E-4DEE-B80F-F2715B1E8BF0__WS17956D7ADBC6E73642AE5CD3117AE33B5CB-7FF5)。

#### 胶片适配偏移(Film Fit Offset)

请参见[胶片适配偏移](../../主菜单/“创建”%28Create%29菜单/创建摄影机选项%28Create%20Camera%20Options%29.md#GUID-35B872B1-840E-4DEE-B80F-F2715B1E8BF0__WS17956D7ADBC6E73642AE5CD3117AE33B5CB-7FF4)。

#### 胶片偏移(Film Offset)

垂直和水平偏移与场景相关的分辨率门和胶片门。更改“胶片偏移”(Film Offset)生成 2D 轨迹。“胶片偏移”(Film Offset)的测量单位是英寸。系统默认设置为 0。

| 1 | 视图助手填充该视图。视图助手的边可以与视图的边精确对齐，在这种情况下，该视图助手是不可见的。 |
|---|---|
| > 1 | 值越大，视图助手外部的空间越大。 |

#### 已启用振动/振动(Shake Enabled / Shake)

使用“振动”属性以应用一定量的 2D 转换到胶片背。曲线或表达式可以连接到“振动”(Shake)属性来指定真实的振动效果。“已启用振动”(Shake Enabled)开关可以用于振动效果的启用和禁用。

“振动”(Shake)和“振动过扫描”(Shake Overscan)属性复制并在功能上与“胶片偏移”(Film Offset)属性和 API 合并。默认情况下为禁用。

“已启用振动”(Shake Enabled)允许将“振动”(Shake)属性设置为摄影机计算的因子。默认情况下，该选项处于禁用状态。

振动指定胶片背上的转换。此值通过单独的水平和垂直振动字段来指定，默认设置都为 0，并仅当“已启用振动”(Shake Enabled)属性处于启用状态时，在摄影机计算中使用。对于摄影机计算的目的，“振动”(Shake)和“胶片偏移”(Film Offset)提供相同的效果。振动在摄影机上提供了一组额外的胶片背转换输入，通过这些额外功能，振动可以通过“已启用振动”属性启用和禁用。

使用以下 MEL 命令打开“已启用振动”：

```text
setAttr perspShape.shakeEnabled 1;
```

使用以下 MEL 命令来设置“振动”属性：

```text
setAttr perspShape.shake 0.5 0.5;
```

#### 已启用振动过扫描/振动过扫描(Shake Overscan Enabled / Shake Overscan)

“已启用振动过扫描”(Shake Overscan Enabled)允许“振动过扫描”(Shake Overscan)属性作为摄影机计算的因子。默认情况下为已禁用。

“振动过扫描”(Shake Overscan)指定了胶片光圈的倍数。此过扫描用于渲染较大的区域，并在摄影机不振动时需要用到。此属性会影响输出渲染。“振动过扫描”(Shake Overscan)属性仅当“已启用振动过扫描”(Shake Overscan Enabled)属性设置为真时可用。默认情况下，“振动过扫描”(Shake Overscan)设置为 1。

使用以下 MEL 命令打开“已启用振动过扫描”：

```text
setAttr perspShape.shakeOverscanEnabled 1;
```

使用以下 MEL 命令设置“振动过扫描”：

```text
setAttr perspShape.shakeOverscan 1.25;
```

#### 前缩放(Pre Scale)

“前缩放”(Pre Scale)值用于 2D 效果。此值代表模拟的 2D 摄影机缩放。在此字段中输入一个值。该值将在胶片滚转之前应用。

#### 胶片平移(Film Translate)

“胶片平移”(Film Translate)值用于 2D 效果。此值代表模拟的 2D 摄影机平移。在此字段中输入一个值。

#### 胶片滚转枢轴(Film Roll Pivot)

从胶片背中心的水平枢轴点。枢轴点在胶片背旋转期间使用。枢轴是围绕其发生旋转的点。该双精度参数对应于已归一化的场景视图。此值后期投影矩阵的一部分。

垂直枢轴点用于旋转胶片背。该双精度参数对应于已归一化的场景视图。该值用于计算胶片滚转矩阵，是后期投影矩阵的一个组件。

#### 胶片滚转值(Film Roll Value)

以度为单位指定了胶片背的旋转量。旋转围绕指定的枢轴点发生。该值用于计算胶片滚转矩阵，是后期投影矩阵的一个组件。

#### 胶片滚转顺序(Film Roll Order)

指定如何相对于枢轴的值应用滚动。

#### 旋转平移(Rotate-Translate)

胶片背将首先旋转，然后按照枢轴点值转换。

#### 平移旋转(Translate-Rotate)

胶片背将首先转换，然后按照胶片滚转值旋转。

#### 后缩放(Post Scale)

“前缩放”(Pre Scale)值用于 2D 效果。此值代表模拟的 2D 摄影机缩放。在此字段中输入一个值。在胶片滚转之后应用该值。

## 景深(Depth of Field)

这些属性可以控制摄影机的焦点。

有关此功能的详细信息，请参见[调整景深](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3FCD5E9C-98AF-4BA9-99A1-381B036724E3)。

**注**

提示：

图像超出焦点越多，生成最终渲染图像所需的时间越长（即后期渲染模糊花费更长的时间）。

**注**

在 Viewport 2.0 中，当启用后期效果（如屏幕空间环境光遮挡、运动模糊和景深）后，线框和组件的图像不会受这些效果的影响。曲面的填充显示会受到影响。但是，如果曲面是半透明的，那么曲面的线框和组件不会与填充的绘图融合到一起。例如，如果创建了一个对象，然后将其着色器透明度设定为半透明并选择该对象或其组件，那么将看到启用和禁用

“屏幕空间环境光遮挡”(Screen-space Ambient Occlusion)

之间的差别。

#### 景深(Depth Of Field)

如果启用，取决于对象与摄影机的距离，焦点将聚焦于场景中的某些对象，而其他对象会模糊或超出焦点。如果禁用此选项，会聚焦于场景中的所有对象。“景深”(Depth Of Field)默认情况下处于禁用状态。

景深可以在每个视口面板中启用，并可以使用“Maya 硬件 2.0”(Maya Hardware 2.0)通过最终渲染进行渲染。在这两种情况下，都必须首先在此摄影机的属性编辑器中启用“景深”(Depth of Field)。

若要在当前视口中启用或禁用景深，请单击面板工具栏中的景深图标，或者从面板菜单中切换“着色 > 景深”(Shading > Depth of Field)。

若要在渲染中包括景深，请在“渲染设置”(Render Settings)窗口“Maya 硬件 2.0”(Maya Hardware 2.0)选项卡的“渲染选项”(Render Options)部分中启用“景深”(Depth of Field)。

#### 聚焦距离(Focus Distance)

显示为聚焦的对象与摄影机之间的距离，在场景中使用线性工作单位测量。减小“聚焦距离”(Focus Distance)也将降低景深。有效范围是 0 到无限。默认值为 5。

**注**

提示：

Viewport 2.0 中

，为

“景深”(Depth of Field)

选择

“聚焦距离”(Focus Distance)

，选择

“显示 > 平视显示 > 对象详细信息”(Display > Heads up Display > Object Details)

，然后选择要保留焦点的对象。

“与摄影机的距离”(Distance From Camera)

平视显示应表示对象与摄影机的距离。将此作为

“聚焦距离”(Focal Distance)

。

#### F 制光圈(F Stop)

“摄影机光圈”(Camera Aperture)的设置范围可影响“景深”(Depth of Field)。“F 制光圈”(F Stop)越低（例如 f-4），景深越浅，更多的前景和背景会超出焦点且模糊。“F 制光圈”(F Stop)越高（例如 f-32），景深越深，更多的前景和背景会在焦点上。

有关“F 制光圈”(fStop)的详细信息，请参见 [fStop（光圈）和快门速度/角度](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-39B2D99C-A395-43D5-AD51-BF14F62A6C5C#GUID-39B2D99C-A395-43D5-AD51-BF14F62A6C5C__SECTION_73E6952285484C7599EC5B3FFA93A49D)。

#### 聚焦区域比例(Focus Region Scale)

缩放“聚焦距离值”(Focus Distance value)。有效范围是 0 到无限。默认值为 1。

## 输出设置(Output Settings)

控制摄影机是否在渲染过程中生成图像，以及摄影机渲染哪些类型的图像。

#### 可渲染(Renderable)

如果启用，摄影机可以在渲染期间创建图像文件、遮罩文件或深度文件；并且可被渲染。默认情况下，“可渲染”(Renderable)对于透视摄影机是默认打开的，而对其他摄影机是默认关闭的。

此选项受“渲染设置”(Render Settings)窗口的“文件输出”(File Output)区域中的“可渲染摄影机”(Renderable Camera)选项影响。有关“渲染设置”(Render Settings)窗口的详细信息，请参见[渲染设置窗口](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-59DFB8B7-776B-4243-B404-A3D602FF8CFD)。

#### 图像(Image)

如果启用（并且启用“可渲染”），该摄影机将在渲染过程中创建图像。默认设置为启用。

#### 遮罩(Mask)

如果启用（并且启用“可渲染”），该摄影机将在渲染过程中创建遮罩。遮罩是图像文件中的 8 位通道（Alpha 通道），表示对象的灰度明暗。黑色区域表示此区域没有对象（或完全透明的对象），而白色的区域表示存在（刚体）对象。遮罩主要用于合成。

对于不支持遮罩通道的图像格式，遮罩将存储为单独的图像。

有关遮罩通道的详细信息，请参见[遮罩和深度通道](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-10817F71-CE9C-4E10-850F-F7C5C49FAB9B)。

#### 深度(Depth)

如果启用（并且启用“可渲染”），摄影机将在渲染期间创建深度文件。深度文件是一种数据文件类型，用于表示对象到摄影机的距离。

深度文件主要用于合成。启用时，“深度类型”(Depth Type)属性（下一个）将处于启用状态。

对于不支持深度通道的图像格式，深度将存储为单独的图像。

有关遮罩通道的详细信息，请参见[颜色、遮罩 (Alpha) 和深度通道](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-10817F71-CE9C-4E10-850F-F7C5C49FAB9B)。

#### 深度类型(Depth Type)

确定如何计算每个像素的深度。

#### 最近可见深度(Closest Visible Depth)

使用离摄影机最近的对象。当透明对象位于其他对象的前面时，启用“基于透明度的深度”(Transparency Based Depth)将忽略透明对象。

#### 最远可见深度(Furthest Visible Depth)

通常在粒子效果被不透明对象阻挡时使用。Maya 使用“最远可见深度”(Furthest Visible Depth)创建“深度”(Depth)文件。

#### 基于透明度的深度(Transparency Based Depth)

启用“阈值”(Threshold)，根据透明度确定哪些对象离摄影机最近。“基于透明度的深度”(Transparency Based Depth)仅在选择“最近可见深度”(Closest Visible Depth)时启用。

**注**

提示：

如果透明对象位于其他对象的前面，可以启用

“基于透明度的深度”(Transparency Based Depth)

忽略透明对象。

#### 阈值(Threshold)

当合成多个层的透明度（从 0 到 1）时使用。例如，如果“阈值”(Threshold)为 0.9（默认值）时，如果透明曲面增加到 0.9 或更大，则曲面将变得不透明。

#### 预合成模板(Pre-Compositing template)

使用此属性，在“合成”中使用预合成。可以在“渲染设置”(Render Settings)窗口的“过程”(Passes)选项卡为每个渲染层指定预合成模板。

装配过程的层上的预合成模板。装配层的摄影机上的预合成模板。如果未指定模板将层堆栈为融合节点的线性链（按照 Maya 中的顺序和融合节点），这是默认行为。

## 环境(Environment)

按照摄影机中的显示，控制场景背景的外观。不同的摄影机可以使用不同的背景。

#### 背景色(Background Color)

场景背景的颜色。默认颜色为黑色。

**注**

摄影机的背景颜色不能是纹理贴图的。如果程序背景是必需的，请使用图像平面。

#### 图像平面(Image Plane)

创建图像平面，并将其附着到摄影机。单击“创建”(Create)按钮自动更改“属性编辑器”(Attribute Editor)的焦点，使其包含图像平面的属性。

有关图像平面的详细信息，请参见[创建、编辑或定位图像平面](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F72F8E1B-EFFE-400E-BD92-5441BE9CD28F)。

## 特殊效果(Special Effects)

#### 快门角度(Shutter Angle)

控制运动模糊对象的模糊度。在真实世界中的摄影机，快门实际上是一个缺少扇形部分的金属磁盘。该磁盘放置在镜头和胶片之间，并旋转以恒定。如果缺少的部分位于胶片前方时，它允许光线从镜头穿过并曝光胶片。扇形部分的角度越大，曝光时间越长，移动对象就越模糊。快门角度以度为单位。有效值范围为 1 到 360。默认值为 144。

请参见[快门角度](../../主菜单/“创建”%28Create%29菜单/创建摄影机选项%28Create%20Camera%20Options%29.md#GUID-35B872B1-840E-4DEE-B80F-F2715B1E8BF0__WS1A9193826455F5FF-4F542F6211C79DEA861-1308)。

**注**

“运动模糊”(Motion Blur)

必须在

“渲染设置”(Render Settings)

窗口中打开。对于 Maya 软件渲染、运动模糊也必须在至少一个对象的

“属性编辑器”(Attribute Editor)

的

“快门角度”(Shutter Angle)

中设置才能产生效果。

## 显示选项(Display Options)

在摄影机视图中控制视图助手的显示，并提供了移动摄影机的选项。也可以通过任意面板的“视图 > 摄影机设置”(View > Camera Settings)菜单来访问大部分选项。

#### 显示胶片门(Display Film Gate)

详细信息请参见[胶片门](“摄影机设置”%28Camera%20Settings%29选项.md#GUID-C092B9DA-C523-4566-9209-ACCBFAEE8285__GUID-33FA379E-A960-49D8-9C28-61355DD0946B)。

#### 显示分辨率(Display Resolution)

将显示一个矩形，表示摄影机视图渲染的区域。分辨率门的尺寸表示渲染分辨率。分辨率门的上方显示渲染分辨率值。详细信息请参见[分辨率门](“摄影机设置”%28Camera%20Settings%29选项.md#WS73099CC142F487553B93539F117EA10CE8F5E43)。

#### 显示门遮罩(Display Gate Mask)

请参见[门遮罩](“摄影机设置”%28Camera%20Settings%29选项.md#WS73099CC142F48755602CAF041189DA6B6082571)。

#### 门遮罩不透明度(Gate Mask Opacity)

通过“门遮罩”(Gate Mask)的遮罩区域可以看到的场景数量。此选项仅在“门遮罩”(Gate Mask)处于启用状态时可用。

#### 门遮罩颜色(Gate Mask Color)

“门遮罩”(Gate Mask)区域的遮罩颜色。此选项仅在“门遮罩”(Gate Mask)处于启用状态时可用。

#### 显示区域图(Display Field Chart)

请参见[区域图](“摄影机设置”%28Camera%20Settings%29选项.md#WS73099CC142F487553B93539F117EA10CE8F5E49)。

#### 显示安全动作(Display Safe Action)

请参见[安全动作](“摄影机设置”%28Camera%20Settings%29选项.md#WS73099CC142F487553B93539F117EA10CE8F5E4C)。

#### 显示安全标题(Display Safe Title)

请参见[安全标题](“摄影机设置”%28Camera%20Settings%29选项.md#WS73099CC142F487553B93539F117EA10CE8F5E50)。

#### 显示胶片枢轴(Display Film Pivot)

在通过摄影机查看时，显示胶片枢轴助手。

#### 显示胶片原点(Display Film Origin)

在通过摄影机查看时，显示胶片原点助手。

#### 过扫描(Overscan)

请参见[“创建摄影机”(Create Camera)选项](../../主菜单/“创建”%28Create%29菜单/创建摄影机选项%28Create%20Camera%20Options%29.md)中的“过扫描”(Overscan)。

### 二维平移/缩放(2D Pan/Zoom)

#### 已启用平移/缩放(Pan Zoom Enabled)

选择此选项以启用“二维平移/缩放”(2D Pan/Zoom)功能。

#### 平移(Pan)

输入 X 和 Y 坐标以水平方向和垂直方向平移视图。

#### 缩放(Zoom)

使用此属性，放大和缩小视图。大于 1 的值放大视图，小于 1 的值缩小视图。

#### 渲染平移缩放(Render Pan Zoom)

“二维平移/缩放”(2D Pan/Zoom)功能不会默认渲染。选择该属性来渲染平移/缩放视图。禁用此属性从完整的摄影机视图渲染场景。

## 移动选项(Movement Options)

#### 可撤消的移动(Undoable Movements)

请参见[可撤消的移动](“摄影机设置”%28Camera%20Settings%29选项.md#WS73099CC142F487553B93539F117EA10CE8F5E31)。

#### 兴趣中心(Center of Interest)

兴趣中心到摄影机的距离，使用场景中的线性单位测量。

#### 翻滚枢轴(Tumble Pivot)

“翻滚工具”(Tumble tool)的枢轴点确定摄影机“翻滚工具”(Tumble tool)设置窗口中的“翻滚摄影机围绕”(Tumble Camera About)合适设置为“翻滚枢轴”(Tumble Pivot)。

#### 将枢轴作为局部空间(Use Pivot As Local Space)

启用此属性，并使用摄影机的翻滚枢轴点作为相对翻滚点，以便侧滚工具沿局部枢轴翻滚。

## 正交视图(Orthographic Views)

详细信息请参见[正交视图](../../主菜单/“创建”%28Create%29菜单/创建摄影机选项%28Create%20Camera%20Options%29.md#GUID-35B872B1-840E-4DEE-B80F-F2715B1E8BF0__WS17956D7ADBC6E73642AE5CD3117AE33B5CB-7FEE)。
