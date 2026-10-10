# “曲线图编辑器”(Graph Editor)  “关键帧”(Keys)菜单

#### 插入关键帧工具(Insert Keys Tool)

选择此工具可在现有动画曲线上放置新关键帧（热键：**Alt** + **i**，或使用[曲线图编辑器工具栏](../“曲线图编辑器”%28Graph%20Editor%29界面概述/“曲线图编辑器”%28Graph%20Editor%29工具栏.md)上的 ![图：选择此工具可在现有动画曲线上放置新关键帧（热键：Alt + i，或使用曲线图编辑器工具栏上的 按钮）。请参见将关键帧添加…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-02DF1766-6F61-4938-89C2-F8E485910316.png) <!-- baize:img-hook downloaded=false reason="正文 1003 字 ≥300，非承重" --> 按钮）。请参见[将关键帧添加到曲线](../../../关键帧动画/关键帧动画/编辑曲线/将关键帧添加到曲线.md)。 单击“插入关键帧”(Insert Keys) > ![图：选择此工具可在现有动画曲线上放置新关键帧（热键：Alt + i，或使用曲线图编辑器工具栏上的 按钮）。请参见将关键帧添加…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1003 字 ≥300，非承重" -->以打开[“插入关键帧工具选项”(Insert Keys tool options)](“曲线图编辑器”%28Graph%20Editor%29%20“关键帧”%28Keys%29菜单/插入关键帧工具选项%28Insert%20Keys%20Tool%20options%29.md)，可在其中设置关键帧的插入行为。

#### 添加关键帧工具(Add Key Tool)

使用该工具可以将关键帧添加到位于图表视图中的任意位置的选定动画曲线。

按住鼠标中键并拖动以设置新关键帧的位置。释放鼠标按钮会放置该关键帧。新关键帧的切线类型将与相邻关键帧的类型相同。 单击“添加关键帧”(Add Keys) > ![图：按住鼠标中键并拖动以设置新关键帧的位置。释放鼠标按钮会放置该关键帧。新关键帧的切线类型将与相邻关键帧的类型相同。 单击“…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1003 字 ≥300，非承重" --> 以打开[添加关键帧工具选项(Add Keys tool options)](“曲线图编辑器”%28Graph%20Editor%29%20“关键帧”%28Keys%29菜单/插入关键帧工具选项%28Insert%20Keys%20Tool%20options%29.md)，可在其中设置关键帧的插入行为。

#### 转化为关键帧(Convert to Key)

将选定的受控关键点转化为关键帧。

#### 转化为受控关键点(Convert to Breakdown)

将选定关键帧转化为受控关键点。 有关受控关键点关键帧和默认关键帧之间差异的详细信息，请参见[受控关键点](../../../关键帧动画/关键帧动画/受控关键点.md)。

#### 添加中间帧(Add Inbetween)

在当前时间插入中间帧。

#### 移除中间帧(Remove Inbetween)

在当前时间的中间帧。

**注**

使用

“移除中间帧”(Remove Inbetween)

时，关键帧之间的空间将减小。这可能会导致关键帧冲突并且出现无法预计的行为。

#### 禁用关键帧(Mute Key)

禁用选定关键帧。禁用的关键帧并不会有助于其通道中的动画。 请参见[禁用关键帧](../../../关键帧动画/关键帧动画/编辑关键帧/禁用关键帧.md)。

关键帧禁用之后，将出现以下现象：

- 在“曲线图编辑器”(Graph Editor)大纲视图中，禁用关键帧通道的名称旁边将出现绿色符号 ![图：在“曲线图编辑器”(Graph Editor)大纲视图中，禁用关键帧通道的名称旁边将出现绿色符号 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F08D20D4-7F55-41B9-A7D0-07B9F718078A.png) <!-- baize:img-hook downloaded=false reason="正文 1003 字 ≥300，非承重" -->。

- 禁用的关键帧将变为黑色，以指示其锁定状态。

- *在“曲线图编辑器”(Graph Editor)中的禁用关键帧曲线下方，将出现带有关键帧的禁用曲线*。

  禁用曲线与禁用关键帧动画曲线具有相同的关键帧数，且其关键帧与禁用关键帧动画曲线中的关键帧位于相同的位置。

  ![图：在“曲线图编辑器”(Graph Editor)中的禁用关键帧曲线下方，将出现带有关键帧的禁用曲线。 禁用曲线与禁用关键帧…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-08207804-64A9-4560-94EE-6A8FA9EB18FE.gif) <!-- baize:img-hook downloaded=false reason="正文 1003 字 ≥300，非承重" -->

#### 取消禁用关键帧(Unmute Key)

取消禁用选定关键帧。未禁用的关键帧将有助于其通道中的动画。取消禁用关键帧时，将禁用其“禁用”曲线（在“曲线图编辑器”(Graph Editor)大纲视图中，禁用关键帧曲线的名称旁边将出现一个红色符号 ![图：取消禁用选定关键帧。未禁用的关键帧将有助于其通道中的动画。取消禁用关键帧时，将禁用其“禁用”曲线（在“曲线图编辑器”(G…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-52DA02F3-EF40-440B-B340-FD6BABA3B6D5.png) <!-- baize:img-hook downloaded=false reason="正文 1003 字 ≥300，非承重" -->），但不会将其移除。

若要移除“禁用”曲线，请参见[禁用通道](../../../关键帧动画/关键帧动画/编辑曲线/禁用通道.md)。

## 相关主题

- [曲线图编辑器(Graph Editor)](../../曲线图编辑器%28Graph%20Editor%29.md)

- [“曲线图编辑器”(Graph Editor)菜单](../“曲线图编辑器”%28Graph%20Editor%29菜单.md)
