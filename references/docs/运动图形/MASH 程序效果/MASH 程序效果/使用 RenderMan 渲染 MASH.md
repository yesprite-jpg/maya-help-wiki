# 使用 RenderMan 渲染 MASH

由于 RenderMan 不完全支持粒子实例化器，因此您必须执行以下两项操作之一才能使用 RenderMan 渲染 MASH 场景。最简单的方法是使用“网格 几何体类型”(Mesh > Geometry Type)只创建 MASH 网络（请参见[创建 MASH 网络](MASH%20参考/MASH%20菜单.md)）。但是，如果需要使用“实例化器”(Instancer)，则必须执行以下步骤：

在 RenderMan 中渲染实例化 MASH 网络

1. 在 RenderMan/RIS“高级”(Advanced)选项卡中，将“MASHtoRenderMan”添加到 RI 注射点。

2. 选择 MASH 网络的源几何体，然后转到“文件 > 导出选定对象”(File > Export Selected) > ![图：选择 MASH 网络的源几何体，然后转到“文件 导出选定对象”(File Export Selected) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-MotionGraphics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 419 字 ≥300，非承重" -->。

3. 启用“着色器”(Shader)导出，然后导出为 RIB 归档。

4. 在 MASH 网络的 Waiter 节点中，将新创建的 RIB 文件的文件路径添加到 RenderMan 归档 (RIB) 属性。

  **注**

  可以使用逗号分隔多个 RIB 引用。

5. 使用 RenderMan 渲染。

## 相关主题

- [Waiter 节点](MASH%20参考/MASH%20节点概述/Waiter.md)
