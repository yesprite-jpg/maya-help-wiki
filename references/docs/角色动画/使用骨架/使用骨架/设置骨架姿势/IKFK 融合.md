# IK/FK 融合

您可以使用 FK 和 IK 设定关节链的关节的姿势和动画。这称为动画*融合*。请参见[融合 IK 和 FK 动画](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-8B0B343A-B00A-427C-8C79-E2B9008C4A88.htm)。由于 IK 控制柄有“IK 融合”(Ik Blend)属性，因此可实现这种 FK 和 IK 动画之间的融合。通过“IK 融合”(Ik Blend)，您可以在使用纯 FK 或纯 IK 的造型与动画之间切换，以及控制这两种动画之间的融合。请参见 [IK 融合](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E71102E0-0BA4-4F9D-9402-E6830889D569.htm#WS73099CC142F48755-7B21313411809411AE9-5EE3)。

设定同时具有 FK 和 IK 的关节链的姿势和动画会改变关节和骨骼在场景视图中的显示方式。使用三种默认颜色或用户定义的颜色绘制具有 FK 和 IK 的关节链。蓝色关节链表示具有纯 FK 动画的骨架，棕色关节链表示具有纯 IK 动画的骨架，而洋红色关节链表示动画融合的结果。

此外，还可以自定义 IK/FK 关节链的颜色和大小。请参见[设定 IK/FK 动画关节链的显示](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-4C49738C-CD0C-4CC4-B3B2-799C9552D1AB.htm)。

除了在多个帧上融合 IK 和 FK 动画外，还可以在单个帧上进行融合。如果要制作 IK 和 FK 之间瞬时切换的动画（如手从放置状态迅速举起来），应该在单个帧上融合 IK 和 FK。反之，如果希望设置轻松进出 IK 或 FK 的运动的动画（如角色跳起并抓住单杠），则应该在几个帧上融合 IK 和 FK。在需要防止动画抖动时，在几个帧上融合 IK 和 FK 也非常有用。

## 相关主题

- [融合 IK 和 FK 动画](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-8B0B343A-B00A-427C-8C79-E2B9008C4A88.htm)

- [IK 解算器属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E71102E0-0BA4-4F9D-9402-E6830889D569.htm#WS17956D7ADBC6E7363438120E117AE30D38F-7FF4)
