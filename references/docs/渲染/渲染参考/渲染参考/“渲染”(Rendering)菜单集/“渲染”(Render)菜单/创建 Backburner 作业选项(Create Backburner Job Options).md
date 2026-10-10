# 创建 Backburner 作业选项(Create Backburner Job Options)

使用这些选项可查看在选择“渲染 > 创建 backburner 作业”(Render > Create Backburner Job)时发生的情况。

**注**

Maya 中不包含 Backburner。可以从

Autodesk App Store

下载它。

## 作业设置

下列属性与您的场景一起保存。保存之后，下次重新打开该场景时会自动加载设置，即使该场景位于一个不同的计算机上。

使用下列属性可为作业设定选项，例如，作业的名称，以及应如何将作业分解为任务并分布到不同的渲染节点。会将这些设置定向到 cmdjob 工具，然后定向到每个渲染节点的命令行渲染器。

**注**

拟保存渲染图像的项目 ..\images 目录位置必须是跨网络可写入的。

#### 作业名称(Job Name)

指定要发送到 cmdjob 工具的作业的名称。

#### 描述(Description)

指定作业的描述。该信息将显示在 Backburner 监视器中。

#### 优先级(Priority)

设定作业优先级。默认值为 50。其他值为 0（关键）或 100（挂起）。

#### 开始帧(Start Frame)

为作业指定开始帧。

**注**

“开始帧”(Start Frame)、“结束帧”(End Frame)和“任务大小”(Task Size)属性用于为 cmdjob 工具自动生成一个任务列表，以指定应如何将作业分解为任务。

#### 结束帧(End Frame)

为作业指定结束帧。

#### 任务大小(Task Size)

指定每个任务的帧数。

#### 渲染器(Renderer)

选择“来自场景文件”(from the Scene File)可使用在场景的“渲染设置”(Render Settings)中指定的渲染器。

选择任何其他选项可覆盖在场景的“渲染设置”(Render Settings)中指定的渲染器。

#### 其他选项(Additional Options)

将任何其他标志指定给命令行渲染器。这与在 Render -r <renderer name> <options> <filename> 中设置这些选项是等效的。有关详细信息，请参见[关于命令行渲染器](../../../../渲染实用程序/渲染实用程序/命令行渲染器/关于命令行渲染器.md)。

**注**

在更新场景后，必须保存场景，再导出到 Backburner。所有未保存的更改都会被忽略。

## Backburner 选项

下列选项与您的计算机一起保存，且不依赖于已打开的场景。会将这些选项定向到 Backburner。

#### 管理员名(Manager Name)

设定管理员的姓名。默认为自动搜索。

**注**

该字段为必填字段。

#### 端口(Port)

要将作业提交到的 Backburner 端口号。输入 0 可使用默认端口。

#### 服务器列表(Server List)

应该处理该作业的服务器列表。在列表中用分号分隔服务器。

#### 服务器组(Server Group)

应该处理该作业的服务器组的名称。

#### 服务器数(Server Count)

应该处理该作业的最大服务器数量。输入 0 时数量不受限制。

#### 手动启动作业(Manually Start Job)

作业被挂起时启动作业。

#### 创建日志文件(Create Log Files)

选择该选项可创建任务日志。日志文件通常用于疑难解答。

#### 日志路径(Log Path)

指定在其中创建任务日志的文件夹或目录的位置。必须指定某个现有文件夹，因为如果该文件夹不存在，命令行工具无法创建它。默认情况下会禁用该选项。

**注**

必须可在网络上访问该路径。

#### 渲染器路径(Renderer Path)

指定每个渲染节点上的渲染器的位置。在所有渲染节点上，渲染器路径必须相同。因此，不能混合平台，且必须将 Maya 安装在每个渲染节点上的相同位置。

#### backburner 路径(Backburner Path)

指定 backburner 的位置。确保默认路径正确，然后再继续。

#### 使用自定义命令(Use Custom Command)

选择该选项可启用“自定义命令选项”(Custom Command Options)属性。否则，将灰显这些属性。

使用“自定义命令选项”(Custom Command Options)可将命令自定义到 Backburner。有关详细信息，请参见[自定义命令选项](创建%20Backburner%20作业选项%28Create%20Backburner%20Job%20Options%29.md#WS1A9193826455F5FF-3859B43C1209703A8387F97)。

## 电子邮件选项

#### 发送电子邮件(Send Email)

选择该选项后，Backburner 会发送通知电子邮件。

#### 通知完成(Notify Completion)

选择该选项后，Backburner 会在完成作业后发送通知电子邮件。

#### 通知进度(Notify Progress)

选择该选项后，Backburner 会在完成设定的任务数后发送通知电子邮件。

#### # 个任务之后更新(Update after # of tasks)

设定用于“通知进度”(Notify Progress)的任务数。

#### 发件人（电子邮件地址）(From email address)

设定通知电子邮件的源电子邮件地址。

#### 收件人（电子邮件地址）(To email address)

设定通知电子邮件的目标电子邮件地址。

#### SMTP 服务器(SMTP Server)

设定 Backburner 用来发送通知电子邮件的 SMTP 电子邮件服务器的名称。

## 自定义命令选项

若要启用“自定义命令选项”(Custom Command Options)，必须选择上面的“使用自定义命令”(Use Custom Command)选项。

#### 填充命令(Populate Command)

单击该按钮可使用概括该窗口中的设置的命令填充下面的框。

可以根据需要自定义命令；例如，可以更改渲染器。或者，可以将命令复制到“脚本编辑器”(Script Editor)。
