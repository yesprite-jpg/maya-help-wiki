# 绘制纹理变形器权重工具(Paint Texture Deformer Weights Tool)

- 在“动画”(Animation)、“建模”(Modeling)和“装备”(Rigging)菜单集中：“变形 > (绘制权重)纹理变形器”(Deform > (Paint Weights) Texture Deformer) > ![图：在“动画”(Animation)、“建模”(Modeling)和“装备”(Rigging)菜单集中：“变形 (绘制权重)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1889 字 ≥300，非承重" -->

通过“绘制纹理权重工具”(Paint Texture Weights Tool)，您可以使用 Maya Artisan 笔刷为变形的几何体绘制纹理权重。

请参见[纹理变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-9D157EC2-C938-493D-B183-38E819369486.htm)、[创建纹理变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-3B002998-EFC0-4C30-B19C-C96812BF4B92.htm)和[绘制纹理变形器权重](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-7D871459-35BA-4F17-A438-74C82F31954A.htm)。

## “绘制纹理权重工具”(Paint Texture Weights Tool)设置

可用于指定“工具设置”(Tool Settings)编辑器中“绘制纹理权重工具”(Paint Texture Weights Tool)的设置。在“绘制属性”(Paint Attributes)区域，“绘制纹理权重工具”(Paint Texture Weights Tool)拥有一些独有的属性。以下结合了一些常用属性及其对该工具的作用方式对这些独特属性进行了描述。有关所有其他区域中的所有其他属性的介绍，请参见 [Artisan 工具设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B8F095-4A0E-4BAE-938C-CB41B3EBD533)。

**注**

提示：

可以定义热键组合，以更在不打开“工具设置”(Tool Settings)编辑器的情况下更改多数设置。有关设定热键组合的详细信息，请参见手册的“Artisan”部分中的[使用 Artisan 热键](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D3E0C098-C385-43F0-A125-525847301EB6)。

### “绘制属性”(Paint Attributes)区域

这些是对“绘制属性”(Paint Attributes)区域内属性的描述。

#### texture*n*.weights jointTexture*n*.weights

显示选定要绘制的纹理的名称和正在绘制的属性（权重）。若要选择其他要绘制的纹理，请单击此按钮并选择相应的纹理权重名称。默认情况下，该工具选择其在曲面上检测到的第一个纹理（例如，texture1.weights 或 jointTexture3.weights）。

#### 过滤器: 纹理(Filter: texture)

设定一个过滤器，以便在其上方的按钮菜单上只显示纹理节点。由于您是使用“绘制纹理权重工具”(Paint Texture Weights Tool)来绘制纹理，所以无需更改该过滤器。

绘制操作(Paint Operation)

选择需对选定纹理进行的绘制操作。

#### 替换(Replace)

笔刷笔划可将顶点权重替换为设定的笔刷权重。

#### 相加(Add)

笔刷笔划可将顶点权重添加到设定的笔刷权重上。

#### 缩放(Scale)

笔刷笔划通过设定的笔刷权重因子缩放顶点权重。

#### 平滑(Smooth)

笔刷笔划可以均衡邻近顶点的权重，以便更加平稳地在权重间进行过渡。

#### 值(Value)

在进行任何一项操作式，设定要应用的权重值。

#### 最小值/最大值(Min/Max Value)

设置可能的最小和最大绘制值。默认情况下，可以绘制介于 0 和 1 之间的值。设定“最小值/最大值”(Min/Max Value)可以扩大或缩小值的范围。

负值用于减去权重。例如，如果将“最小值”(Min Value)设定为 -1，将“值”(Value)设定为 -0.5，然后选择“添加”(Add)进行操作，则绘制的顶点权重将减少 0.5。

正值用作倍数。

**注**

提示：

为了帮助您在绘制范围大于 0 到 1（例如，-5 到 5）时区分绘制值，并在绘制值范围为 0 到 1（例如，0.2 到 0.8）时最大程度地扩大显示的值范围，请设置“最小颜色”(Min Color)和“最大颜色”(Max Color)（在“显示”(Display)部分中）以符合“最小值/最大值”(Min/Max values)。

钳制(Clamp)

选择是否要钳制指定范围内的值，无论绘制时的“值”(Value)集为何。

#### 下限(Lower)

启用此选项可将下限值钳制在下面规定的“钳制值”。例如，如果钳制“下限”(Lower)，并将下限“钳制值”(Clamp Value)设定为 0.5，则即使将“值”(Value)设定为 0.25，绘制的值也绝不会小于 0.5。

#### 上限(Upper)

启用该选项可将上限值钳制到下面指定的“钳制值”(Clamp Value)。例如，如果钳制“上限”(Upper)，将上限“钳制值”(Clamp Value)设定为 0.75，然后将“明度值”(Value)设定为 1，那么绘制的值永远不会大于 0.75。

#### 钳制值(Clamp Values)

设置要钳制的“下限”(Lower)和“上限”(Upper)值。

#### 整体应用(Flood)

单击“整体应用”(Flood)，以便对选定纹理的所有权重采用笔刷设置。结果取决于进行整体应用时定义的笔刷设置。

#### 向量索引(Vector Index)

若正在绘制三通道属性（RGB 或 XYZ），则选择要绘制的通道。纹理权重是单通道属性，因此无需更改设置。
