# 为自定义节点创建 lookdev 视图模板

可以为自定义着色节点创建 Lookdev 视图模板，以便它们以类似的 Lookdev 视图也显示在特性编辑器中。

修改 AE<节点类型>Template.xml 以包括外观制作视图定义，并将该文件放置在安装目录的 ../.scripts/AETemplates 文件夹中。有关如何添加 Lookdev 视图定义的示例，请参见 AEblinnTemplate.xml。请参考以 <view name='Lookdev' template='AEblinn'> 开头的部分。

您还可以将模板文件保存到所选的其他位置，然后使用 MAYA_CUSTOM_TEMPLATE_PATH 环境变量指定路径。请参见[“属性编辑器”(Attribute Editor)模板](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-592870D2-92E6-44CC-AE54-2F79EC43076A)。

有关自定义的属性编辑器模板的详细信息，请参见[自定义的属性编辑器模板](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C386F366-A1F9-49E1-938D-45149F79D354)。

**注**

除了为自定义着色节点创建 Lookdev 视图模板外，还可以通过自定义为每种节点类型显示的属性列表，确定节点显示的方式。详细信息请参见[在节点编辑器中自定义节点属性列表](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C1E02C84-8CCF-4B3D-B080-F4A379AD1FCB)。

AE<NodeType>Template.xml 属性编辑器模板文件确定如何显示特性编辑器和属性编辑器。

NE<NodeType>Template.xml 节点编辑器模板文件确定如何显示节点。例如，NEMyCustomNodeTemplate.xml 确定在 Hypershade 和节点编辑器中为 MyCustomNode 显示的属性列表。在 Hypershade 中，首次创建节点时，MyCustomNode 显示有属性的此自定义列表。在 Hypershade 和节点编辑器中，MyCustomNode 在视图模式 4 下显示有属性的此自定义列表。

## 相关主题

- [“属性编辑器”(Attribute Editor)模板](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-592870D2-92E6-44CC-AE54-2F79EC43076A)

- [“节点编辑器”(Node Editor)模板](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9C223EB6-5926-44A3-8F0A-B0AF4172D3AA)
