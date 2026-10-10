# 面板菜单：“视图”(View)

此“视图”(View)菜单显示在场景视图之上，或者显示在具有多个场景视图的布局中每个视图面板之上。

#### 选择摄影机(Select Camera)

选择视图对应的摄影机。“通道盒”(Channel Box)和“属性编辑器”(Attribute Editor)中将显示该摄影机的属性。

**注**

提示：

如果要编辑观察和与摄影机关联的节点上方的摄影机，则选择摄影机非常有用。

#### 锁定摄影机(Lock Camera)

锁定当前选定的摄影机，避免意外更改摄影机位置并进而更改动画。锁定摄影机后，不能调整其变换信息。请参见[锁定当前摄影机](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A1F37692-BBB0-496A-AA79-48FB86BC082A)。

可以通过“热键编辑器”(Hotkey Editor)将热键指定给菜单项。选择“窗口 > 设置/首选项 > 热键编辑器”(Windows > Settings/Preferences > Hotkey Editor)以打开“热键编辑器”(Hotkey Editor)，然后从“为以下项编辑热键”(Edit Hotkeys For)下拉列表中选择“其他项目”(Other items)，并展开“视口菜单”(Viewport Menus)类别。

#### 从视图创建摄影机(Create Camera From View)

使用当前摄影机设置创建新摄影机。新摄影机将自动变为活动状态。

#### 在摄影机之间循环切换(Cycle Through Cameras)

在场景中的自定义摄影机之间循环切换。如果不存在自定义摄影机，则在场景中的标准摄影机之间循环切换。

#### 撤消视图更改(Undo View Change)

取消最近的视口更改，然后移回视图历史。

#### 重做视图更改(Redo View Change)

取消先前的“撤消视图更改”(Undo View Change)命令，前进至之后的视图历史状态。

#### 默认视图(Default View)

取消之前的视口更改并还原回默认视图。

#### 沿轴查看(View Along Axis)

可以移动摄影机沿不同的轴（例如，-X 或 Y）来查看场景。请从此菜单中选择所需的轴。视口底部的摄影机平视显示仪反射您查看场景所使用的轴（例如，透视 -Z 与透视 Z）。

可以通过“热键编辑器”(Hotkey Editor)将热键指定给这些菜单项。选择“窗口 > 设置/首选项 > 热键编辑器”(Windows > Settings/Preferences > Hotkey Editor)以打开“热键编辑器”(Hotkey Editor)，然后从“为以下项编辑热键”(Edit Hotkeys For)下拉列表中选择“其他项目”(Other items)，并展开“视口菜单”(Viewport Menus)类别。

#### 注视当前选择(Look at Selection)

选择此选项以便摄影机移动时在摄影机视图的中心显示选定的对象。但是，与“框显全部”(Frame All)和“框显当前选择”(Frame Selection)不同，摄影机不缩放或推拉；它仅水平和垂直平移以便选定的对象显示在场景视图的中心。

可以通过“热键编辑器”(Hotkey Editor)将热键指定给菜单项。选择“窗口 > 设置/首选项 > 热键编辑器”(Windows > Settings/Preferences > Hotkey Editor)以打开“热键编辑器”(Hotkey Editor)，然后从“为以下项编辑热键”(Edit Hotkeys For)下拉列表中选择“其他项目”(Other items)，并展开“视口菜单”(Viewport Menus)类别。

#### 当前选择的中心视图(Center View of Selection)

选择此选项后，可在不放大显示的情况下将摄影机移动到选定对象的中心。

可以通过“热键编辑器”(Hotkey Editor)将热键指定给菜单项。选择“窗口 > 设置/首选项 > 热键编辑器”(Windows > Settings/Preferences > Hotkey Editor)以打开“热键编辑器”(Hotkey Editor)，然后从“为以下项编辑热键”(Edit Hotkeys For)下拉列表中选择“其他项目”(Other items)，并展开“视口菜单”(Viewport Menus)类别。

#### 框显全部(Frame All)

选择此选项或按 A 键，可查看视图并使用场景中的所有对象填充视图。还可以从主菜单中选择“显示 > 在所有视图中框显所有内容”(Display > Frame All in All Views) 或者按 Shift+A，以便在所有视图中框显所有对象。

#### 框显当前选择(Frame Selection)

选择此选项或按 F 键，可查看视图并使用场景中的选定对象填充视图。

如果选择父对象、但不选择其子对象，则仅框显父对象。如果未选择对象，则此选项的功能相与“框显全部”(Frame All)相同。此外，您还可以从主菜单中选择“显示 > 在所有视图中框显当前选择”(Display > Frame Selection in All Views)，或者按 Shift+F。

#### 框显当前选择(包含子对象) (Frame Selection with Children)

选择此选项或按 Ctrl+F，可查看视图并使用场景中的选定对象填充视图。如果选择父对象，则会同时框显父对象和子对象。此外，您还可以从主菜单中选择“显示 > 在所有视图中框显当前选择(包含子对象)”(Display > Frame Selection with Children in All Views)，或者按 Ctrl+Shift+F。

#### 将摄影机与多边形对齐(Align Camera To Polygon)

摄影机的视图位置垂直对齐于选定多边形对象的法线方向。

#### 预定义书签(Predefined Bookmarks)

在 Maya 中预定义的摄影机视图之间切换，例如“透视”(Perspective)、“前”(Front)、“顶”(Top)等。

#### 书签

创建书签以保存当前的摄影机视图。

选择“书签 > 编辑书签”(Bookmarks > Edit Bookmarks)打开书签编辑器，可以在其中创建、编辑和删除当前书签。您创建的书签通过此菜单提供。

#### 摄影机设置(Camera Settings)

调整摄影机设置。请参见[摄影机设置选项](面板菜单：“视图”%28View%29/“摄影机设置”%28Camera%20Settings%29选项.md)。

#### 摄影机属性编辑器(Camera Attribute Editor)

打开摄影机属性编辑器。请参见[摄影机属性编辑器](面板菜单：“视图”%28View%29/摄影机属性编辑器%28Camera%20Attribute%20Editor%29.md)。

#### 摄影机工具(Camera Tools)

从各种摄影机工具中选择。请参见[“摄影机工具”(Camera Tools)菜单](面板菜单：“视图”%28View%29/“摄影机工具”%28Camera%20Tools%29菜单.md)。

#### 图像平面(Image Plane)

创建图像平面或访问其属性。请参见[创建、编辑或定位图像平面](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F72F8E1B-EFFE-400E-BD92-5441BE9CD28F)、[“图像平面”(Image plane)菜单](面板菜单：“视图”%28View%29/“图像平面”%28Image%20plane%29菜单.md)和[图像平面属性](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-60471C15-F6AC-4041-A7D7-5F89A2D2A4DB)。

#### 查看序列时间

如果您在有多个面板的布局中使用“摄影机序列器”(Camera Sequencer)，使用该菜单项可以设定面板是从“摄影机序列器”(Camera Sequencer)还是从自身显示活动摄影机视图。
