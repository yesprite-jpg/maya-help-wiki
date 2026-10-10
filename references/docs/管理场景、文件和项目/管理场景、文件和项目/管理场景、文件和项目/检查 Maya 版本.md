# 检查 Maya 版本

您可以检查安装了哪个版本的 Maya 版本以及是否安装了 Service Pack。

选择主[“帮助”(Help)菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E1AB1D0E-88F6-4CDC-A110-407F75FE660C)选项中的**“关于 Maya”(About Maya)**时，将显示 Maya 版本。此时将显示**“关于 Autodesk Maya”(About Autodesk Maya)**窗口。“版本”(Version)和“识别编号”(Cut)显示在窗口左上角。

#### 版本

版本号位于 Maya 主菜单中。如果存在 Service Pack 或 Extension，它们将显示在版本号后面。例如，**Autodesk Maya 2015 SP6**。

#### 识别编号

识别编号显示您当前正在运行的软件的内部版本号。此编号对支持问题很有用。

## 使用命令行确认版本

您可以使用命令来确定您的 Maya 版本：

mayabatch.exe -v

例如

- Windows：d:\branch\maya\builds\main\build>Release\runTime\bin\maya -v

- Mac 和 Linux：optim/runTime/Maya.app/Contents/MacOS/Maya -v
