# LUT3D

LUT3D 元素指定要应用的 3D LUT。

## 包含

- [Description](../元数据元素/Description.md)。可选，任意数量。

- [Array (LUT3D)](LUT3D/Array%20%28LUT3D%29.md)。必需，仅一个。

- [DynamicParameter](DynamicParameter.md)。可选，至多一个。param 属性必须设置为 "DEFAULT_LOOK"。

**注**

IndexMap 元素不受支持。获得相同结果的最有效方法是在运算符之前使用 LUT1D 元素。

## 包含于

- [ProcessList](../ProcessList.md)

## 属性

#### id、name、bypass、inBitDepth、outBitDepth

请参见[通用运算符属性](通用运算符属性.md)。

#### interpolation

支持的值包括 "trilinear" 和 "tetrahedral"。

此属性是可选的。如果未指定，则默认值为 "trilinear"。

## 示例

```text
<ProcessList id="b5b90615-573b-4959-a838-f35e0e588ac2" version="1.2">
    <LUT3D inBitDepth="32f" interpolation="tetrahedral" outBitDepth="32f">
        <Array dim="48 48 48 3">
 0.000669299  0.000704187  0.000766901
 0.001848371  0.001297010  0.010368987
 0.002599007  0.001144927  0.023227118
<!-- 48*48*48-3 lines omitted -->

        </Array>
    </LUT3D>
</ProcessList>
```
