# 在 Maya 中编辑元数据

若要将元数据添加到对象，必须先定义数据结构，创建数据流并将它们附加到对象。执行此操作后，可以将其他元数据添加到同一流和成员，或者通过 Maya 标记菜单编辑现有的元数据。或者，也可以通过 MEL/Python 脚本执行此操作。

有关如何使用 MEL/Python 定义数据结构以及创建和附加数据流的信息，请参见[使用 MEL 脚本将元数据添加到网格](../使用%20MEL%20脚本将元数据添加到网格.md)。

使用标记菜单添加或编辑元数据

1. 右键单击对象，然后选择“元数据 > 选择流”(Metadata > Select Stream)，以选择要为其添加或编辑元数据的流和成员。

  在选择流和成员时会启用元数据可视化。

2. 在视口中，选择要向其添加元数据的对象上的组件，或者选择具有要编辑的元数据的对象上的组件。

  只能将元数据添加到附加到所选对象和组件的流和成员。例如，如果已先将 StreamOne 附加到 smcPlaneShape 的顶点通道，则只能将元数据添加到 smcPlaneShape 的顶点上的 StreamOne。

  ```text
dataStructure -format "raw" -asString "name=ColorStruct:float[3]=Color";
addMetadata -streamName "StreamOne" -channelName "vertex" -structure "ColorStruct" smcPlaneShape;
```

3. 右键单击对象，然后选择“元数据 > 编辑元数据”(Metadata > Edit Metadata)。

  此时将显示“编辑元数据”(Edit Metadata)窗口。验证“当前流”(Current Stream)以确保这是要为其添加或编辑元数据的流。

  **注**

  如果选择没有为其附加元数据流的对象上的组件，则显示错误。

4. 输入元数据值。

  Viewport 2.0 现在反映已添加/编辑的元数据值。

## 相关主题

- [在 Viewport 2.0 中可视化元数据](在%20Viewport%202.0%20中可视化元数据.md)

- [使用脚本可视化元数据](使用脚本可视化元数据.md)

- [在可视化元数据时重新映射颜色范围](在元数据可视化期间重映射颜色范围.md)

- [在可视化元数据时将顶点颜色外推到面](在元数据可视化期间将颜色从顶点外推到面.md)

- [元数据可视化选项](../元数据可视化选项.md)
