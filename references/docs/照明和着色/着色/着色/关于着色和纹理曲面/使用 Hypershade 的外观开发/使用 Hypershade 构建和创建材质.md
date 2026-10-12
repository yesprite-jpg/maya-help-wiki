# 使用 Hypershade 构建和创建材质

Hypershade 由多个面板组成，在即时预览结果的同时可以使用这些面板构建和编辑材质。

- 单击[状态行（工具栏）](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-86E5CEDA-4100-40AE-8F95-346206CF8456)上的 ![图：单击状态行（工具栏）上的 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-1321E0F8-88D9-4120-813A-CCA4BCB1EDEA.png) <!-- baize:img-hook downloaded=false reason="正文 1481 字 ≥300，非承重" -->。

- 选择“窗口 > 渲染编辑器 > Hypershade”(Windows > Rendering Editors > Hypershade)。

将在工作区中自动创建“节点编辑器”(Node Editor)选项卡。在此处可以创建着色网络。

默认情况下 Hypershade 包括以下面板，每个面板都有助于简化外观开发工作流，并有助于更快地获得您的结果：

- ** “浏览器”(Browser) **：此面板列出材质、纹理和灯光，按选项卡排序。

- ** “材质查看器”(Material Viewer) **：此面板渲染着色器或已单放的材质。在硬件渲染器和 Arnold for Maya 之间选择，然后从几种几何体类型中选择。调整着色网络，并实时查看渲染更新。

  使用 Arnold for Maya 进行渲染时，通过从各种预设环境中选择或者添加您自己的环境，可以将基于图像的照明添加到渲染。

  可以在材质查看器中渲染凹凸贴图和平面纹理，并且可以将颜色管理应用于渲染，像在“渲染视图”(Render View)中那样

- ** “创建”(Create) **：单击“创建”(Create)选项卡中的节点可创建节点并将其添加到着色器图表。

  或者，也可以单击 Tab 键，然后输入节点的类型，或者将节点从“创建”(Create)选项卡拖放到工作区。

  **工作区**：使用此面板可以创建节点并构建着色器网络，像在节点编辑器中那样。也可以在同一视图模式下显示各种节点：简单、已连接、完全和自定义。默认情况下，Hypershade 中的节点在自定义模式（仅显示常用的属性）下显示。

  请参见[在 Hypershade 中创建和连接节点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-F90898A6-55E7-47EA-8542-8A9FD9CBC561.htm)。

  从标记菜单中选择“显示 > 对象”(Show > Objects)，以确定在工作区中显示的节点。默认情况下，显示摄影机、着色组和着色节点，但是可以自定义此组过滤器。

  可以创建多个选项卡，每个选项卡都显示有自身的节点集。这样，您就可以同时使用多个着色器图表并对它们进行编辑，而无需重新绘制。

  若要创建其他选项卡，请单击最右侧选项卡旁边的 + 号。可以创建新的选项卡，删除它们，重命名或复制它们，以及在工作区中对它们重新排序。右键单击任意选项卡可显示其选项卡菜单选项。在关闭 Hypershade 时和保存文件时，选项卡保持不变。

- ** “特性编辑器”(Property Editor) **：在 Lookdev 模板视图中查看着色节点属性。此模板已针对外观开发工作流进行优化。它具有更简单的布局，仅列出最常用的属性，使您可以更轻松地查找和调整着色节点属性。单击 ![图：“特性编辑器”(Property Editor) ：在 Lookdev 模板视图中查看着色节点属性。此模板已针对外观开发…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-4A7A53DB-FDC6-4913-800E-FF48465A4C87.png) <!-- baize:img-hook downloaded=false reason="正文 1481 字 ≥300，非承重" --> 以切换到经典属性编辑器视图。

- “存储箱”(Bins)：排序存储箱用作着色节点（材质、纹理等）的容器，以帮助您组织和跟踪场景中的着色节点。

包括其他面板（如视口、“渲染视图”(Render View)或“大纲视图”(Outliner)）作为您的面板之一，方法是从“窗口”(Window)菜单中选择并将它停靠到 Hypershade 中。通过取消停靠和重新排列面板，可以进一步自定义 Hypershade 的布局。请参见[在 Hypershade 中自定义布局](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-FD108D16-572C-44BA-99C7-52307CDBB3AA.htm)。这样就可以在一个编辑器内涵盖整个外观开发工作流。

**注**

Hypershade

专门设计用于创建着色网络。对于工作流（如装备），

节点编辑器

是首选编辑器。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-C59B74F1-2AFF-4EB1-8745-3D742EE005F7.png) <!-- baize:img-hook downloaded=false reason="正文 1481 字 ≥300，非承重" -->

## 相关主题

- [使用 Hypershade 的外观开发](../使用%20Hypershade%20的外观开发.md)

- [在材质查看器中实时渲染着色网络](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-FAB13FA2-7068-4169-8D27-016B13E5C930.htm)

- [在材质查看器中通过预设或自定义环境添加基于图像的照明](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-35DC6688-1D1B-44BA-8DFD-9BB5C764A835.htm)

- [创建和连接节点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-F90898A6-55E7-47EA-8542-8A9FD9CBC561.htm)

- [关于单放](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-3E38FD79-D521-4C0E-AC53-A290770C492D.htm)

- [在 Hypershade 中单放节点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-5B870D6B-7D1D-4E84-A94B-9EEAAB1D97B6.htm)

- [在特性编辑器中查看属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-51DFC2E3-7D78-41C7-BE9A-489C181D8DF5.htm)

- [为自定义节点创建 lookdev 视图模板](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-7CB490A0-75E3-4C6B-9E60-5F744E96457E.htm)

- [暂停材质和纹理的样例生成](暂停材质和纹理的样例生成以提高%20Hypershade%20性能.md)
