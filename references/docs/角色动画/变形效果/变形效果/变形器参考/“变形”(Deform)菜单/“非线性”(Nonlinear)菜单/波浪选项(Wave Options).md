# 波浪选项(Wave Options)

- 在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 > (创建)非线性 > 波浪”(Deform > (Create) Nonlinear > Wave) > ![图：在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 (创建)非线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1143 字 ≥300，非承重" -->

## “基本”(Basic)选项卡

#### 最小半径(Min Radius)

指定圆形正弦波的最小半径。使用滑块来选择从 0.0000 到 1.0000 的值。默认值为 0.0000。

#### 最大半径(Max Radius)

指定圆形正弦波的最大半径。使用滑块来选择从 0.0000 到 10.0000 的值。默认值为 1.0000。

#### 振幅(Amplitude)

指定正弦波的振幅（最大波数）。使用滑块选择从 -5.0000 到 5.0000 的值。默认值为 0.0000（无波）。

#### 波长(Wavelength)

指定正弦波的频率。频率越高，则波长越小。频率越低，则波长越大。使用滑块选择从 -0.1000 到 10.0000 的值。默认值为 1.0000。

#### 衰减(Dropoff)

指定振幅的衰退方式。负值指定朝向变形器控制柄中心方向的衰退（最小值为 -1.0000），正值指定远离变形器控制柄中心方向的衰退（最大为 1.0000）。使用滑块选择从 -1.0000 到 1.0000 的值。默认值为 0.0000（无衰退）。

#### 偏移(Offset)

指定正弦波相对于变形器控制柄中心的位置。更改该值可创造涟漪效果。使用滑块选择从 -10.0000 到 10.0000 的值。默认值为 0。

## “高级”(Advanced)选项卡

请参见[“高级”(Advanced)变形器选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-3D228DBA-C968-4870-9B1D-8C2C60DE6970.htm)。

#### 变形顺序(Deformation Order)

指定变形器节点在可变形对象的历史中的位置。有关变形器放置的详细信息，请参见[变形顺序](../../../使用变形器/节点、历史和变形顺序.md#WS17956D7ADBC6E7361D3EA46F117AE30F9F3-7FFC)。

#### 排除(Exclusive)

指定变形器集是否位于某个划分中。划分中的集不能有重叠的成员。如果启用该选项，“要使用的划分”(Partition To Use)和“新划分名称”(New Partition Name)选项将变为可用。默认设置为禁用。

#### 要使用的划分(Partition To Use)

列出所有现有划分和默认选择“创建新划分”(Create New Partition)。如果选择“创建新划分”(Create New Partition)，可以编辑“新划分名称”(New Partition Name)字段以指定新划分的名称。只有当“排除”(Exclusive)处于启用状态时才可以使用。

#### 划分名称(Partition Name)

指定将包括变形器集的新划分的名称。建议的划分名称为 deformPartition，如果尚不存在，则将创建该名称。通常，可能会将所有排除式变形器集置于名为 deformPartition 的划分中。但是，可以根据需要创建多个划分并为这些划分命名。只有当“排除”(Exclusive)处于启用状态时才可以使用。
