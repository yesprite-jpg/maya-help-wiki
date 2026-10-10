# “安全”(Security)首选项

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 3829 字 ≥300，非承重" -->

可以在[“首选项”(Preferences)窗口](../“首选项”%28Preferences%29窗口.md)的“安全”(Security)类别中设置以下首选项。

启用这些安全首选项会改变在打开/导入场景文件或加载插件时 Maya 的行为。在前一种情况下，可以对其进行设置以标记特定命令，在后一种情况下，仅从受信任的位置加载插件。这可确保，如果这些文件（例如在 Web 上共享的场景文件）中可能隐藏了可能恶意的代码，您会收到相关警告/受到保护。

## 常规安全首选项

#### 安全

启用/禁用此项可同时激活/取消激活所有安全子部分（MEL、Python、插件）。当您手动仅激活/取消激活其中一个或两个子部分时，此项将自动设置为“自定义”(Custom)。

**注**

如果您手动激活/取消激活任一子部分，Maya 会自动将此项切换为“自定义”(Custom)。

## 启动脚本权限

#### 读取和执行“userSetup”脚本(Read and execute 'userSetup' scripts)

控制 Maya 在启动时是否自动运行 userSetup.mel 或 userSetup.py 脚本。默认情况下，这些脚本位于：

- Windows：..\My Documents\maya\<版本>\scripts

- Mac OS X：~/Library/Preferences/Autodesk/maya/<version>/scripts

- Linux：~/maya/<version>/scripts

#### 如果“userSetup”脚本包含更改，则发出警告(Warn me if 'userSetup' scripts contain changes)

控制 Maya 是否自动对所有 userSetup 脚本执行哈希校验（数字指纹），以确保它们不包含并非原始脚本创建者想要的任何内容。如果脚本未通过哈希校验，Maya 将向用户显示警告，并让用户选择是否保存新哈希值。默认情况下禁用此设置。

## 安全日志记录

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 3829 字 ≥300，非承重" -->

#### 启用安全日志记录(Enable security logging)

启用此选项可将所有安全事件（MEL、Python、插件）记录到名为“mayaSecurity”的日志文件中。

#### 日志文件格式(Log file format)

确定“mayaSecurity”写入的文件类型。

#### 默认安全日志记录目录(Default security logging directory)

确定“mayaSecurity”文件的默认保存位置。

## MEL

用于标记要在加载场景文件时拒绝执行的特定 MEL 命令。在您要从未知源接收文件并想要确保系统的完整性时，这很有用。默认情况下，此选项已启用。

**注**

这仅影响加载文件（例如通过 scriptJob/scriptNode）时执行的命令。它不影响从“脚本编辑器”(Script Editor)执行的命令。

#### 安全 MEL 加载(Secure MEL loading)

启用后，对于“已标记命令”(Flagged commands)列表中的命令，Maya 会请求允许执行或拒绝执行（具体取决于当前“已标记命令的默认操作”(Default action for flagged commands)设置）。

#### 已标记命令(Flagged commands)

确定在启用了“安全文件加载”(Secure file loading)时标记哪些命令。单击“添加”(Add)可通过文本输入将命令添加到列表，或选择列表中已有的命令，然后单击“移除”(Remove)以将其取消标记。

#### 已标记命令的默认操作(Default action for flagged commands)

确定 Maya 在加载期间如何处理已标记命令。“请求权限”(Ask for permission)表示提示用户是否允许运行 Maya 在加载时遇到的已标记命令的每个实例。“拒绝”(Deny)表示在加载时自动阻止运行任何已标记命令。默认值为“请求权限”(Ask for permission)。

#### 允许在场景文件中使用全局程序定义(Allow global proc definition in scene file)

![图：确定是否允许嵌入的 MEL 脚本定义全局程序。如果禁用，将在文件加载时阻止所有全局程序调用。默认情况下禁用此设置。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 3829 字 ≥300，非承重" -->

确定是否允许嵌入的 MEL 脚本定义全局程序。如果禁用，将在文件加载时阻止所有全局程序调用。默认情况下禁用此设置。

## Python

定义在导入 .ma/.mb 文件时，Maya 如何处理嵌入到这些文件中的 Python 命令或模块（包括 scriptNode/scriptJob）。在您要从未知源接收文件并想要确保系统的完整性时，这很有用。

**注**

这仅影响加载文件（例如通过 scriptJob/scriptNode）时执行的命令。它不影响从“脚本编辑器”(Script Editor)执行的命令。

#### Python

确定在遇到尝试加载/导入的文件中嵌入了 Python 命令/模块时，Maya 如何继续。使用“执行前检查(安全)”(Check before executing (secure))，可通过以下选项自定义允许或拒绝哪些特定命令/模块。同时，“执行”(Execute)和“不执行”(Don't Execute)分别表示允许或拒绝其遇到的**所有** Python 模块执行。 默认情况下，此项设置为“执行”(Execute)，但我们强烈建议您将其切换为“执行前检查(安全)”(Check before executing(secure)) **，然后**从不受信任的源加载文件。

### Python 内置函数

#### 安全的内置函数(Secure built-in functions)

启用后，对于“已标记内置函数”(Flagged built-in functions)列表中的命令，Maya 会请求允许执行或拒绝执行（具体取决于当前“已标记命令的默认操作”(Default action for flagged commands)设置）。这仅在 Python 设置为“执行前检查(安全)”(Check before executing (secure))时有效。

#### 已标记内置函数(Flagged built-in functions)

指定在启用了“安全的内置函数”(Secure built-in functions)时要拒绝的 Python 命令。带复选标记的函数将被标记为拒绝。

#### 导入模块的默认操作(Default action for importing modules)

确定 Maya 如何处理“已标记内置函数”(Flagged built-in functions)列表中的 Python 命令。“请求权限”(Ask for permission)表示提示用户是否允许执行 Maya 在加载时遇到的每个已标记函数。“拒绝”(Deny)表示在加载时自动阻止执行任何已标记函数。默认值为“请求权限”(Ask for permission)。

### Python 模块

#### 安全模块导入(Secure module import)

启用后，对于**不**在“受信任的模块”(Trusted modules)列表中的所有模块，Maya 会请求允许加载或拒绝加载（具体取决于当前“已标记命令的默认操作”(Default action for flagged commands)设置）。这仅在 Python 设置为“执行前检查(安全)”(Check before executing (secure))时有效。

#### 受信任的模块(Trusted modules)

指定在启用了“安全模块导入”(Secure module import)时允许加载的 Python 模块。单击“添加”(Add)，然后导航到文件浏览器中的文件夹以将位置添加到列表中，或者选择已在列表中的位置，然后单击“移除”(Remove)以将其移除。

#### 导入模块的默认操作(Default action for importing modules)

确定 Maya 如何处理“受信任的模块”(Trusted modules)列表之外的模块。“请求权限”(Ask for permission)表示提示用户是否允许导入 Maya 在加载时遇到的每个未列出模块。“拒绝”(Deny)表示在加载时自动阻止导入任何未列出模块。默认值为“请求权限”(Ask for permission)。

## 插件

用于根据插件的位置控制可以加载的插件。

#### 安全插件加载(Secure plugin loading)

启用后，对于“我的受信任插件位置”(My trusted plugin locations)列表以外的任何位置的插件，Maya 会请求允许加载或拒绝加载（具体取决于当前“已标记命令的默认操作”(Default action for flagged commands)设置）。默认情况下，此选项已启用。

#### 我的受信任插件位置(My trusted plugin locations)

指定在启用了“安全插件加载”(Secure plugin loading)时要从其加载插件的安全位置。单击“添加”(Add)，然后导航到文件浏览器中的文件夹以将位置添加到列表中，或者选择已在列表中的位置，然后单击“移除”(Remove)以将其移除。

**注**

Maya 还维护一个默认的受信任插件位置列表，这些位置不显示在此列表中。

#### 不受信任位置的默认操作(Default action for untrusted locations)

确定在启用了“安全插件加载”(Secure plugin loading)时，Maya 如何处理尝试从“我的受信任插件位置”(My trusted plugin locations)以外的位置加载的插件。“请求权限”(Ask for permission)表示每次用户尝试从不受信任的位置加载插件时提示用户。“拒绝”(Deny)表示自动阻止来自不受信任的位置的任何插件。默认值为“请求权限”(Ask for permission)。
