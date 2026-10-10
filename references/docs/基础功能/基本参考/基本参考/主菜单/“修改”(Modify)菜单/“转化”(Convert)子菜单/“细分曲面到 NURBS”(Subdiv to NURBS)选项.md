# “细分曲面到 NURBS”(Subdiv to NURBS)选项

使用以下选项可设置选择“网格显示 > 设置为面”(Mesh Display > Set to Face)时发生的情况。

#### 原始对象(Original Object)

指定源对象在转化后发生的变化。

#### 替换(Replace)

删除原始对象，仅保留原始变换节点。为了保持场景层次，Maya 将保留原始变换节点，并使生成的 NURBS 面片成为该节点的子对象。

#### 隐藏和显示(Hide and Show)

这些选项将保留原始对象。如果启用了构建历史，您仍可以编辑原始细分曲面，更改生成的 NURBS 面片。如果设置为“隐藏”，视图中将隐藏原始对象。如果以后要显示和编辑原始对象，请在“大纲视图”(Outliner)中选择该对象，然后选择“显示 > 显示 > 显示当前选择”(Display > Show > Show Selection)。

#### 输出类型(Output Type)

除了 NURBS 外，也可以通过启用 Bezier 选项创建 Bezier 曲面Bezier 曲面可以导出供某些游戏引擎使用。

如果执行“曲面”(Surfaces)菜单中的操作（如插入等参线），曲面将从 Bezier 切换为 NURBS。若要切换回 Bezier，请使用“曲面 > 重建”(Surfaces > Rebuild)。
