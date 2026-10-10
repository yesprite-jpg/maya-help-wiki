# 将元数据添加到 Maya 节点

可以使用 Maya 元数据 API 创建任意多的元数据结构，这些结构可以直接附加到 Maya 网格对象的任何 Maya 节点以及组件（顶点、面、边和顶点面）。也可以将元数据整体添加到 Maya 场景中，也就是说无需将其附加到任何特定节点。通过为数不多的一组 MEL 命令，可以从 Maya 内访问元数据。

使用元数据类，可以为组件级别的元数据创建数据结构，并将其合并为单个数据流，该数据流允许元数据流经 Maya DG 中的操作，同时使元数据保持附加到节点。这包括向具有构建历史的网格节点添加组件级别元数据。由于元数据可以通过任意指定关联附加到任意节点，因此可以扩展 API 用途（如将元数据附加到点云中的点、模拟中的粒子或 NURBS 曲面上的顶点）。元数据稍后可通过 MEL 命令或 API 进行检查或修改，并在不同会话之间保存在 Maya 文件中。adsk::Data::Association 类引用中的示例显示了如何将顶点速度和加速数据存储在模拟网格上。请参见 Maya 开发人员帮助。

在构建历史中，元数据索引值不会发生变化。如果网格拓扑改变，则网格组件元数据可能不再与原始组件关联。editMetadata 命令可以帮助将调整插入构建历史，进而修复由此引发的任何问题。

**注**

不应将元数据添加到变形网格。

通常，更改 polyShape 的 inMesh 属性（即，polyShape 节点的输入属性）的拓扑的任何操作（例如，硬边修改）不会以相同方式修改传入的元数据，并且可能会导致意外的结果。

## 元数据 API 类

元数据 API 包括以下最常用的类：adsk::Data::Association、 adsk::Data::Channel、adsk::Data::Stream、adsk::Data::Structure 和 adsk::Data::Handle。

- adsk::Data::Association 类用于为每个组件的数据创建数据结构。 例如，可以定义要附加到网格对象曲面上的每个顶点的数据。

- adsk::Data::Channel 类用于将数据流合并到单个数据块。

- adsk::Data::Stream 类用于管理数据的索引列表，而且已针对典型操作（如从列表中间删除条目以及复制条目）进行优化。

- adsk::Data::Structure 类用于定义和管理元数据的数据结构。

- adsk::Data::Handle 类提供用于访问 adsk::Data::Stream 中的元数据值的接口。

“关联”(Association)、“通道”(Channel)、“流”(Stream)和“结构”(Structure)各自具有等效的 XXIterator 类，有助于遍历类的所有成员。

## 元数据 MEL 命令

从 Maya 中，可以使用以下 MEL 命令访问和操纵从元数据 API 创建的数据结构。有关完整的命令参考，请参见技术文档中的“MEL 命令”部分。

- 使用 [dataStructure](http://www.autodesk.com/maya-help-2018-chs/index.html?contextId=COMMANDS-dataStructure) 创建未附加的元数据结构。

- 使用 [addMetadata](http://www.autodesk.com/maya-help-2018-chs/index.html?contextId=COMMANDS-addMetadata) 将结构的成员应用于 Maya 中的组件。

- 使用 [editMetadata](http://www.autodesk.com/maya-help-2018-chs/index.html?contextId=COMMANDS-editMetadata) 将值指定给选定组件的元数据流的成员。

  此命令可用于具有构建历史的节点。对于具有构建历史的网格节点，将创建 editMetadata 节点以包含对现有元数据所做的修改，而不是直接将修改应用到网格节点。

  您仍然可以选择编辑历史节点上的元数据。执行此操作时，所做编辑将直接应用于网格节点，而不会创建 editMetadata 节点。

- 使用 [hasMetadata](http://www.autodesk.com/maya-help-2018-chs/index.html?contextId=COMMANDS-hasMetadata) 查询节点上是否存在元数据。

- 使用 [getMetadata](http://www.autodesk.com/maya-help-2018-chs/index.html?contextId=COMMANDS-getMetadata) 查询元数据值。

如果要使用其他索引类型，可通过 Maya API 借助插件来实现。元数据命令可以在显示本地索引类型的任意位置使用这些其他索引类型。
