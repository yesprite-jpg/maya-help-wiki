# shrinkWrap

## 收缩包裹属性

#### 投影(Projection)

下列投影方法确定如何将包裹器对象的每个点投影到目标对象：

#### 如果没有交点，则用最近点(Closest If No Intersection)

启用此选项时，Maya 将为未使用当前选定的投影方法碰到目标对象的点使用“最近”(Closest)投影方法。此选项可确保包裹器对象的所有点都变为目标形状。

#### 反转(Reverse)

启用此选项后，会在相反的方向上投影包裹器对象上的点。例如，该选项可用于沿某个轴的负方向投影包裹器。

#### 双向(Bidirectional)

启用此选项后，会向后和向前投影包裹器对象的点，以查看它们是否碰到目标对象。如果某个点在两个方向上都碰到目标，则会使用最短距离。

#### 偏移(Offset)

指定发生变形后包裹器对象与其目标之间的距离。如果增大“偏移”(Offset)值，Maya 会沿目标的曲面法线移动包裹器的点。

**注**

提示：

可以使用

“偏移”(Offset)

修复包裹器和目标之间的穿透。

#### 目标膨胀(Target Inflation)

指定沿其曲面法线应用到目标对象的膨胀量。

虽然“目标膨胀”(Target Inflation)和[“偏移”(Offset)](../“变形”%28Deform%29菜单/收缩包裹选项%28Shrinkwrap%20Options%29.md#GUID-832864E7-A266-4EA8-92A1-7D570759D74E__GUID-22EBF644-C9A7-4D87-86C5-F54EBE6AE417)会产生类似的效果，但“目标膨胀”(Target Inflation)通常会生成更好的变形，尽管会耗费一些额外的计算成本。

#### 边界框中心(Bounding Box Center)

如果禁用此选项（默认设置），会朝向目标的局部坐标系的中心投影包裹器对象的点。启用此选项时，会朝向目标的边界框的中心投影包裹器对象的点。

**注**

该选项仅在

“投影”(Projection)

设置为

“朝向中心”(Toward Center)

时可用。

#### 轴参照(Axis Reference)

设置参考坐标系。您可以从“目标局部”(Target Local)、“变形局部”(Deformed Local)和“全局”(Global)中选择。

**注**

该选项仅在

“投影”(Projection)

设置为

“平行于轴”(Parallel To Axes)

时可用。

#### 沿 X、Y、Z (Along X, Y, Z)

指定沿哪个轴投影包裹器的点。如果选定多个轴，投影会沿相应的单位向量发生。

**注**

该选项仅在

“投影”(Projection)

设置为

“平行于轴”(Parallel To Axes)

时可用。

#### 单个收缩包裹节点(Single Shrinkwrap Node)

启用此选项后，可将所有收缩包裹对象视为单个收缩包裹节点。执行此操作可在整个组内应用同一设置。

#### 目标平滑级别(Target Smooth Level)

指定 Maya 通过向网格上的多边形添加分段来平滑目标对象的次数。“目标平滑级别”(Target Smooth Levels)范围为 1 到 4。值越大，对象就越平滑。

## 衰减控件

#### 衰减(Falloff)

当包裹器对象的某些点撞击目标对象而其他点不撞击时，“衰减”(Falloff)值将跨此边界平滑变形。值越大，包裹器和目标之间的边界越平滑。

#### 衰减迭代次数(Falloff Iterations)

指定将应用于包裹器和目标之间边界的衰减迭代次数。

## 形状保留控件

#### 启用形状保留(Enable Shape Preservation)

使包裹器对象尽可能接近其原始形状，即使在进行收缩包裹处理时也是如此。启用时（默认设置），Maya 会松弛包裹器的边以保持其原始长度。

#### 步数(Steps)

指定执行松弛的次数。

#### 每步长迭代数(Iterations Per Step)

指定每“步长”(Step)迭代次数。迭代次数是在一个步长内发生的计算次数。精确度随迭代次数的增加而增加。

#### 方法(Method)

允许您指定如何将松弛应用于包裹器对象。

#### 三角形(Triangles)

松弛三角化网格的边。此方法可保留包裹器对象的形状和大小。

#### 边(Edges)

仅松弛包裹器对象的边。

#### 重新投影(Reprojection)

在每个松弛步骤后，会使用[最近(Closest)](../“变形”%28Deform%29菜单/收缩包裹选项%28Shrinkwrap%20Options%29.md#GUID-832864E7-A266-4EA8-92A1-7D570759D74E__GUID-767B0744-CC8B-49D5-8E39-1D80D4D09149)投影方法将包裹器对象重新投影到目标对象。以下选项可用于控制重新投影。

#### 无重新投影(No Reprojection)

关闭“重新投影”(Reprojection)。

#### 单一重新投影(Single Reprojection)

在完成所有松弛迭代后，立即将包裹器对象重新投影到目标对象。请参见[每步长迭代数(Iterations Per Step)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-2B3558DD-2EB2-4525-B716-885E859E27B8.htm#GUID-2B3558DD-2EB2-4525-B716-885E859E27B8__GUID-0408EFDC-A0FF-415A-B91E-F95358393441)。

#### 每步长重新投影(Reprojection Per Step)

在每次松弛迭代后，将包裹器对象重新投影到目标对象。请参见[每步长迭代数(Iterations Per Step)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-2B3558DD-2EB2-4525-B716-885E859E27B8.htm#GUID-2B3558DD-2EB2-4525-B716-885E859E27B8__GUID-0408EFDC-A0FF-415A-B91E-F95358393441)。

## 平滑目标控件

有关“平滑目标控件”(Smooth Target Controls)的详细信息，请参见[网格 > 平滑(Mesh > Smooth)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-071B78B2-ACAF-473D-9B5E-4256C4857B96#GUID-071B78B2-ACAF-473D-9B5E-4256C4857B96__WS17956D7ADBC6E736-2B54A37117AE335115-7FFB)。

## 相关主题

- [收缩包裹变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-C2D83E32-2D69-478A-B159-6E1005480378.htm)

- [收缩包裹选项](../“变形”%28Deform%29菜单/收缩包裹选项%28Shrinkwrap%20Options%29.md)

- [编辑 > 收缩包裹(Edit > ShrinkWrap)](../“变形”%28Deform%29菜单.md#GUID-C1B5085D-3229-4BE8-989E-95C460ADB79C__GUID-CEA00618-1FFC-4ACD-8B6A-A6E7900F6BEA)
