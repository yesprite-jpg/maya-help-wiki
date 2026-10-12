# IK 解算器

IK 解算器是 IK 控制柄后面的数学算法。IK 解算器计算由 IK 控制柄控制的一个关节链中所有关节的旋转。IK 控制柄对关节链的效果，取决于 IK 控制柄所使用的 IK 解算器类型。默认情况下，Maya 加载以下 IK 解算器：

- [单链 IK 解算器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-44AFF765-D81B-4A30-81A2-97FC7F683889.htm) (ikSCsolver)

- [旋转平面 IK 解算器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-9942FFB5-65C2-46E2-B5A3-297667A9FB5D.htm) (ikRPsolver)

- [样条线 IK 解算器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-B4EF8784-92D1-4D83-9CA5-A692D06607B8.htm) (ikSplineSolver)

  只能将样条线 IK 解算器与样条线 IK 控制柄结合使用。请参见[使用样条线 IK 控制柄的提示](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-11CFDE9C-2B2F-4EA8-9707-473FE0F289B6.htm)和 [IK 样条线控制柄工具](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-820CF89C-257C-4EA9-A474-6E0146C9099F.htm)。

- Human IK 解算器 (hikSolver)

  只有已经被角色化的角色才能使用 Human IK 解算器。不能将常规 IK 控制柄用于 hikSolver。

除了默认解算器外，您还可以手动加载，然后创建以下解算器：

- [双骨骼 IK 解算器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-CEA46DDD-40C8-4F78-8928-DEBE1A94E430.htm) (ik2Bsolver)

- [多链 IK 解算器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-88793DB4-F48A-4BB8-AB87-20B7D1983D05.htm) (ikMCsolver)

- [弹簧 IK 解算器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-695C3AF4-5DA7-4126-B890-3F4CB4F65E96.htm) (ikSpringSolver)

如果要对拥有两和四关节之间的关节链设定姿势和设置动画，应使用单链或旋转平面 IK。

如果要对更长的关节链设定姿势和设置动画，应使用 IK 样条线。如果要为游戏所使用的简单三关节 IK 链设定姿势和设置动画，请使用双骨骼 IK。

默认情况下，所创建的每个 IK 控制柄都可以使用相同类型的 IK 解算器，并且还可以共享相同的 IK 解算器节点。例如，所有 IK 控制柄还可以使用单链 IK 连接到同一 ikSCsolver 节点。因此，如果编辑共享 IK 解算器节点的属性，则连接到节点的所有 IK 控制柄都会受到影响。如果要微调仅针对某个 IK 控制柄的 IK 解算器，同时不要影响到其他 IK 控制柄，可以使用 [createNode](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Commands/createNode.html) MEL 命令为 IK 控制柄创建其他 IK 解算器。

## 单链 IK 控制柄和旋转平面 IK 控制柄之间的区别

单链 IK 控制柄和旋转平面 IK 控制柄之间的区别在于，单链 IK 控制柄的末端效应器尝试到达其 IK 控制柄的位置和方向，而旋转旋转平面 IK 控制柄的末端效应器仅尝试到达其 IK 控制柄的位置。由于旋转平面 IK 控制柄的末端效应器仅尝试到达其控制柄的位置，因此产生的关节旋转更具有可预测性。对于旋转平面 IK 控制柄，其整个关节链的方向受扭曲圆盘操纵器控制。详细信息请参见主题[旋转平面 IK 解算器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-9942FFB5-65C2-46E2-B5A3-297667A9FB5D.htm)中的“扭曲圆盘”描述。

**注**

如果关节链翻转，请使用旋转平面解算器，而不是单链解算器。旋转平面解算器引入极向量来控制 IK 链的翻转，有时会结合单链解算器使用。建议不要将单链解算器用于双骨骼链。

## IK 解算器计算

移动 IK 控制柄时，解算器执行适当的计算以便在其 IK 链中相应移动和旋转所有关节。首先，解算器查找 IK 控制柄的位置（“平移 X”(Translate X)、“平移 Y”(Translate Y)和“平移 Z”(Translate Z)属性）和方向（“旋转 X”(Rotate X)、“旋转 Y”(Rotate Y)和“旋转 Z”(Rotate Z)属性）。其次，解算器计算如何将末端效应器的位置和方向尽可能地向靠近 IK 控制柄的位置和方向移动。若要执行该操作，解算器计算如何最好地在 IK 控制柄的关节链中旋转关节。最后，解算器旋转关节链中的所有关节，使末端效应器到达 IK 控制柄的位置和方向。

## 相关主题

- [创建单链 IK 控制柄](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0B39A18D-EB13-46F2-9F82-09042EE65D8B.htm)

- [创建旋转平面 IK 控制柄](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-3E27BA31-12AE-4D20-81C9-E0C0640DA111.htm)

- [创建多链解算器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-D9184F1C-0D23-444A-BDA0-654D81C647C9.htm)

- [使用样条线 IK 控制柄的提示](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-11CFDE9C-2B2F-4EA8-9707-473FE0F289B6.htm)

- [创建双骨骼 IK 控制柄](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-6B31E7A8-73A2-4ADD-BE90-9B2C3CF56D88.htm)
