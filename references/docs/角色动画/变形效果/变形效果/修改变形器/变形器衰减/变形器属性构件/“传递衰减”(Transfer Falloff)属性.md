# “传递衰减”(Transfer Falloff)属性

“传递衰减”(Transfer Falloff)的“属性编辑器”(Attribute Editor)构件包含一个表，您可以在其中指定如何将衰减权重从一个变形器应用到另一个变形器。

访问“传递衰减”(Transfer Falloff)属性编辑器构件

- [将变形器衰减应用于几何体](../创建变形器衰减.md)后，在“属性编辑器”(Attribute Editor)的[“变形器属性”(Deformer Attributes)构件](../变形器属性构件.md)中选择“创建传递衰减”(Create Transfer Falloff)。此时将显示“传递衰减属性”(Transfer Falloff Attributes)选项卡。

有关如何将组件标记附加到组件的信息，请参见[使用组件标记创建变形器衰减](../创建变形器衰减.md)。

使用“添加新指定”(Add New assignment) ![图：使用“添加新指定”(Add New assignment) 、“移除指定”(Remove assignment) 、“上…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-B5E33AF1-E48D-488D-91A2-741BE6430588.png) <!-- baize:img-hook downloaded=false reason="正文 1039 字 ≥300，非承重" -->、“移除指定”(Remove assignment) ![图：使用“添加新指定”(Add New assignment) 、“移除指定”(Remove assignment) 、“上…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-13A1DBD2-73D8-4551-9BC7-16F7B375101A.png) <!-- baize:img-hook downloaded=false reason="正文 1039 字 ≥300，非承重" -->、“上移”(Move Up) ![图：使用“添加新指定”(Add New assignment) 、“移除指定”(Remove assignment) 、“上…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-60321F79-3B0F-4BDE-BDAB-4052742B9647.png) <!-- baize:img-hook downloaded=false reason="正文 1039 字 ≥300，非承重" --> 和“下移”(Move Down) ![图：使用“添加新指定”(Add New assignment) 、“移除指定”(Remove assignment) 、“上…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-48E848B6-936E-4E42-866A-7241AC284246.png) <!-- baize:img-hook downloaded=false reason="正文 1039 字 ≥300，非承重" --> 图标来组织表中的衰减效果。

#### 基础权重(Base Weight)

为总体效果设置“基础权重”(Base Weight)。默认值为 **1.00**。每个顶点的值都由该设置定义。

#### “组件”(Component)表

使用“组件”(Component)表来组织和融合衰减效果。

#### 索引(Idx)

组件衰减数组中的衰减索引（放置）。使用“上移”(Move Up) ![图：组件衰减数组中的衰减索引（放置）。使用“上移”(Move Up) 和“下移”(Move Down) 图标以重新排列衰减顺…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-60321F79-3B0F-4BDE-BDAB-4052742B9647.png) <!-- baize:img-hook downloaded=false reason="正文 1039 字 ≥300，非承重" --> 和“下移”(Move Down) ![图：组件衰减数组中的衰减索引（放置）。使用“上移”(Move Up) 和“下移”(Move Down) 图标以重新排列衰减顺…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-48E848B6-936E-4E42-866A-7241AC284246.png) <!-- baize:img-hook downloaded=false reason="正文 1039 字 ≥300，非承重" --> 图标以重新排列衰减顺序。

#### 层名称(Layer Name)

要融合的变形器衰减效果的名称。

#### 重量

变形器衰减效果的权重值。

在“权重”(Weight)字段上单击鼠标右键，可以设置关键帧或锁定权重，以及创建新的表达式或纹理。

#### 创建新表达式...(Create New Expression...)

打开[表达式编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-251640EA-AACC-4F1B-A341-297F0F4CEFE4)。

#### 设置关键帧(Set Key)

为衰减的“权重”(Weight)值设置关键帧。

当“权重”(Weight)属性已设置关键帧时，“权重”(Weight)字段在设置了关键帧的帧上变成亮红色，而暗红色表示该值上有关键帧。

设置关键帧后，在“权重”(Weight)字段上单击鼠标右键，然后选择“断开连接”(Break Connection)以移除关键帧以及到该属性的所有连接。

#### 创建新纹理...(Create New Texture...)

打开[创建渲染节点(Create Render Node)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4918C294-FAAD-45B5-A896-92161177EEED)窗口。

#### 锁定属性(Lock Attribute)

锁定“权重”(Weight)值。Maya 会用灰色背景显示已锁定的属性。

若要解除锁定，请单击鼠标右键，然后选择“解除锁定属性”(Unlock Attribute)。
