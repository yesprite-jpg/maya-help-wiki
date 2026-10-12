# 融合 IK 和 FK 动画

本主题假定您使用的是“动画”(Animation)菜单集（按 F4 键）。

**注**

如果要旋转已设置 IK 动画的关节链中的各个关节或为这些关节设置关键帧，请启用

“ikHandle”

属性中的

“Ik Fk 控制”(Ik Fk Control)

。

创建从 FK 到 IK 的动画融合

1. 选择要使用 FK 为其设置动画的 IK 链的 IK 控制柄。

2. 在“IK 解算器属性”(IK Solver Attributes)中，将“IK 融合”(Ik Blend)滑块拖动到 0.000。

  现在，动画模式设定为纯 FK。

3. 选择“关键帧 > IK/FK 关键帧 > 设置 IK/FK 关键帧”(Key > IK/FK Keys > Set IK/FK Key)。

  将为 IK 链和 IK 控制柄中的所有关节设置关键帧。

  现在，您将为关节 (FK) 而不是控制柄 (IK) 设置关键帧。

4. 取消选择 IK 控制柄。

5. 选择 IK 链中的一个关节，沿“时间滑块”(Time Slider)拖动当前时间指示器并旋转该关节。

6. 设定关键帧。

7. 重复步骤 5 和步骤 6，直到完成动画的 FK 部分。

8. 设置最后一个 FK 关键帧后，取消选择当前关节，然后选择您的关节链的 IK 控制柄。

9. 确保“IK 融合”(Ik Blend)滑块仍位于 0.000 处，然后选择“关键帧 > IK/FK 关键帧 > 设置 IK/FK 关键帧”(Key > IK/FK Keys > Set IK/FK Key)。

10. 将当前时间指示器在时间滑块上向前拖动 1 帧。

11. 将“IK 融合”(Ik Blend)滑块拖动到 1.000，然后设置一个关键帧。

  由于最后一个纯 FK 关键帧和第一个纯 IK 关键帧之间没有动画周期，因此 FK 动画将立即切换到 IK（不进行融合）。

  现在，动画模式设定为纯 IK。

  **注**

  如果纯 FK 关键帧和纯 IK 关键帧之间存在动画周期，它将由“IK 解算器”(IK Solver)插值。插值动画随后显示为介于 0.000 和 1.000 之间的“IK 融合”(Ik Blend)值。

12. 沿“时间滑块”(Time Slider)拖动当前时间指示器，平移 IK 控制柄并根据需要设置关键帧。

在 FK 动画中插入 IK（无论 FK 是否由“设置 IK/FK 关键帧”(Set IK/FK Key)控制）

1. 转到要插入 IK 的时间范围的第一帧。

2. 选择 IK 控制柄并设置一个关键帧（“关键帧 > IK/FK 关键帧 > 设置 IK/FK 关键帧”(Key > IK/FK Keys > Set IK/FK Key)）。

3. 转到要插入 IK 的时间范围的结束帧，选择 IK 控制柄并设置一个关键帧（“关键帧 > IK/FK 关键帧 > 设置 IK/FK 关键帧”(Key > IK/FK Keys > Set IK/FK Key)）。

  这将创建一个融合区域，您在该区域的两个边界关键帧之间设置的任何关键帧都不会出现在设定的范围之外意外地更改动画的情况。

4. 启用 IK 解算器（“关键帧 > IK/FK 关键帧 > 启用 IK 解算器”(Key > IK/FK Keys > Enable IK Solver)）。

5. 操纵 IK 控制柄并根据需要对边界关键帧之间的帧使用“设置 IK/FK 关键帧”(Set IK/FK Key)。

在由“设置 IK/FK 关键帧”(Set IK/FK Key)控制的 IK 动画中插入 FK

1. 在要插入 FK 的时间范围的第一帧处，选择 IK 控制柄并设置一个关键帧（“关键帧 > IK/FK 关键帧 > 设置 IK/FK 关键帧”(Key > IK/FK Keys > Set IK/FK Key)）。

2. 在要插入 FK 的时间范围的最后一帧处，选择 IK 控制柄并设置一个关键帧（“关键帧 > IK/FK 关键帧 > 设置 IK/FK 关键帧”(Key > IK/FK Keys > Set IK/FK Key)）。

3. 禁用 IK 解算器（禁用“关键帧 > IK/FK 关键帧 > 启用 IK 解算器”(Key > IK/FK Keys > Enable IK Solver)）。

4. 旋转所需关节并根据需要对边界关键帧之间的帧使用“设置 IK/FK 关键帧”(Set IK/FK Key)。

在不受“设置 IK/FK 关键帧”(Set IK/FK Key)控制的 IK 动画中插入 FK

1. 在动画的第一个帧处，选择 IK 控制柄，*启用* “解算器启用”(Solver Enable)并为“解算器启用”(Solver Enable)设置一个关键帧。

2. 在要插入 FK 的时间范围的结束帧处，选择 IK 控制柄并设置一个关键帧（“关键帧 > IK/FK 关键帧 > 设置 IK/FK 关键帧”(Key > IK/FK Keys > Set IK/FK Key)）。

3. 在要插入 FK 的时间范围的第一帧处，选择 IK 控制柄并设置一个关键帧（“关键帧 > IK/FK 关键帧 > 设置 IK/FK 关键帧”(Key > IK/FK Keys > Set IK/FK Key)）。

4. 禁用 IK 解算器（禁用“关键帧 > IK/FK 关键帧 > 启用 IK 解算器”(Key > IK/FK Keys > Enable IK Solver)）。

5. 旋转所需关节并根据需要对边界关键帧之间的帧使用“设置 IK/FK 关键帧”(Set IK/FK Key)。

**注**

FK 动画完成后，关节链可能会在启用 IK 解算器后翻转到异常位置。请参见

使用 IK 解算器异常关节翻转的疑难解答

。

## 相关主题

- [IK 和 FK 融合示例](IK%20和%20FK%20融合示例.md)

- [正向运动学(FK)](../../设置骨架姿势.md#WS17956D7ADBC6E736-185AC66B117AE30DA36-7FEE)

- [反向运动学 (IK)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-07C3BA47-32BB-477B-B6C5-1090E5C9B81C.htm)

- [IK/FK 融合](../IKFK%20融合.md)

- [“关键帧 > IK FK 关键帧”(Key > IK FK Keys)菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C5ACDDBC-9E30-443C-8419-F07FC41E9A86)

- [IK 融合](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E71102E0-0BA4-4F9D-9402-E6830889D569.htm#WS73099CC142F48755-7B21313411809411AE9-5EE3)

- [IK FK 控制](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E71102E0-0BA4-4F9D-9402-E6830889D569.htm#WS73099CC142F48755-7B21313411809411AE9-5EE0)
