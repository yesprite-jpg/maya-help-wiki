# 创建 FBX 预设

您可以设计自己的预设，在其中设置界面以包括符合需求的特定选项和设置。然后可以与其他人共享该预设。

要创建自定义预设，请执行以下操作：

1. 选择“文件”(File)，然后单击“导入”(Import)、“导出全部”(Export All)或“导出当前选择”(Export Selection)旁边的选项框。

  ![图：选择“文件”(File)，然后单击“导入”(Import)、“导出全部”(Export All)或“导出当前选择”(Ex…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-FF81884E-3D11-4DB9-B2D2-8451CE0B1DB1.png) <!-- baize:img-hook downloaded=false reason="正文 806 字 ≥300，非承重" -->

  将显示“选项”(Options)对话框。

2. 从“常规选项”(General Options)下的“文件类型”菜单中选择“FBX 导出”(FBX export)。

  ![图：从“常规选项”(General Options)下的“文件类型”菜单中选择“FBX 导出”(FBX export)。 “…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-C24FC35A-9708-4434-B06A-CCEE88B4CC4D.png) <!-- baize:img-hook downloaded=false reason="正文 806 字 ≥300，非承重" -->

  “文件类型”菜单

  “编辑预设”(Edit Preset)按钮显示在“文件类型特定选项”(File Type Specific Options)中。

3. 单击“编辑预设”(Edit Preset)可显示“导出/导入选项”(Export/Import Options)对话框。

  ![图：单击“编辑预设”(Edit Preset)可显示“导出/导入选项”(Export/Import Options)对话框。…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-4A89BC09-FCF4-4334-9F58-9F4355D047EB.png) <!-- baize:img-hook downloaded=false reason="正文 806 字 ≥300，非承重" -->

  “编辑预设”选项

  “编辑预设”(Edit Preset)对话框分为两部分，在左侧部分中添加了 FBX 选项的树视图。

4. 选择树视图中的元素，然后单击鼠标右键以访问“编辑”(Edit)选项。请参见[“编辑模式”(Edit Mode)选项](创建%20FBX%20预设/“编辑模式”%28Edit%20mode%29选项.md)。

  ![图：选择树视图中的元素，然后单击鼠标右键以访问“编辑”(Edit)选项。请参见“编辑模式”(Edit Mode)选项。 注：…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-82CE075B-ADB4-4EF9-9177-47BE0B2D7BEC.png) <!-- baize:img-hook downloaded=false reason="正文 806 字 ≥300，非承重" -->

  **注**

  某些编辑选项是所有结构层级共有的，而某些则特定于某个特殊的结构层级。您可以在任意选项结构层级中应用某些选项。

  请参见[“编辑模式”(Edit Mode)选项](创建%20FBX%20预设/“编辑模式”%28Edit%20mode%29选项.md)。

5. 单击“保存预设”(Save Preset)。

6. 在显示的“正在保存新预设”(Saving new preset)对话框中，键入新预设的名称。例如，“MyNewPreset”。

  ![图：在显示的“正在保存新预设”(Saving new preset)对话框中，键入新预设的名称。例如，“MyNewPrese…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-9BB32035-5A91-4536-87B2-F678F7BC8118.png) <!-- baize:img-hook downloaded=false reason="正文 806 字 ≥300，非承重" -->

  下次加载 Maya 时，新预设将显示在 Maya FBX 插件中。

  ![图：在显示的“正在保存新预设”(Saving new preset)对话框中，键入新预设的名称。例如，“MyNewPrese…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-1ADA864D-62C9-47C3-B925-2060B5B374A8.png) <!-- baize:img-hook downloaded=false reason="正文 806 字 ≥300，非承重" -->

  FBX 插件将自定义预设存储在某个文件中，以便您可以将其进行共享。默认情况下，您可以在您的 \maya\FBX\Presets 目录中找到自定义预设文件。

**注**

烘焙动画(Bake Animation)的“开始”(Start)/“结束”(End)/“步长”(Step)值无法保存在预设中。Maya FBX 插件始终从导出的场景中提取这些值。
