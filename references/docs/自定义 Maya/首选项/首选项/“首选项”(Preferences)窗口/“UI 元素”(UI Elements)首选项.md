# “UI 元素”(UI Elements)首选项

可以在[首选项(Preferences)窗口](../“首选项”%28Preferences%29窗口.md)的“UI 元素”(UI Elements)类别中设置以下首选项。

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

## 可见 UI 元素(Visible UI Elements)

在 Maya 窗口中隐藏或显示这些 UI 元素。此外，您还可以从“窗口 > UI 元素”(Windows > UI Elements)菜单控制该显示。

## 主窗口中的编辑器(Editor in Main Window)

可选择显示或隐藏该编辑器。该编辑器可以是“属性编辑器”(Attribute Editor)、“工具设置”(Tool Settings)或通道盒/层编辑器之一。您还可以从“窗口 > UI 元素”(Windows > UI Elements)菜单或“状态行”(Status Line)最右侧的三个图标控制该显示。

## 面板配置(Panel Configurations)

#### 保存时(When saving)

启用“将面板布局与文件一起保存”(Save panel layouts with file)时，面板布局会与场景文件一同保存。默认设置为启用。

**注**

提示：

在将对象/子场景用作被引用文件时，请禁用该选项。默认情况下，Maya 会在每个场景文件 (.ma/.mb) 中记住有关已打开的每个编辑器的所有情况，如位置、大小、特定于窗口的选项等。它在名为 *uiConfigurationScriptNode* 的脚本节点上另存为一个属性，显示为添加到节点的字符串值属性的 MEL 代码。

#### 打开时(When opening)

如果启用，该选项会从文件中还原已保存的布局。默认设置为启用。

#### 启动新场景(Starting new scenes)

可以为新场景指定布局。

#### 保持当前布局(Keep current layout)

为新场景保持当前布局。

#### 使用下面指定的布局(Use layout specified Below)

基于从下拉菜单中选定的布局创建新场景。默认设置为“单个透视视图”(Single Perspective View)。

#### 在新场景: 重置视口面板设置(Reset viewport panel settings)

取消选择此选项，以便面板首选项（例如，“线框”(Wireframe)等着色模式或“使用所有灯光”(Use All Lights)等照明模式）均随 Maya 的会话一起保存。

如果选择此选项，启动 Maya 的新会话时所有面板设置都将重置。
