# 性能设置(Performance Settings)

**注**

这些选项仅适用于

Viewport 1.0

。在使用 Viewport 2.0 时，它们不会显示在界面中，且不会产生任何效果。请参见

使用 Viewport 2.0

。

若要打开“性能设置”(Performance Settings)，请选择“窗口 > 设置/首选项 > 性能设置”(Windows > Settings/Preferences > Performance Settings)。

此面板用于选择性能与质量之间的平衡，以及暂时禁用某些视觉更新来改善交互效果。

## 依存关系图求值

若要设置操纵对象时的刷新（或重画屏幕）时间，请在“依存关系图求值”(Dependency Graph Evaluation)部分中选择以下选项之一：

#### 拖动(Drag)

拖动时刷新显示。

#### 需要(Demand)

仅当释放鼠标按键并单击显示在显示窗口右下的“更新”(Update)按钮时，才刷新显示。

**注**

当前，

Viewport 2.0

不支持

“依存关系图求值”(Dependency Graph Evaluation)

、

“刷新条件”(Refresh on)

“需要”(Demand)

模式。

#### 释放(Release)

仅当释放鼠标按键时，才刷新显示。

## “曲面”(Surfaces)选项

使用这些选项，可以控制在与特定工具或操作进行交互时 Viewport 中是否显示其结果。与曲面交互时，请在曲面旁边的“曲面”(Surfaces)部分中选择以下选项之一：

#### 启用(On)

在鼠标交互期间执行复杂的操作。 例如，如果拖动用作投影的曲线来修剪曲面，则可看到修剪效果（曲面中生成一个孔）。释放鼠标按钮时，该效果仍保持可见。

#### 禁用(Off)

完全禁用鼠标交互期间的复杂操作。 例如，拖动修剪曲线时，修剪的效果从不会在 Viewport 中显示，无论您是在进行交互（拖动修剪曲线），还是未执行任何操作且 Maya 处于空闲状态，均是如此。

#### 交互式(Interactive)

当 Maya 处于空闲状态时（即，未与几何体交互时），挂起复杂操作。例如，拖动修剪曲线时，显示界面不会更新，而是等到您释放鼠标按钮后才会更新。

## Paint Effects

若要控制已设置动画的“Paint Effects”笔刷或已设置动画的笔划的播放，请在“Paint Effects”区域中选择以下选项之一：

#### 启用(On)

无论是处于播放期间还是对参数进行了修改，只要有所更改，就会刷新场景视图。

#### 禁用(Off)

在笔刷上运行 setAttr 时，才会更新笔刷。

#### 交互式(Interactive)

当播放结束或对参数进行修改时，会刷新场景视图。

## “变形器”(Deformers)选项

若要控制鼠标交互期间对变形器进行的复杂操作，请在“变形器”(Deformers)部分中选择曲面旁的以下选项之一：

#### 启用(On)

在鼠标交互期间执行复杂的操作。

#### 禁用(Off)

完全禁用鼠标交互期间的复杂操作。

#### 交互式(Interactive)

在鼠标交互期间挂起复杂操作。

#### 逐节点(Per Node)

仅适用于“簇分辨率”(Cluster Resolution)和“晶格分辨率”(Lattice Resolution)，通过设置部分的“使用部分分辨率”(Use Partial Resolution)属性和设置每个节点的“百分比分辨率”(Percent Resolution)，可以提高单个簇或晶格变形的重画性能。

#### 全局(Global)

仅适用于“簇分辨率”(Cluster Resolution)和“晶格分辨率”(Lattice Resolution)，可以提高全部簇或晶格变形的重画性能。（无需为每个簇或晶格设置百分比分辨率。）

将“全局簇分辨率”(Global Cluster Resolution)和“全局晶格分辨率”(Global Lattice Resolution)设置为“完全”(Full)、“高”(High)、“中等”(Medium)或“低”(Low)。“低”相对应的百分比较低，因此能进一步提高性能。
