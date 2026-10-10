# FBX MEL 脚本

本部分包含使用 Maya MEL 命令编写 FBX 脚本时所需的脚本。

每个 Maya FBX 插件的 MEL 命令均以 FBX 前缀开头。在遇到错误情况时，将在脚本编辑器窗口中显示错误消息。Maya FBX 插件注册的 MEL 命令都列在“插件管理器信息”(Plug-in Manager information)对话框中。

Maya FBX 插件中几乎每个选项都有一个脚本命令。如果某个特定脚本工作流还没有对应的脚本命令存在，您还可以使用 FBXProperty。仍可以使用 FBXProperty 访问该命令。通过 FBXProperty 命令，可以使用 FBX 插件用户界面中提供的所有选项。

| 命令 | 描述 |
|---|---|
| FBXProperties | 使用此命令可列出所有可用的导入和导出属性。此命令将返回属性路径、类型和当前值。如果属性是枚举属性，则返回所有可能的值。 |
| FBXProperty Import\|IncludeGrp\|LightGrp\|Light -v true; | 使用此命令可将导入值设置为 true。 |
| FBXProperty Import\|IncludeGrp\|LightGrp\|Light -q; | 使用此命令可查询导入值。 |
| FBXProperty Export\|IncludeGrp\|LightGrp\|Light -v true; | 使用此命令可将导出值设置为 true。 |
| FBXProperty Export\|IncludeGrp\|LightGrp\|Light -q; | 使用此命令可查询导出值。 |

**注**

- 要使用 FBX MEL 命令，您必须确保 Maya FBX 插件在相应 Maya 版本中处于活动状态。

- 这些脚本命令不影响 FBX 导出/导入预设窗口中的设置。

- 我们建议使用标准 MEL 脚本命令（如果有）。

- 本部分中的所有脚本命令和路径均区分大小写，因此最好复制并粘贴这些命令，以便您在查询特性列表及其路径时具有准确的“IO 设置”路径。

- 这些脚本命令仅支持“整数”、“双精度”、“布尔”和“枚举”特性。

## 导入 FBX 文件

如果要使用脚本导入 FBX 文件，请使用标准 File(...)（如果 FBX 文件中不包含镜头）。要导入特定镜头，请使用 [FBX 导入 MEL 命令](FBX%20MEL%20脚本/FBX%20导入%20MEL%20命令.md)部分中的 FBXImport。
