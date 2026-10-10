# 捕捉缩略图/播放预览(Capture Thumbnail/Playblast)选项

以下选项可用于设置和捕捉要随场景文件一起保存的缩略图（单个图像）或播放预览（图像序列），以便在[内容浏览器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9221B2E8-7E68-4ECB-94DC-ABEB21E956BF)中可以识别它。仅支持 Maya ASCII (.ma)、二进制 (.mb) 和 FBX 文件。有关使用这些选项的详细信息，请参见[创建场景文件的缩略图和播放预览](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B3FB68-AAA4-415D-A37B-1EAC461613C0)。

选择“文件 > 保存场景”(File > Save Scene) > ![图：选择“文件 保存场景”(File Save Scene) 、“文件 场景另存为”(File Save Scene As)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 984 字 ≥300，非承重" -->、“文件 > 场景另存为”(File > Save Scene As)、“文件 > 导出全部”(File > Export All)、“文件 > 导出当前选择”(File > Export Selection)或“文件 > 导出到脱机文件”(File > Export to Offline File)时，可以访问这些选项。

在相应的“保存/导出选项”(Save/Export Options)对话框中（例如，在[保存场景选项(Save Scene Options)](保存场景选项%28Save%20Scene%20Options%29.md)中），单击“捕捉缩略图/播放预览”(Capture Thumbnail/Playblast)按钮。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-CA2838F7-24F8-4080-9871-16C26F4E4A5B.png) <!-- baize:img-hook downloaded=false reason="正文 984 字 ≥300，非承重" -->

## 类型(Type)

“缩略图”(Thumbnail)保存显示在黄色捕捉帧中的静态图像。单击“保存”(Save)，缩略图将显示在“保存/导出选项”(Save/Export Options)对话框中。

“播放预览”(Playblast)根据指定的“帧范围”(Frame range)值保存显示在黄色捕捉帧中的图像序列。

缩略图保存在项目中用于保存场景文件（例如，项目的 \scenes 文件夹）的 mayaSwatches 文件夹下的 .ma.swatch、.mb.swatch 或 .fbx.swatch 文件中。

播放预览保存在 .ma.preview、.mb.preview 或 .fbx.preview 文件中，每帧捕捉一个文件。

## 帧范围(Frame range)

“开始/结束”(Start/End)定义时间轴中为播放预览捕捉的帧范围。允许的最大帧数为 300。

## 捕捉(Capture)

  “捕捉”(Capture)将显示在活动视图面板的黄色捕捉帧中的当前帧或图像序列保存为缩略图或播放预览。在单击“保存”(Save)之前，按住图像下面的箭头预览播放预览。

  “删除”(Delete)将删除当前缩略图或捕捉的序列。

  标题框(Title Frame)：拖动滑块以选择单帧作为缩略图来表示场景文件的序列。

## 相关主题

- [创建场景文件的缩略图和播放预览](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B3FB68-AAA4-415D-A37B-1EAC461613C0)

- [“文件”(File)菜单](../“文件”%28File%29菜单.md)

- [保存场景选项(Save Scene Options)](保存场景选项%28Save%20Scene%20Options%29.md)
