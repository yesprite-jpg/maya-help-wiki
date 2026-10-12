# 使用“反转”(Reverse)工具

有关“反转”(Reverse)工具的描述，请参见[反转(Reverse)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-EECA80A5-FD6F-4A41-87FF-05461A2BEB2D.htm)。

在下图中，“大理石”(Marble)纹理是反转的。这意味着从 1 中减去 0.9 得出颜色值 0.1。该结果可以按以下公式表示：

```text
Output = 1 - Input
```

可以为“输入”(Input)输入值以获得您在“属性编辑器”(Attribute Editor)中所需的效果。“反转”(Reverse)可输出和接受单个组件的值、两个组件的值以及所有这三个组件的值。

反转属性

1. 将纹理映射到材质的属性，如“颜色”(Color)。

2. 创建“反转”(Reverse)节点。

3. 在 Hypershade 工作区中，将反转”(Reverse)节点的“输出”(Output)属性连接到要反转的纹理节点上的属性。

  如果默认情况下未显示要反转的属性，则选择节点并单击 3，以便在完全模式下显示节点。在过滤器字段中输入搜索项。在本例中，输入了 color 以简化节点，以便仅显示其名称含有 color 的属性。

  有关节点视图模式的详细信息，请参见[在节点编辑器和 Hypershade 中更改视图模式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8BB2DBCA-FB8B-4F7A-A4C3-1BACE18E5879)。

4. 创建另一个“反转”(Reverse)节点，并在必要时重复，具体取决于要反转的属性数。

  ![图：创建另一个“反转”(Reverse)节点，并在必要时重复，具体取决于要反转的属性数。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-D40DCEAE-D16C-4F0F-9E7B-7DA310AFCE35.png) <!-- baize:img-hook downloaded=false reason="正文 609 字 ≥300，非承重" -->

5. 按照上面的示例，在“大理石”(Marble)纹理的属性编辑器中，单击“填充颜色”(Filler Color)旁边的框以打开“反转”(Reverse)节点特性编辑器，然后更改“输入”(Input)属性值。试验不同的值。以下显示了一些示例结果。

  ![图：按照上面的示例，在“大理石”(Marble)纹理的属性编辑器中，单击“填充颜色”(Filler Color)旁边的框以打…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-923F6D9F-AE54-4B27-A7D6-FEE28E6BAD7E.png) <!-- baize:img-hook downloaded=false reason="正文 609 字 ≥300，非承重" -->
