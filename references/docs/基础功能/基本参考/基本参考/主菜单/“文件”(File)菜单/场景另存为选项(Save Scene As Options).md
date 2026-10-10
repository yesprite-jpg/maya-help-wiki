# 场景另存为选项(Save Scene As Options)

使用这些选项可设置在选择“文件 > 场景另存为”(File > Save Scene As)或按 Ctrl+Shift+S 时发生的情况。另请参见[创建、打开或保存场景文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DC183670-EF0F-4E69-AEDF-69D408D82408)。

## 常规选项(General Options)

#### 文件类型(File type)

将文件类型设置为“mayaBinary”或“mayaAscii”。默认值为“mayaAscii”。

**注**

自 Maya 2014 起，mayaBinary (.mb) 文件格式使用 64 位索引。保存为 .mb 文件的场景与 Maya 的较低版本不兼容。

#### 默认文件扩展名(Default file extensions)

为 Maya ASCII 文件名添加文件扩展名 .ma，并为 Maya 二进制文件名添加文件扩展名 .mb。

## 3D 绘制纹理选项(3D Paint Texture Options)

#### 复制纹理贴图(Copy texture maps)

使您可以确定在保存场景时，Maya 如何保存使用“3D 绘制工具”(3D Paint Tool)创建的文件纹理。

#### 始终(Always)

保存不同版本的场景时保存不同版本的文件纹理。如果使用文件纹理的不同迭代次数或版本，请使用该设置。

#### 除非被引用(Unless referenced)

只有在绘制的角色未被引用时，才会保存文件纹理。选定该选项时，Maya 将使用被引用文件中的文件纹理（即使使用新名称保存该场景也一样）。如果角色未被引用，并在选定该选项时保存场景副本，则 Maya 将创建文件纹理的副本。

#### 从不(Never)

不保存新文件纹理。如果不再更改文件纹理并继续使用保存的文件纹理（即使使用新名称保存场景也一样），请使用该设置。这可防止积累多个纹理副本。

## 磁盘缓存选项(Disk cache options)

这指的是需要磁盘缓存的[抖动变形器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EE9CA51E-F618-4EE4-8D9F-6D6470EBF89E)。磁盘缓存作为 DG 节点实现，并在保存文件时更新。

#### 始终(Always)

当第一次保存场景或用新名称保存时，创建抖动磁盘缓存文件副本。缓存文件名与场景文件名相对应。这是默认设置。

#### 从不(Never)

不保存抖动磁盘缓存文件副本。使用此选项可以避免创建副本，从而节省磁盘空间。

**注**

“项目窗口”(Project Window)的“主项目位置”(Primary Project Locations)列表中包含一个“磁盘缓存”(Disk Cache)选项。这使您可以设置用于存储抖动变形器缓存文件的默认位置。

## 引用选项(Referencing options)

#### 锁定文件(Lock File)

在从其他场景文件引用文件时，阻止编辑该文件。

## 文件类型特定选项(File Type Specific Options)

#### 使用节点上属性的全名(Use full names for attributes on nodes)

显示节点属性的全称。

## 缩略图/播放预览选项(Thumbnail/Playblast Options)

这些选项与[保存场景选项(Save Scene Options)](保存场景选项%28Save%20Scene%20Options%29.md)中相同。有关使用这些选项的信息，请参见[创建场景文件的缩略图和播放预览](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B3FB68-AAA4-415D-A37B-1EAC461613C0)。

## 相关主题

- [支持的文件格式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3FDB6F01-1830-4AB3-BB91-287A64A269A6)

- [保存场景选项(Save Scene Options)](保存场景选项%28Save%20Scene%20Options%29.md)

- [捕捉缩略图/播放预览(Capture Thumbnail/Playblast)](捕捉缩略图播放预览%28Capture%20ThumbnailPlayblast%29选项.md)

- [崩溃后恢复数据](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-89F4AF19-AFDC-40BF-8571-8999C520505C)

- [使用代理引用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-11182679-1A3D-4A05-845B-19FBBAEC786A)
