# 复制(Duplicate)

“复制”(Duplicate)和“特殊复制”(Duplicate Special)命令用于创建选定对象的多个副本；可选的变换将应用于每个副本。

您也可以轻量引用现有对象（称为实例）。实例与原始对象链接，所以更改原始对象将自动更新该原始对象的所有实例。

简单复制选定对象

1. 执行以下操作之一

  - 按 Ctrl + D。

  - 选择“编辑 > 复制”(Edit > Duplicate)。

  - 在“对象”(Object)模式下按 Shift 键并拖动任何变换操纵器（也称为智能复制）。

使用指定选项复制选定对象

1. 选择“编辑 > 特殊复制”(Edit > Duplicate Special) > ![图：选择“编辑 特殊复制”(Edit Duplicate Special) 以打开特殊复制选项(Duplicate Spec…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 976 字 ≥300，非承重" --> 以打开[特殊复制选项(Duplicate Special Options)](../../基本参考/基本参考/主菜单/“编辑”%28Edit%29菜单/“特殊复制”%28Duplicate%20Special%29选项.md)面板。

2. 将“几何体类型”(Geometry Type)设置为“复制”(Copy)。

3. 设置副本数量选项以及将应用于每个副本的变换选项。

复制选定对象并重新应用上一变换

1. 选择“编辑 > 复制并变换”(Edit > Duplicate with Transform)。

例如，如果将对象向上移动 2 个单位，然后选择“编辑 > 复制并变换”(Edit > Duplicate with Transform)，则系统将创建重复对象并将该对象再次向上移动 2 个单位。

创建选定对象的轻量实例

1. 选择“编辑 > 特殊复制”(Edit > Duplicate Special) > ![图：选择“编辑 特殊复制”(Edit Duplicate Special) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 976 字 ≥300，非承重" --> 。

2. 将“几何体类型”(Geometry Type)设置为“实例”(Instance)。

3. 设置副本数量选项以及将应用于每个副本的变换选项。

  **注**

  - 如果对象枢轴点的默认值发生更改，则复制该对象的多个副本将导致对复制变换节点的通道进行额外变换。但是，复制对象的生成位置、方向和枢轴仍将正确。若要避免这些额外的变换，应该在副本数量设置为 1 的情况下调用“特殊复制”(Duplicate Special)命令。然后可以根据需要多次使用热键 g。

  - “编辑 > 复制”(Edit > Duplicate)不适用于等参线。请改用“曲线 > 复制曲面曲线”(Curves > Duplicate Surface Curves)。

  - 也可以在任何变换工具的[“智能复制设置”(Smart Duplicate Settings)](../../界面概述/界面概述/工具箱%28Tool%20Box%29/移动工具%28Move%20Tool%29.md)中从“复制”(Copy)更改为“实例”(Instance)。但是，这不会影响[“特殊复制选项”(Duplicate Special Options)](../../基本参考/基本参考/主菜单/“编辑”%28Edit%29菜单/“特殊复制”%28Duplicate%20Special%29选项.md)中的相同设置。

## 相关主题

- [副本与实例](副本与实例.md)

- [翻转对象](../../变换对象/变换对象/变换对象和组件/翻转对象.md)

- [特殊复制选项](../../基本参考/基本参考/主菜单/“编辑”%28Edit%29菜单/“特殊复制”%28Duplicate%20Special%29选项.md)
