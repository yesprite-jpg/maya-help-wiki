# 导出全部选项(Export All Options)/导出当前选择选项(Export Selection Options)

使用这些选项可设置在选择“文件 > 导出全部”(File > Export All)或“文件 > 导出当前选择”(File > Export Selection)时发生的情况。另请参见[将对象导出到新文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-664060EB-EA35-4CD3-83EB-CBCAF59B4495)。

## 常规选项(General Options)

#### 文件类型(File type)

指定要用于场景导出的文件类型。选定的文件类型决定了将显示在“导出选项”(Export Options)窗口中的导出选项。

**注**

自 Maya 2014 起，mayaBinary (.mb) 文件格式使用 64 位索引。导出为 .mb 文件的场景与低于 2014 的 Maya 版本不兼容。

#### 默认文件扩展名(Default file extensions)

启用此选项（默认设置）后，导出具有选定“文件类型”(File type)的扩展名的文件。

## 引用选项(Reference Options)

为包含文件引用的场景指定导出选项。

#### 保留引用(Preserve references)

如果启用“保留引用”(Preserve Reference)，则将保持导出文件中的引用。如果禁用此选项，则所有引用都将导出到文件中；也就是说，它们将不再是引用，而是场景中的对象。默认设置为禁用。

#### 导出卸载引用(Export unloaded references)

导出与当前场景关联的所有卸载引用文件。

#### “仅保持一个引用”(Keep only a reference)（仅限“导出当前选择”(Export Selection)）

将场景中的选定对象作为引用文件导出，并使用指定的名称空间选项将这些对象加载回当前场景。

#### 使用名称空间(Use namespaces)

使用指定的名称空间导出引用。请参见[名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B796BE38-72AC-4B9E-9C03-3C27C3EAA171)。

#### 前缀为(Prefix with)

指定如何生成名称空间。

#### 文件名(the file name)

指定将引用的文件名添加到对象名称空间的开头。

#### 此字符串(this string)

指定将文本字符串添加到对象名称的开头。

## 包括选项(Include Options)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 4171 字 ≥300，非承重" -->

以下“包括选项”(Include Options)取决于您选择的导出文件格式。

#### 包括以下输入(Include these inputs)

启用或禁用下列项，可以启用或禁用特定节点类型的导出：

##### 历史(History)

这是与 file -constructionHistory (-ch) 命令等效的 UI。

**注**

可以在

“节点编辑器”(Node Editor)

中导出连接节点上的所选内容。如果构建历史输入选项（“历史”(History)）处于禁用状态（未选中），那么无论该设置如何，导出的选定节点都将保持其相互之间的历史节点属性连接。但在某些情况下，在导出之前被隐藏并且未被选中的任何辅助节点可能会断开这些节点连接。对于此特定工作流，请在

“节点编辑器”(Node Editor)的

“显示”(Show)

菜单中启用辅助节点的显示，以确保在导出选择操作之前将这些节点包含在选择中。

##### 通道(Channels)

这是与 file -channels(-chn) 命令等效的 UI。

##### 表达式

这是与 file -expressions(-exp) 命令等效的 UI。

##### 约束(Constraints)

这是与 file -constraints(-con) 命令等效的 UI。

#### 包括纹理信息(Include Texture Info)

启用此选项后，纹理图像将包括在导出之列。

#### 其他导出选项

以下导出选项仅适用于 FBX、USD、Obj、Atom、X3D 和任何其他自定义导出器。

## 文件类型特定选项(File Type Specific Options)

这些选项将根据您在“常规选项”(General Options)中选择的“文件类型”(File type)进行更改。

**注**

有关 FBX 导出，请参见

Maya FBX 插件首选项

中的

FBX 导出的文件类型特定选项(File Type Specific Options)

。

**注**

有关 USD 的

“文件类型特定选项”(File Type Specific Options)

的信息，请参见

USD 导出选项

。

#### 使用节点上属性的全名(Use full names for attributes on nodes)

可以在是否使用全名之间切换。

**注**

导出选择时，除导出选定节点本身之外，也将导出下列关联的节点：

- 选定节点的父对象

- 盲数据模板节点

- 灯光链接器节点

#### 包含(Include)

#### 连接(Connections)

- 包括子对象(Include Children)：启用（默认）后，选定对象下方的层次将包括在导出之列。

## 缩略图/播放预览选项(Thumbnail/Playblast Options)

这些选项与[保存场景选项(Save Scene Options)](保存场景选项%28Save%20Scene%20Options%29.md)中的选项相同。有关使用这些选项的信息，请参见[创建场景文件的缩略图和播放预览](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B3FB68-AAA4-415D-A37B-1EAC461613C0)。

## Maya 自身文件（.ma 和 .mb）选项

对于 Maya ASCII (.ma) 和 Maya 二进制格式 (.mb) 而言，“导出全部”(Export All)选项与[场景另存为选项(Save Scene As Options)](场景另存为选项%28Save%20Scene%20As%20Options%29.md)的效果相同。

**注**

“mayaAscii”

和

“mayaBinary”

文件格式是仅有的保留场景中所含全部信息的两种格式。使用

“导出选项”(Export Options)

框设置导出的输出格式将更改当前和后续导出操作的默认导出格式。如果将输出格式设置为除

mayaAscii

或

mayaBinary

之外的格式，并使用该格式导出，然后在未保存整个文件的情况下退出，则可能会丢失数据。

务必在导出文件浏览器中检查导出类型，确保正在使用预期文件格式写入文件。

## 移动文件选项

#### 属性(Attributes)

在“属性”(Attributes)框键入属性名称，然后单击“添加”(Add)，将该属性添加到属性列表中，供导入或导出时使用。如果属性已包含在列表中，系统将不会重复此属性。若要移除一个属性，请输入该属性的名称，然后单击“移除”(Remove)。通过空格分隔属性可以一次添加多个属性。

#### 来自通道盒(From Channel Box)

单击“来自通道盒”(From Channel Box)可以将 Maya 中所有选定的对象按对象的选择顺序与在“通道盒”(Channel Box)中选定的通道合并，然后将其置于列表中。例如，选定了球体 (sphere) 和圆锥体 (cone)，“通道盒”(Channel Box)中选定了 tx 和 sx，则 sphere.tx、sphere.sx、cone.tx 和 cone.sx 将添加到属性列表中，用于导入和导出。

#### 移除选定对象(Remove Selected)

单击“移除选定对象”(Remove Selected)可以移除列表中选定的所有属性。

#### 移除全部(Remove All)

单击“移除全部”(Remove All)可以移除列表中的所有属性。

#### 精度(Precision)

文件导出时将忽略此选项。对于文件导入，这将设置文件的精度。

单击导入或导出时，系统将写入或读取移动文件，只有列表中的属性将受到影响。

## 动画曲线选项（animExport 文件类型）

必须加载 animImportExport 插件才能选择 animExport 文件类型和查看这些选项。（请参见[加载或卸载 Maya 插件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-07A89E6C-199C-4719-98A0-11C3A2BCDF21)。）

#### 精度(Precision)

设置存储在文件中的数字精度。选项如下：

#### 浮点型(Float)

八位数精度

#### 双精度(Double)

十七位数精度

#### 自定义(Custom)

介于 1 到 18 之间的设置。

#### 文件内容(File Contents)

文件内容设置：

#### 使用节点和叶属性名称(Use node and leaf attribute names)

启用此选项时，剪贴板中的节点和叶属性名称将写入到文件中。

禁用此选项时，只有完整的属性名称将写入到文件中。

#### 详细单位(Verbose units)

选中“详细单位”(Verbose units)复选框时，文件中将使用长单位名称；否则使用短单位名称。

#### 层次(Hierarchy)

“层次”设置控制要复制的层次内节点。

#### 选定(Selected)

仅选定对象的动画将复制到关键帧剪贴板。

#### 下方(Below)

将选定对象的动画及其下方的所有对象复制到剪贴板。

#### 通道(Channels)

仅当要复制“通道盒”(Channel Box)中选定的属性时，该设置可用。

#### 所有可设定关键帧(All Keyable)

将所有选定对象的动画可设定关键帧通道复制到剪贴板。

#### 来自通道盒(From Channel Box)

仅将“通道盒”(Channel Box)中选定的通道复制到剪贴板。

#### 控制点(Control Points)

此选项将启用或禁用与几何体图形（或几何体图形层次上方的变换节点）相关联的所有 CV、多边形顶点和晶格点的复制操作。

通常情况下，复制一个控制点时，系统仅会复制选定的控制点。“控制点”(Control Points)选项将启用与对象相关联的所有控制点的复制操作。当您处理控制点密集型动画而又不希望选择每个控制点复制动画时，该选项非常有用。

#### 形状(Shapes)

设置是复制对象图形属性的动画和关联变换属性的动画，还是仅复制变换节点的动画。

通常情况下，如果在建模窗口中选择对象，则变换节点（位于图形层次上方）将处于选中状态。

例如，如果选择了摄影机、NURBS 对象或灯光，则系统也将选择关联的变换节点进行复制。

#### 时间范围(Time Range)

从以下选项中进行选择来指定要从选定对象导出的动画片段：

#### 全部

将选定对象的所有动画信息全部复制到关键帧剪贴板。

#### 开始/结束(Start/End)

仅将选定对象的“开始时间”(Start Time)和“结束时间”(End Time)字段中指定范围内的动画信息复制到关键帧剪贴板。

#### 帮助图像(Help Images)

选中后，该选项将显示复制操作的图表，以图像方式特别呈现复制动画信息的两种方法。

#### 方法(Method)

从下列选项中进行选择：

#### 关键帧(Keys)

仅将选定范围内的关键帧复制到关键帧剪贴板。

#### 分段(Segments)

将选定范围内的动画曲线分段和任何关键帧都复制到关键帧剪贴板。

**注**

“分段”复制关键帧的方法将在复制的动画分段的开始和结束时间处创建关键帧，以便在这些点中不存在关键帧时，系统仍保留动画曲线的图形。

## 相关主题

- [支持的文件格式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3FDB6F01-1830-4AB3-BB91-287A64A269A6)

- [创建、打开或保存场景文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DC183670-EF0F-4E69-AEDF-69D408D82408)

- [崩溃后恢复数据](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-89F4AF19-AFDC-40BF-8571-8999C520505C)

- [保存场景选项(Save Scene Options)](保存场景选项%28Save%20Scene%20Options%29.md)

- [场景另存为选项(Save Scene As Options)](场景另存为选项%28Save%20Scene%20As%20Options%29.md)

- [捕捉缩略图/播放预览(Capture Thumbnail/Playblast)](捕捉缩略图播放预览%28Capture%20ThumbnailPlayblast%29选项.md)
