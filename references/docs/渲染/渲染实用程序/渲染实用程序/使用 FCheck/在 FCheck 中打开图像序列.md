# 在 FCheck 中打开图像序列

**注**

重要：

自 Maya 2020 起，FCheck 在 macOS 上不再受支持。可以在

应用程序首选项

（

“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)

）中选择其他默认图像查看器。

使用 -n 打开动画

1. -n 选项可用来打开动画，同时指定开始和结束帧、以及帧间隔。

2. “FCheck”关闭后，将会打开命令提示窗口。

3. 确定用来打开动画需要的开始帧、结束帧和帧间隔。

4. 找到动画的文件名格式。

  请参见[用于打开文件的惯例](帧编号和填充式数字.md#WS17956D7ADBC6E7365228C7F8117AE33CB28-7FF7)，以了解“FCheck”如何指定打开文件的填充编号。

5. 输入下列命令：

  ```text
fcheck -n <start> <end> <interval> <filename>
```

  <start> 是进行加载的第一个帧的编号。

  <end> 是进行加载的最后一帧的编号。

  <interval> 是加载方式的间隔步骤。

  <filename> 是序列文件名。文件名必须符合[用于打开文件的惯例](帧编号和填充式数字.md#WS17956D7ADBC6E7365228C7F8117AE33CB28-7FF7)中设定的准则。

6. 按 Enter 键。

  “FCheck 播放”(FCheck Playback)窗口将根据所输入的说明显示动画。

创建无关联图像序列。

1. 使用 -s 选项，可以显示无关联图像列表。

2. “FCheck”关闭后，将会打开命令提示窗口。

3. 确定要创建成序列的图像。

4. 类型：

  ```text
fcheck -S <filename1> <filename2> <filename3>...
```

  其中,<filename1,2,3...> 表示要在“FCheck”中显示为序列的图像。列表中的第一个图像为开始帧，最后一个图像为结束帧。

  “FCheck 播放”(FCheck Playback)窗口将会出现，并显示所示的序列。
