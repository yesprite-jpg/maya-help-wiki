# 获得在“节点编辑器”(Node Editor)中显示的节点列表

您可以使用 -getNodeList 标志输出在“节点编辑器”(Node Editor)中显示的节点名称列表。

按如下在命令行中使用标志：

nodeEditor -q -getNodeList (nodeEditorName)

**注**

若要查询

“节点编辑器”(Node Editor)

面板的名称，请输入以下内容：

getPanel -scriptType "nodeEditorPanel";

您获得的结果将类似于以下内容：

// Result: nodeEditorPanel1 nodeEditorPanel2 //

nodeEditorPanel1 是在 Maya 主窗口中构建的编辑器，而 nodeEditorPanel2 是浮动的编辑器。

将 NodeEditorEd 附加到上面的结果中，例如 nodeEditorPanel2NodeEditorEd。

因此，完整的命令为：nodeEditor -q -getNodeList nodeEditorPanel2NodeEditorEd;
