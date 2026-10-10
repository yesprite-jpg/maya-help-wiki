# 从可见渲染层导出“渲染设置”(Render Settings)和 AOV 并将其应用于新场景

处理渲染层以及创建“渲染设置”(Render Settings)和 AOV 覆盖时，您可能希望导出应用覆盖值的“渲染设置”(Render Settings) 的 .json 文件，然后将此预设导入到新场景中。同样，您可能希望导出和导入应用覆盖值的 AOV。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1715 字 ≥300，非承重" -->

导出在当前层中应用覆盖值的渲染设置

1. 确保包含要导出的覆盖值的层设置为可见。

2. 在“渲染设置”(Render Setup)编辑器中选择“文件 > 导出可见层渲染设置”(File > Export Visible Layer Render Settings)。

  也可以在“渲染设置”(Render Settings)窗口中选择“预设 > 导出渲染设置”(Presets > Export Render Settings)，或者在“渲染设置”(Render Setup)编辑器的“场景 > 渲染设置”(Scene > Render Settings)部分中单击 ![图：也可以在“渲染设置”(Render Settings)窗口中选择“预设 导出渲染设置”(Presets Export R…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-15A05717-B953-472A-B6FC-39C64A718DC9.png) <!-- baize:img-hook downloaded=false reason="正文 1715 字 ≥300，非承重" -->。将显示一个对话框，通知您在可见渲染层中应用的覆盖将包括在导出的 .json 文件中。

  导出的文件将保存到用户预设位置，默认情况下为 <Documents>\maya\Presets。有关详细信息，请参见[全局预设和用户预设](将“渲染设置”%28Render%20Settings%29作为预设导出和导入.md#GUID-469A3F38-8E0B-4A28-8913-D8A7E3EF0733__SECTION_1B399EB0AAA34C16AA60AD650DC96FC7)。

  **注**

  提示：

  从

  “渲染设置”(Render Setup)

  编辑器中选择

  “首选项 > 渲染首选项”(Preferences > Rendering Preferences)

  ，可以更改预设的位置。

3. 在新场景中，从“渲染设置”(Render Setup)编辑器中选择“文件 > 导入场景渲染设置”(File > Import Scene Render Settings)。

  .json 将作为预设应用到新场景中。

  **注**

  有关导入预设的其他方式，请参见

  将“渲染设置”(Render Settings)作为预设导出和导入

  。

在此示例中，选择“文件 > 导出可见层渲染设置”(File > Export Visible Layer Render Settings)将创建包括以下值的 .json：“AA 采样最大值”(AASamples Max)值设置为 5，运动模糊处于禁用状态，宽度和高度值设置为 1280x720。换句话说，覆盖值应用于导出的预设。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-84BD6148-ABAA-4D3A-8512-F10B9A2C4D19.png) <!-- baize:img-hook downloaded=false reason="正文 1715 字 ≥300，非承重" -->

导出在当前层中应用覆盖值的 AOV

1. 确保包含要导出的覆盖值的层设置为可见。

2. 在“渲染设置”(Render Setup)编辑器中选择“文件 > 导出可见层 AOV”(File > Export Visible Layer AOVs)。

  也可以在“渲染设置”(Render Settings)窗口中选择“预设 > 导出 AOV”(Presets > Export AOVs)，或者在“渲染设置”(Render Setup)编辑器的“场景 > AOV”(Scene > AOVs)部分中单击 ![图：也可以在“渲染设置”(Render Settings)窗口中选择“预设 导出 AOV”(Presets Export A…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-15A05717-B953-472A-B6FC-39C64A718DC9.png) <!-- baize:img-hook downloaded=false reason="正文 1715 字 ≥300，非承重" -->。将显示一个对话框，通知您在可见渲染层中应用的覆盖将包括在导出的 .json 文件中。

  导出的文件将保存到用户预设位置，默认情况下为 <Documents>\maya\Presets。有关详细信息，请参见[全局预设和用户预设](将“渲染设置”%28Render%20Settings%29作为预设导出和导入.md#GUID-469A3F38-8E0B-4A28-8913-D8A7E3EF0733__SECTION_1B399EB0AAA34C16AA60AD650DC96FC7)。

  **注**

  提示：

  从

  “渲染设置”(Render Setup)

  编辑器中选择

  “首选项 > 渲染首选项”(Preferences > Rendering Preferences)

  ，可以更改预设的位置。

3. 在新场景中，从“渲染设置”(Render Setup)编辑器中选择“文件 > 导入场景 AOV”(File > Import Scene AOVs)。

  应用覆盖值的 AOV 将添加到新场景中。

  **注**

  有关导入 AOV 的其他方法，请参见

  导出和导入 AOV

  。

在此示例中，选择“文件 > 导出可见层 AOV”(File > Export Visible Layer AOVs)将创建 .json，其中直接 AOV 处于禁用状态，“Png 格式”(Png Format)设置为 int16（对于漫反射 AOV）。换句话说，覆盖值应用于导出的预设。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-9EA4A186-E452-46D3-B670-8B59845A783F.png) <!-- baize:img-hook downloaded=false reason="正文 1715 字 ≥300，非承重" -->

**注**

导出时仅考虑已启用的覆盖。

在此示例中，场景层中的“图像大小 > 宽度”(Image Size > Width)属性设置为 960。属性上有三个覆盖。每个覆盖将值乘以 0.5。

仅启用了其中两个覆盖；因此，导出的值是 960 x 0.5 x 0.5 = 240。导出时不考虑已禁用的覆盖。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4AD8C8C8-B0A5-4B9D-9316-B29027B15750.png) <!-- baize:img-hook downloaded=false reason="正文 1715 字 ≥300，非承重" -->

## 相关主题

- [将“渲染设置”(Render Settings)作为预设导出和导入](将“渲染设置”%28Render%20Settings%29作为预设导出和导入.md)

- [导出场景“渲染设置”(Render Settings)和 AOV 并将其应用于新场景](导出场景“渲染设置”%28Render%20Settings%29和%20AOV%20并将其应用于新场景.md)
