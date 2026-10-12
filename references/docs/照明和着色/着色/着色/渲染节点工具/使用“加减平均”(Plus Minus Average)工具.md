# 使用“加减平均”(Plus Minus Average)工具

使用此工具可以在给定的输入属性列表中进行相加、相减或求平均值操作。“加减平均”(Plus Minus Average)工具包含三个部分：两个或两个以上的输入属性、要应用于这些输入属性的运算符以及控制操作结果的输出属性。

有关“加减平均”(Plus Minus Average)工具的描述，请参见[加减平均](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-7799860E-2024-4261-9C76-B94AB6B28381.htm)。

创建 plusMinusAverage 工具节点

1. 请执行下列任一操作：

  - 在 [Hypershade 窗口](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-252707EC-4AAF-4D3F-9600-804F783652B7.htm)的“创建”(Create)选项卡中找到此工具（在“工具”(Utilities)下）。

  - 请参见[在“节点编辑器”中创建节点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6217CD2A-0CDB-41C4-AC47-BD5169BE070C)。

创建后，可以基于一个数字使用“加减平均”(Plus Minus Average)与同一个属性进行多次连接。属性名称的最后部分有一个在方括号之内的数字。

“Input3D[0]”指定第一个连接与“Input3D”属性连接，“Input3D[1]”指定第二个连接与该属性连接，“Input3D[2]”指定第三个连接与该属性连接，依此类推。第一个连接始终指定为 0。每个连接将获取其自身的 ID 编号。例如，灰泥属性的“OutColor”由一组三个值组成，这三个值可以连接到“Input3D”值，而不是“Input 2D”值或“Input1D”值。

**注**

提示：

可以将连接排列到较大或较小数字，而不会干扰列表中的其他连接，此外还可以像对其他连接一般断开连接。
