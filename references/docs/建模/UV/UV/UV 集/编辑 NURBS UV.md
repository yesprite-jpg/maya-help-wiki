# 编辑 NURBS UV

Maya 为在 UV 编辑器内编辑 NURBS 曲面的 UV 纹理坐标提供有限的支持。“编辑 NURBS UV”(Edit NURBS UV)*模式*对游戏开发人员很有用，他们在游戏应用程序中使用 NURBS 曲面类型并需要能够修改显式 UV 集供后续导出到游戏引擎。此功能不为在 Maya 中编辑 NURBS UV 以与纹理贴图或图像渲染功能结合使用提供支持。

“编辑 NURBS UV”(Edit NURBS UV)模式为 NURBS 曲面创建唯一的显式 UV 集。用户在 NURBS 曲面的隐式 UV 和显式创建的 UV 集之间切换。随后可以在受限的范围内编辑显式 NURBS UV。

建议用户仅在 NURBS 曲面模型的所有编辑和修改都完成时才创建和编辑显式 NURBS UV。请参见下面的[注释](编辑%20NURBS%20UV.md#WS17956D7ADBC6E73631FFC8E3117AE3442BA-7FFA)和[编辑 NURBS UV 限制](编辑%20NURBS%20UV.md#WS17956D7ADBC6E73631FFC8E3117AE3442BA-7FF9)。

有关提供此功能的 MEL TM 命令和标志的详细信息，请参见 *MEL* 手册中的 [nurbsUVSet](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Commands/nurbsUVSet.html) 和 [nurbsEditUV](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Commands/nurbsEditUV.html) 命令。

在 UV 编辑器中编辑 NURBS 曲面的 UV

1. 在场景视图中，选择要为纹理创建和编辑显式 UV 的 NURBS 曲面。

2. 确保通过选择编辑 > 按类型删除全部 > 历史(Edit > Delete All by Type > History)删除了 NURBS 曲面的构建历史。

  在进行任何 UV 编辑之前删除构建历史可确保对节点依存关系图进行的后续更新不会移除对显式 NURBS UV 集进行的 UV 编辑。仅在确信将不再需要您编辑模型时执行此操作（保存包含构建历史的模型副本，以防由于任何原因而需要恢复）。

3. 使用“状态行”(Status Line)上的“构建历史开/关”(Construction History on/off)图标在处理 NURBS UV 时关闭构建历史。

4. 通过选择“UV > UV 编辑器”(UV > UV Editor)，打开“UV 编辑器”(UV Editor)。

  使用 NURBS 曲面隐式创建的 NURBS UV 显示在 UV 编辑器的 2D 视图中。

5. 在“UV 编辑器”(UV Editor)中，在 2D 视图中单击鼠标右键，然后从显示的标记菜单中选择“编辑 NURBS UV”(Edit NURBS UV)模式。

  将在 UV 编辑器的 2D 视图中显式创建并显示 NURBS 曲面的 UV 集。创建的 NURBS UV 集基于 NURBS 曲面的拓扑。

6. 通过执行下列操作之一将选择方法更改为 UV：

  - 在场景视图中单击鼠标右键，从标记菜单选择“曲面 UV”(Surface UV)。

  - 在“UV 编辑器”(UV Editor)的 2D 视图中单击鼠标右键，然后从标记菜单中选择“UV”。

7. 选择要在场景视图中或 UV 编辑器的 2D 视图中修改的 UV。

8. 使用工具箱中的变换工具（“移动工具”(Move Tool)、“旋转工具”(Rotate Tool)或“缩放工具”(Scale Tool)），在 UV 编辑器中编辑 NURBS UV 的位置。

## 注释

- 在创建和编辑显式 NURBS UV 之前，需要删除 NURBS 曲面上的构建历史。这样可以确保对依存关系图进行的更新不会覆盖 UV 编辑。

- 在修改显式 UV 集后以任何方式修改 NURBS 曲面拓扑（即，在 NURBS 曲面上插入等参线）都将覆盖唯一的 NURBS UV 集。显式 NURBS UV 集将进行更新，以考虑对拓扑的更改，但是任何 UV 修改都将丢失。

## 编辑 NURBS UV 限制

- 对于每个 NURBS 曲面，使用此功能创建的显式 UV 集是唯一的。即，与多边形和细分曲面类型不同，无法为给定 NURBS 曲面创建多个 NURBS UV 集。

- Maya 渲染器（软件、硬件等）不支持显式 NURBS UV。它们仅能够渲染 NURBS 的隐式 UV。

- 构建历史不受支持。即，用户应规划其纹理工作流，使其在对模型的所有编辑和修改完成后出现。在编辑 NURBS UV 集后对模型拓扑进行的更改将在节点依存关系图更新时覆盖 UV 编辑。

- UV 修改仅限于 UV 选择和变换（即，移动、旋转和缩放）。无法通过面片或等参线选择并修改显式 NURBS UV。多边形和细分曲面 UV 修改功能不适用于显式 NURBS UV。

- UV 共享不受支持。对于显式 NURBS UV，曲面上的每个面片角都存在一个 UV 纹理坐标。边界框选择可用于同时移动内部 NURBS UV。
