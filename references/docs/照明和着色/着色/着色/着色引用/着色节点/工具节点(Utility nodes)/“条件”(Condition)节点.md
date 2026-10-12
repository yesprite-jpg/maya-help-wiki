# “条件”(Condition)节点

请参见[使用条件工具](../../../渲染节点工具/使用“条件”%28Condition%29工具.md)。

“条件”(Condition)工具像比较“第一项”(First Term)和“第二项”(Second Term)中的值一样简单。基于此对比结果，您可以执行以下操作（例如）更改对象的颜色或纹理。

例如，如果“第一项”(First Term)小于“第二项”(Second Term)，则对象的结果颜色（“OutColor”）为“为真时的颜色”(Color If True)，且“第一项”(First Term)不小于“第二项”(Second Term)时，将出现“为假时的颜色”(Color If False)。

#### 第一项(First Term)

表示条件的第一终结点。

#### 第二项(Second Term)

表示条件的第二终结点。

#### 运算(Operation)

显示可从中选择运算符的下拉列表。运算符包括：“相等”(Equal)、“不等于”(Not Equal)、“大于”(Greater Than)、“大于或等于”(Greater or Equal)、“小于”(Less Than)、“小于或等于”(Less or Equal)。

#### 为真时的颜色(Color If True)

条件为 true 时输出的颜色或纹理。

#### 为假时的颜色(Color If False)

条件为 false 时输出的颜色或纹理。

#### 输出颜色(Out Color)

含有获得的结果的输出属性。仅在“连接编辑器”(Connection Editor)中可用。

**注**

提示：

由于还可以映射所有输入属性，因此可以在两个纹理之间切换，例如，将它们连接至

“为真时的颜色”(Color If True)

和

“为假时的颜色”(Color If False)

。
