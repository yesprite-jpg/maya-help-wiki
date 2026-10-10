# 使用“大纲视图”(Outliner)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 2295 字 ≥300，非承重" -->

| 目标 | 操作 |
|---|---|
| 选择对象。 | 在“大纲视图”(Outliner)中单击对象节点名称。如果是复杂场景，相对于尝试在视图面板中单击对象而言，在“大纲视图”(Outliner)中单击对象名称来选择对象通常更为容易。 |
| 选择多个对象。 | 在“大纲视图”(Outliner)中按住 Shift 键并单击或按住 Ctrl 键并单击对象节点名称。前者将添加到选择，而后者则启用和禁用上一选择。 |
| 展开或收拢节点下级别。 | 单击节点名称旁边的加号 ![图：单击节点名称旁边的加号 或减号 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-370190BF-6612-4E4A-AD24-7A5100A32840.png) <!-- baize:img-hook downloaded=false reason="正文 2295 字 ≥300，非承重" --> 或减号 ![图：单击节点名称旁边的加号 或减号 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-97F99310-F0E3-49A2-90EB-2A927A31063C.png) <!-- baize:img-hook downloaded=false reason="正文 2295 字 ≥300，非承重" -->。 |
| 展开或收拢节点下的**所有**级别（查看所有节点的快捷方法）。 | 按住 Shift 键并单击节点名称旁边的加号 ![图：按住 Shift 键并单击节点名称旁边的加号 或减号 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-370190BF-6612-4E4A-AD24-7A5100A32840.png) <!-- baize:img-hook downloaded=false reason="正文 2295 字 ≥300，非承重" --> 或减号 ![图：按住 Shift 键并单击节点名称旁边的加号 或减号 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-97F99310-F0E3-49A2-90EB-2A927A31063C.png) <!-- baize:img-hook downloaded=false reason="正文 2295 字 ≥300，非承重" -->。 |
| 在大纲视图中平移。 | 按住 Alt 键并使用鼠标中键拖动，或按住 (Mac OS X) Option 键并使用鼠标中键拖动。 若要快速平移，请按住 Ctrl + Alt 键并单击鼠标中键进行拖动，或按住 Ctrl + Option (Mac OS X) 键并单击鼠标中键进行拖动。 |
| 使节点成为其他节点的子节点（与其结成父子关系）。 | 使用鼠标中键拖动并将其放置在要成为该节点父节点的节点上。这也可以是某个组的变换节点。 如果无法在“大纲视图”(Outliner)中同时看到这两个节点，请改用[编辑 > 父对象(Edit > Parent)](../../../基本参考/基本参考/主菜单/“编辑”%28Edit%29菜单/“父对象”%28Parent%29选项.md)或按 P 键。 |
| 更改层次中的节点顺序。 | 使用鼠标中键拖动并将其放置在其他两个节点之间。 |
| 将节点从其父节点中移出（与其断开父子关系）。 | 在“大纲视图”(Outliner)的空白区域中按住鼠标中键并拖动子节点，或者将其拖动到另一个要成为其父对象的节点上。 也可以选择子节点，然后选择[编辑 > 断开父子关系(Edit > Unparent)](../../../基本参考/基本参考/主菜单/“编辑”%28Edit%29菜单/“断开父子关系”%28Unparent%29选项.md)或按 Shift+P。 |
| 搜索节点。 | 在“大纲视图”(Outliner)顶部的“搜索”(Search)字段中键入节点名称。有关搜索选项的详细信息，请参见[搜索节点](搜索和过滤节点.md)。 |
| 查找选定对象的节点。 | 在视图面板中选择对象，然后在“大纲视图”(Outliner)中按 **F** 键查找其节点。 |
| 重命名节点。 | 双击该节点名称，或者选中它并按 **Enter** 键。 在节点名称中，除下划线 (_) 和井号 (#) 之外，其他所有标点符号都是非法字符。 |
| 在大纲视图中更改节点名称的颜色。 | 在“属性编辑器”(Attribute Editor)中，单击“变换”(Transform)或“形状”(Shape)选项卡，选择 “显示 > 使用大纲视图颜色”(Display > Use Outliner Color)，然后选择要使用的颜色。 您可以选择“显示”(Display) > “忽略“使用大纲视图颜色”(Ignore 'Use Outliner Color')，从而在大纲视图中使用默认颜色，而无需在属性编辑器中更改设置。 |
| 过滤显示的对象类型。 | 从“大纲视图”(Outliner)的“显示”(Show) > “对象”(Objects)子菜单中选择选项。 |
| 显示指定给每个对象的材质。 | 选择“显示 > 指定的材质”(Display > Assigned Materials)。 指定的材质显示在对象下方。如果指定了多种材质，则着色器将分组到“材质”(Materials)标题下。 |
| 显示或隐藏节点。 | 若要在视图面板中隐藏节点，请选择该节点，然后按 **H** 键。在“大纲视图”(Outliner)中，节点名称为灰色。再次按 **H** 键即可显示。 若要在“大纲视图”(Outliner)隐藏节点，请选择它，然后选择“显示 > 在大纲视图中隐藏 > 隐藏”(Display > Hide In Outliner > Hide)。 由于通过这种方式隐藏的节点不显示在“大纲视图”(Outliner)中，因此必须先选择此菜单中的“忽略‘在大纲视图中隐藏’”(Ignore 'Hidden In Outliner')暂时显示它，或者从视图面板或其他编辑器中选择它，然后才能将其取消隐藏。再次显示之后，选择该节点，然后选择“取消隐藏”(Unhide)更改其隐藏状态。 |
| 在[属性编辑器](../查看和编辑属性/属性编辑器%28Attribute%20Editor%29.md)中打开节点。 | 双击节点名称旁的图标。 |
| 在大纲视图中显示属性（通道）。 | 启用“显示 > 属性(通道)”(Display > Attributes (Channels))。 属性的显示还可以使用“大纲视图”(Outliner)的“显示 > 属性”(Show > Attributes)子菜单进行限制。 |
| 显示或隐藏节点上的属性。 | 单击节点名称旁的圆形加号 (![图：单击节点名称旁的圆形加号 () 或减号 ()。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-CD1F5A9B-A585-4A34-A604-34D3DBEE71CD.png) <!-- baize:img-hook downloaded=false reason="正文 2295 字 ≥300，非承重" -->) 或减号 (![图：单击节点名称旁的圆形加号 () 或减号 ()。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-79A28963-9A0A-4561-A400-42914528DDDB.png) <!-- baize:img-hook downloaded=false reason="正文 2295 字 ≥300，非承重" -->)。 可以进一步展开多值属性。 属性值无法在大纲视图中编辑，请改用属性编辑器或通道盒。 |
| 在[表达式编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-251640EA-AACC-4F1B-A341-297F0F4CEFE4)中打开属性。 | 双击属性名称。 |
| 在浮动窗口中，打开“大纲视图”(Outliner)的另一个实例。 | 选择“面板”(Panels) > “撕下副本”(Tear Off Copy)。在此设置的选项（例如，使用不同的搜索或过滤选项）不会影响固定的大纲视图。 |
| ![图：拆分“大纲视图”(Outliner)窗口。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 2295 字 ≥300，非承重" --> 拆分“大纲视图”(Outliner)窗口。 | 若要水平或垂直分割“大纲视图”(Outliner)，请选择“显示 > 窗口布局”(Display > Window Layout)，然后选择**“水平分割”(Split Horizontally)**或**“垂直分割”(Split Vertically)**。 拖动窗口底部或侧边的分割条。 当指针停留在分割条上方时，光标将变为拖动 ![图：当指针停留在分割条上方时，光标将变为拖动 指示器。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-47682CA6-CE57-4AB3-ADCD-EF21B35F0714.png) <!-- baize:img-hook downloaded=false reason="正文 2295 字 ≥300，非承重" --> 指示器。 若要取消分割窗口，请向后拖动分割条。 注： 用于垂直分割大纲视图的选项仅在 Maya 主[大纲视图(Outliner)](../大纲视图%28Outliner%29.md)（“窗口 > 大纲视图”(Windows > Outliner)）中可用。其他大纲视图（例如[“曲线图编辑器大纲视图”(Graph Editor outliner)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EC141C05-37D8-4835-989B-538432690DBE)或[“摄影表”(Dope Sheet)大纲视图](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5E4AFD3F-16CF-49EA-9766-4090C5A4DB97)）只能水平分割。 |

**注**

“显示”(Display)和“显示”(Show)菜单设置将与场景文件一同保存，因此在打开新场景或不同场景时不会保留。

## 相关主题

- [属性编辑器(Attribute Editor)](../查看和编辑属性/属性编辑器%28Attribute%20Editor%29.md)

- [查看和编辑节点层次](../编辑节点层次.md)
