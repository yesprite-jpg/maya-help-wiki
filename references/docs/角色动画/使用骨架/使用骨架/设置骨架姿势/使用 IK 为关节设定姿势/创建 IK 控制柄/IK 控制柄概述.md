# IK 控制柄概述

在 IK 链中，IK 控制柄开始处的关节称为起始关节，IK 控制柄末端的关节称为末关节。起始关节和末关节之间的所有关节都受 IK 控制柄及其解算器驱动。在场景视图中，会将 IK 控制柄绘制为包含 IK 链的起始关节和末关节的一条线。

IK 控制柄的末端（默认情况下它位于 IK 链的最后一个关节处）称为末端效应器。移动 IK 控制柄时，IK 解算器会在其计算中使用末端效应器的位置和方向，以相应地旋转 IK 链中的关节。末端效应器会始终尝试跟随 IK 控制柄的位置。但是，根据 IK 链的旋转限制和完全延伸长度，末端效应器可能无法接触到 IK 控制柄。

若要将 IK 控制柄移动到末端效应器的位置，请使用“动画”(Animation)菜单集，然后选择“关键帧 > IK/FK 关键帧 > 将 IK 移动到 FK”(Key > IN/FK Keys > Move IK to FK)。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-EF2CF139-88A3-4E6B-8719-2C06DF1FCAEA.png) <!-- baize:img-hook downloaded=false reason="正文 722 字 ≥300，非承重" -->

**注**

只能从

“Hypergraph”

查看 IK 控制柄的末端效应器。

若要创建 IK 控制柄，请使用“IK 控制柄工具”(IK Handle Tool)或“IK 样条线控制柄工具”(IK Spline Handle Tool)。请参见 [IK 控制柄工具](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-DF30CFD7-88EB-421F-9701-69318A1F3D16.htm)和 [IK 样条线控制柄工具](../使用样条线%20IK/IK%20样条线控制柄工具%28IK%20Spline%20Handle%20Tool%29.md)。

## 常规 IK 控制柄组件

若要显示所有当前 IK 控制柄的组件，请参见[查看所有 IK 控制柄组件](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E7374D31-30DA-4BA7-B651-32D76ECE3143.htm)。

### 控制柄线

控制柄线是一条贯穿关节链中所有关节和骨骼的线，而关节链由 IK 控制柄控制。控制柄线开始于起始关节的局部轴，结束于末关节的局部轴。

若要查看控制柄线的图像，请参见[旋转平面 IK 解算器](../使用旋转平面%20IK/旋转平面%20IK%20解算器.md)。

### 控制柄向量

控制柄向量是从 IK 链的起始关节绘制到 IK 控制柄的末关节（末端效应器）的线。这是旋转平面所使用的轴。

若要查看控制柄向量的图像，请参见[旋转平面 IK 解算器](../使用旋转平面%20IK/旋转平面%20IK%20解算器.md)。

## 相关主题

- [创建 IK 控制柄](../创建%20IK%20控制柄.md)

- [创建样条线 IK 控制柄](../使用样条线%20IK/创建样条线%20IK%20控制柄.md)

- [使用 IK 为关节设定姿势](../../使用%20IK%20为关节设定姿势.md)

- [IK 控制柄工具](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-DF30CFD7-88EB-421F-9701-69318A1F3D16.htm)
