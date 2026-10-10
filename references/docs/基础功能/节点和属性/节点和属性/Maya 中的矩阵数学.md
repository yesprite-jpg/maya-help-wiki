# Maya 中的矩阵数学

Maya 使用矩阵数学来计算 3D 空间中点的精确线性位置和方向，这是 Maya 如何处理变换的核心所在。之所以称为“矩阵数学”是因为计算是基于 3 x 3 表完成的，此表由变换（平移、旋转和缩放）坐标行与方向（X、Y 和 Z 轴）行值相乘组成。

在后台，Maya 使用矩阵的方式略有不同，即使用 4 x 4 表，而不是 3 x 3 表。第 4 列表示斜切值。（斜切值表示对象的倾斜。）

## 变换矩阵

变换矩阵用于创建从一个坐标系到另一个坐标系的映射。变换矩阵包含变换的所有组成部分，如旋转、平移、缩放等。可以使用变换矩阵修改几何体的任何方面。

“属性编辑器”(Attribute Editor)中的[“变换偏移父对象矩阵”(Transform Offset Parent Matrix)](矩阵工具节点/变换偏移父对象矩阵%28Transform%20Offset%20Parent%20Matrix%29.md)构件分为两个选项卡：**“合成”(Composition)**选项卡（包含标准 3 x 3 矩阵）和**“矩阵”(Matrix)**选项卡（显示特定于 Maya 的 4 x 4 表）。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-CB82703E-FC21-46A8-B5B5-E5DA899A5DCA.png) <!-- baize:img-hook downloaded=false reason="正文 556 字 ≥300，非承重" -->

“属性编辑器”(Attribute Editor)中的“变换父对象矩阵”(Transform Parent Matrix)选项卡：**A**. 合成(Composition) **B**. 矩阵(Matrix)

“矩阵”(Matrix)选项卡可视作窗口，用于查看和编辑驱动 3D 对象的复杂数学。“合成”(Composition)选项卡则以更容易识别的 T、R 和 S 值显示矩阵信息。
