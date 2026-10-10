# Log

Log 运算符应用对数或反对数函数，在线性和 Cineon 样式编码之间转化。

它是 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。

## 引入

版本 1.3。

## 包含

- [Description](../元数据元素/Description.md)。可选，任意数量。

- [LogParams](Log/LogParams.md)。如果 style 属性为 "logToLin" 或 "linToLog"，则必需。如果值应用于所有 RGB 通道，应出现 1 次，或者如果不同的值分别应用于 R、G 和 B，则应出现 3 次。

- [DynamicParameter](DynamicParameter.md)。可选，至多一个。param 属性必须设置为 "DEFAULT_LOOK"。

## 包含于

[ProcessList](../ProcessList.md)

## 属性

#### id、name、bypass、inBitDepth、outBitDepth

请参见[通用运算符属性](通用运算符属性.md)。

#### style

指定用于转化的公式。必需。

**注**

以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换句话说，存储在 CTF 文件中的 Gamma、基准白色、基准黑色、高光和阴影值不取决于输入和输出位深度。

在以下方程式中：

![图：指定用于转化的公式。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-DD219FEA-AF0E-4E57-9E10-C71DBCE3142A.png) <!-- baize:img-hook downloaded=false reason="正文 1155 字 ≥300，非承重" -->

![图：指定用于转化的公式。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-BF8C75DE-82EC-4596-82B1-A4DE73852079.png) <!-- baize:img-hook downloaded=false reason="正文 1155 字 ≥300，非承重" -->

![图：指定用于转化的公式。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-15EC79E6-8B23-4D4A-B5FB-37822D9F0AEA.png) <!-- baize:img-hook downloaded=false reason="正文 1155 字 ≥300，非承重" -->

| 值 | 含义 |
|---|---|
| "log10" | ![图：指定用于转化的公式。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-B27A5BA8-AAD2-46AE-B564-9DC2E4F56BA8.png) <!-- baize:img-hook downloaded=false reason="正文 1155 字 ≥300，非承重" --> |
| "log2" | ![图：指定用于转化的公式。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-C79B9659-96C9-4F5A-A935-D0B4BE6E48DA.png) <!-- baize:img-hook downloaded=false reason="正文 1155 字 ≥300，非承重" --> |
| "antiLog10" | ![图：指定用于转化的公式。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-AB2939B1-D3E9-43CE-BB40-8DB390DD18DC.png) <!-- baize:img-hook downloaded=false reason="正文 1155 字 ≥300，非承重" --> |
| "antiLog2" | ![图：指定用于转化的公式。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-5C9F8041-2906-4085-ABD6-03F7BABDEB01.png) <!-- baize:img-hook downloaded=false reason="正文 1155 字 ≥300，非承重" --> |
| "logToLin" | ![图：指定用于转化的公式。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-F2D1827D-33AA-4935-B59F-6E953DBBE14F.png) <!-- baize:img-hook downloaded=false reason="正文 1155 字 ≥300，非承重" --> ![图：指定用于转化的公式。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4BBCF8A1-0B30-42F7-B30B-AB9266EBA5F4.png) <!-- baize:img-hook downloaded=false reason="正文 1155 字 ≥300，非承重" --> |
| "linToLog" | ![图：指定用于转化的公式。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4869A894-8439-4C01-A487-85B58FA50D56.png) <!-- baize:img-hook downloaded=false reason="正文 1155 字 ≥300，非承重" --> ![图：指定用于转化的公式。必需。 注： 以下方程式假定输入和输出位深度是浮点。对于整数，值已归一化为 [0.0, 1.0]。换…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-2F6494B1-8F7B-4240-81DD-5E4B7E491881.png) <!-- baize:img-hook downloaded=false reason="正文 1155 字 ≥300，非承重" --> |

## 示例

### 所有通道

```text
<ProcessList id="19510ea6-69a0-4d3d-bc75-d0b36d458f62" name="Log op 1" version="1.3">
     <Log inBitDepth="16f" outBitDepth="12i" style="linToLog">
        <LogParams gamma="0.6" refWhite="685" refBlack="95" highlight="1.0" shadow="0.0005"/>
    </Log>
</ProcessList>
```

### 单独通道

```text
<ProcessList id="19510ea6-69a0-4d3d-bc75-d0b36d458f62" name="Log op 1" version="1.3">
     <Log inBitDepth="16f" outBitDepth="12i" style="linToLog">
        <LogParams channel="R" gamma="0.5" refWhite="685" refBlack="95" highlight="1.0" shadow="0.0005"/>
        <LogParams channel="G" gamma="0.6" refWhite="685" refBlack="95" highlight="1.0" shadow="0.0005"/>
        <LogParams channel="B" gamma="0.65" refWhite="685" refBlack="95" highlight="1.0" shadow="0.0005"/>
    </Log>
</ProcessList>
```
