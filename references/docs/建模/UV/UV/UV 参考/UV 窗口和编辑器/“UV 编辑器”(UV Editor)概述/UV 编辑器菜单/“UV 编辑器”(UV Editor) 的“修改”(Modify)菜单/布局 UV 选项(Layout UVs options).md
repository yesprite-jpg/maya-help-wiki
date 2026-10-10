# 布局 UV 选项(Layout UVs options)

使用这些选项可设置从 [UV 编辑器](../../../../../“UV%20编辑器”%28UV%20Editor%29概述.md)中的“修改”(Modify)菜单选择“布局”(Layout)> ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2767 字 ≥300，非承重" --> 时发生的情况。

**注**

尝试排布时，具有非流形 UV 拓扑的模型可能会返回错误。如果发生这种情况，请在启用“非流形几何体”(Nonmanifold geometry)选项的情况下为对象执行

网格清理(Mesh Cleanup)

，然后再次执行排布。

## 排布(Layout)

在大多数情况下，默认设置能提供最佳的结果。

#### 方法(Method)

使用该选项可以指定 Maya 用于展开 UV 的方法。根据您选择的“方法”(Method)，“展开 UV 选项”(Unfold UVs Option)窗口中会显示不同的选项。从下列方法中选择：

#### 展开 3D(Unfold3D)

（默认）Maya 使用“展开 3D”(Unfold3D)算法。

#### 旧版(Legacy)

Maya 使用旧版展开算法。有关“旧版”(Legacy)选项的详细信息，请参见[“旧版”(Legacy)选项](展开%20UV%20选项%28Unfold%20UVs%20options%29.md#GUID-039FFDA5-3AC5-4CCF-A53E-546CCA6439FC__SECTION_141F3EDE511049CF91905BAEDD46A980)。

**注**

在 Maya 2014 和早期版本中，

“旧版”(Legacy)

是默认

“方法”(Method)

### 设置

#### 修复非流形几何体(Fix non-manifold geometry)

对网格执行的[清理](../../../../../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/“网格”%28Mesh%29菜单/清理选项%28Cleanup%20Options%29.md)操作。如果此选项处于禁用状态，则 Maya 将改为输出一条警告并提供选项来手动运行“清理”(Cleanup)操作。

**注**

Unfold3D

布局方法在非流形网格上不会运行。

### 保压设置

这些设置与如何将选定对象的 UV 壳全部压缩到指定的 UV 空间中相关。

#### 保压分辨率(Packing Resolution)

确定用于将相邻的 UV 壳放置到 UV 空间中的保压栅格的分辨率。值越高，速度就越慢，但如果有大量较小的壳，则会产生更好的效果。默认值为 256。

#### 保压迭代次数(Packing Iterations)

确定保压算法为获得所需结果而尝试的次数。迭代次数越多，速度就越慢，但可以提高精确度。默认值为 1。

#### 多个对象(Multiple Objects)

确定选择多个对象时如何继续操作

#### 紧缩在一起(不重叠) (Pack together (non-overlapping))

（默认）选择了多个对象后，它们会紧缩在一起，就像壳之间没有重叠的单个对象一样。

#### 单独保压(重叠) (Pack Separately (overlapping))

选择了多个对象后，每个对象都单独进行保压。属于不同对象的壳将在 UV 空间中重叠。

### 壳变换前设置

这些设置在开始保压之前确定 UV 壳的开始位置/方向。

#### 壳前期旋转(Shell Pre-Rotation)

允许壳在发生保压之前旋转。

#### 禁用(Off)

不出现前期旋转。

#### 水平(Horizontal)

在保压之前水平定向 UV 壳（通过其边界框）。

#### 垂直(Vertical)

在保压之前垂直定向 UV 壳（通过其边界框）。

#### 沿 X 对齐到 V (Align X to V)

确定 UV 壳方向，使其在 3D 空间中的 X 轴对齐到 UV 空间中的 V 轴。

#### 沿 Y 对齐到 V (Align Y to V)

确定 UV 壳方向，使其在 3D 空间中的 Y 轴对齐到 UV 空间中的 V 轴。

#### 沿 Z 对齐到 V (Align Z to V)

确定 UV 壳方向，使其在 3D 空间中的 Z 轴对齐到 UV 空间中的 V 轴。

#### 壳前缩放(Shell Pre-Scale)

允许壳在发生保压之前缩放。

#### 禁用(Off)

不出现预缩放。

#### 保留三维比(Preserve 3D Ratios)

缩放 UV 壳以保持其在 3D 空间中的曲面区域。

#### 保留 UV 比(Preserve UV Ratios)

缩放 UV 壳以保持整个 UV 区域。将保持选定壳之间的比率，及其在 UV 空间中的整个原始区域。

### 壳变换设置

这些设置与如何在保压期间操作变换 UV 壳相关。平移和旋转深受“布局设置”(Layout Settings)的影响，但可以通过具体描绘出最小/最大范围内的可能步长来进一步自定义旋转。

#### 平移壳(Translate shells)、旋转壳(Rotate shells)

确定能否在保压过程中移动或旋转 UV 壳。如果只想在不影响保压排列的情况下重缩放/重定向，这些设置非常有用，反之亦然。

#### 旋转步(Rotation Steps)

确定 UV 壳在保压过程中的允许方向。在保压过程中，旋转将从“最小壳旋转”(Minimum Shell Rotation)开始，然后根据需要按旋转步(Rotation Steps)长递增，直到达到“最大壳旋转”(Maximum Shell Rotation)为止。因此，值越小，保压速度就越慢。默认值为 90。

#### 最小壳旋转(Minimum Shell Rotation)

确定 UV 壳在保压过程中的最小允许方向。

#### 最大壳旋转(Maximum Shell Rotation)

确定 UV 壳在保压过程中的最大允许方向。

### 布局设置

这些设置确定保压算法如何将 UV 壳放置到指定的 UV 空间中。

#### 纹理贴图大小(Texture Map Size)

确定由 UV 空间表示的分辨率以计算像素填充值。

#### 填充单位(Padding Units)

指定测量“壳填充”(Shell Padding)和“平铺填充”(Tile Padding)的单位（以像素或 UV 表示）。

#### 壳填充(Shell Padding)

确定保压时要在 UV 壳之间留出的空间量。如果未看到效果，请启用“平移壳”(Translate shells)。

#### 平铺填充(Tile Padding)

确定要在 UV 壳与平铺边缘之间留出的空间量。

#### 壳分布(Shell Distribution)

确定壳放置如何与 UV 平铺关联。

#### 分布(Distribute)

选定壳集将自动分成“平铺 U”(Tiles U)和 V 值所指定的可用平铺。

#### 壳中心(Shell Centers)

UV 壳布局由每个壳的边界框中心确定。壳被指定给当前包含其边界框中心的平铺。使用“壳中心”(Shell Centers)模式时，必须确保将“紧缩区域”(Packing Region)设置为所需平铺起点的左下角。例如，如果希望壳与“UV 编辑器”(UV Editor)中的整个可见栅格对齐（因此 U 方向和 V 方向为 -1 到 1），则需要将“紧缩区域”(Packing Region)设置为“自定义”(Custom)，并将其 U 和 V 范围设置为 -1 到 0。然后，将 U 方向和 V 方向上的平铺数设置为 2。

#### 平铺 U (Tiles U)、V

指定要分布的工作 UV 平铺数。

#### 紧缩区域(Packing Region)

确定平铺空间中 UV 壳紧缩在一起的部分（包括边界）。在 U 方向和 V 方向上压缩多个平铺时，此区域表示 UV 空间中的左下角平铺。

#### 缩放模式(Scale Mode)

通用保压后缩放操作。

#### 禁用(Off)

不进行保压后缩放。

#### 一致(Uniform)

（默认）缩放所有壳，使其全局边界框最适合给定的紧缩区域。U 轴和 V 轴按统一比例缩放。

#### 非均匀(Non-Uniform)

在 U 方向和 V 方向上单独缩放所有壳，使其全局边界框与给定的紧缩区域匹配。这样便可最大程度地利用 UV 平铺的空间，但如果未调整对应的纹理来进行补偿，可能会导致扭曲。

## 相关主题

- [显示重叠 UV](../../../../../显示和选择%20UV/显示重叠%20UV.md)

- [世界空间、对象空间和局部空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A63AC5C8-8822-42AC-827E-164B5266DA03)
