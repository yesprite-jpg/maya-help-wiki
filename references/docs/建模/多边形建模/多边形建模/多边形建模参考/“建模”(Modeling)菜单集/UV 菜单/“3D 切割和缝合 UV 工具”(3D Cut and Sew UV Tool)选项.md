# “3D 切割和缝合 UV 工具”(3D Cut and Sew UV Tool)选项

“3D 切割和缝合 UV 工具”(3D Cut and Sew UV Tool)允许您直接在视口中创建或缝合 UV 壳上的接缝，而不必通过 [UV 编辑器](../../../../../UV/UV/“UV%20编辑器”%28UV%20Editor%29概述.md)。有关切割和缝合边的详细信息，请参见[分离和附加 UV](../../../../../UV/UV/编辑%20UV/分离和附加%20UV.md)。

**注**

在

“视口”(Viewport)

和

“UV 编辑器”(UV Editor)

之间移动时，

“3D 切割和缝合 UV 工具”(3D Cut and Sew UV Tool)

将自动更改为

切割 UV 工具(Cut UV Tool)。

使用这些选项可设置在选择“UV > 3D 切割和缝合 UV 工具”(UV > 3D Cut and Sew UV Tool) > ![图：使用这些选项可设置在选择“UV 3D 切割和缝合 UV 工具”(UV 3D Cut and Sew UV Tool) 时…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1029 字 ≥300，非承重" -->时发生的情况。

## 笔刷(Brush)

#### 稳定笔划(Steady Stroke)

激活此选项将自动平滑鼠标笔划。如果您的手颤抖或所处的模型空间狭窄，这将非常有用。

#### 距离(Distance)

确定启用“稳定笔划”(Steady Stroke)时要平滑的抖动宽度。

#### 对称(Symmetry)

跨所选对称轴镜像切割或缝合操作。

## 显示(Display)

#### 显示棋盘格贴图(Show checker map)

显示选定 UV 壳上的棋盘格贴图纹理。

#### 显示纹理边界(Show texture borders)

加粗选定 UV 壳的纹理边界。您可以使用色样调整边界的颜色。

#### 显示 UV 壳上色(Show UV shell coloring)

在 [UV 编辑器](../../../../../UV/UV/“UV%20编辑器”%28UV%20Editor%29概述.md)中显示与相同颜色壳对应的 UV 壳顶部的叠加颜色。

## 键盘/鼠标快捷方式

| 热键 | 操作 |
|---|---|
| 单击 | 切割 UV 边或亮显的 UV 边。 |
| 拖动 | 切割 UV |
| 按住 Shift 键并拖动 | 切割约束到循环边的 UV。 |
| 双击 | 切割 UV 循环边。 |
| 按住 Shift 键并双击 | 从第一条选定边到双击的第二条边切割 UV 循环边。 |
| 按住 Tab 键 | 激活 UV 循环边选择约束。 |
| 按住 Ctrl 键并单击 | 缝合 UV 边或亮显的 UV 边。 |
| 同时按住 Ctrl 和 Shift 键并拖动 | 缝合约束到循环边的 UV。 |
| 按住 Ctrl 键并双击 | 缝合 UV 循环边。 |
| 同时按住 Ctrl 和 Shift 键并双击 | 从第一条选定边到双击的第二条边缝合 UV 循环边。 |
| X | 切割亮显或选定的边。 面选择遮罩(Face selection mask)：运行[创建 UV 壳(Create UV shell)](../../../../../UV/UV/UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“切割缝合”%28CutSew%29菜单.md)操作。 UV 壳选择遮罩(UV Shell selection mask)：不执行任何操作。 |
| S | 缝合亮显或选定的边。 面选择遮罩(Face selection mask)：不执行任何操作。 UV 壳选择遮罩(UV Shell selection mask)：缝合选定 UV 壳的 UV 壳边界。 |
| D | [展开](../../../../../UV/UV/编辑%20UV/展开%20UV%20网格/展开%20UV%20网格.md)亮显的 UV 壳，然后执行[排布](../../../../../UV/UV/编辑%20UV/排布%20UV%20壳.md)操作。 |
| Shift+D | [展开](../../../../../UV/UV/编辑%20UV/展开%20UV%20网格/展开%20UV%20网格.md)亮显的 UV 壳。 |

## 相关主题

- [分离和附加 UV](../../../../../UV/UV/编辑%20UV/分离和附加%20UV.md)

- [切割 UV 工具(Cut UV Tool)](../../../../../UV/UV/UV%20参考/UV%20工具/切割%20UV%20工具%28Cut%20UV%20Tool%29.md)
