# 在 SynColor 中使用用户颜色变换

可以在使用内置颜色空间选项的同时使用用户定义的颜色变换，或使用用户定义的颜色变换替代内置颜色空间选项。添加了用户变换之后，它会显示在相应的菜单上。

**注**

这些步骤仅在使用旧版颜色管理系统（称为 SynColor）时适用。若要结合使用自定义颜色空间与默认 OCIO v2 颜色管理系统，必须使用可定义所需空间的自定义 OCIO 配置文件。

若要将用户变换添加到可用选项，需要一个执行以下操作之一的变换：

- 对于输入空间，您的变换必须从要添加的颜色空间转化为已识别的输入颜色空间之一（请参见[输入颜色空间列表](../输入颜色空间列表.md)）。

- 对于视图或输出变换，变换必须从可用选项之一转化为要添加的颜色空间。

变换可以是 SynColor .ctf 文件，也可以采用任意第三方格式。请参见[支持的颜色变换文件格式](Autodesk%20颜色管理%20-%20补充信息/颜色变换文件/支持的颜色变换文件格式.md)。

用户变换以 .ctf 文件形式存储于在[颜色管理首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2D9BBB9D-49F0-44C6-8BFF-B237FD8ED746)中设置的“用户变换/LUT 目录路径”(User Transform/LUT Directory Path)中。它们包括对包含变换的文件的引用，可以存储在任何位置。此外，用户变换还包括其他元数据，如输入或输出颜色空间。元数据允许 Autodesk 颜色管理自动构建一系列变换，以通过连接空间从一种颜色空间转化到另一种颜色空间。

如果结合使用 SynColor 和 OCIO v1 配置文件进行颜色管理，则不能使用用户变换。使用 OCIO 配置文件时，只有配置文件中指定的颜色变换可用。

颜色空间按名称匹配。如果您打开的场景使用了一个不可用的用户变换，将显示一条消息。如果“文件”(File)纹理和其他节点使用的任意输入颜色空间不存在，将在“属性编辑器”(Attribute Editor)中以红色亮显该颜色空间。此外，图像输入节点中任何缺少的颜色空间在属性编辑器中都以红色亮显，且不应用变换。请参见[修复缺少的颜色变换](../颜色管理任务/修复缺少的颜色变换.md)。

## 添加用户变换

1. 在[颜色管理首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2D9BBB9D-49F0-44C6-8BFF-B237FD8ED746)中，展开变换或颜色空间下拉菜单之一，然后选择“+ 添加新项目”(+ Add New) 。

  也可以使用“渲染设置”(Render Settings)窗口“公用”(Common)选项卡的“颜色管理”(Color Management)组中的“输出变换”(Output Transform)菜单。

2. 在“变换文件”(Transform File)中，输入 LUT 或其他颜色变换文件的路径和文件名。

  **注**

  提示：

  Autodesk 变换集合位于

  Maya

  安装位置的 synColor/transforms/ 文件夹中。它包括默认情况下菜单上未提供的许多变换。

3. 在“变换名称”(Transform Name)中，输入希望显示在菜单中的自定义变换的标签。

4. 执行下列操作之一：

  - 对于输入空间变换，将“目标颜色空间”(Destination Color Space)设置为变换的预期输出颜色空间。

  - 对于视图和输出变换，将“源颜色空间”(Source Color Space)设置为变换的预期输入颜色空间。如果变换的输入与渲染空间相同，则可以选择“原始”(Raw)。

5. 单击“确定”(OK)。

## 移除用户变换

移除用户变换将移除引用“用户变换/LUT 目录路径”(User Transform/LUT Directory Path)中变换的 .ctf 文件，但不会移除引用的变换本身。

1. 在其中一个菜单中选择用户变换。

2. 单击齿轮图标，然后选择“移除”(Remove)。

不能移除任何内置的变换。
