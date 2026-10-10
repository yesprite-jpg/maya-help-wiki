# 结合使用表达式与“时间编辑器”(Time Editor)片段层

表达式是您向 Maya 提供的指令，用于控制随时间变化的属性。属性是对象的特性，例如，X 缩放、Y 平移和可见性，等等。

**注**

时间编辑器不支持动画层。相反，可以使用时间编辑器片段层改变现有片段上的动画。您无法同时使用动画层和片段层驱动动画，因为这会产生冲突。

将表达式添加到时间编辑器片段层

1. 将片段层添加到时间编辑器。有关在时间编辑器中创建片段层的信息，请参见[在片段层上设置关键帧](../../在时间编辑器中设置动画关键帧/在片段层上设置关键帧.md)。

2. 单击“层”(Layer)图标 ![图：单击“层”(Layer)图标 以展开片段层，查看与该层关联的属性。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-B057651A-0B8C-423E-A17F-86DD0BABA664.png) <!-- baize:img-hook downloaded=false reason="正文 361 字 ≥300，非承重" --> 以展开片段层，查看与该层关联的属性。

3. 在名单中，在要创建表达式的属性上单击鼠标右键，然后从[片段层属性上下文菜单](“片段层属性”%28Clip%20Layer%20attribute%29上下文菜单.md)中选择“添加表达式”(Add Expression)。将打开[表达式编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-251640EA-AACC-4F1B-A341-297F0F4CEFE4)，允许您指定表达式来控制关联属性。

当层属性由表达式驱动时，片段层属性所在的行将会更新，显示该属性由表达式驱动

另请参见[结合使用约束和表达式以及动画层](../../../../动画层/动画层/包含动画层的示例工作流/高级工作流：%20结合使用约束和表达式以及动画层.md)。
