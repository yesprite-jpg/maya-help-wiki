# “控制”(Controls)选项卡工具栏

- “控制”(Controls)选项卡工具栏位于 [HumanIK 窗口](../../“HumanIK”窗口.md) 的“定义”(Definition)选项卡上方

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-7A3535FE-8775-4418-BB27-DF5C21E7319C.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" -->

## 显示/隐藏

通过这些图标可以切换显示 FK 效应器、IK 效应器和骨架。

| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-E051B03F-1BC1-4AC1-B693-12184049EE11.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> | 显示/隐藏 IK (Show/Hide IK) | 显示或隐藏角色的 IK 效应器。 |
|---|---|---|
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-4B428D4F-5586-423A-8DE9-7FB56A319B97.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> | 显示/隐藏 FK (Show/Hide FK) | 显示或隐藏角色的 FK 效应器。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-0359D584-3422-4FF7-AE44-E1FE4BDF576F.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> | 显示/隐藏骨架(Show/Hide Skeleton) | 显示或隐藏角色的骨架。 |

## 操纵和设置关键帧模式

这些图标允许使您设定操纵和设置关键帧模式用于处理角色的控制装备。您可以在角色的整个身体(**“全身”(Full Body)**)、身体的一部分(**“身体部位”(Body Part)**)或仅在选定的效应器(** **“选择”(Selection)** **)上操纵和设置关键帧。

| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-C7B1033C-578C-427D-94AA-EC2CC9140196.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> | 全身(Full Body) | 将该工具设置为“全身”(Full Body)设置关键帧和操纵模式，可使您选择单个效应器来操纵整个角色。 例如，在“全身”(Full Body)模式中平移角色的腕部效应器将在全身移动以到达该效应器时影响它。 注： 在该模式下强制使用初始姿势（参见下文）将强制整个角色采用初始姿势，并且该角色将相对于其引用节点进行偏移。 |
|---|---|---|
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-F367DB0D-C070-46F0-8171-D6CC887C364C.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> | 身体部位(Body Part) | 将工具设定为“身体部位”(Body Part)模式，允许您基于选定的效应器，在单个身体部位上操纵和设定关键帧。 注： 在该模式下强制使用初始姿势（参见下文）将强制选定的身体部位采用初始姿势。如果髋部是选择的一部分，则角色将相对于其引用节点进行偏移。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-04EA7E2A-2F13-41AB-B11F-C602DBC678A0.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> | 选择(Selection) | 将工具设定为“选择”(Selection)模式，允许您仅操纵和设定选定效应器的关键帧。 在该模式下，您可以操纵一个效应器，而无需解决角色的其他部位，然后使用“HumanIK 控制”(HumanIK Controls)来调整角色的其他部位对于该效应器所能达到的程度。 |

“角色”(Character)表示以白色亮显单元，以显示角色的哪个部位可用于操纵和设置关键帧。例如，在“身体部位”(Body Part)操纵模式下，如果选择左腕效应器，“角色”(Character)表示中的所有左臂单元都将亮显为白色。有关单元反馈的详细信息，请参见[控制角色表示](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-19B154DE-58F2-46AF-B2EF-7D00B2E46476.htm)。

## 固定

这些图标允许您激活、禁用或暂时解除效应器上的固定。

固定可以更好地控制角色操纵，允许您在调整角色其他部位的位置时，约束特定效应器不移动或旋转。例如，可以固定腕部不旋转，但允许它在平移中移动，以便在调整腕部位置或手臂位置时，手腕可以移动但不会扭曲。

默认情况下，在创建 HumanIK 控制绑定时，该角色脚部的 IK 效应器会在平移和旋转中固定不动。

固定反馈会显示在“角色”(Character)表示中的每个单元上。

| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-0DE4B6D0-CE4A-41AD-8D4A-9E71ABF00D6A.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> | 固定平移(Pin Translation) | 固定和解除固定平移中的选定效应器。 固定后，选定的效应器将无法移动，同时，在“角色”(Character)表示中的相应单元上将显示一个固定图标。 提示： 使用 ![图：固定和解除固定平移中的选定效应器。 固定后，选定的效应器将无法移动，同时，在“角色”(Character)表示中的相应单…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-C48CB823-0167-41AE-B7CF-85871AC36213.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> + W 热键将“固定平移”(Pin Translation)切换为启用或禁用。 |
|---|---|---|
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-7E99335B-DC32-4E20-A645-C3A4DD237CCB.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> | 固定旋转(Pin Rotation) | 固定和解除固定旋转中的选定效应器。 固定后，选定的效应器将无法旋转，同时，在“角色”(Character)表示中的相应单元上将显示一个固定图标。 提示： 使用 ![图：固定和解除固定旋转中的选定效应器。 固定后，选定的效应器将无法旋转，同时，在“角色”(Character)表示中的相应单…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-C48CB823-0167-41AE-B7CF-85871AC36213.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> + E 热键将“固定旋转”(Pin Rotation)切换为启用或禁用。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-5F0321A0-7F9E-475A-86DA-6ABD80B0E483.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> | 释放所有固定(Release All Pinning) | 暂时释放选定的效应器和链下效应器的所有平移或旋转固定。 |

## 其他

| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-3EC18BE2-AA1C-45B2-9C3B-2F5C3CEA7609.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> | 初始姿势(Stance Pose) | 重置控制装备为其默认 T 初始姿势。 在**“全身”(Full Body)**模式下选择此图标可强制整个角色采用初始姿势，并且角色的位置将相对于其引用节点进行偏移。在**“身体部位”(Body Part)**模式下，选定的身体部位将被强制为初始姿势。如果髋部是选择的一部分，则角色将相对于其引用节点进行偏移。请注意，此功能不适用于**“选择”(Selection)**模式。 提示： 您还可以通过选择 ![图：重置控制装备为其默认 T 初始姿势。 在“全身”(Full Body)模式下选择此图标可强制整个角色采用初始姿势，并且角…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-39B60BBD-A9DF-46CA-8078-B4277C4CD703.png) <!-- baize:img-hook downloaded=false reason="正文 1730 字 ≥300，非承重" --> >“编辑”>“控制”>“初始姿势”(Edit > Controls > Stance Pose)来强制采用初始姿势。 |
|---|---|---|

有关与控制装备关联的操作，请参见 HumanIK 中的[编辑控制装备(Edit Control Rig)](../HumanIK%20菜单按钮.md#GUID-847A8632-2621-487E-A8E1-8A0E6340973A__GUID-465F8BFB-AC6D-40E4-AF9F-F5BF13D3338C)菜单。

## 相关主题

- [控制装备、效应器和枢轴](../../../../../HumanIK/HumanIK/控制装备、效应器和枢轴.md)
