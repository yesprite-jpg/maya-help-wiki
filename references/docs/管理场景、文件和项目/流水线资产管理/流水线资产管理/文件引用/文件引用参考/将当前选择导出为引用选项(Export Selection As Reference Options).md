# 将当前选择导出为引用选项(Export Selection As Reference Options)

要访问这些选项，请在“大纲视图”(Outliner)中，通过右键单击要导出为被引用文件的对象，然后选择“引用将当前选择导出为引用”(Reference > Export Selection As Reference) > ![图：要访问这些选项，请在“大纲视图”(Outliner)中，通过右键单击要导出为被引用文件的对象，然后选择“引用将当前选择导…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2579 字 ≥300，非承重" -->

在将场景中的选定对象导出为被引用文件时指定导出设置。另请参见[导出文件引用](../使用文件引用/导出文件引用.md)。

## 常规选项(General Options)

#### 文件类型(File type)

指定要用于场景导出的文件类型。选定的文件类型决定了将显示在“导出选项”(Export Options)窗口中的导出选项。

**注**

自 Maya 2014 起，mayaBinary (.mb) 文件格式使用 64 位索引。导出为 .mb 文件的场景与低于 2014 的 Maya 版本不兼容。

#### 默认文件扩展名(Default file extensions)

启用此选项（默认设置）后，导出具有选定“文件类型”(File type)的扩展名的文件。

## 包括选项(Include Options)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 2579 字 ≥300，非承重" -->

以下“包括选项”(Include Options)取决于您选择的导出文件格式。

#### 包括以下输入(Include these inputs)

启用或禁用下列项，可以启用或禁用特定节点类型的导出：

#### 包括纹理信息(Include Texture Info)

启用此选项后，纹理图像将包括在导出之列。

#### 其他导出选项

以下导出选项仅适用于 FBX、USD、Obj、Atom、X3D 和任何其他自定义导出器。

## 引用选项(Reference Options)

#### 锁定(Lock)

当文件引用加载到场景中时，锁定文件引用。也就是说，选定文件引用的所有节点和属性均处于锁定状态，因此不会被意外修改。锁定图标显示在“引用编辑器”(Reference Editor)中列出的文件引用旁边，用于指示锁定状态。

#### 分组(Group)

指定引用文件时是否将被引用对象分组到一个变换下。通过分组可以更轻松地处理导入对象的节点。默认设置为禁用。

#### 组名称(Group Name)

指定分组引用的名称。参考组将按此名称显示在“大纲视图”(Outliner)中。

#### 定位器(Locator)

与“分组”(Group)选项一起使用时，会将被引用文件的内容分组到定位器下，并使用引用节点的名称进行注释。引用节点具有一条连接至定位器变换的消息。如果指定了“组名称”(Group Name)，则定位器将按此名称显示在“大纲视图”(Outliner)中。

### 共享引用选项(Shared Reference Options)

#### 共享节点(Shared Nodes)

设置节点之间是否共享了显示层、着色网络或渲染层等等。如果被引用文件与引用文件中存在相同名称的渲染层、显示层或着色网络，启用此选项即可让引用文件和被引用文件共享这些节点。

对于共享显示层，合并仅根据名称决定是否进行。如果两个层名称相同，且共享显示层处于启用状态，则会对内容进行合并。

对于共享的着色网络，仅在节点名称和类型均相同的情况下，才会进行合并。

#### 显示层(Display Layers)

启用后，与引用的子场景关联的显示层将集成到父场景中。

请参见[共享显示层](../文件引用提示/共享显示层.md)。

#### 着色网络(Shading Networks)

启用后，引用的场景中的着色网络将与当前场景（以及任意引用）中的着色网络合并。这可以避免在整个场景（包括引用）中使用同一着色网络时，重复创建着色网络的问题。

请参见[文件引用和着色](../文件引用提示/文件引用和着色.md)。

#### 渲染层(Render Layers)

创建引用后，与子场景关联的渲染层将集成到父场景中。

可以选择“按名称”(by Name)还是“按编号”(by Number)使用渲染层来确定要合并的渲染层。如果父场景中已存在该渲染层的名称或 ID，则当对子场景中指定到该同名或同 ID 渲染层的对象进行引用时，系统会将这些对象都添加到引用场景的渲染层中。

## 名称空间选项(Namespace Options)

#### 使用名称空间(Use namespaces)

如果在启用“使用名称空间”(Use namespaces)的情况下引用或导入场景，则 Maya 将创建包含被引用数据的新名称空间。启用“使用名称空间”(Use namespaces)可确保所有节点都具有唯一的名称。请参见[名称空间](../../../../名称空间/名称空间.md)和[在引用或导入时创建名称空间](../../../../名称空间/名称空间/创建名称空间.md#GUID-E173CC3D-1638-499C-9F38-73735934D8E5__SECTION_EB9F55D366104ECB812FB39664922200)。

**注**

提示：

在引用文件之前，请确保重命名前缀不包含任何无效字符。

当前设置的名称空间是在“名称空间选项”(Namespace Options)区域中由 ![图：当前设置的名称空间是在“名称空间选项”(Namespace Options)区域中由 图标指示的。当前设置的名称空间的父…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-085BFA65-7807-43B8-B3C3-3D2393EB8AFB.png) <!-- baize:img-hook downloaded=false reason="正文 2579 字 ≥300，非承重" --> 图标指示的。当前设置的名称空间的父名称空间是由 ![图：当前设置的名称空间是在“名称空间选项”(Namespace Options)区域中由 图标指示的。当前设置的名称空间的父…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-7571C01F-9603-46CB-ACC9-FB41C5768745.png) <!-- baize:img-hook downloaded=false reason="正文 2579 字 ≥300，非承重" --> 图标指示的。当前名称空间可以在“名称空间编辑器”(Namespace Editor)中通过单击“设置当前空间名称”(Set Current)进行设置。请参见[名称空间编辑器概述](../../../../名称空间/名称空间/名称空间编辑器%28Namespace%20Editor%29.md)和[编辑名称空间](../../../../名称空间/名称空间/编辑名称空间.md)。

名称空间不影响 Maya 的当前选择、DAG、依存关系图或任何其他方面。

#### 使用选定的名称空间作为父对象并添加新的名称空间(文件名) (Use selected namespace as parent and add new namespace (file name))

指定将引用的文件名添加到对象名称空间的开头。

例如，如果引用或导入的名为 foo.ma 的场景中包含名为 ball 的对象，则其名称空间为 foo:ball。

#### 使用选定的名称空间作为父对象并添加新的名称空间字符串(Use selected namespace as parent and add new namespace string)：

指定将文本字符串添加到对象名称的开头。在显示的字段中键入字符串。

#### 合并到选定名称空间并重命名匹配的传入对象(Merge into selected namespace and rename incoming objects that match)

将对象的名称空间与现有的选定名称空间合并。

如果出现重复的名称空间，将合并这些名称空间，并且重复的对象名称将以递增的数字作为后缀。使用此选项可以避免在每次引用或导入具有相同名称空间的对象时累积新的名称空间。

## 文件类型特定选项(File Type Specific Options)

#### 使用节点上属性的全名(Use full names for attributes on nodes)

可以在是否使用全名之间切换。

**注**

导出选择时，除导出选定节点本身之外，也将导出下列关联的节点：

- 选定节点的父对象

- 盲数据模板节点

- 灯光链接器节点

## 相关主题

- [使用文件引用](../使用文件引用.md)

- [导出全部选项(Export All Options)/导出当前选择选项(Export Selection Options)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/files/GUID-A1E550E4-1510-4D45-A811-5E424A8D3924.htm)

- [名称空间](../../../../名称空间/名称空间.md)

- [引用编辑](../引用编辑.md)
