# 分离和附加 UV

在“UV 编辑器”(UV Editor)中，Maya 提供了多个用于分离、合并和附加 UV 的功能。这些功能对于许多操作十分重要：

- 将一个壳分离为多个壳并与纹理的不同部分对应。

- 允许 UV 纹理坐标在“展开”(Unfold)或“优化”(Optimize)过程中以尽可能减少扭曲/重叠的形式自由展开。

- 接合通过在“自动映射”(Automatic Mapping)过程中创建的小壳。

| 目标 | 操作 | 示例 |
|---|---|---|
| 沿选定边分离（切割）UV 壳。 | 选择要分离的边。 选择“切割/缝合 > 切割”(Cut/Sew > Cut)，或在“UV 工具包”(UV Toolkit)中选择“切割和缝合 > 切割”(Cut and Sew > Cut)（快捷方式：Shift + X）。 | ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F9C36E6C-7C2C-411A-9849-207D327DBFD0.png) <!-- baize:img-hook downloaded=false reason="正文 1825 字 ≥300，非承重" --> |
| 以交互方式分离（切割） UV 边 | 在 UV 编辑器中分离 UV 边 选择“工具 > 切割”(Tools > Cut)，或在“UV 工具包”(UV Toolkit)中选择“切割和缝合 > 切割工具”(Cut and Sew > Cut Tool) 沿边拖动以将其分离。 在视口中分离 UV 边 选择“UV > 3D 切割和缝合 UV 工具”(UV > 3D Cut and Sew UV Tool)。 沿边拖动以将其分离。 有关详细信息（包括快捷方式的列表），请参见 [3D 切割和缝合工具](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/“3D%20切割和缝合%20UV%20工具”%283D%20Cut%20and%20Sew%20UV%20Tool%29选项.md)。 | ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F1361D3E-B779-4C48-AC71-543EF29D5F0B.gif) <!-- baize:img-hook downloaded=false reason="正文 1825 字 ≥300，非承重" --> ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-3C847798-B1C3-48D5-B672-4F3325904A25.gif) <!-- baize:img-hook downloaded=false reason="正文 1825 字 ≥300，非承重" --> |
| 允许 Maya 分离（切割）边（或选择接缝边） | 选择一个 UV 壳。 在“UV 编辑器”(UV Editor)的“UV 工具包”(UV Toolkit)中，选择“切割/缝合 > 自动接缝”(Cut/Sew > Auto-Seams)。 根据当前的[“自动接缝”(Auto-Seams)选项](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/自动接缝%28Auto%20Seams%29.md)，接缝将被切割为网格或在不进行切割的情况下被选中。 |  |
| 沿选定边附加（缝合）UV 壳。 | 选择要附加的边。 选择“切割/缝合 > 缝合”(Cut/Sew > Sew)，或在“UV 工具包”(UV Toolkit)中选择“切割和缝合 > 缝合”(Cut and Sew > Sew)（快捷方式：Shift + S）。 | ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D27E6921-BAF8-46E5-A006-F05713D29C6D.png) <!-- baize:img-hook downloaded=false reason="正文 1825 字 ≥300，非承重" --> |
| 以交互方式附加（缝合）UV 边 | 在 UV 编辑器中缝合 UV 边 选择“工具 > 缝合”(Tools > Sew)，或在“UV 工具包”(UV Toolkit)中选择“切割/缝合 > 缝合工具”(Cut/Sew > Sew Tool) 沿边拖动以将其附加。 在视口中缝合 UV 边 选择“UV > 3D 切割和缝合 UV 工具”(UV > 3D Cut and Sew UV Tool)。 按住 Shift 键并沿边拖动以将其附加。 有关详细信息（包括快捷方式的列表），请参见 [3D 切割和缝合工具](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/“3D%20切割和缝合%20UV%20工具”%283D%20Cut%20and%20Sew%20UV%20Tool%29选项.md)。 注： 在“视口”(Viewport)和“UV 编辑器”(UV Editor)之间移动时，“3D 切割和缝合 UV 工具”(3D Cut and Sew UV Tool)将自动更改为“切割工具”(Cut Tool)。 | ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D1CE3336-CC79-4B07-8A4F-47BD467C88FB.gif) <!-- baize:img-hook downloaded=false reason="正文 1825 字 ≥300，非承重" --> ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-955AE70B-87EF-479E-8707-ED13AF2E5D8F.gif) <!-- baize:img-hook downloaded=false reason="正文 1825 字 ≥300，非承重" --> |
| 沿选定边附加（缝合）UV 壳并一起移动壳。 | 选择要附加的边。 在“UV 工具包”(UV Toolkit)中选择“切割/缝合 > 缝合到一起”(Cut/Sew > Stitch Together) > 。 | ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D40020D5-0FF3-4ADC-9924-BCC5CFB8DABB.gif) <!-- baize:img-hook downloaded=false reason="正文 1825 字 ≥300，非承重" --> |
| 合并选定 UV。 | 选择要合并的 UV。 选择“修改 > 合并”(Modify > Merge)。 “合并 UV”(Merge UVs)仅合并共享相同的顶点的 UV。可以为 Maya 将移动 UV 以合并它们的最大距离指定一个选项。 |  |
| 自动附加并移动小壳。 | 选择所有壳。 选择“切割/缝合 > 移动并缝合”(Cut/Sew > Move and Sew) > ![图：选择“切割/缝合 移动并缝合”(Cut/Sew Move and Sew) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1825 字 ≥300，非承重" -->。 （可选）启用“限制壳大小”(Limit Shell Size)，然后为 UV 壳设置最大大小（以面数表示）。将不会移动大于该数字的壳。 单击“应用”(Apply)。 在执行“移动并缝合”(Move and Sew)操作之后，可以选择该节点 (polyMapSewMove)，然后在“属性编辑器”(Attribute Editor)或“通道盒”(Channel Box)中编辑它来调整“面数”(Number Faces)。 |  |

## 注释

- 不能切割单个边，除非它与边界接触。

- 在“UV 编辑器”(UV Editor)中，使用“选择 > 组件 > UV 壳”(Select > Components > UV Shell)可在切割之后选择 UV 片段。

- 在“UV 编辑器”(UV Editor)中使用“切割工具”(Cut Tool)或“缝合工具”(Sew Tool)时，Maya 将遵循每个 UV 的当前固定状态（即，固定的 UV 在切割时将保持不动，并且仅在可以不移动它们的情况下对其进行缝合时才进行缝合）。

### 相关主题

- [移动并缝合 UV 边选项(Move and Sew UV Edges options)](../UV%20参考/UV%20窗口和编辑器/“UV%20编辑器”%28UV%20Editor%29概述/UV%20编辑器菜单/“UV%20编辑器”%28UV%20Editor%29%20的“切割缝合”%28CutSew%29菜单/移动并缝合%20UV%20边选项%28Move%20and%20Sew%20UV%20Edges%20options%29.md)

- [合并 UV 选项(Merge UVs options)](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/合并%20UV%20选项%28Merge%20UVs%20options%29.md)

- [显示重叠 UV](../显示和选择%20UV/显示重叠%20UV.md)

- [“3D 切割和缝合 UV 工具选项”(3D Cut and Sew UV Tool options)](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/“3D%20切割和缝合%20UV%20工具”%283D%20Cut%20and%20Sew%20UV%20Tool%29选项.md)
