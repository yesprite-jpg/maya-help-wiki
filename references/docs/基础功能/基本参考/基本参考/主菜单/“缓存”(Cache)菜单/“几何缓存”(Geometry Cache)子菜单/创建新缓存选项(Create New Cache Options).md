# 创建新缓存选项(Create New Cache Options)

使用这些选项可设置在选择“缓存 > 几何缓存 > 创建新缓存”(Cache > Geometry Cache > Create New Cache)创建几何缓存时发生的情况。另请参见[创建和编辑几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F338ECB1-F4C3-4632-9168-EB917C2353DC)。

#### 缓存目录(Cache Directory)

在服务器或本地磁盘上指定保存几何缓存的位置。使用文件夹图标 (![图：在服务器或本地磁盘上指定保存几何缓存的位置。使用文件夹图标 ()，可以浏览到除默认目录以外的不同目录。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-A66E3A22-1319-4CC8-B9C8-76E8CD6EE002.png) <!-- baize:img-hook downloaded=false reason="正文 2107 字 ≥300，非承重" -->)，可以浏览到除默认目录以外的不同目录。

如果已将场景保存到磁盘，那么默认情况下会将几何缓存文件保存到以 \maya\projects\default\data\ 目录中的场景文件命名的文件夹中。如果从未保存场景，那么默认情况下会将几何缓存文件保存到 \maya\projects\default\data\cache 目录中。

#### 缓存名称(Cache Name)

为要创建的几何缓存指定基础名称。

#### 使用缓存名称作为前缀(Use Cache Name as Prefix)

将“缓存名称”(Cache Name)设置为前缀。启用时，几何缓存的基础名称是当前对象的名称加上作为前缀的指定的“缓存名称”(Cache Name)。例如，名为 Ball、前缀为 ted 的对象的缓存文件名如下所示：ted_BallFrame1、ted_BallFrame2、ted_BallFrame3 等。只有当“每帧一个文件”(One File Per Frame)或“每个几何体一个文件”(One File per Geometry)启用时，该选项才可用。

#### 缓存格式(Cache format)

指定 Maya 缓存格式。

#### mcx

创建使用 64 位索引的缓存文件。这些缓存文件可以超过 2.0 GB。

#### mcc

创建使用 32 位索引的缓存文件。这些缓存文件不能超过 2.0 GB。

#### 文件分布(File Distribution)

设定下列选项之一：

#### 每帧一个文件(One File Per Frame)

指定为指定的“缓存时间范围”(Cache Time Range)创建每帧一个几何缓存文件。如果已选择多个对象，则会为所有对象创建每帧一个几何缓存文件。

#### 一个文件(One File)

指定为指定的“缓存时间范围”(Cache Time Range)创建一个几何缓存文件。如果已选择多个对象，那么会为所有对象创建一个几何缓存文件。

#### 每个几何体一个文件(One File per Geometry)

启用时，为每个选定对象和指定的“缓存时间范围”(Cache Time Range)创建一个几何缓存文件（“一个文件”(One File)启用时）或每帧一个几何缓存文件（“每帧一个文件”(One File Per Frame)启用时）。

禁用时，为所有选定对象和指定的“缓存时间范围”(Cache Time Range)创建一个几何缓存文件（“一个文件”(One File)启用时）或每帧一个几何缓存文件（“每帧一个文件”(One File Per Frame)启用时）。

该选项仅在选择多个对象时可用。

**注**

当“一个文件”(One File)或“每个几何体一个文件”(One File per Geometry)缓存超出 2GB 几何缓存大小限制时，会自动分割该缓存并融合生成的缓存分段。

### 将点存储为(Store points as)

指定在其中存储几何缓存点数据的数组类型。几何缓存数组类型确定正在存储的点数据的数值精度或精确度（小数点位）。

#### 双精度(Double)

该向量数组的精确度高于“浮点型”(Float)，但是其大小是“浮点型”(Float)大小的两倍。

#### 浮点型(Float)

向量数组的精确度低于“双精度”(Double)，但是其大小是“双精度”(Double)的一半。

#### 缓存时间范围(Cache Time Range)

设定下列选项之一：

#### 渲染设置(Render Settings)

指定当前“渲染设置”(Render Settings)确定“缓存时间范围”(Cache Time Range)。

#### 时间滑块(Time Slider)

指定时间滑块中的当前播放范围确定“缓存时间范围”(Cache Time Range)。

#### 开始/结束(Start/End)

指定在指定的“开始”(Start)和“结束”(End)时间之间（包括“开始”(Start)和“结束”(End)时间）的帧范围确定“缓存时间范围”(Cache Time Range)。

#### 开始/结束(Start/End)

这些字段用于指定“缓存时间范围”(Cache Time Range)的“开始”(Start)和“结束”(End)时间。

#### “帧求值频率”(Evaluate every frame(s))和“求值保存频率”(Save every evaluation(s))

默认情况下，创建几何缓存时，对象变形的采样将每帧进行一次，并保存到缓存中。

“帧求值频率(s)”(Evaluate every frame(s))将指定创建几何缓存期间进行的采样频率例如，如果值为 2，则当前对象的变形在“缓存时间范围”(Cache Time Range)内每隔一帧进行一次缓存。

“求值保存频率”(Save every evaluation(s))指定创建几何缓存期间将保存哪些采样。例如，如果值为 2，则指定仅由“帧求值频率”(Evaluate every frame(s))选项指定的每隔一次采样才能保存到几何缓存中。

有关详细信息，请参见[创建几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9038BC22-7398-4D90-AC84-83FBC9E40209)。
