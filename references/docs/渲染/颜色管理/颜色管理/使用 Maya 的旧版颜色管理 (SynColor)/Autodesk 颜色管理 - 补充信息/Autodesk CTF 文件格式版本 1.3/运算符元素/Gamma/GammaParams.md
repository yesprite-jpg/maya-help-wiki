# GammaParams

GammaParams 元素定义 Gamma 元素的 Gamma 值和可选偏移。

它是 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。

## 引入

版本 1.2。

## 包含

无内容。

## 包含于

- [Gamma](../Gamma.md)

## 属性

#### channel

要应用 Gamma 校正的颜色通道。可能的值包括“R”、“G”和“B”。可选。

如果未指定此属性，则 Gamma 校正将应用于所有通道。

#### gamma

要使用的强度值。有效值的范围是 0.1 到 10.0（含）。必需。

#### offset

要使用的偏移。有效值的范围是 10–6 到 0.9（含）。可选。

如果使用此属性，Gamma 元素的 style 属性应设置为 "moncurveFwd" 或 "moncurveRev"。如果不使用，style 属性应为 "basicFwd" 或 "basicRev"。

## 示例

### 无偏移

```text
<ProcessList id="9e999646-3e76-4374-814c-e4c46c6438de" version="1.2">
    </Matrix>
    <Gamma inBitDepth="32f" outBitDepth="12i" style="basicRev">
        <GammaParams gamma="2.400000000000000" />
    </Gamma>
</ProcessList>
```

### 有偏移

```text
<ProcessList id="1b86aac2-1fdb-4dd8-bc6b-54f3551b9bd4" version="1.2">
    <Gamma inBitDepth="32f" outBitDepth="32f" style="moncurveFwd">
        <GammaParams gamma="2.600000000000000" offset="0.050000" />
    </Gamma>
</ProcessList>
```

### 单独通道

```text
<ProcessList id="id">
    <Gamma inBitDepth="32f" outBitDepth="10i" style="basicRev">
       <GammaParams channel="R" gamma="2.4" />
        <GammaParams channel="G" gamma="2.35" />
        <GammaParams channel="B" gamma="2.2" />
    </Gamma>
</ProcessList>
```
