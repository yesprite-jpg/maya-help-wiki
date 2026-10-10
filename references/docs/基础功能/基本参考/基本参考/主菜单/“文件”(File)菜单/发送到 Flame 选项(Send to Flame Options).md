# 发送到 Flame 选项(Send to Flame Options)

使用这些选项可设置选择“文件 > 发送到 Flame”(File > Send to Flame)时会发生什么变化。另请参见[将对象发送到 Flame](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7A8C79E4-7A27-4D96-9797-B346C7F14FAD)。

**注**

仅当有匹配的

Maya

和 Flame 版本时，

“发送到 Flame”(Send to Flame)

在 Maya 的

“文件”(File)

菜单中才可用。（Maya 2020 和 Flame 2020 是匹配的版本。）

#### 作为新场景发送(Send as New Scene)

在 Flame 中打开新场景，并从 Maya 发送选定对象。

如果 Flame 未在运行，此选择将打开 Flame。如果 Flame 正在运行，系统将提示保存到当前场景或取消。选择**“取消”**将停止发送操作。

如果在 Maya 场景中有选定的对象，则只会发送这些对象；否则，会发送整个 Maya 场景。

#### 更新当前场景(Update Current Scene)

仅在 Flame 运行时可用。通过发送当前 Maya 选择来更新 Flame 场景。如果未选择任何对象，则此选项将发送先前发送的选择。

#### 添加到当前场景(Add to Current Scene)

仅在 Flame 运行时可用。将当前选择发送到 Flame。已发送的所有选定对象都会在 Flame 场景中进行复制。

#### 选择以前发送的对象(Select Previously Sent Objects)

选择在最后一个“作为新场景发送”(Send as New Scene)、“更新当前场景”(Update Current Scene)或“添加到当前场景”(Add to Current Scene)操作期间发送给 Flame 的对象。如果之前同时发送了多个对象，则此命令将选择全部对象。但是，如果是分别发送多个对象，则此命令将仅选择最近发送的对象。

该选项可用于方便地查看已共享的对象，并选择要添加到所选项中的对象。
