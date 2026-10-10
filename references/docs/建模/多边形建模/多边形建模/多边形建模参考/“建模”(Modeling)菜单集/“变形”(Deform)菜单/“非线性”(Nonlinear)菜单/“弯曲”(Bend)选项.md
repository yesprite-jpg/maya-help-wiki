# “弯曲”(Bend)选项

- 在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 > (创建)非线性 > 弯曲”(Deform > (Create) Nonlinear > Bend) > ![图：在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 (创建)非线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1014 字 ≥300，非承重" -->

打开“创建弯曲变形器选项”(Create Bend Deformer Options)，可在其中更改设置，然后再创建变形器。

请参见[创建弯曲变形器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-71522A4F-F800-46CC-AF53-FD246E89EC8B)。

### “基本”(Basic)选项卡

#### 下限(Low Bound)

指定沿弯曲变形器的负 Y 轴弯曲的下限。值可以是负数或零。值可以是负数或零。使用滑块在 -10.0000 到 0.0000 的范围内选择值。默认值为 -1.0000。

#### 上限(High Bound)

指定沿弯曲变形器的正 Y 轴弯曲的上限。值只能是正数（最小值为 0.0000）。使用滑块在 0.0000 到 10.0000 的范围内选择值。默认值为 1.0000。

#### 曲率(Curvature)

指定弯曲量（以度为单位）。负值指定朝着弯曲变形器的负 X 轴弯曲。正值指定朝着变形器的正 X 轴弯曲。使用滑块选择介于 -230 到 230 之间的值。默认值为 0，表示不指定任何弯曲。

### “高级”(Advanced)选项卡

请参见[“高级”(Advanced)变形器选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-3D228DBA-C968-4870-9B1D-8C2C60DE6970.htm)。

#### 变形顺序(Deformation Order)

指定变形器节点在变形对象历史中的放置。有关变形器放置的详细信息，请参见[变形顺序](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6EC1834B-213C-45F9-B723-0BB8039325FC#WS17956D7ADBC6E7361D3EA46F117AE30F9F3-7FFC)。

#### 排除(Exclusive)

指定变形器集是否位于某个划分中。划分中的集不能有重叠的成员。如果启用该选项，“要使用的划分”(Partition To Use)和“新划分名称”(New Partition Name)选项将变为可用。默认设置为禁用。

#### 要使用的划分(Partition To Use)

列出所有现有划分和默认选择“创建新划分”(Create New Partition)。如果选择“创建新划分”(Create New Partition)，可以编辑“新划分名称”(New Partition Name)字段以指定新划分的名称。只有当“排除”(Exclusive)处于启用状态时才可以使用。

#### 新划分名称(New Partition Name)

指定将包括变形器集的新划分的名称。建议的划分名称为 deformPartition，如果尚不存在，则将创建该名称。通常，可能会将所有排除式变形器集置于名为 deformPartition 的划分中。但是，可以根据需要创建多个划分并为这些划分命名。只有当“排除”(Exclusive)处于启用状态时才可以使用。
