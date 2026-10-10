# 在 SynColor 模式下使用 OCIO 配置文件

旧版 SynColor 颜色管理系统支持使用 OCIO v1 配置文件。但是，最好使用默认的 OCIO 颜色管理系统，该系统既支持 v1 配置又支持 v2 配置。

如果仍要在 SynColor 模式下使用 OCIO v1 配置，请执行以下操作：

1. 在[“颜色管理”(Color Management)首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2D9BBB9D-49F0-44C6-8BFF-B237FD8ED746)中，确保“启用颜色管理”(Enable Color Management)处于激活状态，其他选项按[重要的颜色管理设置](../颜色管理任务/配置颜色管理/重要的颜色管理设置.md)中所述进行设置。

2. 在“OCIO 配置路径”(OCIO config Path)中输入有效 OpenColorIO 配置文件的完整绝对路径。

3. 激活“使用 OCIO 配置”(Use OCIO configuration)。

  - 如果配置文件无效，系统将提示您使用本地支持的颜色空间。如果单击“否”(No)，系统将提示您选择其他配置文件。

  - 在配置之间切换时，颜色空间按名称匹配。如果当前场景中使用的任何颜色空间尚未在当前配置中进行定义，则会显示一条消息。此外，图像输入节点中任何缺少的颜色空间在属性编辑器中都以红色亮显，且不应用变换。请参见[修复缺少的颜色变换](../颜色管理任务/修复缺少的颜色变换.md)。

4. （可选）根据是否要使用标准 OpenColorIO 规则将初始输入颜色空间指定给“文件”(File)纹理和其他图像输入（将它们添加到场景时），可以切换“使用 OCIO 输入颜色空间规则”(Use OCIO Input Color Space Rules)。OpenColorIO 规则考虑颜色空间名称是否出现在文件名中。

  - 启用“使用 OCIO 输入颜色空间规则”(Use OCIO Input Color Space Rules)时，在下面的“输入颜色空间规则”(Input Color Space Rules)中仅显示“OCIO 标准规则”(OCIO Standard Rule)和“默认”(Default)。无法添加任何其他规则，且无法对它们重新排序。您只能为“默认”(Default)规则（仅当“OCIO 标准规则”(OCIO Standard Rule)没有为特定文件指定任何颜色空间时，才会使用此规则）指定颜色空间。

  - 禁用此选项时，您可以定义自己的规则，以将颜色空间指定给“输入颜色空间规则”(Input Color Space Rules)中的输入图像。但是，可用的颜色空间仅限于在 OCIO 配置文件中定义的颜色空间。请参见[定义规则以为输入文件指定颜色空间](../颜色管理任务/配置颜色管理/定义规则以便将颜色空间指定给输入文件.md)。

**注**

如果在启动

Maya

时遇到与颜色管理相关的延迟，请确保 OCIO 配置文件包含

environment

部分。该部分是否为空无关紧要，例如：

```text
environment:
  {}
```
