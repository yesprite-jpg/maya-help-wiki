# 扭曲选项(Twist Options)

- 在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 > (创建)非线性 > 扭曲”(Deform > (Create) Nonlinear > Twist) > ![图：在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 (创建)非线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 998 字 ≥300，非承重" -->

### “基本”(Basic)选项卡

#### 下限(Low Bound)

指定在变形器的局部 Y 轴上开始角度扭曲的位置。值必须为负数或零。使用滑块选择从 -10.0000 到 0.0000 的值。默认值为 -1.0000。

#### 上限(High Bound)

指定在变形器的局部 Y 轴上结束角度扭曲的位置。值必须为正数。使用滑块选择从 0.0000 到 10.0000 的值。默认值为 1.0000。

#### 开始角度(Start Angle)

指定在变形器控制柄局部负 Y 轴上的下限位置处扭曲的度数。使用滑块选择从 -10.0000 到 10.0000 的值。默认值为 0.0000。

#### 结束角度(End Angle)

指定在变形器控制柄局部正 Y 轴上的上限位置处扭曲的度数。使用滑块选择从 -10.0000 到 10.0000 的值。默认值为 0.0000。

### “高级”(Advanced)选项卡

请参见[“高级”(Advanced)变形器选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-3D228DBA-C968-4870-9B1D-8C2C60DE6970.htm)。

#### 变形顺序(Deformation Order)

指定变形器节点在变形对象历史中的放置。有关变形器放置的详细信息，请参见[“高级”(Advanced)变形器选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-3D228DBA-C968-4870-9B1D-8C2C60DE6970.htm)。

#### 排除(Exclusive)

指定变形器集是否位于某个划分中。划分中的集不能有重叠的成员。如果启用该选项，“要使用的划分”(Partition To Use)和“新划分名称”(New Partition Name)选项将变为可用。默认设置为禁用。

#### 要使用的划分(Partition To Use)

列出所有现有划分和默认选择“创建新划分”(Create New Partition)。如果选择“创建新划分”(Create New Partition)，可以编辑“新划分名称”(New Partition Name)字段以指定新划分的名称。只有当“排除”(Exclusive)处于启用状态时才可以使用。

#### 划分名称(Partition Name)

指定将包括变形器集的新划分的名称。建议的划分名称为 deformPartition，如果尚不存在，则将创建该名称。通常，可能会将所有排除式变形器集置于名为 deformPartition 的划分中。但是，可以根据需要创建多个划分并为这些划分命名。只有当“排除”(Exclusive)处于启用状态时才可以使用。
