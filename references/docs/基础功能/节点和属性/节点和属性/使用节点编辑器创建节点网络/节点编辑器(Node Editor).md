# 节点编辑器(Node Editor)

若要打开“节点编辑器”(Node Editor)，请选择“窗口 > 节点编辑器”(Windows > Node Editor)。

“节点编辑器”(Node Editor)提供依赖关系图的可编辑图解，显示节点及其属性之间的连接。允许您查看、修改和创建新的节点连接。“节点编辑器”(Node Editor)对于角色装备等任务有效，但在处理材质和着色网络时，建议使用 Hypershade 编辑器。

第一次打开“节点编辑器”(Node Editor)时，会在您的场景视图中绘制选定对象。

## 节点视图模式

在“节点编辑器”(Node Editor)中可通过以下五种方式查看节点：简单模式、已连接模式、完全模式、查看所有属性或查看自定义属性。

  简单模式显示一个输入和一个输出主端口，以圆形表示。![图：简单模式显示一个输入和一个输出主端口，以圆形表示。 图标也表示您处于简单模式。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-730AFFF2-DB01-483B-B844-3656C37CA20B.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" --> 图标也表示您处于简单模式。

  ![图：简单模式显示一个输入和一个输出主端口，以圆形表示。 图标也表示您处于简单模式。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-75CC0B48-4442-4AB3-AB33-FC84756BF5E1.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" -->

  已连接模式显示输入和输出主端口，以及任何已连接属性。这些属性具有自己的端口，均显示为小圆形。![图：已连接模式显示输入和输出主端口，以及任何已连接属性。这些属性具有自己的端口，均显示为小圆形。 图标也表示您处于已连接模式…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-3C0AFC2F-98DA-4BD4-B79A-F16E1B561B20.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" --> 图标也表示您处于已连接模式。

  ![图：已连接模式显示输入和输出主端口，以及任何已连接属性。这些属性具有自己的端口，均显示为小圆形。 图标也表示您处于已连接模式…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-2DA99678-22C7-4324-9B8D-59E73CD54FD5.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" -->

  完全模式显示输入和输出主端口，以及主要节点属性。给定节点的主属性集基于属性的特性，例如，它们是可设定关键帧还是为动态。![图：完全模式显示输入和输出主端口，以及主要节点属性。给定节点的主属性集基于属性的特性，例如，它们是可设定关键帧还是为动态。 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-C3D62C33-944A-4D5E-9DDE-E124E94AC45B.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" --> 图标也表示您处于完全模式。

  ![图：完全模式显示输入和输出主端口，以及主要节点属性。给定节点的主属性集基于属性的特性，例如，它们是可设定关键帧还是为动态。 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-1BD6318E-D3AA-4355-92CD-45BFC23056F6.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" -->

  您可以从节点标记菜单中选择“显示所有属性”(Show All Attributes)选项，将节点的完全模式暂时替换为所有属性的列表。所有属性的显示仅对该绘制实例有效。如果对节点重新制图，或者更改节点的视图模式，则必须重新选择此选项才可再次显示其所有属性。请参见[“节点编辑器”(Node Editor)标记菜单](节点编辑器%28Node%20Editor%29/“节点编辑器”%28Node%20Editor%29标记菜单.md)。对于没有关联自定义属性列表的节点，也可以使用热键 4 显示其所有属性。

  ![图：您可以从节点标记菜单中选择“显示所有属性”(Show All Attributes)选项，将节点的完全模式暂时替换为所有…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-F0E61944-179E-4929-A3ED-0288C80B94C8.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" -->

  **注**

  当显示所有属性时，节点将显示为完全模式

  图标。

  您也可以自定义针对每个节点显示的属性列表。要创建自定义属性列表，请在节点上单击鼠标右键，然后选择“编辑自定义属性列表”(Edit Custom Attribute List)。创建自定义属性列表后，单击 ![图：您也可以自定义针对每个节点显示的属性列表。要创建自定义属性列表，请在节点上单击鼠标右键，然后选择“编辑自定义属性列表”(…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-01F0B285-2776-4A14-9B4D-0BE4F560BA3C.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" --> 或热键 4，以在其自定义属性视图中显示选定节点。请参见[在“节点编辑器”(Node Editor)中自定义节点属性列表](自定义节点视图/在“节点编辑器”%28Node%20Editor%29中自定义节点属性列表.md)。

  此视图模式下的节点未显示有过滤器字段。若要显示过滤器字段，请单击 ![图：此视图模式下的节点未显示有过滤器字段。若要显示过滤器字段，请单击 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-45BB8F30-E07F-4A78-A5AC-50251902E359.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" -->。

  ![图：您也可以自定义针对每个节点显示的属性列表。要创建自定义属性列表，请在节点上单击鼠标右键，然后选择“编辑自定义属性列表”(…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-AB12E55D-54BA-448E-9010-5E7C6607459E.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" -->

  **注**

  如果已为节点保存对应的自定义属性视图，则按热键 4 将在其自定义视图中显示它，

  位于右上角。如果未为节点保存对应的自定义属性视图，则按热键 4 将在完全模式下显示它，

  位于右上角。

输入属性将显示在完整模式的节点左侧。而输出属性则显示在完整模式的节点右侧。若要展开节点的属性列表，请单击属性旁边的 ![图：输入属性将显示在完整模式的节点左侧。而输出属性则显示在完整模式的节点右侧。若要展开节点的属性列表，请单击属性旁边的 。如…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-6E361A72-D274-4D7B-87A8-EB9B0B0798B4.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" -->。如果属性可以作为输入或输出进行连接，则在节点的左侧和右侧都提供端口。可按住快捷键 Shift 并单击复合属性的 ![图：输入属性将显示在完整模式的节点左侧。而输出属性则显示在完整模式的节点右侧。若要展开节点的属性列表，请单击属性旁边的 。如…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-6E361A72-D274-4D7B-87A8-EB9B0B0798B4.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" -->（加号）图标展开其所有子属性层。或者，也可以按住此快捷键并单击复合属性的 ![图：输入属性将显示在完整模式的节点左侧。而输出属性则显示在完整模式的节点右侧。若要展开节点的属性列表，请单击属性旁边的 。如…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-580E4A04-C7D9-4AA3-A010-3017100B7491.png) <!-- baize:img-hook downloaded=false reason="正文 1471 字 ≥300，非承重" -->（减号）图标收拢其所有子属性层。

有关节点连接的详细信息，请参见[显示连接](显示连接.md)。

## 更改多个节点的视图模式

可以通过一步操作更改多个节点的视图模式，方法为：选择节点，然后在工具栏中通过菜单选项（“编辑 > 简单模式”(Edit > Simple Mode)、“已连接模式”(Connected Mode)、“完全模式”(Full Mode)、“自定义模式”(Custom Mode)）或使用 1、2、3、4 热键选择所需的模式图标。详细信息请参见[节点编辑器的“编辑”(Edit)菜单和工具栏](节点编辑器%28Node%20Editor%29/“节点编辑器”%28Node%20Editor%29菜单和工具栏.md#GUID-6AA14E01-4E9D-4DD4-9ECE-49646C9A917C__SECTION_FAB65FAA51014D3786128B299D06033A)。

**注**

在

节点编辑器

中无节点亮显（活动）时，如果单击工具栏中的图标，从

节点编辑器的“编辑”(Edit)

菜单中或者使用

“编辑”(Edit)

菜单快捷方式选择相同的选项，则所有的节点都受影响。

## 相关主题

- [连接节点](连接节点.md)

- [“节点编辑器”(Node Editor)首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-29B4D1FC-1861-4828-8236-6E6F1F24BFD3)

- [Hypergraph](../“Hypergraph”概述.md)

- [Hypershade 窗口](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-252707EC-4AAF-4D3F-9600-804F783652B7)
