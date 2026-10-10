# 创建摄影机选项(Create Camera Options)

使用这些选项可设置从“创建 > 摄影机”(Create > Cameras)菜单创建的摄影机属性。另请参见[创建和使用摄影机](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C668AE39-9D09-4EFA-932E-E3D4AFF8C099)。

## 摄影机特性(Camera Properties)

当摄影机为基本摄影机时，摄影机查看工具（翻滚、平移和推拉）使用此值来确定“观察”点。

#### 兴趣中心(Center of Interest)

从摄影机到兴趣中心的距离（以场景的线性工作单位为单位测量）。

## 镜头特性(Lens Properties)

#### 焦距(Focal Length)

也可以用于摄影机的“属性编辑器”(Attribute Editor)。摄影机的焦距（以毫米为单位测量）。

增加“焦距”(Focal Length)可拉近摄影机镜头，并放大对象在摄影机视图中的大小。减小“焦距”(Focal Length)可拉远摄影机镜头，并缩小对象在摄影机视图中的大小。有效范围为 2.5 到 100000。如果值大于 3500，则输入值而不是使用滑块。默认值为 35。

有关焦距的常规详细信息，请参见[聚焦和模糊](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-39B2D99C-A395-43D5-AD51-BF14F62A6C5C)。

#### 镜头挤压比(Lens Squeeze Ratio)

摄影机镜头水平压缩图像的程度。大多数摄影机不会压缩所录制的图像，因此其“镜头挤压比”(Lens Squeeze Ratio)为 1。但是，有些摄影机（如变形摄影机）会水平压缩图像，使大纵横比（宽度）的图像落在胶片的方形区域内。默认值为 1。

#### 摄影机比例(Camera Scale)

根据场景缩放摄影机的大小。例如，如果摄影机比例为 0.5，则摄影机视图的覆盖区域为原来的一半，而对象在摄影机中的视图将是原来的两倍大。如果“焦距”(Focal Length)为 35，则摄影机的有效焦距为 70。

## 胶片背特性(Film Back Properties)

请勿编辑这些属性，除非在现场实时拍摄镜头。

#### 水平胶片光圈(Horizontal Film Aperture)、垂直胶片光圈(Vertical Film Aperture)

摄影机光圈或胶片背的高度和宽度（以英寸为单位测量）。“摄影机光圈”(Camera Aperture)属性确定了“焦距”(Focal Length)属性和“视角”(Angle of View)属性之间的关系。默认值为 1.4173 和 0.9449。

#### 水平胶片偏移(Horizontal Film Offset)、垂直胶片偏移(Vertical Film Offset)

根据场景垂直和水平偏移分辨率门和胶片门。更改“胶片偏移”(Film Offset)属性可生成二维轨迹。“胶片偏移”(Film Offset)的测量单位是英寸。默认设置为 0。

#### 胶片适配(Film fit)

控制分辨率门相对于胶片门的大小。如果分辨率门和胶片门具有相同的纵横比，则“胶片适配”(Film Fit)设置不起作用。默认设置为“填充”(Fill)。

| 填充(Fill) | 使分辨率门适配胶片门。 |
|---|---|
| 水平(Horizontal) | 使分辨率门水平适配胶片门。 |
| 垂直(Vertical) | 使分辨率门垂直适配胶片门。 |
| 过扫描(Overscan) | 使胶片门适配分辨率门。 |

也可以在摄影机视图的“视图 > 摄影机设置”(View > Camera Settings)子菜单中设定“胶片适配”(Film Fit)。

#### 胶片适配偏移(Film Fit Offset)

分辨率门相对于胶片门的偏移可以为垂直（如果“胶片适配”(Film Fit)为“水平”(Horizontal)）或水平（如果“胶片适配”(Film Fit)为“垂直”(Vertical)）。如果“胶片适配”(Film Fit)为“填充”(Fill)或“过扫描”(Overscan)，则“胶片适配偏移”(Film Fit Offset)不起作用。“胶片适配偏移”(Film Fit Offset)的测量单位是英寸。默认设置为 0。

#### 过扫描(Overscan)

仅缩放摄影机视图（非渲染图像）中的场景大小。调整“过扫描”(Overscan)值以查看比实际渲染更多或更少的场景。如果显示视图导向，更改“过扫描”(Overscan)值可更改视图导向周围的空间量，使它们更容易被看见。默认值为 1。

| 1 | 视图助手填充该视图。视图助手的边可以与视图的边精确对齐，在这种情况下，该视图助手是不可见的。 |
|---|---|
| > 1 | 该值越大，视图导向外部的空间就越大。 |

## 剪裁平面(Clipping Planes)

有关剪裁平面的详细信息，请参见[剪裁平面](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D69C23DA-ECFB-4D95-82F5-81118ED41C95)。

#### 近剪裁平面(Near Clip Plane)、远剪裁平面(Far Clip Plane)

表示透视或正交摄影机近剪裁平面和远剪裁平面的距离。“近剪裁平面”(Near Clip Plane)的默认设置为 0.1，“远剪裁平面”(Far Clip Plane)的默认设置为 10000。

对于 Maya 软件渲染，默认情况下启用“自动渲染剪裁平面”(Auto Render Clip Plane)（请参见[自动渲染剪裁平面](../../面板菜单/面板菜单：“视图”%28View%29/摄影机属性编辑器%28Camera%20Attribute%20Editor%29.md#WS73099CC142F487553B93539F117EA10CE8F5E72)），且“近剪裁平面”(Near Clip Plane)和“远剪裁平面”(Far Clip Plane)值并不确定剪裁平面的位置。请参见[自动渲染剪裁平面](../../面板菜单/面板菜单：“视图”%28View%29/摄影机属性编辑器%28Camera%20Attribute%20Editor%29.md#WS73099CC142F487553B93539F117EA10CE8F5E72)。

如果近剪裁平面和远剪裁平面之间的距离远大于在场景中包含所有对象所需的距离，则某些对象的图像质量可能较差。将“近剪裁平面”(Near Clip Plane)和“远剪裁平面”(Far Clip Plane)属性分别设定为最小和最大值，从而产生所需结果。

**注**

提示：

通常在摄影机的特定范围内渲染对象。将近剪裁平面和远剪裁平面设定为略微超出场景中对象的界限，这有助于提高图像质量。

**注**

远比率：近剪裁平面确定深度精度。尝试保持尽可能小的比率，以获得更好的结果。

由于大多数深度精度集中在近剪裁平面，因此在远处对象上尽量避免过多细节。

对于硬件渲染来说，此概念非常重要，因为它仅拥有 24 位深度精度，而软件渲染却拥有 32 位深度精度。

## 运动模糊(Motion Blur)

#### 快门角度(Shutter Angle)

“快门角度”(Shutter Angle)会影响运动模糊对象的对象模糊度。快门角度设置越大，对象越模糊。“快门角度”(Shutter Angle)的测量单位是度。有效值范围为 1 到 360。默认值为 144。

“摄影机快门角度”(Camera Shutter Angle)选项是模糊时间范围的倍数。类似于传统的电影和视频摄影机，该摄影机快门角度决定了曝光持续时间。但是，为了进行运动模糊，它只能根据下列等式改变曝光的绝对时间范围：

“模糊”(Blur)范围 =（“摄影机快门角度”(Camera Shutter Angle) /360 度）x 模糊“帧”(Frame)数

（在实际的胶片摄影机中，按照 180 度进行计算；在旋转另一个 180 度过程中，胶片前进到下一帧曝光。计算机图形摄影机没有胶片。）

有关实际摄影机的快门角度和曝光的常规信息，请参见[聚焦和模糊](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-39B2D99C-A395-43D5-AD51-BF14F62A6C5C)。

**注**

要使快门角度设置生效（即显示运动模糊），必须将下列选项设定为“运动模糊”(Motion Blur)：

- 对于“渲染设置”(Render Settings)窗口（针对您使用的特定渲染器）中的场景。

- 对于对象“属性编辑器”(Attribute Editor)的“渲染统计信息”(Render Stats)区域中的至少一个对象。

## 正交视图(Orthographic Views)

默认情况下，从“创建”(Create)菜单创建摄影机时，视图为透视视图。如果想要正交摄影机视图，单击“正交”(Orthographic)复选框并更改“正交宽度”(Orthographic Width)（如果必要）。

“正交视图”(Orthographic Views)属性控制摄影机是透视摄影机还是正交摄影机（顶部、正面或侧面），还可以控制正交摄影机的视野。另请参见[摄影机设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4410F526-56AC-4788-A7AF-2EAA970BB89D)主题中的“查看摄影机与渲染摄影机”。

#### 正交(Orthographic)

如果启用此选项，则摄影机为正交摄影机。如果禁用此选项，则摄影机为透视摄影机。默认情况下，将会禁用“正交”(Orthographic)。

**注**

提示：

默认的摄影机与主轴对齐。可以通过旋转正交摄影机或更改默认的翻滚选项，然后使用翻滚工具来创建离轴正交摄影机。

若要在“翻滚工具”(Tumble tool)选项窗口中旋转正交视图，务必确保禁用锁定设置。请参见[“摄影机工具”(Camera Tools)菜单](../../面板菜单/面板菜单：“视图”%28View%29/“摄影机工具”%28Camera%20Tools%29菜单.md#WS17956D7ADBC6E73642AE5CD3117AE33B5CB-7F90)。

#### 正交宽度(Orthographic Width)

正交摄影机的宽度（以英寸为单位）。正交摄影机宽度可以控制摄影机的可见场景范围。更改正交摄影机的宽度与缩放透视摄影机具有相同的效果。

**注**

提示：

如果要创建新的透视摄影机并退出正交视图模式，请选择“创建摄影机选项”(Create Camera Options)窗口顶部的“编辑 > 重置设置”(Edit > Reset Settings)，然后单击“应用”(Apply)。

## 相关主题

- [摄影机设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4410F526-56AC-4788-A7AF-2EAA970BB89D)
