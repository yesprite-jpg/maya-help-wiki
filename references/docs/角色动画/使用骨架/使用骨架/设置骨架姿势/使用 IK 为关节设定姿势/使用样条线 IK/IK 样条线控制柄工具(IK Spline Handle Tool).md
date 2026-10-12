# IK 样条线控制柄工具(IK Spline Handle Tool)

- 在“装备”(Rigging)菜单集（按 F3 键）中，选择“骨架 > 创建 IK 样条线控制柄”(Skeleton > Create IK Spline Handle) > ![图：在“装备”(Rigging)菜单集（按 F3 键）中，选择“骨架 创建 IK 样条线控制柄”(Skeleton Crea…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2321 字 ≥300，非承重" -->。

## IK 样条线控制柄设置(IK Spline Handle Settings)

#### 根在曲线上(Root on Curve)

启用时，IK 样条线控制柄的起始关节即可约束到曲线。可以拖动偏移操纵器，沿曲线滑动起始关节（及其子对象）。

禁用该选项后，可以移动起始关节远离曲线。起始关节不再被约束到曲线。Maya 会忽略“偏移”(Offset)属性，起始关节中也不存在偏移操纵器。

[IK 控制柄属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E71102E0-0BA4-4F9D-9402-E6830889D569.htm#WS17956D7ADBC6E7363438120E117AE30D38F-7FF9)也提供了该选项。

#### 自动创建根轴(Auto Create Root Axis)

启用该选项后，将使用样条线 IK 控制柄在场景层次中的起始关节上创建父对象变换节点。可通过移动和旋转此变换节点（而不是起始关节）来避免起始关节出现意外翻转。详细信息请参见[防止在样条线 IK 链中翻转](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-D107AA78-C999-451D-BCAC-CFFF1F007F17.htm)。只能在“根在曲线上”(Root on Curve)被禁用时启用该选项。

“自动创建根轴”(Auto Create Root Axis)是“IK 样条线控制柄工具”(IK Spline Handle Tool)设置的专用选项。

#### 自动将曲线结成父子关系(Auto Parent Curve)

如果样条线 IK 控制柄的起始关节有父对象，此设置可以使样条线 IK NURBS 曲线成为该父对象的子对象。因此，曲线和关节链将随着父对象的变换而移动。

如果创建从骨架根关节下的链关节起始的控制柄，启用该选项可确保关节链随其父关节的变换而移动。

“自动将曲线结成父子关系”(Auto Parent Curve)是“IK 样条线控制柄工具”(IK Spline Handle Tool)选项的专用选项。

#### 将曲线捕捉到根(Snap Curve to Root)

启用该选项后，曲线的起点会捕捉到起始关节位置。链中的关节将旋转以适应曲线形状。

“将曲线捕捉到根”(Snap Curve to Root)仅在工具设置中的“自动创建曲线”(Auto Create Curve)已被禁用，且用户已经创建自己的曲线后才会影响样条线 IK 控制柄。

如果要将该曲线作为关节链的固定路径使用，请禁用“将曲线捕捉到根”(Snap Curve to Root)

“将曲线捕捉到根”(Snap Curve to Root)是“IK 样条线控制柄工具”(IK Spline Handle Tool)设置的专用选项。

#### 自动创建曲线(Auto Create Curve)

启用时，在您创建样条线 IK 控制柄时会创建 NURBS 曲线。创建的曲线会跟随关节链路径。

如果“自动创建曲线”(Auto Create Curve)处于启用状态，而且“自动简化曲线”(Auto Simplify Curve)已被禁用，那么在创建样条线 IK 控制柄的同时，将创建一条通过样条线 IK 链所有关节的复杂曲线。

如果“自动创建曲线”(Auto Create Curve)处于启用状态，而且“自动简化曲线”(Auto Simplify Curve)已被启用，那么在创建控制柄时，会自动创建类似于关节链形状的简化曲线。“跨度数”(Number of Spans)越大，曲线与关节链就越匹配。曲线的曲线次数为 3（立方）。

如果样条线 IK 关节链是现有骨架的一部分，应启用“自动创建曲线”(Auto Create Curve)。如果要使用曲线作为滑动关节链的路径，应禁用“自动创建曲线”(Auto Create Curve)。

当“自动创建曲线”(Auto Create Curve)处于禁用状态时，必须为关节链创建 NURBS 曲线。

“自动创建曲线”(Auto Create Curve)是“IK 样条线控制柄工具”(IK Spline Handle Tool)设置的专用选项。

#### 自动简化曲线(Auto Simplify Curve)

启用时，会自动以指定的“跨度数”(Number of Spans)创建 NURBS 曲线。跨度数相当于曲线中的 CV 数。曲线的曲线次数为 3（立方）。

如果创建带有较少 CV 的曲线，对曲线形状和骨架移动的控制精度将会降低，但能够轻松操纵曲线及其关节链。如果使用较少的 CV，选择和拖动 CV 所需的时间将会缩短，而且更有可能获得平滑的曲线。

“自动简化曲线”(Auto Simplify Curve)仅在“自动创建曲线”(Auto Create Curve)被启用时可用。

“自动简化曲线”(Auto Simplify Curve)是“IK 样条线控制柄工具”(IK Spline Handle Tool)设置的专用选项。

#### 跨度数(Number of Spans)

指定在您创建样条线 IK 控制柄时为曲线自动创建的 CV 数。

跨度数和 CV 数之间的比率关系如下：CV 数=跨度数+3。

| 跨度数 | CV 数 |
|---|---|
| 1 | 4 |
| 2 | 5 |
| 3 | 6 |
| 4 | 7 |

“跨度数”(Number of Spans)仅在“自动创建曲线”(Auto Create Curve)处于启用状态时可用。

“跨度数”(Number of Spans)是“IK 样条线控制柄工具”(IK Spline Handle Tool)设置的专用选项。

#### 根扭曲模式(Root Twist Mode)

启用该选项后，在末关节操纵扭曲操纵器会使起始关节和其他关节发生轻微扭曲。

禁用该选项后，起始关节将不会扭曲。如果要旋转起始关节，必须使用滚动操纵器。请参见[弹簧 IK 解算器](../使用弹簧%20IK/弹簧%20IK%20解算器.md)。

#### 扭曲类型(Twist Type)

该选项指定如何在关节链中发生扭曲。

- **“线性”(Linear)**均匀扭曲所有部位。

- **“缓入”(Ease In)**在链结束处的扭曲比开始处多。

- **“缓出”(Ease Out)**在链开始处的扭曲比结束处多。

- **“缓入缓出”(Ease In Out)**在中部的扭曲比两端多。

**注**

提示：

使用

属性编辑器

创建 IK 样条线控制柄后，也可以更改

“扭曲类型”(Twist Type)

。

## 相关主题

- [IK 解算器](../IK%20解算器.md)

- [创建样条线 IK 控制柄](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-356B7E1F-8715-4D8F-978A-888E145B4700.htm)
