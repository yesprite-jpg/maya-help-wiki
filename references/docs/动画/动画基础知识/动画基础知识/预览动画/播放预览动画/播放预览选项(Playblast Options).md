# 播放预览选项(Playblast Options)

打开“播放预览选项”(Playblast Options)

- 在“动画”(Animation)菜单集 (**F4**) 中选择“播放 > 播放预览”(Playback > Playblast) > ![图：在“动画”(Animation)菜单集 (F4) 中选择“播放 播放预览”(Playback Playblast) ，以…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2670 字 ≥300，非承重" -->，以打开“播放预览选项”(Playblast Options)窗口。（请参见[播放预览动画](../播放预览动画.md)。）

**注**

如果您使用的是 Black Magic，并且打开此窗口时 Maya 崩溃，请更新到 Desktop Video 版本 11.0（或更高版本）。有关更多的疑难解答提示，请参见下面的

支持文章

。

#### 时间范围(Time Range)

可用于设定是播放预览显示在“时间滑块”(Time Slider)中的整个时间范围，还是为播放预览设定自己的开始帧和结束帧。

#### 时间滑块(Time Slider)

启用时，播放预览将基于“时间滑块”(Time Slider)中的当前时间范围。

#### 开始/结束(Start/End)

启用时，播放预览将基于使用“开始时间”(Start Time)和“结束时间”(End Time)字段设定的开始时间和结束时间。

#### 使用序列时间(Use Sequence Time)

启用时，播放预览将基于“摄影机序列器”(Sequence Editor)中的“序列时间”(Sequence Time)。（另请参见[摄影机序列器时间轴和播放控件](../../../../Maya%20中的非线性动画/Maya%20中的非线性动画/摄影机序列器%28Camera%20Sequencer%29/“摄影机序列器”%28Camera%20Sequencer%29时间轴和播放控件.md)。）

#### 视图(View)

启用时，“播放预览”(Playblast)将使用默认的查看器显示图像。禁用时，播放预览过的图像将根据“播放预览选项”(Playblast Options)窗口中的“影片文件”(Movie file)设置保存到文件中。

#### 显示装饰(Show Ornaments)

将显示摄影机名称和原点处以及视图左下方处的轴。

通过禁用该选项，可以从“播放预览”(Playblast)动画隐藏图像平面的帧。如果禁用该选项，则无论是已在图像平面的“属性编辑器”(Attribute Editor)中启用还是禁用“帧可见性”(Frame Visibility)，图像平面的帧都不会显示在“播放预览”(Playblast)渲染中。

#### 渲染屏幕外(Render offscreen)

可用于使用屏幕外渲染缓冲区（而不是屏幕抓取）来播放预览。例如，可以在不打开 Maya 场景视图的情况下，使用“脚本编辑器”(Script Editor)来播放预览。

#### 多摄影机输出(Multi-Camera Output)

与立体摄影机一起使用该选项，以捕捉左侧摄影机和右侧摄影机的输出。如果场景视图处于立体模式，并且选择了“保存到文件”(Save to file)属性，则选择该选项后会将一组图像/影片发送到磁盘。

#### 格式(Format)

选择影片输出的格式

**注**

提示：

若要创建图像序列，而不是影片，请从“播放预览选项”(Playblast Options)中的

“格式”(Format)

下拉列表中选择

“图像”(image)

选项，然后在

“编码”(Encoding)

下拉列表中选择图像格式。选择

“全局”(global)

可使用与在

“渲染设置(Render Settings)”:“公用”(Common)选项卡

中指定的格式相同的格式。

#### 编码(Encoding)

选择要用于影片输出的编解码器。此列表将基于选定的“格式”(Format)进行更新。有关其他重要信息，请参见[编解码器支持](../../../../Maya%20中的非线性动画/Maya%20中的非线性动画/摄影机序列器%28Camera%20Sequencer%29/编解码器支持.md)。

#### 质量(Quality)

用于控制影片输出的压缩值。根据在“编码”(Encoding)下拉列表中选择的编解码器，结果会有所不同。质量值的范围从 0 到 100，默认值为 70。

#### 显示大小(Display Size)

有三个选项用于控制已创建的播放预览图像的分辨率。对于这三种情况中的任一情况，图像的最终大小都将根据“缩放”(Scale)选项中的量进一步缩放。

#### 来自窗口(From Window)

使播放预览图像与“活动视图”(Active view)大小相同。

#### 来自渲染设置(From Render Settings)

使播放预览图像具有窗口 > 渲染编辑器 > 渲染设置(Window > Rendering Editors > Render Settings)窗口的“公用”(Common)选项卡的“图像大小”(Image Size)区域所指定的大小。

#### 自定义(Custom)

激活“显示大小”(Display Size)选项下方的两个字段，允许指定播放预览图像的“宽度”(Width)和“高度”(Height)。

#### 缩放(Scale)

“显示大小”(Display Size)选项可提供对图像大小和纵横比的控制，而“缩放”(Scale)选项可通过将比例因子应用于“显示大小”(Display Size)选项中指定的分辨率来进一步细化“播放预览图像”(Playblast images)的大小。

默认值为 0.5，是“显示大小”(Display Size)对应大小的四分之一（宽度的 0.5 和高度的 0.5）。

#### 帧填充(Frame padding)

对于图像的“格式”(Format)，指定用于填充要播放预览的图像文件名的 0（零）的数量。这可用于为将要用的播放工具自定义图像文件名。

默认情况下，“帧填充”(Frame Padding)将设置为 4，以支持 Fcheck。

**注**

也可以将 -framepadding 标志用于 MEL 命令，以设置用于填充要播放预览的图像文件名的 0 的数量。

#### 移除临时文件(Remove temporary files)

启用该选项可在结束 Maya 会话时删除播放预览创建的临时文件。临时文件的写入位置为：C:\temp 目录 (Windows)、/var/tmp/ 或 /tmp/ (Linux)、Home 文件夹中的 Documents/temp 下 (Mac OS X)。

#### 保存到文件(Save to file)

默认情况下，影片或图像文件将写入系统的临时目录。如果要将影片保存到特定位置，请启用该选项。启用时，会显示一个输入字段用于输入文件名。也可以单击“浏览”(Browse)按钮查找相应的目录。如果“输出格式”(Output Format)选择为“Movieplayer”，文件将以“Movieplayer”格式保存。

#### 影片文件(Movie file)

如果使用“浏览”(Browse)按钮为“播放预览图像”(Playblast image(s))指定文件名，则将指定完整路径名称。

如果为影片文件指定没有路径的文件名，文件图像的位置将由当前项目设置设定。如果在[项目窗口(Project Window)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A570696B-95A4-4ED7-87EE-A7EAB63156CF)中指定了“图像位置”(Images location)，将在“图像位置”(Images location)中创建“播放预览图像”(Playblast image(s))。否则，将在项目的默认位置创建图像。

## 相关主题

- [播放预览动画](../播放预览动画.md)
