# DynamicParameter

DynamicParameter 元素向兼容应用程序发送信号指示某个参数是动态的。如果变换用于显示，则 CTF 文件中定义的参数值将被忽略，而改用应用程序中设置的值。

它是 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。

## 更新

版本 1.3。

## 包含

无内容。

## 包含于

- 任何运算符元素 (LOOK_SWITCH)

- [ExposureContrast](ExposureContrast.md) (EXPOSURE, CONTRAST)。

## 属性

#### param

指定在 CTF 文件应用于显示时，将被应用程序覆盖的参数。

| 值 | 含义 |
|---|---|
| "EXPOSURE" | 当变换用于支持此功能的应用程序中的显示时，可以覆盖曝光值。 仅当 DynamicParameter 元素是 [ExposureContrast](ExposureContrast.md) 元素的子对象时，此值才可用。 |
| "CONTRAST" | 当变换用于支持此功能的应用程序中的显示时，可以覆盖对比度值。 仅当 DynamicParameter 元素是 [ExposureContrast](ExposureContrast.md) 元素的子对象时，此值才可用。 |
| "LOOK_SWITCH" | 当变换用于支持此功能的应用程序中的显示时，可以打开和关闭运算符的效果。 它可以与父元素的 [bypass](通用运算符属性.md) 属性结合使用，以创建永远不会影响渲染到文件的值但仍可针对显示打开和关闭的运算符。 版本 1.3 中引入。 |

## 示例

```text
<ProcessList id="561c5aba-8709-477c-8211-7ec4a6fe8820">
    <ExposureContrast inBitDepth="16f" outBitDepth="16f" style="linear">
        <ECParams contrast="1.0000" exposure="0.0000" pivot="0.1800" />
        <DynamicParameter param="EXPOSURE" />
        <DynamicParameter param="CONTRAST" />
    </ExposureContrast>
    <Reference basePath="Autodesk" inBitDepth="16f" outBitDepth="16f" path="misc/default_look-ACESproxy.ctf" bypass="true">
        <DynamicParameter param="LOOK_SWITCH" />
    </Reference>
    <Reference basePath="Autodesk" inBitDepth="16f" outBitDepth="16f" path="RRT+ODT/ACES_to_CIE-XYZ_v0.1.1.ctf" />
    <Reference alias="currentMonitor" inBitDepth="16f" outBitDepth="10i" />
<</ProcessList>
```
