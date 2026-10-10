# 在日语或简体中文环境中运行英语 Maya

现在许多日语/简体中文 Maya 用户可能已经适应了在英语语言 Maya 用户界面中进行工作。

如果在使用日语/简体中文语言环境的 Windows 操作系统时希望使用英语 Maya，可以通过设置 MAYA_UI_LANGUAGE 环境变量实现此操作。

在日语/简体中文环境中运行英语 Maya (Windows)

1. 在 Windows 桌面的“我的电脑”(My Computer)图标上单击鼠标右键，然后从显示的下拉列表中选择“属性”(Properties)。

  **注**

  在 Windows 7 的计算机名称上单击鼠标右键，然后依次选择“特性”(Properties)和“高级系统设置”(Advanced system settings)。

2. 在“系统属性”(System Properties)窗口中，单击“高级”选项卡。

3. 单击“环境变量”(Environment Variables)按钮。

  将显示“环境变量”(Environment Variables)窗口。

4. 在“<userlogin> 的用户变量”区域中，单击“新建”(New)。

5. 在“变量名”(Variable Name)文本字段中键入：MAYA_UI_LANGUAGE

6. 在“变量值”(Variable Value)文本字段中键入：en_US

7. 启动 Maya。

  **注**

  如果以后要运行日语/简体中文 Maya，可以将环境变量值设置为 ja_JP （针对日语）和 zh_CN（针对简体中文）或从环境变量列表中移除该变量。

  **注**

  警告：

  必须通过系统首选项设置 MAYA_UI_LANGUAGE 环境变量。在 Maya.env 文件中

  环境变量不会

  对

  Maya

  的行为产生影响。

在日语/简体中文环境中运行英语 Maya (Mac OS X)

1. 在“系统偏好”(Systems Preferences)的“语言与文本”(International preferences)区域中，暂时将语言设置为英语。

## 相关主题

- [运行日语或简体中文用户界面的 Maya](运行日语或简体中文界面的%20Maya.md)

- [日语/简体中文 Maya 概述](../日语简体中文%20Maya.md)

- [准备包含日语或简体中文文本的 Maya 文件](准备包含日语或简体中文文本的%20Maya%20文件.md)
