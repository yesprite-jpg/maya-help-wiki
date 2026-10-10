# 附加到缓存选项(Append to Cache Options)

使用这些选项可设置在选择“缓存 > 几何缓存 > 附加到缓存”(Cache > Geometry Cache > Append to Cache)时发生的情况。另请参见[附加几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-73B28384-BB9F-4112-AA33-1DC311A153CE)。

### 附加时间范围(Append Time Range)

可用于为要创建并附加到当前对象已启用缓存中的几何缓存定义一个缓存时间范围。

#### 当前时间(Current Time)

指定仅当前帧被缓存并附加到启用的缓存中。

#### 当前时间到时间滑块末端(Current Time to Time Slider End)

针对要创建并附加到已启用缓存中的几何缓存指定其缓存时间范围从“当前时间指示器”(Current Time Indicator)的当前时间位置开始，到“播放结束时间”(Playback End Time)结束。

#### 时间滑块(Time Slider)

针对要创建并附加到已启用缓存中的几何缓存指定其缓存时间范围是整个播放范围。

#### 缓存末尾到时间滑块末端(End of cache to Time Slider End)

针对要创建并附加到已启用缓存中的几何缓存指定其缓存时间范围从已启用缓存的“源结束”(Source End)开始，到“播放结束时间”(Playback End Time)结束。

#### 缓存末尾到结束(End of cache to End)

针对要创建并附加到已启用缓存中的几何缓存指定其缓存时间范围从已启用缓存的“源结束”(Source End)开始，到“动画结束时间”(Animation End Time)结束。

#### 开始/结束(Start/End)

针对要创建并附加到已启用缓存中的几何缓存指定缓存时间范围在“开始/结束”(Start/End)字段中指定的“开始”(Start)和“结束”(End)时间开始和结束。

#### 开始/结束(Start/End)

这些字段用于指定“缓存时间范围”(Cache Time Range)的“开始”(Start)和“结束”(End)时间。

#### “帧求值频率”(Evaluate every frame(s))和“求值保存频率”(Save every evaluation(s))

默认情况下，创建几何缓存时，对象变形的采样将每帧进行一次，并保存到缓存中。

“帧求值频率(s)”(Evaluate every frame(s))将指定创建几何缓存期间进行的采样频率例如，如果值为 2，则当前对象的变形在“缓存时间范围”(Cache Time Range)内每隔一帧进行一次缓存。

“求值保存频率”(Save every evaluation(s))指定创建几何缓存期间将保存哪些采样。例如，如果值为 2，则指定仅由“帧求值频率”(Evaluate every frame(s))选项指定的每隔一次采样才能保存到几何缓存中。

有关详细信息，请参见[创建几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9038BC22-7398-4D90-AC84-83FBC9E40209)。
