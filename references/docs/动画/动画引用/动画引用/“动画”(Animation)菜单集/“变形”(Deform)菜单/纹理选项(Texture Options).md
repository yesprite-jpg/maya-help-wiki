# 纹理选项(Texture Options)

- 在“动画”(Animation)、“绑定”(Rigging)和“建模”(Modeling)菜单集中：“变形 > (创建)纹理”(Deform > (Create) Texture) > ![图：在“动画”(Animation)、“绑定”(Rigging)和“建模”(Modeling)菜单集中：“变形 (创建)纹理…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2610 字 ≥300，非承重" -->

## “基本”(Basic)选项卡

#### 点空间(Point Space)

指定如何对纹理进行采样。

#### 世界(World)

使用“世界”(World)，纹理变形器会将每个顶点的世界位置转化为采样纹理。

对于 2D 纹理，Y 轴将会被忽略。X 轴和 Y 轴上的该值将转化为 UV。

由于顶点的世界位置可以通过变换对象来更改，因此您可以变换对象以修改变形。

#### 局部(Local)

使用“局部”(Local)，纹理变形器会将每个顶点的局部位置转化为采样点。

对于 2D 纹理，Y 轴将会被忽略。X 轴和 Y 轴上的该值将转化为 UV。

由于顶点的局部位置不能通过变换对象来更改，因此您不能变换对象以修改变形。

#### UV

使用“UV”，纹理变形器将使用每个顶点的当前 UV 值来对像素数据进行采样。UV 仅支持 2D 纹理。

**注**

UV 点空间不支持 NURBS 对象。

#### 方向(Direction)

指定变形的方向。

#### 控制柄(Handle)

使用“控制柄”(Handle)，可以使用控制柄来控制变形的方向。选择“控制柄”(Handle)时，将在原点处显示一个控制柄操纵器。您可以移动、旋转和缩放该控制柄来编辑纹理变形器的效果。选择了其他方向选项时，该控制柄将会隐藏。

**注**

如果删除该控制柄，将会同时删除变形器节点和调整节点。

#### 法线(Normal)

使用“法线”(Normal)，可以将变形方向替换为每个多边形面的法线。

#### 向量(Vector)

使用**“向量”(Vector)**，可以让**“纹理”(Texture)**影响变形的方向。**“纹理”(Texture)**包含三个颜色通道。它们可分别用于计算 X、Y 和 Z 轴上的变形。

#### 向量空间(Vector Space)

指定要将纹理变形用于的坐标空间。

#### 切线(Tangent)

面上的坐标空间由法线、切线和次法线定义，这些线相互之间呈正交化和归一化。如果纹理使用“切线”(Tangent)模式提取，则使用此选项。使用“切线”(Tangent)，坐标空间可以通过旋转和缩放对象进行更改。换句话说，当用户旋转或缩放对象时，变形也将旋转或缩放。

#### 对象(Object)

模型的局部坐标空间。如果纹理使用“对象”(Object)模式提取，则使用此选项。使用“对象”(Object)，坐标空间可以通过旋转和缩放对象进行更改。换句话说，当用户旋转或缩放对象时，变形也将旋转或缩放。

#### 世界(World)

3D 场景的坐标空间。如果纹理使用“世界”(World)模式提取，则使用此选项。使用“世界”(World)，坐标空间不能通过旋转和缩放对象进行更改。换句话说，当用户旋转或缩放对象时，变形在三个轴上是固定的。

#### 纹理(Texture)

指定纹理变形器的输入纹理。输入纹理用于计算每个点的变形。选中“控制柄”(Handle)或“法线”(Normal)（请参见[“方向”(Direction)](纹理选项%28Texture%20Options%29.md#GUID-1A135E0C-89AA-4806-A3AB-361E45F06470__GUID-95E2B6EF-E4F1-4F6E-BBE9-E31EA1296813)）时，**“纹理”(Texture)**将转化为亮度。值越大，点沿指定方向的变形通常就越大。选中“向量”(Vector)（请参见[“方向”(Direction)](纹理选项%28Texture%20Options%29.md#GUID-1A135E0C-89AA-4806-A3AB-361E45F06470__GUID-95E2B6EF-E4F1-4F6E-BBE9-E31EA1296813)）时，将为三个轴使用“纹理”(Texture)的三个通道。

您可以将属性**“outColor”**从纹理关联到“纹理”(Texture)以应用有关变形的颜色数据。支持的类型有三种：2D 纹理、3D 纹理和分层纹理。

“纹理”(Texture)的默认值是黑色。您可以使用属性编辑器修改此默认值。如果“纹理”(Texture)没有连接，变形器将使用此默认值。

#### 强度(Strength)

指定变形的影响强度。较大的值会增加变形的强度。

通过将“方向”(Direction)设置为**“控制柄”(Handle)**或**“法线”(Normal)**使用强度。

#### 偏移(Offset)

指定平移的偏移。

更改此值可以创建蠕动效果。使用滑块指定 -10.0000 到 10.0000 间的值。默认值为 0.0000。

通过将“方向”(Direction)设置为**“控制柄”(Handle)**或**“法线”(Normal)**使用偏移。

#### 向量强度(Vector Strength)

指定变形的影响强度。使用**“向量强度”(Vector Strength)**，可以在三个轴的每个轴上设置不同的强度。

**将“方向”(Direction)**设置为**“向量”(Vector)**时，**“向量强度”(Vector Strength)**将会发挥作用。

#### 向量偏移(Vector Offset)

指定变形的偏移。使用**“向量偏移”(Vector Offset)**，可以在三个轴的每个轴上设置偏移变形。

**将“方向”(Direction)**设置为**“向量”(Vector)**时，**“向量偏移”(Vector Offset)**将会发挥作用。

#### 封套(Envelope)

指定变形比例因子。

值为 0.0000 时不提供变形，值为 0.5000 时提供一个缩放成完整效果一半的变形效果，值为 1.0000 时提供完整的变形效果。使用相应滑块可选择介于 0.0000 到 1.0000 之间的值。默认值为 1.0000

## “高级”(Advanced)选项卡

请参见[“高级”(Advanced)变形器选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-3D228DBA-C968-4870-9B1D-8C2C60DE6970.htm)。

#### 变形顺序(Deformation order)

指定在可变形对象的历史中变形器节点的放置。有关变形器放置的详细信息，请参见[变形顺序](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6EC1834B-213C-45F9-B723-0BB8039325FC#GUID-6EC1834B-213C-45F9-B723-0BB8039325FC__WS17956D7ADBC6E7361D3EA46F117AE30F9F3-7FFC)。

#### 排除(Exclusive)

指定变形器集是否位于某个划分中。划分中的集不能有重叠的成员。如果启用该选项，“要使用的划分”(Partition To Use)和“新划分名称”(New Partition Name)选项将变为可用。默认设置为禁用。

#### 要使用的划分(Partition To Use)

列出所有现有划分和默认选择“创建新划分”(Create New Partition)。如果选择“创建新划分”(Create New Partition)，可以编辑“新划分名称”(New Partition Name)字段以指定新划分的名称。只有当“排除”(Exclusive)处于启用状态时才可以使用。

#### 新划分名称(New Partition Name)

指定将包括变形器集的新划分的名称。建议的划分名称为 deformPartition，如果尚不存在，则将创建该名称。通常，可能会将所有排除式变形器集置于名为 deformPartition 的划分中。但是，可以根据需要创建多个划分并为这些划分命名。只有当“排除”(Exclusive)处于启用状态时才可以使用。
