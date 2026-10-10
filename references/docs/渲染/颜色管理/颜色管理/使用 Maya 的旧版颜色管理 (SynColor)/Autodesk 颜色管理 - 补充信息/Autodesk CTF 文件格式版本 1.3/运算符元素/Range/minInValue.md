# minInValue

MinValue 元素指定 Range 元素的最小输入值。

## 包含

- 用于所有通道的单个数值。

## 包含于

- [Range](../Range.md)

## 属性

无。

## 示例

```text
<ProcessList id="7f5b1560-fec4-4603-aa8d-c55bf5e22280" version="1.2">
    <Description>10-bit full range to SMPTE (legal) range.</Description>
    <InputDescriptor>generic RGB</InputDescriptor>
    <OutputDescriptor>generic RGB</OutputDescriptor>
    <Range inBitDepth="10i" outBitDepth="10i">
        <minInValue>  0.0000</minInValue>
        <maxInValue>1023.0000</maxInValue>
        <minOutValue> 64.0000</minOutValue>
        <maxOutValue>940.0000</maxOutValue>
    </Range>
</ProcessList>
```
