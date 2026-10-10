# UV 编辑器标记菜单

[UV 编辑器菜单](UV%20编辑器菜单.md)。

## 按 Shift 键并单击鼠标右键

按住 Shift 键并在“UV 编辑器”(UV Editor)中单击鼠标右键将打开一个标记菜单，其中会显示不同的项，具体取决于选定的组件类型。

### 公用菜单

无论当前处于活动状态的组件模式为何，均会共享以下菜单选项：

| 菜单项 | 效果 |
|---|---|
| [展开(Unfold)](../../../编辑%20UV/展开%20UV%20网格.md) | 重新定位选定 UV，使其平放在 UV 空间中。 |
| [优化(Optimize)](../../UV%20工具/“展开%20UV%20工具”%28Unfold%20UV%20Tool%29和“优化%20UV%20工具”%28Optimize%20UV%20Tool%29.md) | 平均分配选定 UV 之间的间距，这有助于修复扭曲。 |
| [工具(Tools)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 用于快速访问“UV 工具包”(UV Toolkit)的“变换 > 工具”(Transform > Tools)部分。 |
| [固定(Pinning)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 用于快速访问“UV 工具包”(UV Toolkit)的“固定”(Pinning)部分。 |
| [选择约束(Selection Constraints)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 将可以选择的组件限制为符合某一所选标准的组件。 |
| [变换约束(Transform Constraints)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 将 UV 移动限制到沿其相邻边滑动。 |
| [切换壳边界(Toggle Shell Borders)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29的“视图”%28View%29菜单.md) | 确定是否以粗体显示壳边界。 |
| [纹理边界(Texture Borders)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29的“视图”%28View%29菜单.md) | 以粗体显示纹理边界。 |
| [显示图像(Display Image)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29的“图像”%28Image%29菜单.md) | 在 UV 编辑器中显示纹理图像。 |
| [棋盘格贴图(Checker Map)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29的“视图”%28View%29菜单.md) | 显示用于查看扭曲的棋盘格贴图图案。 |
| [扭曲着色器(Distortion Shader)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29的“视图”%28View%29菜单.md) | 显示用于查看扭曲的颜色贴图。 |

### UV

选定 UV 纹理坐标时，标记菜单会显示以下操作：

| 菜单项 | 效果 |
|---|---|
| [捕捉(Snap)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 用于访问“UV 工具包”(UV Toolkit)的“对齐和捕捉”(Align and Snap)部分中的各种捕捉选项。 |
| [归一化(Normalize)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/归一化%20UV%20选项%28Normalize%20UVs%20options%29.md) | 缩放选定 UV 以适配 0 到 1 的 UV 空间。 |
| [拉直(Straighten)](../../../编辑%20UV/拉直%20UV.md) | 重新定位所有选定 UV，使其在所选方向上形成一条直线。 |
| [排布(Layout)](../../../编辑%20UV/排布%20UV%20壳.md) | 重新定位 UV 壳，使其不会重叠并最大程度地利用可用的 UV 空间。 |
| [对齐 UV (Align UVs)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 用于访问“UV 工具包”(UV Toolkit)的“对齐和捕捉”(Align and Snap)部分中的各种对齐选项。 |
| [旋转 UV (Rotate UVs)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 绕由“UV 工具包”(UV Toolkit)的“变换”(Transform)部分指明的当前枢轴点旋转选定 UV。 |
| [分布(Distribute)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 均匀间隔选定 UV。 |
| [翻转(Flip)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 在指定方向上翻转选定 UV 的位置。 |
| [映射边界(Map Border)](../../../编辑%20UV/将边界%20UV%20映射到方形或圆形.md) | 将当前选定的 UV 映射到 UV 空间 0,0，然后相对于该位置展开所有其他边界 UV。 |
| [对称(Symmetrize)](../../UV%20工具/对称%20UV%20工具%28Symmetrize%20UV%20Tool%29.md) | 跨所选对称轴镜像当前选择。 |
| [单位化(Unitize)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单.md) | 将选定 UV 重新定位到 0-1 UV 空间的边界上。 |
| [自动接缝(Auto Seams)](../../../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/自动接缝%28Auto%20Seams%29.md) | 自动识别并选择最佳接缝边。 |
| [创建 UV 壳(Create UV Shell)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 从选定组件创建新的 UV 壳。 |
| [切割 UV(Cut UVs)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 沿附加到选定 UV 的边创建接缝。 |
| [删除 UV(Delete UVs)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 删除选定的 UV。 |
| [合并 UV (Merge UVs)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 将选定 UV 合并为单个 UV。 |
| [缝合 UV (Sew UVs)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 合并附加到选定 UV 的边。 |
| [测量像素距离(Measure Pixel Distance)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 显示两个所选 UV 之间的距离（以像素为单位）。 |

### UV 壳

选定 UV 壳时，标记菜单会显示以下操作：

| 菜单项 | 效果 |
|---|---|
| [映射(Mapping)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 用于访问“UV 工具包”(UV Toolkit)的“创建”(Create)部分中的各种映射选项。 |
| [沿 U 方向翻转(Flip Along U)/沿 V 方向翻转(Flip Along V)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 水平/垂直镜像整个壳。 |
| [排布(Layout)](../../../编辑%20UV/排布%20UV%20壳.md) | 重新定位 UV 壳，使其不会重叠并最大程度地利用可用的 UV 空间。 |
| [对齐 UV (Align UVs)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 用于访问“UV 工具包”(UV Toolkit)的“对齐和捕捉”(Align and Snap)部分中的各种对齐选项。 |
| [旋转 UV (Rotate UVs)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 绕由“UV 工具包”(UV Toolkit)的“变换”(Transform)部分指明的当前枢轴点旋转选定 UV。 |
| [自动接缝(Auto Seams)](../../../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/自动接缝%28Auto%20Seams%29.md) | 自动识别并选择最佳接缝边。 |
| [匹配栅格(Match Grid)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 尝试将与选定面相邻的 UV 对齐到栅格。 |
| [匹配 UV(Match UVs)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 将特定容差距离内与选定面相邻的 UV 移动到其各个位置的平均位置。 |
| [归一化(Normalize)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/归一化%20UV%20选项%28Normalize%20UVs%20options%29.md) | 缩放选定 UV 以适配 0 到 1 的 UV 空间。 |
| [拉直边界(Straighten Border)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 重新定位选定壳上的所有边界 UV，使其形成水平/垂直直线。 |
| [拉直 UV(Straighten UVs)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 重新定位选定壳上的所有 UV，使其形成水平/垂直直线。 |
| [单位化(Unitize)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单.md) | 将选定 UV 重新定位到 0-1 UV 空间的边界上。 |
| [分布壳(Distribute Shells)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 根据所选的方法均匀间隔选定壳。 |
| [聚集壳(Gather Shells)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 将所有 UV 壳移动到 0-1 UV 空间。 |
| [定向壳(Orient Shells)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 旋转所有 UV 壳，使其朝向同一方向。 |
| [随机化壳(Randomize Shells)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 在 0-1 UV 空间中随机排列 UV 壳。 |
| [捕捉和堆叠壳(Snap and Stack Shells)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 通过使选定 UV 相互重叠，将多个 UV 壳移动到另一个 UV 壳之上。 |
| [堆叠和定向壳(Stack and Orient Shells)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 将选定 UV 壳彼此堆叠并进行旋转，使其朝向同一方向。 |
| [堆叠类似的壳(Stack Similar Shells)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 仅将拓扑类似的壳彼此堆叠。 |
| [取消堆叠壳(Unstack Shells)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 移动所有选定 UV 壳，使其不再重叠且相互靠近。 |

### 边

选定多边形边时，标记菜单会显示以下操作：

| 菜单项 | 效果 |
|---|---|
| [移动并缝合 UV (Move and Sew UVs)](../../../编辑%20UV/分离和附加%20UV.md) | 合并选定的 UV 边，同时移动受影响的壳，使其不会变得扭曲。 |
| [将壳定向到边(Orient Shell to Edges)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 旋转 UV 壳，使其与大多数选定边对齐。 |
| [拉直壳(Straighten Shell)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 尝试沿 UV 壳的边界/在 UV 壳的边界内解开所有 UV。 |
| [展开(Unfold)](../../../编辑%20UV/展开%20UV%20网格.md) | 重新定位选定 UV，使其平放在 UV 空间中。 |
| [优化(Optimize)](../../UV%20工具/“展开%20UV%20工具”%28Unfold%20UV%20Tool%29和“优化%20UV%20工具”%28Optimize%20UV%20Tool%29.md) | 平均分配选定 UV 之间的间距，这有助于修复扭曲。 |
| [剪切(Cut)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“切割缝合”%28CutSew%29菜单.md) | 将选定的 UV 边分割为单独的重叠 UV 边。 |
| [缝合(Sew)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“切割缝合”%28CutSew%29菜单.md) | 合并选定的 UV 边。 |
| [缝合到一起(Stitch Together)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“切割缝合”%28CutSew%29菜单.md) | 通过在指定方向上朝一个壳移动另一个壳，将两条选定边缝合在一起。 |

### 面

选定多边形面或 UV 壳时，标记菜单会显示以下操作：

| 菜单项 | 效果 |
|---|---|
| [映射(Mapping)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 用于访问“UV 工具包”(UV Toolkit)的“创建”(Create)部分中的各种映射选项。 |
| [归一化(Normalize)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/归一化%20UV%20选项%28Normalize%20UVs%20options%29.md) | 缩放选定 UV 以适配 0 到 1 的 UV 空间。 |
| [拉直 UV(Straighten UVs)](../../../编辑%20UV/拉直%20UV.md) | 重新定位与选定面相邻的所有 UV，使其在所选方向上形成一条直线。 |
| [创建 UV 壳(Create UV Shell)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 从选定组件创建新的 UV 壳。 |
| [旋转面(Rotate Faces)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 绕由“UV 工具包”(UV Toolkit)的“变换”(Transform)部分指明的当前枢轴点旋转选定面。 |
| [循环(Cycle)](UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单.md) | 旋转选定组件的 U 值和 V 值。 |
| [翻转(Flip)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 在指定方向上翻转选定 UV 的位置。 |
| [匹配栅格(Match Grid)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 尝试将与选定面相邻的 UV 对齐到栅格。 |
| [匹配 UV(Match UVs)](../../../“UV%20编辑器”%28UV%20Editor%29概述.md) | 将特定容差距离内与选定面相邻的 UV 移动到其各个位置的平均位置。 |
| [对称(Symmetrize)](../../UV%20工具/对称%20UV%20工具%28Symmetrize%20UV%20Tool%29.md) | 跨所选对称轴镜像当前选择。 |

## 按 Ctrl 键并单击鼠标右键

在“UV 编辑器”(UV Editor)中按 Ctrl 键并单击鼠标右键将打开一个标记菜单，用于进行或修改选择：

| 菜单项 | 效果 |
|---|---|
| 到边(To Edges)/到顶点(To Vertices)/到 UV(To UVs)/到 UV 壳(To UV Shell)/到面(To Faces)/到 UV 壳边界(To UV Shell Border) | 将当前选择转化为相应的选择。 |
| 扩大选择(Grow Selection)/收缩选择(Shrink Selection) | 在当前选择中添加或移除一层相邻组件。 |
| 选择背面(Select Back Facing)/选择前面(Select Front Facing) | 分别选择缠绕顺序为逆时针或顺时针的所有组件。有关详细信息，请参见[显示 UV 缠绕顺序](../../../显示和选择%20UV/显示%20UV%20缠绕顺序.md)。 |
| [选择约束(Selection Constraints)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-60FD5F79-AC1D-46DE-B66D-2FBE73E15A30) | 限制组件选择。 |
| 选择背面(Select Back Facing)/选择前面(Select Front Facing) | 分别选择缠绕顺序为逆时针或顺时针的所有组件。有关详细信息，请参见[显示 UV 缠绕顺序](../../../显示和选择%20UV/显示%20UV%20缠绕顺序.md)。 |

## 相关主题

- [UV 编辑器概述](../../../“UV%20编辑器”%28UV%20Editor%29概述.md)

- [UV 编辑器菜单](UV%20编辑器菜单.md)

- [标记菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8BA1A3AA-4C44-4779-8B22-0AAE3627E8EB)
