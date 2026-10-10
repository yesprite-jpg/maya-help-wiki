# 引用选项(Reference Options)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 3130 字 ≥300，非承重" -->

使用这些选项可设置选择“文件 > 创建引用”(File > Create Reference)时会发生什么变化。另请参见[创建文件引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-00DA055B-3559-4E60-979F-DA862BBCA9C8)。

**注**

若要引用在 Maya 的早期版本中创建的文件，请确保已启用

“文件项目首选项”(Files Projects preferences)

中的

“忽略版本”(Ignore Version)

首选项。

## 常规选项(General Options)

#### 延缓(Deferred)

启用该选项时，任何添加到场景中的已创建引用都处于未加载状态，仅在手动加载后才会显示。

#### 锁定(Lock)

当文件引用加载到场景中时，锁定文件引用。也就是说，选定文件引用的所有节点和属性均处于锁定状态，因此不会被意外修改。锁定图标显示在“引用编辑器”(Reference Editor)中列出的文件引用旁边，用于指示锁定状态。

#### 分组(Group)

指定引用文件时是否将被引用对象分组到一个变换下。通过分组可以更轻松地处理导入对象的节点。默认设置为禁用。

#### 组名称(Group Name)

指定分组引用的名称。参考组将按此名称显示在“大纲视图”(Outliner)中。

#### 定位器(Locator)

与“分组”(Group)选项一起使用时，会将被引用文件的内容分组到定位器下，并使用引用节点的名称进行注释。引用节点具有一条连接至定位器变换的消息。如果指定了“组名称”(Group Name)，则定位器将按此名称显示在“大纲视图”(Outliner)中。

#### 文件类型(File type)

从下拉列表中选择要导入的文件类型。如果不能确定要导入的文件类型，可以选择“最佳推测”(Best Guess)。

另请参见[导入选项(Import Options)](导入选项%28Import%20Options%29.md)。

## 加载选项(Load Options)

#### 加载保存的引用加载状态(Load saved reference load state)

（默认设置）遵循上次保存引用文件时引用文件中的被引用文件的状态。上次处理文件时加载或卸载的任何引用都将在文件重新打开时正确加载或卸载。

#### 加载所有引用(Load all references)

在加载所有引用的情况下打开文件。在 Maya 中打开文件后可以通过以下方法更改引用加载的状态：打开[引用编辑器(Reference Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8D8E0D4A-DE37-4C63-9F59-8D71F00E3367)，然后选择要卸载的引用。

#### 仅加载顶层级引用(Load top-level references only)

仅加载最顶层的被引用文件（这些文件本身可能包含嵌套的被引用文件）。如果要打开包含许多嵌套引用的复杂嵌套场景引用层次，而您又想要轻松处理层次中的顶层级时，该选项将非常有用。

#### 不加载引用(Load no references)

这将在不加载任何引用的情况下打开文件。在 Maya 中打开文件后可以通过以下方法加载引用：打开[引用编辑器(Reference Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8D8E0D4A-DE37-4C63-9F59-8D71F00E3367)，然后选择要加载的引用。

#### 保留已卸载的名称空间(Reserve unloaded namespaces)

![图：选择此选项，以便即使不加载引用本身，也会创建引用的名称空间。这样可防止名称空间误用于其他节点和引用，导致在最终加载原始引…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 3130 字 ≥300，非承重" -->

选择此选项，以便即使不加载引用本身，也会创建引用的名称空间。这样可防止名称空间误用于其他节点和引用，导致在最终加载原始引用时发生冲突。请参见[为已卸载引用创建名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C69B1AFA-F777-40D8-A537-F84CFAD48A81)。

## 共享引用选项(Shared Reference Options)

#### 共享节点(Shared Nodes)

设置节点之间是否共享了显示层、着色网络或渲染层等等。如果被引用文件与引用文件中存在相同名称的渲染层、显示层或着色网络，启用此选项即可让引用文件和被引用文件共享这些节点。

对于共享显示层，合并仅根据名称决定是否进行。如果两个层名称相同，且共享显示层处于启用状态，则会对内容进行合并。

对于共享的着色网络，仅在节点名称和类型均相同的情况下，才会进行合并。

#### 显示层(Display Layers)

启用后，与引用的子场景关联的显示层将集成到父场景中。

请参见[共享显示层](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-69988528-F956-4383-860C-A8A8E1F4D480)。

#### 着色网络(Shading Networks)

启用后，引用的场景中的着色网络将与当前场景（以及任意引用）中的着色网络合并。这可以避免在整个场景（包括引用）中使用同一着色网络时，重复创建着色网络的问题。

请参见[文件引用和着色](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-83E8811C-BEE2-4753-8F83-4E9EEE66D7DD)。

#### 渲染层(Render Layers)

创建引用后，与子场景关联的渲染层将集成到父场景中。

可以选择“按名称”(by Name)还是“按编号”(by Number)使用渲染层来确定要合并的渲染层。如果父场景中已存在该渲染层的名称或 ID，则当对子场景中指定到该同名或同 ID 渲染层的对象进行引用时，系统会将这些对象都添加到引用场景的渲染层中。

## 名称空间选项(Namespace Options)

#### 使用名称空间(Use namespaces)

如果在启用“使用名称空间”(Use namespaces)的情况下引用或导入场景，则 Maya 将创建包含被引用数据的新名称空间。启用“使用名称空间”(Use namespaces)可确保所有节点都具有唯一的名称。请参见[名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B796BE38-72AC-4B9E-9C03-3C27C3EAA171)和[在引用或导入时创建名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E173CC3D-1638-499C-9F38-73735934D8E5#GUID-E173CC3D-1638-499C-9F38-73735934D8E5__SECTION_EB9F55D366104ECB812FB39664922200)。

**注**

提示：

在引用文件之前，请确保重命名前缀不包含任何无效字符。

当前设置的名称空间是在“名称空间选项”(Namespace Options)区域中由 ![图：当前设置的名称空间是在“名称空间选项”(Namespace Options)区域中由 图标指示的。当前设置的名称空间的父…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-085BFA65-7807-43B8-B3C3-3D2393EB8AFB.png) <!-- baize:img-hook downloaded=false reason="正文 3130 字 ≥300，非承重" --> 图标指示的。当前设置的名称空间的父名称空间是由 ![图：当前设置的名称空间是在“名称空间选项”(Namespace Options)区域中由 图标指示的。当前设置的名称空间的父…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-7571C01F-9603-46CB-ACC9-FB41C5768745.png) <!-- baize:img-hook downloaded=false reason="正文 3130 字 ≥300，非承重" --> 图标指示的。当前名称空间可以在“名称空间编辑器”(Namespace Editor)中通过单击“设置当前空间名称”(Set Current)进行设置。请参见[名称空间编辑器概述](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8139C5B1-3C37-43DF-965E-39800AA98EE2)和[编辑名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9E2F2AF6-48F3-4628-B23E-0B8A07EAF737)。

名称空间不影响 Maya 的当前选择、DAG、依存关系图或任何其他方面。

#### 使用选定的名称空间作为父对象并添加新的名称空间(文件名) (Use selected namespace as parent and add new namespace (file name))

指定将引用的文件名添加到对象名称空间的开头。

例如，如果引用或导入的名为 foo.ma 的场景中包含名为 ball 的对象，则其名称空间为 foo:ball。

#### 使用选定的名称空间作为父对象并添加新的名称空间字符串(Use selected namespace as parent and add new namespace string)：

指定将文本字符串添加到对象名称的开头。在显示的字段中键入字符串。

#### 合并到选定名称空间并重命名匹配的传入对象(Merge into selected namespace and rename incoming objects that match)

将对象的名称空间与现有的选定名称空间合并。

如果出现重复的名称空间，将合并这些名称空间，并且重复的对象名称将以递增的数字作为后缀。使用此选项可以避免在每次引用或导入具有相同名称空间的对象时累积新的名称空间。

## 代理选项(Proxy Options)

#### 将代理标记设置为(Set proxy tag to)

为要应用于代理引用的代理标记键入文本字符串，或者从下拉菜单的列表中选择现有标记。如果代理标记在此列表中以灰色显示，则表示该标记已用于该此特定的文件引用。代理标记将显示在“引用编辑器”(Reference Editor)中。

创建代理标记后，该标记在“代理选项”(Proxy Options)和“引用选项”(Reference Options)窗口中的“将代理标记设置为”(Set proxy tag to)下拉列表菜单中即成为可选项。

请参见[关于代理标记](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A34798B1-53F2-46DB-B11A-8B3FBDEA7A6C)。

创建代理标记后，该标记在“代理选项”(Proxy Options)和“引用选项”(Reference Options)窗口中的“将代理标记设置为”(Set proxy tag to)下拉列表菜单中即成为可选项。

各代理标记在给定代理集中必须是唯一的。也就是说，如果一个代理标记在某个代理集内不在使用中，则该代理标记可供同一个代理集使用。可以自行创建标记，并在不同的代理集中重用。

## 相关主题

- [文件引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-238914C9-4129-454C-99D7-B8C57AF423DB)

- [使用文件引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6E6A219A-1EAE-418A-A92D-91B833BC40AE)

- [关于代理引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C88F2A7A-B25A-4FCD-838B-2B80B230CA39)

- [使用代理引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-11182679-1A3D-4A05-845B-19FBBAEC786A)

- [名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B796BE38-72AC-4B9E-9C03-3C27C3EAA171)

- [文件引用提示](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4C69BD15-DD28-4631-8EC2-2EEC59B7157A)
