# 几何缓存 XML 描述文件

创建几何缓存时，您的缓存以 .mcx 或 .mcc（Maya 缓存）文件保存到磁盘。同时将为缓存生成 .xml 描述文件。XML（可扩展标记语言）描述文件包含一系列重要缓存属性，Maya 使用这些属性查找几何缓存对象的数据文件以及其他有用信息（如其缓存的时间范围）。可以使用 XML 描述文件跟踪几何缓存文件及其关联的对象和场景。

**注**

XML 描述文件是只读文件。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-1BB16083-3C1F-4729-B663-45F58BB466AE.png) <!-- baize:img-hook downloaded=false reason="正文 1947 字 ≥300，非承重" -->

XML 描述文件中包含的几何缓存信息由 XML 元素和属性设置结构或进行组织。每个常规元素（如 cacheType 和通道）或嵌套元素（如 channel#）都包含一个或多个 属性（如“类型”(Type)、“ChannelName”或“SamplingRate”），其中列出了特定几何缓存属性。

## Autodesk_Cache_File

### cacheType

指定几何缓存在磁盘上的格式。

#### 格式(Format)

指定缓存格式为 mcx 还是 mcc 文件。

类型(Type)

从下列选项中进行选择：

#### OneFile

指定几何缓存包含在单个 Maya 缓存文件中。

#### OneFilePerFrame

指定几何缓存分为多个 Maya 缓存文件，每个缓存帧一个文件。

### 时间(time)

#### 范围(Range)

指定几何缓存的帧或时间范围。例如，如果几何缓存从帧 1-25 包含对象的变形，则范围属性将为 250-6250。

时间范围以时间步度量。时间步是子帧单位。每个几何缓存帧包含多个时间步。帧中包含的时间步数由当前工作单位（时间）用户首选项设置确定。

每一帧的时间步数 = 6000/帧速率。例如，如果您的“工作单位(时间)”(Working Units (Time))首选项设置为胶片 (24 fps)，则几何缓存的每个帧包含 250 个时间步。

### cacheTimePerFrame

#### TimePerFrame

指定几何缓存的每个帧中的时间步数。

### cacheVersion

#### 版本(Version)

指定创建当前 XML 描述文件及其几何缓存文件的 Maya 几何缓存功能的版本号。

### 最大(extra)

为几何缓存指定以下内容：

- 几何缓存的 Maya 场景文件的名称及其在磁盘上的位置。

- 创建几何缓存的 Maya 版本。

- 创建几何缓存的帐户的名称。

### 通道(Channels)

包含所有对象或通道特定的几何缓存信息。

channel#

将为每个几何缓存对象指定其各自的 channel# 嵌套元素。例如，如果选择 5 个对象，将“文件分布”(File Distribution)设置为“一个文件”(One File)或“每帧一个文件”(One File Per Frame)，并缓存其变形，则将生成一个 XML 描述文件并且会包含以下嵌套元素：channel0、channel1、channel2、channel3 和 channel4。但是，如果将“文件分布”(File Distribution)设置为“每个几何体一个文件”(One File Per Geometry)，则将为每个选定对象生成一个 XML 描述文件并且每个 .xml 文件中只显示一个 channel# 嵌套元素。

#### ChannelName

指定几何缓存所属的对象的名称。此值对于每个几何缓存对象是唯一的。

#### ChannelType

指定在其中存储通道的几何缓存数据的数组的数据类型。当前，仅支持“DoubleVectorArray”。

#### 通道解释(Channel Interpretation)

指定通道的几何缓存驱动哪些类型的对象数据。当前，仅支持“位置”(Positions)属性值。

#### SamplingType

指定是否以等空间间隔将通道的变形采样保存到磁盘。规则指示以等空间间隔保存这些采样，不规则指示以不等空间间隔保存这些采样。

这些值由 Maya 用于帮助它更高效地在磁盘上搜索通道的几何缓存文件。

通常，几何缓存的采样类型在创建后始终是规则的。但是，如果编辑缓存的方式会更改其采样间隔，则其采样类型将更改为不规则。例如，如果您的几何缓存对每一帧求值，并且您向其附加一个每隔 2 帧进行一次求值的缓存，则您的缓存的采样类型将更改为不规则。

#### SamplingRate

指定在首次创建通道的几何缓存文件时，这些文件在磁盘上的间距。

“SamplingRate”=“帧求值频率”(Evaluate every frame(s)) x“求值保存频率”(}Save every eval(s))。例如，如果将“帧求值频率”(Evaluate every frame(s))设置为 0.5，将“求值保存频率”(Save every eval(s))设置为 1，并将用户“工作单位”(Working Units)设置为 24 fps，则会每 125 个时间步或半帧进行一次采样并将其保存到几何缓存。

#### StartTime

指定通道在磁盘上的第一个缓存文件的时间（以时间步为单位）。

#### EndTime

指定通道在磁盘上的最后一个缓存文件的时间（以时间步为单位）。
