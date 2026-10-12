# 使用“条件”(Condition)工具

该条件节点是分支工具。如果逻辑表达式为 true，则其执行一个操作，如果为 false，则执行其他操作。

根据设置的条件，条件将比较 A 和 B 中的值，了解 A 中的值是否大于、小于、等于、小于、小于或等于、大于或等于或不等于 B 中的值，从而得出一个结果。

可以合并着色器网络中的“条件”(Condition)工具，以便能够在一组环境中以同一种方式操作，而在另外一组不同环境中以不同的方式操作。例如，您可以创建双面着色曲面（请参见[创建双面着色曲面](../关于着色和纹理曲面/创建双面着色曲面.md)）。

如以下示例所示，节点需要一个逻辑运算符(“运算”(Operation)）以及两个选择值(“第一项”(First Term)和“第二项”(Second Term)）:

在本例中，如果 A 中的值不等于 B 中的值，则在“OutColor”中选择“为真时的颜色”(Color If True)。如果 A 中的值等于 B 中的值，则在“OutColor”中选择“为假时的颜色”(Color If False)。

要创建条件工具节点

1. 请执行下列任一操作：

  - 在 [Hypershade 窗口](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-252707EC-4AAF-4D3F-9600-804F783652B7.htm)的“创建”(Create)选项卡中找到此工具。

  - 请参见[在“节点编辑器”中创建节点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6217CD2A-0CDB-41C4-AC47-BD5169BE070C)。

以下内容显示了某些正在使用的“条件”(Condition)工具示例：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-6CDF855D-D91D-4B33-BC19-C40A085BC0AD.png) <!-- baize:img-hook downloaded=false reason="正文 943 字 ≥300，非承重" -->

## 示例

将“条件”(Condition)工具映射到四个纹理

1. 创建一种材质，将其指定给一个对象，然后将“条件”(Condition)工具映射到材质的“颜色”属性。

2. 根据需要调整材质的属性。

3. 在“属性编辑器”(Attribute Editor)中，选择“条件节点”(condition node)选项卡，然后设定以下内容:

  - 将纹理映射到“第一项”(First Term)。

    该纹理表示“第二项”(Second Term)的纹理范围。

  - 将纹理映射到“第二项”(Second Term)。

    该纹理表示覆盖范围的图案。

  - 将纹理映射到“为真时的颜色”(Color If True)。

    该纹理表示曲面颜色。

  - 将纹理映射到“为假时的颜色”(Color If False)。

    该纹理表示叠加纹理的颜色。

  - 更改每个纹理的属性，并根据需要使用纹理放置对象调整对象上的纹理。

  - 使用[运算](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-C1DEE9BC-375C-404C-ABF7-79E9321BE5F8.htm#WS73099CC142F48755-3D114B7511812357EFE-595F)下拉列表项查看纹理之间的过渡。

    **注**

    提示：

    将

    “运算”(Operation)

    选项设置为

    “大于”(Greater Than)

    或

    “小于”(Less Than)

    以查看组合结果。
