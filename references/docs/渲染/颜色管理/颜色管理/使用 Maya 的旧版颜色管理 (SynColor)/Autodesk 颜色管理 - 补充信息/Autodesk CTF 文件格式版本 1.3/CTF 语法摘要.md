# CTF 语法摘要

以下是 CTF 文件语法的简要概述。

在下面的列表中，**?** 表示“0 或 1 个实例”，***** 表示“0 或多个实例”，**+** 表示“1 或多个实例”。如果未以其他方式标记，则需要元素的单个实例。

#### [ProcessList](ProcessList.md)

属性：id、name

包含：

##### [Info](元数据元素/Info.md) ?

包含：

###### [Copyright](元数据元素/Info/Copyright.md) ?

###### [Release](元数据元素/Info/Release.md) ?

##### [Description](元数据元素/Description.md) *

##### [InputDescriptor](元数据元素/InputDescriptor.md) ?

##### [OutputDescriptor](元数据元素/OutputDescriptor.md) ?

##### OperatorNode +

这是一个虚拟元素，使用下面的替换对象（LUT1D、LUT3D 等）之一进行替代。

属性：id、name、inBitDepth、outBitDepth、bypass

包含：

###### [Description](元数据元素/Description.md) *

###### [DynamicParameter](运算符元素/DynamicParameter.md) ?（对于 ExposureContrast，最多 3 个）

属性：param

使用以下选项之一替换每个 OperatorNode：

###### [LUT1D](运算符元素/LUT1D.md)

继承属性：id、name、inBitDepth、outBitDepth、bypass

属性：interpolation、halfDomain、rawHalfs

包含：

###### [Array](运算符元素/LUT1D/Array%20%28LUT1D%29.md)

属性：dim

###### [LUT3D](运算符元素/LUT3D.md)

继承属性：id、name、inBitDepth、outBitDepth、bypass

属性：interpolation

包含：

###### [Array](运算符元素/LUT3D/Array%20%28LUT3D%29.md)

属性：dim

###### [矩阵](运算符元素/Matrix.md)

继承属性：id、name、inBitDepth、outBitDepth、bypass

包含：

###### [Array](运算符元素/Matrix/Array（矩阵）.md)

属性：dim

###### [Range](运算符元素/Range.md)

继承属性：id、name、inBitDepth、outBitDepth、bypass

包含：

###### [minInValue](运算符元素/Range/minInValue.md) ?

###### [maxInValue](运算符元素/Range/maxInValue.md) ?

###### [minOutValue](运算符元素/Range/minOutValue.md) ?

###### [maxOutValue](运算符元素/Range/maxOutValue.md) ?

###### [Gamma](运算符元素/Gamma.md)

继承属性：id、name、inBitDepth、outBitDepth、bypass

属性：style

包含：

###### [GammaParams](运算符元素/Gamma/GammaParams.md)

属性：channel、gamma、offset

###### [ExposureContrast](运算符元素/ExposureContrast.md)

继承属性：id、name、inBitDepth、outBitDepth、bypass

包含：

###### [ECParams](运算符元素/ExposureContrast/ECParams.md)

属性：exposure、contrast、pivot

###### [日志(Log)](运算符元素/Log.md)

继承属性：id、name、inBitDepth、outBitDepth、bypass

属性：style

包含：

###### [LogParams](运算符元素/Log/LogParams.md) 1 或 3

属性：channel、gamma、refWhite、refBlack、highlight、shadow

###### [ASC_CDL](运算符元素/ASC_CDL.md)

继承属性：id、name、inBitDepth、outBitDepth、bypass

包含：

###### [SOPNode](运算符元素/ASC_CDL/SOPNode.md)

包含：

###### [坡度](运算符元素/ASC_CDL/SOPNode/Slope.md)

###### [偏移(Offset)](运算符元素/ASC_CDL/SOPNode/Offset.md)

###### [幂(Power)](运算符元素/ASC_CDL/SOPNode/Power.md)

###### [SatNode](运算符元素/ASC_CDL/SatNode.md)

包含：

###### [饱和度(Saturation)](运算符元素/ASC_CDL/SatNode/Saturation.md)

###### [引用(Reference)](运算符元素/Reference.md)

继承属性：id、name、inBitDepth、outBitDepth、bypass

属性：alias、path、basepath
