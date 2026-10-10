# Saturation

Saturation 元素定义 ASC CDL 颜色变换的饱和度函数所使用的值。

它是 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。

## 引入

版本 1.3。

## 包含

应用于所有颜色通道的单个十进制值。

## 包含于

- [SatNode](../SatNode.md)

## 属性

无。

## 示例

```text
<ProcessList version="1.3" id="7b42c76a-8c7a-4142-8b6e-1c467084075a">
    <ASC_CDL id="cc01234" inBitDepth="16f" outBitDepth="16f" style="v1.2_Fwd">
        <Description>scene 1 exterior look</Description>
        <SOPNode>
            <Slope>1.000000  1.000000  0.900000</Slope>
            <Offset>-0.030000  -0.020000  0.000000</Offset>
            <Power>1.2500000  1.000000  1.000000</Power>
        </SOPNode>
        <SatNode>
            <Saturation>1.700000</Saturation>
        </SatNode>
    </ASC_CDL>
</ProcessList>
```
