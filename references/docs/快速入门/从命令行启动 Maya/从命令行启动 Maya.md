# 从命令行启动 Maya

如果从命令行启动 Maya，您可以指定多种启动选项。例如，使用 -file 标志可以在启动时打开文件：

```text
maya -file filename
maya.exe -file filename
```

若要查看可用的启动标志，请键入以下内容：

```text
maya -help
```

## 在 batch 或 prompt 模式下运行 Maya

Maya 可以在多个影响其整体操作方式的不同模式下运行，其中有两个模式允许您在不使用界面的情况下执行 Maya 命令：-prompt 和 -batch（在 Windows 中，使用 mayabatch.exe 而不是 Maya -batch）。

- -prompt 标志发出 MEL 提示，要求您键入命令，这与脚本编辑器类似。某些需要图形用户界面的命令不可用或没有效果。键入 quit 可退出 prompt 模式。

- 使用 -batch 标志可以在无您输入的情况下运行命令，例如 shell 或批处理脚本。-batch 标志启动 Maya、执行指定的任何命令指定，然后关闭 Maya。例如，可以创建一个脚本，打开先前版本 Maya 中的文件，以便将该文件更新到当前版本。对于 Linux 和 macOS：

  ```text
maya -batch -file someMayaFile.mb -command "file -save"
```

  对于 Windows：

  ```text
mayabatch -file someMayaFile.mb -command "file -save"
```

- 以批处理模式启动 Maya 时，默认情况下将运行分析。若要选择退出分析，请在启动 Maya 之前设置 MAYA_DISABLE_ADP=1。

**注**

- -batch 命令不用于批处理渲染。请改用 Render 命令。

- 在 Windows 中，如果使用 -bath 标志，则键入 mayabatch。mayabatch 命令在命令提示窗口中运行，而 maya 命令则会启动独立的窗口。

- -render 标志现已过时。请改用 Render -r 命令。

## 其他 Maya 启动标志

这些是使用命令行启动 Maya 时可以使用的其他标志（在 Linux 和 macOS 上：maya；在 Windows 上：mayabatch.exe）。

| -archive [file] | 显示将指定场景归档所需的文件列表，然后退出 Maya。 |
|---|---|
| -command [mel command] | 启动时运行指定的命令。命令应放在双引号中，以保护任何特殊字符，包括空格。 |
| -log [file] | 将所有标准输出和错误消息（通常显示“输出窗口”）复制到指定文件（使用完整文件名）中。 此标志仅适用于 Windows。 |
| -noAutoloadPlugins | 不自动加载任何插件。 |
| -optimizeRender [file] [outfile] | 处理特定场景文件，以针对渲染优化该文件，将结果放置在输出文件中，然后退出。使用 maya -optimizeRender -help 可获得更多选项。请参见 [-optimizeRender 标志](从命令行启动%20Maya.md#WS17956D7ADBC6E7362B9D3AA0117AE30A829-7FF2)。 |
| -proj [dir] | 在指定项目目录中查找场景文件。 |
| -recover | 恢复上次日志文件。 |
| -script [file] | 启动时源化指定文件（应是 MEL 脚本）。 |
| -v | 显示产品版本和识别编号，然后退出。 |
| -3 | 启用 Python 3000 兼容性警告。 |

**注**

从 Maya 2012 开始，对于 Linux 和 Mac 平台，在 Maya 尝试使用由 lastLocalWS 指向的目录之前，需要通过检查来确保该目录可访问。该目录必须具有 555 (r-xr-xr-x) 权限。否则，如果目录仅具有“444 (r--r--r--)”权限，Maya 将无法使用该目录，甚至“CD”或“ls”也无效。

除 lastLocalWS 之外，Maya 在启动时还尝试使用其他的工作区，而对这些工作区也将应用相同的检查。Maya 尝试使用这些工作区的顺序如下：

- 从 -proj 命令行参数获取的值

- 从 MAYA_PROJECT 环境变量获取的值

- InitialProject optionVar（即标记为“始终使用此项目启动”(Always start in this project)的首选项）

- lastLocalWS optionVar（在退出时由 Maya 自动存储，以记住上一活动工作区）

- 默认项目

## -optimizeRender 标志

使用该命令可针对渲染优化指定的场景文件，将结果发送到输出文件中，然后关闭 Maya。

maya -optimizeRender [options] [file] [outfile]

可用的 [options] 包括：

| -botRes [Int] | 指定导致 BOT 文件生成的最小文件纹理分辨率。例如，指定“-botRes 256”意味着大于 256x256 的所有文件纹理都将转化为 BOT 格式。 |
|---|---|
| -botLoca [name] | 指定 BOT 文件驻留的目录。默认目录与原始文件所在目录相同。 |
| -help | 显示所有可以与 -optimizeRender 一起使用的标志。 |
| -noBOT | 不创建 BOT 文件。 |
| -noCleanup | 不清理无用数据。 |
| -tessFreeze [startframe] [endframe] [byframe] | 根据摄影机投影计算可产生最佳图像质量的 NURBS 细分。 |
