# 拉直 UV

通常需要沿同一循环边拉直 UV，才能修复 UV 贴图上的扭曲。为此，有以下几种不同方法可供选择：

| 目标 | 请执行以下操作： | 示例： |
|---|---|---|
| 通过对齐拉直 UV | 选择要对齐的 UV。 在“UV 工具包”(UV Toolkit)中，打开“对齐和捕捉”(Align & Snap)区域。 单击其中一个“对齐”(Align)按钮，以在适当方向上相对于最远的 UV 对齐 UV。 | ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-6CC25B4F-056A-4B56-865C-F276FD36F3B2.gif) <!-- baize:img-hook downloaded=false reason="正文 983 字 ≥300，非承重" --> |
| 通过将 UV 的角度调整为相邻 UV 拉直 UV | 选择要对齐的 UV。 在“UV 工具包”(UV Toolkit)中，打开“展开”(Unfold)区域。 在“拉直 UV”(Straighten UVs)旁边，设置要沿其拉直的“最大角度”(Maximum Angle)和“轴”(Axes)。 单击“拉直 UV”(Straighten UVs)。 | ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-C2D528DE-FE6A-43A4-8DCF-4100F1A2EC72.gif) <!-- baize:img-hook downloaded=false reason="正文 983 字 ≥300，非承重" --> |
| 通过将 UV 与栅格匹配拉直 UV | 选择要对齐的 UV。 在“UV 工具包”(UV Toolkit)中，打开“对齐和捕捉”(Align & Snap)区域。 单击“匹配栅格”(Match Grid)。 您可以按 Shift 键并单击该按钮来打开“栅格 UV 选项”(Grid UVs Options)，用于自定义 UV 将对齐到的栅格的大小。请注意，这不一定通过 UV 空间中的可见栅格反映出来。 | ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-018EFD5E-19F7-4689-8908-0FD6BE691CF4.gif) <!-- baize:img-hook downloaded=false reason="正文 983 字 ≥300，非承重" --> |
| 拉直选定循环边，然后在其周围展开 | 选择 UV 或循环边。 在“UV 工具包”(UV Toolkit)中，打开“展开”(Unfold)区域。 单击“拉直壳”(Straighten Shell)。 | ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-6B24F3E9-08FE-45B3-9214-38B6932437A4.gif) <!-- baize:img-hook downloaded=false reason="正文 983 字 ≥300，非承重" --> |
| 拉直 UV 边界 | 在“UV 编辑器”(UV Editor)中，在混乱的 UV 边界周围选择 UV。 如果选择内部 UV 以及边界 UV 则不重要。“拉直 UV 边界”(Straighten UV Border)仅作用在边界上。 在某些情况下，很难选择要拉直的 UV，而不选择其他希望不受影响的 UV。在这些情况下，可以在选择中保留间隙，并使用“填充当前选择中的间隙”(Fill Gaps in Selection)选项以拉直无法选择的 UV。 选择“修改 > 拉直 UV 边界”(Modify > Straighten UV Border)（或者，在主菜单栏中选择“UV > 拉直 UV 边界”(UV > Straighten UV Border)）。 选择“polyStraightenUVBorder”节点并在“属性编辑器”(Attribute Editor)或“通道盒”(Channel Box)中编辑属性。 | ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-1FB117A1-F985-448C-BA14-3B8C2BD78468.png) <!-- baize:img-hook downloaded=false reason="正文 983 字 ≥300，非承重" --> |

## 相关主题

- [拉直 UV 边界选项(Straighten UV Border options)](../UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“修改”%28Modify%29菜单/“拉直边界”%28Straighten%20Border%29选项.md)

- [优化 UV](优化%20UV%20间距.md)
