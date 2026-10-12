# 创建和定义 HumanIK 骨架

例如，如果现有角色网格需要一个骨架，请执行以下步骤。（如果拥有的角色已有骨架，请参见[为 HumanIK 定义现有骨架](为%20HumanIK%20定义现有骨架.md)。）

**注**

注意：

创建骨架时，请确保角色开始时处于标准 T 形站姿，面向正 Z 轴，Y 轴向上，且手臂与 X 轴对齐。请参见[为 HumanIK 准备现有骨架](为%20HumanIK%20准备现有骨架.md)。

创建默认骨架

1. 打开 [HumanIK](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-9921EDE1-05E2-4062-9F0D-4BADECA29226.htm) （“骨架 > HumanIK”(Skeleton > HumanIK)），然后在[开始(Start)窗格](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-708BB8DD-C29F-4112-8704-730716E538C9.htm)的**“创建”(Create)**部分中单击“创建骨架”(Create Skeleton)。

  将创建具有有效骨架定义的默认骨架。

2. （可选）单击 ![图：（可选）单击 “重命名角色”(Rename Character)以重命名角色。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-39B60BBD-A9DF-46CA-8078-B4277C4CD703.png) <!-- baize:img-hook downloaded=false reason="正文 655 字 ≥300，非承重" --> >“重命名角色”(Rename Character)以重命名角色。

3. （可选）使用各种骨骼和关节设置来调整骨架，使其适合您的角色结构。请参见[骨架设置区域](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-3DF80458-E953-4EA8-AE8E-A73627419F1A.htm)。

  **注**

  提示：

  如果要将默认骨架绑定到现有网格，请加载网格并使用

  “角色比例”(Character Scale)

  滑块以交互方式调整默认骨架的比例，直到其大致匹配网格的大小。

4. （可选）如果默认骨架比例与角色并非完全相符，请根据需要平移并旋转骨骼，直到适合角色为止。

  例如，如果角色的肢体比默认生成的骨架更长或更短，请选择生成的骨架肢体并对其进行平移，直到适合角色为止。（请记住，无论角色的比例如何，都必须在 T-stance 中进行定义，面向正 Z 轴，Y 轴向上，且手臂与 X 轴对齐。）

5. （可选）完成定义骨架后，可以从“源”(Source)菜单中选择“控制装备”(Control Rig)来创建控制装备。该操作会自动锁定骨架定义。

## 相关主题

- [HumanIK](../../HumanIK.md)

- [设置 HumanIK 角色](../设置%20HumanIK%20角色.md)

- [重定目标工作流](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-1EE9D0F3-D603-4537-9CEE-554835016282.htm)

- [创建控制装备](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E87CFCB6-030D-4BC3-A18E-E7390C092A3F.htm)
