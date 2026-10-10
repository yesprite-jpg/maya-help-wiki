# LogParams

LogParams 元素定义 Log 元素使用的参数值。

它是 Academy/ASC XML 颜色变换格式的 Autodesk 扩展。

## 引入

版本 1.3。

## 包含

无内容。

## 包含于

[日志(Log)](../Log.md)

## 属性

#### channel

指定要应用参数值的通道。可能的值包括 "R"、"G" 和 "B"。

可选。如果省略，则值将应用于每个 RGB 通道。

#### gamma

合并胶片和视频 Gamma（对数空间中的对比度）。典型值为 0.6。

#### refWhite

对数空间中映射到线性空间中 highlight 的值。以 10 位比例指定（例如，685 为典型值）。

#### refBlack

对数空间中映射到线性空间中 shadow 的值。以 10 位比例指定（例如，95 为典型值）。

#### highlight

线性空间中映射到对数空间中 refWhite 的值。以浮点比例指定（例如，1.0 为典型值）。请注意，大于 refWhite 的对数值不会被钳制，并将映射到大于线性空间中 highlight 的值。

#### shadow

线性空间中映射到对数空间中 refBlack 的值。以浮点比例指定（例如，0.0 为典型值）。请注意，小于 refBlack 的对数值不会被钳制，并将映射到小于线性空间中 shadow 的值（甚至可能是负值）。

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
