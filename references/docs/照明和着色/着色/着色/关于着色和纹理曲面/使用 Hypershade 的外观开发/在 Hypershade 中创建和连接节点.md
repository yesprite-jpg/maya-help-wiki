# 在 Hypershade 中创建和连接节点

在为外观开发而优化的自定义视图中创建节点，然后在节点编辑界面中连接它们。

## 创建节点

可以通过以下三种方式之一在 Hypershade 工作区中创建节点。工作区是位于 Hypershade 底部的面板，可以在其中构建着色图表。

- **按 Tab 键**，然后输入节点的类型。

- **单击**** “创建”(Create) **选项卡中的节点。

  如果“创建时添加到图表中”(Add to Graph on Create)已启用（默认），则可以执行此操作。右键单击工作区时，可从标记菜单提供此选项。

  如果在“创建时添加到图表中”(Add to Graph on Create)已禁用时单击“创建”(Create)选项卡中的节点，仍会创建节点，但是不会将它添加到工作区。

- **使用鼠标中键**将节点从** “创建”(Create) **选项卡拖动到 Hypershade 工作区中。

  不管“创建时添加到图表中”(Add to Graph on Create)是否已启用，都可以使用此方法。

首次创建节点时，将显示其最常用的属性（节点编辑器中的热键 4 模式）。可以使用 1、2、3、4 热键在视图模式之间切换，像在节点编辑器中那样。有关视图模式的详细信息，请参见[在节点编辑器和 Hypershade 中更改视图模式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8BB2DBCA-FB8B-4F7A-A4C3-1BACE18E5879)。显示的属性列表由与每个着色节点关联的节点编辑器模板确定。请参见[节点编辑器模板](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9C223EB6-5926-44A3-8F0A-B0AF4172D3AA)。

## 连接节点

在 Hypershade 工作区中连接节点，像在节点编辑器中那样。例如，您可以单击源端口和目标端口以连接二者；或者，您可以使用鼠标中键或左键拖动在输出和输入属性之间创建连接线。默认情况下公开常用的端口。

或者，可以使用鼠标中键将节点拖动到另一个节点上，以显示可能连接的列表。**按住 Ctrl 键并使用鼠标中键**将节点拖动到另一个节点上，以创建**默认连接**。

## 移除连接

若要移除多个连接线，请按住 Shift 和 Alt 键并拖过要删除的连接。

若要移除单个连接线，请选择它，然后按 Backspace 或 Delete 键 (Mac OS X)。

## 创建多个图表

创建多个选项卡，并在每个选项卡中绘制不同的网络。

单击最右侧选项卡旁边的 + 号以创建新选项卡。右键单击任何选项卡以显示其“关闭选项卡”(Close Tab)、“复制选项卡”(Duplicate Tab)和“重命名选项卡”(Rename Tab)菜单选项。使用鼠标左键或中键拖动可对选项卡重新排序。

## 在 Hypershade 工作区中编辑着色器图表

使用 ![图：使用 、 和 工具栏图标，可以绘制任何渲染节点的上游连接、下游连接或上游和下游连接。详细信息请参见显示节点连接。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-5144BEC8-04D7-4C4C-B4E3-A482BDC19E58.png) <!-- baize:img-hook downloaded=false reason="正文 1115 字 ≥300，非承重" -->、![图：使用 、 和 工具栏图标，可以绘制任何渲染节点的上游连接、下游连接或上游和下游连接。详细信息请参见显示节点连接。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-9292A041-82B0-4D36-99D7-278855A7552C.png) <!-- baize:img-hook downloaded=false reason="正文 1115 字 ≥300，非承重" --> 和 ![图：使用 、 和 工具栏图标，可以绘制任何渲染节点的上游连接、下游连接或上游和下游连接。详细信息请参见显示节点连接。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-2DAD0BAA-9888-4075-B3DB-3C45B5CF4481.png) <!-- baize:img-hook downloaded=false reason="正文 1115 字 ≥300，非承重" --> 工具栏图标，可以绘制任何渲染节点的上游连接、下游连接或上游和下游连接。详细信息请参见[显示节点连接](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-721BE1F1-1634-4107-9179-3439D5E4CE5E.htm)。

通过 Hypershade 工作区工具栏，还可以使用诸如以下的功能来编辑图表：将选定节点添加到图表、从图表中移除选定节点、切换节点的样例大小以及显示节点的过滤器字段。详细信息请参见 [Hypershade 工作区工具栏](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-398B029E-4DD0-4AA6-8C84-DC21CBEA50C3.htm)。
