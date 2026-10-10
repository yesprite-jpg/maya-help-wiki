# polySmoothFace

使用“网格 > 平滑”(Mesh > Smooth)命令平滑网格时，会创建 polySmoothFace 节点。

#### 方法(Method)

“指数”(Exponential)和“线性”(Linear)平滑方法都是均匀平滑，但它们对结果拓扑提供不同的控制。例如，“指数”(Exponential)可选择保持软边和硬边，而“线性”(Linear)可选择更好地控制结果面的数量。请参见[指数多边形平滑历史](polySmoothFace.md#GUID-EF5DE1E7-329D-4354-9D9E-BE8AFD1BE3A6__SECTION_C984CA08DFC44FF1B96C3B62B6D24C1D)和[线性多边形平滑历史](polySmoothFace.md#GUID-EF5DE1E7-329D-4354-9D9E-BE8AFD1BE3A6__SECTION_FC2FC0E932FE49CCBB9CBC75C5FF5B7D)。

## 指数多边形平滑历史

#### 细分类型(Subdivision Type)

允许您选择用于平滑网格的算法。根据您选择的“细分类型”(Subdivision Type)，会显示不同的选项。

#### OpenSubdiv Catmull-Clark

（默认）使用 Maya 的 OpenSubdiv 库实施平滑网格的面。请参见 [OpenSubdiv 概述](../../编辑多边形/平滑多边形/OpenSubdiv%20概述.md)。

“OpenSubdiv Catmull-Clark”对网格面应用统一的细化方案。

有关“OpenSubdiv Catmull-Clark”选项的详细信息，请参见 [OpenSubdiv 控件](polySmoothFace.md#GUID-EF5DE1E7-329D-4354-9D9E-BE8AFD1BE3A6__SECTION_9968881EA5124F759D9786EB9D638050)。

#### Maya Catmull-Clark

使用 Maya 的 Catmull-Clark 算法实施平滑网格的面。

有关“Maya Catmull-Clark”选项的详细信息，请参见 [Maya Catmull-Clark 控件](polySmoothFace.md#GUID-EF5DE1E7-329D-4354-9D9E-BE8AFD1BE3A6__SECTION_88A104096A874298B969D0FED5293B70)。

**注**

在 Maya 2014 和更早的版本中，

“Maya Catmull-Clark”

是默认的

“细分类型”(Subdivision Type)

。

#### 分段级别(Division levels)

Maya 执行平滑的次数。该值越大，网格就越平滑，且生成的面也越多。

## OpenSubdiv 控件

只有当选择的“细分类型”(Subdivision Type)为“OpenSubdiv Catmull-Clark”时，以下选项才可用。

#### 顶点边界(Vertex Boundary)

控制如何对边界边和角顶点进行插值。

**注**

重要：

当使用

“OpenSubdiv Catmull-Clark”

细分类型时，角为两个边相交的网格区域。

#### 锐边和角(Sharp edges and corners)

（默认）边和角在平滑后保持为锐边和角。

在以下示例中，边和双边角均为尖锐。

![图：（默认）边和角在平滑后保持为锐边和角。 在以下示例中，边和双边角均为尖锐。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-C11AD261-DF3D-41F6-A55D-4CDA9868F139.png) <!-- baize:img-hook downloaded=false reason="正文 2668 字 ≥300，非承重" -->

#### 锐边(Sharp edges)

边在平滑后保持为锐边。角已进行平滑。

在以下示例中，边为锐边，但双边角已进行平滑。

![图：边在平滑后保持为锐边。角已进行平滑。 在以下示例中，边为锐边，但双边角已进行平滑。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-33CC24A4-805E-4F01-88EC-92AF62D39339.png) <!-- baize:img-hook downloaded=false reason="正文 2668 字 ≥300，非承重" -->

#### UV 边界(UV Boundary)

控制如何将平滑应用于边界 UV。

**注**

重要：

当使用

“OpenSubdiv Catmull-Clark”

细分类型时，角为两个边相交的网格区域。

#### 无(None)

不平滑 UV。

#### 保留边和角(Preserve edges and corners)

平滑 UV。边和角在平滑后保持为锐边和角。

在以下示例中，边界边和双边角均为尖锐。

![图：平滑 UV。边和角在平滑后保持为锐边和角。 在以下示例中，边界边和双边角均为尖锐。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-BDA1E4D7-0684-4846-B168-97B9FA311BEB.png) <!-- baize:img-hook downloaded=false reason="正文 2668 字 ≥300，非承重" -->

#### 保留边(Preserve edges)

平滑 UV 和角。边在平滑后保持为锐边。

在以下示例中，边界边为锐边，但双边角已进行平滑。

![图：平滑 UV 和角。边在平滑后保持为锐边。 在以下示例中，边界边为锐边，但双边角已进行平滑。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-B83277BB-F8C3-434C-ACD8-963834BE7157.png) <!-- baize:img-hook downloaded=false reason="正文 2668 字 ≥300，非承重" -->

#### Maya Catmull-Clark

（默认）启用时，平滑不连续边界上的顶点附近的面变化数据（UV 和颜色集）。不连续边界上的顶点将按锐化规则细分（对其插值）。

![图：（默认）启用时，平滑不连续边界上的顶点附近的面变化数据（UV 和颜色集）。不连续边界上的顶点将按锐化规则细分（对其插值）…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-DC5C3E6B-43D2-4609-9503-26B2B22BA9D9.png) <!-- baize:img-hook downloaded=false reason="正文 2668 字 ≥300，非承重" -->

**注**

Maya Catmull-Clark

“UV 边界平滑”(UV Boundary Smoothing)

会与

Maya Catmull-Clark

控件中的

“平滑内部”(Smooth Internal)

选项产生相同的结果。

#### 传播 UV 角(Propagate UV Corners)

启用后，原始网格的面变化数据（UV 和颜色集）会应用到平滑网格的 UV 角。默认设置为禁用。

#### 平滑三角形(Smooth Triangles)

启用后（默认），会将细分规则应用到网格，从而使三角形的细分更加平滑。

#### 折痕方法(Crease Method)

控制如何对边界边和顶点进行插值。

#### 正常(Normal)

（默认）不应用折痕锐度平滑。

#### Chaikin

启用后，对关联边的锐度进行插值。在细分折痕边后，结果边的锐度通过 Chaikin 的曲线细分算法确定，该算法会产生半锐化折痕。此方法可以改进各个边具有不同边权重的多边折痕的外观。

## Maya Catmull-Clark 控件

只有当选择的“细分类型”(Subdivision type)为“Maya Catmull-Clark”时，以下选项才可用。

#### 连续性(Continuity)

此处输入的值可确定平滑度。

![图：此处输入的值可确定平滑度。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-5CC5CD58-55FE-4D70-BB28-83AD22840D8B.png) <!-- baize:img-hook downloaded=false reason="正文 2668 字 ≥300，非承重" -->

#### 平滑 UV (Smooth UVs)

对 UV 应用与顶点相同的平滑操作。默认情况下，“平滑 UV”(Smooth UVs)处于启用状态，这样可以为 UV 提供更好的结果。

如果要保持与在旧版 Maya 中创建的场景的兼容性，或者 UV 无需进行平滑但您希望提高性能，则禁用“平滑 UV”(Smooth UVs)。

#### 保留几何体边界(Preserve Geometry Borders)

启用该选项（默认）时，将保留网格的边界边的属性。它控制 PolySmoothFace 节点的“保持边界”(Keep Border)属性。

![图：启用该选项（默认）时，将保留网格的边界边的属性。它控制 PolySmoothFace 节点的“保持边界”(Keep Bo…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-BA5EB5B9-FC40-4878-BD8F-C89F8CF5B01A.png) <!-- baize:img-hook downloaded=false reason="正文 2668 字 ≥300，非承重" -->

#### 保留选择边界(Preserve Selection Borders)

启用该选项（默认）时，将保留设定选定面和未选定面的边界的边的属性。

![图：启用该选项（默认）时，将保留设定选定面和未选定面的边界的边的属性。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-C4F2E6E8-3AAD-442F-9B8F-085F62A1E2F4.png) <!-- baize:img-hook downloaded=false reason="正文 2668 字 ≥300，非承重" -->

#### 保留硬边(Preserve Hard Edges)

保留任何手动硬化或软化的现有边的属性。如果已更改边的硬度或柔和度（“网格显示 > 软化边”(Mesh Display > Soften Edge)或“网格显示 > 硬化边”(Mesh Display > Harden Edge)），则启用此选项以保持这些设置。

#### 传播边的软硬性(Propagate Edge Hardness)

将边的软硬性值从原始网格上的任何硬化边复制到平滑网格预览上关联的新边。默认设置为禁用。

#### 保留细分(Preserve Tessellation)

启用该选项，以便更改历史节点时，平滑节点不会重做细分，而只重新定位已生成的顶点。

#### 保留贴图边界(Preserve Map Borders)

控制“平滑 UV”(Smooth UVs)处于启用状态时如何平滑边界。

#### 全部(All)

平滑所有 UV 边界。

#### 内部(Internal)

（默认）平滑内部边界。这是默认设置。

#### 无(None)

不平滑边界。

#### 边界规则(Boundary Rules)

通过该选项，可以设置在平滑网格时要将折痕应用于边界边和顶点的方式。

#### 旧版(Legacy)

不将折痕应用于边界边和顶点。

#### 折痕全部(Crease All)

（默认设置）在转化为平滑网格之前为所有边界边以及只有两条关联边的所有顶点应用完全折痕。

#### 折痕边(Crease Edges)

仅为边应用完全折痕。

## 线性多边形平滑历史

有关“线性控制”(Linear Controls)的详细信息，请参见“平滑”(Smooth)选项中的[“线性控制”(Linear Controls)](../“建模”%28Modeling%29菜单集/“网格”%28Mesh%29菜单/平滑选项%28Smooth%20Options%29.md#GUID-4D094DC4-9027-4422-9083-6C9D2FE4036E__WS17956D7ADBC6E736-2B54A37117AE335115-7FFA)。
