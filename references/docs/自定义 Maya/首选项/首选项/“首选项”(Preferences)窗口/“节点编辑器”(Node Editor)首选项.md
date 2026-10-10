# “节点编辑器”(Node Editor)首选项

可以在[首选项(Preferences)窗口](../“首选项”%28Preferences%29窗口.md)的“节点编辑器”(Node Editor)类别中设置以下首选项。

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

可以自定义“节点编辑器”(Node Editor)的以下选项。在您下次创建“节点编辑器”(Node Editor)窗口时将应用这些选项。

## 显示(Display)

通过选择提供的任意选项，可以在“节点编辑器”(Node Editor)中自定义图表。

#### 栅格(Grid)

选择或取消选择此选项可启用和禁用栅格背景。

#### 栅格捕捉(Grid snapping)

启用该选项可将节点捕捉到栅格。

#### 形状(Shapes)

在选项中进行选择以自定义要显示的形状。

#### 变换(Transforms)

选择该选项以在图表中包含变换节点。

#### 扩展到形状(Extend to shapes)

选择该选项以包含选定变换的子形状节点。

#### 显示名称空间(Show Namespace)

禁用此选项可避免显示节点名称的名称空间。这允许您显示较短的节点名称，例如 ...:pConeShape1 而不是 Namespace1:pConeShape1。

#### 使用资产和已发布的属性(Use Assets and Published Attributes)

启用此选项后，当您绘制属于资产一部分的对象时，会对该资产而非节点本身进行绘制，并显示已发布的属性连接，而非原始属性连接。

#### 默认节点视图模式(Default node view mode)

- “简单模式”(Simple Mode)：将节点的视图模式设置为简单模式，以便仅显示输入和输出主端口。

- “已连接模式”(Connected Mode)：将节点的视图模式设置为已连接模式，以便显示输入和输出主端口，以及任何已连接属性。

- “完全模式”(Full Mode)：将节点的视图模式设置为完全模式，以便显示输入和输出主端口，以及主节点属性。给定节点的主属性集基于属性的特性，例如，它们是可设定关键帧还是为动态。

- “自定义模式”(Custom Mode)：将节点的视图模式设置为自定义模式，以便节点以自定义属性视图形式显示。您可以通过以下方法为每个节点创建自定义属性视图：在节点上单击鼠标右键，然后选择“编辑自定义属性列表”(Edit Custom Attribute List)。有关详细信息，请参见[自定义节点属性列表](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C1E02C84-8CCF-4B3D-B080-F4A379AD1FCB)。

  **注**

  如果您选择

  “自定义模式”(Custom Mode)

  作为

  “默认节点视图模式”(Default node view mode)

  ，则未保存自定义属性视图的任何节点以其完全模式显示。

也可以从“节点编辑器”(Node Editor)中自定义这些选项。

可以从“节点编辑器”(Node Editor)工具栏、“显示”(Display)菜单或工作区标记菜单中选择“所有形状”(All Shapes)、“除着色组成员以外的所有形状”(All Shapes Except Shading Group Members)和“无形状”(No Shapes)选项。详细信息请参见[节点编辑器菜单栏](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6AA14E01-4E9D-4DD4-9ECE-49646C9A917C#GUID-6AA14E01-4E9D-4DD4-9ECE-49646C9A917C__SECTION_B21F05464FFF461E909407B39BADF3DD)、[节点编辑器工具栏](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6AA14E01-4E9D-4DD4-9ECE-49646C9A917C#GUID-6AA14E01-4E9D-4DD4-9ECE-49646C9A917C__SECTION_CF38E057A67B470585723CE652DCCCDE)和[节点编辑器标记菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B99E6112-CECD-4F1A-8520-265C1407E904)。

可以从“显示”(Display)菜单或工作区标记菜单中选择“变换”(Transforms)和“扩展到形状”(Extend to shapes)选项。详细信息请参见[节点编辑器菜单栏](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6AA14E01-4E9D-4DD4-9ECE-49646C9A917C#GUID-6AA14E01-4E9D-4DD4-9ECE-49646C9A917C__SECTION_B21F05464FFF461E909407B39BADF3DD)和[节点编辑器标记菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B99E6112-CECD-4F1A-8520-265C1407E904)。

您可以从“显示”(Display)菜单中选择“使用资产和已发布的属性”(Use Assets and Published Attributes)选项。

使用以下方法之一，可以在“节点编辑器”(Node Editor)中以交互方式更改多个节点的视图模式（“简单模式”(Simple Mode)、“已连接模式”(Connected Mode)和“完全模式”(Full Mode)）：从“编辑”(Edit)菜单、通过 1、2 或 3 热键或从工具栏。详细信息请参见[更改多个节点的视图模式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-23277302-6665-465F-8579-9BC734228F69#GUID-23277302-6665-465F-8579-9BC734228F69__SECTION_58DF25EE026646BDA0D0B5CF3CD403D8)、[节点编辑器菜单栏](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6AA14E01-4E9D-4DD4-9ECE-49646C9A917C#GUID-6AA14E01-4E9D-4DD4-9ECE-49646C9A917C__SECTION_B21F05464FFF461E909407B39BADF3DD)和[节点编辑器工具栏](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6AA14E01-4E9D-4DD4-9ECE-49646C9A917C#GUID-6AA14E01-4E9D-4DD4-9ECE-49646C9A917C__SECTION_CF38E057A67B470585723CE652DCCCDE)。

## 刷新图表默认值

#### 同步节点编辑器/视口选择(Sync Node Editor/Viewport Selection)

启用此选项后，如果在“节点编辑器”(Node Editor)中亮显某节点，该同一节点同时在场景中处于选中状态，反之亦然。详细信息请参见[节点编辑器(Node Editor)中的选择](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-60127A5E-00C6-4D56-B2DE-113291208186)。

#### 创建时添加到图表(Add to Graph on Create)

启用此选项后，在场景中创建节点时，该节点同时将添加到“节点编辑器中”(Node Editor)。如果此选项处于禁用状态，只显示使用“节点编辑器”(Node Editor)（例如，使用 Tab 键创建或使用拖放创建；详细信息请参见[创建节点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6217CD2A-0CDB-41C4-AC47-BD5169BE070C)）创建的节点。

**注**

还可以从

“节点编辑器”(Node Editor)

中的

“选项”(Options)

菜单（仅

“创建时添加到图表中”(Add to Graph on Create)

）或从

“节点编辑器”(Node Editor)

工作区标记菜单中控制这些选项。详细信息请参见

节点编辑器标记菜单

。
