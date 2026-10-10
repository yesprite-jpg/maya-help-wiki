# 重置 Maya 首选项

重置 Maya 首选项可能是有效解决许多已发生问题的第一步，如缺少菜单、无法启动或在顶点模式下移动对象时性能降低。

通过重命名或删除目录移除首选项后，Maya 会在下次运行应用程序时创建新的首选项。这会将工具和选项刷新为其默认值，并且通常可快速修复任何新的异常工具行为。

**注**

如果您只希望在

“首选项”(Preferences)窗口

中返回到出厂默认设置，请从菜单栏中选择

“编辑 > 还原默认设置”(Edit > Restore Default Setting)

（在

“类别”(Categories)

部分上方）。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-30DB3CC8-0D41-4B6A-889C-705E2351D73C.gif) <!-- baize:img-hook downloaded=false reason="正文 968 字 ≥300，非承重" -->

**注**

提示：

为确保

Maya

始终顺利运行，每次安装新的 Hotfix、Service Pack 或 Update 版本时都移除首选项可能特别有用。

在移除首选项之前，请检查是否已将任何数据保存在受影响的目录中，然后创建所需的任何备份。（例如，如果已将图像保存 \projects\default\renderData 或 \projects\default\images 目录中。）

移除所有首选项

1. 查找以下目录：

  - **Windows：** <驱动器>:\Documents\maya\<版本>\

  - **Mac OS X：** /Users/<用户名>/Library/Preferences/Autodesk/maya/<版本>/

  - **Linux：/home/<用户名>/maya/<版本>/**

  **注**

  提示：

  prefs

  文件夹与

  presets

  和

  scripts

  文件夹位于同一文件夹中。

2. 删除目录，或者如果要保存副本，则对其进行重命名（例如，/myprefs_backup/）。

  **强烈建议重命名目录**，因为如果此过程无法解决该问题，则可选择使用它恢复首选项。

3. 重新启动 Maya，然后选择创建默认首选项的选项（如果提示）。

  Maya 会在相同的位置中重新创建默认首选项目录。界面将恢复为“出厂默认值”布局。

**注**

重要：

如果您希望采用更具迭代性的疑难解答方法，则可仅移除首选项目录的一个子集。例如，先仅移除

..\<版本> \projects\default\autosave

目录，看看这样能否解决您遇到的问题。如果问题仍然存在，则可尝试先移除

..\ <版本> \projects\default\clips

，然后移除

..\ <版本>\projects\default\data

，依此类推。
