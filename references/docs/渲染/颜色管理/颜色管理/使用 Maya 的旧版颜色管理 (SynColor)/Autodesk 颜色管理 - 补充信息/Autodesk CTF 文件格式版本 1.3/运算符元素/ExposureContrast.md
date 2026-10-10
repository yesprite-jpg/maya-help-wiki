# ExposureContrast

ExposureContrast 元素可模拟调整图像的曝光，并修改浅色和深色之间的对比度。

它是 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。

如果颜色变换用于显示，则根据应用程序，用户仍可以交互方式调整曝光和对比度，只要 CTF 文件至少包含一个带有 DynamicParameter 子元素的 ExposureContrast 元素。在这种情况下，将仅在显示中忽略在 ECParams 子元素中定义的相应参数值，而是在变换链中出现带有 DynamicParameter 子元素的 ExposureContrast 元素的每个点应用应用程序中设置的值。

## 引入

版本 1.2。

## 包含

- [Description](../元数据元素/Description.md)。可选，任意数量。

- [ECParams](ExposureContrast/ECParams.md)。必需，仅一个。

- [DynamicParameter](DynamicParameter.md)。可选，最多 3 个。每个 param 属性必须设置为不同的值。

## 包含于

- [ProcessList](../ProcessList.md)

## 属性

#### id、name、bypass、inBitDepth、outBitDepth

请参见[通用运算符属性](通用运算符属性.md)。

#### style

声明输入数据类型。必需。

**注**

以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换句话说，存储在 CTF 文件中的曝光偏移、对比度级别和枢轴值不取决于输入和输出位深度。

| 值 | 含义 |
|---|---|
| "linear" | ![图：声明输入数据类型。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换句…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-476BA7F1-B6E7-41D2-B9F0-89BCBB6D863F.png) <!-- baize:img-hook downloaded=false reason="正文 822 字 ≥300，非承重" --> |
| "video" | ![图：声明输入数据类型。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换句…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-25C6FBBB-70AB-440D-8053-01FF1DECAEB1.png) <!-- baize:img-hook downloaded=false reason="正文 822 字 ≥300，非承重" --> |
| "log" | ![图：声明输入数据类型。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换句…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-B688EAA9-0CC8-48CA-8A36-FEB0E65CB05B.png) <!-- baize:img-hook downloaded=false reason="正文 822 字 ≥300，非承重" --> |

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
