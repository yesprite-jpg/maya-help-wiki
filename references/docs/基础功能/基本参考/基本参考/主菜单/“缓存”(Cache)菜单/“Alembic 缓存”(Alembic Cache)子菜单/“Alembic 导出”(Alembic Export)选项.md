# “Alembic 导出”(Alembic Export)选项

使用这些选项可控制在选择“缓存 > Alembic 缓存 > 全部导出到 Alembic”(Cache > Alembic Cache > Export All to Alembic)或“缓存 > Alembic 缓存 > 将当前选择导出到 Alembic”(Cache > Alembic Cache > Export Selection to Alembic)创建 Alembic 缓存文件时发生的情况。另请参见[创建 Alembic 缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6C9504CD-9107-4DA2-B618-CAA9045906D4)。

## 常规选项(General Options)

#### 缓存时间范围(Cache time range)

从下列选项中选择：

#### 当前帧(Current frame)

仅缓存当前的“时间滑块”(Time Slider)帧。

#### 当前帧(Current frame)

仅缓存当前的“时间滑块”(Time Slider)帧。

#### 渲染设置(Render settings)

指定当前“渲染设置”(Render settings)确定“缓存时间范围”(Cache time range)。

#### 时间滑块(Time Slider)

指定“时间滑块”(Time Slider)中的当前播放范围确定“缓存时间范围”(Cache time range)。

#### 开始/结束(Start/End)

指定在指定的“开始”(Start)和“结束”(End)时间之间（包括“开始”(Start)和“结束”(End)时间）的帧范围确定“缓存时间范围”(Cache time range)。

#### 步长(Step)

指定文件创建过程中的采样频率。默认情况下，对象变形的采样将每帧进行一次，并保存到 Alembic 文件。

例如，如果值为 2，表示对于“缓存时间范围”(Cache Time Rang)每隔一帧缓存当前对象的变换。

#### 帧相对采样(Frame relative sample)

启用时，您可以指定每帧的采样数。您可以使用此选项将可由渲染应用程序解释的帧子采样数据设定为快门打开和关闭值，以实现运动模糊。

#### 低/高(Low/High)

为帧指定相对于采样的低值和高值。

#### 预侧滚开始帧(Pre Roll Start Frame)

指定从哪一帧开始场景求值。使用此选项可以为需要预备运行到开始帧的依赖于时间的平移设定起始帧。

## 缓存时间范围(Cache Time Ranges)

使用“缓存时间范围”(Cache Time Ranges)选项可在同一 Alembic 文件中指定多个时间范围和采样率。例如在缓存文件中，您可以指定在动画的每个第四帧采样一次的时间范围，然后指定在每个帧采样一次的另一时间范围。您可以使用“缓存时间范围”(Cache Time Ranges)创建文件，以较低采样率保存慢运动序列，同时为全操作序列保持高采样率。

#### 缓存时间(Cache Time)

输入缓存时间范围的第一个和最后一个帧。您还可以使用“开始/结束”(Start/End)控件来设置时间范围。

单击“添加范围+”(Add Range+)，创建多个时间范围。

#### 预卷(Pre-Roll)

指示“预卷”(Pre-Roll)范围已设置。

#### 子采样数(Subsamples)

显示范围的“帧相对采样”(Frame Relative sample)设置。

## 属性(Attributes)

通过该选项可以添加动力学和自定义属性数据以导出 Alembic 文件。若要添加属性，请执行下列操作之一：

- 在“属性”(Attribute)字段中键入属性的名称，然后单击“添加”(Add)。

- 在“通道盒”(Channel Box)中选择属性，然后单击“来自通道盒”(From Channel Box)。

添加的属性会显示在“属性”(Attribute)下的表中。

## 属性前缀(Attribute Prefix)

指定前缀以过滤出要写入到 Alembic 文件中的属性名称。在“属性前缀”(Attribute Prefix)字段中键入一个值，然后单击“添加”(Add)。属性名称中包含指定前缀的所有属性均将被添加到 Alembic 文件中。

## 高级选项(Advanced Options)

#### 详细(Verbose)

将帧编号信息输出到“脚本编辑器”(Script Editor)或输出窗口。

#### 无法线(No Normals)

启用该选项以从 Alembic 缓存文件中排除源对象的法线数据。

#### 仅可渲染(Renderable Only)

启用该选项以从 Alembic 文件中排除任何不可渲染的节点或层次，如隐藏的对象。

#### 去除名称空间(Strip Namespaces)

启用该选项以移除与导出的对象关联的名称空间，然后再将其保存到 Alembic 文件。例如，名称空间为 taco:foo:bar 的对象在 Alembic 文件中显示为 bar。

#### UV 写入(UV Write)

启用该选项以将 UV 数据从多边形网格和细分对象写入到 Alembic 文件中。仅包含当前的 UV 贴图。

#### 写入颜色集(Write Color Sets)

您可以将源多边形网格中的颜色逐顶点数据写入到 Alembic 文件中。您可以在渲染时使用此数据从网格中导出运动模糊效果的运动向量数据。

启用“写入颜色集”(Write Color Sets)，然后将“运动向量颜色集”(Motion Vector Color Set)添加到已导出的属性列表。若要执行此操作，请在“属性”(Attributes)区域中，于“属性”(Attributes)旁键入 motionVectorColorSet，然后单击“添加”(Add)。

#### 写入面集(Write Face Sets)

启用此选项可将逐面着色组指定保存到 Alembic 缓存中。Maya 仅会将着色组名称保存到文件中， 不会将任何材质信息写入缓存。

当您加载 Alembic 文件时，如果着色组已存在于场景中，则 Maya 会为面重新指定着色。 Maya 不会创建新材质或着色组。

#### 整帧几何体(Whole Frame Geo)

启用该选项后，将在整帧对几何数据采样并将其写入到文件中。禁用该选项（默认设置）后，将在子帧对几何数据采样并将其写入到文件中。

#### 世界空间(World Space)

启用该选项以将节点层次中的顶部节点存储为世界空间。默认情况下，这些节点存储为局部空间。

#### 写入可见性(Write Visibility)

启用该选项以将对象的可见性状态存储在 Alembic 文件中。否则，所有对象都视为可见。

#### 过滤器 Euler 旋转(Filter Euler Rotations)

启用该选项以使用 Euler 过滤器过滤 X、Y 和 Z 旋转数据。Euler 过滤有助于解决旋转中的违规情况，尤其是 X、Y 和 Z 旋转超过 360 度时。

#### 写入折痕(Write Creases)

启用该选项以将几何体的边和顶点的折痕信息导出到 Alembic 文件中。

**注**

有关使用 Maya 2015、Maya 2014 和 Maya 2013 时将折痕信息导出到 Alembic 文件的信息，请参见

将折痕导出到 Alembic 文件

。

#### 文件格式(File Format)

#### HDF5 - Maya 2014 Extension 1 和旧版(HDF5 - Maya 2014 Extension 1 and Legacy)

创建与 HDF5 数据模型保持一致的 Alembic 缓存文件。此选项提供与先前版本 Alembic 的向后兼容性。

#### Ogawa - Maya 2014 Extension 1

创建 Ogawa Alembic 文件。相对旧版 Alembic 文件而言，采用 Ogawa 格式创建的文件大小更小、性能更优。

**注**

只有 Extension for Maya 2014 和更高版本的 Maya 才能读取 Ogawa Alembic 文件。

## 回调(Callbacks)

结合使用回调与 Alembic 导出的推荐方法是首先定义一个全局过程。例如，在“脚本编辑器”(Script Editor)中，定义以下内容：

```text
global proc perFrameCallback(int $frame)
{
    print $frame;
}
```

完整的 MEL 回调为：

perFrameCallback(#FRAME#)

#### 逐帧回调 MEL (Per Frame Callback MEL)

对每个帧求值时，将以 Mel 命令对指定的字符串求值。例如，print ("#FRAME#")。

#### 作业后回调 MEL (Post Job Callback MEL)

平移完成后，将以 MEL 命令对指定的字符串求值。例如，print ("Done!")。

#### 逐帧回调 Python (Per Frame Callback Python)

对每个帧求值时，将以 Python 命令对指定的字符串求值。例如，print ("#FRAME#")。

#### 作业后回调 Python (Post Job Callback Python)

平移完成后，将以 Python 命令对指定的字符串求值。例如，print ("Done!")。

## 相关主题

- [“Alembic 导入”(Alembic Import)选项](“Alembic%20导入”%28Alembic%20Import%29选项.md)

- [导入 Alembic 缓存文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3C1D1B0C-5D75-41DF-8480-CD7A42CCBCBE)

- [Alembic 缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9D272E39-9279-4146-8449-928DDA865C9D)
