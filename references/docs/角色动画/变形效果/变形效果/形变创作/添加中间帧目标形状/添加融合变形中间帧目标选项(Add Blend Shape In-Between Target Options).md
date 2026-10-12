# 添加融合变形中间帧目标选项(Add Blend Shape In-Between Target Options)

在[形变编辑器](../形变编辑器.md)中选择“形变 > 添加中间帧目标”(Shapes > Add In-Between Target) > ![图：在形变编辑器中选择“形变 添加中间帧目标”(Shapes Add In-Between Target) ，可根据在此处设…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 499 字 ≥300，非承重" -->，可根据在此处设置的选项将中间帧目标形状添加到选定的目标形状。有关详细信息，请参见[添加中间帧目标形状](../添加中间帧目标形状.md)。

## 目标类型(Target Type)

- 绝对(Absolute)：创建状态不会随招牌目标形状（即：要添加中间帧形状的目标形状）而更改的中间帧目标形状。

- 相对(Relative)：创建相对于招牌目标形状的状态而更改的中间帧目标形状。可以选择插值类型（“线性”(Linear)、“平滑”(Smooth)或“自定义”(Custom)），然后编辑用于插值的曲线。

## 最大影响权重(Maximum Influence Weight)

- 使用当前目标形状权重(Use current target shape weight)：使用招牌（选定）目标形状的当前权重值添加中间帧目标形状。

- 自定义(Custom)：使用滑块为要添加到招牌目标形状的中间帧目标形状选择权重值。

## 检查拓扑(Check Topology)

选择此选项可检查选择用于中间帧目标形状的基础对象和目标对象是否具有相同的拓扑（多边形对象为顶点，NURBS 对象为 CV）。默认设置为启用。
