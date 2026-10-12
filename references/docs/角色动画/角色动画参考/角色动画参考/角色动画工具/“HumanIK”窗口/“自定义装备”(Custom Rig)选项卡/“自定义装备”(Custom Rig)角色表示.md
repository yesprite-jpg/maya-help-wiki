# “自定义装备”(Custom Rig)角色表示

显示两足动物角色的图像以及可用于为自定义装备设置动画的效应器。该布局类似于“控制”(Controls)选项卡中的[角色表示](../“控制”%28Controls%29选项卡/控制角色表示.md)。

加载具有有效骨架定义和自定义装备的角色之后，即可开始映射效应器了。“自定义装备”(Custom Rig) **角色**表示包含自定义装备的主 IK 和 FK 效应器的单元。您可以映射任意数量的这些单元。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-E00CE1F5-A330-40E4-9438-170DBABE1695.png) <!-- baize:img-hook downloaded=false reason="正文 444 字 ≥300，非承重" -->

## 单元状态

角色表示的每个 IK 和 FK 单元都会更新，以反映相应效应器的状态。下表介绍了每个单元的各种状态。

#### 选择状态

| IK 单元 | 效应器状态 |
|---|---|
| ![图：IK 单元 效应器状态 选定对象。 未选中。 已指定。 已指定并选中。 注： 小的圆形单元表示膝部和肘部的上方向向量效应…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-968C8A58-285A-47F4-A453-069970C53CD2.png) <!-- baize:img-hook downloaded=false reason="正文 444 字 ≥300，非承重" --> | 选定对象。 |
| ![图：IK 单元 效应器状态 选定对象。 未选中。 已指定。 已指定并选中。 注： 小的圆形单元表示膝部和肘部的上方向向量效应…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-45ACE233-F662-4574-98F1-3EF24BC4423F.png) <!-- baize:img-hook downloaded=false reason="正文 444 字 ≥300，非承重" --> | 未选中。 |
| ![图：IK 单元 效应器状态 选定对象。 未选中。 已指定。 已指定并选中。 注： 小的圆形单元表示膝部和肘部的上方向向量效应…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-9118B694-7B09-4779-A3A1-CCB5DE4EDCD4.png) <!-- baize:img-hook downloaded=false reason="正文 444 字 ≥300，非承重" --> | 已指定。 |
| ![图：IK 单元 效应器状态 选定对象。 未选中。 已指定。 已指定并选中。 注： 小的圆形单元表示膝部和肘部的上方向向量效应…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-ED42D073-B36F-4DFD-A8C9-9BE0D8947F75.png) <!-- baize:img-hook downloaded=false reason="正文 444 字 ≥300，非承重" --> | 已指定并选中。 |

**注**

小的圆形单元表示膝部和肘部的上方向向量效应器。

| FK 单元 | 效应器状态 |
|---|---|
| ![图：IK 单元 效应器状态 选定对象。 未选中。 已指定。 已指定并选中。 注： 小的圆形单元表示膝部和肘部的上方向向量效应…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-5258D454-5A10-4B28-9E7A-EFFCBB19186B.png) <!-- baize:img-hook downloaded=false reason="正文 444 字 ≥300，非承重" --> | 选定对象。 |
| ![图：IK 单元 效应器状态 选定对象。 未选中。 已指定。 已指定并选中。 注： 小的圆形单元表示膝部和肘部的上方向向量效应…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-24F68E68-424A-45AE-9470-8A3DCD82DB91.png) <!-- baize:img-hook downloaded=false reason="正文 444 字 ≥300，非承重" --> | 未选中。 |
| ![图：IK 单元 效应器状态 选定对象。 未选中。 已指定。 已指定并选中。 注： 小的圆形单元表示膝部和肘部的上方向向量效应…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-03055B69-4204-4C1D-B28E-2B5548F79EEE.png) <!-- baize:img-hook downloaded=false reason="正文 444 字 ≥300，非承重" --> | 已指定。 |
| ![图：IK 单元 效应器状态 选定对象。 未选中。 已指定。 已指定并选中。 注： 小的圆形单元表示膝部和肘部的上方向向量效应…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-5E6D5197-B7D6-4BE7-9B6B-ACF86C9CBE2B.png) <!-- baize:img-hook downloaded=false reason="正文 444 字 ≥300，非承重" --> | 已指定并选中。 |

## 身体部位视图

通过脊椎和颈部旁边的箭头图标 ![图：通过脊椎和颈部旁边的箭头图标 ，您可以切换到缩放视图，在该视图中，可以在角色的脊椎和颈部内定义各个效应器。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-5F3CFCD8-AB75-4028-9FEB-27DF5D127EC5.png) <!-- baize:img-hook downloaded=false reason="正文 444 字 ≥300，非承重" -->，您可以切换到缩放视图，在该视图中，可以在角色的脊椎和颈部内定义各个效应器。

默认情况下，脊椎和颈部视图会显示所有 10 个 FK 单元。为角色创建新的自定义装备映射后，该视图将更新以仅显示在骨架定义过程中初始映射的 FK 单元。

| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-06F11A5F-7E08-49B2-BBBD-7EF17F4FE8C3.png) <!-- baize:img-hook downloaded=false reason="正文 444 字 ≥300，非承重" --> |  | ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-3D3FF1AA-71AE-4365-84DF-D3D37F87B39A.png) <!-- baize:img-hook downloaded=false reason="正文 444 字 ≥300，非承重" --> |
|---|---|---|

## 相关主题

- [“自定义装备”(Custom Rig)选项卡概述](../“自定义装备”%28Custom%20Rig%29选项卡.md)
