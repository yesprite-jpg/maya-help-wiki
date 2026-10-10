# vectorExtrude

创建类型或 SVG 对象时会创建一个 vectorExtrude 节点。

## 挤出(Extrude)

#### 启用挤出(Enable Extrusion)

启用时，网格对象向前挤出以增加深度，否则保持为平面。共享与连接的类型或 SVG 节点的“启用挤出”(Enable Extrusion)属性相同的值。

#### 作为分数偏移挤出(Offset Extrude As Fraction)

启用时，将“挤出偏移”(Extrude Offset)属性转化为网格中最短边的百分比。将“挤出偏移”(Extrude Offset)设置为介于 0 和 1 之间的值时，这将确保不会创建由内到外的倒角。默认值为启用。

#### 挤出距离(Extrude Distance)

控制挤出多边形的距离。共享与连接的类型或 SVG 节点的“挤出距离”(Extrude Distance)属性相同的值。

#### 挤出分段(Extrude Divisions)

控制沿挤出面的细分数。共享与连接的类型或 SVG 节点的“挤出分段”(Extrude Divisions)属性相同的值。

#### 挤出偏移(Extrude Offset)

设置网格挤出偏移。当“分数偏移”(Fractional Offset)处于禁用状态时，此偏移以场景单位表示。当“作为分数偏移挤出”(Offset Extrude As Fraction)处于启用状态时，此偏移用网格中最短边的百分比表示。共享与连接的类型或 SVG 节点的“挤出偏移”(Extrude Offset)属性相同的值。

#### 捕捉到栅格(Snap to Grid)

启用时，“挤出剖面曲线”(Extrusion Profile Curve)中的控制点捕捉到经过的图形点。默认设置为禁用。

#### 挤出剖面曲线(Extrusion Profile Curve)

此图控制挤出的形状。最左侧的点始终表示原始类型在挤出之前的位置，而其右侧的所有点则表示相对于该点的位置。通过分别单击图表上方的左键和右键，您可以在曲线自己的窗口中将其打开或将其返回到自己的默认形状。共享与连接的类型或 SVG 节点的“挤出剖面曲线”(Extrusion Profile Curve)相同的形状。

#### 自定义剖面(Custom Profiles)

最多允许保存 12 个自定义“挤出剖面曲线”(Extrusion Profile Curve)形状。您可以通过单击“自定义剖面”(Custom Profiles)属性名称旁边的保存按钮来保存形状。如果已经保存了 12 个剖面，则单击该按钮时将保存最旧的剖面。

## 倒角(Bevel)

#### 启用前倒角(Enable Front Bevel)

将倒角作为前盖上的一组挤出应用于网格。其下的控制属性镜像挤出属性的功能。

**注**

“挤出”(Extrusion)

和

“倒角”(Bevel)

部分中的

“作为分数偏移挤出”(Offset Extrude As Fraction)

均表示同一属性。

## 相关主题

- [创建多边形文本](../../多边形选择和创建/创建多边形文字.md)

- [类型工具](../多边形建模工具/“类型工具”%28Type%20Tool%29选项.md)

- [从 SVG 创建多边形](../../多边形选择和创建/从%20SVG%20对象创建多边形网格.md)

- [SVG 工具](../多边形建模工具/“SVG%20工具”%28SVG%20Tool%29选项.md)
