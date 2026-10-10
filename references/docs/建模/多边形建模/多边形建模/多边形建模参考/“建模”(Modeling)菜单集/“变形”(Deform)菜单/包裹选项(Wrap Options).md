# 包裹选项(Wrap Options)

- 在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 > (创建)包裹”(Deform > (Create) Wrap) > ![图：在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 (创建)包裹…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1642 字 ≥300，非承重" -->

#### 独占式绑定(Exclusive bind)

启用后，包裹变形器目标曲面的行为将类似于刚性绑定蒙皮，同时“权重阈值”(Weight Threshold)将被禁用。包裹变形器目标曲面上的每个曲面点只受单个包裹影响对象点的影响。

**注**

独占式绑定仅适用于多边形网格目标曲面。

#### 自动权重阈值(Auto Weight Threshold)

启用后，包裹变形器将通过计算最小“最大距离”(Max Distance)值，自动设定包裹影响对象形状的最佳权重，从而确保网格上的每个点受一个影响对象的影响。默认情况下，此选项处于启用状态。

#### 权重阈值(Weight Threshold)

允许用户根据包裹影响对象组件与变形对象之间的近似性，手动指定这些对象的形状的影响。根据包裹影响对象的点密度不同（例如，CV 数），更改“权重阈值”(Weight Threshold)可以更改变形效果的整体平滑度。值的范围在 0.000（平滑）到 1.000（尖锐）之间。使用滑块选择 0.000 到 1.000 之间的值。默认值为 0.000。

**注**

“权重阈值”(Weight Threshold)、“使用最大距离”(Use Max Distance)和“最大距离”(Max Distance)仅在禁用“自动权重阈值”(Auto Weight Threshold)时可用。

#### 使用最大距离(Use Max Distance)

如果要设定“最大距离”(Max Distance)值并限制影响区域，启用“使用最大距离”(Use Max Distance)。

#### 最大距离(Max Distance)

指定包裹影响对象点的影响区域。通过使用“最大距离”(Max Distance)限制影响区域，可以手动限制 Maya 执行变形所需的内存量。所需的内存越少，性能越高。在处理高分辨率包裹影响对象时，“最大距离”(Max Distance)的作用尤其明显。

**注**

“权重阈值”(Weight Threshold)在“最大距离”(Max Distance)值定义的影响区域内生效。

“最大距离”(Max Distance)值采用 Maya 的工作单位，默认为厘米（“窗口 > 设置/首选项 > 首选项 > 设置 > 工作单位”(Window > Settings/Preferences > Preferences > Settings > Working Units)）。“最大距离”(Max Distance)的默认值为 1，这会将影响区域限制在每点周围 1 个单位的距离内，有助于减少内存占用。“最大距离”(Max Distance)为 0 时表示影响区域无限大。该设置将使用最大内存量。

“自动权重阈值”(Auto Weight Threshold)值为最小的切割提供合适的开始权重。如果对使用该值生成的变形不够满意，可以禁用“自动权重阈值”(Auto Weight Threshold)并手动调整“权重阈值”(Weight Threshold)。若要获得最佳值，首先使用显示在“属性编辑器”(Attribute Editor)中的“自动权重阈值”(Auto Weight Threshold)值，然后逐渐减少该值，直到获得满意的变形。

#### 渲染影响对象(Render Influence Objects)

设定是否渲染包裹影响对象。如果启用，包裹影响对象将在渲染场景时可见；如果禁用，包裹影响对象将不可见。

#### 衰减模式(Falloff Mode)

从以下选项中进行选择。

#### 体积(Volume)

将包裹变形器设置为使用直接距离来计算包裹影响对象的权重。这是默认选项。

#### 表面(Surface)

将变形器设定为使用基于曲面的距离来计算权重。使用该模式，可以创建包裹变形器效果，如上下唇相互独立移动的嘴部。

**注**

处理稠密几何体时，将“衰减模式”(Falloff Mode)设定为“表面”(Surface)会对性能产生负面影响，因为这需要更多的资源来计算基于曲面的变形。
