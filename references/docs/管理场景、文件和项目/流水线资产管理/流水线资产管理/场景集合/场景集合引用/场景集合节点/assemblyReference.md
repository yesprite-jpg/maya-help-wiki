# assemblyReference

## 集合属性(Assembly Attributes)

#### 定义名称(Definition Name)

显示包含所引用的 assemblyDefinition 节点的场景文件的位置。

单击 ![图：单击 图标可浏览到相应位置，或者为 assemblyDefinition 节点指定一个新文件路径。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-D456810C-E804-45F1-BB8A-8873277816FD.png) <!-- baize:img-hook downloaded=false reason="正文 1085 字 ≥300，非承重" --> 图标可浏览到相应位置，或者为 [assemblyDefinition](assemblyDefinition.md) 节点指定一个新文件路径。

#### ![图：（“重新加载集合定义”(Reload the assembly definition)）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-F78541C3-42B2-49CE-AE34-BDDE1BEC34D2.png) <!-- baize:img-hook downloaded=false reason="正文 1085 字 ≥300，非承重" -->（“重新加载集合定义”(Reload the assembly definition)）

重新加载引用的集合定义。请在更新 [assemblyDefinition](assemblyDefinition.md) 节点后使用此选项。

#### 名称空间(Namespace)

显示 [assemblyDefinition](assemblyDefinition.md) 节点的名称空间。

若要指定名称空间，请在“名称空间”(Namespace)字段中键入，或者单击 ![图：若要指定名称空间，请在“名称空间”(Namespace)字段中键入，或者单击 图标以打开 “名称空间编辑器”(Names…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-9B71492F-A6AD-43D6-8B95-CC8C53559373.png) <!-- baize:img-hook downloaded=false reason="正文 1085 字 ≥300，非承重" --> 图标以打开 “名称空间编辑器”(Namespace Editor)并指定新的名称空间。

## 集合表示(Assembly Representations)

#### 活动表示(Active Representation)

指定列表中哪一个表示显示为活动表示。

**注**

活动表示状态与场景一同保存。重新打开场景时，将自动加载上一个活动表示。

请参见[切换活动集合表示](../../使用场景集合构建场景/切换活动集合表示.md)。

#### 表示列表(Representation List)

显示指定给引用的 assemblyDefinition 节点的表示，其中活动表示以粗体显示。从列表中选择一个表示后，将填充“表示属性”(Representation Attributes)字段。

## 表示属性(Representation Attributes)

“表示属性”(Representation Attributes)的值是只读的。若要更改属性值，请打开包含 assemblyDefinition 节点的场景文件，然后在“属性编辑器”(Attribute Editor)中更新其“表示属性”(Representation Attributes)。

#### 名称(Name)

显示所选表示的名称。对于“缓存”(Cache)和“场景”(Scene)表示，“名称”(Name)属性继承表示源文件名。

#### 数据(Data)

对于“缓存”(Cache)和“场景”(Scene)表示，“数据”(Data)显示所选表示的源文件位置。对于“定位器”(Locator)表示，“数据”(Data)显示用户定义的说明。

#### 标签(Label)

显示用户定义的名称，该名称用于在“表示列表”(Representation List)以及“大纲视图”(Outliner)和场景视图菜单中标识相应表示。

#### 类型(Type)

指示该表示是“缓存”(Cache)、“场景”(Scene)还是“定位器”(Locator)。

## 相关主题

- [使用集合引用来集合场景](../../使用场景集合构建场景/使用集合引用来集合场景.md)

- [assemblyDefinition](assemblyDefinition.md)

- [集合表示](../../场景集合基础知识/集合表示.md)
