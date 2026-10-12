# 在 Hypershade 特性编辑器中查看属性

在特性编辑器的模板视图（为每个着色节点提供最常用属性的优化布局）中查看着色节点属性。

使用 Hypershade 时，可以在特性编辑器中查看着色节点的属性。通过以下两种方式查看着色节点属性：经典的属性编辑器布局或 Lookdev 模板视图。后者是针对 lookdev 工作流优化的模板。它具有更简单的布局，仅列出最常用的属性，使您可以更轻松地查找和调整着色节点属性。

特性编辑器标签行指示 View:Lookdev，表明您正在 Lookdev 模式下查看节点属性。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-AE13B620-EC76-4140-9B12-1EB01481DC99.png) <!-- baize:img-hook downloaded=false reason="正文 672 字 ≥300，非承重" -->

**注**

如果 Lookdev 视图对您选定的节点不可用，则将显示其

属性编辑器

布局。

每个 Maya 着色节点的对应 AE<节点类型>Template.xml（在安装目录的 ../scripts/AETemplates 文件夹中）中定义了外观制作视图模板布局。请参见[“属性编辑器”(Attribute Editor)模板](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-592870D2-92E6-44CC-AE54-2F79EC43076A)。

## 当前选择和特性编辑器

选择多个着色器，特性编辑器中将显示所有的着色节点，每个着色节点都位于单独的选项卡中。

选择多个对象，特性编辑器中将显示应用于选定对象的所有着色节点，每个着色节点都位于单独的选项卡中。

## 预设

预设受特性编辑器支持，正如它们受属性编辑器支持那样。有关保存和重用预设的详细信息，请参见[保存和重用属性预设](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B90EF3C9-EFB8-4BBC-B9A5-69F7EC86B3C3)。

## 扩展属性和特性编辑器

如果将扩展属性添加到 Maya 节点，则通过自定义节点对应的 AE<NodeType>Template.xml 文件并将 MAYA_CUSTOM_TEMPLATE_PATH 环境变量设置为指向模板文件的位置，您可以将这些扩展属性包含在“属性编辑器”(Property Editor)中。
