# 创建“游戏导出器”(Game Exporter)预设

如果您始终希望在导出文件时访问相同的 FBX 选项集，可以创建自定义的选项集以显示在“游戏导出器”(Game Exporter)中。

1. 切换到“动画片段”(Animation Clips)选项卡以创建用于导出动画的预设，或者切换到“模型”(Model)选项卡以创建用于导出网格的预设。

2. 在“游戏导出器”(Game Exporter)工具栏中，单击 ![图：在“游戏导出器”(Game Exporter)工具栏中，单击 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-A4D4B95A-0FFD-4B5E-ACFC-075E23801F9B.png) <!-- baize:img-hook downloaded=false reason="正文 654 字 ≥300，非承重" -->。

3. 在弹出的“创建预设”(Create Preset)窗口中，输入新建预设的名称。

  这是将显示在“游戏导出器”(Game Exporter)顶部的预设下拉列表中的名称。

4. 使用“模板”(Template)字段选择您在预设中从哪个基本选项集开始，然后单击“确定”(OK)。

  **注**

  默认情况下，您可以选择

  “模型默认值”(Model Default)

  或

  “动画默认值”(Anim Default)

  预设作为模板。若要添加自己的预设作为模板，请将这些预设保存在默认目录 (

  ..\maya\<*版本*>\presets\attrPresets\gameFbxExporter

  ) 下。

5. 以您希望的方式设置预设的所有导出选项，然后完成导出操作（单击“导出”(Export)），或关闭“游戏导出器”(Game Exporter)。

  您已经设置的导出选项保存在预设中，并且此预设与场景一起保存。下一次打开场景时，您的预设在“游戏导出器”(Game Exporter)中仍可用。

**注**

若要在另一个场景中使用相同的预设，请单击

，以将该预设保存到磁盘。然后，您可以在新建场景中单击

，以重新加载

“游戏导出器”(Game Exporter)

中的预设。
