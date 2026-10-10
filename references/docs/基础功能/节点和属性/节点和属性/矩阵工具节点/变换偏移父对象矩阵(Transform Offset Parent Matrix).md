# 变换偏移父对象矩阵(Transform Offset Parent Matrix)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 1346 字 ≥300，非承重" -->

访问“变换偏移父对象矩阵”(Transform Offset Parent Matrix)

- 在[属性编辑器(Attribute Editor)](../查看和编辑属性/属性编辑器%28Attribute%20Editor%29.md)中选择节点选项卡，找到“变换属性”(Transform Attributes)，然后展开“变换偏移父对象矩阵”(Transform Offset Parent Matrix)下拉菜单。

[属性编辑器(Attribute Editor)](../查看和编辑属性/属性编辑器%28Attribute%20Editor%29.md)中的“变换偏移父对象矩阵”(Transform Offset Parent Matrix)构件可用于将矩阵放入节点，以便您可以编辑值。您还可以在单独的选项卡中查看和编辑其合成。 它是绑定动画中适应性较强的新范例，可为您提供更清晰的绑定和更高的性能。

矩阵是 4 x 4 的浮点数组，表示变换节点的平移、旋转、缩放和斜切。它将自身插入到其父对象和本地计算之间，以便在移动父对象时，子对象也会移动。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-CB82703E-FC21-46A8-B5B5-E5DA899A5DCA.png) <!-- baize:img-hook downloaded=false reason="正文 1346 字 ≥300，非承重" -->

“属性编辑器”(Attribute Editor)中的“变换父对象矩阵”(Transform Parent Matrix)选项卡 **A**. 合成(Composition) **B**. 矩阵(Matrix)

“合成”(Composition)和“矩阵”(Matrix)选项卡中的值是链接的，因为它们表示相同的变换，但采用两种不同的方式。如果更改“合成”(Composition)选项卡中的值，则会影响“矩阵”(Matrix)选项卡中的值，反之亦然。

**注**

单位矩阵是表示世界或场景中心的中性矩阵。它包含 16 个值：值 1 对应于对角线，但所有项（平移、旋转和缩放）均设置为 0，因此它可以分解为 0 值平移和旋转，1 值缩放和 0 值斜切。

#### “合成”(Composition)选项卡

修改“缩放”(Scale)、“平移”(Translate)、“旋转”(Rotate)、“斜切”(Shear)组件。

在构件中的任何可编辑字段上单击鼠标右键，将矩阵设置为“身份”(Identity)、“反转”(Invert)或“锁定”(Locked)。有关状态颜色，请参考下面的**“变换偏移父对象矩阵”(Transform Offset Parent Matrix)状态**。

#### “矩阵”(Matrix)选项卡

在构件中的任何可编辑字段上单击鼠标右键，将矩阵设置为“身份”(Identity)、“反转”(Invert)或“锁定”(Locked)。有关状态颜色，请参考下面的**“变换偏移父对象矩阵”(Transform Offset Parent Matrix)状态**。

有关将矩阵运算链接在一起的信息，请参见[矩阵运算节点](矩阵运算节点.md)。

## “变换偏移父对象矩阵”(Transform Offset Parent Matrix)状态

“变换偏移父对象矩阵”(Transform Offset Parent Matrix)值字段显示彩色字段，以直观地反馈属性状态：

| 背景色 | 含义 |
|---|---|
| 黄色 | 属性已连接，这意味着属性由另一个属性控制。 若要编辑“合成”(Composition)和“矩阵”(Matrix)选项卡，它们不能处于“已连接”（黄色）状态。 |
| 灰色 | 属性已锁定 |
| 黑色 | 属性未连接 |
| 注： 已连接或已锁定的字段无法编辑。若要解除锁定属性或断开属性连接，请在相应字段上单击鼠标右键，然后选择**“解除锁定”(Unlock)。**有关上下文菜单的说明，请参见[编辑“变换偏移父对象矩阵”(Transform Offset Parent Matrix)](变换偏移父对象矩阵%28Transform%20Offset%20Parent%20Matrix%29/编辑“变换偏移父对象矩阵”%28Transform%20Offset%20Parent%20Matrix%29属性.md)。 |  |
