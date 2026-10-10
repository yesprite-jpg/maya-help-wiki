# 每当 Maya 启动时都运行 MEL 命令

当 Maya 启动时，都会运行 userSetup.mel 文件中的任何命令。您可以使用此文件来设置您的工作环境或执行常用的 MEL 命令（如锯齿）。

userSetup.mel/userSetup.py 脚本将在 Maya 初始化和设置阶段执行，因此只有用于设置工作环境且不依赖于 Maya 功能的命令才能在此脚本中成功运行。

在 Maya 每次启动时都运行一组特定的 MEL 命令

1. 在以下文件夹中创建名为 userSetup.mel 或 userSetup.py 的文件：

  - Windows：..\My Documents\maya\<版本>\scripts

  - Mac OS X：~/Library/Preferences/Autodesk/maya/<version>/scripts

  - Linux：~/maya/<version>/scripts

  (其中 ~ 是主文件夹)

2. 在 userSetup.mel 文件中，键入要让 Maya 在启动时运行的命令。

**注**

您可以通过

“安全”(Security)首选项

控制 Maya 是否自动读取/执行 userSetup。
