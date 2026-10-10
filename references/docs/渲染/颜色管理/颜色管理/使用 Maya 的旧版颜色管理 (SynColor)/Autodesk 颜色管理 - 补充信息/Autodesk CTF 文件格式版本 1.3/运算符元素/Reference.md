# Reference

Reference 元素按路径或别名引用其他 CTF 文件。将外部文件导入到 ProcessList 的相应位置。

它是 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。

**注**

当导出包含 Reference 元素的变换链时，该引用将由引用文件的内容替代。

## 引入

版本 1.2。

## 包含

- [Description](../元数据元素/Description.md)。可选，任意数量。

- [DynamicParameter](DynamicParameter.md)。可选，至多一个。param 属性必须设置为 "DEFAULT_LOOK"。

## 包含于

- [ProcessList](../ProcessList.md)

## 属性

需要指定 path 或 alias 属性，其中之一即可。

#### id、name、bypass、inBitDepth、outBitDepth

请参见[通用运算符属性](通用运算符属性.md)。

请注意，此处指定的值将覆盖外部文件中的值。

#### alias

其他 CTF 文件的路径和文件名的简称。别名必须在 [SynColor 配置文件](../../SynColor%20配置文件.md)的 [Ref](../../SynColor%20配置文件/ReferenceTable/Ref.md) 元素中定义。默认情况下，以下别名可用，并且可以从支持 Autodesk 颜色管理的一些应用程序的用户界面中更改：

- "graphicsMonitor" 别名应引用适合在工作站显示器上显示的变换。

- "broadcastMonitor" 别名应引用适合在广播显示器上显示的变换。

- 根据图像显示的位置，"currentMonitor" 别名会解析为 "graphicsMonitor" 别名的值或 "broadcastMonitor" 别名的值。

- "defaultLook" 别名应引用重新创建在现场使用的外观的变换。

您可以根据需要创建其他别名。

#### path

其他 CTF 文件的路径和文件名。如果定义 basePath 属性，那么路径相对于该属性；否则，就是绝对路径。

#### basePath

相对路径的基点位置。

| 值 | 含义 |
|---|---|
| Autodesk | Autodesk 应用程序随附的颜色变换的安装位置。基于运行的应用程序使用的 Autodesk 颜色管理的版本，解析精确路径。 |
| Shared | 使用 Autodesk 颜色管理的任何应用程序的自定义颜色变换的共享位置。位置在 [SynColor 配置文件](../../SynColor%20配置文件.md)的 [SharedHome](../../SynColor%20配置文件/SharedHome.md) 中设置。 |

## 示例

```text
<ProcessList id="561c5aba-8709-477c-8211-7ec4a6fe8820">
    <Reference basePath="Autodesk" inBitDepth="32f" outBitDepth="32f" path="RRT+ODT/ACES_to_CIE-XYZ_v0.1.1.ctf" />
    <Reference alias="graphicsMonitor" inBitDepth="32f" outBitDepth="8i" />
    <Reference inBitDepth="8i" outBitDepth="8i" path="lut1d_example.xml" basePath="Shared" />
    <Reference inBitDepth="8i" outBitDepth="8i" path="/zeus/toto/toto.xml" />
</ProcessList>
```
