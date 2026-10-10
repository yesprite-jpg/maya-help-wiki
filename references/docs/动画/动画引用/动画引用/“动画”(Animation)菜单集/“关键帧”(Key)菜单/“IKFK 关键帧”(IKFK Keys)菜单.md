# “IK/FK 关键帧”(IK/FK Keys)菜单

- 在“动画”(Animation) [菜单集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D90A2BDB-FD05-4528-8A95-C33A02D15129) (**F4**) 中：“关键帧 > IK/FK 关键帧”(Key > IK/FK Keys)

## 设置 IK/FK 关键帧(Set IK/FK Key)

在所有当前 IK 控制柄的可设置关键帧属性和该控制柄 IK 链中的所有关节上设置关键帧。使用“设置 IK/FK 关键帧”(Set IK/FK Key)时，Maya 将执行附加操作，以确保在 IK 和 FK 之间平滑过渡。

若想在相同关节链上对 IK 和 FK 动画设置关键帧，您可以使用该菜单项，而不是[设置关键帧选项(Set Key Options)](设置关键帧选项%28Set%20Key%20Options%29.md)。用正向运动学和反向运动学为关节链设置动画时，我们建议使用“设置 IK/FK 关键帧”(Set IK/FK keys)。

此外，使用“设置 IK/FK 关键帧”(Set IK/FK Key)对属性设置关键帧时，结果动画曲线将显示为实线或虚线。动画由 IK 完全驱动时，动画曲线显示为实线；动画由 FK 完全驱动时，动画曲线显示为虚线。详细信息请参见手册的“动画”部分中“关键帧动画”一章中的[曲线图编辑器概述](../../../../关键帧动画/关键帧动画/关键帧动画和“曲线图编辑器”%28Graph%20Editor%29.md)。

## 启用 IK 解算器(Enable IK Solver)

该菜单项可启用或禁用当前 IK 控制柄的“解算器启用”(Solver Enable)属性。“解算器启用”(Solver Enable)属性的状态确定 IK 控制柄的解算器是处于活动状态还是非活动状态。

启用“解算器启用”(Solver Enable)时，只能使用 IK 控制柄设置关节链姿势。禁用“解算器启用”(Solver Enable)时，只能通过直接操纵各个关节 (FK) 来设置关节链的姿势。

当使用两种动画方法设置关节链姿势时，可以启用和禁用“启用 IK 解算器”(Enable IK Solver)来在反向运动学与正向运动学之间切换。请参见[设置骨架姿势](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-390788DB-527D-4EE5-A8DC-B99BE2D4861F)。

**注**

提示：

若要显示选定 IK 控制柄的“解算器启用”(Solver Enable)属性是已启用还是已禁用，请启用[“显示 > 平视显示仪”(Display > Heads Up Display)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0E9D9594-6664-4B69-B944-8B69E9551415) > “动画详细信息”(Animation Details)。

## 连接到 IK/FK(Connect to IK/FK)

通过将只读属性“IK 融合”(Ik Blend)添加到对象，该菜单项将选定对象链接到当前 IK 控制柄。请参见 [IK 融合](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E71102E0-0BA4-4F9D-9402-E6830889D569#WS73099CC142F48755-7B21313411809411AE9-5EE3)。

对象连接后，可选择该对象，然后使用[设置 IK/FK 关键帧(Set IK/FK Key)](“IKFK%20关键帧”%28IKFK%20Keys%29菜单.md#GUID-C5ACDDBC-9E30-443C-8419-F07FC41E9A86__SECTION_E3C2A7D6F8064F578E2024CA90F447F9)在 IK 控制柄和其关节链中的所有关节上设置关键帧。

如果要使用对象来操纵 IK 控制柄，也可以约束 IK 控制柄或使 IK 控制柄成为该对象的父对象。控制和驱动 IK 控制柄变换的对象称为“控制对象”。

**注**

如果选中对象时启用[显示 > 平视显示仪(Display > Heads Up Display)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0E9D9594-6664-4B69-B944-8B69E9551415) > 动画详细信息(Animation Details)，则 IK 控制柄的“IK 融合”(Ik Blend)值会显示在场景视图中。

## 将 IK 移动到 FK(Move IK to FK)

利用该菜单项可将当前的 IK 控制柄移动到其关节链中的最后一个关节。

在典型的 IK/FK 绑定中，IK 控制柄在 FK 操纵期间不随骨架移动，因此会出现不同步现象。这在存在多个 IK 控制柄时可能会导致出现混乱。当使用 IK 和 FK 设置动画时，可以使用“将 IK 移动到 FK”(Move IK to FK)使 IK 控制柄的位置与末端效应器的位置同步。

例如，在动画中从 FK 切换到 IK 之前，需要将 IK 控制柄移动到 FK 骨骼的位置，以便在将 FK 切换到 IK 时动画不会跳转。

**注**

如果 IK 控制柄在控制层级中已编组或受约束，请结合使用

连接到 IK/FK(Connect to IK/FK)

和

“将 IK 移动到 FK”(Move IK to FK)

来移动整个层级。
