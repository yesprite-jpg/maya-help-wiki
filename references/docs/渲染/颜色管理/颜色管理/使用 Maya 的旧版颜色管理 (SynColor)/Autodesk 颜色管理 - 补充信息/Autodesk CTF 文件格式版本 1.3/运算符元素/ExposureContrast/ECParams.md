# ECParams

ECParams 元素指定 ExposureContrast 元素的参数。

它是 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。

## 引入

版本 1.2。

## 包含

无内容。

## 包含于

- [ExposureContrast](../ExposureContrast.md)

## 属性

#### exposure

单个十进制值，用于表示光圈中的曝光偏移。值 0.0 对应于无曝光偏移。必需。

#### contrast

单个十进制值，用于表示对比度级别。值 1.0 对应于无对比度调整。必需。

#### pivot

单个十进制值，用于表示用作调整对比度的枢轴的颜色值。值 0.18 会以中灰为枢轴。必需。

## 示例

```text
<ProcessList id="561c5aba-8709-477c-8211-7ec4a6fe8820">
   <ExposureContrast inBitDepth="16f" outBitDepth="32f" style="linear">
      <ECParams exposure="0.65" contrast="1.2" pivot="1" />
      <DynamicParameter param="EXPOSURE" />
      <DynamicParameter param="CONTRAST" />
   </ExposureContrast>
</ProcessList>
```
