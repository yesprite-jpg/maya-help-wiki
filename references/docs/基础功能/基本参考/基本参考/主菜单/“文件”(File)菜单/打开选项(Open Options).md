# 打开选项(Open Options)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 1874 字 ≥300，非承重" -->

使用这些选项可以设置在选择“文件 > 打开”(File > Open)时会发生什么变化。另请参见[创建、打开或保存场景文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DC183670-EF0F-4E69-AEDF-69D408D82408)。

## 常规选项(General options)

#### 文件类型(File type)

选择下次打开文件时的默认文件格式。

如果已经设置项目，那么打开场景时浏览器会指向包含该类型文件的目录。在 Windows 和 Mac OS X 上，它还可以设置过滤器以仅显示选定类型的文件。

根据选择的“文件类型”(File Type)，会显示各种的“文件类型特定选项”(File Type Specific Options)。

#### 执行脚本节点(Execute Script Nodes)

脚本节点包含 mayaAscii 或 mayaBinary 文件中的 MEL 脚本。可以指定一个脚本节点，以便在从文件中读取节点时或在渲染帧前后执行其脚本。

您可以使用“表达式编辑器”(Expression Editor)创建和编辑脚本节点。请参见 [MEL 脚本节点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-296601E8-F5C7-425C-AA8C-4BE5AB69C486)。

用户界面配置信息作为脚本节点的属性存储在 Maya 场景文件中。如果禁用“执行脚本节点”(Execute Script Nodes)选项，则不会执行 UI 脚本节点。但是，我们建议仅在脚本出错时才禁用脚本节点的执行。

## 引用(Referencing)

#### 加载设置(Load Settings)

#### 加载保存的引用加载状态(Load Saved Reference Load State)

遵循上次保存引用文件时引用文件中的被引用文件的状态。上次处理文件时加载或卸载的任何引用都将在文件再次打开时正确加载或卸载。

#### 加载所有引用(Load All References)

在加载所有引用的情况下打开文件。在 Maya 中打开文件后可以通过以下方法更改引用加载的状态：打开[引用编辑器(Reference Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8D8E0D4A-DE37-4C63-9F59-8D71F00E3367)，然后选择要卸载的引用。

#### 仅加载顶层级引用(Load Top-Level References Only)

仅加载最顶层的被引用文件（这些文件本身可能包含嵌套的被引用文件）。如果要打开包含许多嵌套引用的复杂嵌套场景引用层次，而您又想要轻松处理层次中的顶层级时，该选项将非常有用。

#### 不加载引用(Load No References)

这将在不加载任何引用的情况下打开文件。在 Maya 中打开文件后可以通过以下方法加载引用：打开[引用编辑器(Reference Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8D8E0D4A-DE37-4C63-9F59-8D71F00E3367)，然后选择要加载的引用。

#### 保留已卸载的名称空间(Reserve unloaded namespaces)

![图：选择此选项，以便即使不加载引用本身，也会创建引用的名称空间。这样可防止名称空间误用于其他节点和引用，导致在最终加载原始引…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1874 字 ≥300，非承重" -->

选择此选项，以便即使不加载引用本身，也会创建引用的名称空间。这样可防止名称空间误用于其他节点和引用，导致在最终加载原始引用时发生冲突。请参见[为已卸载引用创建名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C69B1AFA-F777-40D8-A537-F84CFAD48A81)。

#### 选择性预加载(Selective preload)

选择此选项将在打开任何文件之前先打开[预加载引用编辑器(Preload Reference Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-445AB4CD-1F87-4F2B-9FA0-C21C502F0455)。可以选择在文件中加载或延缓引用。

## 文件类型特定选项(File Type Specific Options)

根据您在“常规选项”(General Options)区域中指定的“文件类型”(File Type)，这些选项会有所不同。

### 对于“mayaAscii”、“mayaBinary”文件

#### 使用节点上属性的全名(Use full names for attributes on nodes)

显示文件中节点属性的全名。

例如，如果选择“使用节点上属性的全名”(Use Full Names for Attributes on Nodes)选项，在文本编辑器中打开 Maya ASCII 文件时，属性名称将按如下形式列出：setAttr.translate 0 0 0。如果禁用“使用属性的全名”(Use Verbose Names)选项，属性名称将按如下形式列出：setAttr .t 0 0 0。

### 对于“OBJ”文件

#### 单个对象(Single Object)/多个对象(Multiple Objects)

指定如何在 OBJ 文件中创建形状。

“多个对象”(Multiple Objects)可以基于 OBJ 文件中指定的分组信息创建各个形状。“单个对象”(Single Object)可以利用对应于指定的各组的对象集为整个文件创建一个形状。

组不能重叠。如果存在重叠的组，Maya 会通知用户存在重叠组，并会重新读取文件，就如同将选项设置为“单个对象”(Single Object)一样。

### “移动”(Move)文件

必须导入移动文件。请参见[导入选项(Import Options)](导入选项%28Import%20Options%29.md)。

### Illustrator 和 EPS 文件

必须导入 Illustrator 和 EPS 文件。请参见[导入选项(Import Options)](导入选项%28Import%20Options%29.md)。

### 相关主题

- [支持的文件格式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3FDB6F01-1830-4AB3-BB91-287A64A269A6)

- [导入文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BB7ABDA1-86E6-4A83-B8E6-3F4D7F1B0F1B)

- [引用选项](引用选项%28Reference%20Options%29.md)
