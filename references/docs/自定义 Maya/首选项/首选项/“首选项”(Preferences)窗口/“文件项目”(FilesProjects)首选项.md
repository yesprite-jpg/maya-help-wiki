# “文件/项目”(Files/Projects)首选项

可以在[首选项(Preferences)窗口](../“首选项”%28Preferences%29窗口.md)的“文件/项目”(Files/Projects)类别中设置以下首选项。

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

## 项目设置(Projects Settings)

#### 默认项目目录(Default projects directory)、始终使用此项目启动(Always start in this project)

创建新项目或启动项目时，可以使用这些设置来设置默认项目目录。

## 最近的历史大小(Recent History Size)

#### 文件(Files)、递增文件(Increments)、项目(Projects)

指定要在每个“文件 > 最近”(File > Recent)子菜单中列出多少个文件，递增文件和项目。

## 自动保存

#### 启用(Enable)

启用时，“自动保存”(Autosave)会按确定的间隔自动保存您的场景。文件按照“自动保存”(Autosave)选项，以名称 AUTO-SAVE 后跟递增数字进行保存。

#### 保存之前提示(Prompt before save)

在自动保存之前以对话框形式提示用户。

#### 限制自动保存(Limit autosaves)

限制可自动保存文件的次数。

#### 自动保存数(Number of autosaves)

确定在“限制自动保存”(Limit autosaves)限处于启用状态时可以自动保存文件的次数。

#### 间隔(分钟) (Interval (minutes))

确定每次自动保存之间的时间量（默认值为 10 分钟）。

#### 自动保存目标(Autosave destination)

确定自动保存文件存储的位置。“项目”(Project)将其存储在当前项目的“自动保存”(autosave)文件夹下，而“命名的文件夹”(Named folder)将其存储在指定的文件夹中。环境变量根据环境变量 MAYA_AUTOSAVE_FOLDER 的值存储自动保存文件。

## 崩溃恢复(Crash Recovery)

激活此选项可显示崩溃文件信息（如果最后一个会话发生崩溃）。

## Ascii 文件压缩模式(Ascii File Compression Mode)

#### 保存文件时(On file save)

指定保存 ASCII 文件时要使用的压缩模式：

#### 压缩(Compressed)

采用压缩模式保存文件。文件压缩可缩小大文件的大小，使它们不会占用硬盘驱动器上的大量空间。

#### 不压缩(Uncompressed)

采用不压缩模式保存文件。

#### 按现状(As Is)

采用原始压缩模式保存文件，而不要压缩或解除压缩文件。“按现状”(As Is)是默认设置。

**注**

若要使用压缩模式，请确保在计算机上的相应路径中安装了 zip 实用程序。例如，在 Windows 上保存压缩文件之前，必须执行下列操作：

- 安装 gzip

- 将 gzip 在系统上的位置路径添加到系统环境变量中。gzip 的默认路径为 C:\Program Files (x86)\GnuWin32\bin

## 显示层(Display Layer)

#### 文件导入合并(File import merge)

指定在导入文件时希望“显示层”(Display Layer)合并的方式。

#### 无(None)

读入的所有层都被放置在新层中、重新编号并重命名（如有必要）以保留唯一性。

#### 按编号(By Number)

读入的与现有层具有相同索引编号的所有层都与该层合并，而不是创建新的层。

#### 按名称(By Name)

读入的与现有层具有相同名称的所有层都与该层合并，而不是创建新的层。

## 渲染层(Render Layer)

#### 文件导入合并(File import merge)

指定在导入文件时希望“渲染层”合并的方式。

#### 无(None)

读入的所有层都被放置在新层中、重新编号并重命名（如有必要）以保留唯一性。

#### 按编号(By Number)

读入的与现有层具有相同索引编号的所有层都与该层合并，而不是创建新的层。

#### 按名称(By Name)

读入的与现有层具有相同名称的所有层都与该层合并，而不是创建新的层。

## 文件对话框(File Dialog)

#### 对话框样式(Dialog style)

#### 本地操作系统(OS native)

在执行保存、打开、导入和导出操作时使用当前操作系统的本地文件浏览器。

#### Maya 默认(Maya default)

在执行保存、打开、导入和导出操作时使用 Maya 的内置文件浏览器。

#### 在过滤器中隐藏扩展名(Hide extensions in filter)

如果您不希望文件扩展名（例如 *.ma、*.mb）显示在“文件 > 打开”(File > Open)窗口的“文件类型”(Files of Type)字段中，则激活“在过滤器中隐藏扩展名”(Hide extensions in filter)。

## 版本(Version)

#### 忽略版本(Ignore Version)

打开、导入或引用 Maya 文件时忽略文件版本。通过“忽略版本”(Ignore Version)首选项，可以打开由任意版本的 Maya 创建的文件，不管文件保存格式是 ASCII 还是二进制。如果需要在早期版本中打开文件，使用该功能就无需保存，也无需手动编辑 ASCII 版本的 Maya 文件来移除所需的版本行。

“忽略版本”(Ignore Version)首选项适用于“文件 > 打开场景”(File > Open Scene)、“文件 > 导入”(File > Import)和“文件创建引用命令”(File Create Reference commands)。

**注**

在早期版本 Maya 中打开的 Maya 文件不受支持，因为无法确保功能是否与早期版本兼容。例如，在 Maya 2016 中保存为 Maya 二进制文件的场景与先前版本的 Maya 不兼容。

“忽略版本”(Ignore Version)

选项主要用于同时使用多个版本 Maya 的生产环境。

**注**

从 Maya 2012 开始，对于 Linux 和 Mac 平台，在 Maya 尝试使用由 lastLocalWS 指向的目录之前，需要通过检查来确保该目录可访问。该目录必须具有 555 (r-xr-xr-x) 权限。否则，如果该目录仅具有 444 (r--r--r--) 权限，则 Maya 不能使用它；即使 cd 或 ls 不起作用也是如此。

除 lastLocalWS 之外，Maya 在启动时还尝试使用其他的工作区，而对这些工作区也将应用相同的检查。Maya 尝试使用这些工作区的顺序如下：

- 从 -proj 命令行参数获取的值

- 从 MAYA_PROJECT 环境变量获取的值

- InitialProject optionVar（即标记为“始终使用此项目启动”(Always start in this project)的首选项）

- lastLocalWS optionVar（在退出时由 Maya 自动存储，以记住上一活动工作区）

- 默认项目

## 图像文件

#### 自动重新加载更新的图像文件(Automatically reload updated image files)

启用后，Maya 会自动刷新已更新并保存在其他应用程序中的文件纹理。默认情况下，此选项处于禁用状态。

## 文件打开错误对话框(File Open Error Dialog)

激活**“可以抑制错误对话框”(Can Suppress Error Dialog)**可针对在文件加载时出现的无法识别的自定义节点、数据类型或插件隐藏错误对话框。警告/错误消息继续显示在“脚本编辑器”(Script Editor)中。

激活后，错误对话框抑制将一直有效，直到禁用此设置或重置“首选项”(Preferences)为止。

## 脚本编辑器(Script Editor)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 3474 字 ≥300，非承重" -->

选择没有 PEP-263 标头时 Python 文件编码的行为。

#### Python 文件编码(Python files encoding)

默认情况下，Maya 以 UTF-8 格式保存 Python 文件。

- 选择 **UTF-8**，以便在没有 PEP-263 标头时，使用 UTF-8 编码保存文件。加载时，Maya 先使用 UTF-8 进行解码，如果失败，则改用本地编码。UTF-8 是 Python 标准，支持整个 Unicode 字符集，但仍然能够读取系统编码文件以支持旧版。

- 选择**“系统编码”(System Encoding)**以使用旧版 Maya 模式，从而确保向后和向前兼容性。如果要创建的文件可能会在早期版本的 Maya 中使用（例如，在 Maya *2021* 中创建文件，但打算还在 Maya *2019* 中使用），则选择此选项。

#### 将 PEP-263 标头添加到非 ASCII Python 文件(Add a PEP-263 header to non ascii python files)

激活此选项可添加 PEP-263 标头，以在使用 Python 导入加载代码时提高兼容性。
