# 指定脱机文件选项(Assign Offline File Options)

使用这些选项可以设定在选择“文件 > 指定脱机文件”(File > Assign Offline File)时会发生什么变化。另请参见[指定脱机文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8D2F8B56-8546-42A7-B31D-A088D1EC2698)。

## 常规选项(General Options)

#### 应用方式(Apply via)

允许作为任一被引用编辑应用编辑，或者直接将编辑导入到场景中。导入的编辑将烘焙到主场景，无法像被引用编辑一样卸载。

#### 为主场景指定脱机编辑(Assign offline edits to main scene)

如果启用了该选项，则脱机编辑将存储在主场景中。否则，编辑将存储为文件引用。

#### 文件类型(File type)

从下拉列表中选择要导入的文件类型。如果不确定要应用的文件类型，可以选择“最佳推测”。

根据选择的文件类型，可能会显示多种文件类型特定选项。

## 名称空间选项(Namespace Options)

#### 使用名称空间(Use namespaces)

如果在启用“使用名称空间”(Use namespaces)的情况下引用或导入场景，则 Maya 将创建包含被引用数据的新名称空间。启用“使用名称空间”(Use namespaces)可确保所有节点都具有唯一的名称。请参见[名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B796BE38-72AC-4B9E-9C03-3C27C3EAA171)和[在引用或导入时创建名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E173CC3D-1638-499C-9F38-73735934D8E5#GUID-E173CC3D-1638-499C-9F38-73735934D8E5__SECTION_EB9F55D366104ECB812FB39664922200)。

**注**

提示：

在引用文件之前，请确保重命名前缀不包含任何无效字符。

当前设置的名称空间是在“名称空间选项”(Namespace Options)区域中由 ![图：当前设置的名称空间是在“名称空间选项”(Namespace Options)区域中由 图标指示的。当前设置的名称空间的父…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-085BFA65-7807-43B8-B3C3-3D2393EB8AFB.png) <!-- baize:img-hook downloaded=false reason="正文 1548 字 ≥300，非承重" --> 图标指示的。当前设置的名称空间的父名称空间是由 ![图：当前设置的名称空间是在“名称空间选项”(Namespace Options)区域中由 图标指示的。当前设置的名称空间的父…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-7571C01F-9603-46CB-ACC9-FB41C5768745.png) <!-- baize:img-hook downloaded=false reason="正文 1548 字 ≥300，非承重" --> 图标指示的。当前名称空间可以在“名称空间编辑器”(Namespace Editor)中通过单击“设置当前空间名称”(Set Current)进行设置。请参见[名称空间编辑器概述](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8139C5B1-3C37-43DF-965E-39800AA98EE2)和[编辑名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9E2F2AF6-48F3-4628-B23E-0B8A07EAF737)。

名称空间不影响 Maya 的当前选择、DAG、依存关系图或任何其他方面。

#### 使用选定的名称空间作为父对象并添加新的名称空间(文件名) (Use selected namespace as parent and add new namespace (file name))

指定将引用的文件名添加到对象名称空间的开头。

例如，如果引用或导入的名为 foo.ma 的场景中包含名为 ball 的对象，则其名称空间为 foo:ball。

#### 使用选定的名称空间作为父对象并添加新的名称空间字符串(Use selected namespace as parent and add new namespace string)：

指定将文本字符串添加到对象名称的开头。在显示的字段中键入字符串。

#### 合并到选定名称空间并重命名匹配的传入对象(Merge into selected namespace and rename incoming objects that match)

将对象的名称空间与现有的选定名称空间合并。

如果出现重复的名称空间，将合并这些名称空间，并且重复的对象名称将以递增的数字作为后缀。使用此选项可以避免在每次引用或导入具有相同名称空间的对象时累积新的名称空间。

#### 节点名称替换对象

在将其应用于场景时，允许对脱机编辑文件执行文本替换。可以指定一组或多组替换文本，并按它们在列表中显示的顺序将它们应用到文件。

例如，如果需要替换应用于名为 sphere1 的对象的所有编辑，并将这些编辑应用于名为 sphere2 的对象，则会在“搜索”(Search for)字段中键入 sphere1，并在“替换为”(Replace with)字段中键入 sphere2，然后单击“添加”(Add)。

#### 搜索(Search for)

键入要搜索的节点名称，然后单击“添加”(Add)。会将节点名称添加到列表区域中。若要移除节点名称，请在列表区域中选择它，然后单击移除(Remove)。

#### 替换为(Replace with)

键入要用作替换对象的节点名称，然后单击“添加”(Add)。会将节点替换对象规则添加到列表中。若要从列表中移除替换对象，请选择它，然后单击“移除”(Remove)。
