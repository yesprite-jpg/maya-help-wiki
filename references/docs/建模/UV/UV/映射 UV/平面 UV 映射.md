# 平面 UV 映射

平面映射通过平面将 UV 投影到网格。该投影最适用于相对平坦的对象，或者至少可从一个摄影机角度完全可见的对象。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-5D699E6C-4B3F-4136-9C5C-C696DB4D6F98.png) <!-- baize:img-hook downloaded=false reason="正文 1696 字 ≥300，非承重" -->

平面映射通常会提供重叠的 UV 壳。UV 壳可能会完全重叠，且外形类似于单个 UV 壳。在映射到单独的重叠 UV 之后，应使用“UV > 排布”(UV > Layout)。

根据平面投影映射

1. 选择要将 UV 投影到的面。

2. 选择“UV > 平面”(UV > Planar) > ![图：选择“UV 平面”(UV Planar) （如果需要设置选项），或在“UV 编辑器”(UV Editor)的“UV 工具…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1696 字 ≥300，非承重" -->（如果需要设置选项），或在“UV 编辑器”(UV Editor)的“UV 工具包”(UV Toolkit)中，转到“创建 > 平面”(Create > Planar)。

  根据需要设定以下选项：

  - 单击“最佳平面”(Best Plane)，根据选择的面定位操纵器。

  - 单击“边界框”(Bounding Box)，根据网格的边界框定位操纵器。

  - 选择将从中投影 UV 的轴。

3. 单击“投影”(Project)。

4. 使用投影操纵器控制平面如何分布 UV。

5. 使用 UV 编辑器以查看和编辑生成的 UV。

  ![图：使用 UV 编辑器以查看和编辑生成的 UV。 还可以通过单击红色交叉线旋转该操纵器，从而显示“显示操纵器工具”(Show…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-2829F7DF-CD42-4AC4-8203-190064DB6A46.png) <!-- baize:img-hook downloaded=false reason="正文 1696 字 ≥300，非承重" -->

  还可以通过单击红色交叉线旋转该操纵器，从而显示“显示操纵器工具”(Show Manipulator tool)。单击“显示操纵器”(Show Manipulator)控制柄周围的淡蓝色圆形，以激活旋转控制柄。

## 映射到其他平面

“最佳平面纹理工具”(Best Plane Texturing Tool)可根据从指定顶点计算得出的平面，将 UV 指定给选择的面；而不是默认轴平面。

可以在选择“最佳平面纹理工具”(Best Plane Texturing tool)之前选择要映射的面，也可以先选择该工具，然后现单击要映射的每个面。

根据选择的最佳适配平面映射

1. 选择要将 UV 映射到的面。

2. 选择“UV > 最佳平面纹理工具”(UV > Best Plane Texturing Tool)（如果需要设置选项），或在“UV 编辑器”(UV Editor)的“UV 工具包”(UV Toolkit)中，转到“创建 > 最佳平面”(Create > Best Plane)。

3. 如果尚未选择面，请单击面以将其添加到选择中。不能使用蚂蚁线选择面，必须逐个选择面，或者在使用该操作之前选择面。

4. 按 Enter 键。

5. 选择一个或多个顶点（在网格上单击鼠标右键，然后选择“顶点”(Vertex)以切换为选择顶点）来定义投影平面。

6. 按 Enter 键。

7. 使用 UV 编辑器以查看和编辑生成的 UV。

  ![图：使用 UV 编辑器以查看和编辑生成的 UV。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-37A2E60E-DFD9-44FE-9D96-337AEE8492CC.png) <!-- baize:img-hook downloaded=false reason="正文 1696 字 ≥300，非承重" -->

从视图定义的平面中投影

1. 选择要将 UV 投影到的面。

2. 翻滚透视视图，或平移正交视图以观察面。

3. 选择“UV > 基于摄影机”(UV > Camera-Based)（如果需要设置选项），或在“UV 编辑器”(UV Editor)的“UV 工具包”(UV Toolkit)中，转到“创建 > 基于摄影机”(Create > Camera-Based)。

  ![图：选择“UV 基于摄影机”(UV Camera-Based)（如果需要设置选项），或在“UV 编辑器”(UV Editor…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F62CC99A-7E9E-4EDC-AAB4-4C4EE43E03A0.png) <!-- baize:img-hook downloaded=false reason="正文 1696 字 ≥300，非承重" -->

## 注释

- 平面映射可创建外形类似于纹理边界的共享重叠的 UV。启用纹理边界显示（在“显示 > 多边形 > 纹理边界边”(Display > Polygons > Texture Border Edges)中），以清楚地显示纹理边界。

- 如果使用“3D 绘制”(3D Paint)或“绘制毛发属性”(Paint Fur Attributes)工具绘制共享重叠的 UV，则会出现接缝问题。

  若要避免这些问题，请使用“UV > 排布”(UV > Layout) > ![图：若要避免这些问题，请使用“UV 排布”(UV Layout) 手动分离 UV。将“分离壳”(Separate shell…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1696 字 ≥300，非承重" -->手动分离 UV。将“分离壳”(Separate shells)设定为“收拢”(Folds)，并将“壳布局”(Shell layout)选项设定为“沿 U 方向”(Along U)或“置于方形”(Into Square)。

- 投影映射每次仅在单个对象上正常工作。如果需要在单个步骤中将投影应用于多个多边形对象，请将这些对象组合为一个对象，并应用投影，然后将后面部分分离出去。否则，需在每个对象上分别执行投影。

- 如果模型的形状十分有组织，并且要求使用该模型的完整 UV 表示来进行纹理映射，则平面投影将生成重叠且扭曲的 UV。您可能需要[展开](../编辑%20UV/展开%20UV%20网格/展开%20UV%20网格.md) UV 以便使用它们。

  ![图：如果模型的形状十分有组织，并且要求使用该模型的完整 UV 表示来进行纹理映射，则平面投影将生成重叠且扭曲的 UV。您可能…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-43D3AB35-D784-48CE-B248-CD6C904066B3.png) <!-- baize:img-hook downloaded=false reason="正文 1696 字 ≥300，非承重" -->

### 相关主题

- [映射 UV](../映射%20UV.md)

- [圆柱形 UV 映射](圆柱形%20UV%20映射.md)

- [球形 UV 映射](球形%20UV%20映射.md)

- [自动 UV 映射](自动%20UV%20映射.md)

- [排布 UV 选项(Layout UVs options)](../UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/布局%20UV%20选项%28Layout%20UVs%20options%29.md)

- [基于摄影机的映射选项(Camera-Based Mapping options)](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/基于摄影机的映射选项%28Camera-Based%20Mapping%20options%29.md)

- [平面映射选项(Planar Mapping options)](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/平面映射选项%28Planar%20Mapping%20options%29.md)

- [创建 UV 集选项(Create UV Set options)](../UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29的“UV%20集”%28UV%20Sets%29菜单/创建%20UV%20集选项%28Create%20UV%20Set%20options%29.md)
