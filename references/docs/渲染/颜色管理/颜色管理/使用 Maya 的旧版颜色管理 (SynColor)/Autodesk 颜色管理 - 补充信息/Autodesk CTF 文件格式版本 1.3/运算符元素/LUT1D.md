# LUT1D

LUT1D 元素指定要应用的 1D LUT。

## 包含

- [Description](../元数据元素/Description.md)。可选，任意数量。

- [Array (LUT1D)](LUT1D/Array%20%28LUT1D%29.md)。必需，仅一个。

- [DynamicParameter](DynamicParameter.md)。可选，至多一个。param 属性必须设置为 "DEFAULT_LOOK"。

**注**

IndexMap 元素不受支持。获得相同结果的最有效方法是在运算符之前使用其他 LUT1D 元素，或者将两个 LUT 合并为一个。

## 包含于

- [ProcessList](../ProcessList.md)

## 属性

#### id、name、bypass、inBitDepth、outBitDepth

请参见[通用运算符属性](通用运算符属性.md)。

#### interpolation

可选。当前唯一支持的值是 "linear"。

#### halfDomain

可选。如果此属性存在，其值必须为 "true"。在这种情况下，输入域为所有可能的 16 位浮点值，并且 Array 元素中必须精确包含 65536 个条目。例如，无符号整数 15360 与半浮点值 1.0 具有相同的位模式 (0011110000000000)，因此 Array 元素中第 15360 个条目（零索引）是对应于输入值 1.0 的输出值。

#### rawHalfs

可选。如果此属性存在，其值必须为 "true"。在这种情况下，数组中的值应为 16 位浮点值，以表示等效位模式的无符号 16 位整数表示。例如，若要表示值 1.0，您需要在 Array 元素中输入整数 15360，因为它具有相同的位模式。这允许您指定所需的精确半浮点值，而不必依赖从十进制文本字符串进行转化。

## 示例

### 1D LUT

```text
<ProcessList id="8a52d5fb-a903-4805-8bae-24f7553bfb70" version="1.2">
    <LUT1D inBitDepth="10i" outBitDepth="32f">
        <Array dim="1024 1">
-0.014279292
-0.014160193
-0.014040368
<!-- 1021 lines omitted -->

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
