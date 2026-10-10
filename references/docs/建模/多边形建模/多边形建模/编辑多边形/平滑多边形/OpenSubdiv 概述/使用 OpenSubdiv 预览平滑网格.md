# 使用 OpenSubdiv 预览平滑网格

默认情况下，平滑网格预览使用“细分方法”(Subdivision Method)，该方法在[“建模首选项”(Modeling preferences)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F40D8133-73D3-4A1B-8332-4C8E46FFA1E6#GUID-F40D8133-73D3-4A1B-8332-4C8E46FFA1E6__GUID-9E94DA3D-17D3-483E-AE4C-260F1610A274)中设置。此设置为全局首选项，会影响场景中所有新的和现有的对象。

**注**

提示：

在

属性编辑器

中，选择 polyShape 选项卡，打开

“平滑网格”(Smooth Mesh)

面板，然后禁用

“使用全局细分方法”(Use global subdivision method)

选项。这样做将覆盖全局首选项，因此可以基于每个对象设置

“细分方法”(Subdivision Method)

。

使用 OpenSubdiv 预览平滑网格

1. 选择您要平滑的网格。

2. 执行下列操作之一：

  - 按 1 键可关闭“平滑网格预览”(Smooth Mesh Preview)。

  - 按 2 键启用“框架 + 平滑网格”(Cage + Smooth Mesh)显示模式。

    Maya 会同时显示原始网格（作为线框框架）和平滑预览，这样您可以选择任一版本网格上的组件。

  - 按 3 键启用“平滑网格”(Smooth Mesh)显示模式。

    Maya 仅显示平滑预览。当您直接在平滑预览上选择和编辑组件时，更改将反映回原始网格上。

3. 在“属性编辑器”(Attribute Editor)中，选择“polyShape”选项卡 >“平滑网格 > OpenSubdiv 控件”(Smooth Mesh > OpenSubdiv Controls)。

  调整显示的 [OpenSubdiv 控件(OpenSubdiv Controls)](../../../多边形建模参考/多边形节点/平滑网格%28Smooth%20Mesh%29.md#GUID-FF35F773-1FC0-4EBA-A64C-6199375F489A__SECTION_AEC2592F09DA47ACBB9901F1310E01E9)。

4. （可选）[将平滑网格预览转化为多边形](../平滑网格预览概述/将平滑网格预览转化为多边形.md)。

## 相关主题

- [OpenSubdiv 概述](../OpenSubdiv%20概述.md)

- [平滑网格(Smooth Mesh)](../../../多边形建模参考/多边形节点/平滑网格%28Smooth%20Mesh%29.md)
