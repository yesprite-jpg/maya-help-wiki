# 使用 MEL 脚本将元数据添加到网格

若要将元数据添加到网格，请遵循以下准则：

  使用 dataStructure 命令，创建数据结构并定义其名称、其成员及其对应的数据类型。数据结构可以有多个成员。

  在此示例中，定义名为 ColorStruct 的数据结构，它具有成员 Color（类型为 float[3]）和成员 ID（类型为 int32）。

  ```text
dataStructure -format "raw" -asString "name=ColorStruct:float[3]=Color:int32=ID";
```

  创建后，数据结构无法修改。

  使用 addMetadata 命令创建一个空流以添加到对象（-streamName 标志）。指定应该向其添加元数据的通道类型（-channelName 标志），如预定义的网格通道：顶点、边、面或 vertexFace；或者为常规元数据选择的名称。指定定义要添加到对象的元数据的数据结构（-structure 标志）。

  可以将多个流添加到同一通道和同一对象。

  可以在各对象之间共享同一流。

  每个流可以包括多个成员 - 其成员在数据结构中进行定义。每个流仅允许有一个数据结构。

  在此示例中，创建两个流，其数据由 ColorStruct 数据结构定义。将这些流添加到两个网格的顶点通道。

  ```text
addMetadata -streamName "StreamOne" -channelName "vertex" -structure "ColorStruct" smcPlaneShape smcPlane1Shape;
addMetadata -streamName "StreamTwo" -channelName "vertex" -structure "ColorStruct" smcPlaneShape smcPlane1Shape;
```

  使用 editMetadata 命令，在对象上设置或移除元数据值。使用 -streamName 标志指定要填充的流（例如，在上面步骤 2 中创建的流），并使用 -memberName 标志指定流的成员。

  使用 -value 或 -stringValue 标志指定元数据。可以将元数据指定给组件，方法是使用其索引值或者选择它们。通过选择要向其添加元数据的组件（而不是使用 index 标志），可以编辑特殊网格通道（即，与网格组件隐式关联的通道：顶点、面、边和 faceVertex）上的流。其他流必须使用 index 标志进行编辑，因为它们未与任何特定的几何体元素关联。

  在此示例中，将元数据添加到 StreamOne 的 Color 和 ID 成员，再添加到 StreamTwo 的成员。通过引用其索引值将元数据添加到顶点。

  ```text
editMetadata -streamName "StreamOne" -memberName "Color" -value 2 -value 0.5 -value 1 -index 1 smcPlaneShape;
editMetadata -streamName "StreamOne" -memberName "ID" -value 17 -index 1 smcPlaneShape;
editMetadata -streamName "StreamTwo" -memberName "Color" -value -2 -value -0.5 -value 2.5 -index 2 smcPlaneShape;
editMetadata -streamName "StreamTwo" -memberName "ID" -value 3 -index 3 smcPlaneShape;
```

  在上面的示例中，两个流从同一数据结构获取了它们的值（因此顶点通道也是这样）。但是，通过为每个流指定不同的数据结构，也可以将不同的数据结构添加到同一通道。

  例如，

  ```text
//Create two data structures: ColorStruct and NameStruct
dataStructure -format "raw" -asString "name=ColorStruct:float[3]=Color:int32=ID";
dataStructure -format "raw" -asString "name=NameStruct:string=Name:int32=ID";

//Assign the ColorStruct data structure to StreamOne
addMetadata -streamName "StreamOne" -channelName "vertex" -structure "ColorStruct" smcPlaneShape smcPlane1Shape;
//Assign the NameStruct data structure to StreamTwo
addMetadata -streamName "StreamTwo" -channelName "vertex" -structure "NameStruct" smcPlaneShape smcPlane1Shape;

//Assign metadata to the Color and ID members of StreamOne/ColorStruct on smcPlaneShape
editMetadata -streamName "StreamOne" -memberName "Color" -value 2 -value 0.5 -value 1 -index 1 smcPlaneShape;
editMetadata -streamName "StreamOne" -memberName "ID" -value 17 -index 1 smcPlaneShape;
//Assign metadata to the Name and ID members of StreamTwo/NameStruct on smcPlaneShape
editMetadata -streamName "StreamTwo" -memberName "Name" -stringValue "cube1" -index 2 smcPlaneShape;
editMetadata -streamName "StreamTwo" -memberName "ID" -value 3 -index 3 smcPlaneShape;

//Assign metadata to the Color and ID members of StreamOne/ColorStruct on smcPlane1Shape
editMetadata -streamName "StreamOne" -memberName "Color" -value 127 -value 255 -value 212 -index 1 smcPlane1Shape;
editMetadata -streamName "StreamOne" -memberName "ID" -value 8 -index 1 smcPlane1Shape;
//Assign metadata to the Name and ID members of StreamTwo/NameStruct on smcPlane1Shape
editMetadata -streamName "StreamTwo" -memberName "Name" -stringValue "cube2" -index 2 smcPlane1Shape;
editMetadata -streamName "StreamTwo" -memberName "ID" -value 36 -index 3 smcPlane1Shape;
```

**注**

如果 polyShape 节点在其

inMesh

属性上具有传入连接，则将从该同一传入连接提供该形状的元数据。通常，这是由构建历史或变形引起的。但是，当元数据经过 DG 时不会对其进行修改，因此任何居间节点（如更改网格拓扑的删除顶点或硬边修改）都不会修改

元数据与网格组件的关联

，且元数据保持与它最初应用到的同一组件的关联，从而导致意外的结果（例如，元数据附加到不存在的顶点，或者因顶点索引改变而导致元数据在一个顶点上开始但在其他顶点上结束）。使用

editMetadata

命令将 editMetadata 节点插入到历史中，以手动修复任何错误的元数据关联。
