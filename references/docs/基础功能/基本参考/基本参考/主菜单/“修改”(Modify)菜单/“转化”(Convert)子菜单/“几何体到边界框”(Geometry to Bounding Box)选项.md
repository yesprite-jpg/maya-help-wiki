# “几何体到边界框”(Geometry to Bounding Box)选项

使用以下选项可设置在选择“修改 > 转化 > 几何体到边界框”(Modify > Convert > Geometry to Bounding Box)时发生的情况。另请参见[将边界框对象用作表示](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-433860C2-46C5-4848-B704-AC5C86295747)。

#### 名称(Name)

指定新边界框对象的名称。如果未指定名称，则边界框对象将继承原始对象的名称。

#### 名称后缀(Name suffix)

指定附加到新边界框对象的名称。默认情况下，会将 _BBox 后缀添加到边界框名称中。

### 表示层次为(Represent hierarchy as)

#### 一个边界框(One bounding box)

创建表示层次中所有对象的边界框单个实例。

#### 每个形状一个边界框(One bounding box per shape)

在分组对象层次中为每个对象创建边界框。

#### 组合生成的边界框(Combine resulting bounding boxes)

如果已启用“每个形状一个边界框”(One bounding box per shape)，则选择此选项可自动将“网格 > 结合”(Mesh > Combine)应用于生成的边界框。

#### 颜色(Color)

单击“颜色”(Color)样例或使用滑块控件可指定边界框的着色颜色。

### 烘焙动画(Bake Animation)

将原始几何体的动画烘焙到生成的边界框中。当使用“烘焙动画”(Bake Animation)时，对生成的边界框变换和比例值进行插值，以保持原始几何体的外部边界。

**注**

使用

“烘焙动画”(Bake Animation)

时，不能启用

“组合生成的边界框”(Combine resulting bounding boxes)

。

#### 时间范围(Time range)

指定烘焙到边界框的动画的时间范围。

#### 时间滑块(Time Slider)

指定时间滑块范围确定烘焙到边界框的动画的持续时间。

#### 开始/结束(Start/End)

指定指定的“开始时间”(Start Time)和“结束时间”(End Time)之间（包括开始时间和结束时间）的帧范围确定烘焙到边界框的动画的持续时间。

#### 开始时间/结束时间(Start time/End time)

这些字段允许您指定烘焙到边界框的动画的开始和结束时间。

#### 采样频率(Sample by)

将动画烘焙到边界框时，您可以设置“采样频率”(Sample by)以指定 Maya 对边界框动画的求值频率。例如，值为 2 会指定每隔一个帧对动画求值一次。

#### 保持原始(Keep Original)

启用后，在转化为边界框后原始对象或层次将保留在场景中。禁用后，原始对象或层次将被删除，场景中仅保留转化的边界框。
