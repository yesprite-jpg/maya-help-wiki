# 从 Mudbox 接收对象

您可以使用 Mudbox“文件”(File)菜单中的“发送到 Maya”(Send to Maya)选项，将对象从 Mudbox 发送到 Maya。您可以发送在 Mudbox 中创建的新对象或更新最初从 Maya 发送到 Mudbox 的对象。将绘制层或雕刻层应用到 Mudbox 中的对象之后，可以使用与“发送到 Maya”(Send to Maya)选项关联的首选项选择将这些层发送到 Maya 的方式。

将对象从 Mudbox 发送到 Maya

1. 在 Mudbox 中，选择要发送的对象。

  **注**

  如果没有选择特定对象，Mudbox 将发送场景中的所有对象。

2. 选择“文件 > 发送到 Maya”(File > Send to Maya)，然后从以下选项中进行选择：

  - 发送选定对象作为新场景(Send Selected as New Scene)：在 Maya 中打开一个新场景，并从 Mudbox 发送选定对象。

  - 更新当前场景(Update Current Scene)：使用在 Mudbox 中添加的任何绘制层或雕刻层更新场景。

    **注**

    您也可以单击状态栏中的

    “更新”(Update)

    按钮以更新当前场景。

  - 更新当前场景中的纹理(Update Textures in Current Scene)：使用 Mudbox 中的绘制层仅更新对象的纹理。

  - 将选定对象添加到当前场景(Add Selected to Current Scene)：将选定对象添加到现有 Maya 场景中。

  - 选择以前发送的对象(Select Previously Sent Objects)：选择最近发送的对象。

  - 单击“首选项”(Preferences)，打开“发送首选项”(Send Preferences)，并控制绘制层和雕刻层在应用程序之间的移动方式。

    有关在 Mudbox 中“发送首选项”(Send Preferences)的详细信息，请参见 Mudbox 帮助。例如，可以对雕刻层首选项进行设置，以确定在发送到 Maya 时是否将雕刻层转化为融合变形。

  当应用程序连接时，在状态栏中将显示连接状态指示器 ![图：当应用程序连接时，在状态栏中将显示连接状态指示器 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-4AF0646E-70E2-47B0-A249-59B626A8ADF5.png) <!-- baize:img-hook downloaded=false reason="正文 834 字 ≥300，非承重" -->。

## 相关主题

- [将对象发送到其他 Autodesk 应用程序](../../将对象发送到其他应用程序/将对象发送到其他应用程序.md)
