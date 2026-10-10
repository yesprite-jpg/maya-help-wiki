# 连接编辑器(Connection Editor)

导航到“窗口 > 常规编辑器 > 连接编辑器”(Windows > General Editors > Connection Editor)。

连接编辑器以并列布局提供节点连接信息，您可以在其中查看网络中的两个相连接的节点。该编辑器对于微调着色网络非常有用。

您可以快速轻松地从一个节点穿越到另一个节点，并显示节点的输出或输入以促进连接，这意味着您可以在节点网络中以任一方向建立连接。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-2F8F2B8B-7B22-4257-922C-05F39C9B4E4D.png) <!-- baize:img-hook downloaded=false reason="正文 2028 字 ≥300，非承重" -->

**注**

某些工具节点只能通过“连接编辑器”(Connection Editor)连接到材质的属性。

连接的属性在“连接编辑器”(Connection Editor)中以斜体显示（除 Mac OS X有些灰显属性指示嵌套属性列表。双击属性或展开属性，可以查看可连接的节点。

若要使用连接编辑器连接节点，请参见[通过拖动来连接节点](../使用节点编辑器创建节点网络/连接节点/通过拖动来连接节点.md)。

## “连接编辑器”(Connection Editor)按钮

“连接编辑器”(Connection Editor)的按钮控制如何建立连接。

#### “重新加载左侧”(Reload Left)和“重新加载右侧”(Reload Right)

将节点加载到“连接编辑器”(Connection Editor)的输出或输入窗格。选择节点、对象或着色器，然后单击“重新加载左侧”(Reload Left)或“重新加载右侧”(Reload Right)。

#### 从 -> 到(from -> to)

将输出属性切换为输入属性，或将输入属性切换为输出属性。

#### 箭头按钮 (![图：箭头按钮 ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-DF3B21D7-84C5-4441-BE6C-14F70E781619.png) <!-- baize:img-hook downloaded=false reason="正文 2028 字 ≥300，非承重" -->![图：箭头按钮 ()](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-6E8DE98D-355F-4775-A042-E59C6BBD9584.png) <!-- baize:img-hook downloaded=false reason="正文 2028 字 ≥300，非承重" -->)

将输出节点移动到输入窗格 (![图：将输出节点移动到输入窗格 ()，或将输入节点移动到输出窗格 ()。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-DF3B21D7-84C5-4441-BE6C-14F70E781619.png) <!-- baize:img-hook downloaded=false reason="正文 2028 字 ≥300，非承重" -->)，或将输入节点移动到输出窗格 (![图：将输出节点移动到输入窗格 ()，或将输入节点移动到输出窗格 ()。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-6E8DE98D-355F-4775-A042-E59C6BBD9584.png) <!-- baize:img-hook downloaded=false reason="正文 2028 字 ≥300，非承重" -->)。

#### 清除全部(Clear All)

从输出和输入窗格中移除节点。

#### 删除(Remove)

“移除”(Remove)输出窗格中的节点。

#### 断开(Break)

“断开”(Breaks)选定的连接。从输出窗格中选择要断开的连接，然后单击“断开”(Break)。只有当“自动连接”(Auto-connect)选项处于禁用状态时才可以使用该按钮。

#### 生成(Make)

在选定属性之间“创建”(Makes)连接。选择输出属性，再选择输入属性，然后单击“生成”(Make)。只有当“自动连接”(Auto-connect)选项处于禁用状态时才可以使用该按钮。

#### 关闭(Close)

关闭“连接编辑器”(Connection Editor)。

## “连接编辑器”(Connection Editor)菜单栏

#### 选项 > 自动连接(Options > Auto-connect)

选择该选项后，当选择输出属性和输入属性时，系统会自动创建连接。默认情况下，此选项处于启用状态。

#### 选项 > 通道名称(Options > Channel Names)

更改属性在“连接编辑器”(Connection Editor)中的显示方式。“易读”(Nice)设置以最具可读性的方式显示名称，即首字母大写加空格。“长”(Long)设置采用与节点相同的显示方式显示属性。“短”(Short)设置以短形式显示名称，例如，“边界框”(Bounding box)显示为 bb。

#### 选项 > 属性顺序(Options > Attribute Order)

更改属性在“连接编辑器”(Connection Editor)的列表中的显示顺序。属性可以按字母的升序或降序排列。

#### “左侧显示 > 显示可读项”(Left Display > Show Readable)和“右侧显示 > 显示可读项”(Right Display > Show Readable)

显示节点的所有属性，无论属性是否可以设定关键帧。默认情况下，此选项处于启用状态。

#### “左侧显示 > 仅显示输出”(Left Display > Show Outputs Only)和“右侧显示 > 仅显示输出”(Right Display > Show Outputs Only)

仅显示选定节点的输出连接。

#### “左侧显示 > 仅显示输入”(Left Display > Show Inputs Only)和“右侧显示 > 仅显示输入”(Right Display > Show Inputs Only)

仅显示选定节点的输入连接。

#### “左侧显示 > 仅显示已发布项”(Left Display > Show Published Only)和“右侧显示 > 仅显示已发布项”(Right Display > Show Published Only)

仅显示选定资产节点的已发布属性。

#### “左侧显示 > 显示不可设置关键帧的项”(Left Display > Show Non-Keyable)和“右侧显示 > 显示不可设定关键帧的项”(Right Display > Show Non-Keyable)

显示节点的不可设定关键帧的属性（无法为其创建连接的属性）。启用“显示可读项”选项时会启用该选项。

#### “左侧显示 > 仅显示连接项”(Left Display > Show Connected Only)和“右侧显示 > 仅显示连接项”(Right Display > Show Connected Only)

仅显示具有连接的属性。

#### “左侧显示 > 显示隐藏项”(Left Display > Show Hidden)和“右侧显示 > 显示隐藏项”(Right Display > Show Hidden)

显示节点的隐藏属性。
