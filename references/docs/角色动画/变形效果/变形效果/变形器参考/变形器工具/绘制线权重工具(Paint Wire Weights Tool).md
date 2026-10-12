# 绘制线权重工具(Paint Wire Weights Tool)

- 在“建模”(Modelling)和“装备”(Rigging)菜单集中：“变形 > (绘制权重)线”(Deform > (Paint Weights) Wire) > ![图：在“建模”(Modelling)和“装备”(Rigging)菜单集中：“变形 (绘制权重)线”(Deform (Pain…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1692 字 ≥300，非承重" -->

- 在“动画”(Animation)菜单集中：“动画变形 > 打开完整的变形菜单 > (绘制权重)线”(Anim Deform > Open Full Deform Menu > (Paint Weights) Wire) > ![图：在“动画”(Animation)菜单集中：“动画变形 打开完整的变形菜单 (绘制权重)线”(Anim Deform Op…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1692 字 ≥300，非承重" -->

通过“绘制线权重工具”(Paint Wire Weights Tool)，可以使用 Artisan 笔刷在目标对象上应用、分布和移除线权重。请参见[绘制线变形器权重](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-DF0CCC32-C8BC-4C46-A0E3-4E349E738982.htm)。

## “绘制线权重工具”(Paint Wire Weights Tool)设置

有关通用于所有 Artisan 工具的“绘制线权重工具”(Paint Wire Weights Tool)选项的说明，请参见手册的“Artisan”部分中的 [Artisan 工具设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B8F095-4A0E-4BAE-938C-CB41B3EBD533)。

### 绘制属性(Paint Attributes)

#### 线变形器选择

#### wire *n* .weights

显示选择要绘制的曲面的线变形器节点的名称和正在绘制的属性（权重）。要选择要在该曲面上绘制的另一条线，请单击此按钮并选择适当的线权重名称。默认情况下，该工具将选择它在选定曲面上检测到的第一条线（例如，wire1.weights）。

#### 过滤器: 线(Filter: wire)

设置过滤器，以使线节点仅显示在此过滤器上方的按钮对应的菜单中。您正在使用“绘制线权重工具”(Paint Wire Weights Tool)绘制权重，因此不需要更改此过滤器。

绘制操作(Paint Operation)

绘制操作定义如何将线权重应用于目标形状。

#### 替换(Replace)

笔刷笔划会将目标权重替换为笔刷设置的线权重。

#### 添加(Add)

笔刷笔划会将目标权重添加到为笔刷设置的线权重。

#### 缩放(Scale)

笔刷笔划可按为笔刷设置的线权重因子缩放目标权重。

#### 平滑(Smooth)

笔刷笔划可对相邻顶点的权重求平均值，从而在线权重之间产生更平滑的过渡。

#### 值(Value)

设置要在执行任何绘制操作时应用的线权重值。

#### 最小值/最大值(Min/Max Value)

设置最小和最大可能的权重值。默认情况下，可以绘制 0 到 1 之间的权重值。通过设置“最小值/最大值”(Min/Max Value)可以扩大或缩小值范围。负值对于减去权重非常有用。例如，如果将“最小值”(Min Value)设置为 -1，将“值”(Value)设置为 -0.5，然后选择“添加”(Add)作为操作，则将从绘制的顶点权重中减去 0.5。正值用作倍数。

**注**

提示：

为了帮助您在绘制范围大于 0 到 1（例如，-5 到 5）时区分绘制值，并在绘制值范围为 0 到 1（例如，0.2 到 0.8）时最大程度地扩大显示的值范围，请设置“最小颜色”(Min Color)和“最大颜色”(Max Color)（在“显示”(Display)部分中）以符合“最小值/最大值”(Min/Max values)。

钳制(Clamp)

选择是否要在指定范围内钳制值，而不管在绘制时设置的值如何。

#### 上限(Upper)

启用此选项可将上限值钳制到下面指定的“钳制值”(Clamp Value)。例如，如果钳制“上限”(Upper)，请将上限“钳制值”(Clamp Value)设置为 0.75，并将“值”(Value)设置为 1，绘制的权重永远不会大于 0.75。

#### 下限(Lower)

启用此选项可将下限值钳制到下面指定的“钳制值”(Clamp Value)。例如，如果钳制“下限”(Lower)并将下限“钳制值”(Clamp Value)设置为 0.5，则绘制的权重永远不会小于 0.5，即使将“值”(Value)设置为 0.25 也是如此。

#### 钳制值(Clamp Values)

设置要钳制的“下限”(Lower)和“上限”(Upper)值。

#### 整体应用(Flood)

单击“整体应用”(Flood)可将笔刷设置应用于目标形状上的所有权重。结果取决于在执行整体应用时定义的笔刷设置。请参见手册的“Artisan”部分中的[整体应用绘制](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-66B72F2C-C159-4436-9CF7-ED3679C456D5)。

#### 向量索引(Vector index)

如果正在绘制三个通道属性（RGB 或 XYZ），请选择要绘制的通道。线变形器权重是单个通道属性，因此您不需要更改此设置。
