# 应用“属性编辑器”(Attribute Editor)模板

“属性编辑器”(Attribute Editor)模板用于自定义如何在[属性编辑器(Attribute Editor)](../../../属性编辑器%28Attribute%20Editor%29.md)中显示属性。

**注**

重要：

需要具有管理员权限才能将

“属性编辑器”(Attribute Editor)

模板保存在 Maya 安装目录的 scripts\AETemplates 文件夹中。

应用“属性编辑器”(Attribute Editor)模板的步骤

1. 将模板复制到以下位置之一：

  - Maya 安装目录中的 scripts\AETemplates 文件夹。

    这是用于“属性编辑器”(Attribute Editor)模板的默认目录。

  - 选择的文件夹。

    您可以使用 MAYA_CUSTOM_TEMPLATE_PATH 环境变量指定自定义模板的路径和位置。设置此变量并在“属性编辑器”(Attribute Editor)中选择“显示 > 设置当前视图”(Show > Set Current View)或“显示 > 设置全局视图”(Show > Set Global View)以后，Maya 将查询指定的位置。如果此变量未解析或未设置，Maya 将搜索默认目录。

  如果您选择指定模板的路径和位置，则将按顺序搜索目录。在此搜索过程中，特定于节点的模板优先于节点类型模板。如果在第一个目录中无法找到特定于节点的模板，Maya 会查找节点类型模板，以便于使用。如果没有自定义模板位于目录中，Maya 会在下一个目录中重复执行步骤，直到找到一个模板或者已搜索所有目录。

  如果两种类型的模板在目录中都存在（如 AEblinnTemplate.xml 和 AEblinn.blinn1Template.xml），Maya 会将 AEblinn.blinn1Template.xml 用于名为 **blinn1** 的 **blinn** 节点，将 AEblinnTemplate.xml 用于其他 **blinn** 节点。

2. 选择对象或节点。

3. 在“属性编辑器”(Attribute Editor)中，从选择以下选项之一后显示的列表中拾取视图：

  - 显示 > 设置全局视图(Show > Set Global View)

    将选定视图应用于具有相同自定义模板视图的所有节点类型。例如，如果您有一个名为 Animation 的视图，并且您从**“设置全局视图”(Set Global View)**列表中选择了该视图，则具有使用名为 Animation 的视图的自定义模板的所有节点类型将按照 Animation 视图所定义的那样显示属性。

  - 显示 > 设置当前视图(Show > Set Current View)

    将选定视图只应用于选定的节点类型。

  当选择某视图时，该视图的名称及其模板的名称将在“属性编辑器”(Attribute Editor)的标签行中显示。

  ![图：当选择某视图时，该视图的名称及其模板的名称将在“属性编辑器”(Attribute Editor)的标签行中显示。 对于节…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-DF6D1B4F-BD33-4F08-936F-008FC2854E85.png) <!-- baize:img-hook downloaded=false reason="正文 1504 字 ≥300，非承重" -->

  对于节点类型模板（<NodeType>）和特定于节点的模板（<NodeType>.<节点名称>），模板名称将采用不同的格式。

  **注**

  提示：

  通过关闭

  “显示 > 显示视图标签”(Show > Show View Labels)

  可以隐藏标签行。

**注**

如果为某节点类型选定的全局视图未在其自定义模板中定义，则

“属性编辑器”(Attribute Editor)

将使用该节点类型的默认模板。要获得以上效果，必须在

“显示”(Show)

菜单中启用

“如果无全局视图，则显示默认视图”(Show default if no global view)

。如果节点类型不具有自定义模板，则

“属性编辑器”(Attribute Editor)

将使用上一次应用的自定义模板视图。

## 相关主题

- [针对节点类型创建“属性编辑器”(Attribute Editor)模板](针对节点类型创建“属性编辑器”%28Attribute%20Editor%29模板.md)

- [针对特定节点创建“属性编辑器”(Attribute Editor)模板](针对特定节点创建“属性编辑器”%28Attribute%20Editor%29模板.md)

- [刷新“属性编辑器”(Attribute Editor)模板](刷新“属性编辑器”%28Attribute%20Editor%29模板.md)

- [“属性编辑器”(Attribute Editor)菜单](../../“属性编辑器”%28Attribute%20Editor%29菜单.md)
