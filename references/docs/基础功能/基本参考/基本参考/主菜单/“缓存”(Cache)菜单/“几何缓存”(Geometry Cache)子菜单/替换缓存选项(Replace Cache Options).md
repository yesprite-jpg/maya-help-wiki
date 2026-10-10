# 替换缓存选项(Replace Cache Options)

使用这些选项可设置在选择“缓存 > 几何缓存 > 替换缓存”(Cache > Geometry Cache > Replace Cache)时发生的情况。另请参见[替换几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4672CB9D-7ADF-4B09-B49E-703991BC16AA)。

#### 缓存目录(Cache Directory)

指定服务器或本地磁盘上的位置，需要创建以替换当前缓存的几何缓存保存在该位置。使用文件夹图标 (![图：指定服务器或本地磁盘上的位置，需要创建以替换当前缓存的几何缓存保存在该位置。使用文件夹图标 ()，可以浏览到除默认目录以…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-A66E3A22-1319-4CC8-B9C8-76E8CD6EE002.png) <!-- baize:img-hook downloaded=false reason="正文 1622 字 ≥300，非承重" -->)，可以浏览到除默认目录以外的不同目录。

#### 缓存名称(Cache Name)

对需要创建以替换当前缓存的几何缓存指定基础名称。

#### 使用缓存名称作为前缀(Use Cache Name as Prefix)

将“缓存名称”(Cache Name)设置为前缀。启用时，几何缓存的基础名称是当前对象的名称加上作为前缀的指定的“缓存名称”(Cache Name)。例如，命名为 Ball 并带有前缀 ted 的对象的缓存文件名称如下：ted_Ball，ted_Ball2，ted_Ball3 等等。

#### 缓存格式(Cache format)

指定 Maya 缓存格式。

#### mcx

创建使用 64 位索引的缓存文件。这些缓存文件可以超过 2.0 GB。

#### mcc

创建使用 32 位索引的缓存文件。这些缓存文件不能超过 2.0 GB。

#### 文件分布(File Distribution)

设定下列选项之一：

#### 每帧一个文件(One File Per Frame)

指定为指定的“缓存时间范围”(Cache Time Range)创建每帧一个几何缓存文件。

#### 一个文件(One File)

指定为指定的“缓存时间范围”(Cache Time Range)创建一个几何缓存文件。

#### 每个几何体一个文件(One File per Geometry)

启用时，为每个选定对象和指定的“缓存时间范围”(Cache Time Range)创建一个几何缓存文件（“一个文件”(One File)启用时）或每帧一个几何缓存文件（“每帧一个文件”(One File Per Frame)启用时）。

禁用时，为所有选定对象和指定的“缓存时间范围”(Cache Time Range)创建一个几何缓存文件（“一个文件”(One File)启用时）或每帧一个几何缓存文件（“每帧一个文件”(One File Per Frame)启用时）。

该选项仅在选择多个对象时可用。

### 缓存时间范围(Cache Time Range)

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

#### 继承修改(Inherit modifications)

指定替换几何缓存继承它所替换的缓存的位置（在时间上）、修剪、拆分和缩放。
