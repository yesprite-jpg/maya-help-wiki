# 针对特定节点创建“属性编辑器”(Attribute Editor)模板

创建节点特定的“属性编辑器”(Attribute Editor)模板

1. 使用自行选择的 XML 或纯文本编辑器创建模板。请参见[属性编辑器模板的各个部分](“属性编辑器”%28Attribute%20Editor%29模板的各个部分.md)。

  **注**

  提示：

  也可以使用

  “属性编辑器”(Attribute Editor)

  模板生成器创建自定义模板。请从

  http://area.autodesk.com/bonus_tools

  联机下载此 Bonus Tool，或者选择

  “帮助 > Maya 资源和工具 > 下载 Bonus Tools”(Help > Maya Resources and Tools > Download Bonus Tools)

  。

2. 将模板另存为 AE<NodeType>.<NodeName>Template.xml，其中 AE 和 Template 指定相应文件作为“属性编辑器”(Attribute Editor)模板，NodeType 为节点类型，NodeName 为创建模板所针对的特定节点。

  例如，名为 **blinn1** 的 **blinn** 节点的模板命名为 AEblinn.blinn1Template.xml。

### 相关主题

- [应用属性编辑器模板](应用“属性编辑器”%28Attribute%20Editor%29模板.md)

- [刷新“属性编辑器”(Attribute Editor)模板](刷新“属性编辑器”%28Attribute%20Editor%29模板.md)

- [创建自定义属性控件](../在属性编辑器模板中使用回调/创建自定义属性控件.md)
