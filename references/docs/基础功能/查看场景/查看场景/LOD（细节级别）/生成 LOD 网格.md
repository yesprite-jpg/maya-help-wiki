# 生成 LOD 网格

以下步骤介绍如何开始使用高分辨率版本的网格，并在需要不同的细节级别时自动生成要显示的较低分辨率版本。如果您已经拥有各种版本的网格，您希望在不同时间显示并且只想设置 LOD 组，请参见[创建 LOD 组](创建%20LOD%20组.md)。

1. 选择高分辨率网格。

2. 从主菜单栏中，选择“编辑 > LOD (细节级别) > 生成 LOD 网格”(Edit > LOD (Level of Detail) > Generate LOD Meshes)。

  这将根据[生成 LOD 网格选项](../../../基本参考/基本参考/主菜单/“编辑”%28Edit%29菜单/“生成%20LOD%20网格”%28Generate%20LOD%20Meshes%29选项.md)中设置的选项生成新网格。要首先设置或更改“生成 LOD 网格选项”(Generate LOD Meshes Options)选项，请选择“编辑 > LOD (细节级别) > 生成 LOD 网格”(Edit > LOD (Level of Detail) > Generate LOD Meshes) > ![图：这将根据生成 LOD 网格选项中设置的选项生成新网格。要首先设置或更改“生成 LOD 网格选项”(Generate LO…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 656 字 ≥300，非承重" -->。

  在生成新网格时，这些选项可用于设置以下内容：

  - 要生成或重生成多少个网格/级别

  - 要生成或重生成哪些网格/级别

  - 要使用哪种减少方法

  - 根据减少方法，您希望每个网格按级别减少的程度

  - 是否将现有蒙皮权重复制到新网格

  新的 LOD 网格生成后，正好彼此堆栈在一起，以便从一个 LOD 级别无缝切换到下一个级别。您可放大和缩小场景以查看各种级别的外观。

  默认情况下，一次只有一个网格显示在视口中，但是您可以将级别暂时设置为始终显示。请参见[测试或预览 LOD](测试或预览%20LOD.md) 了解详细信息。

3. （可选）打开“大纲视图”(Outliner)（“窗口 > 大纲视图”(Window > Outliner))，以在场景层次中查看 LOD 组。

  展开每个 LOD_*n* 子组，以查看一个或多个关联网格。

## 相关主题

- [创建 LOD 组](创建%20LOD%20组.md)

- [生成 LOD 网格选项](../../../基本参考/基本参考/主菜单/“编辑”%28Edit%29菜单/“生成%20LOD%20网格”%28Generate%20LOD%20Meshes%29选项.md)

- [测试或预览 LOD](测试或预览%20LOD.md)
