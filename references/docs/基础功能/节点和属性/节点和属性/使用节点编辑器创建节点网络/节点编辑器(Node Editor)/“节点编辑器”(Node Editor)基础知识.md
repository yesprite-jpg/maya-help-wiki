# “节点编辑器”(Node Editor)基础知识

下表列出了“节点编辑器”(Node Editor)的基本功能概览。

| 目标 | 操作 |
|---|---|
| 显示连接。 | 选择节点，并在工具栏中单击 ![图：选择节点，并在工具栏中单击 图标，以显示输入和输出节点连接。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-2DAD0BAA-9888-4075-B3DB-3C45B5CF4481.png) <!-- baize:img-hook downloaded=false reason="正文 1392 字 ≥300，非承重" --> 图标，以显示输入和输出节点连接。 |
| 更改节点的视图模式以显示更短或更长的属性列表。 | 使用 1、2、3 和 4 热键在不同的视图模式之间切换。 |
| 创建节点。 | 按 Tab 键，然后输入节点的类型。 或者，可以 ![图：或者，可以 以显示创建节点窗格，然后用鼠标中键将所需的节点拖放到工作区中。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-1938F4A7-9C1D-49F5-830C-8E51F13C3C8F.png) <!-- baize:img-hook downloaded=false reason="正文 1392 字 ≥300，非承重" --> 以显示创建节点窗格，然后用鼠标中键将所需的节点拖放到工作区中。 |
| 使用连接线创建连接。 | 通过单击 ![图：通过单击 ，将节点展开为完全模式。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-C3D62C33-944A-4D5E-9DDE-E124E94AC45B.png) <!-- baize:img-hook downloaded=false reason="正文 1392 字 ≥300，非承重" -->，将节点展开为完全模式。 单击源端口和目标端口，或者单击鼠标中键或左键进行拖动，以便在输出和输入属性之间创建连接线。 |
| 创建默认节点连接。 | 在按住 Ctrl 键的同时使用鼠标中键将节点拖动到“节点编辑器”(Node Editor)中的另一个节点上。 |
| 使用“连接编辑器”(Connection Editor)连接节点。 | 在按住 Shift 键的同时使用鼠标中键将节点拖动到“节点编辑器”(Node Editor)中的另一个节点上。 |
| 将默认输出连接到特定输入属性。 | 使用鼠标中键将节点拖动到“节点编辑器”(Node Editor)中的另一个节点上。 |
| 删除连接。 | 拖动连接线，然后在背景区域中释放鼠标以删除连接。 或者，可以单击连接线/框选连接线，然后按 Backspace 键或 Delete 键。 |
| 更改现有的连接。 | 拖动连接线以断开连接，然后与新的输入/输出重新连接。 |
| 显示具有不同连接线样式的连接。 | 从“显示 > 连接样式”(Display > Connection Style)菜单中选择所需的样式。 |
| 创建或删除选项卡 | 单击最右侧选项卡中的 + 号以创建选项卡。 右键单击选项卡并选择“关闭选项卡”(Close Tab)，或者使用鼠标中键单击选项卡以将其删除。 也可以使用“选项卡”(Tabs)菜单。 |
| 撕下选项卡以放到其自己的窗口中 | 单击鼠标左键或鼠标中键拖动选项卡以关闭选项卡栏。 |
| 为节点制图，并将其添加到现有网络中。 | 启用“选项 > 添加制图模式”(Options > Additive Graphing Mode)。选择一个节点，然后单击 ![图：启用“选项 添加制图模式”(Options Additive Graphing Mode)。选择一个节点，然后单击 、 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-5144BEC8-04D7-4C4C-B4E3-A482BDC19E58.png) <!-- baize:img-hook downloaded=false reason="正文 1392 字 ≥300，非承重" -->、![图：启用“选项 添加制图模式”(Options Additive Graphing Mode)。选择一个节点，然后单击 、 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-2DAD0BAA-9888-4075-B3DB-3C45B5CF4481.png) <!-- baize:img-hook downloaded=false reason="正文 1392 字 ≥300，非承重" --> 和 ![图：启用“选项 添加制图模式”(Options Additive Graphing Mode)。选择一个节点，然后单击 、 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-9292A041-82B0-4D36-99D7-278855A7552C.png) <!-- baize:img-hook downloaded=false reason="正文 1392 字 ≥300，非承重" --> 图标中的一个，以将其图形添加到现有节点网络。 |
| 锁定视图。 | 单击 ![图：单击 。您创建的任何新节点都不会显示在图形中。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-5E297697-7236-4F97-A6B3-FA033569E99D.png) <!-- baize:img-hook downloaded=false reason="正文 1392 字 ≥300，非承重" -->。您创建的任何新节点都不会显示在图形中。 或者，可以从“节点编辑器”(Node Editor)工作区标记菜单禁用“创建时添加到图表中”(Add to Graph on Create)选项。 |
| 将节点固定到视图中。 | 可以固定节点，以便即使重新制图后该节点也保留在“节点编辑器”(Node Editor)视图中，并保持其位置和大小不变。已固定的节点显示有 ![图：可以固定节点，以便即使重新制图后该节点也保留在“节点编辑器”(Node Editor)视图中，并保持其位置和大小不变。已…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-366F0CD5-75B2-4617-8B3D-92B33A0C876F.png) <!-- baize:img-hook downloaded=false reason="正文 1392 字 ≥300，非承重" --> 图标。使用热键 p 在固定和取消固定选定节点之间切换。启用“选项 > 默认固定所有节点”(Options > Pin all nodes by default)（或通过工作区标记菜单启用该选项）可始终固定新创建的节点。 |
| 捕捉到栅格。 | 单击 ![图：单击 或选择“显示 栅格捕捉”(Display Grid Snapping)将节点捕捉到栅格。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-C16958BF-0B1E-431B-A565-94C883298ABC.png) <!-- baize:img-hook downloaded=false reason="正文 1392 字 ≥300，非承重" --> 或选择“显示 > 栅格捕捉”(Display > Grid Snapping)将节点捕捉到栅格。 |
| 关闭栅格背景。 | 单击 ![图：单击 以开启和关闭栅格背景，或选择/取消选择“显示 栅格”(Display Grid)菜单选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-61B00525-4F57-4772-821B-C81467DB4C3A.png) <!-- baize:img-hook downloaded=false reason="正文 1392 字 ≥300，非承重" --> 以开启和关闭栅格背景，或选择/取消选择“显示 > 栅格”(Display > Grid)菜单选项。 |
| 在“节点编辑器”(Node Editor)中选择了节点时，您就不希望在场景视图中选择它，反之亦然。 | 在工作区域中单击鼠标右键以显示标记菜单，并禁用“同步节点编辑器/视口选择”(Sync Node Editor/Viewport Selection)选项。详细信息请参见[节点编辑器(Node Editor)中的选择](../节点编辑器%28Node%20Editor%29中的选择.md)。 |

## 相关主题

- [使用节点编辑器](../../使用节点编辑器创建节点网络.md)

- [连接节点](../连接节点.md)

- [在节点编辑器中更改视图模式。](../自定义节点视图/更改节点编辑器和%20Hypershade%20中的视图模式.md)
