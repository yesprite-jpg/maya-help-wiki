# “摄影机序列器”(Camera Sequencer)菜单栏

## “文件”(File)菜单

#### 导入镜头音频(Import Shot Audio)

打开“导入”(Import)窗口，在该窗口中可以将音频片段与选定快照相关联。选择的文件将指定为要使用每个选定快照播放的音频。请参见[将音频与序列或快照相关联](将音频添加到序列中/将音频与序列或快照相关联.md#GUID-A625FA77-D4EF-414E-B57D-21472CE55A98__GUID-B9FE70E4-F847-454E-AF3A-EA03BAEB24C8)。

#### 导入序列器音频(Import Sequencer Audio)

打开“导入”(Import)窗口，以便可以浏览选择并导入音频片段。请参见[将音频与序列或快照相关联](将音频添加到序列中/将音频与序列或快照相关联.md#GUID-A625FA77-D4EF-414E-B57D-21472CE55A98__GUID-B9FE70E4-F847-454E-AF3A-EA03BAEB24C8)。

#### 导入编辑(Import Editorial)

打开“导入”(Import)窗口，以便可以浏览选择并导入包含音频和视频片段信息的编辑文件。您只能以 Apple® Final Cut Pro® XML 格式导入文件。请参见[导入和导出编辑内容](导入和导出编辑内容.md)。

#### 导入编辑(Import Editorial) > ![图：导入编辑(Import Editorial)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5986 字 ≥300，非承重" -->

打开“导入编辑选项”(Import Editorial Options)。

#### 导入编辑选项(Import Editorial Options)

#### 开始帧覆盖(Start Frame Override)

启用时，可以使用“帧”(Frame)字段指定要将导入的序列加载到的位置。

#### 帧(Frame)

当“开始帧覆盖”(Start Frame Override)处于启用状态时，输入要加载导入序列的位置对应的帧编号。例如，输入值 10 来偏移编辑序列，使其从第 10 帧开始。

#### 导出编辑(Export Editorial)

打开“导出”(Export)窗口，以便采用 Apple® Final Cut Pro® XML 格式导出包含音频和视频片段信息的编辑文件。请参见[导入和导出编辑内容](导入和导出编辑内容.md)。

#### 导出编辑(Export Editorial) > ![图：导出编辑(Export Editorial)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5986 字 ≥300，非承重" -->

打开“导出编辑选项”(Export Editorial Options)。

#### 导出编辑选项

#### 播放预览不同步片段(Playblast out-of-sync clips)

启用时，Maya 将播放预览不含关联影片的任何快照并重新播放预览已禁用影片的任何快照。禁用时，不会进行播放预览，但以前播放预览的快照将仍有位于编辑文件中的关联影片。

## “编辑”(Edit)菜单

“编辑”(Edit)菜单包含所有的修剪、分割和捕捉功能。

#### 撤消(Undo)

撤消上次的修剪、分割或捕捉操作。

#### 重做(Redo)

重做上次修剪、分割或捕捉操作。

#### 复制(Copy)

复制选定的快照。（仅在选择快照时可用）。

Maya 将指定给源快照的同一摄影机指定给目标快照。当重复进行粘贴操作时，任何图像平面或音频节点都会被附着到快照。

#### 粘贴(Paste)

粘贴复制的快照。（仅在已复制快照时可用。）

#### 涟漪编辑(Ripple Edit)

启用和禁用“涟漪编辑”模式。启用时，操纵某个镜头会对其他镜头产生涟漪影响。

如果希望操纵一个要传播到其他快照上的快照，请使用此模式。例如，如果通过拖动使一个快照变得更长，则所有其他快照都会向前移动相同的量。快照之间的空间量保持不变。

请参见[启用涟漪编辑](操纵序列中的摄影机快照/启用涟漪编辑.md)。

#### 剪去前方(Trim Before)

修剪序列时间光标之前的当前快照。

#### 剪去后方(Trim After)

修剪序列时间光标之后的当前快照。

#### 显示所有图像平面(Show All Image Planes)

显示与任何快照关联的所有图像平面。

#### 隐藏所有图形平面(Hide All Image Planes)

隐藏与任何快照关联的所有图形平面

#### 捕捉至上一个(Snap to Previous)

移动选定快照以使其显示在左侧最近相邻快照的旁边，从而消除快照之间的任何间隙。

#### 捕捉至下一个(Snap to Next)

移动选定快照使其位于右侧最近相邻快照的旁边，从而消除快照之间的任何间隙。

#### 捕捉至上一个(当前轨迹) (Snap to Previous (Current Track))

向左移动选定快照，使其位于同一轨迹上最近相邻快照的旁边，从而消除快照之间的任何间隙。

#### 捕捉至下一个(当前轨迹) (Snap to Next (Current Track))

向右移动选定快照，使其位于同一轨迹上最近相邻快照的旁边，从而消除快照之间的任何间隙。

#### 移除镜头间隙(Remove Shot Gaps)

可压缩轨迹，从而移除未定义快照的任何间隙。选择是对“选定镜头”(Selected Shots)还是“所有镜头”(All Shots)消除间隙。

#### 移除镜头重叠(Remove Shot Overlaps)

展开轨迹，从而移除快照之间的任何重叠。选择是对“选定镜头”(Selected Shots)还是“所有镜头”(All Shots)消除重叠。

#### 移除镜头间隙和重叠(Remove Shot Gaps and Overlaps)

移除与轨迹上的选定快照或所有快照对应的所有间隙和重叠。选择要移动“选定镜头”(Selected Shots)还是“所有镜头”(All Shots)。

#### 分割镜头(Split Shots)

分割选定的快照。选择“编辑 > 分割镜头”(Edit > Split Shots) > ![图：分割选定的快照。选择“编辑 分割镜头”(Edit Split Shots) ，以打开“分割镜头选项”(Split Sho…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5986 字 ≥300，非承重" -->，以打开“分割镜头选项”(Split Shot Options)。

#### 分割快照选项

#### 分割时间(Split Time)

设置是否使用“当前时间”(Current Time)，或选择“指定时间”(Specify Time)以输入一个时间值。

## “视图”(View)菜单

#### 修改

#### 属性编辑器(Attribute Editor)

在“属性编辑器”(Attribute Editor)中显示快照属性。

#### 图像平面属性编辑器(Image Plane Attribute Editor)

在“属性编辑器”(Attribute Editor)中显示图像平面属性。

#### 启用声音

启用或禁用声音播放。请参见[将音频添加到序列中](将音频添加到序列中.md)。

#### 播放列表(Playlist)

打开“快照播放列表”(Shot Playlist)窗口，该窗口为您提供了一个表视图，其中包含可快速编辑的所有快照和快照参数。使用“摄影机”(Camera)列可以更改快照相机，或者使用计时单元格可以调整快照长度。请参见[更改快照长度](操纵序列中的摄影机快照/更改快照长度.md)。

## “创建”(Create)菜单

#### 镜头(Shot)

在当前轨迹上创建快照。您还可以选择“创建 > 快照”(Create > Shot) > ![图：在当前轨迹上创建快照。您还可以选择“创建 快照”(Create Shot) ，以打开“创建快照选项”(Create Sh…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5986 字 ≥300，非承重" -->，以打开“创建快照选项”(Create Shot Options)。请参见[创建摄影机快照](创建摄影机快照/创建摄影机快照.md)。

#### 创建快照选项

#### 名称(Name)

输入此快照的名称。此名称将显示在“摄影机序列器”(Camera Sequencer)中的快照上。

#### 镜头摄影机(Shot Camera)

使用该场景中的摄影机下拉列表为此快照指定活动摄影机。

#### 开始时间(Start time)

输入此摄影机快照的开始时间。例如，如果希望快照在第 25 帧开始，请输入 25 作为“开始时间”(Start time)。

#### 结束时间(End time)

输入此摄影机快照的结束时间。

#### 新建快照放置(New Shot Placement)

设置要在其中创建新快照的位置。

选择以下预设位置之一：“当前帧”(Current Frame)、“当前快照之后”(After Current Shot)、“当前快照之前”(Before Current Shot)或“序列末尾”(End of Sequence)，或者选择“手动”(Manual)以使用“序列开始时间”(Sequence Start Time)和“序列结束时间”(Sequence End Time)字段来指定要将快照放置到的位置。

#### 图像(Image)

单击可打开文件浏览器，并选择要在此快照的图像平面上显示的文件。

#### 不透明度(Opacity)

为投影的图像平面输入不透明度值。

## “组”(Group)菜单

#### 创建(Create)

创建一组选定快照。请参见[创建摄影机快照组](创建摄影机快照/创建摄影机快照组/创建摄影机快照组.md)。

#### 设置活动镜头(Set Active Shot)

从选定轨迹中的快照列表中为此组选择活动快照。请参见[在组中设定活动快照](创建摄影机快照/创建摄影机快照组/创建摄影机快照组.md#GUID-401F60F3-05FB-4110-A462-581E4E114209__WS73099CC142F48755-6AAE5668123E144A987-694C)。

#### 选择镜头(Select Shot)

从列表中选择一个快照。

#### 将快镜头加到组(Add Shot To Group)

将选定快照添加到组中。

#### 从组移除镜头(Remove Shot From Group)

从组中移除选定快照。

#### 解组(Ungroup)

从组中移除所有分组的快照，然后删除组。

#### 删除组和内容(Delete Group and Contents)

删除组和其中包含的所有快照。

## “播放预览”(Playblast)菜单

**注**

播放预览快照时，不包括 Alpha 通道信息。

#### 播放预览选定镜头(Playblast Selected Shots)

将选定快照渲染到影片片段中。请参见[播放预览摄影机快照](播放预览摄影机快照.md)。

“播放预览 > 播放预览选定镜头”(Playblast > Playblast Selected Shots) > ![图：“播放预览 播放预览选定镜头”(Playblast Playblast Selected Shots) 可打开 “播放预…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5986 字 ≥300，非承重" --> 可打开 “播放预览快照选项”(Playblast Shot Options)。进行下列设定：

##### 目录

设置要将输出影片文件保存到的文件路径。

默认情况下，“目录”(Directory)设置为 data，即在“编辑项目”(Edit Projects)对话框中设置的默认“影片”(Movie)项目目录。（请参见[项目窗口(Project Window)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A570696B-95A4-4ED7-87EE-A7EAB63156CF)。）

**注**

(Mac OS X) 如果根据默认值更改当前项目，则

“播放预览快照选项”(Playblast Shot Options)

或

“播放预览序列选项”(Playblast Sequence Options)

中的

“目录”(Directory)

字段将列出实际不存在的数据目录。为了浏览选择新目录，请首先删除在

“目录”(Directory)

字段中显示的文件夹名称，然后单击“浏览（文件）”(Browse (folder))图标，并从文件浏览器中选择一个新目录。

##### 文件名模板(File name template)

设置命名约定，以帮助您识别和组织从“摄影机序列器”(Camera Sequencer)中输出的片段。

**注**

提示：

在此字段上单击鼠标右键，可从预定义的文件名组件列表中选择。例如，可以插入摄影机名称或当前日期作为文件名的一部分。

##### 控制柄长度(Handle length)

默认值为 0。

##### 构建图像平面(Build Image Plane)

设置要在图像平面上播放的输出影片。

##### 图像平面不透明(Image Plane Opaque)

用于控制播放预览影片的图像平面的透明度。启用时，图像平面是完全不透明的，因此播放预览影片会隐藏场景视图中的几何体。禁用时，图像平面是透明的，并且不会遮挡场景视图。

##### 屏幕外(Offscreen)

启用时，使用屏幕外渲染缓冲区播放预览，而不是使用屏幕抓取。可以最小化 Maya，并仍然播放预览影片片段。

**注**

此选项对于 Mac OS X 上的

“摄影机序列器”(Camera Sequencer)

不可用。

##### 格式(Format)

选择要输出的影片或图像文件格式。

##### 编码(Encoding)

选择要用于影片输出的编解码器或用于图像输出的文件格式。（此列表将基于选定的“格式”(Format)进行更新。）有关其他重要信息，请参见[编解码器支持](编解码器支持.md)。

##### 质量(Quality)

用于控制影片输出的压缩值。根据在“编码”(Encoding)下拉列表中选择的编解码器，结果会有所不同。质量值的范围从 0 到 100，默认值为 50。

#### 播放预览所有镜头(Playblast All Shots)

将所有快照播放预览到单个影片。播放预览快照之前，选择“播放预览 > 播放预览所有镜头”(Playblast > Playblast All Shots) > ![图：将所有快照播放预览到单个影片。播放预览快照之前，选择“播放预览 播放预览所有镜头”(Playblast Playblas…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5986 字 ≥300，非承重" -->，以打开“播放预览快照选项”(Playblast Shot Options)并设置选项。

#### 播放预览序列(Playblast Sequence)

将序列中的所有快照播放预览到单个影片。所有相关的音频轨迹都将被正确添加到文件中。

播放预览序列时，通过使序列运行时间超过整个序列的长度，可以生成单个影片。单个快照是否对影片起作用取决于快照彼此重叠的方式。

影片输出与任何特定快照都没有关联，并且不会附着到任何摄影机的任何图像平面。如果要生成一个在“摄影机序列器”(Camera Sequencer)外部使用的影片文件，请使用此选项。

请参见[播放预览摄影机快照](播放预览摄影机快照.md)。

“播放预览序列”(Playblast Sequence) > ![图：“播放预览序列”(Playblast Sequence) 将打开“播放预览序列选项”(Playblast Sequenc…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5986 字 ≥300，非承重" -->将打开“播放预览序列选项”(Playblast Sequence Options)。进行下列设定：

##### 目录(Directory)

设置要将输出影片文件保存到的目录。

##### 文件名(File name)

输入输出影片的文件名。

##### 视图(View)

启用时，Maya 会启动一个新窗口，以便在序列预览播放完成后播放影片片段。（默认情况下此选项处于启用状态）。

##### 屏幕外(Offscreen)

启用时，使用屏幕外渲染缓冲区播放预览，而不是使用屏幕抓取。可以最小化 Maya，并仍然播放预览影片片段。

**注**

此选项对于 Mac OS X 上的

“摄影机序列器”(Camera Sequencer)

不可用。

#### 格式(Format)

选择要输出的影片或图像文件格式。

#### 编码(Encoding)

选择要用于影片输出的编解码器或用于图像输出的文件格式。（此列表将基于选定的“格式”(Format)进行更新。）有关其他重要信息，请参见[编解码器支持](编解码器支持.md)。

#### 质量(Quality)

用于控制影片输出的压缩值。根据在“编码”(Encoding)下拉列表中选择的编解码器，结果会有所不同。质量值的范围从 0 到 100，默认值为 50。

#### “分辨率高度”(Resolution Height)和“分辨率宽度”(Resolution Width)

用于指定生成的影片片段的分辨率。

#### 重新播放预览选定镜头(Re-Playblast Selected Shot)

重新播放预览选定快照。在修改整个快照并且希望更新输出影片时，请选择此选项。若要仅重新播放预览特定的帧范围，请选择“播放预览 > 播放预览序列”(Playblast > Playblast Sequence) > ![图：重新播放预览选定快照。在修改整个快照并且希望更新输出影片时，请选择此选项。若要仅重新播放预览特定的帧范围，请选择“播放预…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5986 字 ≥300，非承重" -->。

“重新播放预览选定镜头”(Re-Playblast Selected Shot) > ![图：“重新播放预览选定镜头”(Re-Playblast Selected Shot) 将打开“重新播放预览快照选项”(Re-…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5986 字 ≥300，非承重" -->将打开“重新播放预览快照选项”(Re-Playblast Shot Options)，允许您指定要重新播放预览的选定快照的帧范围。新的重新播放预览的帧将替换目标影片文件中的指定帧范围。设置以下选项：

##### 替换音频(Replace Audio)

设置是否希望替换与要重新播放预览的帧关联的音频。启用时，Maya 将替换输出影片中的选定帧范围的音频。

#### 开始帧(Start Frame)

输入要重新播放预览的分段的第一帧。

#### 结束帧(End Frame)

输入要重新播放预览的分段的最后一帧。

#### 屏幕外(Offscreen)

启用时，使用屏幕外渲染缓冲区播放预览，而不是使用屏幕抓取。可以最小化 Maya，并仍然播放预览影片片段。

**注**

此选项对于 Mac OS X 上的

“摄影机序列器”(Camera Sequencer)

不可用。

#### 格式(Format)

选择要输出的影片或图像文件格式。

#### 编码(Encoding)

选择要用于影片输出的编解码器或用于图像输出的文件格式。（此列表将基于选定的“格式”(Format)进行更新。）有关其他重要信息，请参见[编解码器支持](编解码器支持.md)。

#### 质量(Quality)

用于控制影片输出的压缩值。根据在“编码”(Encoding)下拉列表中选择的编解码器，结果会有所不同。质量值的范围从 0 到 100，默认值为 50。
