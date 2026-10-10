# “大纲视图”(Outliner)上下文菜单

在“大纲视图”(Outliner)的空白区域中或在任何节点上单击鼠标右键时，可以访问您在“显示”(Display)和“显示”(Show)菜单（请参见[“大纲视图”(Outliner)菜单](“大纲视图”%28Outliner%29菜单.md)）中找到的相同命令，以及这些菜单中所没有的其他命令。

在特定节点类型（例如，“材质”(Material)或“集”(Set)节点）上单击鼠标右键时，可以访问仅适用于这些节点类型的命令。

## 显示选定项(Reveal Selected)

在视图中查找选定对象的节点。还可以在大纲视图中按 F 键。大纲视图展开层次以显示当前选定的节点。

## 在大纲视图中隐藏(Hide in Outliner)

选择“隐藏”(Hide)，在大纲视图中隐藏选定节点。

由于隐藏节点在大纲视图中看不到，因此必须先选择此菜单中的忽略“在大纲视图中隐藏”(Ignore 'Hidden In Outliner')暂时显示它，或者从视图面板或其他编辑器中选择它，然后才能将其取消隐藏。再次显示之后，选择该节点，然后选择“取消隐藏”(Unhide)更改其隐藏状态。

## 引用(Reference)菜单

若要访问“引用”(Reference)菜单，请在空白区域或“大纲视图”(Outliner)中的引用节点上单击鼠标右键。

#### 创建引用(Create Reference) > ![图：创建引用(Create Reference)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5191 字 ≥300，非承重" -->

请参见[引用选项(Reference Options)](../../../基本参考/基本参考/主菜单/“文件”%28File%29菜单/引用选项%28Reference%20Options%29.md)和[创建文件引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-00DA055B-3559-4E60-979F-DA862BBCA9C8)。

#### 导出选定对象作为参考(Export Selected As Reference) > ![图：导出选定对象作为参考(Export Selected As Reference)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5191 字 ≥300，非承重" -->

将选定对象导出为被引用文件。将对象导出为文件引用时，Maya 会在指定的位置创建一个新场景文件，并在打开的父场景中引用该文件。请参见[将当前选择导出为引用选项](将当前选择导出为引用选项%28Export%20Selection%20As%20Reference%20Options%29.md)和[导出文件引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-097A9F43-8A36-456E-B888-F635B588C546)。

#### 卸载(Unload) / 加载(Load) / 重新加载(Reload)

加载或卸载选定的引用。如果已加载当前引用，重新加载会更新已加载的引用。正在同时编辑引用文件时，这是很有用的。请参见[卸载和重新加载文件引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-08ADB591-B38F-421D-89CF-8B18FDDF3A09)。

#### 选择引用成员(Select Reference Members)

选择选定引用节点包含的对象。“大纲视图”(Outliner)和场景视图中会选择引用的成员，使您可以查看父场景的引用组织。

#### 复制(Duplicate)

复制与选定引用相关联的文件。请参见[复制文件引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C0A5E29D-3521-4668-A861-DD034E1404C4)。

#### 导入(Import)

将选定引用的对象直接导入到当前场景中。请参见[导入文件引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-550E9963-94EA-4997-AFFF-A828EDC5F073)。

#### 删除(Remove)

从场景文件移除选定引用和关联的引用节点。这是移除引用及其关联的节点的首选方法。

#### 替换(Replace)

打开文件浏览器以使用所选引用替换当前引用。组节点和/或定位器保持不变。

#### 最新替换的文件(Recently Replaced Files)

列出最新替换的引用文件。

#### 保存编辑(Save Edits)

将在父场景内为某个选定文件引用进行的编辑保存到磁盘上相应的被引用文件。编辑得到传递，这样它们就不再位于父场景内。请参见[引用编辑](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-021D6556-CC80-4CE3-8E07-CA80ED72B804)。

#### 导出到脱机文件(Export to Offline File) > ![图：导出到脱机文件(Export to Offline File)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5191 字 ≥300，非承重" -->

使用这些选项可设置选择“文件 > 导出到脱机文件”(File > Export to Offline File)时会发生什么变化。请参见[导出到脱机文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E2D1A00B-A90C-443D-AFC5-B819A037C5B6)。

另请参见[导出到脱机文件选项](../../../基本参考/基本参考/主菜单/“文件”%28File%29菜单/导出到脱机文件选项%28Export%20to%20Offline%20File%20Options%29.md)。

#### 指定脱机文件(Assign Offline File) > ![图：指定脱机文件(Assign Offline File)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5191 字 ≥300，非承重" -->

从所选择的文件引用编辑，并将它们应用于在“大纲视图”(Outliner)或“引用编辑器”(Reference Editor)中选定的引用节点。Maya 通过将编辑文件中的每个 nodename.attribute 与其应用的目标文件匹配来应用编辑。

例如，可以导出场景 sphere.ma 中 pSphere1.translateX 的引用编辑。该编辑会在引用文件中保存为 <main>:sphere_pSphere1.translateX。然后可以将该编辑应用于场景 ball.ma，以便编辑 ball:pSphere1.translateX。

请参见[指定脱机文件选项(Assign Offline File)](../../../基本参考/基本参考/主菜单/“文件”%28File%29菜单/指定脱机文件选项%28Assign%20Offline%20File%20Options%29.md)和[指定脱机文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8D2F8B56-8546-42A7-B31D-A088D1EC2698)

#### 列出编辑(List Edits)

显示选定引用上的当前编辑列表。可以通过单击“刷新编辑列表”(Refresh Edits List)按钮手动刷新该窗口，或者通过选择特定编辑再单击“移除选定编辑”(Remove Selected Edits)移除这些编辑。请参见[列出、复制或移除引用编辑](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9CE1E15D-C0F4-4AA1-B692-B4F4B449A81A)。

#### 锁定引用/取消锁定引用(Lock Reference/Unlock Reference)

为选定的文件引用锁定或取消锁定所有节点和属性。一个锁定图标显示在引用编辑器内列出的文件引用的旁边，指示锁定状态。请参见[锁定文件引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3B6A0258-EF7D-4E25-9744-C27BDE843C1A)。

## 场景集合(Scene Assembly)菜单

### 场景集合 > 创建集合引用(Scene Assembly > Create Assembly Reference)

创建 [assemblyReference](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7ED15645-3C4E-470B-BFE4-9B606601BF0E) 节点。

### 场景集合 > 创建集合定义(Scene Assembly > Create Assembly Definition)

创建 [assemblyDefinition](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9250CB75-70F0-4F3B-A0FC-B40B081BC531) 节点。

#### 场景集合 > 创建集合定义(Scene Assembly > Create Assembly Definition) > ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5191 字 ≥300，非承重" -->

集合表示(Assembly Representations)

#### 添加定位器表示(Add Locator representation)

将“定位器表示”(Locator representation)添加到新的集合定义。默认情况下，“添加定位器表示”(Add Locator representation)处于启用状态。

要访问以下“场景集合”(Scene Assembly)菜单项，请选择 assemblyReference 或 assemblyDefinition 节点，然后在“大纲视图”(Outliner)或场景视图中单击鼠标右键。从显示的菜单中选择“场景集合”(Scene Assembly)。

#### 定位器(Locator)

从任何其他活动表示切换到“定位器表示”(Locator representation)。

如果 assemblyDefinition 节点包含要在其间进行切换的其他表示（如“缓存表示”(Cache representation)或“场景表示”(Scene representation)）选项，则这些表示将在菜单中显示。

#### 卸载活动表示(Unload Active Representation)

从场景视图中移除当前显示为表示的对象，并将“活动表示”(Active Representation)设置为“无”(None)。请参见[卸载活动的集合表示](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-323EFF8E-DF95-4A03-8984-5FFBBA9FE678)。

#### 列出编辑(List Edits)

将编辑列表显示到嵌套集合引用节点的表示上。请参见[“列出集合编辑”(List Assembly Edits)窗口](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-19AAFD06-3917-4FAE-A179-FFE96A13E592)。

场景集合编辑由集合引用节点管理。请参见[场景集合编辑](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7A05C838-CDF5-4731-8E34-782EE773DE8E)。

### “添加缓存表示”(Add Cache representation)、“添加定位器表示”(Add Locator representation)、“添加场景表示”(Add Scene representation)

将指定的表示类型添加到选定 assemblyDefinition 节点。请参见[添加集合表示](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E7A90079-A36C-4B88-A296-30D7D173BCDF)。

#### “添加缓存表示”(Add Cache representation) > ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5191 字 ≥300，非承重" -->/“添加定位器表示”(Add Locator representation) > ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5191 字 ≥300，非承重" -->

加载选项(Load Options)

#### 加载表示(Load representation)

加载新表示时，使其处于活动状态。

## 集

在“大纲视图”(Outliner)中的对象上单击鼠标右键可访问这些命令。

选择“创建”(Create)选项可创建集、划分或快速选择集。[集和快速选择集](../../../场景管理/场景管理/组织对象/集和划分.md)是对象的松散分组，用于组织场景。[划分是集的分组](../../../场景管理/场景管理/组织对象/集和划分.md)，用于确保集不会共享其成员。另请参见[创建和编辑集](../../../场景管理/场景管理/组织对象/集和划分/创建和编辑集.md)以及[创建划分以避免集成员身份重叠](../../../场景管理/场景管理/组织对象/集和划分/创建划分以避免集成员身份重叠.md)。

选择“将当前选择添加到集”(Add Selection to Set)和“从集中移除当前选择”(Remove Selection From Set)选项可在“大纲视图”(Outliner)中编辑集成员身份。

## 资产(Asset)菜单

若要访问“资产”(Asset)菜单，请在“大纲视图”(Outliner)中的资产节点上单击鼠标右键。

“选择资产内容”(Select Asset Contents)用于选择此资产节点内包含的所有元素。它们将在大纲视图和视图面板中亮显。

有关详细信息，请参见[资产](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1826F831-E3D1-4045-B6B9-F7D34360C331)。

## 仅显示 DAG 对象(Show DAG Objects Only)

仅显示可变换节点。有关 DAG 节点的描述，请参见 [DAG 层次](../DAG%20层次.md)。

## “显示”(Display) 和“显示”(Show) 菜单

这些命令与主“显示”(Display)和“显示”(Show)菜单中的命令相同。请参见[“大纲视图”(Outliner)菜单](“大纲视图”%28Outliner%29菜单.md)。

## 渲染设置(Render Setup)菜单

使用渲染层时，可以使用“大纲视图”(Outliner)帮助您查找对象所属的渲染层集合。

在“大纲视图”(Outliner)中，在对象的节点上单击鼠标右键可访问以下“渲染设置”(Render Setup)命令：

- “在所有渲染层中查找”(Find in All Render Layers)和“在选定渲染层中查找”(Find In Selected Render Layers)命令可以帮助您查找此对象所属的渲染层集合。

- “在渲染层中查找”(Find in Render Layer)菜单展开后，将显示场景中的所有渲染层。

通常，有关渲染设置的详细信息，请参见[在 Maya 中设置渲染](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-646154F9-E4D2-4A3E-A0D9-B2F062960A4E)；有关使用这些命令的信息，请参见[标识对象所属的集合](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D6EB87CA-F03B-4952-B6FF-E8E2A32961C6)。

## 时间编辑器节点命令(Time Editor node commands)

在大纲视图中，在 timeEditor 节点中的动画源上单击鼠标右键，即可访问以下命令：

- “从名称空间重映射和创建片段”(Remap and Create Clip from Namespace)用于列出场景中的所有名称空间，这样可以将选定动画重映射到其中任一名称空间。请参见[按名称空间重映射动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-FB4A498B-05CB-4F20-9ACC-C5DCFEDFC1E3)。

## 集节点命令(Set node commands)

在大纲视图中的集或集成员节点上单击鼠标右键，可访问以下命令：

- “选择集成员”(Select Set Members)用于选择选定集的成员。它们将在大纲视图和视图面板中亮显。

- “从当前集中移除”(Remove from Current Set)用于从当前集中删除此集成员。这也可以是嵌套在另一个集内的集节点。

- “显示集成员”(Show Set Members)用于切换集成员在大纲视图中的显示。如果禁用该选项，则仅显示集节点。

有关详细信息，请参见[创建和编辑集](../../../场景管理/场景管理/组织对象/集和划分/创建和编辑集.md)。

## 材质节点命令(Material node commands)

请确保选择“显示”(Display) > “指定的材质”(Assigned Materials)，以便在大纲视图中查看对象的材质节点。如果对象的多种材质已指定给对象上的面，则这些节点将在父“材质”(Materials)节点下显示。

在大纲视图中的材质节点上单击鼠标右键，可访问以下命令：

- “为当前选择指定材质”(Assign Material to Selection)用于将此材质应用于选定对象或多边形面。

  有关详细信息，请参见[为曲面指定材质](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D41AF807-F7CB-447E-BACC-7F0867C14E8D)。

- “选择具有材质的对象”(Select Objects with Material)用于选择已应用此材质的所有对象。它们将在大纲视图和视图面板中亮显。

- “框显具有材质的对象”(Frame Objects with Material)用于在视图面板中框显具有此材质的对象。这包括多边形面已应用此材质的对象。

- “在 Hypershade 中打开”(Open in Hypershade)用于打开 [Hypershade 窗口](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-252707EC-4AAF-4D3F-9600-804F783652B7)，其中此材质已选中并显示在材质球上。

- “绘制指定着色器”(Paint Assign Shader)用于激活[绘制选择工具(Paint Selection Tool)](../../../界面概述/界面概述/工具箱%28Tool%20Box%29/绘制选择工具%28Paint%20Selection%20Tool%29.md)，使您能够在选定对象或其多边形面上绘制此材质。

- “重命名”(Rename)用于输入此材质的新名称。

  **注**

  您无法在大纲视图中重命名

  “材质”(Materials)

  节点（文件夹）。

## UFE 命令

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 5191 字 ≥300，非承重" -->

在“大纲视图”(Outliner)中的 USD 基本体上单击鼠标右键，可访问以下命令：

- 变量(Variants)：列出可用于选定基本体的变量集和变量，以便切换变量。

  **注**

  提示：

  在选择变量时按住 Ctrl 键，可使变量集和变量子菜单保持打开状态。

- 使不可见(Make Invisible)：切换选定基本体的可见性。隐藏基本体后，此选项将重命名为“使可见”(Make Visible)。如果基本体设为不可见，则其子孙对象也将设为不可见。基本体设为不可见后在大纲视图中将灰显，但其子孙对象不会灰显。

  **注**

  还可以在

  “属性编辑器”(Attribute Editor)

  中查看和切换基本体的可见性。

## 相关主题

- [文件引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-238914C9-4129-454C-99D7-B8C57AF423DB)

- [场景集合(Scene Assembly)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E9D00A25-324A-445C-AE04-590AD29C89BA)

- [资产](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1826F831-E3D1-4045-B6B9-F7D34360C331)

- [在 Maya 中设置渲染](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-646154F9-E4D2-4A3E-A0D9-B2F062960A4E)

- [动画层编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-46091038-7F23-467C-8FEC-844A26C11EDA)

- [创建和编辑集](../../../场景管理/场景管理/组织对象/集和划分/创建和编辑集.md)

- [将材质指定给曲面](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D41AF807-F7CB-447E-BACC-7F0867C14E8D)
