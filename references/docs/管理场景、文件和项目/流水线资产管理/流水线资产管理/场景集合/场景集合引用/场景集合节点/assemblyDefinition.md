# assemblyDefinition

## 集合表示(Assembly Representations)

#### 活动表示(Active Representations)

指定列表中的哪个表示将显示在场景中。

请参见[切换活动集合表示](../../使用场景集合构建场景/切换活动集合表示.md)。

**注**

活动表示状态与场景一同保存。重新打开场景时，将自动加载上一个活动表示。

#### “添加缓存表示”(Add Cache representation)、“添加定位器表示”(Add Locator representation)和“添加场景表示”(Add Scene representation)

将选定类型的新集合表示添加到 assemblyDefinition 节点。缓存表示必须为基于 Alembic 的缓存 (.abc) 文件。场景表示必须为 Maya（.ma 或 .mb）场景文件。

请参见[添加集合表示](../../使用场景集合构建场景/添加集合表示.md)。

#### 表示列表(Representation List)

显示指定给 assemblyDefinition 节点的表示。活动表示以粗体形式显示。

使用箭头图标，可以更改列表中表示的顺序。默认情况下，当场景打开时，会加载列表中的第一个表示。“表示列表”(Representation List)的排序还定义了表示将如何显示在“大纲视图”(Outliner)和场景视图菜单中。

## 表示属性(Representation Attributes)

“表示属性”(Representation Attributes)的值应用于在“表示列表”(Representation List)中选择的表示。

#### 名称(Name)

指定所选表示的名称。对于“缓存”(Cache)和“场景”(Scene)表示，“名称”(Name)属性继承表示源文件名。

#### 数据(Data)

对于“缓存”(Cache)和“场景”(Scene)表示，显示选定表示的源文件位置。要为表示源文件指定新位置，请单击 ![图：对于“缓存”(Cache)和“场景”(Scene)表示，显示选定表示的源文件位置。要为表示源文件指定新位置，请单击 图标…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-D456810C-E804-45F1-BB8A-8873277816FD.png) <!-- baize:img-hook downloaded=false reason="正文 1115 字 ≥300，非承重" --> 图标。

对于“定位器”(Locator)表示，可以使用“数据”(Data)属性来添加注释。当“定位器”(Locator)为活动表示时，注释文本将在场景中的定位器附近显示。

#### 标签(Label)

希望其在“表示列表”(Representation List)、“大纲视图”(Outliner)和场景视图菜单中显示的表示名称。

#### 类型

指示表示是“缓存”(Cache)、“场景”(Scene)还是“定位器”(Locator)。这是一个只读属性。

#### ![图：（重新加载表示）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-F78541C3-42B2-49CE-AE34-BDDE1BEC34D2.png) <!-- baize:img-hook downloaded=false reason="正文 1115 字 ≥300，非承重" -->（重新加载表示）

重新加载活动表示。在更新要加载的表示之后执行该操作。例如，如果更新“缓存”(Cache)或“场景”(Secene)表示源文件的位置，则可能需要重新加载表示以查看场景中的更新。

#### ![图：（移除表示）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-1367DAFB-8E31-4038-8C6C-9AE81265C124.png) <!-- baize:img-hook downloaded=false reason="正文 1115 字 ≥300，非承重" -->（移除表示）

从 assemblyDefinition 节点中移除选定表示。请参见[移除集合表示](../../使用场景集合构建场景/移除集合表示.md)。

## 相关主题

- [创建集合定义](../../使用场景集合构建场景/创建集合定义.md)

- [assemblyReference](assemblyReference.md)

- [集合表示](../../场景集合基础知识/集合表示.md)
