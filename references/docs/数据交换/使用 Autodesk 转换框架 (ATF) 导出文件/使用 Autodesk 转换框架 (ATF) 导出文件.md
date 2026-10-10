# 使用 Autodesk 转换框架 (ATF) 导出文件

您可以使用 Autodesk 转换框架 (ATF) 文件转换系统导出 Maya 和第三方文件格式。

**注**

Maya 仅在 Windows 上支持 ATF。

1. 选择“文件 > 导出全部/导出选定对象”(File > Export All/Export Selected) > ![图：选择“文件 导出全部/导出选定对象”(File Export All/Export Selected) 。此时将显示 M…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 567 字 ≥300，非承重" -->。此时将显示 Maya“导出”(Export)选项。

2. 从“文件类型”(File Type)菜单中选择以下 ATF 文件类型之一：

  - IGES_ATF

  - JT_ATF

  - DXF_ATF

  - PARASOLID_ATF

  - SAT_ATF

  - STEP_ATF

  - STL_ATF

  - WIRE_ATF

  - INVENTOR_ATF

  - CATIAV5_ATF

  - DWG_ATF/DXF_ATF

  - NX_ATF

3. 选择任一可用的“导出”(Export)首选项：

  - 默认文件扩展名(Default file extensions)：

    启用此选项（默认设置）后，导出具有选定“文件类型”(File type)的扩展名的文件。

  - 保留引用(Preserve references)：

    如果启用“保留引用”(Preserve Reference)，则将保持导出文件中的引用。如果禁用此选项，则所有引用都将导出到文件中；也就是说，它们将不再是引用，而是场景中的对象。默认设置为禁用。

  - 导出卸载引用(Export unloaded references)：

    导出与当前场景关联的所有卸载引用文件。

4. 单击“导出”(Export)。
