# 将边界 UV 映射到方形或圆形

“映射 UV 边界”(Map UV Border)功能和“拉直 UV 边界”(Straighten UV Border)功能。

使用“映射 UV 边界”(Map UV Border)时，您可以将 UV 壳的边界上的 UV 移出，放到 0 到 1 纹理空间范围（方形）的边或 0 到 1 范围内的内切圆中。映射 UV 以使它们使用 0 到 1 的整个纹理范围。当您需要最大化纹理贴图所需的纹理空间时，该方法非常有用。

您也可以在移动边界 UV 时按比例缩放边。如果您在使用“松弛 UV”(Relax UVs)解开内部 UV 之前解开边界，则该方法非常有用。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-07E1BE0F-91C6-469B-AF5D-48C1D9727C63.png) <!-- baize:img-hook downloaded=false reason="正文 674 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4F1E12EE-4D31-4B98-90FC-3DA0344996DE.png) <!-- baize:img-hook downloaded=false reason="正文 674 字 ≥300，非承重" -->

将边界 UV 映射到方形或圆形

1. 在“UV 编辑器”(UV Editor)中，在要映射其边界 UV 的壳上选择一个 UV。选择的 UV 将表示您希望创建的方形或圆形边界贴图的左下角。

  所选择的 UV 非常重要，因为它将决定 UV 壳映射到 UV 纹理空间的 0,0 原点的位置。如果生成的 UV 边界贴图比较倾斜，您可能希望撤消该操作，然后选择另一个 UV 并重新映射。

2. 选择“修改 > 映射 UV 边界”(Modify > Map UV Border) > ![图：选择“修改 映射 UV 边界”(Modify Map UV Border) （或者，在主菜单栏中选择“UV 映射 UV …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 674 字 ≥300，非承重" -->（或者，在主菜单栏中选择“UV > 映射 UV 边界”(UV > Map UV Border)）。

3. 设置相应选项，然后单击“贴图”(Map)或“应用”(Apply)。

  边界 UV 将基于所进行的设置映射。内部 UV 将保持不变。您可以使用“松弛 UV”(Relax UVs)功能解开内部 UV。

4. 如果 UV 映射显示正确，则可以使用“松弛 UV”(Relax UVs)功能解开壳上的内部 UV。

## 相关主题

- [映射 UV 边界选项(Map UV Border options)](../UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/“映射边界”%28Map%20Border%29选项.md)

- [排布 UV 选项(Layout UVs options)](../UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/布局%20UV%20选项%28Layout%20UVs%20options%29.md)

- [拉直边界 UV](拉直%20UV.md)

- [优化 UV](优化%20UV%20间距.md)
