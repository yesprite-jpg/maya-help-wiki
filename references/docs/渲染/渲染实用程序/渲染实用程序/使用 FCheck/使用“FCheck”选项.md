# 使用“FCheck”选项

**注**

重要：

自 Maya 2020 起，FCheck 在 macOS 上不再受支持。可以在

应用程序首选项

（

“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)

）中选择其他默认图像查看器。

使用命令行执行“FCheck”选项。在执行“FCheck”时，选项将输入至命令提示窗口/壳中。

**注**

关闭该窗口后，“FCheck”

不保存您设定的选项。您必须将图像保存到磁盘，以保留在

“FCheck”

中执行的图像修改和调整。请参见

保存图像或序列

。

输入命令行的标准约定如下所示：

fcheck -<option> <spec> myimage.ext

#### <option>

“FCheck”选项字母。请参见 [FCheck 选项列表](../渲染工具参考/渲染工具窗口和编辑器/FCheck%20引用/FCheck%20选项列表.md)。

#### <spec>

选项特定的参数。

#### myimage.ext

要加载的文件的名称。必须在命令提示的当前目录中打开文件。在 Linux 上，必须在命令行中包含文件名。 使用 Windows 时，可以在命令行中省去文件名。

例如：

```text
fcheck -r 15
```

其中 r 指定帧速率选项，15 是每秒的帧数。

可以使用以下约定，将某些选项组合在一个命令中：

```text
fcheck -<option> <spec> -<option> <spec> ... myimage.ext
```

例如，

```text
fcheck -B -G 1 -r 15 myimage.ext
```

其中：

-B 在图像周围启用边界。

-G 1 将 Gamma 值设置为 1。

-r 15 将帧速率设置为每秒 15 帧。

有关选项列表的完整描述，请参见 [FCheck 选项列表](../渲染工具参考/渲染工具窗口和编辑器/FCheck%20引用/FCheck%20选项列表.md)。
