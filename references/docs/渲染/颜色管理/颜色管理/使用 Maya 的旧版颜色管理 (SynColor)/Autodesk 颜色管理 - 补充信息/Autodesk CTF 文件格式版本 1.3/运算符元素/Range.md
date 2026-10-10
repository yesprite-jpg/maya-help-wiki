# Range

Range 元素通过缩放值和偏移值将输入域映射到输出范围。

如果 minInValue 存在，则 minOutValue 也必须存在，并且结果将钳制在低端。同样，如果 maxInValue 存在，则 maxOutValue 也必须存在，并且结果将钳制在高端。如果 minInValue、minOutValue、maxInValue 或 maxOutValue 都不存在，Range 运算符将仅执行位深度转化。

minInValue 和 maxInValue 的缩放取决于输入位深度，minOutValue 和 maxOutValue 的缩放取决于输出位深度。

如果指定了最小值和最大值，则 Range 的公式为：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-EEB00871-4C59-4BE9-AF65-3FD7D5729FA7.png) <!-- baize:img-hook downloaded=false reason="正文 949 字 ≥300，非承重" -->

如果仅指定了最小值，则公式为：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-0B7CC148-899D-4624-B4F6-8289160E9874.png) <!-- baize:img-hook downloaded=false reason="正文 949 字 ≥300，非承重" -->

如果仅指定了最大值，则公式为：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-921266E0-548D-4987-8FEA-14E79AAC3F46.png) <!-- baize:img-hook downloaded=false reason="正文 949 字 ≥300，非承重" -->

其中：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-DF049D37-0007-4D7F-83FA-3F7FD8F402F2.png) <!-- baize:img-hook downloaded=false reason="正文 949 字 ≥300，非承重" -->

## 包含

- [Description](../元数据元素/Description.md)。可选，任意数量。

- [minInValue](Range/minInValue.md)。可选，至多一个。

- [minOutValue](Range/minOutValue.md)。可选，至多一个。

- [maxInValue](Range/maxInValue.md)。可选，至多一个。

- [maxOutValue](Range/maxOutValue.md)。可选，至多一个。

- [DynamicParameter](DynamicParameter.md)。可选，至多一个。param 属性必须设置为 "DEFAULT_LOOK"。

## 包含于

- [ProcessList](../ProcessList.md)

## 属性

#### id、name、bypass、inBitDepth、outBitDepth

请参见[通用运算符属性](通用运算符属性.md)。

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
