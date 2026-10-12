# HumanIK 窗口中的烘焙选项

HumanIK 窗口 > ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-39B60BBD-A9DF-46CA-8078-B4277C4CD703.png) <!-- baize:img-hook downloaded=false reason="正文 600 字 ≥300，非承重" --> >“烘焙”(Bake)菜单中提供的选项根据选定角色（目标）、[源](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-AD727276-1FE1-4F84-9746-DF3CAB994F96.htm)以及[操纵和设置关键帧模式](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-735DF85A-331C-4049-8C70-E53EFCDB4B73.htm#GUID-735DF85A-331C-4049-8C70-E53EFCDB4B73__SECTION_448E393B3A904F939192EF2FA4C7EF0B)更新。

**注**

必须从

HumanIK 窗口

启动 HumanIK 烘焙。不推荐选择

“编辑 > 关键帧 > 烘焙模拟”(Edit > Keys > Bake Simulation)

来烘焙 HumanIK 角色。

**注**

提示：

选择每个烘焙选项旁的选项框

以在烘焙前编辑

“烘焙模拟选项”(Bake Simulation Options)

。

下面概述了不同目标角色类型的烘焙选项：

- 无源角色

  ![图：无源角色 烘焙骨架(Bake Skeleton)：在自身烘焙全身或身体部位骨架动画。 烘焙到控制装备(Bake To C…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-A5773C80-4323-4AC1-A375-1E48E27E4558.png) <!-- baize:img-hook downloaded=false reason="正文 600 字 ≥300，非承重" -->

  - 烘焙骨架(Bake Skeleton)：在自身烘焙**全身**或**身体部位**骨架动画。

  - 烘焙到控制装备(Bake To Control Rig)：将**全身**骨架动画烘焙到控制装备。

- 以控制装备为源的角色（“全身”(Full Body)模式）

  ![图：以控制装备为源的角色（“全身”(Full Body)模式） 烘焙到骨架(Bake To Skeleton)：将全身控制装…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-0DEA7A01-A399-446D-9367-1BA13083D22A.png) <!-- baize:img-hook downloaded=false reason="正文 600 字 ≥300，非承重" -->

  - 烘焙到骨架(Bake To Skeleton)：将**全身**控制装备动画烘焙到骨架。

    **注**

    烘焙到骨架后，会自动禁用角色的控制装备。

  - 烘焙控制装备(Bake Control Rig)：在控制装备自身烘焙**全身**控制装备动画。

- 以控制装备为源的角色（“身体部位”(Body Part)模式）

  ![图：以控制装备为源的角色（“身体部位”(Body Part)模式） 烘焙装备身体部位(Bake Rig Body Part)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-EF9E88CF-9213-47BF-87CD-6D5376154767.png) <!-- baize:img-hook downloaded=false reason="正文 600 字 ≥300，非承重" -->

  - 烘焙装备身体部位(Bake Rig Body Part)：在控制装备自身烘焙控制装备动画，但仅适用于选定的**身体部位**。

- 装备具有自定义装备映射的角色

  - “烘焙到自定义装备”(Bake To Custom Rig)：基于自定义装备映射，将重定目标动画从源角色烘焙到当前角色的装备。

## 相关主题

- [将重定目标的动画烘焙到目标角色](../../../../../HumanIK/HumanIK/设置%20HumanIK%20重定目标/将重定目标的动画烘焙到目标角色.md)
