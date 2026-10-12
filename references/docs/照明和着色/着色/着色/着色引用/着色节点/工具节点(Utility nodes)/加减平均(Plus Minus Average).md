# 加减平均(Plus Minus Average)

请参见[使用“加减平均”工具](../../../渲染节点工具/使用“加减平均”%28Plus%20Minus%20Average%29工具.md)。

#### 运算(Operation)

显示一个弹出菜单，您可以从中选择一个运算符

#### 无运算(No operation)

在不做任何更改的情况下，将 Input1 属性的值复制到输出属性中。

#### 求和(Sum)

将输入列表中的多个值相加，如以下公式中所示：

输出 = Input1 + Input2 +... + InputN

#### 相减(Subtract)

计算列表中一个元素与另一个元素之间的差值，如以下公式中所示：

输出 = Input3D[1] - Input3D[2]

例如，如果要从多属性节点的“Input3D[2]”中减去“Input3D[1]”，请在“连接编辑器”(Connection Editor)中单击鼠标右键进行必要的连接，然后选择“相减”(Subtract)。

#### 平均(Average)

将每个输入属性的值相加，所得结果再除以输入属性的数量，如以下公式所示：

输出 = (Input1 + Input2 + ... + InputN) /N

其中 N 为输入属性的数量。

例如，如果列表中存在 7 个输入值，则先将列表中介于 1 到 7 之间的每个输入的值相加，所得结果再除以 7。

#### Input1D

由单值连接组成的元素的列表。可以对列表中的值进行相加、相减或求平均值，具体取决于所选的“运算”(Operation)。

#### Input2D

由双值连接组成的元素的列表。可以对列表中的值进行相加、相减或求平均值，具体取决于所选的“运算”(Operation)。

#### Input3D

由三值连接组成的元素（例如颜色）的列表。可以对列表中的值进行相加、相减或求平均值，具体取决于所选的“运算”(Operation)。

**注**

提示：

为节点指定有意义的名称有助于记住其功能。例如，将第一个“multiplyDivide”节点重命名为 PowerSquare，将“plusMinusAverage”节点重命名为 SumComponents，将第二个“multiplyDivide”节点重命名为 PowerSquareRoot。
