# ProcessList

ProcessList 元素是 CTF 文件的根元素。它必须至少包含一个运算符元素。

## 包含

按顺序：

- [Info](元数据元素/Info.md)。可选，至多一个。

- [Description](元数据元素/Description.md)。可选，任意数量。

- [InputDescriptor](元数据元素/InputDescriptor.md)。可选，至多一个。

- [OutputDescriptor](元数据元素/OutputDescriptor.md)。可选，至多一个。

- 至少有一个或多个运算符元素，按照应用顺序任意组合。

  **注**

  每个运算符的 inBitDepth 属性必须与链中上一个运算符的 outBitDepth 属性匹配。请参见

  通用运算符属性

  。

## 包含于

- 没有父对象

## 属性

#### id

唯一标识符（必需）。

#### name

整个颜色变换的别名（可选）。这用于支持 Autodesk 颜色管理的应用程序中的显示和选择。

#### version

表示存在 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。值高于应用程序支持的值的文件将被拒绝。

#### inverseOf

来自其他 CTF 文件的 id 属性。该属性将此变换标识为另一个变换的反向变换。此信息有助于颜色管理系统检测应用变换然后应用其反向变换的情况，因此变换对可能会被优化。它是 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。

## 示例

```text
<ProcessList id="7214fa79-6c42-48b9-b164-3d0c5e543fe0" version="1.2">
    <Description>F65 Raw integer code values to ACES (tungsten illuminant).</Description>
    <InputDescriptor>16-bit integer F65 Raw</InputDescriptor>
    <OutputDescriptor>Academy Color Encoding Specification (ACES)</OutputDescriptor>
    <LUT1D inBitDepth="16i" outBitDepth="32f">
        <Array dim="2 3">
 -0.092903227  -0.092903227  -0.092903227
 11.798709869  11.798709869  11.798709869
        </Array>
    </LUT1D>
    <Matrix inBitDepth="32f" outBitDepth="32f">
        <Array dim="3 3 3">
 1.0110238791 -0.1362526119  0.1252287328
 0.1011994481  0.9562196136 -0.0574190766
 0.0600766540 -0.1010185331  1.0409418344
        </Array>
    </Matrix>
</ProcessList>
```
