# 面板菜单：“显示”(Show)

此“显示”(Show)菜单显示在场景视图之上，或者显示在具有多个场景视图的布局中每个视图面板之上。

使用此菜单中的菜单项可以显示或隐藏面板中的特定对象类型。

**注**

提示：

某些对象或组件具有热键，便于快速切换可见性状态，从而可节省导航到此菜单所用的时间。

以下对象为：

| 热键 | 切换可见性 |
|---|---|
| Alt + 1 | NURBS 曲线 |
| Alt + 2 | 多边形网格 |
| Alt + 4 | 图像平面 |
| Alt + 5 | 线框/着色 |

#### 隔离选择

可以仅显示场景中的某些对象或组件。每个面板都保留自己的“隔离选择”(Isolate Select)设置。

与[隐藏](../主菜单/“显示”%28Display%29菜单/“隐藏”%28Hide%29选项.md)命令不同，“隔离选择”(Isolate Select)支持隔离组件（多边形顶点、面和边、NURBS CV 或细分曲面网格面）和对象，并且只影响显示，而不影响渲染。

**注**

“隔离选择”(Isolate Select)

不处理细分曲面上的顶点或边。

#### 栅格(Grid)

允许用户在单个面板中关闭栅格。

## 隔离选择选项

#### 查看选定对象(View Selected)

激活或取消激活“隔离选择”(Isolate Select)。激活后，将在面板底部显示“隔离”字样，表示当前选择已隔离。

热键：**Ctrl** + 1

#### 自动加载新对象(Auto Load New Objects)、自动加载选定对象(Auto Load Selected Objects)

启用后，在添加新对象或更改选择时，系统将自动更新“隔离选择”(Isolate Select)面板。如果禁用，则必须使用“加载”(Load)、“添加”(Add)或“移除选定对象”(Remove Selected Objects)选项更新面板。

**注**

“自动加载新对象”(Auto Load New Objects)

默认情况下处于启用状态。

#### 加载选定对象(Load Selected Objects)、添加选定对象(Add Selected Objects)、移除选定对象(Remove Selected Objects)

如果“自动加载”(Auto Load)选项处于关闭状态，您可以使用这些选项控制“隔离选择”(Isolate Select)的显示。从场景中选择项目，然后根据需要进行加载、添加或移除。请注意，“加载选定对象”(Load Selected Objects)将使用当前选择替换显示，而“添加选定对象”(Add Selected Objects)会将当前选择添加到已显示的选择中。

#### 书签

用于为隔离的选择添加书签。若要创建书签，请选择“显示 > 隔离选择 > 书签 > 为当前对象建立书签”(Show > Isolate Select > Bookmarks > Bookmark Current Objects)。如果要为书签命名，请选择选项框；否则，系统将使用默认名称。

若要查看书签项，请选择“显示 > 隔离选择 > 书签 > BookmarkName”(Show > Isolate Select > Bookmarks > BookmarkName)。再次选择可禁用该选项，并返回上一个视图。可以同时查看多个书签。书签将与场景作为一个集共同保存。

## 播放预览显示(Playblast Display)

展开此菜单以隐藏来自任何[播放预览](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1C6EDC8D-DA67-490E-81F1-1205336DEBD9)的元素。

默认情况下处于**显示**状态。

## 选择亮显

启用或禁用所选元素的亮显。默认情况下此设置处于启用状态，即选择对象时使对象亮显。请查看以下示例，了解激活“选择亮显”(Selection Highlighting)时的效果，后跟禁用“选择亮显”(Selection Highlighting)时的效果。

**注**

如果要在鼠标移至顶点、边和面等组件上时使其亮显，请参见

“选择”(Selection)首选项

中的“选择前亮显”(Preselection Highlight)选项。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-A001EEAE-08E0-4D6B-934F-3EF85E162672.png) <!-- baize:img-hook downloaded=false reason="正文 1559 字 ≥300，非承重" -->

“选择亮显”(Selection Highlighting)菜单位于**“显示”(Show)** [面板菜单](../面板菜单.md)底部。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-C5F6B73E-95CF-43A0-8784-8B7F2BE318AE.png) <!-- baize:img-hook downloaded=false reason="正文 1559 字 ≥300，非承重" -->

## 相关主题

- [显示或隐藏对象](../../../查看场景/查看场景/显示或隐藏对象和组件/显示或隐藏对象.md)

- [显示、隐藏或更改栅格](../../../查看场景/查看场景/显示、隐藏或更改栅格.md)

- [在面板中显示对象或组件的隔离子集](../../../查看场景/查看场景/显示或隐藏对象和组件/隔离对象或组件的显示.md)
