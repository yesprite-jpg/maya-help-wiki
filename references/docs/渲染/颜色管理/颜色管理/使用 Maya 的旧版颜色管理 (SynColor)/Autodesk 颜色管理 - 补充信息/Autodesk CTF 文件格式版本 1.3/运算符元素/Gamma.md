# Gamma

Gamma 元素对颜色值应用 Gamma 校正。

它是 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。

## 引入

版本 1.2。

## 包含

- [Description](../元数据元素/Description.md)。可选，任意数量。

- [GammaParams](Gamma/GammaParams.md)。必需，最多总计三个。

- [DynamicParameter](DynamicParameter.md)。可选，至多一个。param 属性必须设置为 "DEFAULT_LOOK"。

## 包含于

- [ProcessList](../ProcessList.md)

## 属性

#### id、name、bypass、inBitDepth、outBitDepth

请参见[通用运算符属性](通用运算符属性.md)。

#### style

指定幂律曲线的类型。必需。

**注**

以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换句话说，存储在 CTF 文件中的 Gamma 和偏移值不取决于输入和输出位深度。

| 值 | 含义 |
|---|---|
| "basicFwd" | 应用幂律和 GammaParams 元素中指定的 Gamma 值。GammaParams 元素不得具有 offset 属性。 ![图：应用幂律和 GammaParams 元素中指定的 Gamma 值。GammaParams 元素不得具有 offset 属…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-38995511-B300-485C-96BF-08FFB70D5B26.png) <!-- baize:img-hook downloaded=false reason="正文 1048 字 ≥300，非承重" --> |
| "basicRev" | 应用幂律和反向 Gamma 值。GammaParams 元素不得具有 offset 属性。 ![图：应用幂律和反向 Gamma 值。GammaParams 元素不得具有 offset 属性。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-75FC738E-514F-48E6-9658-6601DE8AC06B.png) <!-- baize:img-hook downloaded=false reason="正文 1048 字 ≥300，非承重" --> |
| "moncurveFwd" | 应用一个函数，该函数在原点（黑色）附近具有线性分段，在较高值处具有幂律分段。连接时，该曲线在值和切线处是连续的。此类型曲线在 Rec. 709、sRGB 和 CIE L* 方程式中使用。 GammaParams 元素必须具有 offset 属性。 ![图：应用一个函数，该函数在原点（黑色）附近具有线性分段，在较高值处具有幂律分段。连接时，该曲线在值和切线处是连续的。此类型曲…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-C6C0C9EF-BABB-40C2-81C8-157E1F9CDB84.png) <!-- baize:img-hook downloaded=false reason="正文 1048 字 ≥300，非承重" --> |
| "moncurveRev" | 应用一个函数，该函数在原点（黑色）附近具有线性分段，在较高值处具有反向幂律分段。GammaParams 元素必须具有 offset 属性。 ![图：应用一个函数，该函数在原点（黑色）附近具有线性分段，在较高值处具有反向幂律分段。GammaParams 元素必须具有 o…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-8F1D0B50-B79F-4470-BE5E-CB3151F9B713.png) <!-- baize:img-hook downloaded=false reason="正文 1048 字 ≥300，非承重" --> |

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
