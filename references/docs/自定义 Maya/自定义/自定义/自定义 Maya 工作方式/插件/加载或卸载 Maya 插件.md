# 加载或卸载 Maya 插件

加载或卸载插件

1. 选择窗口 > 设置/首选项 > 插件管理器(Windows > Settings/Preferences > Plug-in Manager)。

2. 请执行下列任一操作：

  - 启用插件旁边的“已加载”(Loaded)选项来加载插件。

  - 启用“自动加载”(Auto load)选项可始终在启动时加载插件。

  - 单击插件旁边的 ![图：单击插件旁边的 图标可以查看“插件信息”(Plug-in Information)窗口，并查找关于插件的附加信息，例如版…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-DDE3393B-018E-427A-AB8A-28059976D8DA.png) <!-- baize:img-hook downloaded=false reason="正文 503 字 ≥300，非承重" --> 图标可以查看“插件信息”(Plug-in Information)窗口，并查找关于插件的附加信息，例如版本号及其添加的任何 MEL 命令。

    **注**

    如果要加载插件的 Maya 版本在日期上早于编译插件时所面向的目标 Maya 版本，则无法加载该插件。例如，在 Maya 5 中无法使用通过 Maya 6 API 编译的插件。可以在

    “插件信息”(Plug-in Information)

    窗口中查看

    “适用于 API 版本”(For API Version)

    编号。

## 强制卸载当前场景中正在使用的插件

如果尝试卸载在当前场景中提供功能的插件（例如，场景中包含插件提供的节点类型），系统将提示您强制移除插件。这样会将场景中该插件提供的所有节点都转化为“未知”节点类型。即使重新加载插件，这些节点仍保持“未知”节点类型。

## 相关主题

- [支持的文件格式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3FDB6F01-1830-4AB3-BB91-287A64A269A6)

- [插件管理器](插件管理器.md)

- [Maya 随附插件列表](Maya%20随附插件列表.md)
