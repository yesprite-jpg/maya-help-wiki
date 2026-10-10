# 安装 Maya 插件

以下说明对于所有 Linux、Windows 和 Mac OS X 平台是通用的。

1. 在插件目录中，创建三个文件夹：plug-ins、scripts 和 icons。

  将插件文件放置在 /plug-ins 文件夹中。

  如果插件包含脚本，则将脚本文件放置在 /scripts 文件夹中。

  如果插件包含图标，则图标文件放置在 /icons 文件夹中。

  **注**

  警告：

  不建议

  将插件文件复制到 Maya 安装目录，因为它可能会损坏 Maya 的安装。

2. 在名为 Maya.env 的文件中定义以下环境变量：

  - MAYA_PLUG_IN_PATH - 搜索插件的目录。将该目录设置为 /plug-ins 文件夹。

  - MAYA_SCRIPT_PATH - 搜索 MEL 和 Python 脚本的目录。将该目录设置为 /scripts 文件夹。

  - XBMLANGPATH - 搜索图标的目录。将该目录设置为 /icons 文件夹。

  **注**

  提示：

  您可以将插件目录随意放置到任何路径（Maya 安装目录除外），只要通过其各自的环境变量正确指向每个

  plug-ins

  、

  scripts

  和

  icons

  文件夹即可。

  有关 Maya.env 文件的详细信息（包括其应保存到每个平台的位置），请参见[使用 Maya.env 设置环境变量](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8EFB1AC1-ED7D-4099-9EEE-624097872C04)。使用 Maya.env 可以通过简单地复制文件轻松地在其他系统上设置相同的运行时环境。您仍然可以在命令行上为这些变量设置明确的值，并为 Maya.env 附加这些值。

3. 在 Maya 中，选择“窗口 > 设置/首选项 > 插件管理器”(Window > Settings/Preferences > Plug-in Manager)以打开“插件管理器”(Plug-in Manager)。插件将显示在列表中。选择“已加载”(Loaded)以加载插件。

**注**

提示：

作为设置环境变量以指向插件的文件的替代方法，您可以将 plug-in/scripts/icons 文件复制到 Maya 默认指向的目录。查看这些目录的最简单方法是使用 Maya“脚本编辑器”(Script Editor) 中的 getenv 命令。例如，

```text
getenv MAYA_PLUG_IN_PATH
```

第三个选择是，可以单击“插件管理器”(Plug-in Manager)中的“浏览”(Browse)按钮以导航至插件。

**注**

环境变量 MAYA_APP_DIR 可用于帮助查找 Maya.env 文件。如果未设置此变量，Maya 可能查找以下目录：

- (Linux) $HOME/maya

- (Mac OS X) $HOME/Library/Preferences/Autodesk/maya

- (Windows) \Users\<用户名>\Documents\maya

此外，如果您在系统上安装有多个 Maya 版本，则可以将 Maya.env 文件放置在 MAYA_APP_DIR 环境变量所指向目录或以下目录中受版本控制的子目录中：

- (Linux) $HOME/maya

- (Mac OS X) $HOME/Library/Preferences/Autodesk/maya

- (Windows) \Users\<用户名>\Documents\maya

例如，如果将 MAYA_APP_DIR 设置为 /usr/mydir，则可以在仅当运行指定版本的 Maya 时才使用的目录 /usr/mydir/<*版本*>（例如，对于 Maya 2018 为目录 /usr/mydir/2018）中创建 Maya.env 文件。如果未设置 MAYA_APP_DIR，则可以将特定版本的 Maya.env 文件放置在以下目录中：

- (Linux) $HOME/maya/<*版本*>

- (Mac OS X) $HOME/Library/Preferences/Autodesk/maya/<*版本*>

- (Windows) \Users\<用户名>\Documents\maya\<*版本*>
