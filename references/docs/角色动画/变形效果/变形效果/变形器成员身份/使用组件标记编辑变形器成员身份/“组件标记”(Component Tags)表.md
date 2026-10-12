# “组件标记”(Component Tags)表

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 1649 字 ≥300，非承重" -->

- 若要查看“属性编辑器”(Attribute Editor)的“组件标记”(Component Tags)构件，请选择几何体，然后在“属性编辑器”(Attribute Editor)中单击其形状节点选项卡（例如 *pCube1*），然后展开**“组件标记”(Component Tags)**区域。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-1893DFBF-FAFE-424C-BEE0-06299A6498C0.png) <!-- baize:img-hook downloaded=false reason="正文 1649 字 ≥300，非承重" -->

“属性编辑器”(Attribute Editor)中的“组件标记”(Component Tags)表

可在[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)中使用此表编辑来自形状节点的“组件标记”(Component Tags)成员身份。 若要将组件标记添加到对象，请参见[为几何体指定组件标记](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-788B1C8B-7F45-4862-BC42-0A334DFECFD3.htm)。

“组件标记”(Component Tags)属性以表格格式显示在“属性编辑器”(Attribute Editor)的“组件标记”(Component Tags)构件中。单击列标题可对条目进行排序。

| 列名 | 功能 |
|---|---|
| 搜索(Search)字段 | 输入名称以查找指定的组件标记。 |
| 过滤器 ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-7475853B-F682-4B78-844F-4BC9ED56AEAB.png) <!-- baize:img-hook downloaded=false reason="正文 1649 字 ≥300，非承重" --> | 单击以展开一个菜单，您可以在其中将搜索范围限于以下几何体类型：**“顶点”(Vertices)**、**“边”(Edges)**和**“面”(Faces)**，以及以下标记类型：**“可编辑”(Editable)**、**“只读”(Read Only)**和**“程序”(Procedural)**。 您还可以使用表达式进行搜索。请参见[组件标记表达式](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-237E61B3-CA0A-4C35-A3E7-E0D2004A898E.htm)。 |
| **添加(Add)** ![图：添加(Add)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-B5E33AF1-E48D-488D-91A2-741BE6430588.png) <!-- baize:img-hook downloaded=false reason="正文 1649 字 ≥300，非承重" --> | 单击以将条目添加到“组件标记”(Component Tags)表。如果选择了组件，它们将包含在新标记中。 请参见[为几何体指定组件标记](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-788B1C8B-7F45-4862-BC42-0A334DFECFD3.htm)。 |
| **删除(Remove)** ![图：删除(Remove)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-13A1DBD2-73D8-4551-9BC7-16F7B375101A.png) <!-- baize:img-hook downloaded=false reason="正文 1649 字 ≥300，非承重" --> | 从场景中删除当前选定的组件标记。 |
| **名称(Name)** | 相应组件标记的名称。 旁边带有 *****（星号）的名称表示已修改来自上游的组件标记。 |
| **类型(Type)** | 此列中的图标对应于组件标记类型： ![图：此列中的图标对应于组件标记类型： 顶点 边 面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-9F67ECC1-6097-4850-A282-4DEEFD10DEA1.png) <!-- baize:img-hook downloaded=false reason="正文 1649 字 ≥300，非承重" --> 顶点 ![图：此列中的图标对应于组件标记类型： 顶点 边 面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-C3D24B3D-EA00-4645-84FD-8F9F925DB41C.png) <!-- baize:img-hook downloaded=false reason="正文 1649 字 ≥300，非承重" -->边 ![图：此列中的图标对应于组件标记类型： 顶点 边 面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-A8363783-9DB3-479D-AF19-D8CC2632A641.png) <!-- baize:img-hook downloaded=false reason="正文 1649 字 ≥300，非承重" --> 面 |
| **注射位置** | 变形器的原始位置。 |
| **类型计数(Type Count)** | 组件标记中包含的组件数/组件标记类别中的组件总数。 例如，一个面为组件标记的立方体在此字段中显示为 **1/6**。 |
| **顺序(Order)** | 组件标记位置在注射节点变形链中的序列，最小数字指示最远的上游。 |

## “组件标记”(Component Tags)表快捷菜单

在任意行上单击鼠标右键以显示菜单，其中包含**“选择组件”(Select Components)**、**“创建”(Create)**、**“删除”(Delete)**和**“重命名...”(Rename...)**选项，以及**“组件”(Components)**卷展栏。 有关详细信息，请参见[使用组件标记编辑变形器集成员身份](../使用组件标记编辑变形器成员身份.md)。

#### 选择组件(Select Components)

单击以聚焦在“节点”(Node)字段中显示的节点上。

#### “修改标记”(Modify Tag)选项

以下右键单击选项可以更新组件标记

#### 重命名...(Rename...)

单击“重命名”(Rename)以打开一个窗口，您可以在其中为选定的组件标记输入新名称。

#### 删除(Delete)

从列表中移除组件标记。

#### 复制

![图：重命名...(Rename...) 单击“重命名”(Rename)以打开一个窗口，您可以在其中为选定的组件标记输入新名称…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1649 字 ≥300，非承重" -->

复制组件标记。

#### 合并(Merge)

![图：将选定的组件标记成员身份合并为一个。按住 Ctrl 或 Shift 键并选择多个组件标记以基于选定标记创建新的合并标记；…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1649 字 ≥300，非承重" -->

将选定的组件标记成员身份合并为一个。按住 Ctrl 或 Shift 键并选择多个组件标记以基于选定标记创建新的合并标记；合并标记不会覆盖现有标记。

仅当选择多个标记时，“合并”(Merge)选项才会显示在“组件标记”(Component Tags)快捷菜单中。

#### “修改标记组件”(Modify Tag Component)选项

以下右键单击选项可以更新组件标记组件类型。

#### 添加选定对象(Add Selected)

将选定组件合并到相应的组件标记组。

#### 移除选定对象(Remove Selected)

从相应的**组件标记**组中排除选定组件。

#### 替换为选定对象(Replace with Selected)

更改选定组件的选定组件。

#### 清除(Clear)

从相应的组件标记组中移除选定组件。

#### “转化标记组件”(Convert Tag Components)选项

以下右键单击选项可以更新用于相应组件标记的组件类型。重新选择组件标记以查看对新组件类型的更新。

#### 转化为面/边/顶点(Convert to Faces/Edges/Verts)

![图：转化为面/边/顶点(Convert to Faces/Edges/Verts) 将相应组件标记的组件类型更改为所选类型。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1649 字 ≥300，非承重" -->

将相应组件标记的组件类型更改为所选类型。
