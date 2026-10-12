# 2D 放置(2d Placement)

定义一个纹理帧 - 显示纹理的曲面（在 UV 坐标空间中）上的矩形区域。可以使用[覆盖](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-94070C7E-C550-42FD-AFC9-FBE82B173B1D.htm#GUID-94070C7E-C550-42FD-AFC9-FBE82B173B1D__WS1A9193826455F5FF-4F542F6211C79DEA861-1779)、[平移帧](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-94070C7E-C550-42FD-AFC9-FBE82B173B1D.htm#GUID-94070C7E-C550-42FD-AFC9-FBE82B173B1D__WS17956D7ADBC6E73638876AF8117AE33FA94-7ED9)和[旋转帧](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-94070C7E-C550-42FD-AFC9-FBE82B173B1D.htm#GUID-94070C7E-C550-42FD-AFC9-FBE82B173B1D__WS17956D7ADBC6E73638876AF8117AE33FA94-7ED8)属性在曲面上控制该帧的位置、大小和旋转。还可以使用下述属性控制如何在帧内平铺纹理。

“属性编辑器”(Attribute Editor)中的两列框表示 U 值和 V 值。

在“创建”(Create)选项卡中找到该工具（请参见[“创建”(Create)选项卡](../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)）。

若要使用该工具，请参见[使用 2D 放置工具](../../../渲染节点工具/使用“2D%20放置”%282d%20Placement%29工具.md)。

**注**

若要创建没有其对应 place2DTexture 节点的纹理节点，请从

Hypershade

菜单禁用

“创建 > 创建选项 > 包括带纹理的放置”(Create > Create Options > Include Placement with Textures)

。

#### 交互式放置(Interactive Placement)

显示纹理放置操纵器。从“属性编辑器”(Attribute Editor)中单击该按钮或在主窗口中单击“纹理放置工具”(Texture Placement Tool)图标，然后选择曲面。使用鼠标中键拖动操纵器控制柄以放置纹理。

#### 覆盖(Coverage)

指定纹理贴图覆盖的曲面比率。对于 NURBS 曲面而言，有效范围是 0 到 + 无限。值 1（默认）将在 U 或 V 方向上覆盖整个曲面。

例如，若要覆盖一半曲面，则应将 U 和 V 方向上的值都设定为 0.5。

![图：指定纹理贴图覆盖的曲面比率。对于 NURBS 曲面而言，有效范围是 0 到 + 无限。值 1（默认）将在 U 或 V 方…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-8C135698-413F-4ADB-9273-F77CD73C9AB0.png) <!-- baize:img-hook downloaded=false reason="正文 1487 字 ≥300，非承重" -->

#### 平移帧(Translate Frame)

“平移”(Translate)属性将纹理贴图放置于曲面上，并沿曲面移动覆盖区域。范围是 - 无限到 + 无限。

![图：“平移”(Translate)属性将纹理贴图放置于曲面上，并沿曲面移动覆盖区域。范围是 - 无限到 + 无限。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-23B8F817-AFAB-4729-BDDF-521CA1445979.png) <!-- baize:img-hook downloaded=false reason="正文 1487 字 ≥300，非承重" -->

#### 旋转帧(Rotate Frame)

在曲面上旋转纹理贴图。该属性用度表示。

#### U 向镜像(Mirror U)、V 向镜像(Mirror V)

仅当“U 向重复”(U Repeat) 或“V 向重复”(V Repeat) 属性值大于 1 时才适用。分别在 U 方向和 V 方向进行镜像。启用后，将对重复区域进行镜像 - 图像行显示为自身的镜像图像。这有助于掩饰重复区域之间的接缝效果。

![图：仅当“U 向重复”(U Repeat) 或“V 向重复”(V Repeat) 属性值大于 1 时才适用。分别在 U 方向…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-6175FA98-F1BD-4292-BE36-0C3B6A9C1681.png) <!-- baize:img-hook downloaded=false reason="正文 1487 字 ≥300，非承重" -->

#### 交错(Stagger)

Maya 对重复的贴图执行偏移操作，使得其他一些重复行正好偏移一半（例如砖墙）。禁用后，这些重复沿水平和垂直方向排列。

#### U 向折回(Wrap U)、V 向折回(Wrap V)

“U 向折回”(Wrap U)和“V 向折回”(Wrap V)属性控制映射是在 U 方向或 V 方向上重复，还是在 U 和 V 方向上重复。默认情况下，两个“折回”(Wrap)属性均处于启用状态。禁用这些选项以避免在闭合曲面上（例如，圆柱体或球体）显示接缝，或在您使用“转换”(Translation)和“覆盖”(Coverage)属性将限制映射到非常具体的曲面区域时避免纹理复制其自身。

#### UV 向重复(Repeat UV)

指定纹理贴图在覆盖区域内沿 U 或 V 方向（根据纹理）映射的副本数量。默认情况下，Maya 映射纹理的一个副本。大于 1 的值将导致在同一覆盖区域中显示更多贴图副本。小于 1 的值将导致仅显示贴图的部分。

![图：指定纹理贴图在覆盖区域内沿 U 或 V 方向（根据纹理）映射的副本数量。默认情况下，Maya 映射纹理的一个副本。大于 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-CC106202-486F-4A4F-84EA-B359A7B94E31.png) <!-- baize:img-hook downloaded=false reason="正文 1487 字 ≥300，非承重" -->

#### 偏移(Offset)

偏移纹理贴图的图案。这特别适用于曲面上图案放置的微调。“U 向偏移”(U Offset)沿 U 方向偏移纹理图案；“V 向偏移”(V Offset)沿 V 方向偏移纹理图案。每个值的范围都是 - 无限到 + 无限。

#### UV 向旋转(Rotate UV)

由于不能使用交互式工具旋转曲面放置，因此请使用该属性。“UV 向旋转”(Rotate UV)以度为单位进行计算。有效范围是 0 到 360 度。

#### UV 向噪波(Noise UV)

U 和 V 向的 2D 噪波。置换纹理贴图的颜色。

#### 快速(Fast)

启用时，“快速”(Fast)将检查放置是否为默认，并检查是否所有着色时间求值过程都执行较少的计算。启用“快速”(Fast)，可略微提高渲染速度。默认情况下，“快速”(Fast)处于禁用状态。
