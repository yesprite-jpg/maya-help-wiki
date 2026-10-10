# Info

Info 元素是 Copyright 和 Release 元素的容器。

它是 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。

## 引入

版本 1.2。

## 包含

按任意顺序：

- [Copyright](Info/Copyright.md)。可选，至多一个。

- [Release](Info/Release.md)。可选，至多一个。

## 包含于

- [ProcessList](../ProcessList.md)

## 属性

无。

## 示例

```text
<ProcessList id="f8d905db-4ab8-4af6-8465-0db81f7e993c" version="1.2">
    <Info>
        <Copyright>Copyright 2012 Autodesk, Inc.  All rights reserved.</Copyright>
        <Release>2013.1.pr20</Release>
    </Info>
    <Description>F65 Raw integer code values to scene-linear floats with Rec 709 primaries.</Description>
    <InputDescriptor>16-bit integer F65 Raw</InputDescriptor>
    <OutputDescriptor>scene-linear Rec 709 primaries</OutputDescriptor>
    <LUT1D inBitDepth="16i" outBitDepth="32f">
        <Array dim="2 3">
 -0.092903227  -0.092903227  -0.092903227
 11.798709869  11.798709869  11.798709869
        </Array>
    </LUT1D>
    <Matrix inBitDepth="32f" outBitDepth="32f">
        <Array dim="3 3 3">
 1.8779151440 -0.7941687703 -0.0837463662
-0.1768069863  1.3509995937 -0.1741926372
-0.0262011271 -0.1484222561  1.1746233702
        </Array>
    </Matrix>
</ProcessList>
```
