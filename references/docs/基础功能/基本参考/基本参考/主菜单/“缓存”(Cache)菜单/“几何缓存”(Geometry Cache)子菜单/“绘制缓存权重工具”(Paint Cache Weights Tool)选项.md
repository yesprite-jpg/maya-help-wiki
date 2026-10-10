# “绘制缓存权重工具”(Paint Cache Weights Tool)选项

使用这些选项可设置在选择“缓存 > 几何缓存 > 绘制缓存权重工具”(Cache > Geometry Cache > Paint Cache Weights Tool)时发生的情况。另请参见[融合和设置几何缓存的权重](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-83339C2D-6BFF-4D13-A8A8-C844BDF72147)。

此工具的大多数选项（例如，“笔刷”(Brush)、“笔划”(Stroke)和“显示”(Display)）都是标准 Artisan 工具设置。有关这些选项的信息，请参见 [Artisan 工具设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B8F095-4A0E-4BAE-938C-CB41B3EBD533)。下面描述了特定于“绘制缓存权重工具”(Paint Cache Weights Tool)的设置。

## 缓存(Cache)

列出所有当前对象几何缓存的名称。从列表中选择其中一个几何缓存，并将其权重绘制在选定对象上。

## 绘制权重

### 绘制操作(Paint operation)

#### 替换(Replace)

笔刷笔划可将顶点权重替换为设定的笔刷权重。

#### 相加(Add)

笔刷笔划可将顶点权重添加到设定的笔刷权重上。

#### 缩放(Scale)

笔刷笔划通过设定的笔刷权重因子缩放顶点权重。

#### 平滑(Smooth)

笔刷笔划可以均衡邻近顶点的权重，以便更加平稳地在权重间进行过渡。

### 值

设定要在您执行任何绘制操作时应用的权重值。

设置可能的最小和最大绘制值。默认情况下，可以绘制介于 0 和 1 之间的值。设定“最小值/最大值”(Min/Max Value)可以扩大或缩小值的范围。

负值用于减去权重。例如，如果将“最小值”(Min Value)设定为 -1，将“值”(Value)设定为 -0.5，然后选择“添加”(Add)进行操作，则绘制的顶点权重将减少 0.5。

正值用于增加权重。

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

### 钳制

选择是否要将值钳制在指定范围中，而不考虑绘制时设定的“值”(Value)。

#### 下限(Lower)

启用此选项可将下限值钳制在下面规定的“钳制值”。例如，如果钳制“下限”(Lower)，并将下限“钳制值”(Clamp Value)设定为 0.5，则即使将“值”(Value)设定为 0.25，绘制的值也绝不会小于 0.5。

#### 上限(Upper)

启用此选项可将上限值钳制在下面规定的“钳制值”。例如，如果钳制“上限”(Upper)，并将上限“钳制值”(Clamp Value)设定为 0.75，将“值”(Value)设定为 1，则绘制的值绝不会大于 0.75。

#### 钳制值(Clamp Values)

设置要钳制的“下限”(Lower)和“上限”(Upper)值。

#### 整体应用(Flood)

单击“整体应用”(Flood)，以便将笔刷设置应用于选定对象上的所有权重。结果取决于进行整体应用时定义的笔刷设置。
