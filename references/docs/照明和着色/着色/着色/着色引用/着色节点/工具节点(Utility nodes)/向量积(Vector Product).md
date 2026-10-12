# 向量积(Vector Product)

将一个向量与另一个向量或一个矩阵相乘。“向量积”(Vector Product)节点包含三个部分：两个输入属性，一个应用于两个输入属性的运算符，和一个包含结果的输出属性。

- 向量是具有方向（X、Y 和 Z）以及幅值的属性（如颜色）的数量。

- 矩阵是一组互相连接的属性。这些属性组合到一起可创建单一实体。

在“创建”(Create)选项卡中找到该工具（请参见[“创建”(Create)选项卡](../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)）。

若要使用该工具，请参见[使用向量积工具](../../../渲染节点工具/使用“向量积”%28Vector%20Product%29工具.md)。

#### 运算(Operation)

显示可从中选择运算符的下拉列表。以下示例基于 Input 1 作为“栅格”(Grid)纹理，而 Input 2 作为“大理石”(Marble)纹理。“运算”(Operation)设置为“向量矩阵积”(Vector Matrix Product)。

![图：显示可从中选择运算符的下拉列表。以下示例基于 Input 1 作为“栅格”(Grid)纹理，而 Input 2 作为“大…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-643ACB13-9F02-4519-A194-2A17A8C66030.png) <!-- baize:img-hook downloaded=false reason="正文 641 字 ≥300，非承重" -->

#### 无运算(No operation)

将 Input1 属性的值复制到输出，而不进行任何更改。

#### 点积(Dot Product)

由两个输入向量的点积产生的单一分量值。会将点积的值复制到产生的向量的三个分量。

#### 叉积(Cross Product)

两个输入向量的结果。

#### 向量矩阵积(Vector Matrix Product)

通过将“Input1”属性与“矩阵”(Matrix)属性相乘，生成一个向量，如下面的公式中所示：

*Outvector = Input x Matrix*

#### 点矩阵积(Point Matrix Product)

通过将“Input1”属性与“矩阵”(Matrix)属性相乘，生成一个点，如下面的公式中所示：

*Output = Input x Matrix*
