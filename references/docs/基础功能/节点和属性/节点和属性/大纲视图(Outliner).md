# 大纲视图(Outliner)

打开大纲视图

- 在主菜单栏中：“窗口 > 大纲视图”(Windows > Outliner)

- 在面板中：“面板 > 面板 > 大纲视图”(Panels > Panel > Outliner)

- 在界面左侧，单击快速布局按钮下的 ![图：在界面左侧，单击快速布局按钮下的 图标。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-7D65477E-B5C6-4BEF-B23A-72E38E96C10B.png) <!-- baize:img-hook downloaded=false reason="正文 1360 字 ≥300，非承重" --> 图标。

关闭“大纲视图”(Outliner)

如果“大纲视图”(Outliner)已停靠，请单击面板并将其拖动到视口中，然后将其关闭。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-5D9A7CD0-9811-491F-BC32-418A7DCEE4DB.gif) <!-- baize:img-hook downloaded=false reason="正文 1360 字 ≥300，非承重" -->

“大纲视图”(Outliner)以大纲形式显示场景中所有对象的层次列表。可以展开和收拢层次中分支的显示；层次的较低级别在较高级别下缩进。它是 Maya 的两个主要场景管理编辑器之一（另一个是 [Hypergraph](“Hypergraph”概述.md)）。

“大纲视图”(Outliner)还会显示视图面板中通常隐藏的对象，如默认摄影机或没有几何体的节点（例如，着色器和材质）。可以使用相应“显示”(Display)和“显示”(Show)菜单中的项目，控制“大纲视图”(Outliner)中显示的节点。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-ACEDC159-E374-48BC-AB49-5885506A6BC3.png) <!-- baize:img-hook downloaded=false reason="正文 1360 字 ≥300，非承重" -->

您可将“大纲视图”(Outliner)用于这些任务。有关更多详细信息，另请参见[使用大纲视图](大纲视图%28Outliner%29/使用“大纲视图”%28Outliner%29.md)。

**注**

提示：

如果发现在进行选择或展开时

“大纲视图”(Outliner)

性能下降（特别是对于大型场景），请激活

“界面(Interface)”首选项

中的

“大纲视图”(Outliner)

选项。

| 大纲视图中的元素 | 允许执行的操作 |
|---|---|
| 1 - 显示(Display)和显示(Show)菜单 | 过滤大纲视图中显示的内容。请参见[大纲视图(Outliner)菜单](大纲视图%28Outliner%29/“大纲视图”%28Outliner%29菜单.md)。 |
| 2 - 渲染设置过滤器 | 按所在的渲染层过滤场景中的对象。请参见[在大纲视图中过滤并仅显示渲染设置成员](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1A77E0A9-D910-4170-95B5-8A858A7F0C50)。选择“显示 > 渲染设置过滤器”(Display > Render Setup Filter)，以显示此过滤器。 也可在对象的节点上单击鼠标右键以打开“渲染设置”(Render Setup)菜单，然后选择用于[标识对象所属的集合](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D6EB87CA-F03B-4952-B6FF-E8E2A32961C6)命令。 |
| 3 - 搜索(Search)字段 | 搜索场景中的任何节点。请参见[搜索节点](大纲视图%28Outliner%29/搜索和过滤节点.md)。 |
| 4 - 组和层次 | 创建和更改节点层次。通过使用鼠标中键并拖动父节点下的子节点，可以创建层次。使用鼠标中键在组或层次内拖动节点以更改其顺序。 |
| 5 - 材质 | 显示并使用材质和着色器。请参见[大纲视图(Outliner)上下文菜单](大纲视图%28Outliner%29/“大纲视图”%28Outliner%29上下文菜单.md)中的材质节点命令。 |
| 6 - 隐藏对象 | 选择视图面板中隐藏的对象。按 H 键以切换其可见性。 |
| 7 - 集 | 编辑集成员身份，请参见[创建和编辑集](../../场景管理/场景管理/组织对象/集和划分/创建和编辑集.md)。 |
| 8 - 资产 | 使用[资产](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1826F831-E3D1-4045-B6B9-F7D34360C331)。在“资产”(Asset)节点上单击鼠标右键，可打开“资产”(Asset)菜单。 |
| 9 - 被引用文件 | 使用[文件引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-238914C9-4129-454C-99D7-B8C57AF423DB)。在引用节点或大纲视图的空白区域上单击鼠标右键，可打开“引用”(Reference)菜单。请参见[大纲视图(Outliner)上下文菜单](大纲视图%28Outliner%29/“大纲视图”%28Outliner%29上下文菜单.md)。 还可以在要导出为被引用文件的节点上单击鼠标右键，然后设置其选项。请参见[将当前选择导出为引用选项(Export Selection as Reference Options)](大纲视图%28Outliner%29/将当前选择导出为引用选项%28Export%20Selection%20As%20Reference%20Options%29.md)。 |
| 场景集合 | 使用[场景集合](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E9D00A25-324A-445C-AE04-590AD29C89BA)。在集合节点上单击鼠标右键，可打开“场景集合”(Scene Assembly)菜单。请参见[大纲视图(Outliner)上下文菜单](大纲视图%28Outliner%29/“大纲视图”%28Outliner%29上下文菜单.md)。 |

**注**

若要在大纲视图中平移，请按 Alt 键并单击鼠标中键（对于 Mac，请按 Opt 键并单击鼠标中键）。若要快速平移，请按 Ctrl+Alt 并单击鼠标中键（对于 Mac，请按 Ctrl+Opt 并单击鼠标中键）。

## 相关主题

- [场景的两个视图：层次和依存关系](场景的两个视图：层次和依存关系.md)

- [查看和编辑节点层次](编辑节点层次.md)
