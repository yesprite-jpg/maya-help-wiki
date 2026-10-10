# 将 FBX 文件导入到 Maya

本部分介绍如何使用 Maya FBX 插件导入文件：

要导入 FBX 文件，请执行以下操作：

1. 启动 Maya。

2. 选择文件 > 导入(File > Import)。

3. 从“文件导入”(File Import)对话框中，找到要导入的 FBX 文件。

4. 从“文件类型”(File of Type)菜单中，选择 FBX 文件扩展名。

  **注**

  如果 FBX 文件扩展名未显示在

  “文件类型”(File of Type)

  菜单中，则在 Maya

  插件管理器

  中激活

  fbxmaya.mll

  。

5. 如果在 Maya“导入”(Import)对话框右侧看不到“FBX 导入”(FBX Import)选项，请向下滚动。

  ![图：如果在 Maya“导入”(Import)对话框右侧看不到“FBX 导入”(FBX Import)选项，请向下滚动。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-A987A3C7-5409-457D-AC87-918F10C9A859.gif) <!-- baize:img-hook downloaded=false reason="正文 728 字 ≥300，非承重" -->

6. 设置要使用的导入选项，或者从“预设”(Presets)菜单选择一个预设。“Autodesk Media & Entertainment”预设包含适用于一般动画工作流的最佳平衡选项。

  **注**

  提示：

  如果要使用“Maya 到 MotionBuilder，再返回到 Maya”工作流，请使用“Autodesk MotionBuilder”

  预设。

  有关 Autodesk 预设以及适用于您的导入选项的信息，请参见 [FBX 导入选项](FBX%20导入选项.md)中的“导入预设”。

7. 单击 Maya“导入”(Import)对话框中的“导入”(Import)。

  **注**

  要取消导入过程，请按 ESC 键。

8. 如果导入过程中出现转化或错误，则警告管理器会在导入过程结束时报告这些问题。有关“警告管理器”(Warning Manager)的信息，请参见 [FBX 导入选项](FBX%20导入选项.md)主题中的“显示/隐藏警告管理器”(Show/Hide Warning Manager)。

  **注**

  “错误”和“警告”之间存在差别。当出现异常情况时，插件会报告错误。如果插件报告错误，则表示错误的后果未知。当插件对源数据应用转化以使其转化为目标应用程序可以读取的格式时，将会出现警告提醒用户。
