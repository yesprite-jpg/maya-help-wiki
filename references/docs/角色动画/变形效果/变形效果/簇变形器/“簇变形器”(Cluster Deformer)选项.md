# “簇变形器”(Cluster Deformer)选项

- 在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 > (创建)簇”(Deform > (Create) Cluster) > ![图：在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 (创建)簇”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1065 字 ≥300，非承重" -->

## “基本”(Basic)选项卡

#### 相对模式(Relative Mode)

指定簇变形是否仅在簇变形器控制柄本身已变换（移动、旋转或缩放）时发生。在启用“相对模式”(Relative Mode)的情况下，仅对簇变形器控制柄本身的变换会导致变形效果。在禁用“相对模式”(Relative Mode)的情况下，对父对象是簇变形器控制柄的对象的变换会导致变形效果。

例如，假设您正使用簇变形器来平滑角色蒙皮手臂的腕部周围的变形效果。如果在启用“相对模式”(Relative Mode)的情况下创建簇变形器，然后设置簇变形器控制柄与腕关节的父子关系，则可以旋转肩部关节，而不会导致腕部周围出现簇变形效果。但是，当簇变形器控制柄本身移动时，将导致围绕腕部的簇变形效果。默认设置为启用。

#### 封套(Envelope)

指定变形比例因子。值为 0 时不提供变形，值为 0.5 时提供一个缩放成完整效果一半的变形效果，同时值为 1 时提供完整的变形效果。使用滑块选择 0 和 1 之间的值。默认值为 1。

## “高级”(Advanced)选项卡

有关这些创建选项的信息，请参见[“高级”(Advanced)变形器选项](../变形器参考/变形器节点/“高级”%28Advanced%29变形器选项.md)。

#### 变形顺序(Deformation Order)

指定变形器节点在可变形对象的历史中的位置。有关变形器放置的详细信息，请参见[变形顺序](../使用变形器/节点、历史和变形顺序.md#WS17956D7ADBC6E7361D3EA46F117AE30F9F3-7FFC)。

#### 排除(Exclusive)

指定变形器集是否位于某个划分中。划分中的集不能有重叠的成员。如果启用该选项，“要使用的划分”(Partition To Use)和“新划分名称”(New Partition Name)选项将变为可用。默认设置为禁用。

#### 要使用的划分(Partition To Use)

列出所有现有划分和默认选择“创建新划分”(Create New Partition)。如果选择“新建划分”(New Partition)，则可以编辑“划分名称”(Partition Name)字段，以指定新划分的名称。只有当“排除”(Exclusive)处于启用状态时才可以使用。

#### 划分名称(Partition Name)

指定将包括变形器集的新划分的名称。建议的划分名称为 deformPartition，如果尚不存在，则将创建该名称。通常，可能会将所有排除式变形器集置于名为 deformPartition 的划分中。但是，可以根据需要创建多个划分并为这些划分命名。只有当“排除”(Exclusive)处于启用状态时才可以使用。
