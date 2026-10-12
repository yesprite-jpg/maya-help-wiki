# 创建和编辑弹簧 IK 控制柄

创建弹簧 IK 控制柄

1. 激活弹簧 IK 解算器。请参见上面的步骤。

2. 在“装备”(Rigging)菜单集（按 F3 键）中，选择“骨架 > [创建 IK 控制柄](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-5A485049-D0BD-4BBB-BE08-C3D502F17483.htm#GUID-5A485049-D0BD-4BBB-BE08-C3D502F17483__GUID-2FF18188-563E-49CB-B184-B9B74ACEE5F0)”(Skeleton > Create IK Handle)。

  这时，鼠标指针会变为工具的十字光标。

3. 打开“工具设置”(Tool Settings)面板。

  此时将显示“IK 控制柄设置”(IK Handle Settings)。请参见“骨架 > [创建 IK 控制柄](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-5A485049-D0BD-4BBB-BE08-C3D502F17483.htm#GUID-5A485049-D0BD-4BBB-BE08-C3D502F17483__GUID-2FF18188-563E-49CB-B184-B9B74ACEE5F0)”(Skeleton > Create IK Handle)。

4. 从“当前解算器”(Current Solver)下拉列表中选择“ikSpringSolver”，并根据需要设定其他“IK 控制柄设置”(IK Handle Settings)。

5. 单击关节链中要作为弹簧 IK 控制柄的起始关节的关节。

6. 单击关节链中要作为弹簧 IK 控制柄的末关节的关节。

  在选择的关节处开始和结束的弹簧 IK 控制柄将显示在关节链上。

重置弹簧 IK 控制柄的关节静止姿势

1. 重新定位弹簧 IK 关节链，以使其处于作为控制柄的期望新静止姿势。

  如果已为弹簧 IK 控制柄设定关键帧，则首先需禁用该控制柄，然后才能重新定位其弹簧 IK 关节链的关节。请参见[禁用或启用 IK 控制柄](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-6AA69392-0656-48CC-B68E-A24436E3ABFF.htm)。

2. 选择要为其设定新静止姿势的弹簧 IK 控制柄。

3. 在“属性编辑器”(Attribute Editor)中，选择 ikHandle 选项卡。

4. 在“IK 解算器属性”(IK Solver Attributes)部分中，通过单击“IK 弹簧解算器属性”(IK Spring Solver Attributes)子部分的名称旁边的箭头来将其展开。

5. 单击位于“静止姿势”(Rest Pose)属性旁边的“设置为当前姿势”(Set to Current Pose)按钮。

  目前，弹簧 IK 控制柄的关节链的当前姿势为其新的静止姿势。

## 相关主题

- [IK 控制柄概述](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-8AFE1FEB-C69C-4841-9787-3C196FDA9A1F.htm)

- [弹簧 IK 解算器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-695C3AF4-5DA7-4126-B890-3F4CB4F65E96.htm)

- [IK 弹簧解算器属性(IK Spring Solver Attributes)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E71102E0-0BA4-4F9D-9402-E6830889D569.htm#WS17956D7ADBC6E7363438120E117AE30D38F-7FEF)
