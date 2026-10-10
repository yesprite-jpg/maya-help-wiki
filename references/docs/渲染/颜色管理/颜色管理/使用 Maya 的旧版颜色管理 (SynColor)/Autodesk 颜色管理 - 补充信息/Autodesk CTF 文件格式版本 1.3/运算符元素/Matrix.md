# Matrix

Matrix 元素为颜色值相乘指定一个矩阵，也可以选择应用偏移。

## 包含

- [Description](../元数据元素/Description.md)。可选，任意数量。

- [Array (Matrix)](Matrix/Array（矩阵）.md)。必需，仅一个。

- [DynamicParameter](DynamicParameter.md)。可选，至多一个。param 属性必须设置为 "DEFAULT_LOOK"。

## 包含于

- [ProcessList](../ProcessList.md)

## 属性

#### id、name、bypass、inBitDepth、outBitDepth

请参见[通用运算符属性](通用运算符属性.md)。

## 示例

### 3x3 矩阵

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

### 4x4 矩阵

```text
<ProcessList id="d6783d48-dd96-4c71-99af-f3be0cc9392e" version="1.2">
    <Matrix inBitDepth="32f" outBitDepth="10i">
        <Array dim="4 4 3">
499.99996948   0.00000000   0.00000000  94.99999237
  0.00000000 499.99996948   0.00000000  94.99999237
  0.00000000   0.00000000 499.99996948  94.99999237
  0.00000000   0.00000000   0.00000000   1.00000000
        </Array>
    </Matrix>
 </ProcessList>
```
