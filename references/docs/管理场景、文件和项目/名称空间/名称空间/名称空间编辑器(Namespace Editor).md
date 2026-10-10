# 名称空间编辑器(Namespace Editor)

- 若要打开“名称空间编辑器”(Namespace Editor)，请选择“窗口 > 常规编辑器 > 名称空间编辑器(Windows > General Editors > Namespace Editor)。

使用名称空间编辑器可以创建、删除和编辑名称空间。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-4590A500-266C-4E6C-9D66-53BF5D033B23.png) <!-- baize:img-hook downloaded=false reason="正文 1000 字 ≥300，非承重" -->

“名称空间编辑器”(Namespace Editor)显示场景中所有当前名称空间（包括嵌套的名称空间）。根名称空间使用 ":(root)" 来表示。

## 轮廓

| 目标 | 操作 |
|---|---|
| 创建新名称空间 | 单击“新建”(New)。会使用一个新的子名称空间扩展当前选定名称空间。请参见[创建名称空间](创建名称空间.md)。 |
| 重命名现有名称空间 | 双击名称空间。在“重命名名称空间”窗口中，键入一个新名称，然后单击“确定”(OK)。 会将新名称空间名称应用到目标名称空间及其子孙名称空间。 |
| 删除名称空间 | 选择名称空间，然后单击“删除”(Delete)。 不能删除具有关联子名称空间的名称空间。请参见[移除名称空间](移除名称空间.md)。 |
| 选择包含在名称空间中的场景对象 | 选择名称空间，然后单击“选择内容”(Select Contents)。 |
| 列出包含在名称空间中的场景对象 | 选择名称空间，然后单击“列出内容”(List Contents)。 将显示“名称空间内容查看器”(Namespace Contents Viewer)，其中会列出名称空间内容。在“脚本编辑器”(Script Editor)中也会显示该内容列表。 |
| 将选定场景对象添加到名称空间中 | 在场景中，选择要添加的对象。在“名称空间编辑器”(Namespace Editor)中，选择要将对象添加到的名称空间，然后单击“添加选定对象”(Add Selected)。 |
| 查找未使用的名称空间 | 单击“选择所有空的名称空间”(Select All Empty)。在“名称空间编辑器”(Namespace Editor)中会选中所有未使用的名称空间。 |
| 移除空的父名称空间 | 选择一个子名称空间，然后单击“收拢到子名称空间”(Collapse to Child)。会从名称空间层次中移除选定子名称空间的空父名称空间。 |
| 设置当前名称空间 | 选择要设定为当前名称空间的名称空间，然后单击“设置当前名称空间”(Set Current)。![图：选择要设定为当前名称空间的名称空间，然后单击“设置当前名称空间”(Set Current)。 图标指示当前设定的名称空间…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-085BFA65-7807-43B8-B3C3-3D2393EB8AFB.png) <!-- baize:img-hook downloaded=false reason="正文 1000 字 ≥300，非承重" --> 图标指示当前设定的名称空间。 |
| 设定“相对名称空间”(Relative Namespaces)模式，以便可以相对于当前名称空间引用名称空间 | 选择“选项”(Options) >“相对名称空间”(Relative Namespaces)。请参见[设定相对名称空间模式](编辑名称空间.md#GUID-9E2F2AF6-48F3-4628-B23E-0B8A07EAF737__WS73099CC142F48755-6BF62AC8120443AF808-636E)。 |
