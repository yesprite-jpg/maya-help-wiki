# “UV 编辑器”(UV Editor)的“图像”(Image)菜单

有关使用该菜单中的功能的详细信息，请参见[显示 UV 后面的纹理](../../../../显示和选择%20UV/显示%20UV%20后面的纹理.md)。

#### 显示(Display)

显示或隐藏纹理图像。为快速访问，在 UV 编辑器工具栏中也可找到此项目。请参见 [UV 编辑器概述](../../../../“UV%20编辑器”%28UV%20Editor%29概述.md)。

#### 暗淡(Dim)

减小当前显示的背景图像或棋盘格图案的亮度。通过暗淡背景图像，可以更轻松地在 UV 编辑器的视图中查看和选择组件。根据该项目的当前状态，选择该项目可在启用或禁用之间进行切换。 选中该选项框可调整暗显程度。

#### 未过滤(Unfiltered)

禁用像素模糊可显示精确的像素边界。为快速访问，在 UV 编辑器工具栏中也可找到此项目。请参见 [UV 编辑器概述](../../../../“UV%20编辑器”%28UV%20Editor%29概述.md)。

#### RGB、RGBA、Alpha

切换显示纹理图像及其 Alpha（透明度）通道（分别为 RGBA 和 Alpha），或使用 RGB 完全忽略透明度。为快速访问，在 UV 编辑器工具栏中也可找到这些项目。有关工具按钮及其用途的表，请参见 [UV 编辑器概述](../../../../“UV%20编辑器”%28UV%20Editor%29概述.md)。

#### 图像范围(Image Range)

使用这些设置可更改有多少纹理会显示在编辑器中。

#### 最小 U/V 值(Minimum U/V)和最大 U/V 值(Maximum U/V)

通过设置这些选项可以显式设置图像的大小，或者可以选择其中一个预设。

#### 预设(Presets)

选择其中一个预设图像范围，然后单击“应用”。

#### 无(None)

纹理空间是由“最小 U 值”(Minimum U)、“最小 V 值”、“最大 U 值”(Maximum U)和“最大 V 值”定义的。

#### 栅格大小(Grid size)

该纹理会填充栅格的范围（在“栅格选项”(Grid Options)窗口中进行定义）。

#### 单位大小(Unit Size)

该纹理会填充 0 到 1（或单位）的纹理空间。

#### 图像比(Image Ratio)

在显示方形纹理空间与显示与该图像具有相同的宽高比的纹理空间之间进行切换。为快速访问，在 UV 编辑器工具栏中也可找到此项目。请参见 [UV 编辑器概述](../../../../“UV%20编辑器”%28UV%20Editor%29概述.md)。

#### 像素捕捉(Pixel Snap)

确定是否自动将 UV 捕捉到像素。会捕捉到像素角点或像素中心。为快速访问，在 UV 编辑器工具栏中也可找到此项目。有关工具按钮及其用途的表，请参见 [UV 编辑器概述](../../../../“UV%20编辑器”%28UV%20Editor%29概述.md)。

#### 捕捉角(Snap Corner)

如果启用该选项，选定 UV 会捕捉到其他 UV 的角。

#### 捕捉中心(Snap Center)

如果启用该选项，选定 UV 会捕捉到其他 UV 的中心。

#### UV 编辑器烘焙(UV Editor Baking)

烘焙纹理，并将其存储在内存中。另请参见 [UV 编辑器概述](../../../../“UV%20编辑器”%28UV%20Editor%29概述.md)。

#### 烘焙纹理的分辨率(Baked Texture Resolution)

烘焙纹理时使用的分辨率。

#### 创建 PSD 网络(Create PSD Network)

创建可以用作纹理贴图的 Adobe® Photoshop® 纹理。使用该功能时，可以显式创建 UV 的 PSD 层以帮助纹理的绘制。有关详细信息，请参见[将 PSD 网络用作 Maya 中的纹理](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A7687378-DC86-4B80-A208-80AC151BFE54)和[从 Maya 中创建包含层集的 PSD 文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B750BF4E-2343-4AA0-A09F-C7FA5F270B95)。

#### 更新 PSD 网络(Update PSD Networks)

在 Adobe® Photoshop® 中修改连接到 Maya PSD 节点的 PSD 文件时，可以在 Maya 中更新（刷新）图像以便立即显示修改。会更新场景中的所有 PSD 网络。请参见[更新 PSD 网络](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-648C6045-45B5-49FB-9FA5-77A8D67835FF)。

#### UV 快照(UV Snapshot)

保存当前 UV 布局的图像文件。然后可以在绘制程序中在该图像上绘制，或者在图像编辑器（如 Adobe® Photoshop®）中将该图像用作纹理作品的背景引用层。请参见[保存 UV 布局的图像](../../../../编辑%20UV/保存%20UV%20布局的图像.md)。将显示一个包含下列控件的选项窗口：

#### 文件名(File Name)

可以将文件保存在项目内部或外部的任意位置。Maya 会基于所选择的图像格式自动指定文件扩展名。

#### 图像格式(Image Format)

请使用绘制程序可以读取的图像格式。如果在绘制时需要 Alpha 通道，请使用 TIFF 或类似的格式。

#### 大小 X (Size X)、大小 Y (Size Y)

设置导出的图像的尺寸。为将要创建的文件纹理使用需要的相同尺寸。如果不确信，请使用默认大小；可以稍后在绘制程序中缩放导出的图像。

#### 锁定纵横比(Lock Aspect Ratio)

纵横比是“大小 X”(Size X)与“大小 Y”(Size Y)之比。如果启用该选项，则可以更改一个大小滑块，Maya 会自动调整其他大小值以保持相同的比率。如果需要更改纵横比，请暂时禁用该选项并调整其中一个值。

#### 抗锯齿线(Anti-alias Lines)

控制输出图像中的线是否抗锯齿。

#### 边颜色(Edge Color)

设置导出的图像中 UV 面片的颜色。快照的背景为黑色；因此，“颜色”(Color)值应该为白色或另一种对比鲜明的颜色。可以单击该框来打开“颜色选择器”(Color Chooser)。

#### UV 区域(UV Area)

确定将输出至 2D 快照文件的 UV 纹理空间部分。

- 平铺(Tiles)：指定 U 和 V 方向上要包括在快照中（从 0 开始）的平铺数。

- 范围(Range)：通过指定 U 和 V 的最小值和最大值来指定要包括在快照中的自定义 UV 范围。需要在“UV 编辑器”(UV Editor)内输出特定 UV 壳或特定区域的图像时，此选项十分有用。

## 相关主题

- [UV 编辑器菜单栏](../UV%20编辑器菜单.md)

- [UV 编辑器概述](../../../../“UV%20编辑器”%28UV%20Editor%29概述.md)
