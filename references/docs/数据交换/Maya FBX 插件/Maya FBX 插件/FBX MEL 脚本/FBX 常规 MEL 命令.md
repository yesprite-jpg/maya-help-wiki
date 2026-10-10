# FBX 常规 MEL 命令

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 3563 字 ≥300，非承重" -->

以下 MEL 命令用于模拟 FBX 用户界面中的其他选项。

#### FBXClose

FBXClose;

关闭 FBX 导入器，以便解除锁定使用 FBXRead 命令启动的所有 FBX 文件。

使用 FBXRead 命令时，将打开并锁定 FBX 文件。若要释放该文件，必须调用 FBXClose 命令，或者调用可打开一个新文件的命令（例如 FBXRead 或 FBXImporter 等）。

#### ![图：FBXExtPlugin](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 3563 字 ≥300，非承重" --> FBXExtPlugin

FBXExtPlugin -l;

FBXExtPlugin <pluginName> [-q] -state [on|off];

FBXExtPlugin <pluginName> [-q] -opts [optionsString];

用户可使用 FBXExtPlugin 列出、启用、禁用 FBX 扩展插件以及将选项传递到 FBX 扩展插件。

状态和选项存储在内存中，而不是存储在 FBX 文件中。它们将会一直保留其设置，直到再次调用 FBXExtPlugin 更改它们为止。

选项字符串是用双引号引起来的单个字符串。传递到扩展插件的选项的语法由其传递到的扩展插件确定。这意味着，您将需要参阅扩展插件的文档以确定选项名称和值分隔符。如果选项字符串过长，则会被截断。

FBXExtPlugin -l 用于输出安装的扩展插件列表。

FBXExtPlugin <pluginName> -q -state 用于查询特定扩展插件的状态。

FBXExtPlugin <pluginName> -state [on|off] 用于启用或禁用扩展插件。

FBXExtPlugin <pluginName> -q -opts 用于查询传递到扩展插件的选项。

FBXExtPlugin <pluginName> -opts <optionsString> 用于将选项传递到扩展插件。

**注**

有关扩展插件的详细信息，请参阅 FBX 扩展 SDK 软件包。

#### FBXGetTakeComment

FBXGetTakeComment [index];

返回附加到镜头阵列中指定索引处的镜头的注释。此命令使用存储在文件缓冲区中的文件。

可以使用 FBXRead 命令将文件加载到文件缓冲区。

**注**

输入的数字必须介于 1 和文件中包含的镜头数之间，否则脚本会返回消息：

“无此镜头”(No such take)

。Maya FBX 插件将大于文件中所含镜头数的镜头数、负值或 0 视为无效。

#### FBXGetTakeCount

FBXGetTakeCount;

返回在文件缓冲区中存储的文件中保存的镜头数。

可以使用 FBXRead 命令将文件加载到文件缓冲区。

**注**

如果 Maya FBX 插件未在文件中找到任何镜头，该脚本返回的值为 0。

#### FBXGetTakeIndex

FBXGetTakeIndex [take name];

返回镜头阵列中命名为参数的第一个镜头的索引。此命令使用存储在文件缓冲区中的文件。

可以使用 FBXRead 命令将文件加载到文件缓冲区。

**注**

如果 [take name] 不包含有效的名称，脚本将返回消息：

“无此镜头”(No such take)

。

#### FBXGetTakeLocalTimeSpan

FBXGetTakeLocalTimeSpan [index];

返回镜头阵列中指定索引处镜头的本地开始和停止时间。此命令使用存储在文件缓冲区中的文件。

可以使用 FBXRead 命令将文件加载到文件缓冲区。

**注**

输入的数字必须介于 1 和文件中包含的镜头数之间，否则脚本会返回消息：

“无此镜头”(No such take)

。Maya FBX 插件将大于文件中所含镜头数的镜头数、负值或 0 视为无效。

#### FBXGetTakeName

FBXGetTakeName [index];

返回镜头阵列中指定索引处镜头的名称。此命令使用存储在文件缓冲区中的文件。

可以使用 FBXRead 命令将文件加载到文件缓冲区。

FBXGetTakeName [index];

**注**

输入的数字必须介于 1 和文件中包含的镜头数之间，否则脚本会返回消息：

“无此镜头”(No such take)

。Maya FBX 插件将大于文件中所含镜头数的镜头数、负值或 0 视为无效。

#### FBXGetTakeReferenceTimeSpan

FBXGetTakeReferenceTimeSpan [index];

返回镜头阵列中指定索引处的镜头的引用开始和停止时间。此命令使用存储在文件缓冲区中的文件。

可以使用 FBXRead 命令将文件加载到文件缓冲区。

**注**

输入的数字必须介于 1 和文件中包含的镜头数之间，否则脚本会返回消息：

“无此镜头”(No such take)

。Maya FBX 插件将大于文件中所含镜头数的镜头数、负值或 0 视为无效。

#### FBXLoadExportPresetFile

FBXLoadExportPresetFile -f [filepath];

设置导出预设文件路径。

#### FBXLoadImportPresetFile

FBXLoadImportPresetFile -f [filepath];

通过此命令，可以设置导入预设文件路径。

您可以使用此命令加载 MotionBuilder 导入预设，而无需知道其文件路径。

例如：FBXLoadMBImportPresetFile; 将加载“C:\<Maya 版本>\bin\plug-ins\FBX\Presets\<版本>\import\Autodesk MotionBuilder.fbximportpreset”（在您的计算机上，路径可能会有所不同）。

#### FBXLoadMBExportPresetFile

FBXLoadMBExportPresetFile

此命令加载随每个版本提供的 MotionBuilder 预设。

您可以使用此命令加载 MotionBuilder 导入/导出预设，而无需知道其文件路径。

例如：FBXLoadMBExportPresetFile; 将加载“C:\<Maya 版本>\bin\plug-ins\FBX\Presets\<版本>\export\Autodesk MotionBuilder.fbxexportpreset”（在您的计算机上，路径可能会有所不同）。

#### FBXLoadMBImportPresetFile

FBXLoadMBImportPresetFile

此命令加载随每个版本提供的 MotionBuilder 预设。

您可以使用此命令加载 MotionBuilder 导入/导出预设，而无需知道其文件路径。

例如：FBXLoadMBImportPresetFile; 将加载“C:\m<Maya 版本>\bin\plug-ins\FBX\Presets\<版本>\import\Autodesk MotionBuilder.fbximportpreset”，FBXLoadMBExportPresetFile; 将加载“C:\<Maya 版本>\bin\plug-ins\FBX\Presets\<版本>\export\Autodesk MotionBuilder.fbxexportpreset”（在您的计算机上，路径可能会有所不同）。

#### FBXPopSettings

FBXPopSettings;

此设置会加载 Pop 脚本保存的所有设置；在您执行单击操作时会保留设置的当前状态。

#### FBXPushSettings

FBXPushSettings;

此设置保存所有 I/O 设置。使用 FBXPushSettings 可在您执行“发送到”操作时保留设置的当前状态。

#### FBXRead

FBXRead -f [filename];

读取指定的 FBX 文件，而不将任何内容导入到 Maya 中。文件存储在缓冲区中。此命令用于镜头查询。

读取或导入后，使用命令 FBXGetTakeCount、FBXGetTakeName、FBXGetTakeIndex 进行镜头查询。

**注**

正在读取的文件必须与现有文件名匹配，否则如果试图读取或导入不存在的文件，缓冲区中的文件将被损坏。

#### FBXResetImport

FBXResetImport;

该命令可以恢复“FBX 导入器”(FBX Importer)的默认值并加载 Autodesk Media & Entertainment **导入**预设中指定的设置，就像在 UI 中一样。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“导入预设”。

#### FBXResetExport

FBXResetExport;

该命令可以恢复 “FBX 导出器”(FBX Exporter)的默认值，并加载在 Autodesk Media & Entertainment **导出**预设中指定的设置。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“导出预设选项”。

#### FBXResamplingRate

FBXResamplingRate -v [float];

FBXResamplingRate -q;

设置导出器在需要重新对数据采样时生成关键帧所用的速率。

当 Maya 中的动画曲线的插值不能由 MotionBuilder 中的曲线正确表示时，需要进行重采样。
