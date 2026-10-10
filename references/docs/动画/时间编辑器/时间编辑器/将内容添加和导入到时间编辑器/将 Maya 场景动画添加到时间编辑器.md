# 将 Maya 场景动画添加到时间编辑器

您可以导入已在 Maya 场景中打开的动画，以便在时间编辑器中进行编辑。还可以通过其他方法将尚未加载的文件导入时间编辑器中。若要将文件导入时间编辑器中，请参见[将动画导入时间编辑器](将动画导入时间编辑器.md)。

**注**

在将动画文件添加到时间编辑器轨迹时，必须首先存在要将场景中的已有动画添加到的对象。

## 将 Maya 场景动画添加到时间编辑器

时间编辑器支持由受动画曲线驱动的已设置关键帧属性组成的动画。还可以为由非曲线设置动画的属性（例如，约束、表达式等）设置动画。在这些属性的时间编辑器[将动画添加到时间编辑器(Add Animation to the Time Editor options)选项](将%20Maya%20场景动画添加到时间编辑器/将动画添加到时间编辑器%28Add%20Animation%20to%20the%20Time%20Editor%29选项.md)窗口的“要添加的属性”(Attributes to be Added)区域中，使用“受约束”(Constrained)选项。

**注**

当场景中已存在现有装备且未禁用时间编辑器时，如果导入受约束属性的动画，则时间编辑器将覆盖这些属性。使用

“动画”(Animation)首选项（在“设置”(Settings)下）

的“时间编辑器”(Time Editor)区域中的

“允许创建片段来覆盖现有约束”(Allow clip creation to override existing constraints)

选项，可以在导入片段时防止时间编辑器禁用受约束属性。

1. 在视口或[大纲视图](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4B9A9A3A-83C5-445A-95D5-64104BC47406)中选择要编辑的可设置动画属性（骨架、控制器等）。

  **注**

  重要：

  确保已选中对象的动画且其关键帧显示在时间滑块中。如果是角色动画，请确保已启用

  将动画添加到时间编辑器(Add Animation to the Time Editor)选项

  中的

  “包括整个层次”(Include Entire Hierarchy)

  选项，以便导入应用于整个角色的动画。

2. 在“时间编辑器”(Time Editor)中，从[时间编辑器菜单栏](../时间编辑器界面概述/时间编辑器菜单栏.md)中选择“文件 > 从场景选择中添加动画”(File > Add animation from Scene Selection)> ![图：在“时间编辑器”(Time Editor)中，从时间编辑器菜单栏中选择“文件 从场景选择中添加动画”(File Add …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1087 字 ≥300，非承重" -->。将打开[将动画添加到时间编辑器(Add Animation to the Time Editor)选项](将%20Maya%20场景动画添加到时间编辑器/将动画添加到时间编辑器%28Add%20Animation%20to%20the%20Time%20Editor%29选项.md)窗口。

3. 在“将动画添加到时间编辑器”(Add animation to the Time Editor)选项中，选择要导入的可设置动画属性。有关这些选项的更多详细信息，请参见[将动画添加到时间编辑器(Add Animation to the Time Editor options)选项](将%20Maya%20场景动画添加到时间编辑器/将动画添加到时间编辑器%28Add%20Animation%20to%20the%20Time%20Editor%29选项.md)。

场景中的所有[时间编辑器动画源](../使用时间编辑器片段/时间编辑器动画源.md)都将出现在[大纲视图](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4B9A9A3A-83C5-445A-95D5-64104BC47406)中以显示任何动画源，并且可随时重新应用。请参见[通过动画源创建片段](将%20Maya%20场景动画添加到时间编辑器/通过动画源创建片段.md)。

**注**

当任何属性由时间编辑器使用时，将在

“通道盒”(Channel Box)

和

“属性编辑器”(Attribute Editor)

中以浅橙色亮显。
