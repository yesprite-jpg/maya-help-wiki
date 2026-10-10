# blendColorSets

在任何时候合并或融合两种颜色集时都会创建 blendColorSets 节点。可以从“通道盒”(Channel Box)或“属性编辑器”(Attribute Editor)访问该节点。

### 融合样式(Blend Style)

设定用于组合选定颜色集的融合类型。

#### Alpha 融合(Alpha Blend)

请参见[覆盖(Over)](../多边形建模编辑器/颜色集编辑器%28Color%20Set%20Editor%29.md#GUID-D66DA4E9-57C9-46D8-9D9E-9BDA453E455D__GUID-67A8E4EC-D22E-4696-9617-EDFE3475B540)。

#### 相乘(Multiply)

请参见[相乘](../多边形建模编辑器/颜色集编辑器%28Color%20Set%20Editor%29.md#GUID-D66DA4E9-57C9-46D8-9D9E-9BDA453E455D__GUID-3C0CCD4F-ADC3-47A5-ACF7-9A43C4AE1B67)。

#### 相加(Add)

请参见[相加(Add)](../多边形建模编辑器/颜色集编辑器%28Color%20Set%20Editor%29.md#GUID-D66DA4E9-57C9-46D8-9D9E-9BDA453E455D__GUID-423F5D80-DD26-42E1-A07C-58A54810A6D5)。

#### 相减(Subtract)

请参见[相减](../多边形建模编辑器/颜色集编辑器%28Color%20Set%20Editor%29.md#GUID-D66DA4E9-57C9-46D8-9D9E-9BDA453E455D__GUID-C162BE81-0A82-41A2-879D-8C4CCF1CDFF9)。

#### 线性融合(Linear Blend)

请参见[线性](../多边形建模编辑器/颜色集编辑器%28Color%20Set%20Editor%29.md#GUID-D66DA4E9-57C9-46D8-9D9E-9BDA453E455D__GUID-89AC4BFF-0CBD-42D9-A4BE-ACD56276005D)。

#### 双线性融合(Bilinear Blend)

请参见[双线性](../多边形建模编辑器/颜色集编辑器%28Color%20Set%20Editor%29.md#GUID-D66DA4E9-57C9-46D8-9D9E-9BDA453E455D__GUID-234595B0-F5A6-43A9-8356-E7185E35E923)。

#### 颜色通道(Color Channel)

请参见[通道](../多边形建模编辑器/颜色集编辑器%28Color%20Set%20Editor%29.md#GUID-D66DA4E9-57C9-46D8-9D9E-9BDA453E455D__GUID-107682F1-BCF6-45C7-8CDD-0141DDE28ECF)。

#### 主(红)权重(Primary (Red) Weight)

为选定融合颜色集设定主权重值。对于“线性”(Linear)融合，这将仅设定融合颜色集的权重值。对于“双线性”(Bilinear)融合，这将设定融合颜色集的源权重值。对于“颜色通道”(ColorChannel)融合，这将设定融合颜色集的“红色”(Red)通道权重。

#### 次(绿)权重(Secondary (Green) Weight)

为选定融合颜色集设定次权重值。对于“双线性”(Bilinear)融合，这将设定融合颜色集的基础权重值。对于“颜色通道”(ColorChannel)融合，这将设定融合颜色集的“绿色”(Green)通道权重。

#### 蓝色权重(Blue Weight)

设定选定“颜色通道”(ColorChannel)融合颜色集的“蓝色”(Blue)通道权重。

#### Alpha 权重(Alpha Weight)

设定选定融合颜色集的 Alpha 通道权重值。

#### 基础颜色集(Base Color Set)

参与融合的第二种选定颜色集。

#### 融合颜色集

参与融合的第一种选定颜色集。

#### 目标颜色集

融合颜色集的名称。

#### 交换基础集和融合集(Swap Base and Blend Sets)

交换选定融合颜色集的源色彩（“融合颜色集”(Blend Color Set)）和基础颜色（“基础颜色集”(Base Color Set)）。“交换基础集和融合集”(Swap Base and Blend Sets)可能会更改融合结果，这取决于当前融合模式。
