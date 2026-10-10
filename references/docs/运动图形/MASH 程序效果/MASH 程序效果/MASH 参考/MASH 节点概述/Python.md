# Python

允许您创建 Python 脚本以影响 MASH 网络。创建新的 Python 节点时，默认脚本将自动继承编辑器，该编辑器将 MASH 网络数据读取至一个“md”的类中。

查询属性列表如下所示：

- position

- scale

- rotation

- id

- visibility

- angular velocity

- vector velocity

例如，若要查询 MASH 网络中第五个对象的位置，则可使用以下代码：

```text
md.position[5]
```

您还可以查询特定的轴。例如，若要仅查询 x 轴，则可使用以下代码：

```text
md.position[5].x
```

**注**

ID 和 Visibility 数组将作为双精度存储。

用于编写的属性列表如下所示：

- outPosition

- outScale

- outRotation

- outId

- outVisibility

- angularVelocity

- velocityVec

- angularVelocityVec

例如，若要设置第五个对象的 Y 位置，则可以使用以下代码：

```text
outPosition[5].y = 5
```

或者，若要使同一对象不可见，请执行以下操作：

```text
outVisibility[5] = 0
```

其中，值 1 表示可见；值 0 表示不可见。

## 辅助对象函数

以下是列表中的内置辅助对象函数以使特定任务的速度更快。

#### count()

返回 MASH 点数。

#### getFrame()

返回当前帧编号。

#### getFalloffsCount

返回数字的衰减对象连接到该 Python 节点。

#### getFalloff(int index)

从指定的衰减对象中返回强度列表。

例如，若要查询第一个衰减对象的强度数组，则可使用以下代码：

```text
 fallofs=md.getFalloff(0)
```

然后，可以使用以下代码将衰减强度应用于点位置：

```text
for i in range(count):
md.outPosition[i].x=md.position[i].x*fallofs[i]
md.outPosition[i].y=md.position[i].y*fallofs[i]
md.outPosition[i].z=md.position[i].z*fallofs[i]
```

#### getVectorArray(string channelName)、getDoubleArray(string channelName)、getIntArray(string channelName)

返回在参数中指定作为相关类型数组的通道的值。

#### setVectorArray(string channelName, array)、setDoubleArray(string channelName, array)、setIntArray(string channelName, array)

设置在参数中使用指定数组值来指定的通道的值。

#### getMatrix(int id)

返回 ID 指定的点的变换矩阵。

#### setMatrix(matrix, int id)

将指定的矩阵设置为 ID 指定的点。

## 高级函数

Python 节点具有 inputPoints 和 outputPoints 属性允许添加手动 Waiter 和 MASH_Repro 之间的节点。利用这些属性，您可以访问以下数组。

输入

- color

- uvTile

- frame

- isAnimated

- velocity

输出

- outColor

- outUvTile

- outFrame

- outIsAnimated

- outVelocity

## 强度

#### 强度(Strength)

同时减弱对所有点的节点效果。

#### 随机强度(Random Strength)

按随机顺序平滑地减弱所有点的节点效果。

#### 阶跃强度(Step Strength)

每次禁用一个点的节点效果。

#### 强度贴图(Strength Map)

确定输入文件（2D 纹理、动画纹理等）来控制该节点的效果的形状。

#### 贴图投影轴(Map Projection Axis)

确定投影“强度贴图”(Strength Map)时所沿的轴。

#### 贴图辅助对象(Map Helper)

显示用于在场景中交互放置“强度贴图”(Strength Map)的对象。可以在该字段上单击鼠标右键来创建新的辅助对象（平面）（如果不存在）。还可以使用鼠标中键将网格拖入此字段，或者单击鼠标右键连接选定网格。如果网格已连接，还可以单击鼠标右键来断开其连接或者将其显示在大纲视图中。

**注**

为获得最佳结果，请将相同的纹理指定给

“强度贴图”(Strength Map)

和

“贴图辅助对象”(Map Helper)

（在创建新的辅助对象时将自动执行此操作）。
