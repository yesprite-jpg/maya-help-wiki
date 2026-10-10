# 类型和 SVG 挤出（typeExtrude 和 svgExtrude）

分别处理[类型(Type)](../多边形建模工具/“类型工具”%28Type%20Tool%29选项.md)或 [SVG](../多边形建模工具/“SVG%20工具”%28SVG%20Tool%29选项.md) 网格的挤出。

#### 模式(Mode)

确定挤出方向。选项包括：

- 法线(Normals)：几何体沿其法线挤出。

- 距离场(Distance Field)：在尝试避免碰撞时使用预计算的距离场挤出。

## 距离场(Distance Field)

#### 栅格大小(Grid Size)

确定在“模式”(Mode)设置为“距离场”(Distance Field)时用于避免碰撞的预计算场的大小。

## 挤出(Extrude)

#### 挤出曲线(Extrusion Curve)

此图控制挤出的形状。最左侧的点始终表示原始类型在挤出之前的位置，而其右侧的所有点则表示相对于该点的位置。通过分别单击图表上方的左键和右键，您可以在曲线自己的窗口中将其打开或将其返回到自己的默认形状。

#### 启用挤出(Enable Extrusion)

启用时，字母向前挤出以增加深度，否则保持为平面。默认设置为启用。

#### 捕捉到栅格(Snap to Grid)

启用时，“挤出剖面曲线”(Extrusion Profile Curve)中的控制点捕捉到经过的图形点。默认设置为禁用。

#### 自定义剖面(Custom Profiles)

最多允许保存 12 个自定义“挤出剖面曲线”(Extrusion Profile Curve)形状。您可以通过单击“自定义剖面”(Custom Profiles)属性名称旁边的保存按钮来保存形状。如果已经保存了 12 个剖面，则单击该按钮时将保存最旧的剖面。

#### 分数偏移(Fractional Offset)

启用时，将“挤出偏移”(Extrude Offset)属性转化为网格中最短边的百分比。将“挤出距离”(Extrude Distance)设置为介于 0 和 1 之间的值时，这将确保不会创建由内到外的倒角。默认值为启用。

#### 挤出距离(Extrude Distance)

控制挤出多边形的距离。默认值为 2.5。

#### 挤出偏移(Extrude Offset)

设置网格挤出偏移。当“分数偏移”(Fractional Offset)处于禁用状态时，此偏移以场景单位表示。当“分数偏移”(Fractional Offset)处于启用状态时，此偏移用网格中最短边的百分比表示。默认值为 0.5。

#### 挤出分段(Extrude Divisions)

控制沿挤出面的细分数。默认值为 4。

## 倒角(Bevels)

#### 倒角样式(Bevel Style)

确定要应用的倒角类型。

- “外部倒角”(Outer Bevel)将倒角挤出应用于侧面。

- “内部倒角”(Inner Bevel)将倒角挤出应用于正面和背面。

通过选择分别显示“属性编辑器”(Attribute Editor)中的其他“外部倒角”(Outer Bevel)或“前倒角”(Front Bevel)和“后倒角”(Back Bevel)部分。这些部分包含与“挤出”(Extrusion)部分中用于控制其他倒角挤出的属性相同的属性。

**注**

“挤出”(Extrusion)

和

“倒角”(Bevel)

部分中的

“分数偏移”(Fractional Offset)

均表示同一属性。

#### 匹配前倒角(Match Front Bevel)

仅在“后倒角”(Back Bevel)部分中可用。启用时，此选项将“前倒角”(Front Bevel)设置映射到“后倒角”(Back Bevel)。
