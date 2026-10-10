# 使用 Backburner 进行网络渲染

在进行网络渲染时，可以结合使用 Autodesk® Backburner TM 和 Maya 来管理渲染作业和渲染节点。Autodesk Backburner 是一种背景渲染网络系统，允许同一网络上的许多计算机共同渲染动画场景。

有关详细信息，请参见[**“Backburner User Guide”**](https://www.autodesk.com/backburner-documentation-chs)（Backburner 用户指南）。（该文件的大小约为 2 MB。）

## 安装 Backburner

在安装 Backburner 之前，确保已禁用渲染节点上的防火墙或允许通过适当端口。

有关如何在独立工作站上设置背景渲染的信息，请参见[**“Backburner Installation Guide”**](https://www.autodesk.com/backburner-documentation-chs)（Backburner 安装指南）的**“Configuring a Standalone Workstation”**（配置独立工作站）一章。（该文件的大小约为 2 MB。）

有关如何设置渲染场中的 Backburner Manager 和 Backburner Server 的说明，请参见[**“Backburner Installation Guide”**](https://www.autodesk.com/backburner-documentation-chs)（Backburner 安装指南）的**“Backburner Components - Windows”**（Backburner 组件 - Windows）一章。（该文件的大小约为 2 MB。）

下面介绍的安装和设置步骤可直接使用或进行修改以进行自定义集成。

## 在开始之前

在开始之前，必须确保以下事项：

- 将 Backburner 和 Maya 安装在每个渲染场节点上的同一文件夹位置。因此，不能混合使用 Windows 渲染节点和 Linux 渲染节点或者 Windows 渲染节点和 Mac OS X 渲染节点，等等。

- 项目必须可从 Backburner 设置中的所有渲染节点访问。

  - (Windows) 映射到同一驱动器号或 UNC 路径。

  - (Linux) 装载到同一位置。

  - (Mac OS X) 装载到同一位置。

- 必须将项目设定为网络可访问路径。

- 建议项目数据位于与渲染节点和渲染场管理器不同的文件服务器上。

- 必须将场景保存到文件并可跨网络访问它。将忽略所有未保存的更改。

- 拟保存渲染图像的项目 ..\images 目录位置必须是跨网络可写入的。

- 日志文件将保存到的日志路径必须可写。

**注**

Backburner 为渲染动画提供了最佳性能改进。Backburner 只能将作业细分为至少一个帧长的任务。它无法将单个帧细分为多个任务以跨多台计算机进行分发。

## 结合使用 Maya 和 Backburner 进行网络渲染

按照以下步骤设置 Backburner 以与 Maya 结合使用。

设置 Backburner 以与 Windows 上的 Maya 结合使用

1. 在所有渲染场节点上安装 Backburner 和 Maya。

  必须将 Backburner 和 Maya 安装在每台计算机上的同一文件夹位置。

2. 选择要用作渲染场管理器的计算机。在该计算机上，运行 Backburner Manager 并配置它以适合您的环境。

3. 在要用于渲染的所有计算机上（如果需要，包括渲染场管理器），运行 Backburner Server 应用程序并使其指向选择作为 Backburner Manager 的计算机。

  **注**

  可以将 Backburner Manager 和 Server 作为 Windows 中的服务运行。有关详细信息，请参见**“Backburner Installation Guide”**（Backburner 安装手册）。

  **注**

  不建议将渲染场管理器用于渲染。

设置 Backburner 以与 Linux 上的 Maya 结合使用

1. 在所有渲染场节点上安装 Backburner 和 Maya。

  必须将 Backburner 和 Maya 安装在每台计算机上的同一文件夹位置。

2. 选择要用作渲染场管理器的计算机。在该计算机上，以 root 身份运行 /usr/discreet/backburnerConfig 并安装 Backburner Manager 服务。

  **注**

  设置 Backburner Server 服务是可选的。

3. 在要用于渲染的所有计算机上（如果需要，包括渲染场管理器），以 root 身份运行 /usr/discreet/backburnerConfig 并将 Backburner Server 配置为指向选择作为 Backburner Manager 的计算机。

  **注**

  不建议将渲染场管理器用于渲染。

  **注**

  有关详细信息，请参见**“Backburner Installation Guide”**（Backburner 安装手册）。

设置 Backburner 以与 Mac OS X 上的 Maya 结合使用

1. 在所有渲染场节点上安装 Backburner 和 Maya。

  必须将 Backburner 和 Maya 安装在每台计算机上的同一文件夹位置。

2. 选择要用作渲染场管理器的计算机并在位于 /usr/discreet/backburner/cfg 的 manager.host 文件中输入其名称。

3. 重新启动 Backburner Server。

  或者，也可以重新启动计算机。

  **注**

  有关详细信息，请参见**“Backburner Installation Guide”**（Backburner 安装手册）。

## 从 Maya 将作业提交到 Backburner

若要创建渲染作业和管理渲染节点，请选择[渲染 > 创建 Backburner 作业(Render > Create Backburner Job)](../../渲染参考/渲染参考/“渲染”%28Rendering%29菜单集/“渲染”%28Render%29菜单/创建%20Backburner%20作业选项%28Create%20Backburner%20Job%20Options%29.md)。

## 创建自定义集成

除了使用现成的 Backburner 集成外，还可以自定义自己的集成。为此，必须了解以下事项。

- 在选择[渲染 > 创建 Backburner 作业(Render > Create Backburner Job)](../../渲染参考/渲染参考/“渲染”%28Rendering%29菜单集/“渲染”%28Render%29菜单/创建%20Backburner%20作业选项%28Create%20Backburner%20Job%20Options%29.md)时，该脚本创建指示 Maya 渲染命令行工具和 Backburner cmdJob 工具的设置。

- 指示渲染命令工具使用当前投影路径和当前场景路径进行渲染。渲染目录也是项目图像目录。

- “开始帧”(Start Frame)、“结束帧”(End Frame)和“任务大小”(Task Size)属性用于创建用于将帧分发到不同计算机的任务列表文件。例如，如果“开始帧”(Start Frame)是 1，“结束帧”(End Frame)是 30，“任务大小”(Task Size)是 6，则 Backburner 使用文件来指示渲染命令在每个渲染节点上渲染哪些帧。例如，渲染节点 1 渲染帧 1-6，渲染节点 2 渲染帧 7-12 等等。

- 若要查看如何生成 Maya 渲染命令行工具和 Backburner cmdJob 工具的参数，请选择[渲染 > 创建 Backburner 作业(Render > Create Backburner Job)](../../渲染参考/渲染参考/“渲染”%28Rendering%29菜单集/“渲染”%28Render%29菜单/创建%20Backburner%20作业选项%28Create%20Backburner%20Job%20Options%29.md)窗口中的“使用自定义命令”(Use Custom Command)并单击“填充命令”(Populate Command)按钮。也可以根据需要自定义参数。
