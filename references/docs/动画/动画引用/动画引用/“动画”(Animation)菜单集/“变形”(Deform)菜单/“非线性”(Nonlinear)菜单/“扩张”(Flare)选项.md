# “扩张”(Flare)选项

- 在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 > (创建)非线性 > 扩张”(Deform > (Create) Nonlinear > Flare) > ![图：在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 (创建)非线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1518 字 ≥300，非承重" -->

## “基本”(Basic)选项卡

#### 下限(Low Bound)

指定扩张在变形器的局部负 Y 轴上的较低界限。值可以是负数或零。使用滑块从负 10.0000 到 0.0000 的范围内选择值。默认值为 -1.0000。

#### 上限(High Bound)

指定扩张在变形器的局部正 Y 轴上的较高界限。值只能为正数（最小值为 0）。可以使用滑块选择从 0.0000 到 10.0000 的值。默认值为 1.0000。

#### 开始扩张 X (Start Flare X)

在“下限”(Low Bound)中指定沿变形器 X 轴的扩张度。沿变形器的局部 X 轴进行扩张，具体因“曲线”(Curve)的值而异。可以使用滑块选择从 0.0000 到 10.0000 的值。默认值为 1.0000。

#### 开始扩张 Z (Start Flare Z)

指定在“下限”(Low Bound)处从变形器的 Z 轴扩张的量。沿变形器的局部 Z 轴扩张到“上限”(High Bound)，具体因“曲线”(Curve)的值而异。可以使用滑块选择从 0.0000 到 10.0000 的值。默认值为 1.0000。

#### 结束扩张 X (End Flare X)

指定在“上限”(High Bound)处从变形器的 X 轴扩张的量。从“下限”(Low Bound)开始扩张，并沿变形器的局部 X 轴扩张到“上限”(High Bound)，具体因“曲线”(Curve)的值而异。可以使用滑块选择从 0.0000 到 10.0000 的值。默认值为 1.0000。

#### 结束扩张 Z (End Flare Z)

在“上限”(High Bound)中指定沿变形器 Z 轴的扩张度。从“下限”(Low Bound)开始扩张，并沿变形器的局部 Z 轴扩张到“上限”(High Bound)，具体因“曲线”(Curve)的值而异。可以使用滑块选择从 0.0000 到 10.0000 的值。默认值为 1.0000。

#### 曲线(Curve)

指定在“下限”(Low Bound)和“上限”(High Bound)之间曲率（扩张曲线的剖面）的量。值 0 指定无曲率（线性插值）。正值指定向外凸起曲率。负值指定向内凹进曲率。可以使用滑块选择从 0.0000 到 10.0000 的值。默认值为 0.0000。

## “高级”(Advanced)选项卡

请参见[“高级”(Advanced)变形器选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-3D228DBA-C968-4870-9B1D-8C2C60DE6970.htm)。

#### 变形顺序(Deformation Order)

指定变形器节点在变形对象历史中的放置。有关变形器放置的详细信息，请参见[变形顺序](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6EC1834B-213C-45F9-B723-0BB8039325FC#WS17956D7ADBC6E7361D3EA46F117AE30F9F3-7FFC)。

#### 排除(Exclusive)

指定变形器集是否位于某个划分中。划分中的集不能有重叠的成员。如果启用该选项，“要使用的划分”(Partition To Use)和“新划分名称”(New Partition Name)选项将变为可用。默认设置为禁用。

#### 要使用的划分(Partition To Use)

列出所有现有划分和默认选择“创建新划分”(Create New Partition)。如果选择“创建新划分”(Create New Partition)，可以编辑“新划分名称”(New Partition Name)字段以指定新划分的名称。只有当“排除”(Exclusive)处于启用状态时才可以使用。

#### 划分名称(Partition Name)

指定将包括变形器集的新划分的名称。建议的划分名称为 deformPartition，如果尚不存在，则将创建该名称。通常，可能会将所有排除式变形器集置于名为 deformPartition 的划分中。但是，可以根据需要创建多个划分并为这些划分命名。只有当“排除”(Exclusive)处于启用状态时才可以使用。
