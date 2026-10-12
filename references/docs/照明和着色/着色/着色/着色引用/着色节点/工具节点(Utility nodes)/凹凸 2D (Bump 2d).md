# 凹凸 2D (Bump 2d)

将 2D 纹理转化为凹凸贴图。请参见[使用凹凸 2D 工具](../../../渲染节点工具/使用“凹凸%202D”%28Bump%202d%29工具.md)。

#### 凹凸值(Bump Value)

用于凹凸贴图的源 2D 纹理。可以将任何着色网络的输出连接到“凹凸值”(Bump Value)用作凹凸源。

#### 凹凸深度(Bump Depth)

控制显示在曲面上的凹凸的高度。增加“凹凸深度”(Bump Depth)会使曲面更加不平。减小“凹凸深度”(Bump Depth)会使曲面更加平滑。

![图：控制显示在曲面上的凹凸的高度。增加“凹凸深度”(Bump Depth)会使曲面更加不平。减小“凹凸深度”(Bump De…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-E8C458A6-1FB7-4EA3-89C0-04D909556F74.png) <!-- baize:img-hook downloaded=false reason="正文 923 字 ≥300，非承重" -->

通过调整“凹凸深度”(Bump Depth)或纹理的“Alpha 增益”(Alpha Gain)和“Alpha 偏移”(Alpha Offset)，您几乎可以实现相同效果。通过读取纹理的 Alpha 增益值确定“凹凸深度”(Bump Depth)。这两种控制对可能存在多个凹凸的复杂着色网络都很有用。通过 Alpha 增益属性，您可以单独调整每个纹理的凹凸。

#### 凹凸过滤器(Bump Filter)

影响用作凹凸贴图的纹理上执行的过滤级别。Maya 根据最终图像中纹理所占用的屏幕空间大小计算过滤量。“凹凸过滤器”(Bump Filter)属性是该值的倍增。

大于 1.0 的值将生成更多的过滤，使凹凸更为平滑。如果最终渲染中出现锯齿（锯齿状楼梯效果），或者凹凸贴图在几个帧的过程中突然出现或“闪现”，则增大该值。

值小于 1.0 将生成更少的过滤，使凹凸显得更明晰。如果最终渲染图像中凹凸过于平滑，则减小该值。

#### 凹凸过滤器偏移(Bump Filter Offset)

影响纹理上执行的过滤量。

不同于“凹凸过滤器”(Bump Filter)属性（倍增），Maya 将“凹凸过滤器偏移”(Bump Filter Offset)添加到计算的过滤值。这将均匀增加过滤量。

该属性可以用于锁定 Maya 的过滤值。如果希望“凹凸过滤器偏移”(Bump Filter Offset)值完全确定过滤量，请将“凹凸过滤器”(Bump Filter)属性设定为 0。

#### 调整边(Adjust Edges)

如果在 place2dTexture 的“U 向折回”(Wrap U)和“V 向折回”(Wrap V)属性禁用时映射纹理，纹理边界可能出现瑕疵。出现这种情况时，使用“调整边”(Adjust Edges)可以移除这些瑕疵，但此方法在“U 向折回”(Wrap U)和“V 向折回”(Wrap V)属性启用时无效果。
