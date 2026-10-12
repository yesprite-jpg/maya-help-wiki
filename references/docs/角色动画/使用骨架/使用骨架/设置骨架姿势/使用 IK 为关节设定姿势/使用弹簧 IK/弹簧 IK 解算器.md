# 弹簧 IK 解算器

弹簧 IK 解算器 (ikSpringSolver) 对所有关节均产生比例旋转。这在对拥有许多关节的肢体（如昆虫的腿）设定姿势和设置动画时非常有用。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-BC89DA0E-09B9-43A2-8F80-F97C7F2DE2DF.gif) <!-- baize:img-hook downloaded=false reason="正文 339 字 ≥300，非承重" -->

弹簧 IK 解算器通过对关节之间的角度应用偏差值，来保持这些角度与关节链成比例。这样可以确保所有关节之间的角度始终均匀分布。弹簧 IK 解算器类似于旋转平面 IK 解算器，因为它们的 IK 控制柄都拥有极向量。由于弹簧 IK 控制柄拥有极向量，因此如果弹簧 IK 关节链穿过其极向量将会发生翻转。

使用弹簧 IK 解算器的 IK 控制柄需要静止姿势。默认情况下，在创建弹簧 IK 控制柄时目标关节链的位置和方向都为静止姿势。静止姿势的弹簧 IK 关节链的第一和最后关节之间的距离，确定了关节链是弯曲还是延伸，并且影响了每个独立关节的移动。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-030FFD42-05CF-47D4-B735-81BA0BAF6ED7.png) <!-- baize:img-hook downloaded=false reason="正文 339 字 ≥300，非承重" -->

## 相关主题

- [创建弹簧 IK 解算器](创建弹簧%20IK%20解算器.md)

- [ikHandle](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E71102E0-0BA4-4F9D-9402-E6830889D569.htm)
