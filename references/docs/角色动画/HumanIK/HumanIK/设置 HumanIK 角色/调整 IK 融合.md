# 调整 IK 融合

通过[“控制”(Controls)选项卡](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-5522E13D-C958-41E7-BD84-FC160B25DE22.htm)中的“HumanIK 控制”(HumanIK Controls)滑块，您可以调整每个解决方案（IK 或 FK）对特定身体部位的影响量。这使您能够完全控制骨架在同步的关键帧之间遵循的是哪一个解决方案。

调整 IK 融合时使用以下准则：

- 如果达到 100%，骨架将遵循 IK 解决方案。

- 如果为 50%，骨架一半遵循“IK”解决方案，一半遵循“FK”解决方案。

- 如果为 0%，骨架将遵循 FK 解决方案。

调整每个解决方案对骨架的影响的步骤

1. 在[“角色”(Character)表示](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-19B154DE-58F2-46AF-B2EF-7D00B2E46476.htm)中选择一个效应器。

2. 使用“IK 融合平移”(IK Blend T)和“IK 融合旋转”(IK Blend R)滑块调整“IK”解决方案与“FK”解决方案之间的平移和旋转百分比。

  角色表示的单元将更新，为您提供关于 IK 融合设置的可视反馈。（请参见 [IK 单元状态](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-19B154DE-58F2-46AF-B2EF-7D00B2E46476.htm#GUID-19B154DE-58F2-46AF-B2EF-7D00B2E46476__GUID-5DF6FB31-504D-442B-B34F-17A58429CFE4)。）

例如，为下图中的“IK 融合平移”(IK Blend T)指定了值 30%。当平移角色的腕部效应器时，骨架将贴近 FK 装备，因为与 IK 解决方案相比，它更加紧密地遵循 FK 解决方案。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-4A201B44-92B7-4DA8-B67E-A1E617EFAA6A.png) <!-- baize:img-hook downloaded=false reason="正文 456 字 ≥300，非承重" -->

## 相关主题

- [HumanIK 控制](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-D5AB39F5-4677-4C5A-8A4B-BFD31BA00D6C.htm)
