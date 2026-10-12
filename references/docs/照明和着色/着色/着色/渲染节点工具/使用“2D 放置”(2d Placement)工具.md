# 使用“2D 放置”(2d Placement)工具

有关“2D 放置”(2d Placement)工具的描述，请参见 [2D 放置](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-94070C7E-C550-42FD-AFC9-FBE82B173B1D.htm)。

可以使用 place2dTexture 节点的“属性编辑器”(Attribute Editor)中的数字精度重新定位 2D 纹理，也可以使用 Maya 的“纹理放置工具”(Texture Placement Tool)以交互方式重新定位纹理或标签。

以交互方式定位二维纹理

1. 在“Hypershade”中，单击连接至要重新定位的纹理的 place2dTexture 样例。

  将显示 place2dTexture 的“属性编辑器”(Attribute Editor)

  **注**

  提示：

  如果看不到 place2dTexture 样例，请执行以下操作：

  - 选择纹理样例，然后单击“Hypershade”工具栏上的“输入连接”(Input Connections)按钮。

  - 如果不存在 place2dTexture 样例，说明它已被删除或未创建（因为默认情况下已禁用自动创建）。必须添加一个节点（请参见[在 Hypershade 中创建和连接节点](../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/在%20Hypershade%20中创建和连接节点.md)），然后将它连接到纹理（请参见[通过拖动来连接节点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-591E9EB3-7B11-456D-92C2-0A6B470079FC)），再重新定位它。

2. 执行下列操作之一：

  - 在“属性编辑器”(Attribute Editor)中更改属性的值。有关这些属性的详细描述，请参见 [2D 放置](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-94070C7E-C550-42FD-AFC9-FBE82B173B1D.htm)。

  - 对于 NURBS，单击“属性编辑器”(Attribute Editor)中的“交互式放置”(Interactive Placement)按钮，以使用“纹理放置工具”(Texture Placement tool)。若要设置“纹理放置工具”(Texture placement tool)，请参见[纹理放置与标签映射](../关于着色和纹理曲面/纹理/纹理映射/纹理放置与标签映射.md)。

    **注**

    提示：

    可能很难只通过使用操纵器来放置纹理。可同时使用操纵器和“属性编辑器”(Attribute Editor)来获得所需结果。
