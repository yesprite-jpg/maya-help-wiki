# Array (LUT1D)

Array 元素指定 LUT 或矩阵的值数组。当 Array 元素包含在 LUT1D 元素中时，其内容的格式与包含在 LUT3D 或 Matrix 元素中时的格式不同。

## 包含

- 指定 LUT 输出值的一系列数值。相应的输入值由包含元素的 [inBitDepth](../通用运算符属性.md) 指示。对于整数，第一个值对应于输入值 0，最后一个值对应于输入值 (2bitdepth – 1)。对于浮点数，第一个值对应于输入值 0.0，最后一个值对应于输入值 1.0。超出这些域的输入值将被钳制。

  输入值之间的间隔是均匀的，并且取决于条目数。例如，如果有 5 个浮点条目，则它们对应于输入值 0.0、0.25、0.5、0.75 和 1.0。

  对于 1D LUT，每个条目有一个值，用于所有颜色通道。对于 3×1D LUT，每个条目有三个值，用于指定单独的 R、G 和 B 输出值。

## 包含于

- [LUT1D](../LUT1D.md)

## 属性

#### dim

表示数组维度的两个整数。第一个值是 Array 元素内容中的条目数。第二个值是每个条目中值的数量：1 表示将单个值应用于所有通道，3 表示将单独的值分别应用于 R、G 和 B 通道。

dim 是必需属性，并且其值必须匹配实际存在的条目数。

## 示例

### 1D LUT

```text
<ProcessList id="8a52d5fb-a903-4805-8bae-24f7553bfb70" version="1.2">
    <LUT1D inBitDepth="10i" outBitDepth="32f">
        <Array dim="1024 1">
-0.014279292
-0.014160193
-0.014040368
<!-- 1021 values omitted -->

        </Array>
    </LUT1D>
</ProcessList>
```

### 3×1D LUT

```text
<ProcessList id="a76dbe2e-e610-49a6-8c3b-5962375a8b4a" version="1.2">
    <LUT1D inBitDepth="16i" outBitDepth="32f">
        <Array dim="2 3">
 -0.092903227  -0.092903227  -0.092903227
 11.798709869  11.798709869  11.798709869
        </Array>
    </LUT1D>
 </ProcessList>
```

## 另请参见

- [Array (LUT3D)](../LUT3D/Array%20%28LUT3D%29.md)

- [Array（矩阵）](../Matrix/Array（矩阵）.md)
