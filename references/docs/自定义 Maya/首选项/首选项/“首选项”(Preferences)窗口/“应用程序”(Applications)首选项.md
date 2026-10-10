# “应用程序”(Applications)首选项

可以在[首选项(Preferences)窗口](../“首选项”%28Preferences%29窗口.md)的“应用程序”(Applications)类别中设置以下首选项。

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

使用此首选项组指定从 Maya 中打开特定图像或影片文件类型时要使用的应用程序。

输入访问每个列出的文件类型所需程序的路径，或者通过单击文件夹图标浏览到指向应用程序可执行文件的位置。

在“可选标志”(Optional Flags)字段中，您可以使用以下语法来配置图像或影片查看器：

| 标识符 | 含义 |
|---|---|
| %f | 文件名 |
| %s | 开始帧 |
| %e | 结束帧 |
| %b | 按帧跳转 |
| %r | 帧速率 |

（从 Maya 启动图像或影片查看器时，这些标识符将替换为您在 Maya 环境中指定的正确值。）

## 图像查看应用程序(Image Viewing Applications)

#### 所有格式(All formats)

选择要从 Maya 中（而不是使用 FCheck）启动的您自己的图像查看器。在“Hypershade”窗口中选择“文件 > 查看图像”(File > View Image)或“编辑 > 渲染纹理范围”(Edit > Render Texture Range)时，将使用此程序。

**注**

重要：

自 Maya 2020 起，FCheck 在 macOS 上不再受支持。

## 图像编辑应用程序(Image Editing Applications)

输入要用于每个文件类型的应用程序的路径，或浏览到指向应用程序可执行文件的位置。

#### Photoshop (PSD) 文件(Photoshop (PSD) Files)

指定使用“属性编辑器”(Attribute Editor)中的“查看”(View)或“编辑”(Edit)按钮编辑 PSD 文件纹理节点中的 Adobe® Photoshop® 文件时所使用的应用程序，或者在创建或编辑 PSD 网络时所使用的应用程序。该设置在安装了多个 Adobe Photoshop 版本时很有用。

#### 其他图像文件(Other Image Files)

指定使用“属性编辑器”(Attribute Editor)中的“查看”(View)或“编辑”(Edit)按钮编辑文件纹理节点中的图像时所使用的应用程序。

有关详细信息，请参见[文件纹理](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-92234087-2E79-412E-8174-CBAAE0463CD6)。

## 序列查看应用程序

#### 图像序列(Image Sequence)

选择要从 Maya 中（而不是使用 FCheck）启动的您自己的图像序列查看器。选择“文件 > 查看序列”(File > View Sequence)时，将使用该程序。

**注**

重要：

自 Maya 2020 起，FCheck 在 macOS 上不再受支持。

#### 音频视频交错(AVI)文件(Audio Video Interleave (AVI) files)

指定在 Maya 中启动 .avi 文件时要使用的播放器，例如，使用“窗口 > 播放预览”(Window > Playblast)选项。

#### QuickTime (MOV)文件(Quicktime (MOV) files)

指定在 Maya 中启动 .mov 文件时要使用的播放器，例如，使用“窗口 > 播放预览”(Window > Playblast)选项。

## 相关主题

- [指定默认媒体播放器](../../../自定义/自定义/自定义%20Maya%20工作方式/指定默认媒体播放器.md)

- [从 Maya 打开 Adobe Photoshop 中的 PSD 网络](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-FD5CE223-8AEA-446E-9428-E5E38520BCF3)

- [播放预览动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1C6EDC8D-DA67-490E-81F1-1205336DEBD9)
