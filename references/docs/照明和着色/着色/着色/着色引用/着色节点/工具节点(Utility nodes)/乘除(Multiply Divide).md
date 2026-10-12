# 乘除(Multiply Divide)

请参见[使用乘除工具](../../../渲染节点工具/使用“乘除”%28Multiply%20Divide%29工具.md)。

#### 运算(Operation)

显示可从中选择运算符的弹出菜单。

#### 无运算(No operation)

将“Input1”属性的值复制到输出属性，且不会做任何更改。

例如，如果“Input 1”是“棋盘格”(Checker)纹理，而“Input 2”是“凹陷”(Crater)纹理，则选择“无运算”(No Operation)时，仅会渲染“棋盘格”(Checker)纹理的属性。

![图：将“Input1”属性的值复制到输出属性，且不会做任何更改。 例如，如果“Input 1”是“棋盘格”(Checker)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-2CDC3B18-6E00-41F8-9933-16306656DB07.png) <!-- baize:img-hook downloaded=false reason="正文 792 字 ≥300，非承重" -->

#### 相乘(Multiply)

按以下公式所示，将“Input1”属性和“Input2”属性相乘：

输出 = Input1 x Input2

#### 相除(Divide)

按以下公式所示，将“Input1”属性除以“Input2”属性：

输出 = Input1/Input2

在以下示例中，“Input 1”纹理将除以对“Input 2”纹理所做的更改。

![图：按以下公式所示，将“Input1”属性除以“Input2”属性： 输出 = Input1/Input2 在以下示例中，“…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-860FBCF7-FE4C-4D1C-BA59-D4FDE83126A9.png) <!-- baize:img-hook downloaded=false reason="正文 792 字 ≥300，非承重" -->

#### 幂(Power)

将输出设定为等于“Input 1”的“Input 2”幂。请看以下示例：

![图：将输出设定为等于“Input 1”的“Input 2”幂。请看以下示例： 它通过增加选择数字的幂值或计算平方根，求出表达…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-83B30D78-55EE-44E8-B008-CAE51680F4F4.png) <!-- baize:img-hook downloaded=false reason="正文 792 字 ≥300，非承重" -->

它通过增加选择数字的幂值或计算平方根，求出表达式的值。增加幂值意味着使某个数字按给定的次数与自身相乘，如下所示：

2^3 = 2 x 2 x 2

计算数字平方的命令为：

power (value, 2.0)

数学公式为：

幂 = 值^2

计算平方根的公式为：

幂 = sqrt（值）

如果要将分量的值相乘两次，则应将“Input1”设定为表示颜色（可以使用纹理映射它），然后将“Input2”的所有三个分量设定为 2.0。由于输入包括两种颜色，因此，可以使用单个分量值的颜色或所有三个分量的值。

也可以按如下所示将“Input2”设定为 0.5，以求出数字的平方根：

```text
Output = power (input1, input2)
```

在数学术语中，这可写为 input1^input2。

请参见[幂](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-DBD3F3B4-AE68-49B1-B215-34F74782BA63.htm#WS73099CC142F48755-3D114B7511812357EFE-5AAB)运算符示例。

#### Input1

向“乘除”(Multiply Divide)显示的两个参数中的第一个参数。

#### Input2

向“乘除”(Multiply Divide)显示的两个参数中的第二个参数。
