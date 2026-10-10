# “曲线图编辑器”(Graph Editor)  “列表”(List)菜单

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 1628 字 ≥300，非承重" -->

#### 自动加载选定对象(Auto Load Selected Objects)

“自动加载”(Auto Load)启用后，每次选择显示当前选定对象时，“大纲视图”(Outliner)中显示的对象将会更改。如果“自动加载”(Auto Load)已禁用，则它将锁定“大纲视图”(Outliner)中的当前对象，以便即使在场景视图中做出新选择时，也可以继续编辑其动画曲线。

#### 加载选定对象(Load Selected Objects)

仅在“自动加载”(Auto Load)禁用时才可使用该项目。“自动加载”(Auto Load)禁用时，“大纲视图”(Outliner)中显示的对象可能会与当前在场景视图中选择的对象不同步。若要使用当前选择重新加载“大纲视图”(Outliner)，则选择“选项 > 重新加载列表”(Option > Reload List)。

#### 添加选定对象(Add Selected Objects)

若要在“曲线图编辑器”(Graph Editor)中处理某个对象的动画以及另一尚未加载至“大纲视图”(Outliner)的对象，请选择该对象，并选择“选项 > 将选定对象添加到列表中”(Options > Add Selected to List)。这会将选定对象添加到“曲线图编辑器大纲视图”(Graph Editor outliner)中，并且不会中断对象和动画曲线当前在“曲线图编辑器”(Graph Editor)中的布局。

#### 书签(Bookmarks)

若要在“曲线图编辑器”(Graph Editor)中保存一个或多个对象的动画视图，请创建书签。

##### 为当前对象建立书签(Bookmark Current Objects)

打开“为当前对象建立书签”(Bookmark Current Objects)窗口。使用该窗口，可以为当前在“曲线图编辑器”(Graph Editor)中加载的对象设定书签。对象书签允许将对象加载到“曲线图编辑器”(Graph Editor)，而无需在场景视图中选择它们。

对象书签在“书签”(Bookmarks)菜单中显示为列表。选择对象书签（由选中标记指示）时，其关联对象将加载到“曲线图编辑器”(Graph Editor)中。移除对象书签选择（无选中标记）时，其关联对象不会从“曲线图编辑器”(Graph Editor)中卸载。

**注**

提示：

如果要为对象书签指定名称，请选择

“为当前对象建立书签”(Bookmark Current Objects)

>

。

##### 为选定曲线添加书签(Bookmark Selected Curves)

打开“为选定曲线添加书签”(Bookmark Selected Curves)窗口。使用该窗口，可以为选定曲线设定曲线书签。使用曲线书签，可以将曲线节点加载到“曲线图编辑器”(Graph Editor)中，而无需在场景视图中选择曲线的对象。

曲线书签在“书签”(Bookmarks)菜单中显示为列表。选择曲线书签（由选中标记指示0）时，其关联曲线节点将加载到“曲线图编辑器”(Graph Editor)中。取消曲线书签选择（无选中标记）时，其关联曲线节点将从“曲线图编辑器”(Graph Editor)中卸载。

##### 移除所有书签(Remove All Bookmarks)

移除“曲线图编辑器”(Graph Editor)中显示的当前对象和曲线中的所有书签。

#### 显示上游曲线(Show Upstream Curves)

可用于限制要在图表视图中显示选定通道的哪些曲线。启用时，仅显示直接连接的曲线。禁用时，显示选定通道的所有曲线。

请参见[仅显示直接连接的曲线](../../../关键帧动画/关键帧动画/编辑曲线/使用“曲线图编辑器”%28Graph%20Editor%29和“摄影表”%28Dope%20Sheet%29/在曲线图编辑器中设置曲线显示选项.md#WS73099CC142F48755-19B9987911EC57BA220-646F)。

#### 显示动画图形(Show Animated Shapes)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1628 字 ≥300，非承重" -->

控制是否自动展开选定 DAG 节点下的动画图形。

启用（默认设置）该选项后，将展开选定 DAG 节点，并且“曲线图编辑器”(Graph Editor)将显示该节点的曲线和所有动画图形。禁用该选项后，不会展开选定 DAG 节点，并且仅显示选定节点的曲线。

## 相关主题

- [曲线图编辑器(Graph Editor)](../../曲线图编辑器%28Graph%20Editor%29.md)

- [“曲线图编辑器”(Graph Editor)菜单](../“曲线图编辑器”%28Graph%20Editor%29菜单.md)
