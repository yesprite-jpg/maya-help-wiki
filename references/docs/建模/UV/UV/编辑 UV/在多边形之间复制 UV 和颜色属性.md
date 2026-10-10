# 在多边形之间复制 UV 和颜色属性

可以使用“网格 > 剪贴板操作”(Mesh > Clipboard Actions)功能，在不同多边形网格的面之间复制 UV、着色器和逐顶点颜色属性。当修改了多边形网格而无法进一步修改 UV 时，在网格之间复制 UV 属性的功能很有用。该功能还可用于在具有不同拓扑的网格之间复制属性。

只能在顶点数相当的多边形面之间复制属性。复制的 UV 属性将置于一个单独的壳中。

在多边形之间复制 UV、着色器或逐顶点颜色数据

1. 选择您要复制其属性的多边形面，然后选择“网格 > 剪贴板操作 > 复制属性”(Mesh > Clipboard Actions > Copy Attributes) > ![图：选择您要复制其属性的多边形面，然后选择“网格 剪贴板操作 复制属性”(Mesh Clipboard Actions Co…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 605 字 ≥300，非承重" -->。

2. 在“复制属性选项”(Copy Clipboard Options)窗口中，设置要复制的属性（“UV”、“着色器”(Shader)和“颜色”(Color)），然后单击“应用并关闭”(Apply and Close)。

  **注**

  可以设置这些选项，以便将一个或多个属性复制到剪贴板。

3. 选择要将属性复制到的多边形面，然后选择“网格 > 剪贴板操作 > 粘贴属性”(Mesh > Clipboard Actions > Paste Attributes)。

  先前复制的属性将粘贴到所选面上。

  **注**

  也可以通过选择

  “网格 > 剪贴板操作 > 清空剪贴板”(Mesh > Clipboard Actions > Clear Clipboard)

  ，清空剪贴板中包含的属性。

## 相关主题

- [复制属性选项(Copy Attributes Options)](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/“网格”%28Mesh%29菜单/复制属性选项%28Copy%20Attributes%20Options%29.md)

- [在多边形面中生成洞](../../../多边形建模/多边形建模/编辑多边形/修改多边形网格/在多边形面中生成洞.md)
