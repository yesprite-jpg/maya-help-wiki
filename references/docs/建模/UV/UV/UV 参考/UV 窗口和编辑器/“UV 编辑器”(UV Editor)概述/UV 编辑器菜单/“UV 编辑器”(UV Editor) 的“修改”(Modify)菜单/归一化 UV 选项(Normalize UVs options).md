# 归一化 UV 选项(Normalize UVs options)

使用这些选项可设置在选择“UV > 归一化”(UV > Normalize)时发生的情况。

## 设置

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-C1084B3B-8DC9-446E-9CAE-9FE7FF1449F2.png) <!-- baize:img-hook downloaded=false reason="正文 548 字 ≥300，非承重" -->

#### 归一化(Normalize)

#### 整体(Collectively)

选择“整体”(Collectively)可整体归一化所有选定面的 UV。这意味着所有选定面的纹理坐标“整体”适配 0 到 1 纹理空间。这是默认设置。

![图：选择“整体”(Collectively)可整体归一化所有选定面的 UV。这意味着所有选定面的纹理坐标“整体”适配 0 到…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-E621906A-10D6-4710-A47C-1A960B0D9925.png) <!-- baize:img-hook downloaded=false reason="正文 548 字 ≥300，非承重" -->

#### 每个面是独立的(Each face separately)

选择“每个面是独立的”(Each face separately)分别归一化每个选定面的 UV。这意味着每个选定面的纹理坐标的适配边界为 0 到 1。

![图：选择“每个面是独立的”(Each face separately)分别归一化每个选定面的 UV。这意味着每个选定面的纹理…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-5AD68141-EEC3-429A-97BD-0741F998C737.png) <!-- baize:img-hook downloaded=false reason="正文 548 字 ≥300，非承重" -->

#### 保持纵横比(Preserve aspect ratio)

启用该选项可沿 U 和 V 方向均匀缩放 UV。

禁用该选项（默认设置）可拉伸纹理以进行适配（通过非均匀缩放 U 和 V）。

归一化纹理坐标后，就可以缩放选定面的 UV。如果“保持纵横比”(Preserve Aspect Ratio)处于启用状态，则在 U 和 V 轴上的缩放肯定都是均匀缩放。如果处于禁用状态，则 U 和 V 轴上的缩放会有所不同。

#### 以最近的 Tile 为中心(Center on closest tile)

启用后，在最近的 UV 平铺内缩放选定组件或 UV 壳。

**注**

提示：

如果 UV 壳跨平铺边界，将在包含更多壳组件的平铺内缩放选定壳。

## 相关主题

- [移动、旋转和缩放 UV](../../../../../编辑%20UV/移动、旋转和缩放%20UV.md)

- [单位化 UV 选项(Unitize UVs options)](单位化%20UV%20选项%28Unitize%20UVs%20options%29.md)
