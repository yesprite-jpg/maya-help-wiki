# 延伸曲面上的曲线选项(Extend Curve on Surface Options)

使用以下选项可设置在选择“曲线 > 延伸 > 延伸曲面上的曲线”(Curves > Extend > Extend Curve on Surface)时发生的情况。

**注**

延伸曲面上的曲线可能会在编辑延伸距离时出现暂时减慢 Maya。计算的时间可能比预期要长。

### 延伸方法(Extend Method)

指定如何延伸曲面的 UV 空间中的曲线：

#### 参数化距离(Parametric Distance)

以直线方式“线性”(Linear)延伸曲线。

沿圆弧方向“圆形”(Circular)延伸曲线。

“外推”(Extrapolate)将通过推断曲线的方向和切线延伸曲线。

“参数化距离”(Parametric Distance)值指定延伸线的长度。该值将指定曲线延伸方向上曲面长度的百分比。例如，值为 0.5 表示将曲线的长度在曲线延伸方向延伸大约曲面长度的一半。

#### UV 点(UV Point)

允许您在“UV 点将延伸至”(UV Point To Extend To)条目框中指定延伸位置。若要使用实际的 UV 值而不是估算，请选择创建 > 测量工具 > 参数工具(Create > Measure Tools > Parameter Tool)，在曲面上拖动，然后释放鼠标按钮在指针处显示 UV 坐标。

## 相关主题

- [延伸曲线](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-08E73E34-DEAE-4E5B-98DA-CFB4560C06E8.htm)
