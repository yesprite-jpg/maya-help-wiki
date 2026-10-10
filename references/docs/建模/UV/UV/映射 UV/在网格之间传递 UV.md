# 在网格之间传递 UV

可以将 UV 映射到平滑版本的多边形模型，在该模型中更易于获取较好的 UV，例如，可以使导致 UV 重叠的褶皱平滑。然后，您可以使用“传递属性”(Transfer Attributes)操作将映射的 UV 重新复制到复杂的原始模型。

在多边形网格之间传递平滑的 UV

1. 复制多边形网格。

2. 复制时，选择要平滑的顶点。

3. 选择“编辑网格”(Edit Mesh) > [平均化顶点(Average Vertices)](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/“编辑网格”%28Edit%20Mesh%29菜单/平均化顶点选项%28Average%20Vertices%20Options%29.md) > ![图：选择“编辑网格”(Edit Mesh) 平均化顶点(Average Vertices) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 479 字 ≥300，非承重" -->。

4. 在显示的“平均化顶点选项”(Average Vertices Options)中，设置“平滑量”(Smoothing amount)，然后单击“应用”(Apply)。

  **注**

  增大

  “平滑量”(Smoothing amount)

  值可快速平滑选择。也可以反复单击

  “应用”(Apply)

  来重复执行平滑操作。

5. 使用“创建 UV”(Create UVs)菜单中的任何映射选项，将 UV 投影到平滑的重复模型。

6. 使用“网格 > 传递属性”(Mesh > Transfer Attributes)将平滑的重复模型中的 UV 重新复制回原始网格中。

## 相关主题

- [在网格之间传递属性](../../../多边形建模/多边形建模/编辑多边形/修改多边形网格/在网格之间传递属性.md)

- [传递属性选项(Transfer Attributes Options)](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/“网格”%28Mesh%29菜单/传递属性选项%28Transfer%20Attributes%20Options%29.md)
