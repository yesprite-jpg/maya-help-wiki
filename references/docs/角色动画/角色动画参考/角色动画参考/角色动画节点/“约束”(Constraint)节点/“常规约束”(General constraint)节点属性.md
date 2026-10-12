# “常规约束”(General constraint)节点属性

节点行为属性包括“缓存”(Caching)和“节点状态”(Node State)。

## 枢轴(Pivots)

在局部或世界空间中显示点约束的局部旋转和缩放轴所对应的选择。

## 限制信息(Limit Information)

仅供 Maya 内部使用：从变换节点继承的属性。

## 显示(Display)

选择控制柄显示属性所对应的选择，包括控制柄显示、局部轴显示、选择控制柄位置（相对于当前平移 X、平移 Y 和平移 Z 属性值）、默认操纵器显示选择、可见性和模板。“边界框信息”(Bounding Box Information)和“绘制覆盖”(Drawing Overrides)不适用。

## 节点行为(Node Behavior)

#### 缓存(Caching)

指定 Maya 存储输入求值的结果，然后将这些结果提供给节点。因此，Maya 不必在每次节点需要结果时重新对输入节点求值。如果输入节点无任何更改，则该设置可以提高显示性能，同时不丢失任何结果。但是，请注意，与其他方式相比，缓存将使用更多的内存，这可能对性能造成不利影响。此外，如果输入节点存在更改，将分配更多的内存，然后释放，这也可能对显示性能造成不利影响。

#### 节点状态(Node State)

将“节点状态”(Node State)设定为“正常”(Normal)、“无效果”(HasNoEffect)、“阻塞”(Blocking)、“等待-正常”(Waiting-Normal)、“等待-无效果”(Waiting-HasNoEffect)或“等待-阻塞”(Waiting-Blocking)。（请注意，对于约束，“节点状态”(Node State)属性是作为“通道盒”(Channel Box)中的一个通道来提供的。）

#### 正常(Normal)

指定 Maya 对约束求值并显示约束。Maya 将与平常一样对该节点求值。这是默认设置。

#### 无效果(HasNoEffect)

指定 Maya 禁止约束，但显示对象。Maya 将对该节点的历史中的各节点求值，但不对该节点本身求值。

#### 阻塞(Blocking)

指定 Maya 禁止约束，并且不显示对象。Maya 不会对该节点报告输入节点的任何求值结果。

#### 等待-正常(Waiting-Normal)

（仅供 Maya 内部使用。）指定如果将依存关系图求值刷新性能设置（[窗口 > 设置/首选项 > 性能设置(Window > Settings/Preferences > Performance Settings)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9F78C71A-0F3B-4194-BC51-AB462D211426)）设定为“需要”(Demand)或“释放”(Release)，则单击“更新”(Update)或释放鼠标按钮时，该节点将呈现“正常”(Normal)状态。

#### 等待-无效果(Waiting-HasNoEffect)

（仅供 Maya 内部使用。）指定如果将依存关系图求值刷新性能设置设定为“需要”(Demand)或“释放”(Release)，则单击“更新”(Update)或释放鼠标按钮时，该节点将呈现“无效果”(HasNoEffect)状态。

#### 等待-阻塞(Waiting-Blocking)

（仅供 Maya 内部使用。）指定如果将依存关系图求值刷新性能设置设定为“需要”(Demand)或“释放”(Release)，则单击“更新”(Update)或释放鼠标按钮时，该节点将呈现“阻塞”(Blocking)状态。

## 附加属性(Extra Attributes)

如果约束包括多个目标对象，则每个对象的其他属性可以显示在“属性编辑器”(Attribute Editor)的“附加属性”(Extra Attributes)区域，或显示在“通道盒”(Channel Box)中其他约束属性下方。

最常见的附加属性是每个目标对象的权重值。这些权重属性按照以下命名约定显示：<objectname> W <n>。

例如，两个多边形球体的权重属性可以显示为“P 球体 1W0”和“P 球体 2W1”。在约束创建选项中设定这些权重的初始值。

多边形上的点约束还包括每个受约束对象的 UV 坐标的附加属性。这些 UV 属性按照以下命名约定显示：<objectName> U <n> 和 <objectName> V <n>。使用这些属性，您可以定义每个目标对象受网格约束的位置。请参见[编辑多边形上的点约束属性](../../../../约束/约束/多边形上的点约束/编辑多边形上的点约束.md)。
