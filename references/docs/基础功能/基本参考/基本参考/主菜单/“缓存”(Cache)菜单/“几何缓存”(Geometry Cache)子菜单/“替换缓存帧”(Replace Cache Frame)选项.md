# “替换缓存帧”(Replace Cache Frame)选项

使用这些选项可设置在选择“缓存 > 几何缓存 > 替换缓存帧”(Cache > Geometry Cache > Replace Cache Frame)时发生的情况。另请参见[替换几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4672CB9D-7ADF-4B09-B49E-703991BC16AA)中的“替换几何缓存帧”。

#### “当前时间”(Current Time)字段

该字段将显示当前播放时间和帧编号。该字段是只读的。

#### 当前时间(Current Time)

启用时，当前对象的几何缓存帧将会替换，且生成原始未更改的缓存和描述文件的备份（默认情况下，名为 backup#_originalCacheName）。

例如，如果要在几何缓存中替换帧 12，则该选项仅支持为帧 12 创建缓存，然后将选定对象的当前缓存中的帧 12 替换为新创建的缓存帧。默认情况下，“当前时间”(Current Time)已启用。

#### 开始/结束(Start/End)

启用时，将替换当前对象的几何缓存的“开始替换帧”(Start Replace Frame)到“结束替换帧”(End Replace Frame)帧范围，且生成原始未更改的缓存和描述文件的备份（默认情况下，名为backup#_originalCacheName）。

例如，如果要在几何缓存中将帧 10 替换为帧 20，则该选项支持为帧 10 到帧 20 创建缓存，然后将选定对象的当前缓存中的该帧范围替换为新创建的缓存。默认情况下，“开始/结束”(Start/End)已禁用。

#### “帧求值频率”(Evaluate every frame(s))和“求值保存频率”(Save every evaluation(s))

默认情况下，创建几何缓存时，对象变形的采样将每帧进行一次，并保存到缓存中。

“帧求值频率(s)”(Evaluate every frame(s))将指定创建几何缓存期间进行的采样频率例如，如果值为 2，则当前对象的变形在“缓存时间范围”(Cache Time Range)内每隔一帧进行一次缓存。

“求值保存频率”(Save every evaluation(s))指定创建几何缓存期间将保存哪些采样。例如，如果值为 2，则指定仅由“帧求值频率”(Evaluate every frame(s))选项指定的每隔一次采样才能保存到几何缓存中。

有关详细信息，请参见[创建几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9038BC22-7398-4D90-AC84-83FBC9E40209)。

#### 删除备份文件(Delete backup files)

启用时，要替换的缓存帧将从磁盘的缓存文件中删除。删除是永久性的，无法通过“编辑 > 撤消”(Edit > Undo)或 Ctrl+Z 撤消。

#### 无插值(No Interpolation)

启用时，对象的当前缓存帧和要替换的帧之间不会出现插值。

#### 插值帧(Interpolate Frames)

启用时，要替换的帧之前和之后的缓存帧将会插值，以便在对象的当前缓存帧和要替换的帧之间创建平滑过渡。

#### 重命名插值帧(Rename Interpolated Frames)

启用时，原始缓存文件将重命名为您在“重命名插值帧”(Rename Interpolated Frames)字段中指定的名称。

#### 开始替换帧/结束替换帧(Start Replace Frame / End Replace Frame)

使用这些字段，可以为要替换的缓存帧范围指定开始帧和结束帧。“开始替换帧”(Start Replace Frame)和“结束替换帧”(End Replace Frame)仅在“开始/结束”(Start/End)已启用时才可用。

#### 开始插值帧/结束插值帧(Start Interpolation Frame / End Interpolation Frame)

使用这些字段，可以为要插值的缓存帧范围指定开始帧和结束帧。通常，插值范围在要替换的帧之前开始，并在要替换的帧之后结束。“开始插值帧”(Start Interpolation Frame)和“结束插值帧”(End Interpolation Frame)仅在“插值帧”(Interpolate Frames)或“重命名插值帧”(Rename Interpolated Frames)启用时才可用。

### 入切线/出切线(In Tangent/Out Tangent)

使用这些下拉菜单，可以为要替换的几何缓存帧之前（“入切线”(In Tangent)）和之后（“出切线”(Out Tangent)）的缓存插值指定切线类型。如果需要平滑对象的替换缓存帧及其几何缓存静止之间的插值，则该选项十分有用。

#### 线性(Linear)

变形是以线性方式从插值范围中的第一帧到最后一帧进行插值的，它将在和替换帧之间创建平滑而呈直线的过渡效果。

#### 平滑(Smooth)

变形是以样条线方式从插值范围中的第一帧到最后一帧进行插值的，它将在和替换帧之间创建平滑而渐变的过渡效果。

#### 步长(Step)

变形是以阶跃方式从插值范围中的第一帧到最后一帧进行插值的，它将在和替换帧之间创建跳跃的过渡效果。
