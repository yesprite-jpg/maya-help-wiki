# 挤出曲面选项(Extrude Surfaces Options)

使用以下选项可设置在选择“曲面 > 挤出”(Surfaces > Extrude)时发生的情况。

#### 样式(Style)

“平坦”(Flat)将在横截面沿挤出路径移动时保持其方向。

![图：“平坦”(Flat)将在横截面沿挤出路径移动时保持其方向。 “管”(Tube)将在引用向量保持与路径相切时沿路径扫描横截…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-FCD5BDF6-ACD2-40BC-8C81-1FA701F022D2.png) <!-- baize:img-hook downloaded=false reason="正文 2049 字 ≥300，非承重" -->

“管”(Tube)将在引用向量保持与路径相切时沿路径扫描横截面。

![图：“平坦”(Flat)将在横截面沿挤出路径移动时保持其方向。 “管”(Tube)将在引用向量保持与路径相切时沿路径扫描横截…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-ABC1872F-3AB5-4FF1-8B17-2B00123C5063.png) <!-- baize:img-hook downloaded=false reason="正文 2049 字 ≥300，非承重" -->

“距离”(Distance)将以直线形式挤出剖面。启用该选项时，请勿选择路径曲线。“距离”(Distance)启用时，该选项窗口将提供附加选项：“挤出长度”(Extrude Length)、“方向”(Direction)和“曲面次数”(Surface Degree)。

#### 挤出长度(Extrude Length)

指定挤出距离。

![图：指定挤出距离。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-CF9043E4-5028-437B-8409-5C055FA23E00.png) <!-- baize:img-hook downloaded=false reason="正文 2049 字 ≥300，非承重" -->

#### 方向(Direction)

“剖面法线”(Profile Normal)将路径的方向设定为剖面曲线的法线。如果剖面曲线不是平面曲线，则使用平均化法线。

![图：“剖面法线”(Profile Normal)将路径的方向设定为剖面曲线的法线。如果剖面曲线不是平面曲线，则使用平均化法线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-9DCB2124-6FEF-404F-9422-38FD1B5FF3F8.png) <!-- baize:img-hook downloaded=false reason="正文 2049 字 ≥300，非承重" -->

“指定”(Specify)支持您选择挤出的“方向向量”(Direction Vector)：“X 轴”(X Axis)、“Y 轴”(Y Axis)、“Z 轴”(Z Axis)或“自由”(Free)。例如，如果单击“Z 轴”(Z Axis)按钮，则挤出在 Z 轴方向为线性挤出。

如果选择“自由”，则可以在“X”、“Y”和“Z”框中输入值，以指定某个向量作为挤出的方向。

![图：“剖面法线”(Profile Normal)将路径的方向设定为剖面曲线的法线。如果剖面曲线不是平面曲线，则使用平均化法线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23DA44B3-DAC2-4E46-8B90-9A1250737948.png) <!-- baize:img-hook downloaded=false reason="正文 2049 字 ≥300，非承重" -->

#### 曲面次数(Surface Degree)

“线性”(Linear)为曲面提供等参线之间的锐化边。“立方”(Cubic)提供平滑边。

#### 结果位置(Result Position)

该选项仅在将“样式”(Style)设定为“平坦”(Flat)或“管”(Tube)时可用。

“在剖面处”(At Profile)在剖面曲线的位置处创建挤出曲面。

“在路径处”(At Path)将在路径曲线的位置创建挤出曲面。

#### 枢轴(Pivot)

“枢轴”(Pivot)选项仅在“样式”(Style)设定为“管”(Tube)时可用。如果选择“在路径处”(At Path)作为“结果位置”(Result Position)，则可选择剖面曲线，然后将其放置在挤出路径中的枢轴点上。

如果选择“最近结束点”(Closest End Point)，则使用与剖面曲线的边界框的中心最接近的路径端点。该端点将用作所有剖面曲线的枢轴点。如果正在执行多个挤出，则结果曲面将偏移该路径。

如果选择“组件”(Component)，则每条单独的剖面曲线的枢轴点将用于挤出剖面曲线。挤出将沿剖面曲线的组件出现。

![图：“枢轴”(Pivot)选项仅在“样式”(Style)设定为“管”(Tube)时可用。如果选择“在路径处”(At Path…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-7416CF1B-8E1F-4B5E-A7ED-1743C94CB793.png) <!-- baize:img-hook downloaded=false reason="正文 2049 字 ≥300，非承重" -->

![图：“枢轴”(Pivot)选项仅在“样式”(Style)设定为“管”(Tube)时可用。如果选择“在路径处”(At Path…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-9FDB85CE-6031-4BE1-B5B8-8691C62D3FF8.png) <!-- baize:img-hook downloaded=false reason="正文 2049 字 ≥300，非承重" -->

#### 方向(Orientation)

“方向”(Orientation)选项仅在“样式”(Style)设定为“管”(Tube)时可用。

如果选择“路径方向”(Path Direction)，则挤出的方向由路径曲线的方向设定。默认情况下，挤出的方向由“剖面法线”(Profile Normal)方向（即，剖面曲线的法线）设定。

## 方向示例

在下列示例中，“结果位置”(Result Position)已设定为“在剖面处”(At Profile)，“方向”(Orientation)已设定为“剖面法线”(Profile Normal)。移动并旋转路径曲线，使其与剖面曲线匹配。这是默认设置。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-0B1AE715-9B43-4815-8727-3E804F2F4BCA.png) <!-- baize:img-hook downloaded=false reason="正文 2049 字 ≥300，非承重" -->

在下列示例中，“结果位置”(Result Position)已设定为“在路径处”(At Path)，“方向”(Orientation)已设定为“路径方向”(Path Direction)。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-C03B6744-9A9B-42F4-A9B0-4C1A5295353E.png) <!-- baize:img-hook downloaded=false reason="正文 2049 字 ≥300，非承重" -->

在下列示例中，“结果位置”(Result Position)已设定为“在剖面处”(At Profile)，“方向”(Orientation)已设定为“剖面法线”(Profile Normal)。移动并旋转剖面曲线，使其与路径曲线匹配。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-258909AA-8C35-4C99-AC20-D64FE29D2852.png) <!-- baize:img-hook downloaded=false reason="正文 2049 字 ≥300，非承重" -->

#### 旋转(Rotation)

当剖面曲线沿路径曲线挤出时，旋转剖面曲线。较大的值将导致曲面偏离路径，特别是使用缩放时尤其如此。

#### 缩放(Scale)

当剖面曲线沿路径曲线挤出时，缩放剖面曲线。较大的值将导致曲面偏离路径，特别是使用旋转时尤其如此。

#### 曲线范围(Curve Range)

“完成”(Complete)将沿整个路径挤出整个剖面。

“部分”(Partial)将沿部分路径挤出部分剖面。如果启用构建历史，则该选项将创建一个能够编辑、以更改挤出曲面的“细分曲线”节点。请参见[使用操纵器编辑挤出的曲面](挤出曲面选项%28Extrude%20Surfaces%20Options%29.md#WS17956D7ADBC6E736-61417A49117AE32C705-7FD7)。

#### 输出几何体(Output Geometry)

指定创建的几何体类型。（“细分”意味着细分曲面。）

请注意，使用“剖面曲线”(Profile Curve)和“路径曲线”(Path Curve)框，可以访问输入曲线及其相关的统计信息。单击这些框旁边的箭头，可以选择输入曲线。单击该选项卡，可以为它们打开“属性编辑器”(Attribute Editors)。

## 使用操纵器编辑挤出的曲面

挤出曲面之后，请选择曲面，显示“通道盒”(Channel Box)，然后选择“显示操纵器工具”(Show Manipulator Tool)。单击“通道盒”(Channel Box)中的每个“细分”节点，可以显示各种可用的操纵器。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F2B7CE3D-9213-4B8F-A1A2-FF7EFF976296.png) <!-- baize:img-hook downloaded=false reason="正文 2049 字 ≥300，非承重" -->

使用操纵器查看其在曲面上的效果。这些操纵器支持您更改挤出的长度和扫描。

## 相关主题

- [沿路径曲线扫描剖面曲线](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-EF723AD0-6F96-4AD6-B859-F9F9EB0CB821.htm)
