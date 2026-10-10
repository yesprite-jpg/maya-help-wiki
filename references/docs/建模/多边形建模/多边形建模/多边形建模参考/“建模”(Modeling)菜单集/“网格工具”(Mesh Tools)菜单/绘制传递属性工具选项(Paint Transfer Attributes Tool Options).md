# 绘制传递属性工具选项(Paint Transfer Attributes Tool Options)

使用这些选项可设置在选择“网格工具 > 绘制传递属性工具”(Mesh Tools > Paint Transfer Attributes Tool)时发生的情况。在“绘制属性”(Paint Attributes)区域中，有一些特定于“绘制传递属性权重工具”(Paint Transfer Attribute Weights Tool)的属性。以下描述了这些特有属性和一些公用属性以及如何将它们应用到该工具。有关所有其他区域中的所有其他属性的介绍，请参见 [Artisan 工具设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B8F095-4A0E-4BAE-938C-CB41B3EBD533)。

**注**

变形器权重功能仅适用于位置属性传递。所有其他属性将始终以权重值 1 进行传递。

**注**

提示：

您可以定义热键组合以更改大部分设置，而无需打开“工具设置编辑器”(Tool Settings Editor)。有关设置热键组合的详细信息，请参见[使用 Artisan 热键](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D3E0C098-C385-43F0-A125-525847301EB6)。

## 绘制属性(Paint Attributes)

#### transferAttributesn.weights

指定正在绘制的属性的名称。绘制“传递属性权重”(Transfer Attribute Weights)时，该属性为 <nodename>.weights。使用该下拉列表选择要绘制的其他属性（例如，其他传递属性节点的传递权重）。

#### 过滤器: TransferAttributes(Filter: TransferAttributes)

设置一个过滤器，以便只有传递属性节点显示在上方按钮的菜单中。由于您正在使用该工具绘制“传递属性权重”(Transfer Attribute Weights)，因此无需更改此过滤器。

#### 绘制操作(Paint Operation)

选择需对选定簇进行的绘制操作。

#### 替换(Replace)

将顶点权重替换为对笔刷设定的权重。

#### 添加(Add)

将顶点权重添加到为笔刷设定的权重。

#### 缩放(Scale)

按为笔刷设定的权重因子缩放顶点权重。

#### 平滑(Smooth)

平均相邻顶点的权重以在两个权重之间生成较平滑的过渡。

#### 值(Value)

设定要在您执行任何绘制操作时应用的权重值。

值 0（黑色）表示应使用原始（未变形）的网格值，而值 1（白色）表示应使用从源网格传递的值。融合之间的任何值都在这两个值之间。

#### 最小值/最大值(Min/Max Value)

设置可能的最小和最大绘制值。默认情况下，可以绘制介于 0 和 1 之间的值。通过设置“最小值/最大值”(Min/Max Values)，您可以扩大或缩小值范围。

负值用于减去权重。例如，如果将最小值设定为 -1，将值设定为 -0.5，并选择“添加”作为操作，则将从所绘制顶点的权重中减去 0.5。

正值用作倍增。

**注**

提示：

为了帮助您在大于 0 到 1 的范围（例如，-5 到 5）内绘制时区分绘制值，以及在 0 到 1 的范围（例如，0.2 到 0.8）内绘制值时最大化所显示值的范围，请设定“最小颜色”和“最大颜色”（位于“显示”区域中）以便与“最小值/最大值”相一致。

#### 钳制(Clamp)

选择是否要将值钳制在指定范围中，而不考虑绘制时设定的“值”(Value)。

#### 下限(Lower)

启用该选项以将下限值钳制到以下指定的“钳制值”(Clamp Value)。例如，如果钳制“下限”并将下限“钳制值”(Clamp Value)设定为 0.5，则您绘制的值永远也不会小于 0.5，即使将“值”设定为 0.25 也是如此。

#### 上限(Upper)

启用该选项以将上限值钳制到以下指定的“钳制值”(Clamp Value)。例如，如果钳制“上限”并将上限“钳制值”(Clamp Value)设定为 0.75，将“值”设定为 1，则您绘制的值永远也不会大于 0.75。

#### 钳制值(Clamp Values)

设置要钳制的“下限”(Lower)和“上限”(Upper)值。

#### 整体应用(Flood)

单击“整体应用”(Flood)，以便对选定簇的所有权重采用笔刷设置。结果取决于进行整体应用时定义的笔刷设置。

#### 向量索引(Vector Index)

如果您绘制的是三通道属性（RGB 或 XYZ），请选择要绘制的通道。属性权重是单个通道属性，因此无需更改该设置。
