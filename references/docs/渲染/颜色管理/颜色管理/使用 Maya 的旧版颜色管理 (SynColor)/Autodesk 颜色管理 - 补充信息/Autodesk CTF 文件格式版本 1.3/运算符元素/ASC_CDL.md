# ASC_CDL

ASC_CDL 运算符表示美国电影摄影师协会的颜色确定表格式（*.ccc 或 *.cdl）的颜色变换。

ASC CDL 变换由分别应用于每个 RGB 通道的 slope-offset-power (SOP) 函数组成，后跟同等应用于所有通道的饱和度函数。

它是 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。

## 引入

版本 1.3。

## 包含

- [Description](../元数据元素/Description.md)。可选，任意数量。

- [SOPNode](ASC_CDL/SOPNode.md)。可选，至多一个。如果不存在，则不应用任何 slope-offset-power 函数。

- [SatNode](ASC_CDL/SatNode.md)。可选，至多一个。如果不存在，则不应用任何饱和度函数。

- [DynamicParameter](DynamicParameter.md)。可选，至多一个。param 属性必须设置为 "DEFAULT_LOOK"。

## 包含于

- [ProcessList](../ProcessList.md)

## 属性

#### id、name、bypass、inBitDepth、outBitDepth

请参见[通用运算符属性](通用运算符属性.md)。

#### style

确定该运算符应用的公式。

**注**

方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换句话说，存储在 CTF 文件中的渐变、偏移、强度和饱和度值不取决于输入和输出位深度。

**注**

亮度权重假设图像使用由 Rec. 709 指定的主颜色（例如，HD 和 sRGB）。

| 值 | 含义 |
|---|---|
| "v1.2_Fwd" | ![图：确定该运算符应用的公式。 注： 方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换句话说…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-5974DC92-65AE-4760-8155-34CC1891E079.png) <!-- baize:img-hook downloaded=false reason="正文 1031 字 ≥300，非承重" --> ![图：确定该运算符应用的公式。 注： 方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换句话说…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-5A1A322A-F2A1-41E5-9E40-C0E9CA6E8079.png) <!-- baize:img-hook downloaded=false reason="正文 1031 字 ≥300，非承重" --> ![图：确定该运算符应用的公式。 注： 方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换句话说…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-BF519943-654D-4D05-86AF-AEC069EAA811.png) <!-- baize:img-hook downloaded=false reason="正文 1031 字 ≥300，非承重" --> |
| "v1.2_Rev" | "v1.2_Fwd" 的反向值。 |
| "noClampFwd" | 与 "v1.2_Fwd" 相同，但没有两个钳制函数。如果 ![图：与 "v1.2_Fwd" 相同，但没有两个钳制函数。如果 则不应用强度函数。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-E3FCF872-3208-4070-BDD2-0E163245DFEB.png) <!-- baize:img-hook downloaded=false reason="正文 1031 字 ≥300，非承重" --> 则不应用强度函数。 |
| "noClampRev" | "noClampFwd" 的反向值。 |

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
