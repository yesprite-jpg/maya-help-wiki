# “列出集合编辑”(List Assembly Edits)窗口

通过“列出集合编辑”(List Assembly Edits)窗口，可以显示对集合引用节点和场景表示包含的节点进行的编辑。使用“显示”(Show)菜单中的选项，可以显示对 [assemblyReference](场景集合节点/assemblyReference.md) 节点层次中的所有节点进行的编辑或仅显示影响选定 [assemblyReference](场景集合节点/assemblyReference.md) 节点的编辑。

还可以显示未应用于当前场景中的编辑，如在添加到选定集合引用层次之前对 assemblyReference 节点和场景表示进行的编辑。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-F86EBDA2-ED58-4C1A-9E49-F48282A0EE26.png) <!-- baize:img-hook downloaded=false reason="正文 1475 字 ≥300，非承重" -->

若要访问“列出集合编辑”(List Assembly Edits)窗口，请在“大纲视图”(Outliner)中选择集合引用节点，然后在“大纲视图”(Outliner)或场景视图中单击鼠标右键 (![图：若要访问“列出集合编辑”(List Assembly Edits)窗口，请在“大纲视图”(Outliner)中选择集合引…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-339814BD-5F9D-4AF0-AD24-9C56C81EB765.png) <!-- baize:img-hook downloaded=false reason="正文 1475 字 ≥300，非承重" -->)，并从显示的菜单中选择“场景集合 > 列出编辑”(Scene Assembly > List Edits)。请参见[列出场景集合编辑](../使用场景集合构建场景/列出场景集合编辑.md)。

## “显示”(Show)菜单

#### 列出存储在选择中的编辑(List Edits Stored on Selection)

列出存储在选定 assemblyReference 节点上的编辑。如果编辑是在当前会话中进行的，则这包括对嵌套 assemblyReference 节点及其子节点进行的编辑。未列出保存在嵌套 assemblyReference 节点或场景表示的源文件中的编辑。若要使用该选项列出这些编辑，必须选择存储编辑的嵌套 assemblyReference 节点。

#### 列出影响选择内容的编辑(List Edits Affecting Selection Contents)

列出对存储在任何级别集合层次上的选定 assemblyReference 节点的直接子节点进行的编辑。该选项将忽略存储编辑的 assemblyReference 节点，而仅列出影响选定节点的子节点的更改。未列出以下编辑：

- 对选定 assemblyReference 节点进行的编辑。

  若要使用该选项列出对选定 assemblyReference 节点进行的编辑，请选择 assemblyReference 的父节点。

- 对嵌套在直接子 assemblyReference 节点中的 assemblyReference 节点进行的编辑。

“列出影响选择内容的编辑”(List Edits Affecting Selection Contents)是默认设置。

#### 失败的编辑(Failed Edits)

列出 Maya 无法将其应用于选定 assemblyReference 节点或场景表示包含的节点的编辑。例如，如果 Maya 尝试将编辑应用于场景表示的嵌套节点（名称在表示源文件中更改之后），可能会出现失败的编辑。

失败的编辑按其出现顺序以红色显示。

#### 未应用的编辑(Unapplied Edits)

列出无法应用于活动表示的编辑。例如，当对活动场景表示（然后切换到缓存表示）进行编辑时，编辑将显示为未应用，因为编辑无法应用于缓存表示。

未应用的编辑将显示在“未应用的编辑”(Unapplied Edits)标题下。

#### 不可移除的编辑(Non-Removable Edits)

列出存储在嵌套 assemblyReference 节点上的编辑。

不可移除的编辑将显示为灰色。失败的不可移除编辑将显示为深红色。

**注**

这些编辑无法从当前场景中移除。必须从包含源 assemblyReference 节点或场景表示的文件中移除编辑。

#### 移除选定对象(Remove Selected)

移除选定编辑，使其不再应用于当前场景中。不能使用“移除选定对象”(Remove Selected)来移除不可移除的编辑。

请参见[移除场景集合编辑](../使用场景集合构建场景/移除场景集合编辑.md)。

## 相关主题

- [列出场景集合编辑](../使用场景集合构建场景/列出场景集合编辑.md)

- [场景集合编辑](../场景集合编辑.md)

- [移除场景集合编辑](../使用场景集合构建场景/移除场景集合编辑.md)

- [使用场景集合构建场景](../使用场景集合构建场景.md)
