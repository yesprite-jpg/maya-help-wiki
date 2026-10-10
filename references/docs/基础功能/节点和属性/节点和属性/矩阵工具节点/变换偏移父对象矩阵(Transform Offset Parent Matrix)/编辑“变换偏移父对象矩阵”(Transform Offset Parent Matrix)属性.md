# 编辑“变换偏移父对象矩阵”(Transform Offset Parent Matrix)属性

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-57E9DA6F-DB97-48FB-859F-5FA7A7471DF8.png) <!-- baize:img-hook downloaded=false reason="正文 1052 字 ≥300，非承重" -->

如果“变换偏移父对象矩阵”(Transform Offset Parent Matrix) **的“合成”(Composition)**或**“矩阵”(Matrix)**选项卡未锁定或连接（字段背景为黄色或灰色表示已连接或已锁定），则可以编辑每个字段中的值。

“合成”(Composition)和“矩阵”(Matrix)选项卡中的值是链接的，因为它们表示相同的变换，但采用两种不同的方式。如果更改“合成”(Composition)选项卡中的值，则会影响“矩阵”(Matrix)选项卡中的值，反之亦然。

“合成”(Composition)和“矩阵”(Matrix)选项卡中的值是链接的，因为它们表示相同的变换，但采用两种不同的方式。如果更改“合成”(Composition)选项卡中的值，则会影响“矩阵”(Matrix)选项卡中的值，反之亦然。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-17FB0C52-15D9-4F59-BA52-8AF3DF56469A.png) <!-- baize:img-hook downloaded=false reason="正文 1052 字 ≥300，非承重" -->

“合成”(Composition)选项卡状态：**A**. 已连接 **B**. 已锁定

在“属性编辑器”(Attribute Editor)中编辑“变换偏移父对象矩阵”(Transform Offset Parent Matrix)值

1. 在[属性编辑器(Attribute Editor)](../../查看和编辑属性/属性编辑器%28Attribute%20Editor%29.md)中选择节点选项卡，然后展开“变换偏移父对象矩阵”(Transform Offset Parent Matrix)下拉列表。

2. 双击每个字段以输入值。（如果字段为灰色，表示其已锁定。如果字段为黄色，表示其已连接，并且在连接断开之前无法编辑。）

3. 还可以在[变换偏移父对象矩阵(Transform Offset Parent Matrix)](../变换偏移父对象矩阵%28Transform%20Offset%20Parent%20Matrix%29.md)字段上单击鼠标右键以访问以下选项：

  | 选项 | 行为 |
  |---|---|
  | **将矩阵设置为身份(Set Matrix to Identity)** | 将对象移动到定义的起始位置。 注： 单位矩阵是表示世界或场景中心的中性矩阵。它包含 16 个值：值 1 对应于对角线，但所有项（平移、旋转和缩放）均设置为 0，因此它可以分解为 0 值平移和旋转，1 值缩放和 0 值斜切。 |
  | **<*节点名称*>矩阵...(<nodename>matrix...)** | 打开节点[属性编辑器(Attribute Editor)](../../查看和编辑属性/属性编辑器%28Attribute%20Editor%29.md)选项卡。 |
  | **逆矩阵(Inverse Matrix)** | 由内到外翻转矩阵值。 注： 建议不要用于奇异矩阵，否则可能会产生不可预测的结果。 |
  | **锁定属性(Lock Attribute)** | 防止修改属性。字段变为灰色以反映此状态。 |
  | **断开连接(Break Connection)** | 仅可用于“已连接”属性。“已连接”表示属性由另一个属性控制。若要编辑“合成”(Composition)和“矩阵”(Matrix)选项卡，它们不能处于“已连接”（黄色）状态。 |
