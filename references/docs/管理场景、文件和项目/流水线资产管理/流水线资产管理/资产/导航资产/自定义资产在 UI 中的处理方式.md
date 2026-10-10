# 自定义资产在 UI 中的处理方式

可以使用脚本自定义资产与 Maya UI 的交互方式。例如，如果已创建一个封装了许多着色器或材质的资产，那么让该资产显示在当您使用鼠标右键 (![图：可以使用脚本自定义资产与 Maya UI 的交互方式。例如，如果已创建一个封装了许多着色器或材质的资产，那么让该资产显示…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-EAD82E7D-F5FF-4F03-BB2B-BAB585D26B88.png) <!-- baize:img-hook downloaded=false reason="正文 384 字 ≥300，非承重" -->) 单击对象时出现的“指定现有材质”(Assign Existing Materials)列表中可能会非常有用。

自定义资产在 UI 中的处理方式

1. 在“大纲视图”(Outliner)中选择资产。

2. 打开“属性编辑器”(Attribute Editor)。

3. 在资产选项卡的“资产属性”(Asset Attributes)区域下，单击“UI 处理”(UI Treatment)。

4. 执行下列操作之一：

  - 如果要将资产作为着色器处理，请从下拉菜单中选择“着色器”(Shader)。

  - 如果要指定其他一些自定义处理方式，请从下拉菜单中选择“自定义”(Custom)，然后在“自定义处理”(Custom Treatment)字段中输入字符串。然后可以编写使用该字符串的自定义脚本或插件。
