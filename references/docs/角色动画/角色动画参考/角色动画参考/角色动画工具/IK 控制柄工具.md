# IK 控制柄工具

- 骨架 > 创建 IK 控制柄(Skeleton > Create IK Handle) > ![图：骨架 创建 IK 控制柄(Skeleton Create IK Handle) （在“装备”(Rigging)菜单集中）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1302 字 ≥300，非承重" -->（在“装备”(Rigging)菜单集中）

## IK 控制柄设置(IK Handle Settings)

#### 当前解算器(Current Solver)

此下拉菜单指定您的 IK 控制柄将具备的 IK 解算器的类型。默认选择为“旋转平面解算器”(Rotate-Plane Solver)和“单链解算器”(Single-Chain Solver)。请参见 [IK 解算器](../../../使用骨架/使用骨架/设置骨架姿势/使用%20IK%20为关节设定姿势/IK%20解算器.md)。

#### 自动优先级(Autopriority)

如果此选项处于启用状态，则 Maya 会在启动时自动设置 IK 控制柄的“优先级”(Priority)。Maya 根据骨架层次中 IK 控制柄的起始关节所在的位置指定 IK 控制柄的“优先级”(Priority)。例如，如果 IK 控制柄在根关节启动，则“优先级”(Priority)将设置为 1。如果 IK 控制柄从根关节正下方的一个关节开始，则“优先级”(Priority)将设置为 2，依此类推。默认情况下，“自动优先级”(Autopriority)处于禁用状态。

#### 解算器启用(Solver Enable)

如果此选项处于启用状态，IK 解算器（由“当前解算器”(Current Solver)指定）在创建时将处于活动状态。默认情况下，“解算器启用”(Solver Enable)处于启用状态，以便您可以立即使用 IK 控制柄形成关节链。请参见 [IK 解算器](../../../使用骨架/使用骨架/设置骨架姿势/使用%20IK%20为关节设定姿势/IK%20解算器.md)。

#### 捕捉启用(Snap Enable)

如果此选项处于启用状态，IK 控制柄将捕捉回到 IK 控制柄的末关节的位置。默认设置为启用。

#### 粘滞(Sticky)

如果此选项处于启用状态，则在您使用其他 IK 控制柄形成骨架时或平移、旋转或缩放各个关节时，IK 控制柄将粘滞到其当前位置和方向。默认情况下，“粘滞”(Sticky)处于禁用状态。请参见[粘滞](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E71102E0-0BA4-4F9D-9402-E6830889D569.htm#WS73099CC142F48755-7B21313411809411AE9-5EFC)。

#### 优先级(Priority)

此选项仅在“自动优先级”(Autopriority)处于禁用状态时才可用。指定 IK 单链控制柄的优先级。在两个或多个 IK 单链控制柄重叠（影响某些或所有的相同关节）时非常有用。“优先级”为 1 的 IK 控制柄为第一优先级，将首先旋转关节。“优先级”为 2 的 IK 控制柄为第二优先级，将接下来旋转关节，依此类推。默认值为 1。请参见[优先级](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E71102E0-0BA4-4F9D-9402-E6830889D569.htm#WS73099CC142F48755-7B21313411809411AE9-5EF8)。

#### 权重(Weight)

设置当前 IK 控制柄的权重值。

权重值与 IK 控制柄的末端效应器及其目标之间的当前距离相结合，用于确定当前 IK 链的解决方案及其具有相同“优先级”(Priority)设置的其他 IK 控制柄的解决方案的优先级。

当两个或多个具有相同“优先级”(Priority)的 IK 控制柄的末端效应器不能同时到达其目标时，首先对其末端效应器距离其目标最远且其权重最大的 IK 控制柄进行解算。

#### 位置方向权重(POWeight)

指定当前 IK 控制柄的末端效应器是否支持到达其目标的方向或位置。

设置为 1 时，末端效应器将试图到达 IK 控制柄的位置。设置为 0 时，末端效应器仅尝试到达 IK 控制柄的方向。默认值为 1.000。

**注**

ikHandle 节点参考中还介绍了

“IK 控制柄工具”(IK Handle Tool)

中可用的某些选项。有关其他信息，请参见

IK 控制柄属性

。

## 相关主题

- [IK 控制柄概述](../../../使用骨架/使用骨架/设置骨架姿势/使用%20IK%20为关节设定姿势/创建%20IK%20控制柄/IK%20控制柄概述.md)

- [IK 解算器](../../../使用骨架/使用骨架/设置骨架姿势/使用%20IK%20为关节设定姿势/IK%20解算器.md)

- [创建 IK 控制柄](../../../使用骨架/使用骨架/设置骨架姿势/使用%20IK%20为关节设定姿势/创建%20IK%20控制柄.md)
