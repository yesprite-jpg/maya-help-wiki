# “正弦”(Sine)选项

- 在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 > (创建)非线性 > 正弦”(Deform > (Create) Nonlinear > Sine) > ![图：在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 (创建)非线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1198 字 ≥300，非承重" -->

## “基本”(Basic)选项卡

#### 下限(Low Bound)

指定正弦沿变形器的局部 Y 轴负向波动的程度。值可以是负数或零。使用滑块指定 -10.0000 到 0.0000 间的值。默认值为 -1.0000。

#### 上限(High Bound)

指定正弦沿变形器的局部 Y 轴正向波动的程度。值只能为正数（最小值为 0）。使用滑块指定 0.0000 到 10.0000 间的值。默认值为 1.0000。

#### 振幅(Amplitude)

指定正弦波的振幅（最大波数）。使用滑块指定 -5.0000 到 5.0000 间的值。默认值为 0.0000（无波）。

#### 波长(Wavelength)

指定正弦沿变形器局部 Y 轴波动的频率。频率越高，则波长越小。频率越低，则波长越大。使用滑块指定 -0.1000 到 10.0000 间的值。默认值为 2.0000。

#### 衰减(Dropoff)

指定振幅的衰退方式。负值指定朝向变形器控制柄中心方向的衰退（最小值为 -1.0000），正值指定远离变形器控制柄中心方向的衰退（最大为 1.0000）。使用滑块指定 -1.0000 到 1.0000 间的值。默认值为 0.0000（无衰退）。

#### 偏移(Offset)

指定正弦波相对于变形器控制柄中心的位置。更改此值可以创建蠕动效果。使用滑块指定 -10.0000 到 10.0000 间的值。默认值为 0.0000。

## “高级”(Advanced)选项卡

请参见[“高级”(Advanced)变形器选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-3D228DBA-C968-4870-9B1D-8C2C60DE6970.htm)。

#### 变形顺序(Deformation Order)

指定变形器节点在变形对象历史中的放置。有关变形器放置的详细信息，请参见[变形顺序](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6EC1834B-213C-45F9-B723-0BB8039325FC#WS17956D7ADBC6E7361D3EA46F117AE30F9F3-7FFC)。

#### 排除(Exclusive)

指定变形器集是否位于某个划分中。划分中的集不能有重叠的成员。可选择启用或禁用（默认设置为禁用）。如果启用，则“要使用的划分”(Partition To Use)和“新划分名称”(New Partition Name)选项变为可用。

#### 要使用的划分(Partition To Use)

列出所有现有划分和默认选择“创建新划分”(Create New Partition)。如果选择“创建新划分”(Create New Partition)，可以编辑“新划分名称”(New Partition Name)字段以指定新划分的名称。只有当“排除”(Exclusive)处于启用状态时才可以使用。

#### 划分名称(Partition Name)

指定将包括变形器集的新划分的名称。建议的划分名称为 deformPartition，如果尚不存在，则将创建该名称。通常，可能会将所有排除式变形器集置于名为 deformPartition 的划分中。但是，可以根据需要创建多个划分并为这些划分命名。只有当“排除”(Exclusive)处于启用状态时才可以使用。
