# 旋转选项(Revolve Options)

使用以下选项可设置在选择“曲面 > 旋转”(Surfaces > Revolve)时发生的情况。

#### 轴预设(Axis Preset)

指定旋转轴。默认设置为 Y。下图使用透视视图中的每个旋转轴来旋转剖面曲线（在前视图中绘制）。

![图：指定旋转轴。默认设置为 Y。下图使用透视视图中的每个旋转轴来旋转剖面曲线（在前视图中绘制）。 如果将“轴预设”(Axis…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-8831E437-D9CE-4146-9337-F01A0170AB2E.png) <!-- baize:img-hook downloaded=false reason="正文 1905 字 ≥300，非承重" -->

![图：指定旋转轴。默认设置为 Y。下图使用透视视图中的每个旋转轴来旋转剖面曲线（在前视图中绘制）。 如果将“轴预设”(Axis…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-7723B629-66BF-46CD-8898-D14488AE5A3A.png) <!-- baize:img-hook downloaded=false reason="正文 1905 字 ≥300，非承重" -->

如果将“轴预设”(Axis Preset)设定为“自由”(Free)，可以在“轴 X”(Axis X)、“轴 Y”(Axis Y)或“轴 Z”(Axis Z)框中输入值，以指定剖面曲线的旋转轴。下图是“轴 X”(Axis X)、“轴 Y”(Axis Y)和“轴 Z”(Axis Z)的值为 1 时生成的曲面。

![图：指定旋转轴。默认设置为 Y。下图使用透视视图中的每个旋转轴来旋转剖面曲线（在前视图中绘制）。 如果将“轴预设”(Axis…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-697DF403-00AD-4127-A7A1-161C4EDA3F99.png) <!-- baize:img-hook downloaded=false reason="正文 1905 字 ≥300，非承重" -->

#### 枢轴(Pivot)

如果将“枢轴”(Pivot)设定为“对象”(Object)，则从默认枢轴位置 (0, 0, 0) 执行旋转。这是默认设置。

如果选择“预设”(Preset)，可以在“枢轴点”(Pivot Point)框中输入值以更改枢轴点的 X、Y 或 Z 位置。

下图显示了如何在使用默认枢轴值以及 X、Y、Z 值为 5 时创建旋转曲面。

![图：如果将“枢轴”(Pivot)设定为“对象”(Object)，则从默认枢轴位置 (0, 0, 0) 执行旋转。这是默认设置…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-2AF97928-4E47-4280-BA82-86F3B1A8D28B.png) <!-- baize:img-hook downloaded=false reason="正文 1905 字 ≥300，非承重" -->

#### 曲面次数(Surface Degree)

“曲面次数”(Surface Degree)选项决定了是否使用线性（次数为 1）或立方（次数为 3）几何体创建曲面的 V 参数方向。

如果选择“线性”(Linear)，曲面将由周围的平面构建。

如果选择“立方”(Cubic)，平滑剖面将由原始剖面曲线定义。这是默认设置。

![图：“曲面次数”(Surface Degree)选项决定了是否使用线性（次数为 1）或立方（次数为 3）几何体创建曲面的 V…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-04704493-DF74-4980-BA39-C88AE387D541.png) <!-- baize:img-hook downloaded=false reason="正文 1905 字 ≥300，非承重" -->

#### 开始和结束扫描角度(Start and End Sweep Angle)

使用“开始扫描角度”(Start Sweep Angle)和“结束扫描角度”(End Sweep Angle)值指定旋转角度（以度为单位）。默认值为 360，有效范围为 0 到 360。

#### 使用容差(Use Tolerance)

“使用容差”(Use Tolerance)选项控制生成旋转曲面的精度。可以全局或局部应用容差。

如果选择“无”(None)，可以更改分段值。

如果选择“全局”(Global)容差，Maya 将使用“首选项”(Preferences)窗口的“设置”(Settings)区域中的“位置”(Positional)和“切向”(Tangential)值。

如果选择“局部”(Local)容差，可以直接输入一个新值来覆盖“首选项”(Preferences)窗口的“位置”(Positional)容差。这样可以创建更接近于实际旋转曲面的旋转曲面。

#### 分段(Segments)

“分段”(Segments)值决定了创建旋转曲面使用的截面数量。对于 360 度扫描，六个或八个截面通常已经足够。在下图中，左侧曲面显示了使用八个分段的旋转。右侧则包含 20 个分段。

![图：“分段”(Segments)值决定了创建旋转曲面使用的截面数量。对于 360 度扫描，六个或八个截面通常已经足够。在下图…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-FFF0D4CD-84EB-4441-9791-630EC386E4B1.png) <!-- baize:img-hook downloaded=false reason="正文 1905 字 ≥300，非承重" -->

如果“使用容差”(Use Tolerance)未被设定为“无”(None)，则会自动计算“分段”(Segments)值，以便结果与默认旋转曲面的差别小于指定容差值。

如果“局部”(Local)被设定为“使用容差”(Use Tolerance)选项，旋转曲面的容差值将更接近于实际旋转曲面。

![图：“分段”(Segments)值决定了创建旋转曲面使用的截面数量。对于 360 度扫描，六个或八个截面通常已经足够。在下图…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-A31DAB19-18ED-484E-9150-29FDB76B7B92.png) <!-- baize:img-hook downloaded=false reason="正文 1905 字 ≥300，非承重" -->

**注**

提示：

如果要设置扫描角度的动画，则更改“分段”(Segments)值而不是容差值，才能更改曲面的 CV 数量。

#### 曲线范围(Curve Range)

选择“完整”(Complete)作为“曲线范围”(Curve Range)，沿整个剖面曲线创建旋转曲面。这是默认设置。

如果希望在旋转时使用曲线分段，则选择“部分”(Partial)。

如果在创建旋转曲面之前将“曲线范围”(Curve Range)设定为“部分”(Partial)，就会创建“subCurve”。通过减少“subCurve”的长度，可以减少旋转曲面的长度。

若要编辑“细分曲线”(subCurve)的长度，选择旋转曲面，在“通道盒”(Channel Box)中选择“细分曲线”(subCurve)，选择“显示操纵器工具”(Show Manipulator Tool)，然后拖动曲线分段操纵器或在“通道盒”(Channel Box)中编辑“最小值”和“最大值”(Max Value)。

![图：选择“完整”(Complete)作为“曲线范围”(Curve Range)，沿整个剖面曲线创建旋转曲面。这是默认设置。 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-5E6850CC-694C-4CEE-A129-EE5DDE9B656D.png) <!-- baize:img-hook downloaded=false reason="正文 1905 字 ≥300，非承重" -->

有关编辑“subCurve”的详细信息，请参见[编辑 subCurve 属性](旋转选项%28Revolve%20Options%29.md#WS17956D7ADBC6E736-61417A49117AE32C705-7FDB)。

#### 输出几何体(Output Geometry)

指定创建的几何体类型。（“细分”表示“细分曲面”(Subdiv)。）

#### 输入曲线(Input Curve)

“输入曲线”(Input Curve)信息为只读类型。它用于访问创建旋转曲面时使用的曲线历史。

### 编辑“subCurve”属性

如果在创建旋转时，在选项窗口中将“曲线范围”(Curve Range)设定为“部分”(Partial)，则可以编辑曲线长度。选择旋转曲面，然后使用“显示操纵器工具”(Show Manipulator tool)或“通道盒”(Channel Box)编辑“subCurve”属性。

## 相关主题

- [使用旋转创建曲面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-2F7560AF-7A95-49B0-B5BC-7D48B696B414.htm)
