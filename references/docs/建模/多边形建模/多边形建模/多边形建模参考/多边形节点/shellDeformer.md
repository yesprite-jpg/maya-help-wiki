# shellDeformer

当您创建类型或 SVG 对象时，将会创建 shellDeformer 节点。

## 变换

#### 启用动画(Enable Animation)

启用后，将基于其下方的属性设置对相应的网格制作动画。

#### “动画位置”(Animation Position)、“动画旋转”(Animation Rotation)、“动画缩放”(Animation Scale)

适当地变换相应的网格对象。默认情况下，这些属性都受“动画”(Animation)部分中类型或 SVG 节点的“平移”(Translate)、“旋转”(Rotate)和“缩放”(Scale)属性的驱动。动画曲线可以在“曲线图编辑器”(Graph Editor)中进行调整。

## 步长

#### 随机延迟(Random Delay)

启用后，为相应网格中的每个对象指定随机延迟。共享与连接类型或 SVG 节点的“随机化延迟”(Randomize Delay)属性相同的值。

#### 反转顺序(Reverse Order)

启用此选项后，将反转在相应网格中为对象制作动画的当前顺序。共享与连接的类型或 SVG 节点的“反转顺序”(Reverse Order)属性相同的值。

#### 延迟帧(Delay Frames)

设置对网格中的每个对象制作动画之间的延迟。延迟是指动画时间内所有对象的总延迟（因此每个对象的延迟是网格中的动画总帧数/对象数量）。共享与连接的类型或 SVG 节点的“延迟帧”(Delay Frames)属性相同的值。

#### 随机种子(Random Seed)

设定用于初始化伪随机编号生成器（用于“随机延迟”(Random Delay)属性）的编号。更改该值可更改当前的随机化。共享与连接的类型或 SVG 节点的“随机种子”(Random Seed)属性相同的值。

## 枢轴

#### “X 枢轴位置”(X Pivot Location)、“Y 枢轴位置”(Y Pivot Location)、“Z 枢轴位置”(Z Pivot Location)

相对于 1, 1, 1 边界框为网格中的所有对象设定轴点。共享与连接的类型或 SVG 节点的“X 轴”(X Pivot)、“Y 轴”(Y Pivot)和“Z 轴”(Z Pivot)属性相同的值。

#### 局部 XRotation 轴(Local XRotation Pivot)、局部 YRotation 轴(Local YRotation Pivot)、局部 ZRotation 轴(Local ZRotation Pivot)、局部 XScale 轴(Local XScale Pivot)、局部 YScale 轴(Local YScale Pivot)、局部 ZScale 轴(Local ZScale Pivot)

启用后，将相应的枢轴设定为相对于每个对象的局部轴。共享与连接的类型或 SVG 节点的相应“局部轴”(Local Pivot)属性相同的值。

#### 时间(Time)

显示当前帧。连接到全局“时间”(Time)节点。

## 相关主题

- [创建多边形文本](../../多边形选择和创建/创建多边形文字.md)

- [类型工具](../多边形建模工具/“类型工具”%28Type%20Tool%29选项.md)

- [从 SVG 创建多边形](../../多边形选择和创建/从%20SVG%20对象创建多边形网格.md)

- [SVG 工具](../多边形建模工具/“SVG%20工具”%28SVG%20Tool%29选项.md)
