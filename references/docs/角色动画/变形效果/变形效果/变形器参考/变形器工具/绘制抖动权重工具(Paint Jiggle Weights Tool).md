# 绘制抖动权重工具(Paint Jiggle Weights Tool)

- 在“建模”(Modelling)和“装备”(Rigging)菜单集中：“变形 > (绘制权重)抖动”(Deform > (Paint Weights) Jiggle) > ![图：在“建模”(Modelling)和“装备”(Rigging)菜单集中：“变形 (绘制权重)抖动”(Deform (Pai…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1881 字 ≥300，非承重" -->

- 在“动画”(Animation)菜单集中：“动画变形 > 打开完整的变形菜单 > (绘制权重)抖动”(Anim Deform > Open Full Deform Menu > (Paint Weights) Jiggle) > ![图：在“动画”(Animation)菜单集中：“动画变形 打开完整的变形菜单 (绘制权重)抖动”(Anim Deform O…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1881 字 ≥300，非承重" -->

借助“绘制抖动权重工具”(Paint Jiggle Weights Tool)，可以在变形的几何体上使用 Maya Artisan 笔刷绘制抖动权重。

请参见[抖动变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-EE9CA51E-F618-4EE4-8D9F-6D6470EBF89E.htm)、[创建抖动变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-96A962ED-A8F8-4F1D-BC06-8AB9EF86DA2A.htm)和[绘制抖动变形器权重](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-7496A4C7-4B78-4098-874A-F458E64A9D3F.htm)。

## “绘制抖动权重工具”(Paint Jiggle Weights Tool)设置

可用于在“工具设置”(Tool Settings)编辑器中指定“绘制抖动权重工具”(Paint Jiggle Weights Tool)的设置。在“绘制属性”(Paint Attributes)区域中有一些“绘制抖动权重工具”(Paint Jiggle Weights Tool)独有的属性。下面介绍了这些独有属性以及一些常用属性，此外还介绍了如何将这些属性应用到该工具中。有关其他所有区域中其他所有属性的描述，请参见 [Artisan 工具设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B8F095-4A0E-4BAE-938C-CB41B3EBD533)和 [Artisan 笔刷工具的工作方式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D0A5ACD2-8D10-4B51-ADD3-E261F9337B07)。

### 绘制属性(Paint Attributes)

下面介绍了“绘制属性”(Paint Attributes)区域中的属性。

#### jiggle*n*.weights

显示要绘制的选定抖动节点的名称以及正在绘制（权重）的属性。若要选择其他要绘制的变形器，请单击该按钮，然后选择相应的抖动变形器权重名称。默认情况下，该工具将选择其在曲面上检测到的第一个抖动变形器（例如，jiggle2.weights）。

#### 过滤器: 抖动(Filter: jiggle)

设定过滤器，以便在该按钮之上的按钮对应的菜单上仅显示抖动变形器节点。因为正在使用“绘制抖动权重工具”(Paint Jiggle Weights Tool)绘制抖动权重，因此无需更改该过滤器。

绘制操作(Paint Operation)

选择要在选定抖动变形器上执行的绘制操作。

#### 替换(Replace)

笔刷笔划将使用为笔刷设定的权重替换绘制的权重。

#### 添加(Add)

笔刷笔划将绘制的权重添加到为笔刷设定的权重中。

#### 缩放(Scale)

笔刷笔划按照为笔刷设定的权重因子缩放绘制的权重。

#### 平滑(Smooth)

笔刷笔划可以均衡邻近顶点的权重，以便更加平稳地在权重间进行过渡。

#### 值(Value)

在进行任何一项操作式，设定要应用的权重值。

#### 最小值/最大值(Min/Max Value)

设置可能的最小和最大绘制值。默认情况下，可以绘制介于 0 和 1 之间的值。设定“最小值/最大值”(Min/Max Value)可以扩大或缩小值的范围。

负值用于减去权重。例如，如果将“最小值”(Min Value)设定为 -1，将“值”(Value)设定为 -0.5，然后选择“添加”(Add)进行操作，则绘制的顶点权重将减少 0.5。

正值用于增加权重。

**注**

提示：

为了帮助您在绘制范围大于 0 到 1（例如，-5 到 5）时区分绘制值，并在绘制值范围为 0 到 1（例如，0.2 到 0.8）时最大程度地扩大显示的值范围，请设置“最小颜色”(Min Color)和“最大颜色”(Max Color)（在“显示”(Display)部分中）以符合“最小值/最大值”(Min/Max values)。

钳制(Clamp)

选择是否要在指定的范围内钳制数值，而不考虑绘制时的“值”(Value)集。

#### 下限(Lower)

启用该选项之后可将下限值钳制在如下文指定的“钳制值”(Clamp Value)范围内。例如，如果钳制“下限”(Lower)并将“钳制值”(Clamp Value)下限设定为 0.5，则绘制的值永远不会小于 0.5，即使将“值”(Value)设定为 0.25 也仍然如此。

#### 上限(Upper)

启用此选项可将上限值钳制在下面规定的“钳制值”。例如，如果钳制“上限”(Upper)，并将上限“钳制值”(Clamp Value)设定为 0.75，将“值”(Value)设定为 1，则绘制的值绝不会大于 0.75。

#### 钳制值(Clamp Values)

设置要钳制的“下限”(Lower)和“上限”(Upper)值。

#### 整体应用(Flood)

单击“整体应用”(Flood)，将笔刷设置应用到选定抖动变形器的所有权重。结果取决于执行整体应用时定义的笔刷设置。

#### 向量索引(Vector Index)

如果正在绘制三个通道属性（RGB 或 XYZ）中，则请选择要绘制的通道。抖动变形器权重是单个通道的属性，因此不需要更改该设置。
