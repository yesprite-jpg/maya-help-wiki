# 雕刻变形器选项(Sculpt Deformer Options)

- 在“动画”(Animation)、“绑定”(Rigging)和“建模”(Modeling)菜单集中：“变形 > 雕刻变形器”(Deform > Sculpt Deformer) > ![图：在“动画”(Animation)、“绑定”(Rigging)和“建模”(Modeling)菜单集中：“变形 雕刻变形器”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2027 字 ≥300，非承重" -->

## “基本”(Basic)选项卡

#### 模式(Mode)

指定雕刻变形器的模式。选择“翻转”(Flip)、“投影”(Project)或“拉伸”(Stretch)。默认值为“拉伸”(Stretch)。

#### 翻转(Flip)

在“翻转”(Flip)模式中，变形将在雕刻工具接近目标对象的几何体时发生。此外，“翻转”(Flip)模式会在雕刻工具的中心放置隐式定位器。该模式之所以称为“翻转”(Flip)，是因为雕刻工具的中心通过曲面时，变形的曲面将翻转到雕刻工具的另一侧。

#### 投影(Project)

在“投影”(Project)模式中，雕刻变形器将目标对象几何体投影到雕刻工具的曲面上。投影的范围取决于雕刻变形器的“衰减距离”(Dropoff Distance)属性。此外，“最大置换”(Max Displacement)属性指定投影直接发生在雕刻工具上，发生在雕刻工具内部，还是发生在雕刻工具外部。

#### 拉伸(Stretch)

在“拉伸”(Stretch)模式中，将雕刻工具移离几何体时，受影响的几何体曲面会拉伸或凸起，以追随雕刻工具。拉伸方向是从拉伸原点定位器标记的点到雕刻工具图形的曲面。

#### 内部模式(Inside Mode)

指定变形器如何影响可变形对象中位于雕刻球体内部的点。包含以下两种模式：“环形”(Ring)和“平坦”(Even)。

#### 环形(Ring)

该模式会将内部点推动到雕刻球体外部，从而在雕刻球体周围创建一种具有轮廓的类环效果。

#### 平坦(Even)

该模式会将内部点在雕刻球体周围均匀地扩散，从而创建一种平滑的球形效果。默认值为“平坦”(Even)。

#### 最大置换(Max Displacement)

指定雕刻球体可以将可变形对象的点从球体曲面推出的距离。可以使用滑块选择从 -10.000 到 10.000 之间的值。默认值为 0.100。

#### 衰减类型(Dropoff Type)

指定雕刻球体的影响范围如何下倾或衰减。（影响范围通过“衰减距离”(Dropoff Distance)指定。）包含以下两种“衰减类型”(Dropoff Types)：“无”(None)和“线性”(Linear)。

“无”指定没有下倾，即提供突然的衰减效果。

“线性”指定逐渐下倾，即提供线性降低的衰减效果。

选择“无”(None)或“线性”(Linear)。（默认值为“线性”(Linear)。）

#### 衰减距离(Dropoff Distance)

指定雕刻球体的影响范围。（影响范围的下倾方式是通过“衰减类型”(Dropoff Type)指定的。）

#### 位置(Positioning)

指定雕刻球体的放置。单击打开“位置”(Positioning)将雕刻球体定位到可变形对象内的中心。单击关闭该选项可将雕刻球体放置在工作区原点。请注意，如果要创建拉伸雕刻变形器（“模式”(Mode)设定为“拉伸”(Stretch)），将在雕刻球体上放置拉伸原点定位器。默认为打开，即将雕刻球体定位到可变形对象内的中心。

#### 分组(Grouping)

如果要创建拉伸雕刻变形器（“模式”(Mode)设定为“拉伸”(Stretch)），则可以选择是否将拉伸原点定位器与雕刻球体分组在一起。单击打开可将雕刻球体与拉伸原点定位器分组在一起。默认为关闭。

#### 雕刻工具(Sculpt Tool)

通过该工具，可以使用自定义 NURBS 曲面或多边形网格作为雕刻变形器对象。请参见[将 NURBS 或多边形对象用作雕刻变形器的雕刻工具](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-260F55C7-988E-4995-97C9-F7E0AE883551#WS1A9193826455F5FF6026605B1181C8F4F2E-3253)。

## “高级”(Advanced)选项卡

请参见[“高级”(Advanced)变形器选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-3D228DBA-C968-4870-9B1D-8C2C60DE6970.htm)。

#### 变形顺序(Deformation Order)

指定变形器节点在可变形对象的历史中的位置。有关变形器放置的详细信息，请参见[变形顺序](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6EC1834B-213C-45F9-B723-0BB8039325FC#WS17956D7ADBC6E7361D3EA46F117AE30F9F3-7FFC)。

#### 排除(Exclusive)

指定变形器集是否位于某个划分中。划分中的集不能有重叠的成员。如果启用该选项，“要使用的划分”(Partition To Use)和“新划分名称”(New Partition Name)选项将变为可用。默认设置为禁用。

#### 要使用的划分(Partition To Use)

列出所有现有划分和默认选择“创建新划分”(Create New Partition)。如果选择“创建新划分”(Create New Partition)，可以编辑“新划分名称”(New Partition Name)字段以指定新划分的名称。只有当“排除”(Exclusive)处于启用状态时才可以使用。

#### 新划分名称(New Partition Name)

指定将包括变形器集的新划分的名称。建议的划分名称为 deformPartition，如果尚不存在，则将创建该名称。通常，可能会将所有排除式变形器集置于名为 deformPartition 的划分中。但是，可以根据需要创建多个划分并为这些划分命名。只有当“排除”(Exclusive)处于启用状态时才可以使用。
