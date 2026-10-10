# “属性编辑器”(Attribute Editor)模板

## “属性编辑器”(Attribute Editor)模板

属性编辑器模板确定如何在属性编辑器中显示属性。

例如，可以创建不同的视图（如建模、动画和渲染），其中每个都显示属性的不同子集。请参见[自定义属性编辑器模板](自定义“属性编辑器”%28Attribute%20Editor%29/自定义“属性编辑器”%28Attribute%20Editor%29模板.md)和[属性编辑器模板的各个部分](自定义“属性编辑器”%28Attribute%20Editor%29/自定义“属性编辑器”%28Attribute%20Editor%29模板/“属性编辑器”%28Attribute%20Editor%29模板的各个部分.md)。

模板采用 .xml 格式。可以为特定的节点类型（例如 phong）或特定的节点（例如 phong1）创建属性编辑器模板。可以为 Maya 节点或您自己的自定义节点自定义属性编辑器。

### 文件名和位置

若要为节点类型创建属性编辑器模板，请将模板另存为 AE<NodeType>Template.xml。

若要为特定的节点创建属性编辑器模板，请将模板另存为 AE<NodeType>.<NodeName>Template.xml。

请参见[为节点类型创建属性编辑器模板](自定义“属性编辑器”%28Attribute%20Editor%29/自定义“属性编辑器”%28Attribute%20Editor%29模板/针对节点类型创建“属性编辑器”%28Attribute%20Editor%29模板.md)和[为特定的节点创建属性编辑器模板](自定义“属性编辑器”%28Attribute%20Editor%29/自定义“属性编辑器”%28Attribute%20Editor%29模板/针对特定节点创建“属性编辑器”%28Attribute%20Editor%29模板.md)。

默认情况下，可在安装目录的 ../scripts/AETemplates 文件夹中找到属性编辑器模板。也可以通过设置 MAYA_CUSTOM_TEMPLATE_PATH 覆盖此默认位置。可以将环境变量设置为多个路径。

Maya 按以下顺序搜索 AE 模板。使用找到的第一个模板：

  MAYA_CUSTOM_TEMPLATE_PATH

2. ../scripts/AETemplates

### Hypershade 中的属性编辑器和特性编辑器

在 Hypershade 属性编辑器中，默认情况下 Maya 着色器显示在 Lookdev 视图中。这是因为 Lookdev 视图定义存在于每个 Maya 着色节点的对应 AE<NodeType>Template.xml 中。

请参见[在 Hypershade 特性编辑器中查看属性](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-51DFC2E3-7D78-41C7-BE9A-489C181D8DF5)和[使用 Hypershade 的外观开发](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-447C9ADA-A285-483E-A93D-6ED1B2792D5F)。

若要在 Hypershade 特性编辑器中类似的外观制作视图中显示自定义着色节点，请编辑 AE<节点类型>Template.xml 以包括外观制作视图定义，并将 .xml 文件保存在 ../scripts/AETemplates 文件夹（或者由 MAYA_CUSTOM_TEMPLATE_PATH 设置的文件夹）中。

如果在对应节点的 AE<NodeType>Template.xml 中不存在 Lookdev 视图，则在特性编辑器中显示其属性编辑器布局。
