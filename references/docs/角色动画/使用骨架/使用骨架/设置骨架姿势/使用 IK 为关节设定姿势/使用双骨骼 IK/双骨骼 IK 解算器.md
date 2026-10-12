# 双骨骼 IK 解算器

双骨骼解算器非常适用于对要保持在同一平面上的关节链设定姿势（例如手臂和腿）。例如，由旋转平面 IK 控制柄驱动的手臂的肩部、肘部和腕部关节都保持在与肘部旋转相同的平面内。该平面本身可以通过极向量从肩部关节进行旋转。

双骨骼 IK 解算器是旋转平面 IK 解算器的一个子集。因此，带有双骨骼 IK 解算器的 IK 控制柄使用与旋转平面 IK 控制柄相同的方式来解算其关节链的旋转。请参见[旋转平面 IK 解算器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-9942FFB5-65C2-46E2-B5A3-297667A9FB5D.htm)和[旋转平面 IK 控制柄组件](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-9942FFB5-65C2-46E2-B5A3-297667A9FB5D.htm)。

双骨骼 IK 控制柄非常适用于对包含三关节（双骨骼）的短关节链设定姿态和设置动画。如果尝试对拥有双骨骼 IK 控制柄的关节链设定姿势和设置动画，则双骨骼解算器将只解算起始关节和倒数第二个关节的旋转，并将忽略关节链中的所有其他关节。

双骨骼解算器是 Maya 中最快的 IK 解算器。这使得双骨骼 IK 控制柄非常适合于在游戏开发环境中设置角色。Maya 包含双骨骼 IK 解算器插件的源代码，使得游戏开发商能在游戏引擎中复制此功能的精确行为，或修改代码以创建自己的自定义 IK 解算器。

## IK 双骨骼解算器插件源代码

在开发人员工具包安装的 devkit\ik2Bsolver 文件夹中提供了双骨骼 IK 解算器的源代码。源代码提供了如何创建自己的 IK 解算器插件的示例。此外，通过提取核心算法，可以在游戏引擎中复制双骨骼 IK 解算器的精确行为。详细信息请阅读 ik2Bsolver 目录中的自述文件。

[Autodesk Developer Network](https://www.autodesk.com/developmaya) 中提供了开发人员工具包。
