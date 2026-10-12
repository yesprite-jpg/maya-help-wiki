# 使用 componentMatch 节点创建顶点查找表

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 726 字 ≥300，非承重" -->

使用 [componentMatch 节点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E97DDDC2-CF1D-4199-9AE0-86687E946003.htm)自动创建提供给组件列表的查找表，这样您就不必创建自己的顶点表。componentMatch 节点使用算法来比较几何体，构建顶点之间的相关性，以及输出预配置的查找表。

如果您希望创建自己的查找表，请确保“变形选项”(Morph Options)中的“使用组件查找”(Use Component Lookup)选项处于禁用状态。

使用 componentMatch 节点创建顶点查找表

1. 从由驱动者对象和变形对象组成的变形几何体开始。

2. 在驱动者和变形几何体上设置组件标记。（请参见[为几何体指定组件标记](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-788B1C8B-7F45-4862-BC42-0A334DFECFD3.htm)。）

  **注**

  在驱动者和变形几何体之间，组件必须具有相同数量的组件元素，否则无法自动生成表。如果多边形数不匹配，则

  componentMatch 节点

  无法在形状之间切合实际地插值。

3. [应用变形变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-07A9B4B2-6DE3-4E26-BB2B-D1C0A27BCA5B.htm)，将驱动者对象的变形传递到要变形的对象。在[变形选项(Morph Options)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-DAC2AA0B-3E70-4F5C-A656-1219219092A1.htm)中，激活**“使用组件查找”(Use Component Lookup)**以生成 [componentMatch 节点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E97DDDC2-CF1D-4199-9AE0-86687E946003.htm)。

4. 在[节点编辑器(Node Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-23277302-6665-465F-8579-9BC734228F69)中，选择 **componentMatch** 节点以在“属性编辑器”(Attribute Editor)中打开**“组件匹配属性”(Component Match Attributes)**。

5. 在“属性编辑器”(Attribute Editor) **的“组件匹配属性”(Component Match Attributes)**中的**“标记表达式”(Tag Expression)**字段中输入组件标记名称。（此字段支持表达式，因此您可以输入部分标记名称，例如，输入“**_left*”以查找包含“left”的所有组件标记名称。）

6. 按 **Enter** 键以应用组件匹配。将基于驱动者对象修改目标几何体。
