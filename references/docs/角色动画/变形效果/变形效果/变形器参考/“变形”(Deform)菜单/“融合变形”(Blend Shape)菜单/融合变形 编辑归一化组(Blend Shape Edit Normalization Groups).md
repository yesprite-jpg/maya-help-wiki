# 融合变形 > 编辑归一化组(Blend Shape > Edit Normalization Groups)

- 在“动画”(Animation)、“绑定”(Rigging)和“建模”(Modeling)菜单集中：“变形 > (编辑)融合变形 > 编辑归一化组”(Deform > (Edit) Blend Shape > Edit Normalization Groups)

通过归一化组可以定义一组目标，使用[“组件编辑器”(Component Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B698CC5D-2771-488E-98E8-2D4E31DB3B2D)或[“绘制融合变形权重工具”(Paint Blend Shape Weights Tool)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E49E9C30-D03A-456D-B7E8-FF99DA8C11E4.htm)对这些目标进行编辑时，这些目标的权重总和将归一化为 1.0。请参见[绘制融合形变变形器权重](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-950716A4-19CF-4C14-96F1-FD6B4D48663C.htm)。

创建归一化组的步骤

1. 打开“编辑归一化组”(Edit Normalization Groups)窗口（“变形 > (编辑)融合变形 > 编辑归一化组”(Deform > (Edit) Blend Shape > Edit Normalization Groups)）。

  “编辑归一化组”(Edit Normalization Groups)窗口会列出当前场景中的所有融合变形。

2. 为每个融合变形指定组编号。

  （例如，如果列出了三个融合变形，则可以在第一个目标旁输入 1 以将其指定给组 1，然后在后面的两个目标旁输入 2 以将它们添加到归一化组 2）。

创建归一化组后，它们将在“组件编辑器”(Component Editor)中显示为新列，并在“绘制融合变形权重工具”(Paint Blend Shape Weights Tool)中显示为新的可绘制目标。
