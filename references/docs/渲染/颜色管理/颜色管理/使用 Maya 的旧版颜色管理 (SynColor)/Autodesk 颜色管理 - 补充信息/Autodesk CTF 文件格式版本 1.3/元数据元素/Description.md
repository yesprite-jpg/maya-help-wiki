# Description

Description 元素可用于添加有关 ProcessList 或运算符元素的函数或者用法的信息。它会显示在支持 Autodesk 颜色管理的产品的颜色变换的元数据面板中。

## 包含

  文本字符串。使用 &gt; 表示 >；使用 &lt; 表示 <；使用 &amp; 表示 &。

## 包含于

- [ProcessList](../ProcessList.md)

- [LUT1D](../运算符元素/LUT1D.md)

- [LUT3D](../运算符元素/LUT3D.md)

- [矩阵](../运算符元素/Matrix.md)

- [Range](../运算符元素/Range.md)

- [ExposureContrast](../运算符元素/ExposureContrast.md)

- [Gamma](../运算符元素/Gamma.md)

- [引用(Reference)](../运算符元素/Reference.md)

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
