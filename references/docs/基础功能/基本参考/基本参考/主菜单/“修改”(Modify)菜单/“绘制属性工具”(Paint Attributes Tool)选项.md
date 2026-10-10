# “绘制属性工具”(Paint Attributes Tool)选项

使用这些选项可设置在选择“修改 > 绘制属性工具”(Modify > Paint Attributes Tool)时发生的情况。另请参见[绘制属性值](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EE522A09-CE1E-4F24-987F-89DB522A45DA)。

## 绘制属性(Paint Attributes)

下面描述了“工具设置”(Tool Settings)编辑器的“绘制属性”(Paint Attributes)区域中的设置。这些设置不仅应用于“绘制属性工具”(Paint Attributes Tool)，而且还应用于“绘制簇权重工具”(Paint Cluster Weights Tool)、“绘制抖动权重工具”(Paint Jiggle Weights Tool)和“绘制柔体权重工具”(Paint Soft Body Weights Tool)。

有关其他区域（例如，“笔刷”(Brush)、“笔划”(Stroke)和“显示”(Display)）中的设置的信息，请参见 [Artisan 工具设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B8F095-4A0E-4BAE-938C-CB41B3EBD533)。

### 可绘制属性的列表

如果曲面没有可绘制的节点或属性，则该按钮的名称为“未选择属性”(No attribute selected)。否则，该按钮的名称将为在曲面上检测到的节点和节点属性。单击该按钮，然后选择要绘制的节点和节点属性的名称。根据选定的过滤器，“绘制属性工具”(Paint Attributes Tool)会自动检测曲面（甚至您自己注册的曲面）上可绘制的节点和属性，并将它们列出以进行选择。

#### 过滤(Filter)器

单击该按钮，然后选择在单击“可绘制属性的列表”(List of Paintable Attributes)按钮时显示的可绘制节点。当选择过滤器时，该按钮的名称将更改以指示要过滤的属性。可以选择任意可绘制节点。例如，如果过滤器设定为全部，则会列出所有可绘制节点和属性。如果过滤器设定为簇，则只列出簇节点。

绘制操作(Paint Operation)

选择操作，以定义要对绘制的值的影响方式。

#### 替换(Replace)

将绘制的值替换为指定的“值”(Value)和“不透明度”(Opacity)。

#### 相加(Add)

将指定的“值”(Value)和“不透明度”(Opacity)添加到绘制的当前顶点值。如果“最小”(Min)或“最大”(Max) “值”(Value)为负值，则值实际上会减小。

#### 比例(Scale)

根据“值”(Value)和“不透明度”(Opacity)系数缩放您绘制的值。

#### 平滑(Smooth)

将值更改为周围值的平均值。

#### 值(Value)

设定执行任意绘制操作时要应用的值。

#### 最小值/最大值(Min/Max Value)

设置可能的最小和最大绘制值。默认情况下，可以绘制介于 0 和 1 之间的值。设置“最小值/最大值”(Min/Max Values)可以扩展或缩小值的范围。负值用于减去权重。例如，如果将“最小值”(Min Value)设定为 -1，将“值”(Value)设定为 -0.5，然后选择“添加”(Add)进行操作，则绘制的顶点权重将减少 0.5。正值用于增加权重。

**注**

提示：

为了帮助您在绘制范围大于 0 到 1（例如，-5 到 5）时区分绘制值，并在绘制值范围为 0 到 1（例如，0.2 到 0.8）时最大程度地扩大显示的值范围，请设置

“最小颜色”(Min Color)

和

“最大颜色”(Max Color)

（在

Artisan 工具设置

的

显示(Display)部分

中）以符合

“最小值/最大值”(Min/Max values)

。

钳制(Clamp)

选择是否要在指定范围内钳制值，而不管在绘制时设置的值如何。

#### 下限(Lower)

启用该选项可将下限值钳制为下面指定的“钳制值”(Clamp Values)。例如，如果钳制“下限”(Lower)并将下限“钳制值”(Clamp Values)设定为 0.5，则绘制的值从不会小于 0.5，即使将“值”(Value)设定为 0.25 也是如此。

#### 上限(Upper)

启用该选项可将上限值钳制为下面指定的“钳制值”(Clamp Values)。例如，如果钳制“上限”(Upper)，将上限“钳制值”(Clamp Values)设定为 0.75，并将“值”(Value)设定为 1，则绘制的值将从不会大于 0.75。

#### 钳制值(Clamp Values)

设置要钳制的“下限”(Lower)和“上限”(Upper)值。

#### 整体应用(Flood)

单击“整体应用”(Flood)可将笔刷设置应用于选定节点上的所有属性值。结果取决于笔刷、值、绘制操作和执行整体应用时定义的其他笔刷设置。

#### 向量索引(Vector Index)

如果要绘制三通道属性（RGB 或 XYZ），请选择要绘制的通道。如果要绘制单通道属性，则可使用任意设置。
