# 为 HumanIK 准备现有骨架

在使用[“定义”(Definition)选项卡](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-630B5349-213C-414D-B6C9-D283CE319472.htm)将角色骨架中的骨骼映射到 HumanIK 解算器理解的节点之前，必须将角色设置为基本的 T 形站姿，以便为 HumanIK 提供有关角色骨架和关节变换比例的重要信息。

角色的 T 形站姿必须尽可能与以下的描述和示例相匹配，以便反向运动学和重定目标解算器为角色生成精确的结果。如果未正确配置 T 形站姿，那么解算器会将全部操作基于错误数据之上，并很可能产生出歪斜、古怪或意想不到的姿势。

T 形站姿有以下要求：

- 角色必须面向 Z 轴的正方向。

- 手臂必须沿 X 轴扩散。因此，左臂应指向 X 轴的正方向。

- 角色的头顶必须向上，并位于 Y 轴的正方向上。

- 角色的手将展平，手掌朝向地面，拇指平行于 X 轴。

- 角色的脚需要垂直于腿（脚趾指向 Z 轴方向，如图所示）。脚不得绕 Y 轴旋转（即，左脚脚趾不应向内朝向右腿，也不应向外远离右腿）。

典型的 T 形站姿如下图所示：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-B8EDA668-E911-4215-8372-CCE2354A566C.png) <!-- baize:img-hook downloaded=false reason="正文 570 字 ≥300，非承重" -->

**注**

有关 HumanIK 所需特定骨骼结构的其他信息，请参见

HumanIK 角色结构

。

## 四足动物

HumanIK 可用于控制四足动物以及两足动物。如果为四足动物的角色创建特征，则必须将角色骨架设置为上图所示的相同的 T 形站姿。尽管此两足动物 T 形站姿对于四足动物而言有些古怪，但您必须将角色设置为该两足动物位置，才能确保 HumanIK 可以正确地设置角色骨架的比例。

## 相关主题

- [“定义”(Definition)选项卡](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-630B5349-213C-414D-B6C9-D283CE319472.htm)

- [绑定姿势](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-36808BCC-ACF9-4A9E-B0D8-B8F509FEC0D5.htm)
