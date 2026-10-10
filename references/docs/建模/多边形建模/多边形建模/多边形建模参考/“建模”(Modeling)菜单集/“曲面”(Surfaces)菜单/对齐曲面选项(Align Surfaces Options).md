# 对齐曲面选项(Align Surfaces Options)

使用以下选项可设置在选择“曲面 > 对齐”(Surfaces > Align)时发生的情况。

#### 附加(Attach)

如果要附加曲面并对齐，请选择“附加”(Attach)。

#### 多点结(Multiple Knots)

接合对象时，会在“接合参数”(Join Parameter)中创建“多点结”(Multiple Knots)。选择“保持”(Keep)以保留这些结。

选择“移除”(Remove)，在执行附加操作时无需更改对象图形，就可以移除尽可能多的结。

#### 连续性(Continuity)

“连续性”(Continuity)是指两个曲面共享一个边界。通过“连续性”(Continuity)选项，可以指定如何实现两个曲面的连续性。

位置连续性是指两个曲面的终点恰好汇合。下图显示了如何使用每个“修改位置”(Modify Position)选项（“第一个”(First)、“第二个”(Second)和“二者”(Both)）对齐曲面的侧视图。出现的对齐具体取决于选择曲面的先后顺序（先选的为白色，后选的为绿色）。

![图：“连续性”(Continuity)是指两个曲面共享一个边界。通过“连续性”(Continuity)选项，可以指定如何实现…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-40CCD8C6-076B-4C57-BF0A-2B877AF92CE8.png) <!-- baize:img-hook downloaded=false reason="正文 2629 字 ≥300，非承重" -->

当两个曲面端对端连接且端点处的切线能够匹配时，存在“切线”(Tangent)连续性。对齐的曲面的示例侧视图如下所示：

![图：“连续性”(Continuity)是指两个曲面共享一个边界。通过“连续性”(Continuity)选项，可以指定如何实现…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-92A16D72-C13D-40DB-8986-F43D253727BA.png) <!-- baize:img-hook downloaded=false reason="正文 2629 字 ≥300，非承重" -->

当两个曲面满足切线连续性且在关节处具有相同的曲率时，存在“曲率”(Curvature)连续性。选中该选项时，曲率比例滑块将处于启用状态。

#### 修改位置(Modify Position)、修改边界(Modify Boundary)、修改切线(Modify Tangent)

可以选择修改曲面的顺序。下表显示了使用不同“修改”(Modify)选项时所修改的内容。

| 修改位置(Modify Position) | 曲面 |
|---|---|
| 第一个(First) 仅修改所选的第一个曲面的图形。 | 移动整个第一个曲面，使其结束边界与第二个曲面的开始边界重合。对第一个曲面的结束边界 CV 做出了一些调整。 |
| 第二个(Second) 仅修改所选的第二个曲面的图形。 | 移动整个第二个曲面，使其开始边界与第一个曲面的结束边界重合。对第二个曲面的开始边界 CV 做出了一些调整。 |
| 二者(Both) 同时修改所选的第一个和第二个曲面的图形。 | 移动整个第一个和第二个曲面，使第一个曲面的结束边界与第二个曲面的开始边界重合。相邻边界 CV 将沿着最短距离线向中间移动。 |

| 修改边界(Modify Boundary) | 曲面 |
|---|---|
| 第一个(First) 仅修改所选的第一个曲面的图形。 | 移动第一个曲面的所有结束边界 CV，使其与第二个曲面的相邻开始边界 CV 重合。 |
| 第二个(Second) 仅修改所选的第二个曲面的图形。 | 移动第二个曲面的所有开始边界 CV，使其与第一个曲面的相邻结束边界 CV 重合。 |
| 二者(Both) 同时修改所选的第一个和第二个曲面的图形。 | 移动第一个曲面的所有结束边界 CV 和第二个曲面的开始边界 CV，使它们互相重合。相邻 CV 将沿着最短距离线向中间移动。 |

| 修改切线(Modify Tangent) | 曲面 |
|---|---|
| 第一个(First) 仅修改所选的第一个曲面的图形。 | 调整第一个曲面的结束边界上的切线，使其与第二个曲面的开始边界上的切线重合。 |
| 第二个(Second) 仅修改所选的第二个曲面的图形。 | 调整第二个曲面的开始边界上的切线，使其与第一个曲面的结束边界上的切线重合。 |

**注**

“曲率”(Curvature)连续性会应用到修改后具有切线连续性的曲面（请参见上表）。

#### 切线比例(Tangent Scale)、曲率比例(Curvature Scale)

“切线比例”(Tangent Scale)和“曲率比例”(Curvature Scale)框中的值可以增加或减少曲面终点处的切线幅值或曲率。可以在该框中输入一个值或拖动滑块栏。下表显示了缩放切线和曲率时发生的情况。

| 切线比例(Tangent Scale) | 曲面 |
|---|---|
| 第一个(First) 仅缩放所选的第一个曲面的图形。 | 调整第一个曲面的结束边界上的切线幅值。 |
| 第二个(Second) 仅缩放所选的第二个曲面的图形。 | 调整第二个曲面的开始边界上的切线幅值。 |

| 曲率比例(Curvature Scale) | 曲面 |
|---|---|
| 第一个(First) 仅缩放所选的第一个曲面的图形。 | 调整第一个曲面的结束边界上的曲率。 |
| 第二个(Second) 仅缩放所选的第二个曲面的图形。 | 调整第二个曲面的开始边界上的曲率。 |

#### 保持原始(Keep Originals)

如果“保持原始”(Keep Originals)处于禁用状态，原始曲面将替换为已对齐的曲面。如果处于启用状态，则将创建两个新曲面，并保留原始曲面。

#### 输入曲面(Input Surface)

“输入曲面”(Input Surface)信息为只读信息。通过它，可以访问对齐的曲面的历史。单击箭头按钮，选择一个输入曲面并打开其编辑器区域。

#### 接合参数(Join Parameter)

“接合参数”(Join Parameter)滑块是否可用取决于所选的“位置连续性类型”(Positional Continuity Type)。使用“接合参数”(Join Parameter)可在执行对齐操作的第一个/第二个曲面上定义参数。

#### 反转/交换(Reverse/Swap)

曲面的“反转”(Reverse)和“交换”(Swap)选项定义曲面在执行对齐操作之前是否必须进行反转和/或交换（请记住，对齐使用第一个曲面的终点和第二个曲面的起点）。反转是沿着“通道盒”(Channel Box)中的“方向 U”(Direction U)（无论启用还是禁用）定义的方向来执行。

#### 扭曲(Twist)

如果“扭曲”(Twist)处于启用状态，则第二个曲面也会沿着“方向 U”(Direction U)的反方向进行反转。如果对齐的曲面已扭曲，请启用该选项。

例如，如果对齐曲面并且曲面边界是沿着不同的方向伸展，将导致以下结果。

![图：如果“扭曲”(Twist)处于启用状态，则第二个曲面也会沿着“方向 U”(Direction U)的反方向进行反转。如果…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4BDCE101-4E9F-4CDF-8E74-F507CE92252B.png) <!-- baize:img-hook downloaded=false reason="正文 2629 字 ≥300，非承重" -->

选择曲面后，对齐结果将呈扭曲状态。从“属性编辑器”(Attribute Editor)中或在“通道盒”(Channel Box)中启用“扭曲”(Twist)可解决该问题。

![图：如果“扭曲”(Twist)处于启用状态，则第二个曲面也会沿着“方向 U”(Direction U)的反方向进行反转。如果…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F23741A0-5EBC-4002-A529-019FA5B00F05.png) <!-- baize:img-hook downloaded=false reason="正文 2629 字 ≥300，非承重" -->

另一种替代方法是，在对齐曲面之前检查曲面的 U/V 方向。使用“曲面 > 反转方向”(Surfaces > Reverse Direction)来反转曲面方向（如有必要）。

![图：如果“扭曲”(Twist)处于启用状态，则第二个曲面也会沿着“方向 U”(Direction U)的反方向进行反转。如果…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-30E5F86F-0CF3-4AD5-9DB8-AD8675CBB2AC.png) <!-- baize:img-hook downloaded=false reason="正文 2629 字 ≥300，非承重" -->

**注**

“对齐曲面”(Align Surfaces)会计算各条边的扭曲值，因此无需在对齐曲面后，再启用扭曲属性以获取纯接合。

#### 内部融合(Interior Blending)

“内部融合”(Interior Blending)区域与选项窗口中的“切线比例”(Tangent Scale)选项相同。滑块是否可用取决于所选的连续性类型。

## 相关主题

- [对齐曲面边](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-A0AD44A6-E7E0-42D0-ACFD-AF83DAC6B5EC.htm)
