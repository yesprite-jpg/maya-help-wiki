# 绘制 Delta Mush 权重工具(Paint Delta Mush Weights Tool)

- 在“建模”(Modelling)和“装备”(Rigging)菜单集中：“变形 > (绘制权重) [Delta Mush](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-5FAB8DEA-F82E-4519-8062-D4E91CA6E296.htm)”(Deform > (Paint Weights) Delta Mush) > ![图：在“建模”(Modelling)和“装备”(Rigging)菜单集中：“变形 (绘制权重) Delta Mush”(De…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1650 字 ≥300，非承重" -->

- 在“动画”(Animation)菜单集中：“动画变形 > 打开完整的变形菜单 > (绘制权重) [Delta Mush](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-5FAB8DEA-F82E-4519-8062-D4E91CA6E296.htm)”(Anim Deform > Open Full Deform Menu > (Paint Weights) Delta Mush) > ![图：在“动画”(Animation)菜单集中：“动画变形 打开完整的变形菜单 (绘制权重) Delta Mush”(Anim…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1650 字 ≥300，非承重" -->

通过绘制 Delta Mush 权重工具，可以使用笔刷绘制变形的几何体上的 Delta Mush 权重。

**注**

提示：

可以定义热键组合，以更在不打开“工具设置”(Tool Settings)编辑器的情况下更改多数设置。有关设置热键组合的详细信息，请参见[使用 Artisan 热键](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D3E0C098-C385-43F0-A125-525847301EB6)。

## 绘制属性工具

### Delta Mush 选择

#### deltaMush *n* .weights

显示选择要绘制的曲面的变形器节点的名称和正在绘制的属性（权重）。若要选择其他要绘制的变形器，请单击此按钮，然后选择相应的 Delta Mush 权重名称。

#### 过滤器: deltaMush(Filter: deltaMush)

设置过滤器，以使 Delta Mush 节点仅显示在此过滤器上方的按钮对应的菜单中。您正在使用“绘制 Delta Mush 权重工具”(Paint Delta Mush Weights Tool)绘制权重，因此不需要更改此过滤器。

#### 绘制操作(Paint Operation)

绘制操作定义如何将权重应用于目标形状。

#### 替换(Replace)

笔刷笔划会将目标权重替换为笔刷设置的权重。

#### 添加(Add)

笔刷笔划会将目标权重添加到为笔刷设置的权重。

#### 缩放(Scale)

笔刷笔划可按为笔刷设置的权重因子缩放目标权重。

#### 平滑(Smooth)

笔刷笔划可以均衡邻近顶点的权重，以便更加平稳地在权重间进行过渡。

#### 值(Value)

设置要在执行任何绘制操作时应用的权重值。

#### 最小值/最大值(Min/Max Value)

设置最小和最大可能的权重值。默认情况下，可以绘制 0 到 1 之间的权重值。通过设置“最小值/最大值”(Min/Max Value)可以扩大或缩小值范围。负值对于减去权重非常有用。例如，如果将“最小值”(Min Value)设置为 -1，将“值”(Value)设置为 -0.5，然后选择“添加”(Add)作为操作，则将从绘制的顶点权重中减去 0.5。正值用作倍数。

**注**

提示：

为了帮助您在绘制范围大于 0 到 1（例如，-5 到 5）时区分绘制值，并在绘制值范围为 0 到 1（例如，0.2 到 0.8）时最大程度地扩大显示的值范围，请设置

“最小颜色”(Min Color)

和

“最大颜色”(Max Color)

（在

“显示”(Display)

部分中）以符合

“最小值/最大值”(Min/Max values)

。

#### 钳制(Clamp)

选择是否要将值钳制在指定范围中，而不考虑绘制时设定的“值”(Value)。

#### 下限(Lower)

启用此选项可将下限值钳制到下面指定的“钳制值”(Clamp Value)。例如，如果钳制“下限”(Lower)并将下限“钳制值”(Clamp Value)设置为 0.5，则绘制的权重永远不会小于 0.5，即使将“值”(Value)设置为 0.25 也是如此。

#### 上限(Upper)

启用此选项可将上限值钳制到下面指定的“钳制值”(Clamp Value)。例如，如果钳制“上限”(Upper)，请将上限“钳制值”(Clamp Value)设置为 0.75，并将“值”(Value)设置为 1，绘制的权重永远不会大于 0.75。

#### 钳制值(Clamp Values)

设置要钳制的“下限”(Lower)和“上限”(Upper)值。

#### 整体应用(Flood)

单击“整体应用”(Flood)可将笔刷设置应用于目标形状上的所有权重。结果取决于在执行整体应用时定义的笔刷设置。请参见[整体应用绘制](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-66B72F2C-C159-4436-9CF7-ED3679C456D5)。

#### 向量索引(Vector index)

如果正在绘制三个通道属性（RGB 或 XYZ），请选择要绘制的通道。

**注**

Delta Mush 变形器权重是单通道属性，因此您不需要更改

“向量索引”(Vector Index)

设置。
