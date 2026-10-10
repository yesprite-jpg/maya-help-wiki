# 启动“FCheck”

在 Windows 上启动“FCheck”

1. 执行下列操作之一：

  - 从“开始”(Start)菜单中选择“开始 > 程序 > Autodesk > Autodesk Maya > FCheck”(Start > Programs > Autodesk > Autodesk Maya > FCheck)。

  - 打开 <驱动器>\Program Files\Autodesk\Maya<*版本*>\bin 文件夹，然后双击 FCheck 应用程序。

  - 打开命令提示，然后输入 fcheck。

  将显示“FCheck 播放”(FCheck Playback)窗口和命令提示窗口。

在 Linux 上启动“FCheck”

1. 在壳窗口中，键入 FCheck，后跟要显示的图像的名称：

  ```text
fcheck -<option> myimage
```

  有关选项列表，请参见 [FCheck 选项列表](../渲染工具参考/渲染工具窗口和编辑器/FCheck%20引用/FCheck%20选项列表.md)

  通过使用通配符（即，*）可以一次显示多个图像。输入以下内容，以显示其名称以字符 mytest 开头的所有图像：

  ```text
fcheck mytest*
```

  每个图像将显示在一个单独的窗口中。

  对于动画，可以使用点扩展名 (.) 和“FCheck”自动查找序列的开始值、结束值和步长值。输入以下内容，以在单个窗口中显示名称以字符 mysequence 开头的所有图像：

  ```text
fcheck mysequence.
```

  在 Linux 上，必须指定要打开的文件。

  有关将命令行与序列文件名一起使用的信息，请参见[用于打开文件的惯例](帧编号和填充式数字.md#WS17956D7ADBC6E7365228C7F8117AE33CB28-7FF7)。

**注**

自 Maya 2020 起，FCheck 在 macOS 上不再受支持。可以在

应用程序首选项

（

“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)

）中选择其他默认图像查看器。
