# 在 Viewport 2.0 中可视化元数据

在对象标记菜单中选择“元数据 > 可视化元数据”(Metadata > Visualize Metadata)时，可以对所有对象启用元数据可视化。一次只能查看一个流和一个成员。

也可以使用脚本可视化元数据。请参见[使用脚本可视化元数据](使用脚本可视化元数据.md)。

## 使用“显示”(Display)菜单可视化元数据

可视化场景中的元数据

1. 请执行下列任一操作：

  - 右键单击对象，然后启用“元数据 > 可视化元数据”(Metadata > Visualize Metadata)。

  - 在主菜单栏中启用“显示 > 多边形 > 元数据 > 可视化元数据”(Display > Polygons > Metadata > Visualize Metadata)。

  将基于在[元数据可视化选项](../元数据可视化选项.md)中选择的选项显示元数据。

设置元数据可视化选项

1. 选择“显示 > 多边形 > 元数据 > 可视化元数据”(Display > Polygons > Metadata > Visualize Metadata) > ![图：选择“显示 多边形 元数据 可视化元数据”(Display Polygons Metadata Visualize Me…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1391 字 ≥300，非承重" --> 以打开“元数据可视化选项”(Metadata Visualization Options)。

  属于您场景的所有元数据流将显示在“要可视化的流”(Stream to visualize)下拉列表中。

2. 选择要可视化的流，在“成员”(Member)下拉列表中将显示其可用成员。

3. 选择要可视化的成员以及要按其可视化元数据的方法：“颜色”(Color)、“字符串”(String)、“光线”(Ray)。请参见[元数据可视化选项](../元数据可视化选项.md)。

  **注**

  提示：

  也可以从对象的标记菜单中选择要可视化的元数据流和成员：

  “元数据 > 选择流”(Metadata > Select Stream)

  。在菜单中将显示属于对象的所有元数据流。选择要可视化的流，然后选择成员。

禁用元数据可视化

1. 请执行下列任一操作：

  - 在主菜单栏中禁用“显示 > 多边形 > 元数据 > 可视化元数据”(Display > Polygons > Metadata > Visualize Metadata)。

  - 在对象标记菜单中禁用“元数据 > 可视化元数据”(Metadata > Visualize Metadata)。

## 可视化元数据的已知限制

- 在通道的任何成员上设置值时，在同一通道的其他成员上也为已指定值的组件提供默认值。

  例如，在此例中，数据结构具有两个成员：颜色和状态。

  在面通道的状态成员上为面 2:4 设置值时，将为该面通道的颜色成员上的面 2:4 自动指定默认值。可视化 stream1 的颜色成员时，将显示默认值。

  由于自动指定的默认值和有意设置的元数据值被添加到不同的成员，因此它们从不同时显示。

  ```text
dataStructure -format "raw" -asString "name=struct1:float[3]=color:bool=status";
addMetadata -streamName "stream1" -channelName "face" -structure "struct1" smcPlaneShape;
select -r smcPlane.f[2:4];
editMetadata -streamName "stream1" -memberName "status" - value 1
```

- 可视化长度为 3 或更小值的数组时，Maya 仅支持显示最多 3 位小数。其他小数位或超过 6 个可显示数字的值可能是近似的。超过 10 位的数值显示可能会返回 INF。

  可视化长度为 4 或更大值的数组或者可视化多字节字符时，Maya 可能无法同时显示大量的唯一值。

- [元数据可视化选项](../元数据可视化选项.md)

- [使用 MEL 脚本将元数据添加到网格](../使用%20MEL%20脚本将元数据添加到网格.md)
