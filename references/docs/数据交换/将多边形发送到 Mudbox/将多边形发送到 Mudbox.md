# 将多边形发送到 Mudbox

您可以在 Maya 和 Mudbox 之间发送各种数据，如网格、网格上的 UV 以及与网格相关联的材质。然后，您可以使用 Mudbox“文件”(File)菜单中的“发送到 Maya”(Send to Maya)命令，将绘制或雕刻层添加到 Mudbox 中的对象，并将其发送回 Maya。

**注**

只有具有

Maya

和 Mudbox 的匹配版本，

“发送到 Mudbox”(Send to Mudbox)

才在

“文件”(File)

菜单中可用。（

Maya

2016 和 Mudbox 2016 是匹配版本。）

将对象从 Maya 发送到 Mudbox

1. 在 Maya 中，选择要发送的对象。

  **注**

  只能将多边形对象发送到 Mudbox。

2. 选择文件(File) > 发送到 Mudbox(Send to Mudbox)，然后从以下选项中进行选择：

  - 作为新场景发送(Send as New Scene)。

    在 Mudbox 中打开新场景，并发送选定对象。如果在场景中有选定的对象，则只会发送这些对象；否则，会发送整个场景。

  - 更新当前场景(Update Current Scene)。

    仅在 Mudbox 运行时可用。通过发送当前选择，更新 Mudbox 场景。如果未选择任何对象，则此选项将发送先前发送的相同选择。

    **注**

    您也可以单击状态栏中的

    “更新”(Update)

    按钮以更新当前场景。

    **提示：**更新当前场景之前，逐步减低至级别 0，或者减低至当源网格和目标网格在形状中彼此接近时细节传输效率最佳时与 Maya 网格对应的任何级别。

  - 添加到当前场景(Add to Current Scene)。

    只有正在运行 Mudbox 时才可以使用。将当前选择发送到 Mudbox。将已发送的全部选定对象都复制至 Mudbox 场景。

  界面的底部显示连接指示器。

  ![图：选择文件(File) 发送到 Mudbox(Send to Mudbox)，然后从以下选项中进行选择： 作为新场景发送(…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-34EC2A3B-A9F0-4699-BCA8-F27F245237CB.png) <!-- baize:img-hook downloaded=false reason="正文 938 字 ≥300，非承重" -->

**注**

如果在“发送到”(Send to)操作期间存在与对象匹配的问题，将出现错误消息，显示不匹配对象的列表。该消息将转至 Mudbox 中的日志窗口。

Maya 会将您的对象发送到 Mudbox，自动指定添加到新对象的任何纹理。如果您正在更新场景，必须手动添加纹理。

将纹理添加到已更新的场景

1. 选择要将纹理添加到的对象。

2. 在模型上单击鼠标右键，然后选择“指定现有材质”(Assign Existing Material)。

## 相关主题

- [将对象发送到 Autodesk 应用程序](../将对象发送到其他应用程序/将对象发送到其他应用程序.md)

- [从 Mudbox 接收对象](将多边形发送到%20Mudbox/从%20Mudbox%20接收对象.md)

- [Suites 特定的环境变量](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4CC2471C-5801-4663-85ED-0C5104897FD8)
