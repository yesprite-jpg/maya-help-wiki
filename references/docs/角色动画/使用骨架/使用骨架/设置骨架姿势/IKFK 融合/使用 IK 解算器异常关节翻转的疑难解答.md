# 使用 IK 解算器异常关节翻转的疑难解答

FK 动画完成后，关节链可能会在启用 IK 解算器（“关键帧 > IK/FK 关键帧 > 启用 IK 解算器”(Key > IK/FK Keys > Enable IK Solver)）时翻转到异常位置。

关节翻转是样条线 IK 解算器计算的正常结果。当关节方向从其旋转值 0 超过 90 度时，便会发生这种情况。如果关节的“旋转 X”(Rotate X)值、“旋转 Y”(Rotate Y)值和“旋转 Z”(Rotate Z)值相对于其父关节的旋转值为 0，则其旋转值为 0。当关节旋转接近 180 度时，翻转最为显著。

**注**

如果关节链翻转，请使用旋转平面解算器，而不是单链解算器。旋转平面解算器引入极向量来控制 IK 链的翻转，有时会结合单链解算器使用。建议不要将单链解算器用于双骨骼链。

若要撤消关节翻转和防止在您启用“启用 IK 解算器”(Enable IK Solver)时发生翻转，请执行下列操作：

1. 在“动画”(Animation)菜单集中，禁用“关键帧 > IK/FK 关键帧 > 启用 IK 解算器”(Key > IK/FK Keys > Enable IK Solver)。

  这会将关节链返回到发生翻转之前的位置。

2. 选择 IK 控制柄，然后从“装备”(Rigging)菜单集中选择“骨架 > [设置首选角度](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-5A485049-D0BD-4BBB-BE08-C3D502F17483.htm#GUID-5A485049-D0BD-4BBB-BE08-C3D502F17483__GUID-1CB03947-7681-4035-90F2-3DA4B58740CF)”(Skeleton > Set Preferred Angle)。

3. 重新启用“关键帧 > IK/FK 关键帧 > 启用 IK 解算器”(Key > IK/FK Keys > Enable IK Solver)。

4. 选择“关键帧 > IK/FK 关键帧 > 设置 IK/FK 关键帧”(Key > IK/FK Keys > Set IK/FK Key)。

  根据需要继续使用 IK。

## 请参见

- [使用样条线 IK 控制柄的提示](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-11CFDE9C-2B2F-4EA8-9707-473FE0F289B6.htm)

- [防止在样条线 IK 链中翻转](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-D107AA78-C999-451D-BCAC-CFFF1F007F17.htm)
