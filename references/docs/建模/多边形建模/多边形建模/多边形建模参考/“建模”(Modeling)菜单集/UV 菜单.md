# UV 菜单

- 位于“建模”(Modeling)[菜单集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D90A2BDB-FD05-4528-8A95-C33A02D15129)中。

## 编辑器(Editors)

#### UV 编辑器(UV Editor)

显示 UV 编辑器。

请参见 [UV 编辑器概述](../../../../UV/UV/“UV%20编辑器”%28UV%20Editor%29概述.md)、[UV 编辑器菜单栏](../../../../UV/UV/UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单.md)和 [UV 编辑器标记菜单](../../../../UV/UV/UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器标记菜单.md)。

#### UV 集编辑器(UV Set Editor)

显示 UV 集编辑器。请参见[UV 集编辑器](../../../../UV/UV/UV%20参考/UV%20窗口和编辑器/UV%20集编辑器%28UV%20Set%20Editor%29.md)。

## 创建(Create)

#### 指定棋盘格着色器(Assign Checker Shader)

在投影 UV 纹理坐标时，将具有棋盘格纹理的着色器指定给选定的网格。这有助于通过提供已知视觉参照来确定 UV 的对齐。默认设置为禁用。

#### 自动(Automatic)

同时从多个角度将 UV 纹理坐标投影到选定对象上。一个“自动映射投影”(Automatic Mapping Projection)操纵器显示在选定对象周围，以便进行更精确的 UV 投影。

选择“UV > 自动”(UV > Automatic) > ![图：选择“UV 自动”(UV Automatic) 可设置“自动映射选项”(Automatic Mapping option…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2217 字 ≥300，非承重" --> 可设置[“自动映射选项”(Automatic Mapping options)](UV%20菜单/自动映射选项%28Automatic%20Mapping%20options%29.md)。

#### 最佳平面纹理工具(Best Plane Texturing Tool)

根据从指定顶点计算的平面，将 UV 指定给选择的面。

**注**

务必选择所有面，然后再调用工具，或者明确将选择遮罩设置为“多边形”(Polygon)。否则会发生选择问题。一次对一个图形使用“最佳平面纹理工具”(Best Plane Texturing Tool)。您仍然可以使用来自不同图形的顶点定义平面。

#### 基于摄影机(Camera-Based)

基于当前摄影机视图为选定对象创建 UV 纹理坐标作为平面投影。也就是说，摄影机视图成为投影的平面。

选择“UV > 基于摄影机”(UV > Camera-Based) > ![图：选择“UV 基于摄影机”(UV Camera-Based) 可设置“基于摄影机的映射选项”(Camera-Based M…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2217 字 ≥300，非承重" --> 可设置[“基于摄影机的映射选项”(Camera-Based Mapping options)](UV%20菜单/基于摄影机的映射选项%28Camera-Based%20Mapping%20options%29.md)。

#### 轮廓拉伸(Contour Stretch)

选择“UV > 轮廓拉伸”(UV > Contour Stretch) > ![图：选择“UV 轮廓拉伸”(UV Contour Stretch) 可设置“轮廓拉伸贴图选项”(Contour Stretc…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2217 字 ≥300，非承重" --> 可设置[“轮廓拉伸贴图选项”(Contour Stretch Mapping options)](UV%20菜单/轮廓拉伸映射选项%28Contour%20Stretch%20Mapping%20options%29.md)。

#### 基于法线(Normal-Based)

根据关联顶点的法线放置 UV。

#### 圆柱形(Cylindrical)

通过向内投影 UV 纹理坐标到一个虚构的圆柱体上，以映射它们到选定对象。

选择“UV > 圆柱形”(UV > Cylindrical) > ![图：选择“UV 圆柱形”(UV Cylindrical) 可设置“圆柱形映射选项”(Cylindrical Mapping …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2217 字 ≥300，非承重" --> 可设置[“圆柱形映射选项”(Cylindrical Mapping options)](UV%20菜单/圆柱形映射选项%28Cylindrical%20Mapping%20options%29.md)。

#### 平面(Planar)

从假设平面沿一个方向投影 UV 纹理坐标，可以将其映射到选定的曲面网格。

选择“UV > 平面”(UV > Planar) > ![图：选择“UV 平面”(UV Planar) 可设置“平面映射选项”(Planar Mapping options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2217 字 ≥300，非承重" --> 可设置[“平面映射选项”(Planar Mapping options)](UV%20菜单/平面映射选项%28Planar%20Mapping%20options%29.md)。

#### 球形(Spherical)

通过将 UV 从假想球体向内投影，将 UV 映射到选定对象上。

选择“UV > 球形”(UV > Spherical) > ![图：选择“UV 球形”(UV Spherical) 可设置“球形映射选项”(Spherical Mapping option…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2217 字 ≥300，非承重" --> 可设置[“球形映射选项”(Spherical Mapping options)](UV%20菜单/球形映射选项%28Spherical%20Mapping%20options%29.md)。

## 切割/缝合(Cut/Sew)

#### 自动接缝(Auto Seams)

允许 Maya 自动选择或切割选定对象/UV 壳上的边，以形成适当的接缝。有关详细信息，请参见[自动接缝(Auto Seams)选项](UV%20菜单/自动接缝%28Auto%20Seams%29.md)。

#### 切割 UV 边(Cut UV Edges)

沿选定边分割 UV，可以创建新纹理边界。UV 编辑器的工具栏中也提供了此功能。也可以单击 UV 编辑器工具栏上的 ![图：沿选定边分割 UV，可以创建新纹理边界。UV 编辑器的工具栏中也提供了此功能。也可以单击 UV 编辑器工具栏上的 以使用…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-59131FE3-81C5-40EF-9E6A-8D18FA9A3281.png) <!-- baize:img-hook downloaded=false reason="正文 2217 字 ≥300，非承重" --> 以使用此工具。请参见[切割 UV 工具](../../../../UV/UV/UV%20参考/UV%20工具/切割%20UV%20工具%28Cut%20UV%20Tool%29.md)。

#### 缝合 UV 边(Sew UV Edges)

沿选定边界附着 UV，但不在 UV 编辑器视图中一起移动它们。也可以单击 UV 编辑器工具栏上的 ![图：沿选定边界附着 UV，但不在 UV 编辑器视图中一起移动它们。也可以单击 UV 编辑器工具栏上的 以使用此工具。请参见缝…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-422BA3A9-B526-429B-A4FA-B2C0FF2CB213.png) <!-- baize:img-hook downloaded=false reason="正文 2217 字 ≥300，非承重" --> 以使用此工具。请参见[缝合 UV 工具(Sew UV Tool)](../../../../UV/UV/UV%20参考/UV%20工具/缝合%20UV%20工具%28Sew%20UV%20Tool%29.md)。

#### 分割 UV (Split UVs)

沿连接到选定 UV 点的边将 UV 彼此分离，从而创建边界。

**注**

提示：

通过单击

UV 编辑器

工具栏上的分割 UV 图标

快速分离 UV。

#### 删除 UV(Delete UVs)

将 UV 从网格的选定面中移除。如果希望将纹理映射到其中 UV 已删除的曲面网格区域，将需要使用 UV 投影映射功能重映射或重投影 UV。

#### 合并 UV (Merge UVs)

使用“合并 UV”(Merge UVs)将单独的 UV 壳合并到一起。“合并 UV”(Merge UVs)与“缝合 UV”(Sew UVs)具有类似效果。但是，“合并 UV”(Merge UVs)更适合在多边形具有非流形几何体时合并壳。例如，如果有三个 UV 壳共享一条边（由于几何体是非流形的），则“合并 UV”(Merge UVs)可以合并其中两个 UV 壳，而不影响其他 UV 壳。如果在本示例中使用“缝合 UV”(Sew UVs)，则将组合所有壳，因为它们共享一条边。

有关详细信息，请参见[合并 UV (Merge UVs)选项](UV%20菜单/合并%20UV%20选项%28Merge%20UVs%20options%29.md)。

#### 3D 切割和缝合 UV 工具(3D Cut and Sew UV Tool)

使用此工具可切割和缝合场景中的 UV 边。

拖动到边上可在关联的 UV 壳中对其进行切割，或者按住 Shift 键并拖动可沿同一循环边切割其他边。

按住 Ctrl 键并拖动可缝合边，或者同时按住 Ctrl 和 Shift 键并拖动可沿同一循环边缝合其他边。

**注**

请注意，不要使用 Ctrl + Shift + S，否则您可能会无意中关闭关键帧切线标记菜单。

选择“UV > 3D 切割和缝合 UV 工具”(UV > 3D Cut and Sew UV Tool) > ![图：选择“UV 3D 切割和缝合 UV 工具”(UV 3D Cut and Sew UV Tool) ，以设置 3D 切割和…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2217 字 ≥300，非承重" -->，以设置 [3D 切割和缝合 UV 工具(3D Cut and Sew UV Tool)选项](UV%20菜单/3D%20UV%20抓取工具选项%283D%20UV%20Grab%20Tool%20options%29.md)。

#### 3D 抓取 UV 工具(3D Grab UV Tool)

使用此工具可以直接在场景中的模型上操纵 UV。

选择“UV > 3D 抓取 UV 工具”(UV > 3D Grab UV Tool) > ![图：选择“UV 3D 抓取 UV 工具”(UV 3D Grab UV Tool) 可设置“3D 抓取 UV 工具选项”(3D…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2217 字 ≥300，非承重" --> 可设置[“3D 抓取 UV 工具选项”(3D Grab UV Tool options)](UV%20菜单/3D%20UV%20抓取工具选项%283D%20UV%20Grab%20Tool%20options%29.md)。

## 相关主题

- [UV 编辑器概述](../../../../UV/UV/“UV%20编辑器”%28UV%20Editor%29概述.md)

- [UV 编辑器菜单栏](../../../../UV/UV/UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单.md)
