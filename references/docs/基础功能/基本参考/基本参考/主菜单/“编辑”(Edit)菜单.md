# “编辑”(Edit)菜单

#### 撤消(Undo)、重做(Redo)、重复(Repeat)、最近命令列表(Recent Commands List)

| 目标 | 操作 |
|---|---|
| 撤消上次操作。 | 选择“编辑 > 撤消”(Edit > Undo)或按 Ctrl+Z。 |
| 重做上次操作。 | 选择“编辑 > 重做”(Edit > Redo)或按 Ctrl+Y。 |
| 重复上一命令。 | 选择“编辑 > 重复”(Edit > Repeat)或按 G 键。 还可以使用鼠标中键单击菜单名称来重复从中选择的上一命令。 |
| 重复最近的命令。 | 选择“编辑 > 最近命令列表”(Edit > Recent Commands List)，显示最近命令列表。 按住空格键以打开热盒，并在左侧的“最近的命令”(Recent Commands)区域按下鼠标左键以显示最近的命令菜单。 |

#### 关键帧(Keys)

通过此子菜单中的选项，可以对选定关键帧执行编辑操作（剪切、剪切、粘贴等）。

有关选项的详细信息，请参见[“关键帧”(Key)菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-FA1DF2DA-86C9-49EE-A23A-8749E4D31822)。

## 删除(Delete)

#### 删除(Delete)

删除当前选择。

#### “按类型删除”(Delete by Type)菜单

使用该子菜单中的选项可以删除场景中特定类型的每个对象。

有关选项的详细信息，请参见[“按类型删除”(Delete by Type)菜单](“编辑”%28Edit%29菜单/“按类型删除”%28Delete%20by%20Type%29菜单.md)。

#### 按类型删除全部(Delete All by Type)

使用该子菜单中的项目可以选择场景中特定类型的每个对象。

另请参见[删除](../../../创建和编辑对象/创建和编辑对象/删除%28Delete%29.md)。

## 复制(Duplicate)

#### 复制(Duplicate)

创建选择的单个副本。此外，您也可以按 Ctrl+D。

另请参见[复制](../../../创建和编辑对象/创建和编辑对象/复制%28Duplicate%29.md)。

#### 特殊复制(Duplicate Special)

创建一个或多个选择副本，并可以选择对每个副本应用变换。此外，您也可以按 Ctrl+Shift+D。

选择“编辑 > 特殊复制”(Edit > Duplicate Special) > ![图：选择“编辑 特殊复制”(Edit Duplicate Special) ，以设置“特殊复制”(Duplicate Spe…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2422 字 ≥300，非承重" -->，以设置[“特殊复制”(Duplicate Special)选项](“编辑”%28Edit%29菜单/“特殊复制”%28Duplicate%20Special%29选项.md)。

#### 复制并变换(Duplicate with Transform)

复制所选内容并使用当前操纵器应用已执行的上一个变换。此外，您也可以按 Shift+D。

如果执行变换，然后使操纵器消失（例如，取消选择对象），则 Maya 不保留上一个变换。另请参见[复制](../../../创建和编辑对象/创建和编辑对象/复制%28Duplicate%29.md)。

#### 传递属性值(Transfer Attribute Values)

对于源和目标共享的所有同名属性，用一个对象（源）的属性值来填充另一个对象（目标）的属性值，该操作适用于时间轴内的所有帧。

选择“编辑 > 传递属性值”(Edit > Transfer Attribute Values) > ![图：选择“编辑 传递属性值”(Edit Transfer Attribute Values) 以设置“传递属性值”(Tran…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2422 字 ≥300，非承重" --> 以设置[“传递属性值”(Transfer Attribute Values)选项](“编辑”%28Edit%29菜单/“传递属性值”%28Transfer%20Attribute%20Values%29选项.md)。

## 层次(Hierarchy)

#### 分组(Group)

将对象一起分组到新的空变换节点下，可以一次选择和变换所有这些对象。此外，您也可以按 Ctrl+G 来创建组。

选择“编辑 > 分组”(Edit > Group) > ![图：选择“编辑 分组”(Edit Group) ，以设置分组选项(Group Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2422 字 ≥300，非承重" -->，以设置[分组选项(Group Options)](“编辑”%28Edit%29菜单/“组”%28Group%29选项.md)。

有关变换节点的详细信息，请参见 [DAG 层次](../../../节点和属性/节点和属性/DAG%20层次.md)。

#### 解组(Ungroup)

解组位于组节点下方的对象。

选择“编辑 > 解组”(Edit > Ungroup) > ![图：选择“编辑 解组”(Edit Ungroup) ，以设置解组选项(Ungroup Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2422 字 ≥300，非承重" -->，以设置[解组选项(Ungroup Options)](“编辑”%28Edit%29菜单/“解组”%28Ungroup%29选项.md)。

**注**

不要在

“细节级别”(Level of Detail)

组上使用

“编辑 > 解组”(Edit > Ungroup)

；LOD 阈值信息不会在

“撤消”(Undo)

时正确重置。使用

“编辑 > 细节级别 > 解组”(Edit > Level of Detail > Ungroup)

可以正确解组 lodGroup 节点。

#### 创建 LOD 组(Create LOD Group)

创建细节级别组，该组关联您想要基于游戏引擎中的摄影机距离替换的同一几何体的多个不同分辨率版本。这样使用远处和近处之间的多个版本就可以为近处生成模型的高质量版本，为远处生成模型的低质量版本。另请参见 [LOD（细节级别）](../../../查看场景/查看场景/LOD（细节级别）.md)。

选择“编辑 > LOD (细节级别) > 创建 LOD 组”(Edit > LOD (Level of Detail) > Create LOD Group) > ![图：选择“编辑 LOD (细节级别) 创建 LOD 组”(Edit LOD (Level of Detail) Create…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2422 字 ≥300，非承重" -->，以在创建组之前指定以下各项：

##### 阈值类型(Threshold Type)

指定在确定要显示的细节级别时要使用的方法。

默认情况下，“阈值类型”(Threshold Type)设置为“屏幕高度百分比”(Screen Height Percentage)，以便根据当前摄影机帧中的整个 LOD 组占据的屏幕高度百分比显示级别。“屏幕高度百分比”(Screen Height Percentage)测量 LOD 组中所有网格相对于当前摄影机帧的总体高度，并为要显示的每个级别建立初始默认百分比。您还可以根据与摄影机的“距离”(Distance)设置要切换的阈值。

使用 FBX 导出选定几何体时，此设置存储在 FBX 文件中，以便您的游戏引擎进行读取。（另请参见[将 LOD 组导出到游戏引擎](../../../查看场景/查看场景/LOD（细节级别）/将%20LOD%20组导出到您的游戏引擎.md)。）

#### 生成 LOD 网格(Generate LOD Meshes)

生成选定高分辨率网格的较低分辨率版本，然后将其作为新级别添加到 LOD 组中。另请参见[生成 LOD 网格](../../../查看场景/查看场景/LOD（细节级别）/生成%20LOD%20网格.md)。

选择“编辑 > LOD (细节级别) > 生成 LOD 网格”(Edit > LOD (Level of Detail) > Generate LOD Meshes) > ![图：选择“编辑 LOD (细节级别) 生成 LOD 网格”(Edit LOD (Level of Detail) Gener…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2422 字 ≥300，非承重" -->，以打开[生成 LOD 网格选项](“编辑”%28Edit%29菜单/“生成%20LOD%20网格”%28Generate%20LOD%20Meshes%29选项.md)，然后指定用于生成网格的设置。

#### 解组 LOD 组(Ungroup LOD Group)

解组选定 LOD 组。

#### 父对象(Parent)

使选定节点成为最后选定节点（关键对象）的子对象。选择要指定给父对象的对象，按住 Shift 键选择父对象，然后选择“编辑 > 父对象”(Edit > Parent)或按 P 键。也就是说，如果按顺序选定两个对象，则第一个选定对象将成为第二个选定对象的子对象。

父对象操作完成后，子对象将保持选定状态而父对象将被取消选择。

当选择父对象时，子对象也将被选中，且父对象的变换节点控制子对象的变换。有关变换节点的详细信息，请参见 [DAG 层次](../../../节点和属性/节点和属性/DAG%20层次.md)。

#### 断开父子关系(Unparent)

断开选定对象的父子关系。此外，您也可以按 Shift+P。

选择“编辑 > 父对象”(Edit > Parent) > ![图：选择“编辑 父对象”(Edit Parent) ，以设置断开父子关系选项(Unparent Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2422 字 ≥300，非承重" -->，以设置[断开父子关系选项(Unparent Options)](“编辑”%28Edit%29菜单/“断开父子关系”%28Unparent%29选项.md)。
