# Hypershade 标记菜单

除了工具栏和菜单外，Hypershade 标记菜单提供了自定义着色器图表的其他方式。

## Hypershade 浏览器标记菜单

在 [Hypershade 浏览器](../Hypershade%20浏览器.md)中的空白区域单击鼠标右键将显示一个标记菜单，通过它可以访问与 Hypershade 菜单栏相同的菜单。

在样例上单击鼠标右键将显示一个标记菜单，其中包含与指定、显示和选择材质相关的常见操作。

| 菜单项 | 效果 |
|---|---|
| 为当前选择指定材质(Assign Material To Selection) | 为在工作区中选择的任何对象指定样例材质。 |
| 绘制指定着色器(Paint Assign Shader) | 激活“绘制选择工具”(Paint Selection Tool)，用于通过绘制特定面为选定对象指定样例材质。 |
| 选择具有材质的对象(Select Objects With Material) | 选择场景中使用亮显样例材质的所有对象。 |
| 为网络制图(Graph Network) | 在工作区中显示亮显样例材质的图表。 |
| 刷新样例(Refresh Swatch) | 更新亮显样例。 |
| 框显具有材质的对象(Frame Objects With Material) | 在工作区中框显具有亮显样例材质的所有对象。 |
| [从以下对象移除材质覆盖(Remove Material Override From)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3ADB39A0-B350-4564-8FF6-7BCC624AD906) | 移除在渲染层上为亮显样例材质创建的任何材质覆盖，从而还原为主层的材质着色器。 注： 仅适用于传统渲染层。 |
| 选择输入节点(Select Input Nodes) | 选择所有提供亮显样例材质属性的输入（上游）节点。 |
| 选择输出节点(Select Output Nodes) | 选择由亮显样例材质属性馈送的所有输出（下游）节点。 |
| 重命名(Rename) | 用于重命名与亮显样例对应的材质。 |
| [从选定对象中创建资产(Create asset from selected)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1826F831-E3D1-4045-B6B9-F7D34360C331) | 创建包含选定样例材质的资产。 |
| 从资产中移除选定节点(Remove selected nodes from asset) | 从可能包含选定样例材质的任何资产中移除该材质。 |

## Hypershade 工作区标记菜单

在 [Hypershade 工作区](../Hypershade%20工作区.md)中的空白区域单击鼠标右键将显示一个标记菜单，通过它可以访问用于创建和显示着色网络的命令。

| 菜单项 | 效果 |
|---|---|
| [创建节点(Create Node)](../../../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/在%20Hypershade%20中创建和连接节点.md) | 打开“创建节点”(Create Node)窗口，用于创建新的着色器节点。如果“创建”(Create)选项卡当前已关闭，这将非常有用。 |
| [选择流中的项目(Select Items in Stream)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B80E8A92-F75D-4512-A135-BB157E928E97) | 用于快速选择所有相对于选定输入（上游）和输出（下游）节点的此类节点。 |
| [单放最后一个连接(Solo Last Connection)](../../../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/关于单放/在%20Hypershade%20中单放节点.md) | 重新单放最近单放的属性。有关单放的详细信息，请参见[关于单放](../../../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/关于单放.md)。 |
| 对视口选择上的材质制图(Graph Materials on Viewport Selection) | 在工作区中显示连接到任何选定对象的所有着色网络。 |
| 选择图表中的所有对象(Select All in Graph) | 在 Hypershade 图形中亮显所有节点。 |
| [删除材质单放(Remove Material Soloing)](../../../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/关于单放.md) | 从场景中删除单放。 |
| 同步节点编辑器/视口选择(Sync Node Editor/Viewport Selection) | 切换是否也在工作区和“节点编辑器”(Node Editor)中选择您在工作区中做出的选择。 |
| 创建时添加到图表(Add to Graph on Create) | 切换是否将新创建的着色节点自动添加到工作区和场景。如果禁用，则只有使用 Tab 创建或拖放创建方法创建的节点才添加到工作区。默认情况下，该选项处于启用状态。 |
| [添加制图模式(Additive Graphing Mode)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6EDB8816-0957-4E95-982A-6E751502E7B8) | 切换是将选定节点添加到工作区中的当前图形，还是完全替换图形。启用此选项，然后选择一个节点并单击 ![图：切换是将选定节点添加到工作区中的当前图形，还是完全替换图形。启用此选项，然后选择一个节点并单击 、 和 图标之一，可对选…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-5144BEC8-04D7-4C4C-B4E3-A482BDC19E58.png) <!-- baize:img-hook downloaded=false reason="正文 3376 字 ≥300，非承重" -->、![图：切换是将选定节点添加到工作区中的当前图形，还是完全替换图形。启用此选项，然后选择一个节点并单击 、 和 图标之一，可对选…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-2DAD0BAA-9888-4075-B3DB-3C45B5CF4481.png) <!-- baize:img-hook downloaded=false reason="正文 3376 字 ≥300，非承重" --> 和 ![图：切换是将选定节点添加到工作区中的当前图形，还是完全替换图形。启用此选项，然后选择一个节点并单击 、 和 图标之一，可对选…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-9292A041-82B0-4D36-99D7-278855A7552C.png) <!-- baize:img-hook downloaded=false reason="正文 3376 字 ≥300，非承重" --> 图标之一，可对选定节点制图并将其添加到现有网络中。 |
| 默认固定所有节点(Pin all nodes by default) | 切换是否自动固定节点，确保即使刷新工作区后这些节点也停留在相同点上。 |
| 显示(Display) | 通过选择提供的任一选项来自定义图表。 |
| 显示(Show) | 过滤工作区中要显示的节点类型。默认情况下，显示“摄影机”(Cameras)、“着色组”(Shading Groups)和“着色节点”(Shading Nodes)。 |
| [切换选择样例大小(Toggle Selection Swatch Size)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-773364B4-9F82-4751-8F8A-0EEEECADE51D) | 增大或减小工作区中所有选定样例的大小。 |
| [Hypergraph](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5EC40DB1-FBD9-4553-A2FD-6D3508C9B868) | 打开 Hypergraph，其中显示选定节点的层次。 |

在 [Hypershade 工作区](../Hypershade%20工作区.md)中的节点上单击鼠标右键将显示一个标记菜单，通过它可以访问相对于该节点有用的命令。

| 菜单项 | 效果 |
|---|---|
| 将材质指定给视口选择(Assign Material To Viewport Selection) | 将材质指定给在工作区中选择的任何对象（仅着色器节点）。 |
| 绘制指定着色器(Paint Assign Shader) | 激活“绘制选择工具”(Paint Selection Tool)，用于通过绘制特定面为选定对象指定样例材质（仅着色器节点）。 |
| [选择/重新绘制/移除流节点(Select/Regraph/Remove Stream Nodes)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B80E8A92-F75D-4512-A135-BB157E928E97) | 用于选择和修改其他节点相对于工作区中选定节点的显示状态。 |
| 刷新样例(Refresh Swatch) | 通过单击 Hypershade “浏览器”(Browser)工具栏上的 ![图：通过单击 Hypershade “浏览器”(Browser)工具栏上的 按钮，可以禁用所有节点的样例生成。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-E877B724-DC07-4153-8B4B-E4B3661E9311.png) <!-- baize:img-hook downloaded=false reason="正文 3376 字 ≥300，非承重" --> 按钮，可以禁用所有节点的样例生成。 然后，通过选择此选项，可以对着色器图表中的特定节点启用样例渲染。请参见[暂停材质和纹理的样例生成](../../../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/暂停材质和纹理的样例生成以提高%20Hypershade%20性能.md)。 |
| 选择具有材质的对象(Select Objects With Material) | 选择场景中使用亮显样例材质的所有对象（仅着色器节点）。 |
| [删除材质单放(Remove Material Soloing)](../../../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/关于单放.md) | 从场景中删除单放。 |
| [单放(Solo)](../../../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/关于单放.md) | 单放节点，在“材质查看器”(Material Viewer)中隔离其效果（仅着色器节点）。有关单放的详细信息，请参见[关于单放](../../../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/关于单放.md)。 |
| 框显具有材质的对象(Frame Objects With Material) | 在工作区中框显具有亮显样例材质的所有对象（仅着色器节点）。 |
| [从以下对象移除材质覆盖(Remove Material Override From)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3ADB39A0-B350-4564-8FF6-7BCC624AD906) | 移除在渲染层上创建的任何材质覆盖，从而还原为主层的材质着色器（仅着色器节点）。 注： 仅适用于传统渲染层。 |
| [渲染纹理范围(Render Texture Range)](../../../../关于着色和纹理曲面/纹理/测试纹理（和纹理范围）.md) | 打开 FCheck 窗口，以显示纹理图像的范围（仅本地渲染节点）。 |
| [测试纹理(Test Texture)](../../../../关于着色和纹理曲面/纹理/测试纹理（和纹理范围）.md) | 打开“渲染视图”(Render View)窗口，以显示一个样例用于展现材质的样例（仅本地渲染节点）。 |
| 输入(Inputs) | 列出所有提供节点属性的输入（上游）节点。 |
| 输出(Outputs) | 列出所有由节点属性馈送的输出（下游）节点。 |
| 重命名(Rename) | 用于重命名节点。 |
| [切换样例大小(Toggle Swatch Size)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-773364B4-9F82-4751-8F8A-0EEEECADE51D) | 增大或减小节点样例的大小。此选项仅影响通过其访问标记菜单的节点。 |
| [切换选择样例大小(Toggle Selection Swatch Size)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-773364B4-9F82-4751-8F8A-0EEEECADE51D) | 增大或减小工作区中所有选定样例的大小。您也可以使用快捷方式 v。 |
| [编辑自定义属性列表(Edit Custom Attribute List)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C1E02C84-8CCF-4B3D-B080-F4A379AD1FCB) | 用于修改在工作区中对特定节点显示和隐藏的属性。创建自定义属性列表后，单击 ![图：用于修改在工作区中对特定节点显示和隐藏的属性。创建自定义属性列表后，单击 以提交更改。请参见自定义节点属性列表](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-01F0B285-2776-4A14-9B4D-0BE4F560BA3C.png) <!-- baize:img-hook downloaded=false reason="正文 3376 字 ≥300，非承重" --> 以提交更改。请参见[自定义节点属性列表](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C1E02C84-8CCF-4B3D-B080-F4A379AD1FCB) |
| 显示所有属性(Show All Attributes) | 显示选定节点的所有属性。所有属性的显示仅对该绘制实例有效。如果对节点重新制图，或者更改节点的视图模式，则必须重新选择此选项才可再次显示其所有属性。 |
| [添加属性(Add Attributes)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EC37B453-05D8-4A60-B6A9-57895363759E) | 打开“添加属性”(Add Attribute)窗口，用于创建选定节点的自定义属性。 |
| [删除属性(Delete Attributes)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EC37B453-05D8-4A60-B6A9-57895363759E) | 打开“删除属性”(Delete Attribute)窗口，用于移除选定节点的自定义属性。 |

在 [Hypershade 工作区](../Hypershade%20工作区.md)中的连接上单击鼠标右键将显示一个标记菜单，通过它可以访问相对于该连接有用的命令。

| 菜单项 | 效果 |
|---|---|
| 断开连接(Break Connection) | 移除链接的节点之间的连接。 |
| 隔离连接的节点(Isolate connected nodes) | 减少工作区显示的内容，仅显示由选定连接相连的节点。 |
| 选择连接的节点(Select connected nodes) | 选择由选定连接相连的所有节点。 |

## 相关主题

- [标记菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8BA1A3AA-4C44-4779-8B22-0AAE3627E8EB)
