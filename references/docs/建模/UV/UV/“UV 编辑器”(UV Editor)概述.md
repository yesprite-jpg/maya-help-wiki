# “UV 编辑器”(UV Editor)概述

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

打开“UV 编辑器”(UV Editor)

- 选择“窗口 > 建模编辑器 > UV 编辑器”(Windows > Modeling Editors > UV Editor)

- 在“建模”(Modeling)[菜单集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D90A2BDB-FD05-4528-8A95-C33A02D15129)中，选择“UV > UV 编辑器”(UV > UV Editor)

“UV 编辑器”(UV Editor)可用于查看 2D 视图内的多边形、NURBS 和细分曲面的 UV 纹理坐标，并以交互方式对其进行编辑。有关如何使用 UV 壳的详细信息，请参见以下相关主题。

与在 Maya 中使用的其他建模工具非常类似，您可以为曲面选择、移动、缩放和大体修改 UV 拓扑。还可以将与指定的纹理贴图相关联的图像作为 UV 编辑器内的背景查看，同时也可以修改 UV 布局以根据需要进行匹配。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F94498EA-6CFD-42B4-9DAC-15F901182E67.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

通过使用“UV 编辑工作区”(UV Editing Workspace)，可以轻松地将 3D 对象与其 2D 纹理坐标进行比较。此工作区同时显示透视视图和“UV 编辑器”(UV Editor)，允许您查看 3D 场景视图内的 UV 与“UV 编辑器”(UV Editor)的 2D 视图中的这些 UV 有何关系，反之亦然。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-DD8C6A7C-2E0E-453E-BCFB-1A6DF429BA04.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

在“UV 编辑器”(UV Editor)中，可以通过“UV 编辑器”(UV Editor)的[菜单](../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/3D%20UV%20抓取工具选项%283D%20UV%20Grab%20Tool%20options%29.md)、视图栏或“UV 工具包”(UV Toolkit)访问所有主要的 UV 任务。此外，可以在该编辑器的外部通过“建模”(Modeling)菜单集的“UV”菜单使用许多功能。 您可以在下面找到 UV 工具包特性和功能的快速视频概述，后跟其各种命令和工具的详细描述。

## UV 编辑器菜单

有关 UV 编辑器菜单项的列表，请参见 [UV 编辑器菜单栏](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单.md)。

## 视图栏

视图栏包含用于在“UV 编辑器”(UV Editor)和（有时）“视口”(Viewport)中更改 UV 壳显示的选项。

| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4A1113ED-F886-4A07-92B2-7160F1378B96.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-DA630F7E-CF94-4673-813C-CF7E155182E9.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **线框显示(Wireframe display)/着色显示(Shaded display)** | 将 UV 壳显示为未着色的线框或使用半透明着色显示 UV 壳。彩色着色选项位于[视图 > 着色(View > Shaded)](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29的“视图”%28View%29菜单.md)中。 |
|---|---|---|
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-6EF6E8DD-7A18-428C-BFF5-7091B93B2C74.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **扭曲着色器(Distortion Shader)** | 通过使用挤压和拉伸的 UV 来着色面，确定拉伸或压缩区域。请参见[识别 UV 扭曲](显示和选择%20UV/显示%20UV%20扭曲.md)。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-543E00DF-EA98-4E88-98E7-63FF921AB5A9.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **纹理边界(Texture Borders)** | 切换 UV 壳上纹理边界的显示。纹理边界显示有一条粗线。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-A5ACD26E-A6C2-4205-A15A-503382881ACF.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **彩色 UV 壳边界(Color UV Shell Borders)** | 将彩色 UV 边界的显示切换为任何选定组件。用于查找壳共享相同边的位置。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-7748D20F-FF5B-4BCE-872D-4B9D665DB74F.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **栅格 UV (Grid UVs)** | 将每个选定 UV 移动到纹理空间中其最近的栅格交点处。“UV > 栅格”(UV > Grid)的快捷方式。 若要更改栅格，请在工具栏上的“视图栅格”(View Grid)按钮上单击鼠标右键。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-FE25C995-A9F2-46BB-9CA2-31EED1693BF6.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **隔离选定 UV(Isolate selected UVs)** | 仅显示选定 UV 或与当前 UV 集中的 UV（如果未选择任何对象）。有关详细信息，请参见[显示 UV 的子集](显示和选择%20UV/显示%20UV%20的子集.md)。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-E904C041-31F5-464F-85FA-1C3D7CCD6FF8.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **保存图像(Save image)** | 将当前 UV 布局的图像保存到外部文件。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F1A1CC45-DD9C-4A33-8381-BFBC747B727A.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **图像(Image)** | 切换是否在“UV 编辑器”(UV Editor)中显示纹理。使用“棋盘格着色器”(Checker shader)按钮旁边的下拉列表在图像之间切换。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96307EC3-7425-4FA5-BEEB-40BAF69406D6.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **棋盘格着色器(Checker shader)** | 在 UV 编辑器中，将棋盘格图案纹理应用于 UV 网格的曲面和后面的 UV。请参见[将棋盘格图案着色器应用到 UV 网格](显示和选择%20UV/将棋盘格图案着色器应用到%20UV%20网格.md)。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-6298BE58-CC51-467D-8D94-C634A4381A8C.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> / ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-12E4DBC5-A853-4CDB-9D9A-471704B5E1DC.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **通道显示(Channel display)** | 显示 RGBA 或 Alpha 通道。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-1935BD8B-7F0C-41FE-8613-BABFBB581450.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **暗淡图像(Dim Image)** | 减小当前显示的背景图像的亮度。使用滑块可控制量。 “图像 > 暗淡”(Image > Dim)的快捷方式。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-E9E62905-E696-40D1-89CD-FF3A2359DF5B.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **过滤的图像(Filtered Image)** | 在硬件纹理过滤和明晰定义的像素之间切换背景图像。“图像 > 未过滤”(Image > Unfiltered)的快捷方式。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-94748642-FE92-4DEC-912D-B99D50CE3FD2.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **使用图像比(Use Image Ratio)** | 在显示方形纹理空间与显示与该图像具有相同的宽高比的纹理空间之间进行切换。“图像 > 图像比”(Image > Image Ratio)的快捷方式。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-960DB20F-FAE6-4369-8A4C-0D5A2F5040DA.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **像素捕捉(Pixel Snap)** | 选择是否自动将 UV 捕捉到像素边界。“图像 > 像素捕捉”(Image > Pixel Snap)的快捷方式。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-E6E1D59B-407D-418B-9315-69E84C40FB8D.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **UV 编辑器烘焙(UV Editor Baking)** | 烘焙纹理，并将其存储在内存中。“图像 > UV 编辑器烘焙”(Image > UV Editor Baking)的快捷方式。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-A9308C54-6096-431E-84D9-CE5C57E995C5.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **更新 PSD 网络(Update PSD Networks)** | 为场景刷新当前使用的 PSD 纹理。修改连接到 Maya PSD 节点（在 Maya 中）的 PSD 文件（在 Photoshop 中）时，可以在 Maya 中更新（刷新）图像以便立即显示修改。请参见“图像 > 更新 PSD 网络”(Image > Update PSD Networks)。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-0C938344-3473-45B9-B382-8AF1F2D36566.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **曝光(Exposure)** | 调整显示亮度。通过减小曝光，可查看默认在高光下看不见的细节。 单击图标在默认值和修改值之间切换。 这是一个诊断选项，不保存在场景中，也不应用于渲染输出。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D52ACE5A-B71A-42D6-A821-7386BC4D8B1C.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **Gamma** | 调整要显示的图像的对比度和中间调亮度。增加 Gamma 值，可查看图像阴影部分的细节。 单击图标在默认值和修改值之间切换。 这是一个诊断选项，不保存在场景中，也不应用于渲染输出。特别是，该选项在视图变换（如果有）之上应用，您无需将其设置为 2.2 以模拟 sRGB。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D17FFDCA-A95F-4FE2-8DA6-46BEFC3C593C.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" --> | **视图变换(View Transform)** | 控制从用于显示的工作颜色空间转化颜色的视图变换。此选项非常有用，例如，如果要快速检查原始颜色值或临时应用其他视图变换，可以使用此选项。可以选择的可用颜色空间取决于您使用 OCIO 配置文件进行颜色管理还是已定义用户变换。 单击该图标可暂时将视图变换切换到禁用状态，然后再切换到启用状态。 使用该下拉列表可选择其他视图变换。 这些是诊断选项，不保存在场景中，也不应用于渲染输出。 除非已启用颜色管理，否则它们将不可用。请参见[颜色管理](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5320733B-F9B6-4429-BCAA-F7251D77A8E2)。 |

## UV 工具包

默认情况下，“UV 工具包”(UV Toolkit)显示在 UV 编辑器的右侧，并包含修改 UV 排列所需的全部工具。对于具有附加选项的工具和命令，可以按住 Shift 键并单击该按钮以打开相应的选项窗口。您也可以在某些选项上单击鼠标右键来访问替代功能。

#### 选择遮罩(Selection masks) (![图：选择遮罩(Selection masks) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-BA524841-E41D-4DAC-B8BC-3F24DF060781.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

将选择限制为“顶点”(Vertices)、“边”(Edges)、“面”(Faces)、“UV”(UVs)或“UV 壳”(UV Shells)。双击任意图标可选择在“UV 编辑器”(UV Editor)中加载的所有该类组件。在任意图标上单击鼠标右键可取消选择在“UV 编辑器”(UV Editor)中加载的所有该类组件。

#### 选择方法(Selection method)

在拖动鼠标光标时切换选择方法。有关详细信息，请参见[选择工具(Select Tool)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-60FD5F79-AC1D-46DE-B66D-2FBE73E15A30)。

如果“移动工具”(Move Tool)或“缩放工具”(Scale Tool)处于活动状态，您还可以选择通过拖动来变换组件。

#### 对称(Symmetry)

激活对称选择。有关详细信息，请参见[激活或取消激活对称](../../多边形建模/多边形建模/编辑多边形/对称编辑/激活或取消激活对称.md)。

您可以使用“镜像 UV”(Mirror UVs)按钮 (![图：激活对称选择。有关详细信息，请参见激活或取消激活对称。 您可以使用“镜像 UV”(Mirror UVs)按钮 () 跨所…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4BA930E5-89E6-4365-BF02-C16CB4471511.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->) 跨所选对称轴快速镜像当前选择。有关详细信息，请参见[对称 UV](编辑%20UV/对称%20UV.md)。

![图：激活对称选择。有关详细信息，请参见激活或取消激活对称。 您可以使用“镜像 UV”(Mirror UVs)按钮 () 跨所…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-CC4F086B-5387-4CFC-BBE2-79D2D71291B7.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 选择约束(Selection Constraint)

限制可以选择的组件。选项包括：

- 背面(Back-facing)/前面(Front-facing)：UV [缠绕顺序](显示和选择%20UV/显示%20UV%20缠绕顺序.md)为逆时针或顺时针的组件。

- 几何体边界(Geometry Borders)：网格开口端上的组件。

- 纹理边界(Texture Borders)：UV 壳开口端上的组件。

- UV 循环边(UV Edge Loop)：（仅限“边选择”(Edge selection)模式）基于所单击边的整个 UV 循环边。

- UV 环形边(UV Edge Ring)：（仅限“边选择”(Edge selection)模式）基于所单击边的整个 UV 环形边。

- UV 壳(UV Shell)：基于所单击组件的整个 UV 壳。

![图：限制可以选择的组件。选项包括： 背面(Back-facing)/前面(Front-facing)：UV 缠绕顺序为逆时针…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-DA5CD4C7-1619-44A1-A673-80EBA2D46637.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 变换约束(Transform Constraint)

[移动(Move)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9BCE8B23-6DA6-4C7F-B897-7E25D6E8A865)、[旋转(Rotate)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C2D0F80C-812B-465D-A634-DB6ECFABFCB3)或[缩放工具(Scale Tool)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-487B6A23-E135-45E2-94F1-B0D59D6B6F33)可以临时激活此功能。

#### 修改选择(Modify Selection)按钮

这些按钮可用于以不同的方式修改当前选择。

- 全部(All)：选择当前所有的组件类型。

- 清除(Clear)：清除当前选择。

- 反转(Inverse)：选择所有未选定的组件，反之亦然。

- ![图：：沿相邻循环边移除或添加一个级别的组件。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-6A9331B3-64C4-4562-9B8F-B01CB24D25D5.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->：沿相邻循环边移除或添加一个级别的组件。

- ![图：：沿相邻面移除或添加一个级别的组件。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-3CE1F53C-16BE-447E-A7D7-80395CF139E8.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->：沿相邻面移除或添加一个级别的组件。

### 固定

使用以下选项可固定 UV，防止它们移动。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-2D6AD11F-6175-4C74-ACE0-E2B5114DF71F.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 固定(Pin) (![图：固定(Pin) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-1DFACB90-700E-4130-A495-28F6803A9EC1.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

锁定选定 UV，使其无法移动。默认情况下，网格的固定区域显示为蓝色。

#### 锁定工具(Pin Tool) (![图：锁定工具(Pin Tool) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-DC12B635-CD40-4977-BB0C-EAA2B6B3A942.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

用于在 UV 上绘制以将其锁定。按住 Shift 键并单击可打开[固定 UV 工具(Pin UV Tool)](UV%20参考/UV%20工具/固定%20UV%20工具%28Pin%20UV%20Tool%29.md)选项。

#### 反转固定(Invert Pinning) (![图：反转固定(Invert Pinning) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-577CFA62-916B-4296-8B2D-142AFDC290BD.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

取消固定当前固定的 UV，反之亦然。

#### 取消固定(Unpin) (![图：取消固定(Unpin) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-A1B9BCE1-09BA-4729-B798-FCF13BD684E4.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

解除锁定选定 UV。

#### 取消固定所有(Unpin All) (![图：取消固定所有(Unpin All) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-790947E0-0DAA-404F-B698-BB21ABE24DCE.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

解除锁定所有 UV。

## 按类型选择

使用以下选项可选择具有共同特点的所有 UV。

#### 背面(Back-Facing) (![图：背面(Back-Facing) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-5756D106-049B-40DF-B7E4-7BA59A09426F.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

[缠绕顺序](显示和选择%20UV/显示%20UV%20缠绕顺序.md)为逆时针的 UV。

#### 前面(Front-Facing) (![图：前面(Front-Facing) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-1F765750-050B-41B0-B666-280056973C96.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

[缠绕顺序](显示和选择%20UV/显示%20UV%20缠绕顺序.md)为顺时针的 UV。

#### 重叠(Overlapping) (![图：重叠(Overlapping) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-326916E4-47A1-40CA-8F88-4BE9FA3B3E11.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

面与网格上的其他面占据相同 UV 空间的 UV。

#### 非重叠(Non-Overlapping) (![图：非重叠(Non-Overlapping) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-DC5B983C-B5FD-408E-B88C-502E49A8BD66.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

面不与网格上的其他面占据相同 UV 空间的 UV。

#### 纹理边界(Texture Borders) (![图：纹理边界(Texture Borders) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-6A03DF75-D39B-440D-895A-E55F99327FE3.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

UV 壳开口端上的 UV。

#### 未映射(Unmapped) (![图：未映射(Unmapped) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4BA2FE9D-B460-4C0A-8B82-7B4587EE87B8.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

对应于未映射面的 UV。这有助于直观地确定任何未显示或未正确显示纹理贴图的区域。

## 软选择

用于选择和影响当前选择周围渐变上的 UV 范围。有关详细信息，请参见[选择工具(Select Tool)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-60FD5F79-AC1D-46DE-B66D-2FBE73E15A30)。

## 变换

使用以下选项可比标准变换工具更精确地移动 UV。

### 枢轴

允许设置用于变换工具的自定义枢轴。有关详细信息，请参见[更改枢轴点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-150B390E-840B-4FE3-B8E9-8DEBCE7CEC97)。

#### 枢轴(Pivot)

相对于当前“选择”(Selection)或“UV 区域”(UV Area)设置将枢轴移动到九个共用位置。

#### 选择(Selection)

处于活动状态时，枢轴按钮将相对于当前选择移动枢轴。

#### UV 区域(UV Area)

处于活动状态时，枢轴按钮将相对于由“U”和“V”字段指定的 UV 空间移动枢轴。

#### 编辑枢轴(Edit Pivot)

单击此选项，然后移动操纵器以手动定位枢轴。还可以使用 Insert 键启用和禁用此选项。

#### 重置(Reset)

将枢轴重置为其默认位置。

### 移动

允许以设置的增量旋转选定 UV

#### 移动方向(Move direction)

单击七个箭头按钮中的任何一个可在相应的方向上移动选定 UV。单击中间按钮以在相对于原来的位置移动组件与在 UV 空间中绝对地移动组件之间切换。

#### 移动输入字段(Move input field)

位于“移动方向”(Move direction)中心，此项指定在按下移动按钮之一时选定 UV 将移动的增量。可以通过在值上单击鼠标右键将其保存供以后使用（保存的值在下拉列表中可用）。

#### UV 输入字段(UV input fields)

![图：显示/设置选定 UV 在 UV 空间中的确切位置。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

显示/设置选定 UV 在 UV 空间中的确切位置。

#### 步长捕捉(Step Snap)

允许将 UV 捕捉到特定的 UV 空间增量。

#### 保留组件间距(Retain Component Spacing)

在移动时保持选定组件之间的相对距离。这在启用[捕捉](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7B4932A8-D3AF-4F52-81B6-9F2C7F8D9746)的情况下使用时尤其有用，因为如果不使用此选项，所有选定 UV 均会捕捉到同一位置（导致重叠）。

#### 分布(Distribute) (![图：分布(Distribute) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-E024D858-BF2D-4371-BBA8-06F1095F2C45.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

在 U 或 V 方向上均匀分布相邻的选定 UV。单击鼠标右键可按“移动输入字段”(Move input field)中的数值分布 UV。按住 Shift 键并单击可打开[“分布 UV”(Distribute UVs)选项](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单.md)。

![图：在 U 或 V 方向上均匀分布相邻的选定 UV。单击鼠标右键可按“移动输入字段”(Move input field)中的…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-990763CA-E5D1-4E6D-A442-E2A81CFD8143.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 工具

包含各种工具，可帮助更有效地围绕 UV 空间移动 UV。

#### 抓取(Grab) (![图：抓取(Grab) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-303E12DD-980F-4480-8489-04169665F3C2.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

选择 UV 并在基于笔刷的区域中沿拖动方向移动 UV。对于进行精细调整很有用。 按住 Shift 键并单击可打开[“抓取 UV 工具”(Grab UV Tool)选项](UV%20参考/UV%20工具/抓取%20UV%20工具%28Grab%20UV%20Tool%29.md)。

#### 晶格(Lattice) (![图：晶格(Lattice) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-CB37C260-756F-4B42-A323-60F54D2DCCA2.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

借助 [UV 晶格工具(UV Lattice Tool)](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29的“工具”%28Tool%29菜单/晶格工具%28Lattice%20Tool%29.md)，您可以通过围绕 UV 创建晶格（出于变形目的），将 UV 的布局作为组进行操纵。按住 Shift 键并单击可打开[使用“UV 晶格工具”(UV Lattice Tool)修改 UV 选项](编辑%20UV/使用“UV%20晶格工具”%28UV%20Lattice%20Tool%29修改%20UV.md)。

#### 收缩(Pinch) (![图：收缩(Pinch) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-8D1AB1D7-5BD5-455F-A5AE-EFE73C6C14CD.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

向工具光标的中心拉近顶点。对于更明晰地定义现有折痕很有用。 按住 Shift 键并单击可打开[“收缩 UV 工具”(Pinch UV Tool)选项](UV%20参考/UV%20工具/固定%20UV%20工具%28Pin%20UV%20Tool%29.md)。

#### 涂抹(Smear) (![图：涂抹(Smear) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-BD441811-DD9C-4D05-916C-A3A5E784A314.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

按与曲面上笔划方向的原始位置相切的方向移动 UV。 按住 Shift 键并单击可打开[“涂抹 UV 工具”(Smear UV Tool)选项](UV%20参考/UV%20工具/涂抹%20UV%20工具%28Smear%20UV%20Tool%29.md)。

#### 对称(Symmetrize) (![图：对称(Symmetrize) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-99A0FA0E-C082-42CC-BC23-A142F4F61AE8.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

根据拓扑对称的对应项在所选轴上镜像绘制的 UV。按住 Shift 键并单击可打开[“对称 UV 工具”(Symmetrize UV Tool)选项](UV%20参考/UV%20工具/对称%20UV%20工具%28Symmetrize%20UV%20Tool%29.md)。

### 旋转

允许按设置的增量旋转选定 UV。

#### 旋转输入(Rotate input)字段

指定按下移动按钮之一时选定 UV 将旋转的增量。可以通过在值上单击鼠标右键将其保存供以后使用（保存的值在下拉列表中可用）。

#### 逆时针旋转(Rotate Counterclockwise)/顺时针旋转(Rotate Clockwise) (![图：逆时针旋转(Rotate Counterclockwise)/顺时针旋转(Rotate Clockwise) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-924BA200-4EF2-49E5-AE82-D01B883B7C3C.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

单击相应的按钮可按在输入字段中指定的量旋转选定 UV。

#### 步长捕捉(Step Snap)

允许将 UV 捕捉到特定的 UV 空间增量。这与[旋转工具(Rotate Tool)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C2D0F80C-812B-465D-A634-DB6ECFABFCB3)中的“步长捕捉”(Step Snap)属性有关。

### 缩放

允许按设置的增量缩放选定 UV。

#### 缩放输入(Scale input)字段

指定按下移动按钮之一时选定 UV 将缩放的增量。可以通过在值上单击鼠标右键将其保存供以后使用（保存的值在下拉列表中可用）。

#### 缩放(Scale) (![图：缩放(Scale) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-B7E8902F-F9DD-4DFD-B45F-9B332CF82556.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

单击此按钮可按在输入字段中指定的量缩放选定 UV。可以通过激活相应的按钮将缩放锁定到特定方向。

#### 步长捕捉(Step Snap)

允许将 UV 捕捉到特定的 UV 空间增量。

#### 防止负比例(Prevent Negative Scale)

启用后，Maya 会禁用 UV 的负缩放。沿每个轴的缩放限制为正值。

#### 翻转(Flip) (![图：翻转(Flip) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-22C2FCC9-5E2C-4BE1-AB1B-BD5A9473DD7D.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

在指定方向上翻转选定 UV 的位置。有关详细信息，请参见[“翻转 UV”(Flip UV)选项](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/翻转%20UV%20选项%28Flip%20UVs%20options%29.md)。

### Texel 密度(Texel Density)

允许通过指定 UV 壳应该包含的 Texel 数（每单位像素数）快速设置 UV 壳的大小。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F33B1537-9257-4FEE-816D-DF812841D5C7.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 获取(Get)

显示选定 UV 壳的当前 Texel 密度。

#### 设定(Set)

缩放选定 UV 壳以适应指定的 Texel 密度。

#### 贴图大小(Map Size)

指定整个纹理的方形贴图大小。首先设置此大小，因为它用于计算 Texel 密度基值。

## 创建

使用以下选项可为选定网格创建新的 UV 映射。

#### 自动(Automatic) (![图：自动(Automatic) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-C186812A-4576-4FC0-8B3E-7D16D88A458A.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

尝试通过自动投影多个平面查找最佳 UV 放置。按住 Shift 键并单击可打开[“自动映射”(Automatic Mapping)选项](../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/自动映射选项%28Automatic%20Mapping%20options%29.md)。

#### 基于法线(Normal-Based) (![图：基于法线(Normal-Based) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-3D679A8E-BD0B-4D8A-BB1D-6D1FFE53E100.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

根据关联顶点的法线放置 UV。

#### 圆柱形(Cylindrical) (![图：圆柱形(Cylindrical) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-BD74C84B-91A0-45FD-9330-377D32880CBA.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

通过从周围的圆柱体投影 UV 将其放置。按住 Shift 键并单击可打开[“圆柱形映射”(Cylindrical Mapping)选项](../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/圆柱形映射选项%28Cylindrical%20Mapping%20options%29.md)。

#### 平面(Planar) (![图：平面(Planar) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-EC77076D-48F2-4397-BAC7-D37895D9466B.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

通过从平面投影 UV 将其放置。按住 Shift 键并单击可打开[“平面映射”(Planar Mapping)选项](../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/平面映射选项%28Planar%20Mapping%20options%29.md)。

#### 球形(Spherical) (![图：球形(Spherical) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-50A4631A-327D-4057-8FA7-BF67DA3B89ED.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

通过从周围的球体投影 UV 将其放置。按住 Shift 键并单击可打开[“球形映射”(Spherical Mapping)选项](../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/球形映射选项%28Spherical%20Mapping%20options%29.md)。

#### 最佳平面(Best Plane) (![图：最佳平面(Best Plane) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4CE127E6-9D20-4AF5-A046-2C3D3B537552.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

根据从指定顶点计算的平面，将 UV 指定给选择的面。

#### 基于摄影机(Camera-Based) (![图：基于摄影机(Camera-Based) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-1437E556-E7A1-47A1-8EE5-49B4A2B5254D.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

等同于平面投影，但使用当前摄影机作为平面。按住 Shift 键并单击可打开[基于摄影机的映射选项](../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/基于摄影机的映射选项%28Camera-Based%20Mapping%20options%29.md)。

#### 轮廓拉伸(Contour Stretch) (![图：轮廓拉伸(Contour Stretch) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-52138A4F-397A-4C7A-ADE6-45B4E81B6370.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

分析有四个角点的选择，确定如何以最佳方式在图像上拉伸多边形的 UV 坐标。按住 Shift 键并单击可打开[轮廓拉伸映射选项](../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/轮廓拉伸映射选项%28Contour%20Stretch%20Mapping%20options%29.md)。

## 切割和缝合(Cut and Sew)

使用以下选项可分离或接合 UV 壳。

#### 自动接缝(Auto-Seams) (![图：自动接缝(Auto-Seams) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-314768DC-E9DB-4F7E-9FD2-90FF073A8F78.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

尝试在选定网格或 UV 壳上查找要用作接缝的最佳边。按住 Shift 键并单击可打开[“自动接缝”(Auto Seams)选项](../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/自动接缝%28Auto%20Seams%29.md)。

#### 切割(Cut) (![图：切割(Cut) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-49B7D0BC-47E4-4B45-A470-DC09F17FCA94.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

沿选定边分离 UV，从而创建边界。有关详细信息，请参见[分离和附加 UV](编辑%20UV/分离和附加%20UV.md)。

#### 切割工具(Cut Tool) (![图：切割工具(Cut Tool) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-59131FE3-81C5-40EF-9E6A-8D18FA9A3281.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

允许通过在相邻边上单击 UV 将其分离。按住 Shift 键并单击可打开[切割 UV 工具(Cut UV Tool)](UV%20参考/UV%20工具/切割%20UV%20工具%28Cut%20UV%20Tool%29.md)选项。

![图：允许通过在相邻边上单击 UV 将其分离。按住 Shift 键并单击可打开切割 UV 工具(Cut UV Tool)选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F1361D3E-B779-4C48-AC71-543EF29D5F0B.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 创建 UV 壳(Create UV Shell) (![图：创建 UV 壳(Create UV Shell) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-0A64416A-6004-4183-82DE-60039087EE08.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

将连接到选定组件的所有面分离成一个新的 UV 壳。有关详细信息，请参见[创建 UV 壳](编辑%20UV/创建%20UV%20壳.md)。

#### 创建壳(栅格)(Create Shell (Grid)) (![图：创建壳(栅格)(Create Shell (Grid)) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-834A7026-09CC-43FF-B6E8-DF058BDBD8B0.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

通过沿当前选择的边周长切割，然后将 UV 均匀地分布到 0 到 1 的 UV 栅格空间，创建归一化的方形 UV 壳。

#### 缝合(Sew) (![图：缝合(Sew) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-422BA3A9-B526-429B-A4FA-B2C0FF2CB213.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

沿选定边界附加 UV，但不在编辑器视图中一起移动它们。按住 Shift 键并单击可打开[分离和附加 UV](编辑%20UV/分离和附加%20UV.md)。

#### 缝合工具(Sew Tool) (![图：缝合工具(Sew Tool) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-CA2D7EDB-8140-4620-842D-AB712BC1E15B.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

沿拖动的接缝焊接 UV。 按住 Shift 键并单击可打开[缝合 UV 工具(Sew UV Tool)](UV%20参考/UV%20工具/缝合%20UV%20工具%28Sew%20UV%20Tool%29.md)选项。

![图：沿拖动的接缝焊接 UV。 按住 Shift 键并单击可打开缝合 UV 工具(Sew UV Tool)选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D1CE3336-CC79-4B07-8A4F-47BD467C88FB.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 缝合到一起(Stitch Together) (![图：缝合到一起(Stitch Together) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-ABF5C3CB-F629-402F-B037-5A04FA713317.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

通过在指定方向上朝一个壳移动另一个壳，将两条选定边缝合在一起。

![图：通过在指定方向上朝一个壳移动另一个壳，将两条选定边缝合在一起。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D40020D5-0FF3-4ADC-9924-BCC5CFB8DABB.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

## 展开

使用以下选项可围绕接缝展开 UV。这特别适用于对称的有机对象。有关详细信息，请参见[展开 UV 网格](编辑%20UV/展开%20UV%20网格.md)。

#### 优化(Optimize) (![图：优化(Optimize) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-12ED58F2-6056-4EF1-BB59-F795D9ED2CE9.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

自动移动 UV 以改善纹理空间分辨率。按住 Shift 键并单击可打开[“优化 UV”(Optimize UVs)选项](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/优化%20UV%20选项%28Optimize%20UVs%20options%29.md)。

#### 优化工具(Optimize Tool) (![图：优化工具(Optimize Tool) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-67D8C3D5-33D5-46F7-AE75-83EB1EA4A2BD.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

通过在 UV 上拖动解开和松弛 UV 之间的间距。按住 Shift 键并单击可打开[“优化 UV 工具”(Optimize UV Tool)选项](UV%20参考/UV%20工具/“展开%20UV%20工具”%28Unfold%20UV%20Tool%29和“优化%20UV%20工具”%28Optimize%20UV%20Tool%29.md)。

#### 展开(Unfold) (![图：展开(Unfold) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-EC006B4F-BD99-4A28-B6AF-FB11E734CBC4.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

在尝试确保 UV 不重叠的同时，展开选定的 UV 网格。按住 Shift 键并单击可打开[“展开 UV”(Unfold UVs)选项](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/展开%20UV%20选项%28Unfold%20UVs%20options%29.md)。

#### 展开方向(Unfold Along) (![图：展开方向(Unfold Along) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-EC006B4F-BD99-4A28-B6AF-FB11E734CBC4.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

旧版算法。

#### 展开工具(Unfold Tool) (![图：展开工具(Unfold Tool) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-9570DE44-A1F8-4465-8312-7E3AB24E1254.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

通过在重叠 UV 上拖动将其展开和消除。按住 Shift 键并单击可打开[“展开 UV 工具”(Unfold UV Tool)选项](UV%20参考/UV%20工具/“展开%20UV%20工具”%28Unfold%20UV%20Tool%29和“优化%20UV%20工具”%28Optimize%20UV%20Tool%29.md)。

#### 拉直 UV(Straighten UVs) (![图：拉直 UV(Straighten UVs) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-246D7157-364E-48BF-B9CE-082EE147C85E.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

对齐其边在特定角度容差内的相邻 UV。按住 Shift 键并单击可调整轴和角度容差以便拉直。有关详细信息，请参见[拉直 UV](编辑%20UV/拉直%20UV.md)。

#### 拉直壳(Straighten Shell) (![图：拉直壳(Straighten Shell) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-871CF2E9-87F5-4F5B-AF7E-75A82488D251.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

尝试沿 UV 壳的边界/在 UV 壳的边界内解开所有 UV。若要正确使用该工具，必须选择一组包含到一个 UV 壳的内部或边界 UV（但不能同时选择两者）。使用内部 UV 时，它们还必须沿同一循环边。

![图：尝试沿 UV 壳的边界/在 UV 壳的边界内解开所有 UV。若要正确使用该工具，必须选择一组包含到一个 UV 壳的内部或…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-65B74AC7-6C7B-4B74-9F81-F37BF16D86D5.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

在上述示例中，A 和 C 有效，因为它们包含所有边界或内部 UV 且全部沿同一循环边。相反，B 无效，因为它同时包含边界和内部 UV 以及两条不同的边循环，而 C 无效是因为 UV 跨多个 UV 壳。有关详细信息，请参见[拉直 UV](编辑%20UV/拉直%20UV.md)￼。

## 对齐和捕捉

使用以下选项可定位 UV 并使其彼此对齐。

#### 对齐(Align) (![图：对齐(Align) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-52BC6D2F-5F69-4202-81BB-E17111B245A1.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

对齐所有选定 UV，使其在指定方向上共面。对齐将在指定方向上相对于距离最远的选定 UV 进行。有关详细信息，请参见[拉直 UV](编辑%20UV/拉直%20UV.md)。

#### 线性对齐(Linear Align) (![图：线性对齐(Linear Align) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D5555F5E-4219-4D9D-8C9F-CD8C6AB1A2E3.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

沿穿过所有选定 UV 的线性趋势线对齐这些 UV。

#### 捕捉(Snap)

将选定 UV 壳移动到指定 UV 空间中的九个位置之一。

![图：将选定 UV 壳移动到指定 UV 空间中的九个位置之一。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F724EE3A-2E82-4840-B1CB-1E265F5EB7A1.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 捕捉到一起(Snap Together) (![图：捕捉到一起(Snap Together) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-2CF73EFF-47ED-49A3-9A15-B256A36F6998.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

通过使选定 UV 相互重叠，将一个 UV 壳移动到另一个 UV 壳。您可以通过相应的按钮选择捕捉方向（按选择顺序）。

#### 捕捉和堆叠(Snap & Stack) (![图：捕捉和堆叠(Snap & Stack) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-FD6EAD41-E088-4507-9F7B-AE9B6B38B593.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

通过使选定 UV 相互重叠，将多个 UV 壳移动到另一个 UV 壳之上。壳始终朝最后一个选定 UV 移动。

#### 匹配栅格(Match Grid) (![图：匹配栅格(Match Grid) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F6F196DC-B6A9-458E-92C0-BEA2EAC9F888.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

将每个选定 UV 移动到 UV 空间中其最近的栅格交点处。按住 Shift 键并单击可打开[“栅格 UV”(Grid UVs)选项](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/“匹配栅格”%28Match%20Grid%29选项.md)。

#### 匹配 UV(Match UVs) (![图：匹配 UV(Match UVs) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-EE81DC5B-C047-4693-BA9A-8CEFF11E31AA.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

将特定容差距离内的选定 UV 移动到所有各个位置的平均位置。按住 Shift 键并单击可调整“容差”(Tolerance)。

还可以选择多个壳以匹配其中的 UV。如果您有两个彼此堆叠的几乎相同的壳，而您希望使其完全相同，这将非常有用。

![图：将特定容差距离内的选定 UV 移动到所有各个位置的平均位置。按住 Shift 键并单击可调整“容差”(Tolerance…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-BF03A9F2-3F13-4771-AA62-F6C860F9138F.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 归一化(Normalize) (![图：归一化(Normalize) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-C31DD43E-21A5-41B1-9DD8-10A6265F6E92.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

缩放选定 UV 以适配 0 到 1 的 UV 空间。单击鼠标右键可缩放 UV，使其所有面填充 0 到 1 的 UV 空间。按住 Shift 键并单击可打开[“归一化 UV”(Normalize UVs)选项](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/归一化%20UV%20选项%28Normalize%20UVs%20options%29.md)。

## 排列和布局

使用以下选项可定位 UV 并使其彼此对齐。

#### 分布(Distribute)

在所选方向上分布（请参见上文）选定 UV 壳，同时确保 UV 壳之间相隔一定数量的单位。您也可以使用“目标”(Target)按钮沿上一个选定壳（即：目标壳）的方向均匀分布它们。

#### 定向壳(Orient Shells) (![图：定向壳(Orient Shells) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-0E6FD8E3-ABB6-45B9-94B2-3E63C8CA2F67.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

旋转选定 UV 壳，使其与最近的相邻 U 或 V 轴平行。

![图：旋转选定 UV 壳，使其与最近的相邻 U 或 V 轴平行。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-A81B6B08-EA16-47D9-B65A-52EE47239459.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 定向到边(Orient to Edges) (![图：定向到边(Orient to Edges) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-279F2C3C-5C09-491F-BF2C-7A7E7B7DEB43.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

旋转选定 UV 壳，使其与选定边平行。

#### 堆叠壳(Stack Shells) (![图：堆叠壳(Stack Shells) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-12EE2740-03B9-49CD-94B4-1FC45327E224.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

将所有选定 UV 壳移动到 UV 空间的中心，使其重叠。

![图：将所有选定 UV 壳移动到 UV 空间的中心，使其重叠。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-56AF1DF6-42B9-48D0-A8D6-087E602D2959.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 取消堆叠壳(Unstack Shells) (![图：取消堆叠壳(Unstack Shells) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-3BC34CA4-4EDE-42AE-8698-B74F927785CE.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

移动所有选定 UV 壳，使其不再重叠且相互靠近。按住 Shift 键并单击可打开“取消堆叠选项”(Unstack Options)，允许您翻转已反转的 UV 壳。

#### 堆叠和定向(Stack & Orient) (![图：堆叠和定向(Stack & Orient) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-1364B87E-7E57-4671-A874-06661624AB44.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

将选定 UV 壳堆叠到 UV 空间的中心，然后旋转，使其与最近的相邻 U 或 V 轴平行。

![图：将选定 UV 壳堆叠到 UV 空间的中心，然后旋转，使其与最近的相邻 U 或 V 轴平行。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-B6A4A0E3-2253-465C-B65C-7C4D46DE482D.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 堆叠类似(Stack Similar) (![图：堆叠类似(Stack Similar) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-E2E26276-1112-486A-B761-5A72116E6EDF.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

仅将拓扑类似的壳彼此堆叠。按住 Shift 键并单击可打开“堆叠类似”(Stack Similar)选项。

![图：仅将拓扑类似的壳彼此堆叠。按住 Shift 键并单击可打开“堆叠类似”(Stack Similar)选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-8E29639D-D2B8-4DCD-AFFE-ED150CC179AB.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 容差(Tolerance)

确定两个壳的拓扑必须匹配至何种程度才能进行堆叠。

#### 选择堆叠壳(Select Stacked Shells)

选择在“堆叠类似”(Stack Similar)操作完成后已堆叠的所有壳。

#### 聚集壳(Gather Shells) (![图：聚集壳(Gather Shells) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-975B617D-EBB5-4410-8F94-EE37A5322820.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

将选定 UV 壳移回到 0 到 1 的 UV 范围。

![图：将选定 UV 壳移回到 0 到 1 的 UV 范围。 注： 为了保持 UV 布局，壳将以 1.0 个单位为步长偏移。因此…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-A9685DD2-B8D1-4CF8-A6E8-F1F0F6F5BDCF.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

**注**

为了保持 UV 布局，壳将以 1.0 个单位为步长偏移。因此，在

“聚集”(Gather)

操作之后，壳可能跨越 0-1 UV 空间的边界。

#### 随机化壳(Randomize Shells) (![图：随机化壳(Randomize Shells) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-9E89D9C5-6392-40DB-94B1-D65735EFA3C1.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

随机化 UV 壳平移、旋转和缩放。您可以通过“随机化壳选项”(Randomize Shells options)窗口（按住 Shift 键并单击）调整各个方向和允许的最大平移、旋转、缩放量。

![图：随机化 UV 壳平移、旋转和缩放。您可以通过“随机化壳选项”(Randomize Shells options)窗口（按…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-166842DF-4821-4024-8696-FE1B82B922C9.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 测量(Measure) (![图：测量(Measure) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-02867278-78DB-4042-A230-74D6CFBCE14F.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

显示两个选定 UV 的所选度量。选项包括：

- U 距离(U Distance)：U 轴方向上 UV 之间的单位数。

- V 距离(V Distance)：V 轴方向上 UV 之间的单位数。

- 像素距离(Pixel Distance)：打开一个窗口，其中基于许多可能的不同贴图大小显示各方向上两个最远 UV 之间的像素数量。

- 夹角(Angle Between)：两个选定 UV 之间的角度（选择多个 UV 将产生不一致的结果）。

#### 排布(Layout) (![图：排布(Layout) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-8B9AA3F1-DF5D-450D-A3A9-5450AB8C6F79.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

自动排列 UV 壳以最大限度地使用 0 到 1 的 UV 空间。按住 Shift 键并单击可打开[“排布 UV”(Layout UVs)选项](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/布局%20UV%20选项%28Layout%20UVs%20options%29.md)。

![图：自动排列 UV 壳以最大限度地使用 0 到 1 的 UV 空间。按住 Shift 键并单击可打开“排布 UV”(Layo…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F8B30822-91BE-4698-BFBE-A5376B23BC9B.gif) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 排布方向(Layout Along) (![图：排布方向(Layout Along) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-8B9AA3F1-DF5D-450D-A3A9-5450AB8C6F79.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

自动排列 UV 壳以最大限度地使用指定方向上的 UV 空间。

## UV 集

可用于为场景中的对象创建和控制 [UV 集](UV%20集.md)。有关详细信息，请参见[“UV 集”(UV Sets)菜单](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29的“UV%20集”%28UV%20Sets%29菜单.md)。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-1604C1C1-BB98-4358-8960-DB66C72BBB9E.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->

#### 创建空 UV 集(Create empty UV set) (![图：创建空 UV 集(Create empty UV set) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-8A8CAEA5-F4DF-414A-8A42-C6EE5AB72F17.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

在当前对象上创建一个新的空 UV 集。然后可以使用其中一种映射/投影方法在集中创建 UV。还可以通过在“UV 集”(UV Set)列表上单击鼠标右键来访问此命令。

#### 将 UV 复制到剪贴板(Copy UVs to clipboard) (![图：将 UV 复制到剪贴板(Copy UVs to clipboard) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-449BC7DC-288B-4D20-93B4-452A6250EFF7.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

将当前 UV 布局复制到剪贴板

#### 将剪贴板中的 UV 粘贴到当前 UV 集(Paste UVs from clipboard to current UV set) (![图：将剪贴板中的 UV 粘贴到当前 UV 集(Paste UVs from clipboard to current UV …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-27C19D47-471E-47CE-AB1B-7BF3B3B3593D.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

将剪贴板中的 UV 布局粘贴到选定 UV 集。

#### 复制 UV 集(Duplicate UV set) (![图：复制 UV 集(Duplicate UV set) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-678E1F80-E315-419B-9DEB-910D23FFFA77.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

创建选定 UV 集的相同副本。

#### 传播 UV 集(Propagate UV set) (![图：传播 UV 集(Propagate UV set) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-406BDF56-E1A4-41EA-B2BD-4E69DD839B04.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

将“UV 集”(UV Set)列表中的选定 UV 集指定给场景中的选定对象。选定的 UV 集成为那些对象的活动 UV 集。

#### “UV 集”(UV Set)列表

可用于控制选定对象后将显示哪个 UV 集。若要显示特定的 UV 集，请在左列中选择其所属的对象，然后在右列中选择特定的 UV 集。

通过在右列中的 UV 集名称上单击鼠标右键，可以选择在列表中更改其位置，将 UV 复制到另一个集，复制或删除该集，或者生成该集的 [UV 快照](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29的“图像”%28Image%29菜单.md)。

**注**

Maya 将不允许您删除

“UV 集”(UV Set)

列表中的最上方条目。如果需要删除此条目，可以将其移至列表中更低的位置，然后将其删除。

#### 共享实例(Share instances) (![图：共享实例(Share instances) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-486D610B-77CA-4B3F-88AB-8939310A6D8B.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

选择要共享的多边形，后跟要共享的实例。

#### 选择共享实例(Select shared instances) (![图：选择共享实例(Select shared instances) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-8D3117C2-D5C6-4582-B713-7464E7686B86.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

选择与选定实例共享 UV 集系列的实例。

#### 打开关系编辑器(Open Relationship Editor) (![图：打开关系编辑器(Open Relationship Editor) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-8939BF71-204E-4B9E-8247-84104F41C366.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

在“UV 链接”(UV Linking)模式下打开[关系编辑器(Relationship Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3DA58150-A73D-403E-A988-798DED4956BD)。

#### 自动加载纹理(Auto-load Textures) (![图：自动加载纹理(Auto-load Textures) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-2A61FF1D-F0C0-4CFB-868B-CFEB9E90D3E9.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

加载选定 UV 集的链接纹理。

#### 保存图像文件(Save image file) (![图：保存图像文件(Save image file) ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-E904C041-31F5-464F-85FA-1C3D7CCD6FF8.png) <!-- baize:img-hook downloaded=false reason="正文 10110 字 ≥300，非承重" -->)

导出选定 UV 集的 [UV 快照](UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29的“图像”%28Image%29菜单.md)。

## 相关主题

- [什么是 UV？](../UV.md)

- [创建 UV](创建%20UV.md)

- [查看 UV 并解算](查看%20UV%20并求值.md)
