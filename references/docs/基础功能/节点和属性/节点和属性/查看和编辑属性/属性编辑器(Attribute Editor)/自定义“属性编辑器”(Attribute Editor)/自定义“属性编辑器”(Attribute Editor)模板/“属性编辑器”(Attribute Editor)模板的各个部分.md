# “属性编辑器”(Attribute Editor)模板的各个部分

自定义“属性编辑器”(Attribute Editor)模板与 Maya 资产模板使用相同的 XML 结构，并且包含许多相同的元素。下图中亮显了属性编辑器(Attribute Editor)模板的主要部分。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-06995BA2-EA68-41BB-AA04-9A10C6020BE7.png) <!-- baize:img-hook downloaded=false reason="正文 414 字 ≥300，非承重" -->

## 属性声明

要在视图中使用某个属性，必须在自定义“属性编辑器”(Attribute Editor)模板的第一部分中声明该属性。您可以根据需要声明任意数量的属性。

## 视图定义

您可以在模板中包括任意数量的视图。您可以加载自定义视图，方法是在“属性编辑器”(Attribute Editor)中选择“显示 > 设置当前视图”(Show > Set Current view)或“显示 > 设置全局视图”(Show > Set Global View)，然后从显示的列表中选择所需视图的名称。

## 回调

回调链接到属性，且可用于创建自定义属性控件或运行影响属性编辑器(Attribute Editor)布局和场景的脚本。请参见[在属性编辑器模板中使用回调](../在属性编辑器模板中使用回调.md)。

## 相关主题

- [资产模板](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F2616A37-4119-428D-BE50-9DB9C43796EE)

- [资产模板的各个部分](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D2DF8C97-0AFE-4EDE-938C-B99BF1E46B6E)
