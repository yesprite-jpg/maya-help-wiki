# FBX 预设存储位置

可将自定义预设保存在可与其他用户共享的文件中。请参见下表以了解保存预设的位置。

| 平台 | 预设位置 |
|---|---|
| Windows | C:/Users/<用户名>/Documents/maya<当前版本>/plug-ins/fbx/plug-ins/import |
| Macintosh | /Users/<用户名>/Library/Preferences/Autodesk/maya<当前版本>/plug-ins/fbx/plug-ins/import |
| Linux | /home/<用户名>/maya<当前版本>/plug-ins/fbx/plug-ins/import |
| 注： 以上表格显示了导入预设的路径。导出预设遵循相同的路径，但改为使用“export”。 |  |

预设文件具有文件扩展名 .fbximportpreset（用于导入）和 .fbxexportpreset（用于导出），例如，My Preset.fbximportpreset。

这些预设按用户名进行存储，以便多个用户能够在同一台计算机上存储自定义预设。

也可以运行以下 MELscript 命令找到 FBX 用户的预设路径：internalVar -userAppDir
