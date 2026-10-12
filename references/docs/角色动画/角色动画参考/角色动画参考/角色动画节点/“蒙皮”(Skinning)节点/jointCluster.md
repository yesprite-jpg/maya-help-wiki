# jointCluster

## 关节簇属性(Joint Cluster Attributes)

#### 上边界(Upper Bound)

指定簇权重沿着其方向减少的父骨骼的长度百分比。根据“上方衰减类型”(Upper Dropoff Type)，当簇权重接近关节时簇权重会从“上限值”(Upper Value)开始减少。默认值为 10。

#### 上限值(Upper Value)

在“上边界”(Upper Bound)位置指定初始簇权重值。默认值为 0.5。

#### 上方衰减类型(Upper Dropoff Type)

指定簇权重如何在接近关节时沿着父骨骼减小。选择“线性”(linear) (0)、“正弦”(sine) (1)、“指数”(exponential) (2) 或“无”(none) (3)。默认值为“线性”(linear)。

#### 下边界(Lower Bound)

指定簇权重沿着其方向减少的关节骨骼的长度百分比。根据“下方衰减类型”(Lower Dropoff Type)，当簇权重接近关节时簇权重会从“下限值”(Lower Value)开始减少。默认值为 10。

#### 下限值(Lower Value)

在“下边界”(Lower Bound)位置指定初始簇权重值。默认值为 1。

#### 下方衰减类型(Lower Dropoff Type)

指定簇权重如何在接近关节时沿着关节的骨骼减小。选择“线性”(linear) (0)、“正弦”(sine) (1)、“指数”(exponential) (2) 或“无”(none) (3)。默认值为“线性”(linear)。

#### 相对(Relative)

指定仅当父关节簇柄发生移动、旋转或缩放时，变形才会生效。

#### 分辨率(Resolution)

指定 Maya 是提供完全变形，还是仅提供近似变形。选择包括“完全”(full)和“部分”(partial)。“完全”(Full)指定完全变形。“部分”指定近似变形，此种变形可提高 Maya 的显示性能。如果使用“部分”(partial)，Maya 会根据“分辨率”(Resolution)对簇权重向下取整。默认值为“完全”。

#### 百分比分辨率(Percent Resolution)

指定关节簇变形分辨率向下取整的增量百分比。Maya 使用增量百分比将蒙皮点簇权重舍入为下一个最小增量。例如，如果使用的“百分比分辨率”(Percent Resolution)为 5.00，则系统会将值为 .94 的蒙皮点的关节簇权重舍入为 .90。而值为 .46 的关节簇权重会被舍入为 .45。默认值为 5.00。（仅当将“分辨率”(Resolution)设定为“部分”(partial)时才可用。）

#### 角度插值(Angle Interpolation)

指定插值方向。当更改关节角度或权重百分比（即使是很小的量）时，使用该属性可以校正变形效果中的意外中断。当关节簇节点使用不合适的方向指导变形效果时，会发生中断。若要更改插值方向，可以将“角度插值”(Angle Interpolation)设定为最近（正值或负值）。默认情况下，“角度插值”(Angle Interpolation)为最近，可提供常见的刚性蒙皮变形效果。默认设置适用于大多数情况，但当遇到中断时，可以通过选择正或负的插值来调整变形效果。
