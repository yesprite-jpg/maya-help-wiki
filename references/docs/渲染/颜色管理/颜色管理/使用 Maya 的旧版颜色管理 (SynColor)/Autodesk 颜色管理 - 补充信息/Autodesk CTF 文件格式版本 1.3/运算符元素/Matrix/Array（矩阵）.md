# Array（矩阵）

Array 元素指定 LUT 或矩阵的值数组。当 Array 元素包含在 Matrix 元素中时，其内容的格式与包含在 LUT1D 或 LUT3D 元素中时的格式不同。

## 更新

版本 1.3。

## 包含

- 指定矩阵元素的一系列数值。

  在矩阵中，这些数值指定从左到右、从上到下，逐行序列化的矩阵条目。数组值的缩放取决于输入和输出位深度。出于相乘目的，将颜色值视为列向量。

  数组值的缩放取决于输入和输出位深度。例如，如果输入深度为 10i，输出深度为 12i，则在主对角线和条目 0 的任意其他位置上包含条目 4095/1023 的矩阵为身份变换。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-8B6A24AB-BD27-43EA-B0DD-E8EBED2F0504.png) <!-- baize:img-hook downloaded=false reason="正文 1134 字 ≥300，非承重" -->![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-0DED02AE-3ACC-43FA-AE61-433C1D1C883F.png) <!-- baize:img-hook downloaded=false reason="正文 1134 字 ≥300，非承重" -->

3×3 矩阵相乘

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-793A4E2F-1935-4DC0-B05F-DCDD758191E4.png) <!-- baize:img-hook downloaded=false reason="正文 1134 字 ≥300，非承重" -->![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-B07AAF20-DD36-4BBD-A311-51DAC8DBCA3D.png) <!-- baize:img-hook downloaded=false reason="正文 1134 字 ≥300，非承重" -->

3×4 矩阵相乘

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-0C0BAF04-820C-46CD-B5D6-53D2A5461CE4.png) <!-- baize:img-hook downloaded=false reason="正文 1134 字 ≥300，非承重" -->![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-82C912DD-B0E1-4D2B-8C63-107D61B387A8.png) <!-- baize:img-hook downloaded=false reason="正文 1134 字 ≥300，非承重" -->

4×4 矩阵相乘

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-567DDC54-344A-42EC-BD69-004F102C01B8.png) <!-- baize:img-hook downloaded=false reason="正文 1134 字 ≥300，非承重" -->![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-AE8537A8-F175-41F7-9CDB-4E701AFB7D67.png) <!-- baize:img-hook downloaded=false reason="正文 1134 字 ≥300，非承重" -->

4×5 矩阵相乘

## 包含于

- [矩阵](../Matrix.md)

## 属性

#### dim

指定矩阵大小和对其进行操作的通道数量。

| 值 | 含义 |
|---|---|
| "3 3 3" | 对 RGB 值进行操作的 3×3 矩阵。 |
| "3 4 3" | 对 RGB 值进行操作的 3×4 矩阵。 版本 1.3 中引入。 |
| "4 4 4" | 对 RGBA 值进行操作的 4×4 矩阵。 版本 1.3 中引入。 |
| "4 5 4" | 对 RGBA 值进行操作的 4×5 矩阵。 版本 1.3 中引入。 |
| "4 4 3" | 对 RGB 值进行操作的 4×4 矩阵。如果您使用此选项，矩阵的底端行应为 [0 0 0 1]。 只有当 ProcessList 元素的 version 属性为 "1.2" 时，此选项才有效。对于版本 1.3 及更高版本，请改用 "3 4 3"。 |

## 示例

## 对 RGB 值进行操作的 3×3 矩阵

```text
<ProcessList id="af6a6c73-aae9-4be6-8051-a796bc480b1c" version="1.2">
    <Matrix inBitDepth="32f" outBitDepth="32f">
        <Array dim="3 3 3">
 0.7841929793  0.0904410034  0.1253670007
 0.0445200019  1.0391299725 -0.0836500004
 0.0358299986 -0.3302420080  1.2944129705
        </Array>
    </Matrix>
</ProcessList>
```

## 对 RGB 值进行操作的 3×4 矩阵

```text
<ProcessList id="53d366de-e200-476f-b3fd-ed1ca7044197" version="1.3">
    <Matrix inBitDepth="32f" outBitDepth="10i">
        <Array dim="3 4 3">
499.99996948   0.00000000   0.00000000  94.99999237
  0.00000000 499.99996948   0.00000000  94.99999237
  0.00000000   0.00000000 499.99996948  94.99999237
        </Array>
    </Matrix>
 </ProcessList>
```

## 另请参见

- [Array (LUT1D)](../LUT1D/Array%20%28LUT1D%29.md)

- [Array (LUT3D)](../LUT3D/Array%20%28LUT3D%29.md)
