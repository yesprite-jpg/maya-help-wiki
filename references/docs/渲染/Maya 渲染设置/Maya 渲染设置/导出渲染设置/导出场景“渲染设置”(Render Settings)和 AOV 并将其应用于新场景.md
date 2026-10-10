# 导出场景“渲染设置”(Render Settings)和 AOV 并将其应用于新场景

导出未应用任何覆盖的场景“渲染设置”(Render Settings)和 AOV，然后将此预设导入到新场景中。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 1439 字 ≥300，非承重" -->

处理场景以及在渲染层中创建“渲染设置”(Render Settings)和 AOV 覆盖时，可能希望导出未应用任何覆盖值的场景**“渲染设置”(Render Settings)**的 .json，然后将此预设导入到新场景中。同样，您可能希望导出未应用任何覆盖值的 AOV。

若要导出未应用任何覆盖值的场景“渲染设置”(Render Settings)，请执行以下操作之一：

- 从“渲染设置”(Render Setup)编辑器中选择“文件 > 导出场景渲染设置”(File > Export Scene Render Settings)。

  这始终会在没有任何覆盖值的情况下导出场景“渲染设置”(Render Settings)，而不管您是在场景层中还是在渲染层中。

- ![图：确保场景层设置为可见，然后在“渲染设置”(Render Settings)窗口中选择“预设 导出渲染设置”(Preset…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1439 字 ≥300，非承重" --> 确保场景层设置为可见，然后在“渲染设置”(Render Settings)窗口中选择“预设 > 导出渲染设置”(Presets > Export Render Settings)，或者在“渲染设定”(Render Setup)编辑器的“场景 > 渲染设置”(Scene > Render Settings)部分中单击 ![图：确保场景层设置为可见，然后在“渲染设置”(Render Settings)窗口中选择“预设 导出渲染设置”(Preset…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-15A05717-B953-472A-B6FC-39C64A718DC9.png) <!-- baize:img-hook downloaded=false reason="正文 1439 字 ≥300，非承重" -->。

  如果在可见渲染层中选择其中任一选项，并且在当前层中应用了“渲染设置”(Render Settings)覆盖，则将显示一个对话框，警告您导出中将包括覆盖值。单击“取消”(Cancel)，然后切换到场景层并再次导出。

  导出的文件将保存到用户预设位置，默认情况下为 <Documents>\maya\Presets。有关详细信息，请参见[全局预设和用户预设](将“渲染设置”%28Render%20Settings%29作为预设导出和导入.md#GUID-469A3F38-8E0B-4A28-8913-D8A7E3EF0733__SECTION_1B399EB0AAA34C16AA60AD650DC96FC7)。

  **注**

  提示：

  从

  “渲染设置”(Render Setup)

  编辑器中选择

  “首选项 > 渲染首选项”(Preferences > Rendering Preferences)

  ，可以更改预设的位置。

若要导出未应用任何覆盖值的场景 AOV，请执行以下操作之一：

- 从“渲染设置”(Render Setup)编辑器中选择“文件 > 导出场景 AOV”(File > Export Scene AOVs)。

  这始终会在没有任何覆盖值的情况下导出场景 AOV，而不管您当前是在场景层中还是在渲染层中。

- ![图：确保场景层设置为可见，然后在“渲染设置”(Render Settings)窗口中选择“预设 导出 AOV”(Preset…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1439 字 ≥300，非承重" --> 确保场景层设置为可见，然后在“渲染设置”(Render Settings)窗口中选择“预设 > 导出 AOV”(Presets > Export AOVs)，或者在“渲染设定”(Render Setup)编辑器的“场景 > AOV”(Scene > AOVs)部分中单击 ![图：确保场景层设置为可见，然后在“渲染设置”(Render Settings)窗口中选择“预设 导出 AOV”(Preset…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-15A05717-B953-472A-B6FC-39C64A718DC9.png) <!-- baize:img-hook downloaded=false reason="正文 1439 字 ≥300，非承重" -->。

  如果在可见渲染层中选择其中任一选项，并且在当前层中应用了 AOV 覆盖，则将显示一个对话框，警告您导出中将包括覆盖值。单击“取消”(Cancel)，然后切换到场景层并再次导出。

  导出的文件将保存到用户预设位置，默认情况下为 <Documents>\maya\Presets。有关详细信息，请参见[全局预设和用户预设](将“渲染设置”%28Render%20Settings%29作为预设导出和导入.md#GUID-469A3F38-8E0B-4A28-8913-D8A7E3EF0733__SECTION_1B399EB0AAA34C16AA60AD650DC96FC7)。

  **注**

  提示：

  从

  “渲染设置”(Render Setup)

  编辑器中选择

  “首选项 > 渲染首选项”(Preferences > Rendering Preferences)

  ，可以更改预设的位置。

在此示例中，选择“文件 > 导出场景 AOV”(File > Export Scene AOVs)将创建不包括覆盖值的 .json：直接 AOV 保持启用状态，且漫反射 AOV 的 Png 格式设置为 int8，就像在场景层中那样。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-5615E988-18E9-4F93-8F13-5A2DD37E5E20.png) <!-- baize:img-hook downloaded=false reason="正文 1439 字 ≥300，非承重" -->

## 相关主题

- [将“渲染设置”(Render Settings)作为预设导出和导入](将“渲染设置”%28Render%20Settings%29作为预设导出和导入.md)

- [从可见渲染层导出“渲染设置”(Render Settings)和 AOV 并将其应用于新场景](从可见渲染层导出“渲染设置”%28Render%20Settings%29和%20AOV%20并将其应用于新场景.md)
