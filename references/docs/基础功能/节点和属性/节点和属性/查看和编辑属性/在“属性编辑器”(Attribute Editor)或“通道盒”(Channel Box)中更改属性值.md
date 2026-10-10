# 在“属性编辑器”(Attribute Editor)或“通道盒”(Channel Box)中更改属性值

“通道盒”(Channel Box)或“属性编辑器”(Attribute Editor)中背景为紫色的属性值受与其他属性之间的连接所控制。无法手动编辑这些属性值。

| 目标 | 操作 |
|---|---|
| 为属性输入一个值 | 在文本框中单击，然后键入新值并按 Enter 键。 对于布尔 (on/off) 值，键入 1 或 on，或者键入 0 或 off。 请注意，在“通道盒”(Channel Box)中不能设置旋转和平移的限制。必须改为使用“属性编辑器”(Attribute Editor)进行设置。若要立即为许多对象设置限制，请使用“属性总表”(Attribute Spread Sheet)（“窗口 > 常规编辑器 > 属性总表”(Windows > General Editors > Attribute Spread Sheet)）中的“全部”(All)选项卡。 |
| 更改值并将键盘焦点返回到视图窗口，以便使用热键。 | 键入值并按 Enter 键或 Return 键。 |
| 更改值并将键盘焦点保留在编辑框中。 | 键入值并按数字键盘上的 Enter 键。 注： 按数字键盘上的 Enter 键后，值将亮显，使得更容易输入新值和查看结果。 |
| 同时为多个属性输入相同的值。 | 按住 Shift 键并单击、按住 Ctrl 键并单击或拖过多个文本框即可选择文本框。然后键入新值并按 Enter 键。 |
| 更改“通道盒”(Channel Box)中滑块的敏感度。 | 单击滑块速度图标可以在慢/中/快滑块之间切换。 单击双曲线图标可以切换到双曲线缩放。这样就能够极为快速地更改值。将其运用到需要大幅进行调整的值上。 |
| 使用鼠标调整数值属性的值。 | 单击属性，然后使用鼠标中键向左或向右拖动。 使用“通道盒”(Channel Box)工具栏中的图标来控制鼠标移动距离与数值更改之间的映射。 ![图：使用“通道盒”(Channel Box)工具栏中的图标来控制鼠标移动距离与数值更改之间的映射。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-B4354490-0895-425E-A124-5B9FFAABA56F.png) <!-- baize:img-hook downloaded=false reason="正文 1270 字 ≥300，非承重" --> 注： 这些设置也会影响视图中编辑器内不可见滑块的速度。 |
| 输入相对于当前值的一个值。 | 键入 +=n，当前值加 n。 类型 -=n，当前值减 n。 键入 *=n，当前值乘 n。 键入 /=n，当前值除 n。 后缀 % 表示基于百分比进行操作（例如，+=10% 表示为选定值增加当前值的 10%）。 |
| 将属性快速链接到其他值。（仅适用于“属性编辑器”(Attribute Editor)） | 在文本框中键入 =time 或 =frame，以便使用保留关键字 time 或 frame 并将属性值快速链接到当前时间或当前帧。也可以包括简单的运算符，例如：=frame/2、=time*3.5。 |
| 创建复杂表达式 | 在文本框上单击鼠标右键，然后选择“创建新表达式”(Create New Expression)（“属性编辑器”(Attribute Editor)）或“表达式”(Expressions)（“通道盒”(Channel Box)）。 |

**注**

提示：

当在“通道盒”(Channel Box)中键入值时：

- 按数字键盘上的 Enter 键可以输入值并保持焦点停留在“通道盒”(Channel Box)中。

- 按键盘上的 Enter 键可以输入值并让焦点返回到视图窗口（这样即可使用热键）。

## 相关主题

- [显示或隐藏“通道盒”(Channel Box)中属性的操纵器](通道盒%28Channel%20Box%29/显示或隐藏“通道盒”%28Channel%20Box%29中属性的操纵器.md)

- [多个单元中的行内数值计算](多个单元中的行内数值计算.md)

- [查看和编辑多个节点上的多个属性](查看和编辑多个节点上的多个属性.md)

- [保存和重用属性预设](保存和重用属性预设.md)

- [锁定属性值](锁定属性值.md)

- [创建动画表达式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EF3F2007-74E7-4F23-B4A3-8D2EF94579A1)
